from __future__ import annotations

import argparse
import json
import math
import statistics
import time
from collections import deque
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Callable

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


@dataclass(frozen=True)
class SchedulerConfig:
    min_parallelism: int = 1
    max_parallelism: int = 4
    poll_interval_s: float = 1.0
    cooldown_s: float = 5.0
    scale_up_streak: int = 3
    pressure_streak: int = 2
    cpu_low_percent: float = 65.0
    cpu_high_percent: float = 85.0
    memory_low_percent: float = 70.0
    memory_high_percent: float = 85.0
    latency_high_ratio: float = 1.75

    def __post_init__(self) -> None:
        if self.min_parallelism < 1:
            raise ValueError("minimum parallelism must be at least one")
        if self.max_parallelism < self.min_parallelism:
            raise ValueError("maximum parallelism must be at least the minimum")
        if self.poll_interval_s <= 0 or self.cooldown_s < 0:
            raise ValueError("scheduler timing values must be positive")


@dataclass(frozen=True)
class ScaleDecision:
    action: str
    reason: str
    previous_target: int
    target: int


class AdaptiveController:
    """Deterministic AIMD controller driven by live profiler pressure."""

    def __init__(self, config: SchedulerConfig) -> None:
        self.config = config
        self.target = config.min_parallelism
        self._healthy_ticks = 0
        self._pressure_ticks = 0
        self._missing_ticks = 0
        self._last_change = -math.inf
        self._durations: deque[float] = deque(maxlen=8)

    def observe(
        self,
        *,
        now: float,
        metrics,
        completed_durations: list[float],
        task_failed: bool,
    ) -> ScaleDecision:
        prior_durations = list(self._durations)
        baseline = statistics.median(prior_durations) if prior_durations else None
        self._durations.extend(completed_durations)
        recent = max(completed_durations, default=None)
        latency_pressure = (
            baseline is not None
            and recent is not None
            and recent > baseline * self.config.latency_high_ratio
        )
        immediate_pressure = task_failed or latency_pressure
        if metrics is None:
            self._missing_ticks += 1
            healthy = False
            pressure = self._missing_ticks >= self.config.pressure_streak or task_failed
            pressure_reason = "task failure" if task_failed else "telemetry unavailable"
        else:
            self._missing_ticks = 0
            memory = metrics.memory_percent
            cpu_pressure = metrics.cpu_capacity_percent >= self.config.cpu_high_percent
            memory_pressure = memory is not None and memory >= self.config.memory_high_percent
            pressure = cpu_pressure or memory_pressure or latency_pressure or task_failed
            healthy = (
                metrics.cpu_capacity_percent <= self.config.cpu_low_percent
                and (memory is None or memory <= self.config.memory_low_percent)
                and not latency_pressure
                and not task_failed
            )
            pressure_reason = (
                "task failure"
                if task_failed
                else "task latency regression"
                if latency_pressure
                else "memory pressure"
                if memory_pressure
                else "CPU pressure"
            )

        self._healthy_ticks = self._healthy_ticks + 1 if healthy else 0
        self._pressure_ticks = self._pressure_ticks + 1 if pressure else 0
        previous = self.target
        cooldown_complete = now - self._last_change >= self.config.cooldown_s
        if (
            (immediate_pressure or self._pressure_ticks >= self.config.pressure_streak)
            and self.target > self.config.min_parallelism
            and cooldown_complete
        ):
            self.target = max(self.config.min_parallelism, math.ceil(self.target / 2))
            self._last_change = now
            self._pressure_ticks = 0
            self._healthy_ticks = 0
            return ScaleDecision("scale_down", pressure_reason, previous, self.target)
        if (
            self._healthy_ticks >= self.config.scale_up_streak
            and self.target < self.config.max_parallelism
            and cooldown_complete
        ):
            self.target += 1
            self._last_change = now
            self._healthy_ticks = 0
            return ScaleDecision("scale_up", "sustained spare capacity", previous, self.target)
        reason = pressure_reason if pressure else "cooldown" if not cooldown_complete else "stable"
        return ScaleDecision("hold", reason, previous, self.target)


