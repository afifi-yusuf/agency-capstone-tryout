import json
import os
from types import SimpleNamespace

import pytest

import capstone.run_benchmark as benchmark_module
from capstone.mini_swe import (
    RepairTask,
    load_manifest,
    load_private_environment,
    make_config,
    prepare_workspace,
    restore_protected_files,
    run_test,
    snapshot_protected_files,
)
from capstone.run_benchmark import AdaptiveController, SchedulerConfig, aggregate_results


def test_manifest_is_pinned_and_tasks_are_unique():
    revision, tasks = load_manifest()

    assert len(revision) == 40
    assert len(tasks) >= 6
    assert len({task.name for task in tasks}) == len(tasks)


def test_manifest_rejects_unsafe_paths(tmp_path):
    manifest = tmp_path / "tasks.json"
    manifest.write_text(
        json.dumps(
            {
                "revision": "a" * 40,
                "tasks": [
                    {
                        "name": "escape",
                        "program": "../answer.py",
                        "test": "test_answer.py",
                        "category": "invalid",
                    }
                ],
            }
        )
    )

    with pytest.raises(ValueError, match="unsafe path"):
        load_manifest(manifest)


def test_manifest_rejects_unsafe_task_name(tmp_path):
    manifest = tmp_path / "tasks.json"
    manifest.write_text(
        json.dumps(
            {
                "revision": "a" * 40,
                "tasks": [
                    {
                        "name": "../../escape",
                        "program": "answer.py",
                        "test": "test_answer.py",
                        "category": "invalid",
                    }
                ],
            }
        )
    )

    with pytest.raises(ValueError, match="safe path component"):
        load_manifest(manifest)


def test_private_environment_restores_profiled_process_settings(tmp_path, monkeypatch):
    env_file = tmp_path / "env"
    env_file.write_text(
        "export LLM_BASE_URL=http://example.test:18000/v1\n"
        "export LLM_MODEL=example/model\n"
        "export LLM_API_KEY=private-value\n"
    )
    for key in ("LLM_BASE_URL", "LLM_MODEL", "LLM_API_KEY"):
        monkeypatch.delenv(key, raising=False)

    assert load_private_environment(env_file) is True
    assert os.environ["LLM_BASE_URL"] == "http://example.test:18000/v1"
    assert os.environ["LLM_API_KEY"] == "private-value"


def test_prepare_workspace_removes_reference_implementations(tmp_path):
    source = tmp_path / "source"
    (source / "python_programs").mkdir(parents=True)
    (source / "python_testcases").mkdir()
    (source / "correct_python_programs").mkdir()
    (source / "java_programs").mkdir()
    (source / ".git").mkdir()
    (source / "python_programs" / "gcd.py").write_text("def gcd(a, b): return a\n")
    (source / "python_testcases" / "test_gcd.py").write_text("def test_gcd(): pass\n")
    (source / "correct_python_programs" / "gcd.py").write_text("secret\n")

    task = RepairTask("gcd", "python_programs/gcd.py", "python_testcases/test_gcd.py", "math")
    destination = prepare_workspace(source, tmp_path / "workspace", task)

    assert (destination / task.program).is_file()
    assert not (destination / "correct_python_programs").exists()
    assert not (destination / "java_programs").exists()
    assert not (destination / ".git").exists()


def test_protected_files_are_restored_but_target_patch_is_preserved(tmp_path):
    programs = tmp_path / "python_programs"
    tests = tmp_path / "python_testcases"
    programs.mkdir()
    tests.mkdir()
    target = programs / "gcd.py"
    protected_test = tests / "test_gcd.py"
    target.write_text("BUG = True\n")
    protected_test.write_text("def test_gcd(): pass\n")
    task = RepairTask("gcd", "python_programs/gcd.py", "python_testcases/test_gcd.py", "math")
    protected = snapshot_protected_files(tmp_path, task)

    target.write_text("BUG = False\n")
    protected_test.write_text("def test_gcd(): assert True\n")
    (tmp_path / "conftest.py").write_text("pytest_plugins = []\n")
    changed = restore_protected_files(tmp_path, task, protected)

    assert changed == ["conftest.py", "python_testcases/test_gcd.py"]
    assert target.read_text() == "BUG = False\n"
    assert protected_test.read_text() == "def test_gcd(): pass\n"
    assert not (tmp_path / "conftest.py").exists()


def test_capstone_config_disables_network_and_bounds_llm_wait(tmp_path):
    cfg = make_config(tmp_path)

    assert cfg.get("agSandbox", "network_mode") == "none"
    assert cfg.get("agllm", "max_retries") == 3
    assert cfg.get("agllm", "idle_timeout") == 180.0


