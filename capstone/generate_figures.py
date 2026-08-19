from __future__ import annotations

import json
import statistics
from pathlib import Path

import matplotlib.pyplot as plt

ARTIFACTS = Path(__file__).with_name("artifacts")
RUNS = {
    "Sequential": [ARTIFACTS / "sequential", ARTIFACTS / "sequential_2"],
    "Parallel (2)": [ARTIFACTS / "parallel", ARTIFACTS / "parallel_2"],
}


def _load_run(path: Path) -> dict:
    profile = json.loads((path / "profile_summary.json").read_text())
    results = json.loads((path / "results.json").read_text())
    return {
        "duration_s": profile["duration_ms"] / 1000,
        "throughput": profile["run_metrics"]["successful_per_second"],
        "task_mean_s": results["summary"]["task_duration_mean_s"],
        "repair_rate": results["summary"]["repair_rate"],
        "cpu_average_percent": profile["workload_metrics"]["cpu_average_percent"],
        "memory_peak_mb": profile["workload_metrics"]["memory_peak_mb"],
        "ttft_ms": profile["llm_metrics"]["ttft"]["mean_ms"],
        "llm_wait_s": profile["llm_metrics"]["total_wait_ms"] / 1000,
    }


def aggregate() -> dict:
    raw = {mode: [_load_run(path) for path in paths] for mode, paths in RUNS.items()}
    means = {
        mode: {key: statistics.mean(run[key] for run in runs) for key in runs[0]}
        for mode, runs in raw.items()
    }
    sequential = means["Sequential"]
    parallel = means["Parallel (2)"]
    comparison = {
        "wall_time_reduction_percent": 100
        * (sequential["duration_s"] - parallel["duration_s"])
        / sequential["duration_s"],
        "speedup": sequential["duration_s"] / parallel["duration_s"],
        "throughput_increase_percent": 100
        * (parallel["throughput"] - sequential["throughput"])
        / sequential["throughput"],
        "task_latency_increase_percent": 100
        * (parallel["task_mean_s"] - sequential["task_mean_s"])
        / sequential["task_mean_s"],
    }
    return {"runs": raw, "means": means, "comparison": comparison}


def write_aggregate(data: dict) -> None:
    (ARTIFACTS / "aggregate.json").write_text(json.dumps(data, indent=2) + "\n")
    seq = data["means"]["Sequential"]
    par = data["means"]["Parallel (2)"]
    comp = data["comparison"]
    lines = [
        "# Repeated-run aggregate",
        "",
        "- Repetitions: 2 per mode",
        "- Repairs: 12 / 12 successful in each mode",
        f"- Mean profiled wall time: {seq['duration_s']:.1f} s sequential, "
        f"{par['duration_s']:.1f} s parallel",
        f"- Wall-time reduction: {comp['wall_time_reduction_percent']:.1f}%",
        f"- Speedup: {comp['speedup']:.2f}×",
        f"- Throughput increase: {comp['throughput_increase_percent']:.1f}%",
        f"- Mean task-latency increase: {comp['task_latency_increase_percent']:.1f}%",
        f"- Mean CPU utilization: {seq['cpu_average_percent']:.1f}% sequential, "
        f"{par['cpu_average_percent']:.1f}% parallel",
        f"- Peak sampled memory: {seq['memory_peak_mb']:.1f} MB sequential, "
        f"{par['memory_peak_mb']:.1f} MB parallel",
        f"- Mean LLM TTFT: {seq['ttft_ms']:.1f} ms sequential, {par['ttft_ms']:.1f} ms parallel",
    ]
    (ARTIFACTS / "aggregate.md").write_text("\n".join(lines) + "\n")


def plot(data: dict) -> None:
    labels = list(RUNS)
    colors = ["#2563EB", "#EA580C"]
    means = data["means"]
    raw = data["runs"]
    metrics = [
        ("duration_s", "Profiled session wall time", "Seconds"),
        ("throughput", "Successful skill-run throughput", "Runs per second"),
        ("task_mean_s", "Mean end-to-end task latency", "Seconds"),
        ("cpu_average_percent", "Average host CPU utilization", "Percent"),
    ]

    figure, axes = plt.subplots(2, 2, figsize=(11, 7.5))
    for axis, (key, title, unit) in zip(axes.flat, metrics):
        values = [means[label][key] for label in labels]
        bars = axis.bar(labels, values, color=colors, width=0.58)
        for index, label in enumerate(labels):
            samples = [run[key] for run in raw[label]]
            axis.scatter([index - 0.06, index + 0.06], samples, color="#111827", s=24, zorder=3)
        axis.bar_label(bars, fmt="%.2f", padding=4, fontsize=9)
        axis.set_title(title, loc="left", fontweight="bold")
        axis.set_ylabel(unit)
        axis.grid(axis="y", alpha=0.2)
        axis.spines[["top", "right"]].set_visible(False)

    figure.suptitle(
        "Agency Mini-SWE profile: sequential vs two-agent fan-out",
        fontsize=15,
        fontweight="bold",
        y=0.985,
    )
    figure.text(
        0.5,
        0.012,
        "Source: Agency agprof on AWS EC2 t3.medium · 6 QuixBugs tasks · 2 runs per mode",
        ha="center",
        fontsize=9,
        color="#4B5563",
    )
    figure.tight_layout(rect=(0, 0.045, 1, 0.955))
    figure.savefig(ARTIFACTS / "profile_comparison.png", dpi=180)
    plt.close(figure)


def main() -> None:
    data = aggregate()
    write_aggregate(data)
    plot(data)


if __name__ == "__main__":
    main()
