from __future__ import annotations

import difflib
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

from agency import agent, agdata, agteam
from agency.agconfig import agConfig
from agency.agllm import agLLMConfig
from agency.agllm_backends import agVLLMBackendConfig
from agency.agsandbox import agSandboxConfig
from agency.common_skills import agbuild, agplan
from agency.profiler import agprof

QUIXBUGS_URL = "https://github.com/jkoppel/QuixBugs.git"
DEFAULT_MANIFEST = Path(__file__).with_name("tasks.json")
MAX_TEST_OUTPUT = 20_000
PRIVATE_ENV_FILE = Path.home() / ".config" / "agency-capstone" / "env"
SAFE_TASK_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")
IGNORED_WORKSPACE_PARTS = {".pytest_cache", "__pycache__"}


@dataclass(frozen=True)
class RepairTask:
    name: str
    program: str
    test: str
    category: str
    expected_baseline: str = "failure"
    baseline_timeout_s: int = 10

    @property
    def test_command(self) -> str:
        return f"python -m pytest -q {self.test}"


class OfflinePlanSkill(agplan):
    """An agplan variant that cannot reach the web or mutate the sandbox."""

    def _build_toolkit(
        self,
        agent_sandbox,
        resource_pool,
        agent_terminal,
        agent_log,
        _ensure_read: bool = False,
        agconfig=None,
    ):
        from agency.tools import make_glob, make_grep, make_read

        original = self.replace_tools
        self.replace_tools = [
            make_read(agent_sandbox),
            make_grep(agent_sandbox),
            make_glob(agent_sandbox),
        ]
        try:
            return super()._build_toolkit(
                agent_sandbox,
                resource_pool,
                agent_terminal,
                agent_log,
                _ensure_read=_ensure_read,
                agconfig=agconfig,
            )
        finally:
            self.replace_tools = original


class OfflineBuildSkill(agbuild):
    """An agbuild variant that retains local tools but cannot fetch answers."""

    def _build_toolkit(
        self,
        agent_sandbox,
        resource_pool,
        agent_terminal,
        agent_log,
        _ensure_read: bool = False,
        agconfig=None,
    ):
        from agency.tools import make_sandboxed_tools

        tools = make_sandboxed_tools(agent_sandbox, resource_pool)
        original = self.replace_tools
        self.replace_tools = [tool for tool in tools if tool.name not in {"webfetch", "ask_human"}]
        try:
            return super()._build_toolkit(
                agent_sandbox,
                resource_pool,
                agent_terminal,
                agent_log,
                _ensure_read=_ensure_read,
                agconfig=agconfig,
            )
        finally:
            self.replace_tools = original


def load_private_environment(path: Path = PRIVATE_ENV_FILE) -> bool:
    """Restore endpoint settings after agprof's privileged cgroup re-exec."""
    if not path.is_file():
        return False
    allowed = {"LLM_BASE_URL", "LLM_MODEL", "LLM_API_KEY", "AGENCY_CAPSTONE_IMAGE"}
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line.removeprefix("export ")
        key, separator, encoded = line.partition("=")
        if separator and key in allowed:
            parsed = shlex.split(encoded)
            if len(parsed) != 1:
                raise ValueError(f"invalid private environment value for {key}")
            os.environ.setdefault(key, parsed[0])
    return True


def load_manifest(path: Path = DEFAULT_MANIFEST) -> tuple[str, list[RepairTask]]:
    document = json.loads(path.read_text())
    revision = document.get("revision", "")
    if len(revision) != 40 or any(c not in "0123456789abcdef" for c in revision):
        raise ValueError("manifest revision must be a full lowercase Git commit SHA")

    tasks = [RepairTask(**item) for item in document.get("tasks", [])]
    if not tasks:
        raise ValueError("manifest must contain at least one task")
    if len({task.name for task in tasks}) != len(tasks):
        raise ValueError("task names must be unique")
    for task in tasks:
        if not SAFE_TASK_NAME.fullmatch(task.name):
            raise ValueError(f"task name must be a safe path component: {task.name!r}")
        if task.expected_baseline not in {"failure", "timeout"}:
            raise ValueError(
                f"task {task.name!r} has invalid expected baseline: {task.expected_baseline!r}"
            )
        if task.baseline_timeout_s < 1:
            raise ValueError(f"task {task.name!r} baseline timeout must be positive")
        for relative in (task.program, task.test):
            candidate = Path(relative)
            if candidate.is_absolute() or ".." in candidate.parts:
                raise ValueError(f"task {task.name!r} contains an unsafe path: {relative!r}")
    return revision, tasks