def test_run_test_reports_success_and_failure(tmp_path):
    tests = tmp_path / "python_testcases"
    programs = tmp_path / "python_programs"
    tests.mkdir()
    programs.mkdir()
    test_file = tests / "test_sample.py"
    test_file.write_text("def test_sample():\n    assert True\n")
    (programs / "sample.py").write_text("VALUE = 1\n")
    task = RepairTask(
        "sample", "python_programs/sample.py", "python_testcases/test_sample.py", "fixture"
    )

    assert run_test(tmp_path, task)["passed"] is True
    test_file.write_text("def test_sample():\n    assert False\n")
    result = run_test(tmp_path, task)
    assert result["passed"] is False
    assert result["returncode"] == 1


def test_aggregate_results():
    summary = aggregate_results(
        [
            {"success": True, "duration_s": 1.0},
            {"success": False, "duration_s": 3.0},
        ],
        mode="parallel",
        parallelism=2,
    )
    assert summary["repair_rate"] == 0.5
    assert summary["task_duration_mean_s"] == 2.0


def test_adaptive_controller_scales_up_then_down():
    controller = AdaptiveController(
        SchedulerConfig(
            min_parallelism=1,
            max_parallelism=4,
            cooldown_s=0,
            scale_up_streak=2,
            pressure_streak=2,
        )
    )
    healthy = SimpleNamespace(cpu_capacity_percent=20.0, memory_percent=30.0)
    pressured = SimpleNamespace(cpu_capacity_percent=95.0, memory_percent=30.0)

    assert (
        controller.observe(now=0, metrics=healthy, completed_durations=[], task_failed=False).action
        == "hold"
    )
    increased = controller.observe(
        now=1, metrics=healthy, completed_durations=[], task_failed=False
    )
    assert (increased.action, increased.target) == ("scale_up", 2)

    decreased = controller.observe(now=2, metrics=healthy, completed_durations=[], task_failed=True)
    assert (decreased.action, decreased.target, decreased.reason) == (
        "scale_down",
        1,
        "task failure",
    )

    controller.observe(now=3, metrics=healthy, completed_durations=[], task_failed=False)
    controller.observe(now=4, metrics=healthy, completed_durations=[], task_failed=False)
    controller.observe(now=5, metrics=pressured, completed_durations=[], task_failed=False)
    decreased = controller.observe(
        now=6, metrics=pressured, completed_durations=[], task_failed=False
    )
    assert (decreased.action, decreased.target) == ("scale_down", 1)


def test_adaptive_scheduler_bounds_concurrency_and_persists_events(tmp_path, monkeypatch):
    source = tmp_path / "source"
    (source / "python_programs").mkdir(parents=True)
    (source / "python_testcases").mkdir()
    tasks = []
    for index in range(3):
        name = f"task{index}"
        program = f"python_programs/{name}.py"
        test = f"python_testcases/test_{name}.py"
        (source / program).write_text("VALUE = False\n")
        (source / test).write_text(
            f"from python_programs.{name} import VALUE\n\ndef test_value():\n    assert VALUE\n"
        )
        tasks.append(RepairTask(name, program, test, "fixture"))

    current = 0
    peak = 0

    class FakePending:
        def __init__(self, task):
            self.task = task
            self.polls = 1

        def is_pending(self):
            self.polls -= 1
            return self.polls >= 0

        def to_dict(self):
            nonlocal current
            current -= 1
            return {
                "task": self.task.name,
                "category": self.task.category,
                "success": True,
                "duration_s": 1.0,
                "patch": "patch\n",
                "error": "",
            }

    def fake_run_task(task, workspace, baseline):
        nonlocal current, peak
        current += 1
        peak = max(peak, current)
        return object(), FakePending(task)

    metrics = SimpleNamespace(
        sample_age_ms=1.0,
        cpu_capacity_percent=20.0,
        memory_mb=100.0,
        memory_percent=10.0,
        active_sandboxes=1,
    )
    monkeypatch.setattr(benchmark_module, "_run_task", fake_run_task)
    monkeypatch.setattr(benchmark_module, "agsync", lambda team: None)

    results, summary = benchmark_module.run_benchmark(
        tasks,
        source,
        tmp_path / "run",
        mode="adaptive",
        parallelism=2,
        scheduler_config=SchedulerConfig(
            min_parallelism=1,
            max_parallelism=2,
            poll_interval_s=0.001,
            cooldown_s=0,
            scale_up_streak=2,
        ),
        telemetry_provider=lambda: metrics,
        sleep=lambda _: None,
    )

    assert len(results) == 3
    assert peak == 2
    assert summary["scheduler"]["peak_concurrency"] == 2
    events = [
        json.loads(line)
        for line in (tmp_path / "run" / "scheduler_events.jsonl").read_text().splitlines()
    ]
    assert any(event["action"] == "scale_up" for event in events)