def aggregate_results(
    results: list[dict],
    mode: str,
    parallelism: int,
    scheduler_events: "list[dict] | None" = None,
) -> dict:
    durations = [float(result["duration_s"]) for result in results]
    successes = sum(bool(result["success"]) for result in results)
    summary = {
        "mode": mode,
        "parallelism": parallelism,
        "tasks": len(results),
        "successful_repairs": successes,
        "repair_rate": successes / len(results) if results else 0.0,
        "task_duration_mean_s": statistics.mean(durations) if durations else 0.0,
        "task_duration_median_s": statistics.median(durations) if durations else 0.0,
        "task_duration_max_s": max(durations, default=0.0),
    }
    if scheduler_events:
        concurrency = [event["in_flight"] for event in scheduler_events]
        summary["scheduler"] = {
            "average_concurrency": statistics.mean(concurrency),
            "peak_concurrency": max(concurrency, default=0),
            "scale_ups": sum(event["action"] == "scale_up" for event in scheduler_events),
            "scale_downs": sum(event["action"] == "scale_down" for event in scheduler_events),
            "events": len(scheduler_events),
        }
    return summary


def write_artifacts(
    run_dir: Path,
    results: list[dict],
    summary: dict,
    scheduler_events: "list[dict] | None" = None,
) -> None:
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
    if scheduler_events is not None:
        with (run_dir / "scheduler_events.jsonl").open("w") as stream:
            for event in scheduler_events:
                stream.write(json.dumps(event, sort_keys=True) + "\n")
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
    submitted_at = time.perf_counter()
    team = RepairTeam(
        agconfig=make_config(workspace),
        task=task,
        workspace=workspace,
        baseline=baseline,
        submitted_at=submitted_at,
        name=f"repair_{task.name}",
    )
    return team, team.run()


def _failed_task_result(task: RepairTask, baseline: dict, started: float, exc: Exception) -> dict:
    return {
        "task": task.name,
        "category": task.category,
        "success": False,
        "baseline": baseline,
        "verification": {
            "passed": False,
            "returncode": None,
            "output": "",
            "duration_s": 0.0,
        },
        "plan": "",
        "build_status": "scheduler_failure",
        "build_summary": "",
        "patch": "",
        "protected_changes": [],
        "error": f"{type(exc).__name__}: {exc}",
        "duration_s": time.perf_counter() - started,
    }


def _metrics_payload(metrics) -> dict:
    if metrics is None:
        return {
            "sample_age_ms": None,
            "cpu_capacity_percent": None,
            "memory_mb": None,
            "memory_percent": None,
            "active_sandboxes": None,
        }
    return {
        "sample_age_ms": metrics.sample_age_ms,
        "cpu_capacity_percent": metrics.cpu_capacity_percent,
        "memory_mb": metrics.memory_mb,
        "memory_percent": metrics.memory_percent,
        "active_sandboxes": metrics.active_sandboxes,
    }


def _baseline_matches(task: RepairTask, baseline: dict) -> bool:
    if task.expected_baseline == "timeout":
        return baseline["returncode"] is None and baseline["output"].startswith("TIMEOUT")
    return baseline["returncode"] == 1


