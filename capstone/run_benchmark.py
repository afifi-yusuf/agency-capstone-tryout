from __future__ import annotations

import argparse
import json
import statistics
from datetime import datetime
from pathlib import Path

from agency import agent, agdata, agsync
from agency.profiler import agprof

from capstone.mini_swe import (
    DEFAULT_MANIFEST,
    RepairTask,
    RepairTeam,
    ensure_benchmark,
    load_manifest,
    load_private_environment,
    make_config,
    prepare_workspace,
    run_test,
)


def batches(items: list, size: int) -> list[list]:
    if size < 1:
        raise ValueError("parallelism must be at least one")
    return [items[index : index + size] for index in range(0, len(items), size)]


def aggregate_results(results: list[dict], mode: str, parallelism: int) -> dict:
    durations = [float(result["duration_s"]) for result in results]
    successes = sum(bool(result["success"]) for result in results)
    return {
        "mode": mode,
        "parallelism": parallelism,
        "tasks": len(results),
        "successful_repairs": successes,
        "repair_rate": successes / len(results) if results else 0.0,
        "task_duration_mean_s": statistics.mean(durations) if durations else 0.0,
        "task_duration_median_s": statistics.median(durations) if durations else 0.0,
        "task_duration_max_s": max(durations, default=0.0),
    }


def write_artifacts(run_dir: Path, results: list[dict], summary: dict) -> None:
    task_dir = run_dir / "task_results"
    patch_dir = run_dir / "patches"
    task_dir.mkdir(parents=True, exist_ok=True)
    patch_dir.mkdir(parents=True, exist_ok=True)

    with (run_dir / "results.jsonl").open("w") as stream:
        for result in results:
            stream.write(json.dumps(result, sort_keys=True) + "\n")
            (task_dir / f"{result['task']}.json").write_text(
                json.dumps(result, indent=2, sort_keys=True) + "\n"
            )
            (patch_dir / f"{result['task']}.diff").write_text(result["patch"])

    (run_dir / "results.json").write_text(
        json.dumps({"summary": summary, "results": results}, indent=2, sort_keys=True) + "\n"
    )
    lines = [
        "# Agency Mini-SWE Results",
        "",
        f"- Mode: `{summary['mode']}`",
        f"- Parallelism: {summary['parallelism']}",
        f"- Successful repairs: {summary['successful_repairs']} / {summary['tasks']}",
        f"- Repair rate: {summary['repair_rate']:.1%}",
        f"- Mean task duration: {summary['task_duration_mean_s']:.2f} s",
        f"- Median task duration: {summary['task_duration_median_s']:.2f} s",
        f"- Maximum task duration: {summary['task_duration_max_s']:.2f} s",
        "",
        "## Tasks",
        "",
    ]
    for result in results:
        outcome = "PASS" if result["success"] else "FAIL"
        lines.append(
            f"- `{result['task']}`: **{outcome}**, {result['duration_s']:.2f} s"
            + (f", {result['error']}" if result["error"] else "")
        )
    (run_dir / "results.md").write_text("\n".join(lines) + "\n")


def _run_task(task: RepairTask, workspace: Path, baseline: dict) -> tuple[RepairTeam, agdata]:
    team = RepairTeam(
        agconfig=make_config(workspace),
        task=task,
        workspace=workspace,
        baseline=baseline,
        name=f"repair_{task.name}",
    )
    return team, team.run()


def run_benchmark(
    tasks: list[RepairTask],
    source: Path,
    run_dir: Path,
    mode: str,
    parallelism: int,
) -> tuple[list[dict], dict]:
    prepared: list[tuple[RepairTask, Path, dict]] = []
    for task in tasks:
        with agprof.span(f"capstone:prepare:{task.name}"):
            workspace = prepare_workspace(source, run_dir / "workspaces" / task.name, task)
            baseline = run_test(workspace, task)
        if baseline["passed"]:
            raise RuntimeError(f"benchmark task {task.name!r} unexpectedly passes before repair")
        prepared.append((task, workspace, baseline))

    results: list[dict] = []
    batch_size = 1 if mode == "sequential" else parallelism
    for group in batches(prepared, batch_size):
        teams: list[RepairTeam] = []
        pending: list[agdata] = []
        for task, workspace, baseline in group:
            team, result = _run_task(task, workspace, baseline)
            teams.append(team)
            pending.append(result)
        agsync(teams)
        results.extend(item.to_dict() for item in agdata.wait_all(pending))

    summary = aggregate_results(results, mode=mode, parallelism=batch_size)
    write_artifacts(run_dir, results, summary)
    return results, summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Profile an Agency QuixBugs repair workflow")
    parser.add_argument("--mode", choices=("sequential", "parallel"), default="sequential")
    parser.add_argument("--parallelism", type=int, default=2)
    parser.add_argument("--tasks", help="Comma-separated task names; default is the full manifest")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--cache-dir", type=Path, default=Path(".cache/capstone"))
    parser.add_argument("--run-dir", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    load_private_environment()
    revision, manifest_tasks = load_manifest(args.manifest)
    requested = set(args.tasks.split(",")) if args.tasks else None
    tasks = [task for task in manifest_tasks if requested is None or task.name in requested]
    unknown = requested - {task.name for task in tasks} if requested else set()
    if unknown:
        raise ValueError(f"unknown task(s): {sorted(unknown)}")
    if not tasks:
        raise ValueError("no benchmark tasks selected")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_dir = args.run_dir or Path("runs") / f"{timestamp}_mini_swe_{args.mode}"
    run_dir.mkdir(parents=True, exist_ok=False)
    agent.log_dir = run_dir / "logs"
    agent.output_dir = run_dir / "agent_output"

    source = ensure_benchmark(args.cache_dir, revision)
    print(f"Run directory: {run_dir}")
    print(f"QuixBugs revision: {revision}")
    print(f"Tasks: {', '.join(task.name for task in tasks)}")
    print(f"Mode: {args.mode} (parallelism={1 if args.mode == 'sequential' else args.parallelism})")

    _, summary = run_benchmark(
        tasks=tasks,
        source=source,
        run_dir=run_dir,
        mode=args.mode,
        parallelism=args.parallelism,
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