def ensure_benchmark(cache_dir: Path, revision: str) -> Path:
    checkout = cache_dir / "QuixBugs"
    cache_dir.mkdir(parents=True, exist_ok=True)
    if not checkout.exists():
        subprocess.run(
            ["git", "clone", "--filter=blob:none", QUIXBUGS_URL, str(checkout)],
            check=True,
        )
    subprocess.run(["git", "-C", str(checkout), "fetch", "--quiet", "origin", revision], check=True)
    subprocess.run(
        ["git", "-C", str(checkout), "checkout", "--quiet", "--detach", revision], check=True
    )
    actual = subprocess.run(
        ["git", "-C", str(checkout), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    if actual != revision:
        raise RuntimeError(f"QuixBugs checkout mismatch: expected {revision}, got {actual}")
    return checkout


def prepare_workspace(source: Path, destination: Path, task: RepairTask) -> Path:
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(source, destination, ignore=shutil.ignore_patterns(".git"))

    # Correct implementations would leak the answer to the repair agent.
    for hidden in ("correct_python_programs", "java_programs"):
        shutil.rmtree(destination / hidden, ignore_errors=True)

    if not (destination / task.program).is_file():
        raise FileNotFoundError(f"missing benchmark program: {task.program}")
    if not (destination / task.test).is_file():
        raise FileNotFoundError(f"missing benchmark test: {task.test}")
    return destination


def snapshot_protected_files(workspace: Path, task: RepairTask) -> dict[str, bytes]:
    """Snapshot every benchmark file except the one program the agent may edit."""
    snapshot: dict[str, bytes] = {}
    for path in workspace.rglob("*"):
        relative = path.relative_to(workspace)
        if (
            relative.as_posix() == task.program
            or any(part in IGNORED_WORKSPACE_PARTS for part in relative.parts)
            or path.suffix == ".pyc"
        ):
            continue
        if path.is_symlink():
            snapshot[relative.as_posix()] = b"SYMLINK\0" + os.readlink(path).encode()
        elif path.is_file():
            snapshot[relative.as_posix()] = path.read_bytes()
    return snapshot


def restore_protected_files(
    workspace: Path, task: RepairTask, original: dict[str, bytes]
) -> list[str]:
    """Restore immutable benchmark inputs and report every attempted modification."""
    current = snapshot_protected_files(workspace, task)
    changed = sorted(
        path for path in set(original) | set(current) if original.get(path) != current.get(path)
    )
    for relative in set(current) - set(original):
        path = workspace / relative
        if path.is_file() or path.is_symlink():
            path.unlink()
    for relative, content in original.items():
        if current.get(relative) == content:
            continue
        path = workspace / relative
        if path.is_symlink():
            path.unlink()
        path.parent.mkdir(parents=True, exist_ok=True)
        if content.startswith(b"SYMLINK\0"):
            path.symlink_to(content.removeprefix(b"SYMLINK\0").decode())
        else:
            path.write_bytes(content)
    return changed


def run_test(workspace: Path, task: RepairTask, timeout: int = 120) -> dict:
    started = time.perf_counter()
    try:
        completed = subprocess.run(
            [sys.executable, "-m", "pytest", "-q", task.test],
            cwd=workspace,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        output = (completed.stdout + completed.stderr)[-MAX_TEST_OUTPUT:]
        return {
            "passed": completed.returncode == 0,
            "returncode": completed.returncode,
            "duration_s": time.perf_counter() - started,
            "output": output,
        }
    except subprocess.TimeoutExpired as error:
        captured = f"{error.stdout or ''}{error.stderr or ''}"[-MAX_TEST_OUTPUT:]
        return {
            "passed": False,
            "returncode": None,
            "duration_s": time.perf_counter() - started,
            "output": f"TIMEOUT after {timeout}s\n{captured}",
        }


def make_config(workspace: Path) -> agConfig:
    llm = agVLLMBackendConfig(
        base_url=os.environ.get("LLM_BASE_URL"),
        model=os.environ.get("LLM_MODEL", ""),
        api_key=os.environ.get("LLM_API_KEY", ""),
        temperature=0.0,
        top_p=1.0,
    )
    sandbox = (
        agSandboxConfig()
        .set_base_image(os.environ.get("AGENCY_CAPSTONE_IMAGE", "agency-capstone:latest"))
        .set_network_mode("none")
        .add_mount("quixbugs", workspace, "/workspace", "rw")
    )
    llm_runtime = agLLMConfig(
        max_retries=3,
        idle_timeout=180.0,
        stream_timeout=300.0,
    )
    return agConfig(llm, llm_runtime, sandbox)


class RepairTeam(agteam):
    """Diagnose and repair one QuixBugs task in an isolated mounted checkout."""

    def setup(self) -> None:
        self.planner = OfflinePlanSkill(
            name="diagnose_bug",
            system_prompt=(
                "Diagnose exactly one QuixBugs Python defect. Work only in /workspace. "
                "Read the target program and its tests, explain the root cause, and propose "
                "a minimal repair. Do not inspect similarly named external projects or seek "
                "reference/correct implementations."
            ),
            input_schema=agdata(
                task_name=str,
                program_path=str,
                test_path=str,
                baseline_failure=str,
            ),
            output_schema=agdata(plan=str),
        )
        self.builder = OfflineBuildSkill(
            name="repair_bug",
            system_prompt=(
                "Implement a minimal repair for the diagnosed QuixBugs defect in /workspace. "
                "Modify only the target Python program. Run the supplied pytest command and do "
                "not weaken, skip, delete, or otherwise alter tests or harness files. The "
                "sandbox has no network access; do not search for a reference implementation."
            ),
            input_schema=agdata(
                task_name=str,
                program_path=str,
                test_command=str,
                diagnosis=str,
            ),
            output_schema=agdata(status=str, summary=str),
        )
        self.worker = agent()

    def run(self) -> agdata:
        task: RepairTask = self.task
        workspace = Path(self.workspace)
        program_path = workspace / task.program
        original = program_path.read_text()
        protected = snapshot_protected_files(workspace, task)
        started = self.submitted_at
        plan_text = ""
        build_status = "not_started"
        build_summary = ""
        error = ""

        try:
            with agprof.span(f"capstone:plan:{task.name}"):
                diagnosis = self.worker.run(
                    self.planner,
                    agdata(
                        task_name=task.name,
                        program_path=f"/workspace/{task.program}",
                        test_path=f"/workspace/{task.test}",
                        baseline_failure=self.baseline["output"],
                    ),
                    max_steps=16,
                )
                plan_text = diagnosis.plan

            with agprof.span(f"capstone:build:{task.name}"):
                built = self.worker.run(
                    self.builder,
                    agdata(
                        task_name=task.name,
                        program_path=f"/workspace/{task.program}",
                        test_command=f"cd /workspace && {task.test_command}",
                        diagnosis=plan_text,
                    ),
                    max_steps=16,
                )
                build_status = built.status
                build_summary = built.summary
        except Exception as exc:
            error = f"{type(exc).__name__}: {exc}"

        protected_changes = restore_protected_files(workspace, task, protected)
        if protected_changes:
            violation = "agent modified protected files: " + ", ".join(protected_changes)
            error = f"{error}; {violation}".lstrip("; ")

        with agprof.span(f"capstone:verify:{task.name}"):
            verification = run_test(workspace, task)

        program_valid = program_path.is_file() and not program_path.is_symlink()
        modified = program_path.read_text() if program_valid else ""
        if not program_valid:
            error = f"{error}; target program missing or not a regular file".lstrip("; ")
        patch = "".join(
            difflib.unified_diff(
                original.splitlines(keepends=True),
                modified.splitlines(keepends=True),
                fromfile=f"a/{task.program}",
                tofile=f"b/{task.program}",
            )
        )
        return agdata(
            task=task.name,
            category=task.category,
            success=bool(
                verification["passed"] and patch and program_valid and not protected_changes
            ),
            baseline=self.baseline,
            verification=verification,
            plan=plan_text,
            build_status=build_status,
            build_summary=build_summary,
            patch=patch,
            protected_changes=protected_changes,
            error=error,
            duration_s=time.perf_counter() - started,
        )
