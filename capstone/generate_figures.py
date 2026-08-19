from __future__ import annotations

import json
import statistics
from pathlib import Path

import matplotlib.pyplot as plt

ARTIFACTS = Path(__file__).with_name("artifacts")
RUNS = {
    "Fixed 1": [ARTIFACTS / "scaling" / f"seq_{index}" for index in range(1, 4)],
    "Fixed 2": [ARTIFACTS / "scaling" / f"p2_{index}" for index in range(1, 4)],
    "Fixed 4": [ARTIFACTS / "scaling" / f"p4_{index}" for index in range(1, 4)],
    "Adaptive 1–4": [ARTIFACTS / "scaling" / f"adaptive_{index}" for index in range(1, 4)],
}


def _load_run(path: Path) -> dict:
    profile = json.loads((path / "profile_summary.json").read_text())
    results = json.loads((path / "results.json").read_text())
    return {
        "duration_s": profile["duration_ms"] / 1000,
        "throughput": results["summary"]["successful_repairs"]
        / results["summary"]["benchmark_wall_s"],
        "task_mean_s": results["summary"]["task_duration_mean_s"],
        "repair_rate": results["summary"]["repair_rate"],
        "cpu_average_percent": profile["workload_metrics"]["cpu_average_percent"],
        "memory_peak_mb": profile["workload_metrics"]["memory_peak_mb"],
        "ttft_ms": profile["llm_metrics"]["ttft"]["mean_ms"],
        "llm_wait_s": profile["llm_metrics"]["total_wait_ms"] / 1000,
        "average_concurrency": results["summary"]["scheduler"]["average_concurrency"],
        "peak_concurrency": results["summary"]["scheduler"]["peak_concurrency"],
    }


def aggregate() -> dict:
    raw = {mode: [_load_run(path) for path in paths] for mode, paths in RUNS.items()}
    means = {
        mode: {key: statistics.mean(run[key] for run in runs) for key in runs[0]}
        for mode, runs in raw.items()
    }
    confidence_95 = {
        mode: {
            key: 4.303 * statistics.stdev(run[key] for run in runs) / len(runs) ** 0.5
            for key in runs[0]
        }
        for mode, runs in raw.items()
    }
    sequential = means["Fixed 1"]
    adaptive = means["Adaptive 1–4"]
    fastest_fixed_label = min(
        ("Fixed 1", "Fixed 2", "Fixed 4"), key=lambda label: means[label]["duration_s"]
    )
    fastest_fixed = means[fastest_fixed_label]
    comparison = {
        "adaptive_vs_sequential_speedup": sequential["duration_s"] / adaptive["duration_s"],
        "adaptive_vs_sequential_wall_reduction_percent": 100
        * (sequential["duration_s"] - adaptive["duration_s"])
        / sequential["duration_s"],
        "fastest_fixed": fastest_fixed_label,
        "adaptive_vs_fastest_fixed_speedup": fastest_fixed["duration_s"] / adaptive["duration_s"],
    }
    return {
        "runs": raw,
        "means": means,
        "confidence_95": confidence_95,
        "comparison": comparison,
    }


def write_aggregate(data: dict) -> None:
    (ARTIFACTS / "aggregate.json").write_text(json.dumps(data, indent=2) + "\n")
    comp = data["comparison"]
    lines = [
        "# Profile-guided scaling aggregate",
        "",
        "- Repetitions: 3 per policy",
        "- Tasks: 12 pinned QuixBugs repairs per run",
        f"- Adaptive speedup over fixed 1: {comp['adaptive_vs_sequential_speedup']:.2f}×",
        "- Adaptive wall-time reduction over fixed 1: "
        f"{comp['adaptive_vs_sequential_wall_reduction_percent']:.1f}%",
        f"- Fastest fixed policy: {comp['fastest_fixed']}",
        f"- Adaptive speedup over fastest fixed: {comp['adaptive_vs_fastest_fixed_speedup']:.2f}×",
        "",
        "## Policy means",
        "",
    ]
    for label, values in data["means"].items():
        lines.append(
            f"- {label}: {values['duration_s']:.1f} s, "
            f"{values['throughput']:.4f} repairs/s, "
            f"{values['cpu_average_percent']:.1f}% CPU, "
            f"{values['repair_rate']:.1%} repair rate, "
            f"{values['average_concurrency']:.2f} average concurrency"
        )
    (ARTIFACTS / "aggregate.md").write_text("\n".join(lines) + "\n")


