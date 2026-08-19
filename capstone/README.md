# Agency Mini-SWE Capstone Workflow

This workflow uses Agency to diagnose, repair, and independently verify real
Python defects from the QuixBugs program-repair benchmark. It compares a
sequential run with two-way agent fan-out and records Agency profiler traces.

## What is measured

- End-to-end repair rate and task latency
- LLM latency, time to first token, token counts, and retries
- Tool and sandbox operation latency
- CPU, memory, and storage I/O
- Container CLI contention (`sync:container`) under parallel fan-out

The benchmark is pinned in `tasks.json`. Each task checkout excludes QuixBugs'
correct implementations and Git history so the agent cannot retrieve the answer.
The harness verifies that each task fails before the agent runs and passes
afterward.

## EC2 prerequisites

The profiler requires Linux, cgroups v2, `/proc`, `systemd-run`, `setpriv`, and
non-interactive sudo. The current `t3.medium` is CPU-only, so this experiment is
an end-to-end bug-fix and concurrency workload, not a GPU workload.

Use at least a 40 GB root volume. On a 4 GB instance, add swap and cap fan-out at
two tasks:

```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

sudo apt-get update
sudo apt-get install -y docker.io git curl util-linux
sudo systemctl enable --now docker
sudo usermod -aG docker "$USER"
```

Log out and reconnect after adding the Docker group. Then verify:

```bash
docker info
test -f /sys/fs/cgroup/cgroup.controllers
sudo -n systemd-run --version
```

## Install and build

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

cd agency-staging
uv venv --python 3.12 --seed --managed-python
uv pip install -e ".[profiler,dev]"

GPU_TYPE=cpu ./images/build.sh
docker build -t agency-capstone:latest -f capstone/Dockerfile .
```

## Configure the endpoint

Do not put the API key in a file committed to Git or directly in a shell command.
The helper stores it in a private user-level file:

```bash
./capstone/configure_env.sh
source "$HOME/.config/agency-capstone/env"

curl -fsS -H "Authorization: Bearer $LLM_API_KEY" "$LLM_BASE_URL/models"
```

## Smoke test

```bash
uv run python -m capstone.run_benchmark \
  --mode sequential \
  --tasks gcd \
  --run-dir runs/smoke_gcd
```

## Profile sequential and parallel runs

Run from a clean shell for each profile. The profiler re-executes the command in
a dedicated systemd cgroup.

```bash
AGENCY_PROFILE=1 \
AGENCY_PROFILE_SCOPE=process \
AGENCY_PROFILE_DIR=runs/profile_sequential \
uv run python -m capstone.run_benchmark \
  --mode sequential \
  --run-dir runs/results_sequential

AGENCY_PROFILE=1 \
AGENCY_PROFILE_SCOPE=process \
AGENCY_PROFILE_DIR=runs/profile_parallel \
uv run python -m capstone.run_benchmark \
  --mode parallel \
  --parallelism 2 \
  --run-dir runs/results_parallel
```

Repeat both modes at least twice. The endpoint is shared and live, so latency is
an uncontrolled variable; do not interpret one run as a deterministic speedup.

## Artifacts

Each result directory contains aggregate JSON/Markdown, task JSON, patches,
agent logs, and isolated workspaces. Each profile directory contains:

- `summary.json`
- `summary.md`
- `*.pt.trace.json`

Download the trace and open it in [Perfetto](https://ui.perfetto.dev). Use an
SSH tunnel rather than opening dashboard ports publicly if the Web UI is used.

After copying repeated run summaries into `capstone/artifacts/`, regenerate the
aggregate and comparison figure with:

```bash
uv run --with matplotlib python -m capstone.generate_figures
```

