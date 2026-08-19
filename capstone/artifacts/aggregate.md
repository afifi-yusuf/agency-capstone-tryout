# Profile-guided scaling aggregate

- Repetitions: 3 per policy
- Tasks: 12 pinned QuixBugs repairs per run
- Adaptive speedup over fixed 1: 2.26×
- Adaptive wall-time reduction over fixed 1: 55.8%
- Fastest fixed policy: Fixed 4
- Adaptive speedup over fastest fixed: 0.97×

## Policy means

- Fixed 1: 708.5 s, 0.0171 repairs/s, 15.3% CPU, 100.0% repair rate, 1.00 average concurrency
- Fixed 2: 416.7 s, 0.0290 repairs/s, 28.2% CPU, 100.0% repair rate, 1.90 average concurrency
- Fixed 4: 304.8 s, 0.0404 repairs/s, 37.7% CPU, 100.0% repair rate, 3.53 average concurrency
- Adaptive 1–4: 313.1 s, 0.0391 repairs/s, 36.5% CPU, 100.0% repair rate, 3.41 average concurrency