def plot(data: dict) -> None:
    labels = list(RUNS)
    colors = ["#2563EB", "#0EA5E9", "#7C3AED", "#EA580C"]
    means = data["means"]
    raw = data["runs"]
    confidence = data["confidence_95"]
    metrics = [
        ("duration_s", "Profiled session wall time", "Seconds"),
        ("throughput", "Successful repair throughput", "Repairs per second"),
        ("task_mean_s", "Mean end-to-end task latency", "Seconds"),
        ("cpu_average_percent", "Average host CPU utilization", "Core percent"),
        ("memory_peak_mb", "Peak sampled memory", "MB"),
        ("average_concurrency", "Average active repair teams", "Teams"),
    ]

    figure, axes = plt.subplots(2, 3, figsize=(14, 8))
    for axis, (key, title, unit) in zip(axes.flat, metrics):
        values = [means[label][key] for label in labels]
        errors = [confidence[label][key] for label in labels]
        bars = axis.bar(labels, values, yerr=errors, capsize=3, color=colors, width=0.62)
        for index, label in enumerate(labels):
            samples = [run[key] for run in raw[label]]
            axis.scatter(
                [index - 0.08, index, index + 0.08],
                samples,
                color="#111827",
                s=20,
                zorder=3,
            )
        axis.bar_label(bars, fmt="%.2f", padding=4, fontsize=9)
        axis.set_title(title, loc="left", fontweight="bold")
        axis.set_ylabel(unit)
        axis.tick_params(axis="x", rotation=18)
        axis.grid(axis="y", alpha=0.2)
        axis.spines[["top", "right"]].set_visible(False)

    figure.suptitle(
        "Agency Mini-SWE: fixed versus profile-guided agent scaling",
        fontsize=15,
        fontweight="bold",
        y=0.985,
    )
    figure.text(
        0.5,
        0.012,
        "Agency agprof · AWS EC2 t3.medium · 12 QuixBugs tasks · 3 runs per policy · error bars: 95% CI",
        ha="center",
        fontsize=9,
        color="#4B5563",
    )
    figure.tight_layout(rect=(0, 0.045, 1, 0.955))
    figure.savefig(ARTIFACTS / "profile_comparison.png", dpi=180)
    plt.close(figure)


def plot_adaptive_timeline() -> None:
    run = ARTIFACTS / "scaling" / "adaptive_1"
    events = [
        json.loads(line) for line in (run / "scheduler_events.jsonl").read_text().splitlines()
    ]
    elapsed = [event["elapsed_s"] for event in events]
    figure, primary = plt.subplots(figsize=(11, 5.5))
    primary.step(elapsed, [event["target"] for event in events], where="post", label="Target")
    primary.step(
        elapsed,
        [event["in_flight"] for event in events],
        where="post",
        label="In flight",
        alpha=0.8,
    )
    primary.set_xlabel("Elapsed seconds")
    primary.set_ylabel("Repair teams")
    primary.set_ylim(0, 4.5)
    primary.grid(alpha=0.2)
    secondary = primary.twinx()
    cpu = [
        float("nan") if event["cpu_capacity_percent"] is None else event["cpu_capacity_percent"]
        for event in events
    ]
    memory = [
        float("nan") if event["memory_percent"] is None else event["memory_percent"]
        for event in events
    ]
    secondary.plot(elapsed, cpu, color="#DC2626", alpha=0.55, label="CPU capacity")
    secondary.plot(elapsed, memory, color="#059669", alpha=0.55, label="Memory")
    secondary.set_ylabel("Resource utilization (%)")
    lines = primary.get_lines() + secondary.get_lines()
    primary.legend(lines, [line.get_label() for line in lines], loc="upper right")
    primary.set_title("Adaptive scheduler decisions and live profiler pressure", loc="left")
    figure.tight_layout()
    figure.savefig(ARTIFACTS / "adaptive_timeline.png", dpi=180)
    plt.close(figure)


def main() -> None:
    data = aggregate()
    write_aggregate(data)
    plot(data)
    plot_adaptive_timeline()


if __name__ == "__main__":
    main()