def run_benchmark(
    tasks: list[RepairTask],
    source: Path,
    run_dir: Path,
    mode: str,
    parallelism: int,
    *,
    scheduler_config: "SchedulerConfig | None" = None,
    telemetry_provider: "Callable[[], object | None]" = agprof.live_metrics,
    sleep: "Callable[[float], None]" = time.sleep,
) -> tuple[list[dict], dict]:
    benchmark_started = time.perf_counter()
    prepared: list[tuple[RepairTask, Path, dict]] = []
    for task in tasks:
        with agprof.span(f"capstone:prepare:{task.name}"):
            workspace = prepare_workspace(source, run_dir / "workspaces" / task.name, task)
            baseline = run_test(workspace, task, timeout=task.baseline_timeout_s)
        if not _baseline_matches(task, baseline):
            raise RuntimeError(
                f"benchmark task {task.name!r} baseline was not an expected test failure "
                f"({task.expected_baseline=}, pytest return code {baseline['returncode']}):\n"
                f"{baseline['output']}"
            )
        prepared.append((task, workspace, baseline))

    results: list[dict] = []
    events: list[dict] = []
    queued = deque(prepared)
    active: list[dict] = []
    config = scheduler_config or SchedulerConfig(
        min_parallelism=1,
        max_parallelism=max(1, parallelism),
    )
    controller = AdaptiveController(config) if mode == "adaptive" else None
    fixed_target = 1 if mode == "sequential" else parallelism
    if fixed_target < 1:
        raise ValueError("parallelism must be at least one")

    while queued or active:
        now = time.perf_counter()
        completed_durations: list[float] = []
        task_failed = False
        remaining: list[dict] = []
        for entry in active:
            if entry["pending"].is_pending():
                remaining.append(entry)
                continue
            try:
                agsync(entry["team"])
                result = entry["pending"].to_dict()
            except Exception as exc:
                result = _failed_task_result(
                    entry["task"], entry["baseline"], entry["started"], exc
                )
            results.append(result)
            completed_durations.append(float(result["duration_s"]))
            task_failed = task_failed or not bool(result["success"])
        active = remaining

        metrics = telemetry_provider()
        with agprof.span("capstone:scheduler:tick"):
            if controller is not None:
                decision = controller.observe(
                    now=now,
                    metrics=metrics,
                    completed_durations=completed_durations,
                    task_failed=task_failed,
                )
                target = decision.target
            else:
                target = fixed_target
                decision = ScaleDecision("hold", f"fixed concurrency {target}", target, target)

            while queued and len(active) < target:
                task, workspace, baseline = queued.popleft()
                started = time.perf_counter()
                try:
                    team, pending = _run_task(task, workspace, baseline)
                except Exception as exc:
                    results.append(_failed_task_result(task, baseline, started, exc))
                    completed_durations.append(time.perf_counter() - started)
                    task_failed = True
                    continue
                active.append(
                    {
                        "task": task,
                        "baseline": baseline,
                        "team": team,
                        "pending": pending,
                        "started": started,
                    }
                )

            event = {
                "elapsed_s": time.perf_counter() - benchmark_started,
                "action": decision.action,
                "reason": decision.reason,
                "previous_target": decision.previous_target,
                "target": target,
                "in_flight": len(active),
                "queued": len(queued),
                "completed": len(results),
                **_metrics_payload(metrics),
            }
            events.append(event)
            agprof.annotate(
                action=decision.action,
                reason=decision.reason,
                target=target,
                in_flight=len(active),
            )

        if completed_durations:
            reported_parallelism = config.max_parallelism if mode == "adaptive" else fixed_target
            partial = aggregate_results(
                results,
                mode=mode,
                parallelism=reported_parallelism,
                scheduler_events=events,
            )
            if mode == "adaptive":
                partial["scheduler"]["policy"] = asdict(config)
            partial["benchmark_wall_s"] = time.perf_counter() - benchmark_started
            write_artifacts(run_dir, results, partial, events)

        if active:
            sleep(config.poll_interval_s)

    reported_parallelism = config.max_parallelism if mode == "adaptive" else fixed_target
    summary = aggregate_results(
        results,
        mode=mode,
        parallelism=reported_parallelism,
        scheduler_events=events,
    )
    if mode == "adaptive":
        summary["scheduler"]["policy"] = asdict(config)
    summary["benchmark_wall_s"] = time.perf_counter() - benchmark_started
    write_artifacts(run_dir, results, summary, events)
    return results, summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Profile an Agency QuixBugs repair workflow")
    parser.add_argument(
        "--mode", choices=("sequential", "parallel", "adaptive"), default="sequential"
    )
    parser.add_argument("--parallelism", type=int, default=2)
    parser.add_argument("--min-parallelism", type=int, default=1)
    parser.add_argument("--max-parallelism", type=int, default=4)
    parser.add_argument("--scheduler-poll-s", type=float, default=1.0)
    parser.add_argument("--scheduler-cooldown-s", type=float, default=5.0)
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
    if args.mode == "adaptive" and not agprof.enabled():
        raise RuntimeError(
            "adaptive mode requires an active agprof session; set AGENCY_PROFILE=1 "
            "and AGENCY_PROFILE_SCOPE=process"
        )

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_dir = args.run_dir or Path("runs") / f"{timestamp}_mini_swe_{args.mode}"
    run_dir.mkdir(parents=True, exist_ok=False)
    agent.log_dir = run_dir / "logs"
    agent.output_dir = run_dir / "agent_output"

    source = ensure_benchmark(args.cache_dir, revision)
    print(f"Run directory: {run_dir}")
    print(f"QuixBugs revision: {revision}")
    print(f"Tasks: {', '.join(task.name for task in tasks)}")
    if args.mode == "adaptive":
        mode_detail = f"adaptive range={args.min_parallelism}-{args.max_parallelism}"
    else:
        mode_detail = f"parallelism={1 if args.mode == 'sequential' else args.parallelism}"
    print(f"Mode: {args.mode} ({mode_detail})")

    _, summary = run_benchmark(
        tasks=tasks,
        source=source,
        run_dir=run_dir,
        mode=args.mode,
        parallelism=args.parallelism,
        scheduler_config=SchedulerConfig(
            min_parallelism=args.min_parallelism,
            max_parallelism=args.max_parallelism,
            poll_interval_s=args.scheduler_poll_s,
            cooldown_s=args.scheduler_cooldown_s,
        ),
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
