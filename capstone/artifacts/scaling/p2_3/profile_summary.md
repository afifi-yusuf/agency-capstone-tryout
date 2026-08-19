# agprof summary

- Duration: **412.446 s**
- Runs: **24/24 completed**, 24 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.058 runs/s**
- LLM: **85 calls**, 85 succeeded, 0 failed, 0 interrupted, 0 retries, 517.145 s total wait
- Tools: **109/109 completed**, 2 failed, 0 interrupted
- Raw resource samples: **49725** at 9.836 Hz effective (10 Hz configured)
- GPU sampling: **unavailable** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 25862.949 / 44157.911 ms |
| LLM latency p50 / p95 | 3586.776 / 23783.853 ms |
| LLM TTFT p50 / p95 | 719.101 / 1173.373 ms |
| LLM input / output tokens | 427241 / 22323 |
| LLM output throughput | 49.356 tokens/s |
| LLM attempts | 85 total, 85 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 423.641 / 1419.905 ms |

### Tool outcomes

| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 13/13 | 13 | 0 | 0 | 1199.153 ms | 2716.661 ms |
| edit | 13/13 | 13 | 0 | 0 | 430.273 ms | 659.210 ms |
| glob | 4/4 | 4 | 0 | 0 | 352.172 ms | 480.904 ms |
| grep | 1/1 | 1 | 0 | 0 | 345.284 ms | 345.284 ms |
| read | 40/40 | 40 | 0 | 0 | 580.064 ms | 864.438 ms |
| return_plan | 12/12 | 12 | 0 | 0 | 0.328 ms | 0.516 ms |
| return_status | 12/12 | 12 | 0 | 0 | 0.282 ms | 0.338 ms |
| return_summary | 14/14 | 12 | 2 | 0 | 0.352 ms | 0.441 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 26.476% | 189.365% | 110.250 s | 515.488 MB | 579.250 MB | 0.464844 MB | 0.687500 MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python3 | 143037 |  | 4056 | 5.423% | 115.889% | 22.660 s | 692.259 MB | 711.406 MB | 3921.070 MB | 3976.641 MB | 19.289062 MB | 35.644531 MB |
| git-remote-http | 143045 |  | 5 | 9.886% | 29.643% | 0.040 s | 18.961 MB | 19.012 MB | 106.966 MB | 107.566 MB | 0.332031 MB | 0.000000 MB |
| git | 143043 |  | 5 | 0.000% | 0.000% | 0.000 s | 4.793 MB | 4.793 MB | 12.516 MB | 12.516 MB | 0.000000 MB | 0.000000 MB |
| git | 143044 |  | 5 | 0.000% | 0.000% | 0.000 s | 3.387 MB | 3.387 MB | 11.273 MB | 11.273 MB | 0.000000 MB | 0.000000 MB |
| python3 | 143051 |  | 99 | 99.888% | 109.050% | 9.880 s | 33.824 MB | 34.148 MB | 56.205 MB | 56.461 MB | 0.312500 MB | 0.015625 MB |
| python3 | 143052 |  | 4 | 102.324% | 108.937% | 0.310 s | 29.750 MB | 35.164 MB | 52.877 MB | 57.512 MB | 0.000000 MB | 0.281250 MB |
| python3 | 143053 |  | 4 | 102.331% | 108.872% | 0.310 s | 28.667 MB | 36.480 MB | 52.322 MB | 59.520 MB | 0.000000 MB | 0.285156 MB |
| python3 | 143054 |  | 4 | 99.030% | 108.981% | 0.300 s | 23.045 MB | 34.371 MB | 48.162 MB | 57.465 MB | 0.000000 MB | 0.015625 MB |
| python3 | 143055 |  | 25 | 99.445% | 108.973% | 2.410 s | 33.480 MB | 34.945 MB | 56.677 MB | 57.512 MB | 0.000000 MB | 0.289062 MB |
| python3 | 143056 |  | 70 | 100.022% | 108.973% | 6.970 s | 41.615 MB | 47.441 MB | 64.675 MB | 70.648 MB | 0.000000 MB | 0.289062 MB |
| python3 | 143058 |  | 5 | 99.028% | 99.125% | 0.400 s | 26.413 MB | 35.355 MB | 50.220 MB | 57.762 MB | 0.000000 MB | 0.289062 MB |
| python3 | 143059 |  | 99 | 99.828% | 109.057% | 9.890 s | 34.173 MB | 34.453 MB | 57.221 MB | 57.465 MB | 0.000000 MB | 0.015625 MB |
| python3 | 143060 |  | 4 | 99.029% | 99.112% | 0.300 s | 25.955 MB | 35.008 MB | 49.755 MB | 57.465 MB | 0.000000 MB | 0.296875 MB |
| python3 | 143061 |  | 4 | 102.245% | 108.681% | 0.310 s | 29.486 MB | 35.105 MB | 52.784 MB | 57.496 MB | 0.000000 MB | 0.296875 MB |
| python3 | 143062 |  | 4 | 102.299% | 108.929% | 0.310 s | 27.833 MB | 34.988 MB | 51.432 MB | 57.512 MB | 0.000000 MB | 0.296875 MB |
| python3 | 143063 |  | 4 | 102.296% | 108.975% | 0.310 s | 24.544 MB | 34.352 MB | 48.627 MB | 57.465 MB | 0.000000 MB | 0.015625 MB |
| docker | 143092 |  | 1 | n/a% | n/a% | n/a s | 9.238 MB | 9.238 MB | 1315.695 MB | 1315.695 MB | n/a MB | n/a MB |
| docker | 143108 |  | 1 | n/a% | n/a% | n/a s | 26.012 MB | 26.012 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 143133 |  | 1 | n/a% | n/a% | n/a s | 3.672 MB | 3.672 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 143134 |  | 1 | n/a% | n/a% | n/a s | 5.047 MB | 5.047 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 143157 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.155 MB | 27.355 MB | 1709.026 MB | 1805.031 MB | 0.000000 MB | 0.000000 MB |
| docker | 143159 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.172 MB | 27.461 MB | 1684.775 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 143242 | alex_0000 | 6 | 5.810% | 29.049% | 0.030 s | 2.264 MB | 10.422 MB | 250.411 MB | 1497.191 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 143240 | andy_0000 | 6 | 5.810% | 29.049% | 0.030 s | 2.316 MB | 10.734 MB | 274.495 MB | 1641.699 MB | n/a MB | n/a MB |
| tail | 143266 | alex_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 143274 |  | 1 | n/a% | n/a% | n/a s | 9.359 MB | 9.359 MB | 1443.695 MB | 1443.695 MB | n/a MB | n/a MB |
| tail | 143265 | andy_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 143268 |  | 1 | n/a% | n/a% | n/a s | 20.938 MB | 20.938 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 143321 |  | 1 | n/a% | n/a% | n/a s | 25.633 MB | 25.633 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 143327 |  | 1 | n/a% | n/a% | n/a s | 18.234 MB | 18.234 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 143380 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.906 MB | 11.906 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 143373 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.836 MB | 11.836 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 143341 |  | 1 | n/a% | n/a% | n/a s | 27.086 MB | 27.086 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 143338 |  | 1 | n/a% | n/a% | n/a s | 27.055 MB | 27.055 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 143395 |  | 1 | n/a% | n/a% | n/a s | 27.461 MB | 27.461 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 143393 |  | 1 | n/a% | n/a% | n/a s | 27.625 MB | 27.625 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 143438 | andy_0000 | 1 | n/a% | n/a% | n/a s | 12.250 MB | 12.250 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 143462 |  | 1 | n/a% | n/a% | n/a s | 27.207 MB | 27.207 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 143504 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.828 MB | 11.828 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 143464 |  | 1 | n/a% | n/a% | n/a s | 27.316 MB | 27.316 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 143501 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.863 MB | 11.863 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 143535 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.051 MB | 26.051 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 143537 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.582 MB | 25.582 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 143656 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.613 MB | 25.613 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 143654 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.645 MB | 25.645 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 143740 | andy_0000 | 5 | 4.758% | 19.031% | 0.020 s | 2.912 MB | 12.027 MB | 314.889 MB | 1570.227 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 143733 | alex_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.085 MB | 12.895 MB | 315.039 MB | 1570.977 MB | n/a MB | n/a MB |
| tail | 143761 | alex_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| tail | 143762 | andy_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 143784 |  | 1 | n/a% | n/a% | n/a s | 15.457 MB | 15.457 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 143782 |  | 1 | n/a% | n/a% | n/a s | 21.344 MB | 21.344 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 143835 |  | 1 | n/a% | n/a% | n/a s | 22.469 MB | 22.469 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 143837 |  | 1 | n/a% | n/a% | n/a s | 25.855 MB | 25.855 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 143894 |  | 1 | n/a% | n/a% | n/a s | 25.770 MB | 25.770 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 143903 |  | 1 | n/a% | n/a% | n/a s | 8.680 MB | 8.680 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 143960 |  | 1 | n/a% | n/a% | n/a s | 2.531 MB | 2.531 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 143976 |  | 1 | n/a% | n/a% | n/a s | 26.102 MB | 26.102 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 143978 |  | 1 | n/a% | n/a% | n/a s | 25.895 MB | 25.895 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 144062 |  | 1 | n/a% | n/a% | n/a s | 26.219 MB | 26.219 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 144086 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.672 MB | 26.672 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 144124 | andy_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.693 MB | 13.074 MB | 411.411 MB | 1642.480 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 144170 | andy_0000 | 1 | n/a% | n/a% | n/a s | 12.109 MB | 12.109 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 144140 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 144150 |  | 1 | n/a% | n/a% | n/a s | 27.328 MB | 27.328 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 144212 |  | 1 | n/a% | n/a% | n/a s | 6.641 MB | 6.641 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 144249 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.180 MB | 26.180 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 144302 |  | 1 | n/a% | n/a% | n/a s | 2.621 MB | 2.621 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 144350 | alex_0000 | 3 | 9.766% | 19.532% | 0.020 s | 3.931 MB | 10.527 MB | 523.768 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 144310 |  | 1 | n/a% | n/a% | n/a s | 26.949 MB | 26.949 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 144374 |  | 1 | n/a% | n/a% | n/a s | 0.414 MB | 0.414 MB | 30.578 MB | 30.578 MB | n/a MB | n/a MB |
| tail | 144363 | alex_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 144420 | alex_0000 | 1 | n/a% | n/a% | n/a s | 10.566 MB | 10.566 MB | 1641.449 MB | 1641.449 MB | n/a MB | n/a MB |
| docker | 144401 |  | 1 | n/a% | n/a% | n/a s | 27.266 MB | 27.266 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 144443 |  | 1 | n/a% | n/a% | n/a s | 26.945 MB | 26.945 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 144486 |  | 1 | n/a% | n/a% | n/a s | 26.211 MB | 26.211 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 144503 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.773 MB | 26.773 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 144543 | alex_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.743 MB | 13.074 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 144580 |  | 1 | n/a% | n/a% | n/a s | 27.371 MB | 27.371 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| tail | 144556 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.691 MB | 1.691 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 144591 |  | 1 | n/a% | n/a% | n/a s | 25.812 MB | 25.812 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 144613 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.305 MB | 11.305 MB | 1569.961 MB | 1569.961 MB | n/a MB | n/a MB |
| docker | 144626 |  | 40 | 0.000% | 0.000% | 0.000 s | 25.402 MB | 25.402 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 144634 |  | 1 | n/a% | n/a% | n/a s | 27.469 MB | 27.469 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 144655 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.699 MB | 11.699 MB | 1498.223 MB | 1498.223 MB | n/a MB | n/a MB |
| docker | 144671 |  | 1 | n/a% | n/a% | n/a s | 27.418 MB | 27.418 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 144707 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.848 MB | 25.848 MB | 1659.961 MB | 1659.961 MB | 0.000000 MB | 0.000000 MB |
| docker | 144792 |  | 1 | n/a% | n/a% | n/a s | 27.074 MB | 27.074 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 144844 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 144846 |  | 1 | n/a% | n/a% | n/a s | 18.188 MB | 18.188 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker-init | 144831 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 144882 |  | 1 | n/a% | n/a% | n/a s | 27.500 MB | 27.500 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 144920 |  | 1 | n/a% | n/a% | n/a s | 27.391 MB | 27.391 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 144942 | andy_0000 | 1 | n/a% | n/a% | n/a s | 6.570 MB | 6.570 MB | 1432.941 MB | 1432.941 MB | n/a MB | n/a MB |
| docker | 144959 |  | 1 | n/a% | n/a% | n/a s | 25.816 MB | 25.816 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 145001 |  | 1 | n/a% | n/a% | n/a s | 6.219 MB | 6.219 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 145018 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.414 MB | 25.414 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 145058 | andy_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.761 MB | 13.039 MB | 143.729 MB | 1570.477 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 145099 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.598 MB | 11.598 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 145070 | andy_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 145080 |  | 1 | n/a% | n/a% | n/a s | 27.402 MB | 27.402 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| bash | 145125 | andy_0000 | 9 | 0.000% | 0.000% | 0.000 s | 3.328 MB | 3.328 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 145106 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.332 MB | 27.332 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 145134 | andy_0000 | 9 | 100.379% | 107.857% | 0.820 s | 31.310 MB | 41.945 MB | 38.394 MB | 52.238 MB | n/a MB | n/a MB |
| docker | 145144 |  | 1 | n/a% | n/a% | n/a s | 27.008 MB | 27.008 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 145187 |  | 1 | n/a% | n/a% | n/a s | 18.289 MB | 18.289 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 145205 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.719 MB | 26.719 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 145244 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 145257 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 145294 |  | 1 | n/a% | n/a% | n/a s | 9.117 MB | 9.117 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 145329 |  | 1 | n/a% | n/a% | n/a s | 27.438 MB | 27.438 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 145365 |  | 1 | n/a% | n/a% | n/a s | 25.914 MB | 25.914 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 145406 |  | 1 | n/a% | n/a% | n/a s | 19.934 MB | 19.934 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 145423 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 145447 |  | 47 | 0.000% | 0.000% | 0.000 s | 25.652 MB | 25.652 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 145464 |  | 1 | n/a% | n/a% | n/a s | 22.336 MB | 22.336 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 145488 |  | 48 | 0.000% | 0.000% | 0.000 s | 25.891 MB | 25.891 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 145504 |  | 1 | n/a% | n/a% | n/a s | 23.414 MB | 23.414 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 145522 |  | 1 | n/a% | n/a% | n/a s | 25.828 MB | 25.828 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| python3 | 145538 |  | 7 | 96.479% | 107.845% | 0.590 s | 25.365 MB | 34.828 MB | 49.834 MB | 57.441 MB | 0.000000 MB | 0.281250 MB |
| docker | 145568 |  | 1 | n/a% | n/a% | n/a s | 26.004 MB | 26.004 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 145584 |  | 1 | n/a% | n/a% | n/a s | 25.465 MB | 25.465 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 145618 |  | 3 | 4.939% | 9.878% | 0.010 s | 23.350 MB | 27.242 MB | 1660.501 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 145660 | arch_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.742 MB | 13.070 MB | 393.473 MB | 1570.727 MB | n/a MB | n/a MB |
| tail | 145672 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 145701 |  | 1 | n/a% | n/a% | n/a s | 20.324 MB | 20.324 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 145735 |  | 1 | n/a% | n/a% | n/a s | 27.066 MB | 27.066 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 145771 |  | 1 | n/a% | n/a% | n/a s | 27.227 MB | 27.227 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 145791 | arch_0000 | 1 | n/a% | n/a% | n/a s | 11.773 MB | 11.773 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 145818 |  | 1 | n/a% | n/a% | n/a s | 26.012 MB | 26.012 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 145820 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.855 MB | 25.855 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 145894 | alex_0000 | 5 | 2.342% | 9.367% | 0.010 s | 3.008 MB | 12.508 MB | 300.438 MB | 1497.973 MB | n/a MB | n/a MB |
| docker | 145907 |  | 1 | n/a% | n/a% | n/a s | 4.168 MB | 4.168 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 145948 |  | 1 | n/a% | n/a% | n/a s | 27.172 MB | 27.172 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 145937 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.770 MB | 25.770 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| tail | 145924 | alex_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 146017 |  | 1 | n/a% | n/a% | n/a s | 27.117 MB | 27.117 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 146010 | arch_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.090 MB | 12.918 MB | 314.889 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 146049 | arch_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 146064 |  | 1 | n/a% | n/a% | n/a s | 27.273 MB | 27.273 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 146077 |  | 2 | 16.735% | 16.735% | 0.020 s | 13.621 MB | 27.242 MB | 845.672 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 146146 | arch_0000 | 1 | n/a% | n/a% | n/a s | 3.676 MB | 3.676 MB | 1208.676 MB | 1208.676 MB | n/a MB | n/a MB |
| docker | 146123 |  | 1 | n/a% | n/a% | n/a s | 27.102 MB | 27.102 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| sh | 146115 | alex_0000 | 1 | n/a% | n/a% | n/a s | 1.766 MB | 1.766 MB | 2.617 MB | 2.617 MB | n/a MB | n/a MB |
| docker | 146186 |  | 1 | n/a% | n/a% | n/a s | 20.500 MB | 20.500 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 146164 |  | 1 | n/a% | n/a% | n/a s | 25.992 MB | 25.992 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 146247 |  | 1 | n/a% | n/a% | n/a s | 22.160 MB | 22.160 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 146256 |  | 2 | 9.413% | 9.413% | 0.010 s | 14.059 MB | 25.859 MB | 846.486 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| run4:repair_bug | 146306 |  | 1 | n/a% | n/a% | n/a s | 680.781 MB | 680.781 MB | 3967.781 MB | 3967.781 MB | n/a MB | n/a MB |
| docker | 146314 |  | 4 | 15.243% | 45.730% | 0.050 s | 20.173 MB | 26.711 MB | 1253.768 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 146353 | alex_0000 | 15 | 3.932% | 55.054% | 0.060 s | 2.111 MB | 13.000 MB | 219.876 MB | 1642.730 MB | n/a MB | n/a MB |
| tail | 146368 | alex_0000 | 13 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 146370 |  | 1 | n/a% | n/a% | n/a s | 14.383 MB | 14.383 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 146397 | alex_0000 | 1 | n/a% | n/a% | n/a s | 10.875 MB | 10.875 MB | 1569.445 MB | 1569.445 MB | n/a MB | n/a MB |
| docker | 146378 |  | 1 | n/a% | n/a% | n/a s | 26.980 MB | 26.980 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 146424 | alex_0000 | 10 | 5.410% | 48.686% | 0.050 s | 3.520 MB | 4.371 MB | 148.071 MB | 1441.195 MB | n/a MB | n/a MB |
| docker | 146404 |  | 10 | 0.000% | 0.000% | 0.000 s | 26.914 MB | 26.914 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 146434 | alex_0000 | 9 | 100.251% | 107.851% | 0.820 s | 30.257 MB | 42.766 MB | 37.054 MB | 52.238 MB | n/a MB | n/a MB |
| docker | 146444 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.957 MB | 25.957 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 146503 |  | 2 | 9.879% | 9.879% | 0.010 s | 26.664 MB | 26.977 MB | 1660.492 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 146543 | alex_0000 | 4 | 3.250% | 9.750% | 0.010 s | 3.743 MB | 13.074 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 146586 | alex_0000 | 1 | n/a% | n/a% | n/a s | 10.812 MB | 10.812 MB | 1569.711 MB | 1569.711 MB | n/a MB | n/a MB |
| tail | 146555 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 146566 |  | 1 | n/a% | n/a% | n/a s | 27.273 MB | 27.273 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 146623 |  | 1 | n/a% | n/a% | n/a s | 4.477 MB | 4.477 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 146659 |  | 1 | n/a% | n/a% | n/a s | 12.801 MB | 12.801 MB | 1451.699 MB | 1451.699 MB | n/a MB | n/a MB |
| docker | 146668 |  | 1 | n/a% | n/a% | n/a s | 26.902 MB | 26.902 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 146753 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.223 MB | 25.223 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 146777 |  | 1 | n/a% | n/a% | n/a s | 2.406 MB | 2.406 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| python3 | 146800 |  | 4 | 98.816% | 108.791% | 0.300 s | 28.708 MB | 34.789 MB | 52.146 MB | 57.469 MB | 0.000000 MB | 0.257812 MB |
| docker | 146826 |  | 1 | n/a% | n/a% | n/a s | 26.578 MB | 26.578 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| docker | 146851 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.383 MB | 27.543 MB | 1756.779 MB | 1804.781 MB | 0.000000 MB | 0.000000 MB |
| docker | 146917 |  | 1 | n/a% | n/a% | n/a s | 25.598 MB | 25.598 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 146895 | bake_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.711 MB | 13.102 MB | 274.667 MB | 1642.730 MB | n/a MB | n/a MB |
| tail | 146935 | bake_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.809 MB | 1.809 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 146967 |  | 1 | n/a% | n/a% | n/a s | 11.809 MB | 11.809 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 146938 |  | 43 | 0.000% | 0.000% | 0.000 s | 25.746 MB | 25.746 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 146940 |  | 1 | n/a% | n/a% | n/a s | 26.930 MB | 26.930 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 146983 |  | 1 | n/a% | n/a% | n/a s | 25.906 MB | 25.906 MB | 1659.961 MB | 1659.961 MB | n/a MB | n/a MB |
| docker | 147010 |  | 1 | n/a% | n/a% | n/a s | 27.328 MB | 27.328 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 147047 |  | 1 | n/a% | n/a% | n/a s | 27.480 MB | 27.480 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 147083 |  | 2 | 9.686% | 9.686% | 0.010 s | 13.688 MB | 26.000 MB | 846.486 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 147132 |  | 1 | n/a% | n/a% | n/a s | 15.688 MB | 15.688 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 147141 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.414 MB | 25.414 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 147183 | bake_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.091 MB | 12.922 MB | 329.290 MB | 1642.230 MB | n/a MB | n/a MB |
| docker | 147206 |  | 1 | n/a% | n/a% | n/a s | 27.223 MB | 27.223 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 147196 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 147232 |  | 1 | n/a% | n/a% | n/a s | 27.309 MB | 27.309 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 147268 |  | 1 | n/a% | n/a% | n/a s | 2.090 MB | 2.090 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 147296 |  | 1 | n/a% | n/a% | n/a s | 4.734 MB | 4.734 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 147304 |  | 1 | n/a% | n/a% | n/a s | 25.820 MB | 25.820 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 147343 |  | 1 | n/a% | n/a% | n/a s | 25.051 MB | 25.051 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 147360 |  | 1 | n/a% | n/a% | n/a s | 10.648 MB | 10.648 MB | 1323.949 MB | 1323.949 MB | n/a MB | n/a MB |
| docker | 147387 |  | 3 | 4.920% | 9.840% | 0.010 s | 19.229 MB | 25.891 MB | 1117.728 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 147403 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.977 MB | 26.977 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| tail | 147494 | arch_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.707 MB | 1.707 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 147464 | arch_0000 | 5 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 147481 | bake_0000 | 5 | 2.425% | 9.702% | 0.010 s | 3.074 MB | 12.840 MB | 314.939 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 147526 |  | 1 | n/a% | n/a% | n/a s | 26.816 MB | 26.816 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| docker | 147517 |  | 1 | n/a% | n/a% | n/a s | 27.066 MB | 27.066 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 147503 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 147545 | arch_0000 | 1 | n/a% | n/a% | n/a s | 10.723 MB | 10.723 MB | 1569.453 MB | 1569.453 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 147599 | arch_0000 | 1 | n/a% | n/a% | n/a s | 11.578 MB | 11.578 MB | 1570.090 MB | 1570.090 MB | n/a MB | n/a MB |
| docker | 147577 |  | 1 | n/a% | n/a% | n/a s | 27.422 MB | 27.422 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 147570 |  | 1 | n/a% | n/a% | n/a s | 27.316 MB | 27.316 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 147645 |  | 1 | n/a% | n/a% | n/a s | 25.824 MB | 25.824 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 147642 |  | 1 | n/a% | n/a% | n/a s | 27.277 MB | 27.277 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 147702 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 147704 |  | 1 | n/a% | n/a% | n/a s | 25.867 MB | 25.867 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 147719 |  | 1 | n/a% | n/a% | n/a s | 26.113 MB | 26.113 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 147721 |  | 1 | n/a% | n/a% | n/a s | 26.809 MB | 26.809 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 147828 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.754 MB | 26.879 MB | 1660.648 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 147867 | arch_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.761 MB | 13.047 MB | 143.752 MB | 1570.727 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 147909 | arch_0000 | 1 | n/a% | n/a% | n/a s | 11.547 MB | 11.547 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 147880 | arch_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 147890 |  | 1 | n/a% | n/a% | n/a s | 26.844 MB | 26.844 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 147916 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.371 MB | 27.371 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 147946 | arch_0000 | 8 | 100.235% | 117.817% | 0.730 s | 30.581 MB | 41.914 MB | 37.700 MB | 51.219 MB | n/a MB | n/a MB |
| bash | 147936 | arch_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.441 MB | 3.441 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 147956 |  | 1 | n/a% | n/a% | n/a s | 27.055 MB | 27.055 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 148013 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.535 MB | 25.535 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 148052 | arch_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.723 MB | 12.992 MB | 393.473 MB | 1570.727 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 148096 | arch_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| docker | 148075 |  | 1 | n/a% | n/a% | n/a s | 27.340 MB | 27.340 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| tail | 148065 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 148138 |  | 1 | n/a% | n/a% | n/a s | 18.234 MB | 18.234 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 148174 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.852 MB | 25.852 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 148253 |  | 1 | n/a% | n/a% | n/a s | 26.559 MB | 26.559 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 148261 |  | 49 | 0.000% | 0.000% | 0.000 s | 26.707 MB | 26.707 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 148285 |  | 1 | n/a% | n/a% | n/a s | 0.129 MB | 0.129 MB | 30.570 MB | 30.570 MB | n/a MB | n/a MB |
| docker | 148300 |  | 51 | 0.000% | 0.000% | 0.000 s | 25.312 MB | 25.312 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 148325 |  | 1 | n/a% | n/a% | n/a s | 25.742 MB | 25.742 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 148343 |  | 1 | n/a% | n/a% | n/a s | 25.961 MB | 25.961 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| python3 | 148350 |  | 7 | 94.707% | 98.729% | 0.580 s | 27.270 MB | 34.781 MB | 51.111 MB | 57.441 MB | 0.000000 MB | 0.285156 MB |
| docker | 148369 |  | 1 | n/a% | n/a% | n/a s | 26.129 MB | 26.129 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 148396 |  | 1 | n/a% | n/a% | n/a s | 26.477 MB | 26.477 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 148414 |  | 1 | n/a% | n/a% | n/a s | 15.289 MB | 15.289 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 148422 |  | 1 | n/a% | n/a% | n/a s | 26.746 MB | 26.746 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 148461 | bake_0000 | 5 | 7.345% | 29.379% | 0.030 s | 2.846 MB | 11.699 MB | 314.836 MB | 1569.961 MB | n/a MB | n/a MB |
| tail | 148473 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 148483 |  | 1 | n/a% | n/a% | n/a s | 27.246 MB | 27.246 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 148524 |  | 1 | n/a% | n/a% | n/a s | 27.320 MB | 27.320 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 148526 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.589 MB | 27.727 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 148553 | bake_0000 | 1 | n/a% | n/a% | n/a s | 4.246 MB | 4.246 MB | 1216.680 MB | 1216.680 MB | n/a MB | n/a MB |
| docker | 148569 |  | 1 | n/a% | n/a% | n/a s | 27.102 MB | 27.102 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 148628 | bale_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.134 MB | 13.141 MB | 314.939 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 148638 |  | 1 | n/a% | n/a% | n/a s | 25.730 MB | 25.730 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 148662 |  | 1 | n/a% | n/a% | n/a s | 27.000 MB | 27.000 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 148704 |  | 1 | n/a% | n/a% | n/a s | 10.773 MB | 10.773 MB | 1569.711 MB | 1569.711 MB | n/a MB | n/a MB |
| docker | 148647 |  | 1 | n/a% | n/a% | n/a s | 26.941 MB | 26.941 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 148660 | bale_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 148740 |  | 1 | n/a% | n/a% | n/a s | 27.305 MB | 27.305 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 148797 |  | 1 | n/a% | n/a% | n/a s | 5.016 MB | 5.016 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 148843 |  | 2 | 9.791% | 9.791% | 0.010 s | 14.037 MB | 26.293 MB | 846.486 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 148902 |  | 2 | 9.851% | 9.851% | 0.010 s | 24.916 MB | 26.660 MB | 1624.488 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 148941 | bale_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.709 MB | 12.938 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 148963 |  | 1 | n/a% | n/a% | n/a s | 27.359 MB | 27.359 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 148983 | bale_0000 | 1 | n/a% | n/a% | n/a s | 11.402 MB | 11.402 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 148953 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 149019 |  | 1 | n/a% | n/a% | n/a s | 26.980 MB | 26.980 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 149064 |  | 2 | 0.000% | 0.000% | 0.000 s | 24.863 MB | 25.945 MB | 1624.207 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 149123 |  | 2 | 9.444% | 9.444% | 0.010 s | 25.506 MB | 26.695 MB | 1660.492 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 149163 | bake_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.751 MB | 12.930 MB | 143.729 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 149186 |  | 1 | n/a% | n/a% | n/a s | 27.324 MB | 27.324 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 149176 | bake_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 149206 | bake_0000 | 1 | n/a% | n/a% | n/a s | 12.008 MB | 12.008 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| python | 149240 | bake_0000 | 9 | 100.223% | 107.869% | 0.820 s | 31.474 MB | 41.832 MB | 38.414 MB | 51.375 MB | n/a MB | n/a MB |
| docker | 149213 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.352 MB | 27.352 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| bash | 149232 | bake_0000 | 9 | 0.000% | 0.000% | 0.000 s | 3.395 MB | 3.395 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 149251 |  | 1 | n/a% | n/a% | n/a s | 25.953 MB | 25.953 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 149347 | bake_0000 | 4 | 6.446% | 19.337% | 0.020 s | 3.237 MB | 11.051 MB | 393.277 MB | 1569.945 MB | n/a MB | n/a MB |
| docker | 149309 |  | 1 | n/a% | n/a% | n/a s | 26.590 MB | 26.590 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 149371 |  | 1 | n/a% | n/a% | n/a s | 19.598 MB | 19.598 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| tail | 149360 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 149398 |  | 1 | n/a% | n/a% | n/a s | 26.953 MB | 26.953 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 149418 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.555 MB | 11.555 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 149433 |  | 1 | n/a% | n/a% | n/a s | 27.391 MB | 27.391 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 149452 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.523 MB | 11.523 MB | 1642.230 MB | 1642.230 MB | n/a MB | n/a MB |
| docker | 149469 |  | 1 | n/a% | n/a% | n/a s | 26.000 MB | 26.000 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 149537 |  | 1 | n/a% | n/a% | n/a s | 6.344 MB | 6.344 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 149555 |  | 54 | 0.000% | 0.000% | 0.000 s | 27.012 MB | 27.012 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 149581 |  | 1 | n/a% | n/a% | n/a s | 22.539 MB | 22.539 MB | 1524.203 MB | 1524.203 MB | n/a MB | n/a MB |
| python3 | 149605 |  | 4 | 98.766% | 98.939% | 0.300 s | 28.784 MB | 34.547 MB | 52.458 MB | 57.441 MB | 0.000000 MB | 0.281250 MB |
| docker | 149623 |  | 1 | n/a% | n/a% | n/a s | 26.227 MB | 26.227 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 149639 |  | 1 | n/a% | n/a% | n/a s | 2.219 MB | 2.219 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 149671 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.344 MB | 25.344 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 149713 |  | 1 | n/a% | n/a% | n/a s | 26.922 MB | 26.922 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 149727 |  | 2 | 9.878% | 9.878% | 0.010 s | 27.334 MB | 27.488 MB | 1732.777 MB | 1804.781 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 149770 | band_0000 | 5 | 2.460% | 9.841% | 0.010 s | 2.972 MB | 12.328 MB | 314.939 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 149784 |  | 1 | n/a% | n/a% | n/a s | 27.090 MB | 27.090 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 149803 |  | 1 | n/a% | n/a% | n/a s | 11.859 MB | 11.859 MB | 1570.977 MB | 1570.977 MB | n/a MB | n/a MB |
| tail | 149782 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 149818 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 149882 |  | 1 | n/a% | n/a% | n/a s | 22.566 MB | 22.566 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 149918 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.945 MB | 25.945 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 149975 |  | 1 | n/a% | n/a% | n/a s | 27.094 MB | 27.094 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 150030 |  | 1 | n/a% | n/a% | n/a s | 2.664 MB | 2.664 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker-init | 150015 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 150027 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 150066 |  | 1 | n/a% | n/a% | n/a s | 25.504 MB | 25.504 MB | 1596.211 MB | 1596.211 MB | n/a MB | n/a MB |
| docker | 150102 |  | 1 | n/a% | n/a% | n/a s | 27.109 MB | 27.109 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 150139 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.070 MB | 27.070 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 150198 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.113 MB | 27.113 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| tail | 150250 | bale_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 150237 | bale_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 150286 |  | 1 | n/a% | n/a% | n/a s | 9.461 MB | 9.461 MB | 1323.699 MB | 1323.699 MB | n/a MB | n/a MB |
| docker | 150324 |  | 1 | n/a% | n/a% | n/a s | 26.859 MB | 26.859 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 150361 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.137 MB | 27.137 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 150420 |  | 1 | n/a% | n/a% | n/a s | 26.398 MB | 26.398 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker-init | 150461 | bale_0000 | 37 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 150474 | bale_0000 | 37 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 150476 |  | 1 | n/a% | n/a% | n/a s | 4.836 MB | 4.836 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 150511 |  | 36 | 0.556% | 19.473% | 0.020 s | 27.315 MB | 27.359 MB | 1660.760 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| bash | 150531 | bale_0000 | 35 | 0.000% | 0.000% | 0.000 s | 3.449 MB | 3.449 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 150541 | bale_0000 | 35 | 99.776% | 117.788% | 3.460 s | 39.573 MB | 41.824 MB | 48.493 MB | 51.324 MB | n/a MB | n/a MB |
| docker | 150551 |  | 1 | n/a% | n/a% | n/a s | 25.703 MB | 25.703 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 150597 |  | 1 | n/a% | n/a% | n/a s | 6.516 MB | 6.516 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 150606 |  | 1 | n/a% | n/a% | n/a s | 11.148 MB | 11.148 MB | 1451.949 MB | 1451.949 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 150653 | bale_0000 | 4 | 9.724% | 29.172% | 0.030 s | 3.226 MB | 11.285 MB | 393.152 MB | 1569.445 MB | n/a MB | n/a MB |
| docker | 150614 |  | 1 | n/a% | n/a% | n/a s | 26.754 MB | 26.754 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 150677 |  | 1 | n/a% | n/a% | n/a s | 22.785 MB | 22.785 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| tail | 150667 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.809 MB | 1.809 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 150724 | bale_0000 | 1 | n/a% | n/a% | n/a s | 11.863 MB | 11.863 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 150704 |  | 1 | n/a% | n/a% | n/a s | 26.984 MB | 26.984 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 150760 | bale_0000 | 1 | n/a% | n/a% | n/a s | 12.199 MB | 12.199 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 150740 |  | 1 | n/a% | n/a% | n/a s | 27.320 MB | 27.320 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 150777 |  | 1 | n/a% | n/a% | n/a s | 25.887 MB | 25.887 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 150853 |  | 1 | n/a% | n/a% | n/a s | 9.363 MB | 9.363 MB | 1379.695 MB | 1379.695 MB | n/a MB | n/a MB |
| docker | 150861 |  | 39 | 0.000% | 0.000% | 0.000 s | 26.395 MB | 26.395 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 150886 |  | 1 | n/a% | n/a% | n/a s | 16.344 MB | 16.344 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| python3 | 150909 |  | 24 | 100.200% | 108.872% | 2.330 s | 33.174 MB | 34.016 MB | 56.643 MB | 57.469 MB | 0.000000 MB | 0.000000 MB |
| docker | 150911 |  | 1 | n/a% | n/a% | n/a s | 10.512 MB | 10.512 MB | 1451.699 MB | 1451.699 MB | n/a MB | n/a MB |
| docker | 150938 |  | 1 | n/a% | n/a% | n/a s | 25.469 MB | 25.469 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 150966 |  | 1 | n/a% | n/a% | n/a s | 25.461 MB | 25.461 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 150981 |  | 45 | 0.000% | 0.000% | 0.000 s | 25.159 MB | 25.730 MB | 1623.317 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 150989 |  | 1 | n/a% | n/a% | n/a s | 17.875 MB | 17.875 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 151003 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.221 MB | 27.348 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 151043 | bart_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.723 MB | 13.172 MB | 262.667 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 151057 |  | 1 | n/a% | n/a% | n/a s | 27.375 MB | 27.375 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 151076 |  | 1 | n/a% | n/a% | n/a s | 11.730 MB | 11.730 MB | 1642.223 MB | 1642.223 MB | n/a MB | n/a MB |
| tail | 151055 | bart_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 151092 |  | 1 | n/a% | n/a% | n/a s | 27.500 MB | 27.500 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 151176 | bart_0000 | 1 | n/a% | n/a% | n/a s | 11.961 MB | 11.961 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 151154 |  | 1 | n/a% | n/a% | n/a s | 27.340 MB | 27.340 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 151193 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.758 MB | 25.758 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 151254 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.527 MB | 25.527 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 151294 | bart_0000 | 6 | 7.806% | 39.031% | 0.040 s | 2.496 MB | 11.812 MB | 274.580 MB | 1642.207 MB | n/a MB | n/a MB |
| docker | 151311 |  | 1 | n/a% | n/a% | n/a s | 23.906 MB | 23.906 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| tail | 151307 | bart_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 151320 |  | 1 | n/a% | n/a% | n/a s | 27.398 MB | 27.398 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 151338 | bart_0000 | 1 | n/a% | n/a% | n/a s | 12.023 MB | 12.023 MB | 1642.980 MB | 1642.980 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 151364 | bart_0000 | 1 | n/a% | n/a% | n/a s | 11.949 MB | 11.949 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 151346 |  | 1 | n/a% | n/a% | n/a s | 27.285 MB | 27.285 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 151401 | bart_0000 | 1 | n/a% | n/a% | n/a s | 4.367 MB | 4.367 MB | 1344.680 MB | 1344.680 MB | n/a MB | n/a MB |
| docker | 151381 |  | 1 | n/a% | n/a% | n/a s | 27.453 MB | 27.453 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 151417 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.000 MB | 26.000 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 151505 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.156 MB | 27.156 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 151544 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.766 MB | 13.164 MB | 393.473 MB | 1570.727 MB | n/a MB | n/a MB |
| tail | 151556 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 151566 |  | 1 | n/a% | n/a% | n/a s | 27.156 MB | 27.156 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 151587 | band_0000 | 1 | n/a% | n/a% | n/a s | 12.547 MB | 12.547 MB | 1570.977 MB | 1570.977 MB | n/a MB | n/a MB |
| docker | 151632 |  | 1 | n/a% | n/a% | n/a s | 9.156 MB | 9.156 MB | 1235.438 MB | 1235.438 MB | n/a MB | n/a MB |
| docker | 151670 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.887 MB | 25.887 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 151728 |  | 1 | n/a% | n/a% | n/a s | 25.828 MB | 25.828 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 151783 |  | 1 | n/a% | n/a% | n/a s | 25.863 MB | 25.863 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 151781 | band_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 151769 | band_0000 | 11 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 151818 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.112 MB | 27.223 MB | 1661.023 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| bash | 151839 | band_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.324 MB | 3.324 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 151848 | band_0000 | 8 | 100.744% | 107.846% | 0.720 s | 32.380 MB | 41.930 MB | 39.451 MB | 51.324 MB | n/a MB | n/a MB |
| docker | 151858 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.176 MB | 26.176 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 151916 |  | 2 | 9.862% | 9.862% | 0.010 s | 24.330 MB | 26.953 MB | 1588.486 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 151957 | bart_0000 | 3 | 4.908% | 9.816% | 0.010 s | 4.516 MB | 12.281 MB | 524.112 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 151971 | bart_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.723 MB | 1.723 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 151981 |  | 1 | n/a% | n/a% | n/a s | 27.438 MB | 27.438 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 152003 | bart_0000 | 1 | n/a% | n/a% | n/a s | 10.656 MB | 10.656 MB | 1569.695 MB | 1569.695 MB | n/a MB | n/a MB |
| docker | 152010 |  | 1 | n/a% | n/a% | n/a s | 27.395 MB | 27.395 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 152051 |  | 1 | n/a% | n/a% | n/a s | 27.188 MB | 27.188 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 152111 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.719 MB | 26.719 MB | 1660.523 MB | 1660.523 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 152153 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 4.747 MB | 12.977 MB | 524.195 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 152165 | bart_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 152175 |  | 1 | n/a% | n/a% | n/a s | 27.020 MB | 27.020 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 152195 | bart_0000 | 1 | n/a% | n/a% | n/a s | 11.988 MB | 11.988 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 152246 |  | 2 | 19.555% | 19.555% | 0.020 s | 17.748 MB | 26.953 MB | 1444.041 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 152300 | band_0000 | 4 | 10.098% | 30.293% | 0.040 s | 3.254 MB | 11.117 MB | 393.090 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 152280 |  | 1 | n/a% | n/a% | n/a s | 27.102 MB | 27.102 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 152348 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 152367 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 30.570 MB | 30.570 MB | n/a MB | n/a MB |
| docker | 152394 |  | 1 | n/a% | n/a% | n/a s | 27.012 MB | 27.012 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 152429 |  | 1 | n/a% | n/a% | n/a s | 27.434 MB | 27.434 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 152448 | band_0000 | 1 | n/a% | n/a% | n/a s | 11.871 MB | 11.871 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 152465 |  | 1 | n/a% | n/a% | n/a s | 25.973 MB | 25.973 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 152517 |  | 1 | n/a% | n/a% | n/a s | 23.469 MB | 23.469 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 152525 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.641 MB | 26.641 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 152566 | bart_0000 | 8 | 5.562% | 38.931% | 0.040 s | 1.965 MB | 11.289 MB | 188.120 MB | 1497.578 MB | n/a MB | n/a MB |
| tail | 152578 | bart_0000 | 7 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 152588 |  | 1 | n/a% | n/a% | n/a s | 27.082 MB | 27.082 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 152616 |  | 2 | 39.072% | 39.072% | 0.040 s | 15.648 MB | 27.016 MB | 846.768 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 152636 | bart_0000 | 1 | n/a% | n/a% | n/a s | 11.492 MB | 11.492 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 152643 |  | 1 | n/a% | n/a% | n/a s | 25.242 MB | 25.242 MB | 1596.211 MB | 1596.211 MB | n/a MB | n/a MB |
| docker | 152651 |  | 1 | n/a% | n/a% | n/a s | 27.316 MB | 27.316 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 152687 |  | 3 | 0.000% | 0.000% | 0.000 s | 26.137 MB | 26.137 MB | 1659.961 MB | 1659.961 MB | 0.000000 MB | 0.000000 MB |
| docker | 152738 |  | 1 | n/a% | n/a% | n/a s | 8.789 MB | 8.789 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 152764 |  | 1 | n/a% | n/a% | n/a s | 25.965 MB | 25.965 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 152772 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.633 MB | 25.633 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 152797 |  | 1 | n/a% | n/a% | n/a s | 3.805 MB | 3.805 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 152813 |  | 1 | n/a% | n/a% | n/a s | 22.910 MB | 22.910 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| python3 | 152820 |  | 4 | 102.051% | 108.786% | 0.310 s | 27.321 MB | 34.559 MB | 51.063 MB | 57.441 MB | 0.000000 MB | 0.281250 MB |
| docker | 152838 |  | 1 | n/a% | n/a% | n/a s | 25.148 MB | 25.148 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 152873 |  | 2 | 9.846% | 9.846% | 0.010 s | 27.447 MB | 27.750 MB | 1696.775 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 152912 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 152924 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 152926 |  | 1 | n/a% | n/a% | n/a s | 22.414 MB | 22.414 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 152960 |  | 1 | n/a% | n/a% | n/a s | 27.434 MB | 27.434 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 152988 |  | 1 | n/a% | n/a% | n/a s | 27.484 MB | 27.484 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 153008 | base_0000 | 1 | n/a% | n/a% | n/a s | 12.547 MB | 12.547 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 153052 |  | 1 | n/a% | n/a% | n/a s | 8.547 MB | 8.547 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 153060 |  | 1 | n/a% | n/a% | n/a s | 25.887 MB | 25.887 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 153117 |  | 2 | 0.000% | 0.000% | 0.000 s | 22.883 MB | 25.410 MB | 1624.082 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 153157 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.659 MB | 12.738 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 153180 |  | 1 | n/a% | n/a% | n/a s | 27.379 MB | 27.379 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 153200 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.855 MB | 11.855 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 153169 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 153236 |  | 1 | n/a% | n/a% | n/a s | 20.609 MB | 20.609 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 153283 |  | 2 | 0.000% | 0.000% | 0.000 s | 15.994 MB | 26.969 MB | 846.768 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 153356 |  | 1 | n/a% | n/a% | n/a s | 26.797 MB | 26.797 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 153370 |  | 38 | 0.000% | 0.000% | 0.000 s | 27.027 MB | 27.027 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 153387 |  | 1 | n/a% | n/a% | n/a s | 25.641 MB | 25.641 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 153415 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.578 MB | 27.105 MB | 1660.492 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 153454 | bart_0000 | 4 | 3.238% | 9.715% | 0.010 s | 3.657 MB | 12.730 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 153466 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 153476 |  | 1 | n/a% | n/a% | n/a s | 26.930 MB | 26.930 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 153496 | bart_0000 | 1 | n/a% | n/a% | n/a s | 10.633 MB | 10.633 MB | 1569.582 MB | 1569.582 MB | n/a MB | n/a MB |
| docker | 153529 |  | 1 | n/a% | n/a% | n/a s | 4.410 MB | 4.410 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 153569 |  | 1 | n/a% | n/a% | n/a s | 21.023 MB | 21.023 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 153578 |  | 1 | n/a% | n/a% | n/a s | 26.867 MB | 26.867 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 153638 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.656 MB | 25.656 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 153679 | bart_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.741 MB | 12.828 MB | 143.707 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 153692 | bart_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 153723 | bart_0000 | 1 | n/a% | n/a% | n/a s | 11.449 MB | 11.449 MB | 1498.223 MB | 1498.223 MB | n/a MB | n/a MB |
| docker | 153703 |  | 1 | n/a% | n/a% | n/a s | 27.496 MB | 27.496 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| bash | 153749 | bart_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.273 MB | 3.273 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 153729 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.375 MB | 27.375 MB | 1661.023 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| python | 153758 | bart_0000 | 8 | 99.160% | 107.883% | 0.710 s | 30.609 MB | 41.805 MB | 37.916 MB | 51.324 MB | n/a MB | n/a MB |
| docker | 153769 |  | 2 | 0.000% | 0.000% | 0.000 s | 21.561 MB | 25.695 MB | 1587.955 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 153831 |  | 2 | 0.000% | 0.000% | 0.000 s | 22.508 MB | 26.906 MB | 1588.236 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 153870 | bart_0000 | 4 | 3.044% | 9.131% | 0.010 s | 3.635 MB | 12.641 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 153883 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 153894 |  | 1 | n/a% | n/a% | n/a s | 27.066 MB | 27.066 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 153914 | bart_0000 | 1 | n/a% | n/a% | n/a s | 11.773 MB | 11.773 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 153949 |  | 1 | n/a% | n/a% | n/a s | 20.289 MB | 20.289 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 153994 |  | 2 | 9.779% | 9.779% | 0.010 s | 15.668 MB | 27.168 MB | 846.768 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 154054 |  | 1 | n/a% | n/a% | n/a s | 8.719 MB | 8.719 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 154078 |  | 40 | 0.000% | 0.000% | 0.000 s | 26.844 MB | 26.844 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 154110 |  | 1 | n/a% | n/a% | n/a s | 26.859 MB | 26.859 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 154125 |  | 4 | 102.048% | 108.744% | 0.310 s | 24.724 MB | 34.496 MB | 48.690 MB | 57.441 MB | 0.000000 MB | 0.281250 MB |
| docker | 154135 |  | 1 | n/a% | n/a% | n/a s | 27.016 MB | 27.016 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 154191 |  | 39 | 0.259% | 9.829% | 0.010 s | 26.551 MB | 26.699 MB | 1657.272 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 154244 |  | 3 | 4.928% | 9.855% | 0.010 s | 18.953 MB | 27.461 MB | 1214.108 MB | 1804.781 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 154285 | beam_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.680 MB | 12.820 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 154297 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 154362 |  | 1 | n/a% | n/a% | n/a s | 25.645 MB | 25.645 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 154419 | beam_0000 | 1 | n/a% | n/a% | n/a s | 3.988 MB | 3.988 MB | 1208.676 MB | 1208.676 MB | n/a MB | n/a MB |
| docker | 154399 |  | 1 | n/a% | n/a% | n/a s | 27.730 MB | 27.730 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 154435 |  | 1 | n/a% | n/a% | n/a s | 26.766 MB | 26.766 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 154484 |  | 1 | n/a% | n/a% | n/a s | 4.043 MB | 4.043 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 154529 | beam_0000 | 4 | 9.755% | 29.264% | 0.030 s | 3.324 MB | 11.398 MB | 393.187 MB | 1569.582 MB | n/a MB | n/a MB |
| docker | 154493 |  | 1 | n/a% | n/a% | n/a s | 26.531 MB | 26.531 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 154555 |  | 1 | n/a% | n/a% | n/a s | 27.414 MB | 27.414 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 154545 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 154601 | beam_0000 | 1 | n/a% | n/a% | n/a s | 12.496 MB | 12.496 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 154581 |  | 1 | n/a% | n/a% | n/a s | 27.234 MB | 27.234 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 154655 |  | 1 | n/a% | n/a% | n/a s | 26.914 MB | 26.914 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 154705 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 30.570 MB | 30.570 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 154755 | base_0000 | 4 | 6.492% | 19.475% | 0.020 s | 3.149 MB | 10.699 MB | 375.089 MB | 1497.191 MB | n/a MB | n/a MB |
| docker | 154714 |  | 1 | n/a% | n/a% | n/a s | 27.012 MB | 27.012 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 154767 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 154777 |  | 1 | n/a% | n/a% | n/a s | 23.547 MB | 23.547 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 154824 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.363 MB | 11.363 MB | 1569.969 MB | 1569.969 MB | n/a MB | n/a MB |
| docker | 154805 |  | 1 | n/a% | n/a% | n/a s | 27.238 MB | 27.238 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 154860 | base_0000 | 1 | n/a% | n/a% | n/a s | 12.035 MB | 12.035 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 154840 |  | 1 | n/a% | n/a% | n/a s | 27.129 MB | 27.129 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 154879 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.023 MB | 27.023 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 154919 |  | 1 | n/a% | n/a% | n/a s | 20.246 MB | 20.246 MB | 1524.203 MB | 1524.203 MB | n/a MB | n/a MB |
| docker | 154936 |  | 3 | 9.777% | 19.555% | 0.020 s | 19.342 MB | 26.934 MB | 1118.103 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 154976 | base_0000 | 14 | 0.000% | 0.000% | 0.000 s | 1.515 MB | 12.980 MB | 113.156 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 154999 |  | 1 | n/a% | n/a% | n/a s | 18.156 MB | 18.156 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| tail | 154989 | base_0000 | 13 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 155028 |  | 11 | 0.000% | 0.000% | 0.000 s | 27.094 MB | 27.109 MB | 1661.023 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| python | 155056 | base_0000 | 10 | 99.867% | 107.804% | 0.920 s | 30.714 MB | 41.641 MB | 37.952 MB | 51.957 MB | n/a MB | n/a MB |
| bash | 155047 | base_0000 | 10 | 0.000% | 0.000% | 0.000 s | 3.273 MB | 3.273 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 155067 |  | 2 | 9.742% | 9.742% | 0.010 s | 15.812 MB | 27.031 MB | 846.768 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 155125 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.684 MB | 26.684 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 155164 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 155176 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 155212 |  | 1 | n/a% | n/a% | n/a s | 23.848 MB | 23.848 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 155249 |  | 1 | n/a% | n/a% | n/a s | 27.320 MB | 27.320 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 155288 |  | 1 | n/a% | n/a% | n/a s | 27.082 MB | 27.082 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 155329 |  | 1 | n/a% | n/a% | n/a s | 23.688 MB | 23.688 MB | 1524.203 MB | 1524.203 MB | n/a MB | n/a MB |
| docker | 155346 |  | 2 | 0.000% | 0.000% | 0.000 s | 17.238 MB | 25.758 MB | 1443.822 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 155385 | base_0000 | 4 | 6.535% | 19.605% | 0.020 s | 3.624 MB | 12.598 MB | 411.411 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 155408 |  | 1 | n/a% | n/a% | n/a s | 27.117 MB | 27.117 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 155398 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 155502 |  | 1 | n/a% | n/a% | n/a s | 14.453 MB | 14.453 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 155510 |  | 1 | n/a% | n/a% | n/a s | 25.980 MB | 25.980 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 155561 |  | 1 | n/a% | n/a% | n/a s | 16.387 MB | 16.387 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 155612 | base_0000 | 8 | 2.790% | 19.527% | 0.020 s | 1.955 MB | 11.211 MB | 197.104 MB | 1569.445 MB | n/a MB | n/a MB |
| docker | 155569 |  | 1 | n/a% | n/a% | n/a s | 25.707 MB | 25.707 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 155634 |  | 1 | n/a% | n/a% | n/a s | 18.414 MB | 18.414 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 155624 | base_0000 | 7 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 155682 | base_0000 | 5 | 4.857% | 19.429% | 0.020 s | 4.805 MB | 10.742 MB | 317.429 MB | 1569.582 MB | n/a MB | n/a MB |
| docker | 155661 |  | 5 | 0.000% | 0.000% | 0.000 s | 26.973 MB | 26.973 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| python | 155691 | base_0000 | 4 | 97.906% | 117.662% | 0.300 s | 26.517 MB | 34.797 MB | 33.779 MB | 45.023 MB | n/a MB | n/a MB |
| docker | 155701 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.859 MB | 25.859 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 155766 |  | 1 | n/a% | n/a% | n/a s | 25.469 MB | 25.469 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 155781 |  | 41 | 0.000% | 0.000% | 0.000 s | 26.941 MB | 26.941 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 155797 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.527 MB | 25.527 MB | 1588.207 MB | 1588.207 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 155836 | base_0000 | 6 | 7.794% | 38.971% | 0.040 s | 2.410 MB | 11.293 MB | 262.536 MB | 1569.945 MB | n/a MB | n/a MB |
| docker | 155853 |  | 1 | n/a% | n/a% | n/a s | 3.293 MB | 3.293 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| tail | 155849 | base_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 155882 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.957 MB | 11.957 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 155863 |  | 1 | n/a% | n/a% | n/a s | 27.352 MB | 27.352 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 155908 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.598 MB | 11.598 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 155890 |  | 1 | n/a% | n/a% | n/a s | 27.496 MB | 27.496 MB | 1733.027 MB | 1733.027 MB | n/a MB | n/a MB |
| docker | 155925 |  | 1 | n/a% | n/a% | n/a s | 27.633 MB | 27.633 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 155961 |  | 1 | n/a% | n/a% | n/a s | 25.762 MB | 25.762 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 155996 |  | 1 | n/a% | n/a% | n/a s | 9.281 MB | 9.281 MB | 1315.695 MB | 1315.695 MB | n/a MB | n/a MB |
| docker | 156040 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.297 MB | 26.297 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 156081 | beam_0000 | 4 | 3.248% | 9.745% | 0.010 s | 3.751 MB | 13.105 MB | 393.535 MB | 1570.977 MB | n/a MB | n/a MB |
| tail | 156093 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 156168 |  | 1 | n/a% | n/a% | n/a s | 21.520 MB | 21.520 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 156208 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.992 MB | 26.992 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 156296 |  | 48 | 0.000% | 0.000% | 0.000 s | 25.754 MB | 25.754 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 156304 |  | 1 | n/a% | n/a% | n/a s | 19.113 MB | 19.113 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 156313 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.094 MB | 27.094 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 156352 | beam_0000 | 18 | 0.574% | 9.757% | 0.010 s | 1.324 MB | 13.070 MB | 88.245 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 156374 |  | 1 | n/a% | n/a% | n/a s | 25.359 MB | 25.359 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 156364 | beam_0000 | 17 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 156399 |  | 15 | 0.680% | 9.516% | 0.010 s | 27.228 MB | 27.352 MB | 1660.736 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 156429 | beam_0000 | 14 | 96.637% | 106.385% | 1.330 s | 31.769 MB | 41.715 MB | 38.897 MB | 51.238 MB | n/a MB | n/a MB |
| bash | 156420 | beam_0000 | 14 | 0.000% | 0.000% | 0.000 s | 3.316 MB | 3.316 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 156439 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.969 MB | 26.969 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 156496 |  | 3 | 0.000% | 0.000% | 0.000 s | 25.527 MB | 25.527 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 156537 | beam_0000 | 5 | 7.142% | 28.566% | 0.030 s | 2.655 MB | 10.742 MB | 314.683 MB | 1569.195 MB | n/a MB | n/a MB |
| tail | 156549 | beam_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 156559 |  | 1 | n/a% | n/a% | n/a s | 26.934 MB | 26.934 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 156577 | beam_0000 | 1 | n/a% | n/a% | n/a s | 10.715 MB | 10.715 MB | 1569.445 MB | 1569.445 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 156648 | beam_0000 | 1 | n/a% | n/a% | n/a s | 11.586 MB | 11.586 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 156623 |  | 1 | n/a% | n/a% | n/a s | 27.215 MB | 27.215 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 156666 |  | 1 | n/a% | n/a% | n/a s | 25.965 MB | 25.965 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 156687 |  | 1 | n/a% | n/a% | n/a s | 6.512 MB | 6.512 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 156724 |  | 1 | n/a% | n/a% | n/a s | 10.395 MB | 10.395 MB | 1451.949 MB | 1451.949 MB | n/a MB | n/a MB |
| docker | 156702 |  | 1 | n/a% | n/a% | n/a s | 25.508 MB | 25.508 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| python3 | 156748 |  | 4 | 102.042% | 108.805% | 0.310 s | 29.181 MB | 34.848 MB | 52.523 MB | 57.441 MB | 0.000000 MB | 0.257812 MB |
| docker | 156768 |  | 1 | n/a% | n/a% | n/a s | 19.387 MB | 19.387 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 156812 |  | 1 | n/a% | n/a% | n/a s | 27.188 MB | 27.188 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 156820 |  | 46 | 0.000% | 0.000% | 0.000 s | 27.188 MB | 27.188 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 156828 |  | 1 | n/a% | n/a% | n/a s | 26.789 MB | 26.789 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 156842 |  | 3 | 0.000% | 0.000% | 0.000 s | 26.845 MB | 27.398 MB | 1660.586 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[0:PARENT] | 156878 |  | 1 | n/a% | n/a% | n/a s | 1.969 MB | 1.969 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| runc:[1:CHILD] | 156879 |  | 1 | n/a% | n/a% | n/a s | 0.793 MB | 0.793 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker-init | 156880 | bear_0000 | 6 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 156893 | bear_0000 | 6 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 156951 | bear_0000 | 1 | n/a% | n/a% | n/a s | 12.375 MB | 12.375 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 156933 |  | 1 | n/a% | n/a% | n/a s | 27.352 MB | 27.352 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 156958 |  | 1 | n/a% | n/a% | n/a s | 27.793 MB | 27.793 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 156997 |  | 1 | n/a% | n/a% | n/a s | 27.223 MB | 27.223 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 157018 | bear_0000 | 1 | n/a% | n/a% | n/a s | 10.617 MB | 10.617 MB | 1569.445 MB | 1569.445 MB | n/a MB | n/a MB |
| docker | 157036 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.160 MB | 26.820 MB | 1660.490 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 157082 |  | 1 | n/a% | n/a% | n/a s | 25.508 MB | 25.508 MB | 1596.211 MB | 1596.211 MB | n/a MB | n/a MB |
| docker | 157090 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.848 MB | 25.848 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 157130 | bear_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.042 MB | 12.680 MB | 314.889 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 157142 | bear_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 157153 |  | 1 | n/a% | n/a% | n/a s | 26.996 MB | 26.996 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 157179 |  | 1 | n/a% | n/a% | n/a s | 27.098 MB | 27.098 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 157214 |  | 1 | n/a% | n/a% | n/a s | 23.656 MB | 23.656 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 157244 |  | 1 | n/a% | n/a% | n/a s | 16.297 MB | 16.297 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 157252 |  | 1 | n/a% | n/a% | n/a s | 26.043 MB | 26.043 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 157293 |  | 1 | n/a% | n/a% | n/a s | 26.637 MB | 26.637 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 157302 |  | 1 | n/a% | n/a% | n/a s | 26.402 MB | 26.402 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 157310 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.922 MB | 25.922 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 157358 | bear_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.661 MB | 12.746 MB | 375.347 MB | 1498.223 MB | n/a MB | n/a MB |
| tail | 157373 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 157405 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.445 MB | 11.445 MB | 1570.090 MB | 1570.090 MB | n/a MB | n/a MB |
| docker | 157404 |  | 1 | n/a% | n/a% | n/a s | 15.133 MB | 15.133 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 157383 |  | 1 | n/a% | n/a% | n/a s | 27.543 MB | 27.543 MB | 1733.027 MB | 1733.027 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 157453 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.656 MB | 11.656 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 157426 |  | 1 | n/a% | n/a% | n/a s | 27.332 MB | 27.332 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 157437 |  | 1 | n/a% | n/a% | n/a s | 25.801 MB | 25.801 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 157487 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.012 MB | 27.012 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python3 | 157492 |  | 5 | 96.003% | 108.759% | 0.390 s | 24.346 MB | 34.684 MB | 48.520 MB | 57.441 MB | 0.000000 MB | 0.277344 MB |
| docker | 157546 |  | 1 | n/a% | n/a% | n/a s | 21.129 MB | 21.129 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 157582 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.148 MB | 27.148 MB | 1660.523 MB | 1660.523 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 157625 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 4.792 MB | 13.109 MB | 548.197 MB | 1642.480 MB | n/a MB | n/a MB |
| tail | 157638 | bear_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 157648 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 157718 |  | 2 | 0.000% | 0.000% | 0.000 s | 17.125 MB | 25.707 MB | 1443.822 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 157780 |  | 1 | n/a% | n/a% | n/a s | 26.473 MB | 26.473 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker-init | 157818 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 157835 |  | 1 | n/a% | n/a% | n/a s | 18.180 MB | 18.180 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 157833 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 157871 |  | 1 | n/a% | n/a% | n/a s | 27.281 MB | 27.281 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 157929 | bear_0000 | 1 | n/a% | n/a% | n/a s | 10.566 MB | 10.566 MB | 1569.453 MB | 1569.453 MB | n/a MB | n/a MB |
| docker | 157908 |  | 1 | n/a% | n/a% | n/a s | 27.348 MB | 27.348 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 157945 |  | 1 | n/a% | n/a% | n/a s | 27.148 MB | 27.148 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 157987 |  | 1 | n/a% | n/a% | n/a s | 8.672 MB | 8.672 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 157997 |  | 1 | n/a% | n/a% | n/a s | 27.172 MB | 27.172 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 158012 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.570 MB | 27.570 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 158051 | beef_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.741 MB | 13.066 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 158064 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 158095 |  | 1 | n/a% | n/a% | n/a s | 8.680 MB | 8.680 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 158131 |  | 1 | n/a% | n/a% | n/a s | 27.008 MB | 27.008 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 158185 | beef_0000 | 1 | n/a% | n/a% | n/a s | 4.000 MB | 4.000 MB | 1208.676 MB | 1208.676 MB | n/a MB | n/a MB |
| docker | 158166 |  | 1 | n/a% | n/a% | n/a s | 26.828 MB | 26.828 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 158201 |  | 1 | n/a% | n/a% | n/a s | 25.742 MB | 25.742 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 158244 |  | 1 | n/a% | n/a% | n/a s | 23.543 MB | 23.543 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 158262 |  | 1 | n/a% | n/a% | n/a s | 26.973 MB | 26.973 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 158301 | beef_0000 | 4 | 6.434% | 19.302% | 0.020 s | 1.474 MB | 3.996 MB | 302.960 MB | 1208.676 MB | n/a MB | n/a MB |
| docker | 158324 |  | 1 | n/a% | n/a% | n/a s | 8.848 MB | 8.848 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| tail | 158314 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.684 MB | 1.684 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 158371 | beef_0000 | 1 | n/a% | n/a% | n/a s | 10.660 MB | 10.660 MB | 1569.582 MB | 1569.582 MB | n/a MB | n/a MB |
| docker | 158351 |  | 1 | n/a% | n/a% | n/a s | 27.324 MB | 27.324 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 158386 |  | 1 | n/a% | n/a% | n/a s | 27.527 MB | 27.527 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 158405 | beef_0000 | 1 | n/a% | n/a% | n/a s | 11.855 MB | 11.855 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 158421 |  | 1 | n/a% | n/a% | n/a s | 25.848 MB | 25.848 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 158472 |  | 1 | n/a% | n/a% | n/a s | 23.789 MB | 23.789 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 158504 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.715 MB | 25.715 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 158520 |  | 1 | n/a% | n/a% | n/a s | 25.629 MB | 25.629 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 158538 |  | 1 | n/a% | n/a% | n/a s | 25.621 MB | 25.621 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 158570 |  | 48 | 0.000% | 0.000% | 0.000 s | 26.875 MB | 26.875 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 158587 |  | 3 | 0.000% | 0.000% | 0.000 s | 18.122 MB | 27.184 MB | 1107.182 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 158626 | bear_0000 | 6 | 7.765% | 38.825% | 0.040 s | 2.518 MB | 11.941 MB | 262.581 MB | 1570.211 MB | n/a MB | n/a MB |
| tail | 158638 | bear_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.809 MB | 1.809 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 158668 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.898 MB | 11.898 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 158649 |  | 1 | n/a% | n/a% | n/a s | 27.387 MB | 27.387 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 158675 |  | 1 | n/a% | n/a% | n/a s | 27.246 MB | 27.246 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| base64 | 158700 | bear_0000 | 1 | n/a% | n/a% | n/a s | 1.297 MB | 1.297 MB | 2.590 MB | 2.590 MB | n/a MB | n/a MB |
| sh | 158694 | bear_0000 | 1 | n/a% | n/a% | n/a s | 1.586 MB | 1.586 MB | 2.617 MB | 2.617 MB | n/a MB | n/a MB |
| docker | 158710 |  | 1 | n/a% | n/a% | n/a s | 27.285 MB | 27.285 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 158742 |  | 1 | n/a% | n/a% | n/a s | 26.633 MB | 26.633 MB | 1732.277 MB | 1732.277 MB | n/a MB | n/a MB |
| docker | 158751 |  | 1 | n/a% | n/a% | n/a s | 26.000 MB | 26.000 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 158811 |  | 3 | 4.907% | 9.813% | 0.010 s | 17.417 MB | 25.219 MB | 1117.728 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| tail | 158863 | bear_0000 | 16 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 158849 | bear_0000 | 16 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 158893 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.094 MB | 11.094 MB | 1569.703 MB | 1569.703 MB | n/a MB | n/a MB |
| docker | 158873 |  | 1 | n/a% | n/a% | n/a s | 27.469 MB | 27.469 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 158901 |  | 14 | 0.000% | 0.000% | 0.000 s | 27.070 MB | 27.070 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 158920 | bear_0000 | 14 | 1.448% | 18.824% | 0.020 s | 4.086 MB | 11.957 MB | 116.254 MB | 1570.477 MB | n/a MB | n/a MB |
| python | 158929 | bear_0000 | 13 | 96.318% | 110.948% | 1.220 s | 31.628 MB | 41.156 MB | 38.701 MB | 51.340 MB | n/a MB | n/a MB |
| docker | 158939 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.883 MB | 25.883 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 159009 |  | 1 | n/a% | n/a% | n/a s | 27.008 MB | 27.008 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 159020 |  | 1 | n/a% | n/a% | n/a s | 25.797 MB | 25.797 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 159068 | beef_0000 | 4 | 3.250% | 9.750% | 0.010 s | 3.507 MB | 12.129 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 159028 |  | 1 | n/a% | n/a% | n/a s | 25.457 MB | 25.457 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 159091 |  | 1 | n/a% | n/a% | n/a s | 27.402 MB | 27.402 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 159081 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 159118 |  | 1 | n/a% | n/a% | n/a s | 27.578 MB | 27.578 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 159184 |  | 1 | n/a% | n/a% | n/a s | 8.844 MB | 8.844 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 159193 |  | 1 | n/a% | n/a% | n/a s | 26.691 MB | 26.691 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 159254 |  | 1 | n/a% | n/a% | n/a s | 26.770 MB | 26.770 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| 6 | 159289 | beef_0000 | 1 | n/a% | n/a% | n/a s | 1.805 MB | 1.805 MB | 13.980 MB | 13.980 MB | n/a MB | n/a MB |
| docker-init | 159293 | beef_0000 | 14 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 159305 | beef_0000 | 14 | 0.000% | 0.000% | 0.000 s | 1.773 MB | 1.773 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 159362 | beef_0000 | 12 | 1.765% | 19.420% | 0.020 s | 3.670 MB | 7.301 MB | 134.791 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 159342 |  | 12 | 0.000% | 0.000% | 0.000 s | 27.168 MB | 27.168 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 159371 | beef_0000 | 11 | 97.499% | 107.858% | 1.080 s | 32.934 MB | 41.520 MB | 40.515 MB | 51.238 MB | n/a MB | n/a MB |
| docker | 159399 |  | 1 | n/a% | n/a% | n/a s | 15.652 MB | 15.652 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 159408 |  | 45 | 0.000% | 0.000% | 0.000 s | 25.852 MB | 25.852 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 159425 |  | 2 | 9.150% | 9.150% | 0.010 s | 13.871 MB | 26.000 MB | 846.486 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 159467 |  | 1 | n/a% | n/a% | n/a s | 17.062 MB | 17.062 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 159484 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.691 MB | 25.691 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 159523 | beef_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.708 MB | 13.086 MB | 274.709 MB | 1642.980 MB | n/a MB | n/a MB |
| tail | 159537 | beef_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 159548 |  | 1 | n/a% | n/a% | n/a s | 9.305 MB | 9.305 MB | 1315.695 MB | 1315.695 MB | n/a MB | n/a MB |
| docker | 159575 |  | 1 | n/a% | n/a% | n/a s | 15.145 MB | 15.145 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 159602 |  | 1 | n/a% | n/a% | n/a s | 4.480 MB | 4.480 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 159611 |  | 1 | n/a% | n/a% | n/a s | 27.520 MB | 27.520 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 159629 | beef_0000 | 1 | n/a% | n/a% | n/a s | 11.590 MB | 11.590 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 159646 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.930 MB | 25.930 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 159706 |  | 1 | n/a% | n/a% | n/a s | 26.418 MB | 26.418 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| docker | 159730 |  | 1 | n/a% | n/a% | n/a s | 16.020 MB | 16.020 MB | 1587.703 MB | 1587.703 MB | n/a MB | n/a MB |
| python3 | 159737 |  | 4 | 98.738% | 98.907% | 0.300 s | 28.207 MB | 34.621 MB | 51.820 MB | 57.438 MB | 0.000000 MB | 0.277344 MB |
| docker | 159755 |  | 1 | n/a% | n/a% | n/a s | 26.809 MB | 26.809 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 159774 |  | 1 | n/a% | n/a% | n/a s | 26.938 MB | 26.938 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 159788 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.949 MB | 27.949 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 159828 | bell_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.675 MB | 12.801 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 159841 | bell_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 159870 |  | 1 | n/a% | n/a% | n/a s | 3.324 MB | 3.324 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 159905 |  | 1 | n/a% | n/a% | n/a s | 25.676 MB | 25.676 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 159940 |  | 1 | n/a% | n/a% | n/a s | 27.383 MB | 27.383 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 159976 |  | 1 | n/a% | n/a% | n/a s | 26.840 MB | 26.840 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 160017 |  | 1 | n/a% | n/a% | n/a s | 25.859 MB | 25.859 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 160072 | bell_0000 | 4 | 9.735% | 29.205% | 0.030 s | 3.045 MB | 10.492 MB | 375.089 MB | 1497.191 MB | n/a MB | n/a MB |
| docker | 160033 |  | 1 | n/a% | n/a% | n/a s | 26.930 MB | 26.930 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 160085 | bell_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 160095 |  | 1 | n/a% | n/a% | n/a s | 9.230 MB | 9.230 MB | 1235.438 MB | 1235.438 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 160142 | bell_0000 | 1 | n/a% | n/a% | n/a s | 11.289 MB | 11.289 MB | 1570.090 MB | 1570.090 MB | n/a MB | n/a MB |
| docker | 160123 |  | 1 | n/a% | n/a% | n/a s | 27.535 MB | 27.535 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 160177 | bell_0000 | 1 | n/a% | n/a% | n/a s | 11.914 MB | 11.914 MB | 1642.980 MB | 1642.980 MB | n/a MB | n/a MB |
| docker | 160157 |  | 1 | n/a% | n/a% | n/a s | 26.988 MB | 26.988 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 160209 |  | 1 | n/a% | n/a% | n/a s | 22.660 MB | 22.660 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 160194 |  | 1 | n/a% | n/a% | n/a s | 27.102 MB | 27.102 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| docker | 160278 |  | 1 | n/a% | n/a% | n/a s | 27.027 MB | 27.027 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 160286 |  | 40 | 0.000% | 0.000% | 0.000 s | 25.473 MB | 25.473 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 160319 |  | 1 | n/a% | n/a% | n/a s | 25.656 MB | 25.656 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| python3 | 160334 |  | 4 | 98.731% | 98.943% | 0.300 s | 26.365 MB | 34.703 MB | 50.380 MB | 57.441 MB | 0.000000 MB | 0.277344 MB |
| docker | 160353 |  | 1 | n/a% | n/a% | n/a s | 26.035 MB | 26.035 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 160377 |  | 1 | n/a% | n/a% | n/a s | 15.715 MB | 15.715 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 160399 |  | 38 | 0.000% | 0.000% | 0.000 s | 27.188 MB | 27.188 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 160481 | bell_0000 | 4 | 3.254% | 9.762% | 0.010 s | 3.558 MB | 12.332 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 160441 |  | 1 | n/a% | n/a% | n/a s | 26.938 MB | 26.938 MB | 1588.520 MB | 1588.520 MB | n/a MB | n/a MB |
| tail | 160495 | bell_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 160506 |  | 1 | n/a% | n/a% | n/a s | 27.281 MB | 27.281 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 160560 |  | 1 | n/a% | n/a% | n/a s | 2.031 MB | 2.031 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 160600 |  | 1 | n/a% | n/a% | n/a s | 26.133 MB | 26.133 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 160608 |  | 1 | n/a% | n/a% | n/a s | 25.816 MB | 25.816 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 160666 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.699 MB | 25.699 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 160706 | bell_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.730 MB | 12.703 MB | 143.707 MB | 1570.227 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 160748 | bell_0000 | 1 | n/a% | n/a% | n/a s | 12.199 MB | 12.199 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 160728 |  | 1 | n/a% | n/a% | n/a s | 27.066 MB | 27.066 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 160718 | bell_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| python | 160785 | bell_0000 | 8 | 100.651% | 107.904% | 0.720 s | 30.632 MB | 41.719 MB | 37.978 MB | 51.238 MB | n/a MB | n/a MB |
| bash | 160775 | bell_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.340 MB | 3.340 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 160755 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.098 MB | 27.207 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 160795 |  | 2 | 9.775% | 9.775% | 0.010 s | 16.275 MB | 25.934 MB | 846.486 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 160879 |  | 1 | n/a% | n/a% | n/a s | 9.609 MB | 9.609 MB | 1459.953 MB | 1459.953 MB | n/a MB | n/a MB |
| docker | 160887 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.344 MB | 25.344 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 160920 |  | 1 | n/a% | n/a% | n/a s | 7.820 MB | 7.820 MB | 32.867 MB | 32.867 MB | n/a MB | n/a MB |
| python3 | 160936 |  | 4 | 102.003% | 108.773% | 0.310 s | 24.580 MB | 34.535 MB | 48.613 MB | 57.438 MB | 0.003906 MB | 0.277344 MB |
| docker | 160955 |  | 1 | n/a% | n/a% | n/a s | 2.676 MB | 2.676 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |

## GPU metrics

_No GPU samples were collected._

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| alex_0000 | 52.416% | 100.962% | 1.745 s | 7.401 MB | 36.238 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| andy_0000 | 56.750% | 100.874% | 1.343 s | 9.529 MB | 35.633 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| arch_0000 | 55.256% | 112.872% | 1.328 s | 8.670 MB | 35.430 MB | 0.000000 MB | 0.003906 MB | 3567.778607 MB | 40.536980 MB |
| bake_0000 | 52.602% | 101.060% | 1.525 s | 8.304 MB | 35.695 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bale_0000 | 83.205% | 100.526% | 3.992 s | 23.044 MB | 35.461 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| band_0000 | 60.499% | 100.759% | 1.245 s | 9.721 MB | 35.531 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bart_0000 | 47.340% | 100.107% | 1.719 s | 6.579 MB | 35.582 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| base_0000 | 58.500% | 100.848% | 2.286 s | 8.611 MB | 35.160 MB | 0.000000 MB | 0.007812 MB | 0.000000 MB | 0.000000 MB |
| beam_0000 | 62.423% | 99.140% | 1.851 s | 12.246 MB | 35.340 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bear_0000 | 54.896% | 101.583% | 1.989 s | 9.668 MB | 34.863 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| beef_0000 | 61.180% | 105.087% | 1.722 s | 10.799 MB | 35.250 MB | 0.000000 MB | 0.003906 MB | 3571.712593 MB | 42.504932 MB |
| bell_0000 | 66.138% | 100.044% | 1.153 s | 11.029 MB | 35.215 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |

## Incomplete spans

_No spans were still open when profiling stopped._

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sync:result_wait | 24/24 | 0 | 0 | 694.918 | 0.007 | 694.908 | 28954.914 | 25862.018 | 44157.632 |
| turn | 85/85 | 0 | 0 | 584.180 | 2.742 | 580.891 | 6872.712 | 4327.099 | 23808.323 |
| llm:attempt | 85/85 | 0 | 0 | 517.145 | 2.194 | 514.549 | 6084.056 | 3586.776 | 23783.853 |
| run:diagnose_bug | 12/12 | 0 | 0 | 420.897 | 1.525 | 418.973 | 35074.771 | 33796.344 | 47892.618 |
| llm:diagnose_bug | 34/34 | 0 | 0 | 339.918 | 1.202 | 338.410 | 9997.582 | 5241.632 | 26631.606 |
| run:repair_bug | 12/12 | 0 | 0 | 274.030 | 1.352 | 272.507 | 22835.799 | 20302.565 | 33802.597 |
| llm:repair_bug | 51/51 | 0 | 0 | 177.256 | 1.019 | 176.141 | 3475.615 | 3196.060 | 6981.045 |
| teardown:commit | 24/24 | 0 | 0 | 110.372 | 0.061 | 110.297 | 4598.851 | 4300.770 | 5350.715 |
| sandbox:commit | 24/24 | 0 | 0 | 109.828 | 0.048 | 109.766 | 4576.183 | 4281.033 | 5329.568 |
| capstone:plan:bucketsort | 1/1 | 0 | 0 | 52.413 | 0.001 | 52.412 | 52412.820 | 52412.820 | 52412.820 |
| capstone:plan:find_first_in_sorted | 1/1 | 0 | 0 | 44.195 | 0.001 | 44.194 | 44194.808 | 44194.808 | 44194.808 |
| capstone:build:find_first_in_sorted | 1/1 | 0 | 0 | 43.951 | 0.000 | 43.951 | 43951.072 | 43951.072 | 43951.072 |
| capstone:plan:bitcount | 1/1 | 0 | 0 | 42.538 | 0.003 | 42.534 | 42538.087 | 42538.087 | 42538.087 |
| tool_dispatch:repair_bug | 51/51 | 0 | 0 | 40.089 | 0.237 | 39.793 | 786.054 | 612.844 | 2008.682 |
| capstone:plan:mergesort | 1/1 | 0 | 0 | 39.478 | 0.001 | 39.478 | 39478.350 | 39478.350 | 39478.350 |
| capstone:plan:hanoi | 1/1 | 0 | 0 | 37.071 | 0.001 | 37.069 | 37070.881 | 37070.881 | 37070.881 |
| capstone:plan:powerset | 1/1 | 0 | 0 | 34.459 | 0.002 | 34.457 | 34458.767 | 34458.767 | 34458.767 |
| capstone:plan:next_palindrome | 1/1 | 0 | 0 | 33.134 | 0.001 | 33.134 | 33134.229 | 33134.229 | 33134.229 |
| capstone:plan:rpn_eval | 1/1 | 0 | 0 | 31.546 | 0.001 | 31.546 | 31546.328 | 31546.328 | 31546.328 |
| capstone:plan:is_valid_parenthesization | 1/1 | 0 | 0 | 28.733 | 0.001 | 28.732 | 28732.967 | 28732.967 | 28732.967 |
| capstone:plan:gcd | 1/1 | 0 | 0 | 28.728 | 0.001 | 28.727 | 28727.726 | 28727.726 | 28727.726 |
| tool_dispatch:diagnose_bug | 34/34 | 0 | 0 | 26.850 | 0.225 | 26.543 | 789.715 | 602.146 | 1920.788 |
| capstone:plan:levenshtein | 1/1 | 0 | 0 | 26.226 | 0.001 | 26.225 | 26226.454 | 26226.454 | 26226.454 |
| capstone:build:powerset | 1/1 | 0 | 0 | 25.499 | 0.000 | 25.499 | 25499.357 | 25499.357 | 25499.357 |
| capstone:build:mergesort | 1/1 | 0 | 0 | 25.147 | 0.001 | 25.146 | 25146.594 | 25146.594 | 25146.594 |
| capstone:build:levenshtein | 1/1 | 0 | 0 | 24.808 | 0.000 | 24.808 | 24808.313 | 24808.313 | 24808.313 |
| tool:read | 40/40 | 0 | 0 | 22.943 | 0.180 | 22.696 | 573.568 | 580.064 | 864.438 |
| sandbox:start | 71/71 | 0 | 0 | 22.713 | 0.122 | 22.551 | 319.896 | 253.459 | 555.477 |
| capstone:plan:flatten | 1/1 | 0 | 0 | 22.383 | 0.001 | 22.381 | 22382.888 | 22382.888 | 22382.888 |
| sandbox:exec | 18/18 | 0 | 0 | 22.215 | 0.055 | 22.147 | 1234.157 | 1164.366 | 2230.409 |
| capstone:build:next_palindrome | 1/1 | 0 | 0 | 20.985 | 0.001 | 20.985 | 20985.306 | 20985.306 | 20985.306 |
| capstone:build:is_valid_parenthesization | 1/1 | 0 | 0 | 20.539 | 0.000 | 20.538 | 20538.816 | 20538.816 | 20538.816 |
| tool:bash | 13/13 | 0 | 0 | 20.330 | 0.052 | 20.266 | 1563.827 | 1199.153 | 2716.661 |
| capstone:build:bucketsort | 1/1 | 0 | 0 | 20.066 | 0.001 | 20.065 | 20065.615 | 20065.615 | 20065.615 |
| capstone:build:hanoi | 1/1 | 0 | 0 | 19.572 | 0.000 | 19.572 | 19572.255 | 19572.255 | 19572.255 |
| capstone:build:rpn_eval | 1/1 | 0 | 0 | 18.805 | 0.001 | 18.805 | 18805.069 | 18805.069 | 18805.069 |
| capstone:build:gcd | 1/1 | 0 | 0 | 18.617 | 0.001 | 18.616 | 18616.706 | 18616.706 | 18616.706 |
| capstone:build:bitcount | 1/1 | 0 | 0 | 18.390 | 0.001 | 18.389 | 18389.781 | 18389.781 | 18389.781 |
| capstone:build:flatten | 1/1 | 0 | 0 | 17.652 | 0.000 | 17.651 | 17652.319 | 17652.319 | 17652.319 |
| sandbox:stop | 133/133 | 0 | 0 | 15.955 | 0.116 | 15.793 | 119.963 | 169.707 | 242.288 |
| capstone:prepare:bitcount | 1/1 | 0 | 0 | 10.135 | 0.043 | 10.092 | 10134.824 | 10134.824 | 10134.824 |
| capstone:prepare:find_first_in_sorted | 1/1 | 0 | 0 | 10.042 | 0.032 | 10.010 | 10041.815 | 10041.815 | 10041.815 |
| sandbox:read_file | 53/53 | 0 | 0 | 9.318 | 0.082 | 9.214 | 175.806 | 129.183 | 409.705 |
| capstone:prepare:mergesort | 1/1 | 0 | 0 | 7.117 | 0.045 | 7.072 | 7117.209 | 7117.209 | 7117.209 |
| tool:edit | 13/13 | 0 | 0 | 6.296 | 0.054 | 6.229 | 484.334 | 430.273 | 659.210 |
| capstone:scheduler:tick | 372/372 | 0 | 0 | 2.940 | 0.689 | 2.231 | 7.903 | 0.196 | 0.996 |
| agent:create | 12/12 | 0 | 0 | 2.756 | 0.586 | 2.159 | 229.671 | 136.004 | 642.655 |
| capstone:prepare:levenshtein | 1/1 | 0 | 0 | 2.554 | 0.032 | 2.522 | 2553.557 | 2553.557 | 2553.557 |
| capstone:verify:levenshtein | 1/1 | 0 | 0 | 2.502 | 0.001 | 2.500 | 2502.185 | 2502.185 | 2502.185 |
| tool:glob | 4/4 | 0 | 0 | 1.552 | 0.012 | 1.538 | 387.895 | 352.172 | 480.904 |
| sandbox:destroy | 12/12 | 0 | 0 | 1.499 | 0.019 | 1.479 | 124.949 | 118.788 | 159.878 |
| sandbox:write_file | 13/13 | 0 | 0 | 1.449 | 0.014 | 1.429 | 111.460 | 93.398 | 169.956 |
| capstone:verify:gcd | 1/1 | 0 | 0 | 0.704 | 0.001 | 0.701 | 704.163 | 704.163 | 704.163 |
| capstone:verify:flatten | 1/1 | 0 | 0 | 0.631 | 0.001 | 0.629 | 630.808 | 630.808 | 630.808 |
| capstone:prepare:gcd | 1/1 | 0 | 0 | 0.461 | 0.030 | 0.431 | 460.971 | 460.971 | 460.971 |
| capstone:verify:hanoi | 1/1 | 0 | 0 | 0.454 | 0.001 | 0.452 | 454.142 | 454.142 | 454.142 |
| capstone:prepare:bucketsort | 1/1 | 0 | 0 | 0.449 | 0.030 | 0.419 | 449.113 | 449.113 | 449.113 |
| capstone:prepare:hanoi | 1/1 | 0 | 0 | 0.448 | 0.030 | 0.418 | 448.471 | 448.471 | 448.471 |
| capstone:prepare:powerset | 1/1 | 0 | 0 | 0.444 | 0.031 | 0.413 | 443.936 | 443.936 | 443.936 |
| capstone:verify:is_valid_parenthesization | 1/1 | 0 | 0 | 0.441 | 0.001 | 0.440 | 440.842 | 440.842 | 440.842 |
| capstone:prepare:rpn_eval | 1/1 | 0 | 0 | 0.440 | 0.031 | 0.409 | 439.546 | 439.546 | 439.546 |
| capstone:prepare:next_palindrome | 1/1 | 0 | 0 | 0.436 | 0.031 | 0.405 | 435.751 | 435.751 | 435.751 |
| capstone:prepare:flatten | 1/1 | 0 | 0 | 0.435 | 0.031 | 0.404 | 435.212 | 435.212 | 435.212 |
| capstone:verify:mergesort | 1/1 | 0 | 0 | 0.434 | 0.001 | 0.432 | 433.934 | 433.934 | 433.934 |
| capstone:prepare:is_valid_parenthesization | 1/1 | 0 | 0 | 0.423 | 0.030 | 0.392 | 422.511 | 422.511 | 422.511 |
| capstone:verify:find_first_in_sorted | 1/1 | 0 | 0 | 0.407 | 0.001 | 0.406 | 407.461 | 407.461 | 407.461 |
| capstone:verify:bitcount | 1/1 | 0 | 0 | 0.404 | 0.001 | 0.402 | 403.566 | 403.566 | 403.566 |
| capstone:verify:rpn_eval | 1/1 | 0 | 0 | 0.400 | 0.001 | 0.399 | 400.433 | 400.433 | 400.433 |
| capstone:verify:bucketsort | 1/1 | 0 | 0 | 0.394 | 0.001 | 0.392 | 393.999 | 393.999 | 393.999 |
| capstone:verify:next_palindrome | 1/1 | 0 | 0 | 0.388 | 0.001 | 0.387 | 388.463 | 388.463 | 388.463 |
| capstone:verify:powerset | 1/1 | 0 | 0 | 0.385 | 0.001 | 0.384 | 385.165 | 385.165 | 385.165 |
| tool:grep | 1/1 | 0 | 0 | 0.345 | 0.003 | 0.342 | 345.284 | 345.284 | 345.284 |
| sandbox:provision | 12/12 | 0 | 0 | 0.284 | 0.012 | 0.269 | 23.674 | 0.631 | 125.363 |
| sandbox:create | 12/12 | 0 | 0 | 0.282 | 0.010 | 0.269 | 23.510 | 0.423 | 125.225 |
| sync:container | 916/916 | 0 | 0 | 0.121 | 0.108 | 0.010 | 0.132 | 0.134 | 0.268 |
| run:detect | 1/1 | 0 | 0 | 0.038 | 0.001 | 0.037 | 38.211 | 38.211 | 38.211 |
| prune | 24/24 | 0 | 0 | 0.007 | 0.004 | 0.002 | 0.307 | 0.242 | 0.678 |
| tool:return_summary | 14/14 | 2 | 0 | 0.005 | 0.005 | 0.000 | 0.360 | 0.352 | 0.441 |
| llm:sync | 85/85 | 0 | 0 | 0.004 | 0.004 | 0.000 | 0.052 | 0.041 | 0.088 |
| tool:return_plan | 12/12 | 0 | 0 | 0.004 | 0.004 | 0.000 | 0.356 | 0.328 | 0.516 |
| tool:return_status | 12/12 | 0 | 0 | 0.003 | 0.003 | 0.000 | 0.287 | 0.282 | 0.338 |
| agsync:join | 12/12 | 0 | 0 | 0.003 | 0.003 | 0.000 | 0.231 | 0.218 | 0.275 |
| input:prepare | 24/24 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.095 | 0.091 | 0.129 |
| proc_wait | 24/24 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.083 | 0.069 | 0.143 |
| agprof:clock_sync | 1/1 | 0 | 0 | 0.002 | 0.001 | 0.001 | 1.893 | 1.893 | 1.893 |
| resolve | 24/24 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.070 | 0.065 | 0.091 |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 3646 | 40.661 | 0.000 | 275.180 | 1.836 | 151.676430 CPU seconds | n/a |
| python3 (PID 143037) CPU | percent | 4055 | 5.423 | 0.000 | 115.889 | 19.843 | 22.660000 CPU seconds | n/a |
| python3 (PID 143037) io read MB/s | MB/s | 4055 | 0.045 | 0.000 | 12.580 | 0.000 | 19.289062 MB | n/a |
| python3 (PID 143037) io write MB/s | MB/s | 4055 | 0.087 | 0.000 | 23.093 | 8.526 | 35.644531 MB | n/a |
| python3 (PID 143037) rss_mb | MB | 4056 | 692.259 | 612.363 | 711.406 | 711.406 | n/a | n/a |
| python3 (PID 143037) vms_mb | MB | 4056 | 3921.070 | 3406.684 | 3976.641 | 3952.551 | n/a | n/a |
| git (PID 143043) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| git (PID 143043) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 143043) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 143043) rss_mb | MB | 5 | 4.793 | 4.793 | 4.793 | 4.793 | n/a | n/a |
| git (PID 143043) vms_mb | MB | 5 | 12.516 | 12.516 | 12.516 | 12.516 | n/a | n/a |
| git (PID 143044) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| git (PID 143044) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 143044) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 143044) rss_mb | MB | 5 | 3.387 | 3.387 | 3.387 | 3.387 | n/a | n/a |
| git (PID 143044) vms_mb | MB | 5 | 11.273 | 11.273 | 11.273 | 11.273 | n/a | n/a |
| git-remote-http (PID 143045) CPU | percent | 4 | 9.886 | 0.000 | 29.643 | 0.000 | 0.040000 CPU seconds | n/a |
| git-remote-http (PID 143045) io read MB/s | MB/s | 4 | 0.820 | 0.000 | 3.088 | 0.000 | 0.332031 MB | n/a |
| git-remote-http (PID 143045) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git-remote-http (PID 143045) rss_mb | MB | 5 | 18.961 | 18.758 | 19.012 | 19.012 | n/a | n/a |
| git-remote-http (PID 143045) vms_mb | MB | 5 | 106.966 | 106.566 | 107.566 | 107.566 | n/a | n/a |
| python3 (PID 143051) CPU | percent | 98 | 99.888 | 89.207 | 109.050 | 99.104 | 9.880000 CPU seconds | n/a |
| python3 (PID 143051) io read MB/s | MB/s | 98 | 0.032 | 0.000 | 3.059 | 0.000 | 0.312500 MB | n/a |
| python3 (PID 143051) io write MB/s | MB/s | 98 | 0.002 | 0.000 | 0.155 | 0.000 | 0.015625 MB | n/a |
| python3 (PID 143051) rss_mb | MB | 99 | 33.824 | 13.449 | 34.148 | 34.148 | n/a | n/a |
| python3 (PID 143051) vms_mb | MB | 99 | 56.205 | 39.566 | 56.461 | 56.461 | n/a | n/a |
| python3 (PID 143052) CPU | percent | 3 | 102.324 | 98.964 | 108.937 | 108.937 | 0.310000 CPU seconds | n/a |
| python3 (PID 143052) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 143052) io write MB/s | MB/s | 3 | 0.928 | 0.000 | 2.631 | 2.631 | 0.281250 MB | n/a |
| python3 (PID 143052) rss_mb | MB | 4 | 29.750 | 21.020 | 35.164 | 35.164 | n/a | n/a |
| python3 (PID 143052) vms_mb | MB | 4 | 52.877 | 45.371 | 57.512 | 57.512 | n/a | n/a |
| python3 (PID 143053) CPU | percent | 3 | 102.331 | 99.050 | 108.872 | 99.050 | 0.310000 CPU seconds | n/a |
| python3 (PID 143053) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 143053) io write MB/s | MB/s | 3 | 0.941 | 0.000 | 2.786 | 2.786 | 0.285156 MB | n/a |
| python3 (PID 143053) rss_mb | MB | 4 | 28.667 | 17.516 | 36.480 | 36.480 | n/a | n/a |
| python3 (PID 143053) vms_mb | MB | 4 | 52.322 | 42.430 | 59.520 | 59.520 | n/a | n/a |
| python3 (PID 143054) CPU | percent | 3 | 99.030 | 89.074 | 108.981 | 99.034 | 0.300000 CPU seconds | n/a |
| python3 (PID 143054) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 143054) io write MB/s | MB/s | 3 | 0.052 | 0.000 | 0.155 | 0.155 | 0.015625 MB | n/a |
| python3 (PID 143054) rss_mb | MB | 4 | 23.045 | 5.469 | 34.371 | 34.371 | n/a | n/a |
| python3 (PID 143054) vms_mb | MB | 4 | 48.162 | 34.922 | 57.465 | 57.465 | n/a | n/a |
| python3 (PID 143055) CPU | percent | 24 | 99.445 | 89.067 | 108.973 | 89.143 | 2.410000 CPU seconds | n/a |
| python3 (PID 143055) io read MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 143055) io write MB/s | MB/s | 24 | 0.119 | 0.000 | 2.708 | 2.708 | 0.289062 MB | n/a |
| python3 (PID 143055) rss_mb | MB | 25 | 33.480 | 20.410 | 34.945 | 34.945 | n/a | n/a |
| python3 (PID 143055) vms_mb | MB | 25 | 56.677 | 45.238 | 57.512 | 57.512 | n/a | n/a |
| python3 (PID 143056) CPU | percent | 69 | 100.022 | 89.105 | 108.973 | 98.977 | 6.970000 CPU seconds | n/a |
| python3 (PID 143056) io read MB/s | MB/s | 69 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 143056) io write MB/s | MB/s | 69 | 0.041 | 0.000 | 2.700 | 0.000 | 0.289062 MB | n/a |
| python3 (PID 143056) rss_mb | MB | 70 | 41.615 | 16.594 | 47.441 | 47.441 | n/a | n/a |
| python3 (PID 143056) vms_mb | MB | 70 | 64.675 | 41.164 | 70.648 | 70.648 | n/a | n/a |
| python3 (PID 143058) CPU | percent | 4 | 99.028 | 98.923 | 99.125 | 98.923 | 0.400000 CPU seconds | n/a |
| python3 (PID 143058) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 143058) io write MB/s | MB/s | 4 | 0.715 | 0.000 | 2.705 | 2.705 | 0.289062 MB | n/a |
| python3 (PID 143058) rss_mb | MB | 5 | 26.413 | 9.445 | 35.355 | 35.355 | n/a | n/a |
| python3 (PID 143058) vms_mb | MB | 5 | 50.220 | 35.465 | 57.762 | 57.762 | n/a | n/a |
| python3 (PID 143059) CPU | percent | 98 | 99.828 | 89.080 | 109.057 | 99.062 | 9.890000 CPU seconds | n/a |
| python3 (PID 143059) io read MB/s | MB/s | 98 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 143059) io write MB/s | MB/s | 98 | 0.002 | 0.000 | 0.155 | 0.000 | 0.015625 MB | n/a |
| python3 (PID 143059) rss_mb | MB | 99 | 34.173 | 17.613 | 34.453 | 34.453 | n/a | n/a |
| python3 (PID 143059) vms_mb | MB | 99 | 57.221 | 42.445 | 57.465 | 57.465 | n/a | n/a |
| python3 (PID 143060) CPU | percent | 3 | 99.029 | 98.935 | 99.112 | 99.112 | 0.300000 CPU seconds | n/a |
| python3 (PID 143060) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 143060) io write MB/s | MB/s | 3 | 0.981 | 0.000 | 2.942 | 2.942 | 0.296875 MB | n/a |
| python3 (PID 143060) rss_mb | MB | 4 | 25.955 | 12.902 | 35.008 | 35.008 | n/a | n/a |
| python3 (PID 143060) vms_mb | MB | 4 | 49.755 | 38.293 | 57.465 | 57.465 | n/a | n/a |
| python3 (PID 143061) CPU | percent | 3 | 102.245 | 99.027 | 108.681 | 99.027 | 0.310000 CPU seconds | n/a |
| python3 (PID 143061) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 143061) io write MB/s | MB/s | 3 | 0.980 | 0.000 | 2.901 | 2.901 | 0.296875 MB | n/a |
| python3 (PID 143061) rss_mb | MB | 4 | 29.486 | 20.789 | 35.105 | 35.105 | n/a | n/a |
| python3 (PID 143061) vms_mb | MB | 4 | 52.784 | 45.238 | 57.496 | 57.496 | n/a | n/a |
| python3 (PID 143062) CPU | percent | 3 | 102.299 | 98.875 | 108.929 | 99.094 | 0.310000 CPU seconds | n/a |
| python3 (PID 143062) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 143062) io write MB/s | MB/s | 3 | 0.981 | 0.000 | 2.942 | 2.942 | 0.296875 MB | n/a |
| python3 (PID 143062) rss_mb | MB | 4 | 27.833 | 16.660 | 34.988 | 34.988 | n/a | n/a |
| python3 (PID 143062) vms_mb | MB | 4 | 51.432 | 41.164 | 57.512 | 57.512 | n/a | n/a |
| python3 (PID 143063) CPU | percent | 3 | 102.296 | 89.103 | 108.975 | 108.975 | 0.310000 CPU seconds | n/a |
| python3 (PID 143063) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 143063) io write MB/s | MB/s | 3 | 0.052 | 0.000 | 0.155 | 0.155 | 0.015625 MB | n/a |
| python3 (PID 143063) rss_mb | MB | 4 | 24.544 | 10.727 | 34.352 | 34.352 | n/a | n/a |
| python3 (PID 143063) vms_mb | MB | 4 | 48.627 | 36.633 | 57.465 | 57.465 | n/a | n/a |
| docker (PID 143092) rss_mb | MB | 1 | 9.238 | 9.238 | 9.238 | 9.238 | n/a | n/a |
| docker (PID 143092) vms_mb | MB | 1 | 1315.695 | 1315.695 | 1315.695 | 1315.695 | n/a | n/a |
| docker (PID 143108) rss_mb | MB | 1 | 26.012 | 26.012 | 26.012 | 26.012 | n/a | n/a |
| docker (PID 143108) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 143133) rss_mb | MB | 1 | 3.672 | 3.672 | 3.672 | 3.672 | n/a | n/a |
| docker (PID 143133) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 143134) rss_mb | MB | 1 | 5.047 | 5.047 | 5.047 | 5.047 | n/a | n/a |
| docker (PID 143134) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 143157) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 143157) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 143157) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 143157) rss_mb | MB | 3 | 27.155 | 27.055 | 27.355 | 27.355 | n/a | n/a |
| docker (PID 143157) vms_mb | MB | 3 | 1709.026 | 1661.023 | 1805.031 | 1805.031 | n/a | n/a |
| docker (PID 143159) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 143159) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 143159) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 143159) rss_mb | MB | 3 | 27.172 | 27.027 | 27.461 | 27.461 | n/a | n/a |
| docker (PID 143159) vms_mb | MB | 3 | 1684.775 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [andy_0000] (PID 143240) CPU | percent | 5 | 5.810 | 0.000 | 29.049 | 0.000 | 0.030000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 143240) rss_mb | MB | 6 | 2.316 | 0.633 | 10.734 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 143240) vms_mb | MB | 6 | 274.495 | 1.055 | 1641.699 | 1.055 | n/a | n/a |
| docker-init [alex_0000] (PID 143242) CPU | percent | 5 | 5.810 | 0.000 | 29.049 | 0.000 | 0.030000 CPU seconds | n/a |
| docker-init [alex_0000] (PID 143242) rss_mb | MB | 6 | 2.264 | 0.633 | 10.422 | 0.633 | n/a | n/a |
| docker-init [alex_0000] (PID 143242) vms_mb | MB | 6 | 250.411 | 1.055 | 1497.191 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 143265) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 143265) rss_mb | MB | 5 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [andy_0000] (PID 143265) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| tail [alex_0000] (PID 143266) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 143266) rss_mb | MB | 5 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [alex_0000] (PID 143266) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 143268) rss_mb | MB | 1 | 20.938 | 20.938 | 20.938 | 20.938 | n/a | n/a |
| docker (PID 143268) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 143274) rss_mb | MB | 1 | 9.359 | 9.359 | 9.359 | 9.359 | n/a | n/a |
| docker (PID 143274) vms_mb | MB | 1 | 1443.695 | 1443.695 | 1443.695 | 1443.695 | n/a | n/a |
| docker (PID 143321) rss_mb | MB | 1 | 25.633 | 25.633 | 25.633 | 25.633 | n/a | n/a |
| docker (PID 143321) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 143327) rss_mb | MB | 1 | 18.234 | 18.234 | 18.234 | 18.234 | n/a | n/a |
| docker (PID 143327) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 143338) rss_mb | MB | 1 | 27.055 | 27.055 | 27.055 | 27.055 | n/a | n/a |
| docker (PID 143338) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 143341) rss_mb | MB | 1 | 27.086 | 27.086 | 27.086 | 27.086 | n/a | n/a |
| docker (PID 143341) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 143373) rss_mb | MB | 1 | 11.836 | 11.836 | 11.836 | 11.836 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 143373) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 143380) rss_mb | MB | 1 | 11.906 | 11.906 | 11.906 | 11.906 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 143380) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 143393) rss_mb | MB | 1 | 27.625 | 27.625 | 27.625 | 27.625 | n/a | n/a |
| docker (PID 143393) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 143395) rss_mb | MB | 1 | 27.461 | 27.461 | 27.461 | 27.461 | n/a | n/a |
| docker (PID 143395) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 143438) rss_mb | MB | 1 | 12.250 | 12.250 | 12.250 | 12.250 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 143438) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 143462) rss_mb | MB | 1 | 27.207 | 27.207 | 27.207 | 27.207 | n/a | n/a |
| docker (PID 143462) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 143464) rss_mb | MB | 1 | 27.316 | 27.316 | 27.316 | 27.316 | n/a | n/a |
| docker (PID 143464) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 143501) rss_mb | MB | 1 | 11.863 | 11.863 | 11.863 | 11.863 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 143501) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 143504) rss_mb | MB | 1 | 11.828 | 11.828 | 11.828 | 11.828 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 143504) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 143535) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 143535) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 143535) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 143535) rss_mb | MB | 2 | 26.051 | 26.051 | 26.051 | 26.051 | n/a | n/a |
| docker (PID 143535) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 143537) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 143537) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 143537) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 143537) rss_mb | MB | 2 | 25.582 | 25.582 | 25.582 | 25.582 | n/a | n/a |
| docker (PID 143537) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 143654) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 143654) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 143654) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 143654) rss_mb | MB | 2 | 25.645 | 25.645 | 25.645 | 25.645 | n/a | n/a |
| docker (PID 143654) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 143656) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 143656) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 143656) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 143656) rss_mb | MB | 2 | 25.613 | 25.613 | 25.613 | 25.613 | n/a | n/a |
| docker (PID 143656) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 143733) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 143733) rss_mb | MB | 5 | 3.085 | 0.633 | 12.895 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 143733) vms_mb | MB | 5 | 315.039 | 1.055 | 1570.977 | 1.055 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 143740) CPU | percent | 4 | 4.758 | 0.000 | 19.031 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 143740) rss_mb | MB | 5 | 2.912 | 0.633 | 12.027 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 143740) vms_mb | MB | 5 | 314.889 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 143761) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 143761) rss_mb | MB | 4 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [alex_0000] (PID 143761) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| tail [andy_0000] (PID 143762) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 143762) rss_mb | MB | 4 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [andy_0000] (PID 143762) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 143782) rss_mb | MB | 1 | 21.344 | 21.344 | 21.344 | 21.344 | n/a | n/a |
| docker (PID 143782) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 143784) rss_mb | MB | 1 | 15.457 | 15.457 | 15.457 | 15.457 | n/a | n/a |
| docker (PID 143784) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 143835) rss_mb | MB | 1 | 22.469 | 22.469 | 22.469 | 22.469 | n/a | n/a |
| docker (PID 143835) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 143837) rss_mb | MB | 1 | 25.855 | 25.855 | 25.855 | 25.855 | n/a | n/a |
| docker (PID 143837) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 143894) rss_mb | MB | 1 | 25.770 | 25.770 | 25.770 | 25.770 | n/a | n/a |
| docker (PID 143894) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 143903) rss_mb | MB | 1 | 8.680 | 8.680 | 8.680 | 8.680 | n/a | n/a |
| docker (PID 143903) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 143960) rss_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| docker (PID 143960) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 143976) rss_mb | MB | 1 | 26.102 | 26.102 | 26.102 | 26.102 | n/a | n/a |
| docker (PID 143976) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 143978) rss_mb | MB | 1 | 25.895 | 25.895 | 25.895 | 25.895 | n/a | n/a |
| docker (PID 143978) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 144062) rss_mb | MB | 1 | 26.219 | 26.219 | 26.219 | 26.219 | n/a | n/a |
| docker (PID 144062) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 144086) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 144086) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 144086) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 144086) rss_mb | MB | 2 | 26.672 | 26.672 | 26.672 | 26.672 | n/a | n/a |
| docker (PID 144086) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 144124) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 144124) rss_mb | MB | 4 | 3.693 | 0.566 | 13.074 | 0.566 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 144124) vms_mb | MB | 4 | 411.411 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 144140) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 144140) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [andy_0000] (PID 144140) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 144150) rss_mb | MB | 1 | 27.328 | 27.328 | 27.328 | 27.328 | n/a | n/a |
| docker (PID 144150) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 144170) rss_mb | MB | 1 | 12.109 | 12.109 | 12.109 | 12.109 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 144170) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 144212) rss_mb | MB | 1 | 6.641 | 6.641 | 6.641 | 6.641 | n/a | n/a |
| docker (PID 144212) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 144249) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 144249) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 144249) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 144249) rss_mb | MB | 2 | 26.180 | 26.180 | 26.180 | 26.180 | n/a | n/a |
| docker (PID 144249) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 144302) rss_mb | MB | 1 | 2.621 | 2.621 | 2.621 | 2.621 | n/a | n/a |
| docker (PID 144302) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 144310) rss_mb | MB | 1 | 26.949 | 26.949 | 26.949 | 26.949 | n/a | n/a |
| docker (PID 144310) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 144350) CPU | percent | 2 | 9.766 | 0.000 | 19.532 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 144350) rss_mb | MB | 3 | 3.931 | 0.633 | 10.527 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 144350) vms_mb | MB | 3 | 523.768 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 144363) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 144363) rss_mb | MB | 2 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [alex_0000] (PID 144363) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 144374) rss_mb | MB | 1 | 0.414 | 0.414 | 0.414 | 0.414 | n/a | n/a |
| docker (PID 144374) vms_mb | MB | 1 | 30.578 | 30.578 | 30.578 | 30.578 | n/a | n/a |
| docker (PID 144401) rss_mb | MB | 1 | 27.266 | 27.266 | 27.266 | 27.266 | n/a | n/a |
| docker (PID 144401) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 144420) rss_mb | MB | 1 | 10.566 | 10.566 | 10.566 | 10.566 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 144420) vms_mb | MB | 1 | 1641.449 | 1641.449 | 1641.449 | 1641.449 | n/a | n/a |
| docker (PID 144443) rss_mb | MB | 1 | 26.945 | 26.945 | 26.945 | 26.945 | n/a | n/a |
| docker (PID 144443) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 144486) rss_mb | MB | 1 | 26.211 | 26.211 | 26.211 | 26.211 | n/a | n/a |
| docker (PID 144486) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 144503) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 144503) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 144503) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 144503) rss_mb | MB | 2 | 26.773 | 26.773 | 26.773 | 26.773 | n/a | n/a |
| docker (PID 144503) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 144543) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 144543) rss_mb | MB | 4 | 3.743 | 0.633 | 13.074 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 144543) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 144556) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 144556) rss_mb | MB | 3 | 1.691 | 1.691 | 1.691 | 1.691 | n/a | n/a |
| tail [alex_0000] (PID 144556) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 144580) rss_mb | MB | 1 | 27.371 | 27.371 | 27.371 | 27.371 | n/a | n/a |
| docker (PID 144580) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 144591) rss_mb | MB | 1 | 25.812 | 25.812 | 25.812 | 25.812 | n/a | n/a |
| docker (PID 144591) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 144613) rss_mb | MB | 1 | 11.305 | 11.305 | 11.305 | 11.305 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 144613) vms_mb | MB | 1 | 1569.961 | 1569.961 | 1569.961 | 1569.961 | n/a | n/a |
| docker (PID 144626) CPU | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 144626) io read MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 144626) io write MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 144626) rss_mb | MB | 40 | 25.402 | 25.402 | 25.402 | 25.402 | n/a | n/a |
| docker (PID 144626) vms_mb | MB | 40 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 144634) rss_mb | MB | 1 | 27.469 | 27.469 | 27.469 | 27.469 | n/a | n/a |
| docker (PID 144634) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 144655) rss_mb | MB | 1 | 11.699 | 11.699 | 11.699 | 11.699 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 144655) vms_mb | MB | 1 | 1498.223 | 1498.223 | 1498.223 | 1498.223 | n/a | n/a |
| docker (PID 144671) rss_mb | MB | 1 | 27.418 | 27.418 | 27.418 | 27.418 | n/a | n/a |
| docker (PID 144671) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 144707) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 144707) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 144707) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 144707) rss_mb | MB | 2 | 25.848 | 25.848 | 25.848 | 25.848 | n/a | n/a |
| docker (PID 144707) vms_mb | MB | 2 | 1659.961 | 1659.961 | 1659.961 | 1659.961 | n/a | n/a |
| docker (PID 144792) rss_mb | MB | 1 | 27.074 | 27.074 | 27.074 | 27.074 | n/a | n/a |
| docker (PID 144792) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [andy_0000] (PID 144831) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 144831) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 144831) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 144844) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 144844) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [andy_0000] (PID 144844) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 144846) rss_mb | MB | 1 | 18.188 | 18.188 | 18.188 | 18.188 | n/a | n/a |
| docker (PID 144846) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 144882) rss_mb | MB | 1 | 27.500 | 27.500 | 27.500 | 27.500 | n/a | n/a |
| docker (PID 144882) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 144920) rss_mb | MB | 1 | 27.391 | 27.391 | 27.391 | 27.391 | n/a | n/a |
| docker (PID 144920) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 144942) rss_mb | MB | 1 | 6.570 | 6.570 | 6.570 | 6.570 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 144942) vms_mb | MB | 1 | 1432.941 | 1432.941 | 1432.941 | 1432.941 | n/a | n/a |
| docker (PID 144959) rss_mb | MB | 1 | 25.816 | 25.816 | 25.816 | 25.816 | n/a | n/a |
| docker (PID 144959) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 145001) rss_mb | MB | 1 | 6.219 | 6.219 | 6.219 | 6.219 | n/a | n/a |
| docker (PID 145001) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 145018) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 145018) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 145018) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 145018) rss_mb | MB | 2 | 25.414 | 25.414 | 25.414 | 25.414 | n/a | n/a |
| docker (PID 145018) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 145058) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 145058) rss_mb | MB | 11 | 1.761 | 0.633 | 13.039 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 145058) vms_mb | MB | 11 | 143.729 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 145070) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 145070) rss_mb | MB | 10 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [andy_0000] (PID 145070) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 145080) rss_mb | MB | 1 | 27.402 | 27.402 | 27.402 | 27.402 | n/a | n/a |
| docker (PID 145080) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 145099) rss_mb | MB | 1 | 11.598 | 11.598 | 11.598 | 11.598 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 145099) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 145106) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 145106) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 145106) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 145106) rss_mb | MB | 9 | 27.332 | 27.332 | 27.332 | 27.332 | n/a | n/a |
| docker (PID 145106) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [andy_0000] (PID 145125) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [andy_0000] (PID 145125) rss_mb | MB | 9 | 3.328 | 3.328 | 3.328 | 3.328 | n/a | n/a |
| bash [andy_0000] (PID 145125) vms_mb | MB | 9 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [andy_0000] (PID 145134) CPU | percent | 8 | 100.379 | 88.172 | 107.857 | 98.014 | 0.820000 CPU seconds | n/a |
| python [andy_0000] (PID 145134) rss_mb | MB | 9 | 31.310 | 9.922 | 41.945 | 41.945 | n/a | n/a |
| python [andy_0000] (PID 145134) vms_mb | MB | 9 | 38.394 | 14.531 | 52.238 | 52.238 | n/a | n/a |
| docker (PID 145144) rss_mb | MB | 1 | 27.008 | 27.008 | 27.008 | 27.008 | n/a | n/a |
| docker (PID 145144) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 145187) rss_mb | MB | 1 | 18.289 | 18.289 | 18.289 | 18.289 | n/a | n/a |
| docker (PID 145187) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 145205) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 145205) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 145205) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 145205) rss_mb | MB | 2 | 26.719 | 26.719 | 26.719 | 26.719 | n/a | n/a |
| docker (PID 145205) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [andy_0000] (PID 145244) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 145244) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 145244) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 145257) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 145257) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [andy_0000] (PID 145257) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 145294) rss_mb | MB | 1 | 9.117 | 9.117 | 9.117 | 9.117 | n/a | n/a |
| docker (PID 145294) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 145329) rss_mb | MB | 1 | 27.438 | 27.438 | 27.438 | 27.438 | n/a | n/a |
| docker (PID 145329) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 145365) rss_mb | MB | 1 | 25.914 | 25.914 | 25.914 | 25.914 | n/a | n/a |
| docker (PID 145365) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 145406) rss_mb | MB | 1 | 19.934 | 19.934 | 19.934 | 19.934 | n/a | n/a |
| docker (PID 145406) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 145423) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 145423) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 145447) CPU | percent | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 145447) io read MB/s | MB/s | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 145447) io write MB/s | MB/s | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 145447) rss_mb | MB | 47 | 25.652 | 25.652 | 25.652 | 25.652 | n/a | n/a |
| docker (PID 145447) vms_mb | MB | 47 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 145464) rss_mb | MB | 1 | 22.336 | 22.336 | 22.336 | 22.336 | n/a | n/a |
| docker (PID 145464) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 145488) CPU | percent | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 145488) io read MB/s | MB/s | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 145488) io write MB/s | MB/s | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 145488) rss_mb | MB | 48 | 25.891 | 25.891 | 25.891 | 25.891 | n/a | n/a |
| docker (PID 145488) vms_mb | MB | 48 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 145504) rss_mb | MB | 1 | 23.414 | 23.414 | 23.414 | 23.414 | n/a | n/a |
| docker (PID 145504) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 145522) rss_mb | MB | 1 | 25.828 | 25.828 | 25.828 | 25.828 | n/a | n/a |
| docker (PID 145522) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| python3 (PID 145538) CPU | percent | 6 | 96.479 | 88.236 | 107.845 | 88.239 | 0.590000 CPU seconds | n/a |
| python3 (PID 145538) io read MB/s | MB/s | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 145538) io write MB/s | MB/s | 6 | 0.460 | 0.000 | 2.757 | 0.000 | 0.281250 MB | n/a |
| python3 (PID 145538) rss_mb | MB | 7 | 25.365 | 5.105 | 34.828 | 34.828 | n/a | n/a |
| python3 (PID 145538) vms_mb | MB | 7 | 49.834 | 34.922 | 57.441 | 57.441 | n/a | n/a |
| docker (PID 145568) rss_mb | MB | 1 | 26.004 | 26.004 | 26.004 | 26.004 | n/a | n/a |
| docker (PID 145568) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 145584) rss_mb | MB | 1 | 25.465 | 25.465 | 25.465 | 25.465 | n/a | n/a |
| docker (PID 145584) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 145618) CPU | percent | 2 | 4.939 | 0.000 | 9.878 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 145618) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 145618) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 145618) rss_mb | MB | 3 | 23.350 | 15.566 | 27.242 | 27.242 | n/a | n/a |
| docker (PID 145618) vms_mb | MB | 3 | 1660.501 | 1515.949 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [arch_0000] (PID 145660) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [arch_0000] (PID 145660) rss_mb | MB | 4 | 3.742 | 0.633 | 13.070 | 0.633 | n/a | n/a |
| docker-init [arch_0000] (PID 145660) vms_mb | MB | 4 | 393.473 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 145672) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 145672) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [arch_0000] (PID 145672) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 145701) rss_mb | MB | 1 | 20.324 | 20.324 | 20.324 | 20.324 | n/a | n/a |
| docker (PID 145701) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 145735) rss_mb | MB | 1 | 27.066 | 27.066 | 27.066 | 27.066 | n/a | n/a |
| docker (PID 145735) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 145771) rss_mb | MB | 1 | 27.227 | 27.227 | 27.227 | 27.227 | n/a | n/a |
| docker (PID 145771) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 145791) rss_mb | MB | 1 | 11.773 | 11.773 | 11.773 | 11.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 145791) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 145818) rss_mb | MB | 1 | 26.012 | 26.012 | 26.012 | 26.012 | n/a | n/a |
| docker (PID 145818) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 145820) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 145820) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 145820) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 145820) rss_mb | MB | 2 | 25.855 | 25.855 | 25.855 | 25.855 | n/a | n/a |
| docker (PID 145820) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 145894) CPU | percent | 4 | 2.342 | 0.000 | 9.367 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 145894) rss_mb | MB | 5 | 3.008 | 0.633 | 12.508 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 145894) vms_mb | MB | 5 | 300.438 | 1.055 | 1497.973 | 1.055 | n/a | n/a |
| docker (PID 145907) rss_mb | MB | 1 | 4.168 | 4.168 | 4.168 | 4.168 | n/a | n/a |
| docker (PID 145907) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| tail [alex_0000] (PID 145924) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 145924) rss_mb | MB | 4 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [alex_0000] (PID 145924) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 145937) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 145937) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 145937) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 145937) rss_mb | MB | 2 | 25.770 | 25.770 | 25.770 | 25.770 | n/a | n/a |
| docker (PID 145937) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 145948) rss_mb | MB | 1 | 27.172 | 27.172 | 27.172 | 27.172 | n/a | n/a |
| docker (PID 145948) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 146010) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 146010) rss_mb | MB | 5 | 3.090 | 0.633 | 12.918 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 146010) vms_mb | MB | 5 | 314.889 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| docker (PID 146017) rss_mb | MB | 1 | 27.117 | 27.117 | 27.117 | 27.117 | n/a | n/a |
| docker (PID 146017) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| tail [arch_0000] (PID 146049) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 146049) rss_mb | MB | 4 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [arch_0000] (PID 146049) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 146064) rss_mb | MB | 1 | 27.273 | 27.273 | 27.273 | 27.273 | n/a | n/a |
| docker (PID 146064) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 146077) CPU | percent | 1 | 16.735 | 16.735 | 16.735 | 16.735 | 0.020000 CPU seconds | n/a |
| docker (PID 146077) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 146077) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 146077) rss_mb | MB | 2 | 13.621 | 0.000 | 27.242 | 27.242 | n/a | n/a |
| docker (PID 146077) vms_mb | MB | 2 | 845.672 | 30.570 | 1660.773 | 1660.773 | n/a | n/a |
| sh [alex_0000] (PID 146115) rss_mb | MB | 1 | 1.766 | 1.766 | 1.766 | 1.766 | n/a | n/a |
| sh [alex_0000] (PID 146115) vms_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| docker (PID 146123) rss_mb | MB | 1 | 27.102 | 27.102 | 27.102 | 27.102 | n/a | n/a |
| docker (PID 146123) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 146146) rss_mb | MB | 1 | 3.676 | 3.676 | 3.676 | 3.676 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 146146) vms_mb | MB | 1 | 1208.676 | 1208.676 | 1208.676 | 1208.676 | n/a | n/a |
| docker (PID 146164) rss_mb | MB | 1 | 25.992 | 25.992 | 25.992 | 25.992 | n/a | n/a |
| docker (PID 146164) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 146186) rss_mb | MB | 1 | 20.500 | 20.500 | 20.500 | 20.500 | n/a | n/a |
| docker (PID 146186) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 146247) rss_mb | MB | 1 | 22.160 | 22.160 | 22.160 | 22.160 | n/a | n/a |
| docker (PID 146247) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 146256) CPU | percent | 1 | 9.413 | 9.413 | 9.413 | 9.413 | 0.010000 CPU seconds | n/a |
| docker (PID 146256) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 146256) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 146256) rss_mb | MB | 2 | 14.059 | 2.258 | 25.859 | 25.859 | n/a | n/a |
| docker (PID 146256) vms_mb | MB | 2 | 846.486 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| run4:repair_bug (PID 146306) rss_mb | MB | 1 | 680.781 | 680.781 | 680.781 | 680.781 | n/a | n/a |
| run4:repair_bug (PID 146306) vms_mb | MB | 1 | 3967.781 | 3967.781 | 3967.781 | 3967.781 | n/a | n/a |
| docker (PID 146314) CPU | percent | 3 | 15.243 | 0.000 | 45.730 | 0.000 | 0.050000 CPU seconds | n/a |
| docker (PID 146314) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 146314) io write MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 146314) rss_mb | MB | 4 | 20.173 | 0.559 | 26.711 | 26.711 | n/a | n/a |
| docker (PID 146314) vms_mb | MB | 4 | 1253.768 | 32.750 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 146353) CPU | percent | 14 | 3.932 | 0.000 | 55.054 | 0.000 | 0.060000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 146353) rss_mb | MB | 15 | 2.111 | 0.633 | 13.000 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 146353) vms_mb | MB | 15 | 219.876 | 1.055 | 1642.730 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 146368) CPU | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 146368) rss_mb | MB | 13 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [alex_0000] (PID 146368) vms_mb | MB | 13 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 146370) rss_mb | MB | 1 | 14.383 | 14.383 | 14.383 | 14.383 | n/a | n/a |
| docker (PID 146370) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 146378) rss_mb | MB | 1 | 26.980 | 26.980 | 26.980 | 26.980 | n/a | n/a |
| docker (PID 146378) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 146397) rss_mb | MB | 1 | 10.875 | 10.875 | 10.875 | 10.875 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 146397) vms_mb | MB | 1 | 1569.445 | 1569.445 | 1569.445 | 1569.445 | n/a | n/a |
| docker (PID 146404) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 146404) io read MB/s | MB/s | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 146404) io write MB/s | MB/s | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 146404) rss_mb | MB | 10 | 26.914 | 26.914 | 26.914 | 26.914 | n/a | n/a |
| docker (PID 146404) vms_mb | MB | 10 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 146424) CPU | percent | 9 | 5.410 | 0.000 | 48.686 | 0.000 | 0.050000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 146424) rss_mb | MB | 10 | 3.520 | 3.426 | 4.371 | 3.426 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 146424) vms_mb | MB | 10 | 148.071 | 4.391 | 1441.195 | 4.391 | n/a | n/a |
| python [alex_0000] (PID 146434) CPU | percent | 8 | 100.251 | 88.065 | 107.851 | 106.964 | 0.820000 CPU seconds | n/a |
| python [alex_0000] (PID 146434) rss_mb | MB | 9 | 30.257 | 10.621 | 42.766 | 42.766 | n/a | n/a |
| python [alex_0000] (PID 146434) vms_mb | MB | 9 | 37.054 | 14.770 | 52.238 | 52.238 | n/a | n/a |
| docker (PID 146444) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 146444) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 146444) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 146444) rss_mb | MB | 2 | 25.957 | 25.957 | 25.957 | 25.957 | n/a | n/a |
| docker (PID 146444) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 146503) CPU | percent | 1 | 9.879 | 9.879 | 9.879 | 9.879 | 0.010000 CPU seconds | n/a |
| docker (PID 146503) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 146503) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 146503) rss_mb | MB | 2 | 26.664 | 26.352 | 26.977 | 26.977 | n/a | n/a |
| docker (PID 146503) vms_mb | MB | 2 | 1660.492 | 1660.211 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 146543) CPU | percent | 3 | 3.250 | 0.000 | 9.750 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 146543) rss_mb | MB | 4 | 3.743 | 0.633 | 13.074 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 146543) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 146555) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 146555) rss_mb | MB | 3 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [alex_0000] (PID 146555) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 146566) rss_mb | MB | 1 | 27.273 | 27.273 | 27.273 | 27.273 | n/a | n/a |
| docker (PID 146566) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 146586) rss_mb | MB | 1 | 10.812 | 10.812 | 10.812 | 10.812 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 146586) vms_mb | MB | 1 | 1569.711 | 1569.711 | 1569.711 | 1569.711 | n/a | n/a |
| docker (PID 146623) rss_mb | MB | 1 | 4.477 | 4.477 | 4.477 | 4.477 | n/a | n/a |
| docker (PID 146623) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 146659) rss_mb | MB | 1 | 12.801 | 12.801 | 12.801 | 12.801 | n/a | n/a |
| docker (PID 146659) vms_mb | MB | 1 | 1451.699 | 1451.699 | 1451.699 | 1451.699 | n/a | n/a |
| docker (PID 146668) rss_mb | MB | 1 | 26.902 | 26.902 | 26.902 | 26.902 | n/a | n/a |
| docker (PID 146668) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 146753) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 146753) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 146753) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 146753) rss_mb | MB | 39 | 25.223 | 25.223 | 25.223 | 25.223 | n/a | n/a |
| docker (PID 146753) vms_mb | MB | 39 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 146777) rss_mb | MB | 1 | 2.406 | 2.406 | 2.406 | 2.406 | n/a | n/a |
| docker (PID 146777) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| python3 (PID 146800) CPU | percent | 3 | 98.816 | 88.939 | 108.791 | 88.939 | 0.300000 CPU seconds | n/a |
| python3 (PID 146800) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 146800) io write MB/s | MB/s | 3 | 0.849 | 0.000 | 2.548 | 2.548 | 0.257812 MB | n/a |
| python3 (PID 146800) rss_mb | MB | 4 | 28.708 | 18.793 | 34.789 | 34.789 | n/a | n/a |
| python3 (PID 146800) vms_mb | MB | 4 | 52.146 | 43.703 | 57.469 | 57.469 | n/a | n/a |
| docker (PID 146826) rss_mb | MB | 1 | 26.578 | 26.578 | 26.578 | 26.578 | n/a | n/a |
| docker (PID 146826) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 146851) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 146851) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 146851) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 146851) rss_mb | MB | 3 | 27.383 | 27.062 | 27.543 | 27.543 | n/a | n/a |
| docker (PID 146851) vms_mb | MB | 3 | 1756.779 | 1660.773 | 1804.781 | 1804.781 | n/a | n/a |
| docker-init [bake_0000] (PID 146895) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bake_0000] (PID 146895) rss_mb | MB | 6 | 2.711 | 0.633 | 13.102 | 0.633 | n/a | n/a |
| docker-init [bake_0000] (PID 146895) vms_mb | MB | 6 | 274.667 | 1.055 | 1642.730 | 1.055 | n/a | n/a |
| docker (PID 146917) rss_mb | MB | 1 | 25.598 | 25.598 | 25.598 | 25.598 | n/a | n/a |
| docker (PID 146917) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| tail [bake_0000] (PID 146935) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 146935) rss_mb | MB | 5 | 1.809 | 1.809 | 1.809 | 1.809 | n/a | n/a |
| tail [bake_0000] (PID 146935) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 146938) CPU | percent | 42 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 146938) io read MB/s | MB/s | 42 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 146938) io write MB/s | MB/s | 42 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 146938) rss_mb | MB | 43 | 25.746 | 25.746 | 25.746 | 25.746 | n/a | n/a |
| docker (PID 146938) vms_mb | MB | 43 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 146940) rss_mb | MB | 1 | 26.930 | 26.930 | 26.930 | 26.930 | n/a | n/a |
| docker (PID 146940) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] (PID 146967) rss_mb | MB | 1 | 11.809 | 11.809 | 11.809 | 11.809 | n/a | n/a |
| runc:[2:INIT] (PID 146967) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 146983) rss_mb | MB | 1 | 25.906 | 25.906 | 25.906 | 25.906 | n/a | n/a |
| docker (PID 146983) vms_mb | MB | 1 | 1659.961 | 1659.961 | 1659.961 | 1659.961 | n/a | n/a |
| docker (PID 147010) rss_mb | MB | 1 | 27.328 | 27.328 | 27.328 | 27.328 | n/a | n/a |
| docker (PID 147010) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 147047) rss_mb | MB | 1 | 27.480 | 27.480 | 27.480 | 27.480 | n/a | n/a |
| docker (PID 147047) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 147083) CPU | percent | 1 | 9.686 | 9.686 | 9.686 | 9.686 | 0.010000 CPU seconds | n/a |
| docker (PID 147083) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 147083) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 147083) rss_mb | MB | 2 | 13.688 | 1.375 | 26.000 | 26.000 | n/a | n/a |
| docker (PID 147083) vms_mb | MB | 2 | 846.486 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 147132) rss_mb | MB | 1 | 15.688 | 15.688 | 15.688 | 15.688 | n/a | n/a |
| docker (PID 147132) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 147141) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 147141) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 147141) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 147141) rss_mb | MB | 2 | 25.414 | 25.414 | 25.414 | 25.414 | n/a | n/a |
| docker (PID 147141) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 147183) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 147183) rss_mb | MB | 5 | 3.091 | 0.633 | 12.922 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 147183) vms_mb | MB | 5 | 329.290 | 1.055 | 1642.230 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 147196) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 147196) rss_mb | MB | 4 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [bake_0000] (PID 147196) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 147206) rss_mb | MB | 1 | 27.223 | 27.223 | 27.223 | 27.223 | n/a | n/a |
| docker (PID 147206) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 147232) rss_mb | MB | 1 | 27.309 | 27.309 | 27.309 | 27.309 | n/a | n/a |
| docker (PID 147232) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 147268) rss_mb | MB | 1 | 2.090 | 2.090 | 2.090 | 2.090 | n/a | n/a |
| docker (PID 147268) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 147296) rss_mb | MB | 1 | 4.734 | 4.734 | 4.734 | 4.734 | n/a | n/a |
| docker (PID 147296) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 147304) rss_mb | MB | 1 | 25.820 | 25.820 | 25.820 | 25.820 | n/a | n/a |
| docker (PID 147304) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 147343) rss_mb | MB | 1 | 25.051 | 25.051 | 25.051 | 25.051 | n/a | n/a |
| docker (PID 147343) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 147360) rss_mb | MB | 1 | 10.648 | 10.648 | 10.648 | 10.648 | n/a | n/a |
| docker (PID 147360) vms_mb | MB | 1 | 1323.949 | 1323.949 | 1323.949 | 1323.949 | n/a | n/a |
| docker (PID 147387) CPU | percent | 2 | 4.920 | 0.000 | 9.840 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 147387) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 147387) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 147387) rss_mb | MB | 3 | 19.229 | 5.906 | 25.891 | 25.891 | n/a | n/a |
| docker (PID 147387) vms_mb | MB | 3 | 1117.728 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 147403) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 147403) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 147403) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 147403) rss_mb | MB | 2 | 26.977 | 26.977 | 26.977 | 26.977 | n/a | n/a |
| docker (PID 147403) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [arch_0000] (PID 147464) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [arch_0000] (PID 147464) rss_mb | MB | 5 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [arch_0000] (PID 147464) vms_mb | MB | 5 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 147481) CPU | percent | 4 | 2.425 | 0.000 | 9.702 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 147481) rss_mb | MB | 5 | 3.074 | 0.633 | 12.840 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 147481) vms_mb | MB | 5 | 314.939 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 147494) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 147494) rss_mb | MB | 5 | 1.707 | 1.707 | 1.707 | 1.707 | n/a | n/a |
| tail [arch_0000] (PID 147494) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| tail [bake_0000] (PID 147503) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 147503) rss_mb | MB | 4 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [bake_0000] (PID 147503) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 147517) rss_mb | MB | 1 | 27.066 | 27.066 | 27.066 | 27.066 | n/a | n/a |
| docker (PID 147517) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 147526) rss_mb | MB | 1 | 26.816 | 26.816 | 26.816 | 26.816 | n/a | n/a |
| docker (PID 147526) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 147545) rss_mb | MB | 1 | 10.723 | 10.723 | 10.723 | 10.723 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 147545) vms_mb | MB | 1 | 1569.453 | 1569.453 | 1569.453 | 1569.453 | n/a | n/a |
| docker (PID 147570) rss_mb | MB | 1 | 27.316 | 27.316 | 27.316 | 27.316 | n/a | n/a |
| docker (PID 147570) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 147577) rss_mb | MB | 1 | 27.422 | 27.422 | 27.422 | 27.422 | n/a | n/a |
| docker (PID 147577) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 147599) rss_mb | MB | 1 | 11.578 | 11.578 | 11.578 | 11.578 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 147599) vms_mb | MB | 1 | 1570.090 | 1570.090 | 1570.090 | 1570.090 | n/a | n/a |
| docker (PID 147642) rss_mb | MB | 1 | 27.277 | 27.277 | 27.277 | 27.277 | n/a | n/a |
| docker (PID 147642) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 147645) rss_mb | MB | 1 | 25.824 | 25.824 | 25.824 | 25.824 | n/a | n/a |
| docker (PID 147645) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 147702) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 147702) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 147704) rss_mb | MB | 1 | 25.867 | 25.867 | 25.867 | 25.867 | n/a | n/a |
| docker (PID 147704) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 147719) rss_mb | MB | 1 | 26.113 | 26.113 | 26.113 | 26.113 | n/a | n/a |
| docker (PID 147719) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 147721) rss_mb | MB | 1 | 26.809 | 26.809 | 26.809 | 26.809 | n/a | n/a |
| docker (PID 147721) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 147828) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 147828) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 147828) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 147828) rss_mb | MB | 2 | 26.754 | 26.629 | 26.879 | 26.879 | n/a | n/a |
| docker (PID 147828) vms_mb | MB | 2 | 1660.648 | 1660.523 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 147867) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 147867) rss_mb | MB | 11 | 1.761 | 0.633 | 13.047 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 147867) vms_mb | MB | 11 | 143.752 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 147880) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 147880) rss_mb | MB | 10 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [arch_0000] (PID 147880) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 147890) rss_mb | MB | 1 | 26.844 | 26.844 | 26.844 | 26.844 | n/a | n/a |
| docker (PID 147890) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 147909) rss_mb | MB | 1 | 11.547 | 11.547 | 11.547 | 11.547 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 147909) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 147916) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 147916) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 147916) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 147916) rss_mb | MB | 8 | 27.371 | 27.371 | 27.371 | 27.371 | n/a | n/a |
| docker (PID 147916) vms_mb | MB | 8 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [arch_0000] (PID 147936) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [arch_0000] (PID 147936) rss_mb | MB | 8 | 3.441 | 3.441 | 3.441 | 3.441 | n/a | n/a |
| bash [arch_0000] (PID 147936) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [arch_0000] (PID 147946) CPU | percent | 7 | 100.235 | 95.271 | 117.817 | 97.940 | 0.730000 CPU seconds | n/a |
| python [arch_0000] (PID 147946) rss_mb | MB | 8 | 30.581 | 9.828 | 41.914 | 41.914 | n/a | n/a |
| python [arch_0000] (PID 147946) vms_mb | MB | 8 | 37.700 | 13.531 | 51.219 | 51.219 | n/a | n/a |
| docker (PID 147956) rss_mb | MB | 1 | 27.055 | 27.055 | 27.055 | 27.055 | n/a | n/a |
| docker (PID 147956) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 148013) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 148013) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 148013) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 148013) rss_mb | MB | 2 | 25.535 | 25.535 | 25.535 | 25.535 | n/a | n/a |
| docker (PID 148013) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 148052) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 148052) rss_mb | MB | 4 | 3.723 | 0.633 | 12.992 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 148052) vms_mb | MB | 4 | 393.473 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 148065) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 148065) rss_mb | MB | 3 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [arch_0000] (PID 148065) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 148075) rss_mb | MB | 1 | 27.340 | 27.340 | 27.340 | 27.340 | n/a | n/a |
| docker (PID 148075) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 148096) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 148096) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| docker (PID 148138) rss_mb | MB | 1 | 18.234 | 18.234 | 18.234 | 18.234 | n/a | n/a |
| docker (PID 148138) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 148174) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 148174) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 148174) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 148174) rss_mb | MB | 2 | 25.852 | 25.852 | 25.852 | 25.852 | n/a | n/a |
| docker (PID 148174) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 148253) rss_mb | MB | 1 | 26.559 | 26.559 | 26.559 | 26.559 | n/a | n/a |
| docker (PID 148253) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 148261) CPU | percent | 48 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 148261) io read MB/s | MB/s | 48 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 148261) io write MB/s | MB/s | 48 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 148261) rss_mb | MB | 49 | 26.707 | 26.707 | 26.707 | 26.707 | n/a | n/a |
| docker (PID 148261) vms_mb | MB | 49 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 148285) rss_mb | MB | 1 | 0.129 | 0.129 | 0.129 | 0.129 | n/a | n/a |
| docker (PID 148285) vms_mb | MB | 1 | 30.570 | 30.570 | 30.570 | 30.570 | n/a | n/a |
| docker (PID 148300) CPU | percent | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 148300) io read MB/s | MB/s | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 148300) io write MB/s | MB/s | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 148300) rss_mb | MB | 51 | 25.312 | 25.312 | 25.312 | 25.312 | n/a | n/a |
| docker (PID 148300) vms_mb | MB | 51 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 148325) rss_mb | MB | 1 | 25.742 | 25.742 | 25.742 | 25.742 | n/a | n/a |
| docker (PID 148325) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 148343) rss_mb | MB | 1 | 25.961 | 25.961 | 25.961 | 25.961 | n/a | n/a |
| docker (PID 148343) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| python3 (PID 148350) CPU | percent | 6 | 94.707 | 86.719 | 98.729 | 98.034 | 0.580000 CPU seconds | n/a |
| python3 (PID 148350) io read MB/s | MB/s | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 148350) io write MB/s | MB/s | 6 | 0.466 | 0.000 | 2.796 | 0.000 | 0.285156 MB | n/a |
| python3 (PID 148350) rss_mb | MB | 7 | 27.270 | 12.484 | 34.781 | 34.781 | n/a | n/a |
| python3 (PID 148350) vms_mb | MB | 7 | 51.111 | 38.293 | 57.441 | 57.441 | n/a | n/a |
| docker (PID 148369) rss_mb | MB | 1 | 26.129 | 26.129 | 26.129 | 26.129 | n/a | n/a |
| docker (PID 148369) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 148396) rss_mb | MB | 1 | 26.477 | 26.477 | 26.477 | 26.477 | n/a | n/a |
| docker (PID 148396) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 148414) rss_mb | MB | 1 | 15.289 | 15.289 | 15.289 | 15.289 | n/a | n/a |
| docker (PID 148414) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 148422) rss_mb | MB | 1 | 26.746 | 26.746 | 26.746 | 26.746 | n/a | n/a |
| docker (PID 148422) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 148461) CPU | percent | 4 | 7.345 | 0.000 | 29.379 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 148461) rss_mb | MB | 5 | 2.846 | 0.633 | 11.699 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 148461) vms_mb | MB | 5 | 314.836 | 1.055 | 1569.961 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 148473) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 148473) rss_mb | MB | 4 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [bake_0000] (PID 148473) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 148483) rss_mb | MB | 1 | 27.246 | 27.246 | 27.246 | 27.246 | n/a | n/a |
| docker (PID 148483) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 148524) rss_mb | MB | 1 | 27.320 | 27.320 | 27.320 | 27.320 | n/a | n/a |
| docker (PID 148524) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 148526) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 148526) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 148526) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 148526) rss_mb | MB | 3 | 27.589 | 27.312 | 27.727 | 27.727 | n/a | n/a |
| docker (PID 148526) vms_mb | MB | 3 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 148553) rss_mb | MB | 1 | 4.246 | 4.246 | 4.246 | 4.246 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 148553) vms_mb | MB | 1 | 1216.680 | 1216.680 | 1216.680 | 1216.680 | n/a | n/a |
| docker (PID 148569) rss_mb | MB | 1 | 27.102 | 27.102 | 27.102 | 27.102 | n/a | n/a |
| docker (PID 148569) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [bale_0000] (PID 148628) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bale_0000] (PID 148628) rss_mb | MB | 5 | 3.134 | 0.633 | 13.141 | 0.633 | n/a | n/a |
| docker-init [bale_0000] (PID 148628) vms_mb | MB | 5 | 314.939 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| docker (PID 148638) rss_mb | MB | 1 | 25.730 | 25.730 | 25.730 | 25.730 | n/a | n/a |
| docker (PID 148638) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 148647) rss_mb | MB | 1 | 26.941 | 26.941 | 26.941 | 26.941 | n/a | n/a |
| docker (PID 148647) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| tail [bale_0000] (PID 148660) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 148660) rss_mb | MB | 4 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [bale_0000] (PID 148660) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 148662) rss_mb | MB | 1 | 27.000 | 27.000 | 27.000 | 27.000 | n/a | n/a |
| docker (PID 148662) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] (PID 148704) rss_mb | MB | 1 | 10.773 | 10.773 | 10.773 | 10.773 | n/a | n/a |
| runc:[2:INIT] (PID 148704) vms_mb | MB | 1 | 1569.711 | 1569.711 | 1569.711 | 1569.711 | n/a | n/a |
| docker (PID 148740) rss_mb | MB | 1 | 27.305 | 27.305 | 27.305 | 27.305 | n/a | n/a |
| docker (PID 148740) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 148797) rss_mb | MB | 1 | 5.016 | 5.016 | 5.016 | 5.016 | n/a | n/a |
| docker (PID 148797) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 148843) CPU | percent | 1 | 9.791 | 9.791 | 9.791 | 9.791 | 0.010000 CPU seconds | n/a |
| docker (PID 148843) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 148843) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 148843) rss_mb | MB | 2 | 14.037 | 1.781 | 26.293 | 26.293 | n/a | n/a |
| docker (PID 148843) vms_mb | MB | 2 | 846.486 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 148902) CPU | percent | 1 | 9.851 | 9.851 | 9.851 | 9.851 | 0.010000 CPU seconds | n/a |
| docker (PID 148902) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 148902) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 148902) rss_mb | MB | 2 | 24.916 | 23.172 | 26.660 | 26.660 | n/a | n/a |
| docker (PID 148902) vms_mb | MB | 2 | 1624.488 | 1588.203 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 148941) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 148941) rss_mb | MB | 4 | 3.709 | 0.633 | 12.938 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 148941) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 148953) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 148953) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [bale_0000] (PID 148953) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 148963) rss_mb | MB | 1 | 27.359 | 27.359 | 27.359 | 27.359 | n/a | n/a |
| docker (PID 148963) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 148983) rss_mb | MB | 1 | 11.402 | 11.402 | 11.402 | 11.402 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 148983) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 149019) rss_mb | MB | 1 | 26.980 | 26.980 | 26.980 | 26.980 | n/a | n/a |
| docker (PID 149019) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 149064) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 149064) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 149064) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 149064) rss_mb | MB | 2 | 24.863 | 23.781 | 25.945 | 25.945 | n/a | n/a |
| docker (PID 149064) vms_mb | MB | 2 | 1624.207 | 1588.203 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 149123) CPU | percent | 1 | 9.444 | 9.444 | 9.444 | 9.444 | 0.010000 CPU seconds | n/a |
| docker (PID 149123) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 149123) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 149123) rss_mb | MB | 2 | 25.506 | 24.316 | 26.695 | 26.695 | n/a | n/a |
| docker (PID 149123) vms_mb | MB | 2 | 1660.492 | 1660.211 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 149163) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 149163) rss_mb | MB | 11 | 1.751 | 0.633 | 12.930 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 149163) vms_mb | MB | 11 | 143.729 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 149176) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 149176) rss_mb | MB | 10 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [bake_0000] (PID 149176) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 149186) rss_mb | MB | 1 | 27.324 | 27.324 | 27.324 | 27.324 | n/a | n/a |
| docker (PID 149186) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 149206) rss_mb | MB | 1 | 12.008 | 12.008 | 12.008 | 12.008 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 149206) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 149213) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 149213) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 149213) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 149213) rss_mb | MB | 9 | 27.352 | 27.352 | 27.352 | 27.352 | n/a | n/a |
| docker (PID 149213) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [bake_0000] (PID 149232) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bake_0000] (PID 149232) rss_mb | MB | 9 | 3.395 | 3.395 | 3.395 | 3.395 | n/a | n/a |
| bash [bake_0000] (PID 149232) vms_mb | MB | 9 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bake_0000] (PID 149240) CPU | percent | 8 | 100.223 | 88.192 | 107.869 | 97.568 | 0.820000 CPU seconds | n/a |
| python [bake_0000] (PID 149240) rss_mb | MB | 9 | 31.474 | 10.223 | 41.832 | 41.832 | n/a | n/a |
| python [bake_0000] (PID 149240) vms_mb | MB | 9 | 38.414 | 14.531 | 51.375 | 51.375 | n/a | n/a |
| docker (PID 149251) rss_mb | MB | 1 | 25.953 | 25.953 | 25.953 | 25.953 | n/a | n/a |
| docker (PID 149251) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 149309) rss_mb | MB | 1 | 26.590 | 26.590 | 26.590 | 26.590 | n/a | n/a |
| docker (PID 149309) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 149347) CPU | percent | 3 | 6.446 | 0.000 | 19.337 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 149347) rss_mb | MB | 4 | 3.237 | 0.633 | 11.051 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 149347) vms_mb | MB | 4 | 393.277 | 1.055 | 1569.945 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 149360) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 149360) rss_mb | MB | 3 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [bake_0000] (PID 149360) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 149371) rss_mb | MB | 1 | 19.598 | 19.598 | 19.598 | 19.598 | n/a | n/a |
| docker (PID 149371) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 149398) rss_mb | MB | 1 | 26.953 | 26.953 | 26.953 | 26.953 | n/a | n/a |
| docker (PID 149398) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 149418) rss_mb | MB | 1 | 11.555 | 11.555 | 11.555 | 11.555 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 149418) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 149433) rss_mb | MB | 1 | 27.391 | 27.391 | 27.391 | 27.391 | n/a | n/a |
| docker (PID 149433) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 149452) rss_mb | MB | 1 | 11.523 | 11.523 | 11.523 | 11.523 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 149452) vms_mb | MB | 1 | 1642.230 | 1642.230 | 1642.230 | 1642.230 | n/a | n/a |
| docker (PID 149469) rss_mb | MB | 1 | 26.000 | 26.000 | 26.000 | 26.000 | n/a | n/a |
| docker (PID 149469) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 149537) rss_mb | MB | 1 | 6.344 | 6.344 | 6.344 | 6.344 | n/a | n/a |
| docker (PID 149537) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 149555) CPU | percent | 53 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 149555) io read MB/s | MB/s | 53 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 149555) io write MB/s | MB/s | 53 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 149555) rss_mb | MB | 54 | 27.012 | 27.012 | 27.012 | 27.012 | n/a | n/a |
| docker (PID 149555) vms_mb | MB | 54 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 149581) rss_mb | MB | 1 | 22.539 | 22.539 | 22.539 | 22.539 | n/a | n/a |
| docker (PID 149581) vms_mb | MB | 1 | 1524.203 | 1524.203 | 1524.203 | 1524.203 | n/a | n/a |
| python3 (PID 149605) CPU | percent | 3 | 98.766 | 98.458 | 98.939 | 98.939 | 0.300000 CPU seconds | n/a |
| python3 (PID 149605) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 149605) io write MB/s | MB/s | 3 | 0.928 | 0.000 | 2.783 | 2.783 | 0.281250 MB | n/a |
| python3 (PID 149605) rss_mb | MB | 4 | 28.784 | 20.355 | 34.547 | 34.547 | n/a | n/a |
| python3 (PID 149605) vms_mb | MB | 4 | 52.458 | 45.188 | 57.441 | 57.441 | n/a | n/a |
| docker (PID 149623) rss_mb | MB | 1 | 26.227 | 26.227 | 26.227 | 26.227 | n/a | n/a |
| docker (PID 149623) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 149639) rss_mb | MB | 1 | 2.219 | 2.219 | 2.219 | 2.219 | n/a | n/a |
| docker (PID 149639) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 149671) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 149671) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 149671) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 149671) rss_mb | MB | 39 | 25.344 | 25.344 | 25.344 | 25.344 | n/a | n/a |
| docker (PID 149671) vms_mb | MB | 39 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 149713) rss_mb | MB | 1 | 26.922 | 26.922 | 26.922 | 26.922 | n/a | n/a |
| docker (PID 149713) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 149727) CPU | percent | 1 | 9.878 | 9.878 | 9.878 | 9.878 | 0.010000 CPU seconds | n/a |
| docker (PID 149727) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 149727) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 149727) rss_mb | MB | 2 | 27.334 | 27.180 | 27.488 | 27.488 | n/a | n/a |
| docker (PID 149727) vms_mb | MB | 2 | 1732.777 | 1660.773 | 1804.781 | 1804.781 | n/a | n/a |
| docker-init [band_0000] (PID 149770) CPU | percent | 4 | 2.460 | 0.000 | 9.841 | 0.000 | 0.010000 CPU seconds | n/a |
| docker-init [band_0000] (PID 149770) rss_mb | MB | 5 | 2.972 | 0.633 | 12.328 | 0.633 | n/a | n/a |
| docker-init [band_0000] (PID 149770) vms_mb | MB | 5 | 314.939 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 149782) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 149782) rss_mb | MB | 4 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [band_0000] (PID 149782) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 149784) rss_mb | MB | 1 | 27.090 | 27.090 | 27.090 | 27.090 | n/a | n/a |
| docker (PID 149784) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] (PID 149803) rss_mb | MB | 1 | 11.859 | 11.859 | 11.859 | 11.859 | n/a | n/a |
| runc:[2:INIT] (PID 149803) vms_mb | MB | 1 | 1570.977 | 1570.977 | 1570.977 | 1570.977 | n/a | n/a |
| docker (PID 149818) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 149818) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 149882) rss_mb | MB | 1 | 22.566 | 22.566 | 22.566 | 22.566 | n/a | n/a |
| docker (PID 149882) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 149918) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 149918) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 149918) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 149918) rss_mb | MB | 2 | 25.945 | 25.945 | 25.945 | 25.945 | n/a | n/a |
| docker (PID 149918) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 149975) rss_mb | MB | 1 | 27.094 | 27.094 | 27.094 | 27.094 | n/a | n/a |
| docker (PID 149975) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [band_0000] (PID 150015) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [band_0000] (PID 150015) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [band_0000] (PID 150015) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 150027) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 150027) rss_mb | MB | 3 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [band_0000] (PID 150027) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 150030) rss_mb | MB | 1 | 2.664 | 2.664 | 2.664 | 2.664 | n/a | n/a |
| docker (PID 150030) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 150066) rss_mb | MB | 1 | 25.504 | 25.504 | 25.504 | 25.504 | n/a | n/a |
| docker (PID 150066) vms_mb | MB | 1 | 1596.211 | 1596.211 | 1596.211 | 1596.211 | n/a | n/a |
| docker (PID 150102) rss_mb | MB | 1 | 27.109 | 27.109 | 27.109 | 27.109 | n/a | n/a |
| docker (PID 150102) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 150139) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 150139) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 150139) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 150139) rss_mb | MB | 2 | 27.070 | 27.070 | 27.070 | 27.070 | n/a | n/a |
| docker (PID 150139) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 150198) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 150198) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 150198) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 150198) rss_mb | MB | 2 | 27.113 | 27.113 | 27.113 | 27.113 | n/a | n/a |
| docker (PID 150198) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [bale_0000] (PID 150237) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bale_0000] (PID 150237) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bale_0000] (PID 150237) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 150250) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 150250) rss_mb | MB | 4 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [bale_0000] (PID 150250) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 150286) rss_mb | MB | 1 | 9.461 | 9.461 | 9.461 | 9.461 | n/a | n/a |
| docker (PID 150286) vms_mb | MB | 1 | 1323.699 | 1323.699 | 1323.699 | 1323.699 | n/a | n/a |
| docker (PID 150324) rss_mb | MB | 1 | 26.859 | 26.859 | 26.859 | 26.859 | n/a | n/a |
| docker (PID 150324) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 150361) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 150361) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 150361) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 150361) rss_mb | MB | 2 | 27.137 | 27.137 | 27.137 | 27.137 | n/a | n/a |
| docker (PID 150361) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 150420) rss_mb | MB | 1 | 26.398 | 26.398 | 26.398 | 26.398 | n/a | n/a |
| docker (PID 150420) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [bale_0000] (PID 150461) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bale_0000] (PID 150461) rss_mb | MB | 37 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bale_0000] (PID 150461) vms_mb | MB | 37 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 150474) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 150474) rss_mb | MB | 37 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bale_0000] (PID 150474) vms_mb | MB | 37 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 150476) rss_mb | MB | 1 | 4.836 | 4.836 | 4.836 | 4.836 | n/a | n/a |
| docker (PID 150476) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 150511) CPU | percent | 35 | 0.556 | 0.000 | 19.473 | 0.000 | 0.020000 CPU seconds | n/a |
| docker (PID 150511) io read MB/s | MB/s | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 150511) io write MB/s | MB/s | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 150511) rss_mb | MB | 36 | 27.315 | 25.766 | 27.359 | 27.359 | n/a | n/a |
| docker (PID 150511) vms_mb | MB | 36 | 1660.760 | 1660.273 | 1660.773 | 1660.773 | n/a | n/a |
| bash [bale_0000] (PID 150531) CPU | percent | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bale_0000] (PID 150531) rss_mb | MB | 35 | 3.449 | 3.449 | 3.449 | 3.449 | n/a | n/a |
| bash [bale_0000] (PID 150531) vms_mb | MB | 35 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bale_0000] (PID 150541) CPU | percent | 34 | 99.776 | 88.223 | 117.788 | 107.919 | 3.460000 CPU seconds | n/a |
| python [bale_0000] (PID 150541) rss_mb | MB | 35 | 39.573 | 13.387 | 41.824 | 41.824 | n/a | n/a |
| python [bale_0000] (PID 150541) vms_mb | MB | 35 | 48.493 | 16.527 | 51.324 | 51.324 | n/a | n/a |
| docker (PID 150551) rss_mb | MB | 1 | 25.703 | 25.703 | 25.703 | 25.703 | n/a | n/a |
| docker (PID 150551) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 150597) rss_mb | MB | 1 | 6.516 | 6.516 | 6.516 | 6.516 | n/a | n/a |
| docker (PID 150597) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 150606) rss_mb | MB | 1 | 11.148 | 11.148 | 11.148 | 11.148 | n/a | n/a |
| docker (PID 150606) vms_mb | MB | 1 | 1451.949 | 1451.949 | 1451.949 | 1451.949 | n/a | n/a |
| docker (PID 150614) rss_mb | MB | 1 | 26.754 | 26.754 | 26.754 | 26.754 | n/a | n/a |
| docker (PID 150614) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 150653) CPU | percent | 3 | 9.724 | 0.000 | 29.172 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 150653) rss_mb | MB | 4 | 3.226 | 0.539 | 11.285 | 0.539 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 150653) vms_mb | MB | 4 | 393.152 | 1.055 | 1569.445 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 150667) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 150667) rss_mb | MB | 3 | 1.809 | 1.809 | 1.809 | 1.809 | n/a | n/a |
| tail [bale_0000] (PID 150667) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 150677) rss_mb | MB | 1 | 22.785 | 22.785 | 22.785 | 22.785 | n/a | n/a |
| docker (PID 150677) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 150704) rss_mb | MB | 1 | 26.984 | 26.984 | 26.984 | 26.984 | n/a | n/a |
| docker (PID 150704) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 150724) rss_mb | MB | 1 | 11.863 | 11.863 | 11.863 | 11.863 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 150724) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 150740) rss_mb | MB | 1 | 27.320 | 27.320 | 27.320 | 27.320 | n/a | n/a |
| docker (PID 150740) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 150760) rss_mb | MB | 1 | 12.199 | 12.199 | 12.199 | 12.199 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 150760) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 150777) rss_mb | MB | 1 | 25.887 | 25.887 | 25.887 | 25.887 | n/a | n/a |
| docker (PID 150777) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 150853) rss_mb | MB | 1 | 9.363 | 9.363 | 9.363 | 9.363 | n/a | n/a |
| docker (PID 150853) vms_mb | MB | 1 | 1379.695 | 1379.695 | 1379.695 | 1379.695 | n/a | n/a |
| docker (PID 150861) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 150861) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 150861) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 150861) rss_mb | MB | 39 | 26.395 | 26.395 | 26.395 | 26.395 | n/a | n/a |
| docker (PID 150861) vms_mb | MB | 39 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 150886) rss_mb | MB | 1 | 16.344 | 16.344 | 16.344 | 16.344 | n/a | n/a |
| docker (PID 150886) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| python3 (PID 150909) CPU | percent | 23 | 100.200 | 98.531 | 108.872 | 98.988 | 2.330000 CPU seconds | n/a |
| python3 (PID 150909) io read MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 150909) io write MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 150909) rss_mb | MB | 24 | 33.174 | 20.289 | 34.016 | 34.016 | n/a | n/a |
| python3 (PID 150909) vms_mb | MB | 24 | 56.643 | 45.188 | 57.469 | 57.469 | n/a | n/a |
| docker (PID 150911) rss_mb | MB | 1 | 10.512 | 10.512 | 10.512 | 10.512 | n/a | n/a |
| docker (PID 150911) vms_mb | MB | 1 | 1451.699 | 1451.699 | 1451.699 | 1451.699 | n/a | n/a |
| docker (PID 150938) rss_mb | MB | 1 | 25.469 | 25.469 | 25.469 | 25.469 | n/a | n/a |
| docker (PID 150938) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 150966) rss_mb | MB | 1 | 25.461 | 25.461 | 25.461 | 25.461 | n/a | n/a |
| docker (PID 150966) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 150981) CPU | percent | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 150981) io read MB/s | MB/s | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 150981) io write MB/s | MB/s | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 150981) rss_mb | MB | 45 | 25.159 | 0.000 | 25.730 | 0.000 | n/a | n/a |
| docker (PID 150981) vms_mb | MB | 45 | 1623.317 | 0.000 | 1660.211 | 0.000 | n/a | n/a |
| docker (PID 150989) rss_mb | MB | 1 | 17.875 | 17.875 | 17.875 | 17.875 | n/a | n/a |
| docker (PID 150989) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 151003) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 151003) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 151003) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 151003) rss_mb | MB | 3 | 27.221 | 26.969 | 27.348 | 27.348 | n/a | n/a |
| docker (PID 151003) vms_mb | MB | 3 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [bart_0000] (PID 151043) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bart_0000] (PID 151043) rss_mb | MB | 6 | 2.723 | 0.633 | 13.172 | 0.633 | n/a | n/a |
| docker-init [bart_0000] (PID 151043) vms_mb | MB | 6 | 262.667 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 151055) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 151055) rss_mb | MB | 5 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [bart_0000] (PID 151055) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 151057) rss_mb | MB | 1 | 27.375 | 27.375 | 27.375 | 27.375 | n/a | n/a |
| docker (PID 151057) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] (PID 151076) rss_mb | MB | 1 | 11.730 | 11.730 | 11.730 | 11.730 | n/a | n/a |
| runc:[2:INIT] (PID 151076) vms_mb | MB | 1 | 1642.223 | 1642.223 | 1642.223 | 1642.223 | n/a | n/a |
| docker (PID 151092) rss_mb | MB | 1 | 27.500 | 27.500 | 27.500 | 27.500 | n/a | n/a |
| docker (PID 151092) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 151154) rss_mb | MB | 1 | 27.340 | 27.340 | 27.340 | 27.340 | n/a | n/a |
| docker (PID 151154) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 151176) rss_mb | MB | 1 | 11.961 | 11.961 | 11.961 | 11.961 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 151176) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 151193) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 151193) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 151193) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 151193) rss_mb | MB | 2 | 25.758 | 25.758 | 25.758 | 25.758 | n/a | n/a |
| docker (PID 151193) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 151254) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 151254) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 151254) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 151254) rss_mb | MB | 2 | 25.527 | 25.527 | 25.527 | 25.527 | n/a | n/a |
| docker (PID 151254) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 151294) CPU | percent | 5 | 7.806 | 0.000 | 39.031 | 0.000 | 0.040000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 151294) rss_mb | MB | 6 | 2.496 | 0.633 | 11.812 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 151294) vms_mb | MB | 6 | 274.580 | 1.055 | 1642.207 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 151307) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 151307) rss_mb | MB | 5 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bart_0000] (PID 151307) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 151311) rss_mb | MB | 1 | 23.906 | 23.906 | 23.906 | 23.906 | n/a | n/a |
| docker (PID 151311) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 151320) rss_mb | MB | 1 | 27.398 | 27.398 | 27.398 | 27.398 | n/a | n/a |
| docker (PID 151320) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 151338) rss_mb | MB | 1 | 12.023 | 12.023 | 12.023 | 12.023 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 151338) vms_mb | MB | 1 | 1642.980 | 1642.980 | 1642.980 | 1642.980 | n/a | n/a |
| docker (PID 151346) rss_mb | MB | 1 | 27.285 | 27.285 | 27.285 | 27.285 | n/a | n/a |
| docker (PID 151346) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 151364) rss_mb | MB | 1 | 11.949 | 11.949 | 11.949 | 11.949 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 151364) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 151381) rss_mb | MB | 1 | 27.453 | 27.453 | 27.453 | 27.453 | n/a | n/a |
| docker (PID 151381) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 151401) rss_mb | MB | 1 | 4.367 | 4.367 | 4.367 | 4.367 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 151401) vms_mb | MB | 1 | 1344.680 | 1344.680 | 1344.680 | 1344.680 | n/a | n/a |
| docker (PID 151417) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 151417) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 151417) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 151417) rss_mb | MB | 2 | 26.000 | 26.000 | 26.000 | 26.000 | n/a | n/a |
| docker (PID 151417) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 151505) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 151505) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 151505) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 151505) rss_mb | MB | 2 | 27.156 | 27.156 | 27.156 | 27.156 | n/a | n/a |
| docker (PID 151505) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 151544) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 151544) rss_mb | MB | 4 | 3.766 | 0.633 | 13.164 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 151544) vms_mb | MB | 4 | 393.473 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 151556) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 151556) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [band_0000] (PID 151556) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 151566) rss_mb | MB | 1 | 27.156 | 27.156 | 27.156 | 27.156 | n/a | n/a |
| docker (PID 151566) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 151587) rss_mb | MB | 1 | 12.547 | 12.547 | 12.547 | 12.547 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 151587) vms_mb | MB | 1 | 1570.977 | 1570.977 | 1570.977 | 1570.977 | n/a | n/a |
| docker (PID 151632) rss_mb | MB | 1 | 9.156 | 9.156 | 9.156 | 9.156 | n/a | n/a |
| docker (PID 151632) vms_mb | MB | 1 | 1235.438 | 1235.438 | 1235.438 | 1235.438 | n/a | n/a |
| docker (PID 151670) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 151670) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 151670) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 151670) rss_mb | MB | 2 | 25.887 | 25.887 | 25.887 | 25.887 | n/a | n/a |
| docker (PID 151670) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 151728) rss_mb | MB | 1 | 25.828 | 25.828 | 25.828 | 25.828 | n/a | n/a |
| docker (PID 151728) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [band_0000] (PID 151769) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [band_0000] (PID 151769) rss_mb | MB | 11 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [band_0000] (PID 151769) vms_mb | MB | 11 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 151781) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 151781) rss_mb | MB | 11 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [band_0000] (PID 151781) vms_mb | MB | 11 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 151783) rss_mb | MB | 1 | 25.863 | 25.863 | 25.863 | 25.863 | n/a | n/a |
| docker (PID 151783) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 151818) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 151818) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 151818) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 151818) rss_mb | MB | 9 | 27.112 | 27.098 | 27.223 | 27.223 | n/a | n/a |
| docker (PID 151818) vms_mb | MB | 9 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| bash [band_0000] (PID 151839) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [band_0000] (PID 151839) rss_mb | MB | 8 | 3.324 | 3.324 | 3.324 | 3.324 | n/a | n/a |
| bash [band_0000] (PID 151839) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [band_0000] (PID 151848) CPU | percent | 7 | 100.744 | 88.290 | 107.846 | 98.103 | 0.720000 CPU seconds | n/a |
| python [band_0000] (PID 151848) rss_mb | MB | 8 | 32.380 | 14.441 | 41.930 | 41.930 | n/a | n/a |
| python [band_0000] (PID 151848) vms_mb | MB | 8 | 39.451 | 18.371 | 51.324 | 51.324 | n/a | n/a |
| docker (PID 151858) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 151858) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 151858) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 151858) rss_mb | MB | 2 | 26.176 | 26.176 | 26.176 | 26.176 | n/a | n/a |
| docker (PID 151858) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 151916) CPU | percent | 1 | 9.862 | 9.862 | 9.862 | 9.862 | 0.010000 CPU seconds | n/a |
| docker (PID 151916) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 151916) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 151916) rss_mb | MB | 2 | 24.330 | 21.707 | 26.953 | 26.953 | n/a | n/a |
| docker (PID 151916) vms_mb | MB | 2 | 1588.486 | 1516.199 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 151957) CPU | percent | 2 | 4.908 | 0.000 | 9.816 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 151957) rss_mb | MB | 3 | 4.516 | 0.633 | 12.281 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 151957) vms_mb | MB | 3 | 524.112 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 151971) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 151971) rss_mb | MB | 2 | 1.723 | 1.723 | 1.723 | 1.723 | n/a | n/a |
| tail [bart_0000] (PID 151971) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 151981) rss_mb | MB | 1 | 27.438 | 27.438 | 27.438 | 27.438 | n/a | n/a |
| docker (PID 151981) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 152003) rss_mb | MB | 1 | 10.656 | 10.656 | 10.656 | 10.656 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 152003) vms_mb | MB | 1 | 1569.695 | 1569.695 | 1569.695 | 1569.695 | n/a | n/a |
| docker (PID 152010) rss_mb | MB | 1 | 27.395 | 27.395 | 27.395 | 27.395 | n/a | n/a |
| docker (PID 152010) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 152051) rss_mb | MB | 1 | 27.188 | 27.188 | 27.188 | 27.188 | n/a | n/a |
| docker (PID 152051) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 152111) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 152111) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 152111) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 152111) rss_mb | MB | 2 | 26.719 | 26.719 | 26.719 | 26.719 | n/a | n/a |
| docker (PID 152111) vms_mb | MB | 2 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 152153) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 152153) rss_mb | MB | 3 | 4.747 | 0.633 | 12.977 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 152153) vms_mb | MB | 3 | 524.195 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 152165) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 152165) rss_mb | MB | 2 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bart_0000] (PID 152165) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 152175) rss_mb | MB | 1 | 27.020 | 27.020 | 27.020 | 27.020 | n/a | n/a |
| docker (PID 152175) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 152195) rss_mb | MB | 1 | 11.988 | 11.988 | 11.988 | 11.988 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 152195) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 152246) CPU | percent | 1 | 19.555 | 19.555 | 19.555 | 19.555 | 0.020000 CPU seconds | n/a |
| docker (PID 152246) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 152246) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 152246) rss_mb | MB | 2 | 17.748 | 8.543 | 26.953 | 26.953 | n/a | n/a |
| docker (PID 152246) vms_mb | MB | 2 | 1444.041 | 1227.309 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 152280) rss_mb | MB | 1 | 27.102 | 27.102 | 27.102 | 27.102 | n/a | n/a |
| docker (PID 152280) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 152300) CPU | percent | 3 | 10.098 | 0.000 | 30.293 | 0.000 | 0.040000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 152300) rss_mb | MB | 4 | 3.254 | 0.633 | 11.117 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 152300) vms_mb | MB | 4 | 393.090 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 152348) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 152348) rss_mb | MB | 3 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [band_0000] (PID 152348) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 152367) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 152367) vms_mb | MB | 1 | 30.570 | 30.570 | 30.570 | 30.570 | n/a | n/a |
| docker (PID 152394) rss_mb | MB | 1 | 27.012 | 27.012 | 27.012 | 27.012 | n/a | n/a |
| docker (PID 152394) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 152429) rss_mb | MB | 1 | 27.434 | 27.434 | 27.434 | 27.434 | n/a | n/a |
| docker (PID 152429) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 152448) rss_mb | MB | 1 | 11.871 | 11.871 | 11.871 | 11.871 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 152448) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 152465) rss_mb | MB | 1 | 25.973 | 25.973 | 25.973 | 25.973 | n/a | n/a |
| docker (PID 152465) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 152517) rss_mb | MB | 1 | 23.469 | 23.469 | 23.469 | 23.469 | n/a | n/a |
| docker (PID 152517) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 152525) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 152525) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 152525) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 152525) rss_mb | MB | 2 | 26.641 | 26.641 | 26.641 | 26.641 | n/a | n/a |
| docker (PID 152525) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 152566) CPU | percent | 7 | 5.562 | 0.000 | 38.931 | 0.000 | 0.040000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 152566) rss_mb | MB | 8 | 1.965 | 0.633 | 11.289 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 152566) vms_mb | MB | 8 | 188.120 | 1.055 | 1497.578 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 152578) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 152578) rss_mb | MB | 7 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [bart_0000] (PID 152578) vms_mb | MB | 7 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 152588) rss_mb | MB | 1 | 27.082 | 27.082 | 27.082 | 27.082 | n/a | n/a |
| docker (PID 152588) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 152616) CPU | percent | 1 | 39.072 | 39.072 | 39.072 | 39.072 | 0.040000 CPU seconds | n/a |
| docker (PID 152616) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 152616) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 152616) rss_mb | MB | 2 | 15.648 | 4.281 | 27.016 | 27.016 | n/a | n/a |
| docker (PID 152616) vms_mb | MB | 2 | 846.768 | 32.762 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 152636) rss_mb | MB | 1 | 11.492 | 11.492 | 11.492 | 11.492 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 152636) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 152643) rss_mb | MB | 1 | 25.242 | 25.242 | 25.242 | 25.242 | n/a | n/a |
| docker (PID 152643) vms_mb | MB | 1 | 1596.211 | 1596.211 | 1596.211 | 1596.211 | n/a | n/a |
| docker (PID 152651) rss_mb | MB | 1 | 27.316 | 27.316 | 27.316 | 27.316 | n/a | n/a |
| docker (PID 152651) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 152687) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 152687) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 152687) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 152687) rss_mb | MB | 3 | 26.137 | 26.137 | 26.137 | 26.137 | n/a | n/a |
| docker (PID 152687) vms_mb | MB | 3 | 1659.961 | 1659.961 | 1659.961 | 1659.961 | n/a | n/a |
| docker (PID 152738) rss_mb | MB | 1 | 8.789 | 8.789 | 8.789 | 8.789 | n/a | n/a |
| docker (PID 152738) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 152764) rss_mb | MB | 1 | 25.965 | 25.965 | 25.965 | 25.965 | n/a | n/a |
| docker (PID 152764) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 152772) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 152772) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 152772) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 152772) rss_mb | MB | 39 | 25.633 | 25.633 | 25.633 | 25.633 | n/a | n/a |
| docker (PID 152772) vms_mb | MB | 39 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 152797) rss_mb | MB | 1 | 3.805 | 3.805 | 3.805 | 3.805 | n/a | n/a |
| docker (PID 152797) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 152813) rss_mb | MB | 1 | 22.910 | 22.910 | 22.910 | 22.910 | n/a | n/a |
| docker (PID 152813) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| python3 (PID 152820) CPU | percent | 3 | 102.051 | 98.416 | 108.786 | 108.786 | 0.310000 CPU seconds | n/a |
| python3 (PID 152820) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 152820) io write MB/s | MB/s | 3 | 0.927 | 0.000 | 2.781 | 2.781 | 0.281250 MB | n/a |
| python3 (PID 152820) rss_mb | MB | 4 | 27.321 | 17.105 | 34.559 | 34.559 | n/a | n/a |
| python3 (PID 152820) vms_mb | MB | 4 | 51.063 | 42.305 | 57.441 | 57.441 | n/a | n/a |
| docker (PID 152838) rss_mb | MB | 1 | 25.148 | 25.148 | 25.148 | 25.148 | n/a | n/a |
| docker (PID 152838) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 152873) CPU | percent | 1 | 9.846 | 9.846 | 9.846 | 9.846 | 0.010000 CPU seconds | n/a |
| docker (PID 152873) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 152873) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 152873) rss_mb | MB | 2 | 27.447 | 27.145 | 27.750 | 27.750 | n/a | n/a |
| docker (PID 152873) vms_mb | MB | 2 | 1696.775 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [base_0000] (PID 152912) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [base_0000] (PID 152912) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [base_0000] (PID 152912) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 152924) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 152924) rss_mb | MB | 4 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [base_0000] (PID 152924) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 152926) rss_mb | MB | 1 | 22.414 | 22.414 | 22.414 | 22.414 | n/a | n/a |
| docker (PID 152926) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 152960) rss_mb | MB | 1 | 27.434 | 27.434 | 27.434 | 27.434 | n/a | n/a |
| docker (PID 152960) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 152988) rss_mb | MB | 1 | 27.484 | 27.484 | 27.484 | 27.484 | n/a | n/a |
| docker (PID 152988) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 153008) rss_mb | MB | 1 | 12.547 | 12.547 | 12.547 | 12.547 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 153008) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 153052) rss_mb | MB | 1 | 8.547 | 8.547 | 8.547 | 8.547 | n/a | n/a |
| docker (PID 153052) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 153060) rss_mb | MB | 1 | 25.887 | 25.887 | 25.887 | 25.887 | n/a | n/a |
| docker (PID 153060) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 153117) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 153117) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 153117) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 153117) rss_mb | MB | 2 | 22.883 | 20.355 | 25.410 | 25.410 | n/a | n/a |
| docker (PID 153117) vms_mb | MB | 2 | 1624.082 | 1587.953 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 153157) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 153157) rss_mb | MB | 4 | 3.659 | 0.633 | 12.738 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 153157) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 153169) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 153169) rss_mb | MB | 3 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [base_0000] (PID 153169) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 153180) rss_mb | MB | 1 | 27.379 | 27.379 | 27.379 | 27.379 | n/a | n/a |
| docker (PID 153180) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 153200) rss_mb | MB | 1 | 11.855 | 11.855 | 11.855 | 11.855 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 153200) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 153236) rss_mb | MB | 1 | 20.609 | 20.609 | 20.609 | 20.609 | n/a | n/a |
| docker (PID 153236) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 153283) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 153283) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 153283) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 153283) rss_mb | MB | 2 | 15.994 | 5.020 | 26.969 | 26.969 | n/a | n/a |
| docker (PID 153283) vms_mb | MB | 2 | 846.768 | 32.762 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 153356) rss_mb | MB | 1 | 26.797 | 26.797 | 26.797 | 26.797 | n/a | n/a |
| docker (PID 153356) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 153370) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 153370) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 153370) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 153370) rss_mb | MB | 38 | 27.027 | 27.027 | 27.027 | 27.027 | n/a | n/a |
| docker (PID 153370) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 153387) rss_mb | MB | 1 | 25.641 | 25.641 | 25.641 | 25.641 | n/a | n/a |
| docker (PID 153387) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 153415) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 153415) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 153415) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 153415) rss_mb | MB | 2 | 25.578 | 24.051 | 27.105 | 27.105 | n/a | n/a |
| docker (PID 153415) vms_mb | MB | 2 | 1660.492 | 1660.211 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 153454) CPU | percent | 3 | 3.238 | 0.000 | 9.715 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 153454) rss_mb | MB | 4 | 3.657 | 0.633 | 12.730 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 153454) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 153466) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 153466) rss_mb | MB | 3 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [bart_0000] (PID 153466) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 153476) rss_mb | MB | 1 | 26.930 | 26.930 | 26.930 | 26.930 | n/a | n/a |
| docker (PID 153476) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 153496) rss_mb | MB | 1 | 10.633 | 10.633 | 10.633 | 10.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 153496) vms_mb | MB | 1 | 1569.582 | 1569.582 | 1569.582 | 1569.582 | n/a | n/a |
| docker (PID 153529) rss_mb | MB | 1 | 4.410 | 4.410 | 4.410 | 4.410 | n/a | n/a |
| docker (PID 153529) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 153569) rss_mb | MB | 1 | 21.023 | 21.023 | 21.023 | 21.023 | n/a | n/a |
| docker (PID 153569) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 153578) rss_mb | MB | 1 | 26.867 | 26.867 | 26.867 | 26.867 | n/a | n/a |
| docker (PID 153578) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 153638) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 153638) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 153638) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 153638) rss_mb | MB | 2 | 25.656 | 25.656 | 25.656 | 25.656 | n/a | n/a |
| docker (PID 153638) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 153679) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 153679) rss_mb | MB | 11 | 1.741 | 0.633 | 12.828 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 153679) vms_mb | MB | 11 | 143.707 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 153692) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 153692) rss_mb | MB | 10 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [bart_0000] (PID 153692) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 153703) rss_mb | MB | 1 | 27.496 | 27.496 | 27.496 | 27.496 | n/a | n/a |
| docker (PID 153703) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 153723) rss_mb | MB | 1 | 11.449 | 11.449 | 11.449 | 11.449 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 153723) vms_mb | MB | 1 | 1498.223 | 1498.223 | 1498.223 | 1498.223 | n/a | n/a |
| docker (PID 153729) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 153729) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 153729) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 153729) rss_mb | MB | 8 | 27.375 | 27.375 | 27.375 | 27.375 | n/a | n/a |
| docker (PID 153729) vms_mb | MB | 8 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| bash [bart_0000] (PID 153749) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bart_0000] (PID 153749) rss_mb | MB | 8 | 3.273 | 3.273 | 3.273 | 3.273 | n/a | n/a |
| bash [bart_0000] (PID 153749) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bart_0000] (PID 153758) CPU | percent | 7 | 99.160 | 96.530 | 107.883 | 97.431 | 0.710000 CPU seconds | n/a |
| python [bart_0000] (PID 153758) rss_mb | MB | 8 | 30.609 | 10.230 | 41.805 | 41.805 | n/a | n/a |
| python [bart_0000] (PID 153758) vms_mb | MB | 8 | 37.916 | 14.531 | 51.324 | 51.324 | n/a | n/a |
| docker (PID 153769) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 153769) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 153769) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 153769) rss_mb | MB | 2 | 21.561 | 17.426 | 25.695 | 25.695 | n/a | n/a |
| docker (PID 153769) vms_mb | MB | 2 | 1587.955 | 1515.699 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 153831) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 153831) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 153831) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 153831) rss_mb | MB | 2 | 22.508 | 18.109 | 26.906 | 26.906 | n/a | n/a |
| docker (PID 153831) vms_mb | MB | 2 | 1588.236 | 1515.699 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 153870) CPU | percent | 3 | 3.044 | 0.000 | 9.131 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 153870) rss_mb | MB | 4 | 3.635 | 0.633 | 12.641 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 153870) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 153883) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 153883) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bart_0000] (PID 153883) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 153894) rss_mb | MB | 1 | 27.066 | 27.066 | 27.066 | 27.066 | n/a | n/a |
| docker (PID 153894) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 153914) rss_mb | MB | 1 | 11.773 | 11.773 | 11.773 | 11.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 153914) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 153949) rss_mb | MB | 1 | 20.289 | 20.289 | 20.289 | 20.289 | n/a | n/a |
| docker (PID 153949) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 153994) CPU | percent | 1 | 9.779 | 9.779 | 9.779 | 9.779 | 0.010000 CPU seconds | n/a |
| docker (PID 153994) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 153994) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 153994) rss_mb | MB | 2 | 15.668 | 4.168 | 27.168 | 27.168 | n/a | n/a |
| docker (PID 153994) vms_mb | MB | 2 | 846.768 | 32.762 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 154054) rss_mb | MB | 1 | 8.719 | 8.719 | 8.719 | 8.719 | n/a | n/a |
| docker (PID 154054) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 154078) CPU | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 154078) io read MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 154078) io write MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 154078) rss_mb | MB | 40 | 26.844 | 26.844 | 26.844 | 26.844 | n/a | n/a |
| docker (PID 154078) vms_mb | MB | 40 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 154110) rss_mb | MB | 1 | 26.859 | 26.859 | 26.859 | 26.859 | n/a | n/a |
| docker (PID 154110) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 154125) CPU | percent | 3 | 102.048 | 98.580 | 108.744 | 108.744 | 0.310000 CPU seconds | n/a |
| python3 (PID 154125) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 154125) io write MB/s | MB/s | 3 | 0.927 | 0.000 | 2.780 | 2.780 | 0.281250 MB | n/a |
| python3 (PID 154125) rss_mb | MB | 4 | 24.724 | 11.477 | 34.496 | 34.496 | n/a | n/a |
| python3 (PID 154125) vms_mb | MB | 4 | 48.690 | 36.938 | 57.441 | 57.441 | n/a | n/a |
| docker (PID 154135) rss_mb | MB | 1 | 27.016 | 27.016 | 27.016 | 27.016 | n/a | n/a |
| docker (PID 154135) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 154191) CPU | percent | 38 | 0.259 | 0.000 | 9.829 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 154191) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 154191) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 154191) rss_mb | MB | 39 | 26.551 | 20.922 | 26.699 | 26.699 | n/a | n/a |
| docker (PID 154191) vms_mb | MB | 39 | 1657.272 | 1524.203 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 154244) CPU | percent | 2 | 4.928 | 0.000 | 9.855 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 154244) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 154244) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 154244) rss_mb | MB | 3 | 18.953 | 1.938 | 27.461 | 27.461 | n/a | n/a |
| docker (PID 154244) vms_mb | MB | 3 | 1214.108 | 32.762 | 1804.781 | 1804.781 | n/a | n/a |
| docker-init [beam_0000] (PID 154285) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beam_0000] (PID 154285) rss_mb | MB | 4 | 3.680 | 0.633 | 12.820 | 0.633 | n/a | n/a |
| docker-init [beam_0000] (PID 154285) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 154297) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 154297) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [beam_0000] (PID 154297) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 154362) rss_mb | MB | 1 | 25.645 | 25.645 | 25.645 | 25.645 | n/a | n/a |
| docker (PID 154362) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 154399) rss_mb | MB | 1 | 27.730 | 27.730 | 27.730 | 27.730 | n/a | n/a |
| docker (PID 154399) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 154419) rss_mb | MB | 1 | 3.988 | 3.988 | 3.988 | 3.988 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 154419) vms_mb | MB | 1 | 1208.676 | 1208.676 | 1208.676 | 1208.676 | n/a | n/a |
| docker (PID 154435) rss_mb | MB | 1 | 26.766 | 26.766 | 26.766 | 26.766 | n/a | n/a |
| docker (PID 154435) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 154484) rss_mb | MB | 1 | 4.043 | 4.043 | 4.043 | 4.043 | n/a | n/a |
| docker (PID 154484) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 154493) rss_mb | MB | 1 | 26.531 | 26.531 | 26.531 | 26.531 | n/a | n/a |
| docker (PID 154493) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 154529) CPU | percent | 3 | 9.755 | 0.000 | 29.264 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [beam_0000] (PID 154529) rss_mb | MB | 4 | 3.324 | 0.633 | 11.398 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 154529) vms_mb | MB | 4 | 393.187 | 1.055 | 1569.582 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 154545) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 154545) rss_mb | MB | 3 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [beam_0000] (PID 154545) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 154555) rss_mb | MB | 1 | 27.414 | 27.414 | 27.414 | 27.414 | n/a | n/a |
| docker (PID 154555) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 154581) rss_mb | MB | 1 | 27.234 | 27.234 | 27.234 | 27.234 | n/a | n/a |
| docker (PID 154581) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 154601) rss_mb | MB | 1 | 12.496 | 12.496 | 12.496 | 12.496 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 154601) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 154655) rss_mb | MB | 1 | 26.914 | 26.914 | 26.914 | 26.914 | n/a | n/a |
| docker (PID 154655) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 154705) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 154705) vms_mb | MB | 1 | 30.570 | 30.570 | 30.570 | 30.570 | n/a | n/a |
| docker (PID 154714) rss_mb | MB | 1 | 27.012 | 27.012 | 27.012 | 27.012 | n/a | n/a |
| docker (PID 154714) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 154755) CPU | percent | 3 | 6.492 | 0.000 | 19.475 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 154755) rss_mb | MB | 4 | 3.149 | 0.633 | 10.699 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 154755) vms_mb | MB | 4 | 375.089 | 1.055 | 1497.191 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 154767) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 154767) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [base_0000] (PID 154767) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 154777) rss_mb | MB | 1 | 23.547 | 23.547 | 23.547 | 23.547 | n/a | n/a |
| docker (PID 154777) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 154805) rss_mb | MB | 1 | 27.238 | 27.238 | 27.238 | 27.238 | n/a | n/a |
| docker (PID 154805) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 154824) rss_mb | MB | 1 | 11.363 | 11.363 | 11.363 | 11.363 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 154824) vms_mb | MB | 1 | 1569.969 | 1569.969 | 1569.969 | 1569.969 | n/a | n/a |
| docker (PID 154840) rss_mb | MB | 1 | 27.129 | 27.129 | 27.129 | 27.129 | n/a | n/a |
| docker (PID 154840) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 154860) rss_mb | MB | 1 | 12.035 | 12.035 | 12.035 | 12.035 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 154860) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 154879) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 154879) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 154879) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 154879) rss_mb | MB | 2 | 27.023 | 27.023 | 27.023 | 27.023 | n/a | n/a |
| docker (PID 154879) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 154919) rss_mb | MB | 1 | 20.246 | 20.246 | 20.246 | 20.246 | n/a | n/a |
| docker (PID 154919) vms_mb | MB | 1 | 1524.203 | 1524.203 | 1524.203 | 1524.203 | n/a | n/a |
| docker (PID 154936) CPU | percent | 2 | 9.777 | 0.000 | 19.555 | 0.000 | 0.020000 CPU seconds | n/a |
| docker (PID 154936) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 154936) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 154936) rss_mb | MB | 3 | 19.342 | 4.160 | 26.934 | 26.934 | n/a | n/a |
| docker (PID 154936) vms_mb | MB | 3 | 1118.103 | 32.762 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 154976) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 154976) rss_mb | MB | 14 | 1.515 | 0.633 | 12.980 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 154976) vms_mb | MB | 14 | 113.156 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 154989) CPU | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 154989) rss_mb | MB | 13 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [base_0000] (PID 154989) vms_mb | MB | 13 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 154999) rss_mb | MB | 1 | 18.156 | 18.156 | 18.156 | 18.156 | n/a | n/a |
| docker (PID 154999) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 155028) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 155028) io read MB/s | MB/s | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 155028) io write MB/s | MB/s | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 155028) rss_mb | MB | 11 | 27.094 | 26.941 | 27.109 | 27.109 | n/a | n/a |
| docker (PID 155028) vms_mb | MB | 11 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| bash [base_0000] (PID 155047) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [base_0000] (PID 155047) rss_mb | MB | 10 | 3.273 | 3.273 | 3.273 | 3.273 | n/a | n/a |
| bash [base_0000] (PID 155047) vms_mb | MB | 10 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [base_0000] (PID 155056) CPU | percent | 9 | 99.867 | 97.201 | 107.804 | 98.072 | 0.920000 CPU seconds | n/a |
| python [base_0000] (PID 155056) rss_mb | MB | 10 | 30.714 | 9.797 | 41.641 | 40.969 | n/a | n/a |
| python [base_0000] (PID 155056) vms_mb | MB | 10 | 37.952 | 13.602 | 51.957 | 51.027 | n/a | n/a |
| docker (PID 155067) CPU | percent | 1 | 9.742 | 9.742 | 9.742 | 9.742 | 0.010000 CPU seconds | n/a |
| docker (PID 155067) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 155067) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 155067) rss_mb | MB | 2 | 15.812 | 4.594 | 27.031 | 27.031 | n/a | n/a |
| docker (PID 155067) vms_mb | MB | 2 | 846.768 | 32.762 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 155125) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 155125) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 155125) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 155125) rss_mb | MB | 2 | 26.684 | 26.684 | 26.684 | 26.684 | n/a | n/a |
| docker (PID 155125) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [base_0000] (PID 155164) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [base_0000] (PID 155164) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [base_0000] (PID 155164) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 155176) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 155176) rss_mb | MB | 3 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [base_0000] (PID 155176) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 155212) rss_mb | MB | 1 | 23.848 | 23.848 | 23.848 | 23.848 | n/a | n/a |
| docker (PID 155212) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 155249) rss_mb | MB | 1 | 27.320 | 27.320 | 27.320 | 27.320 | n/a | n/a |
| docker (PID 155249) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 155288) rss_mb | MB | 1 | 27.082 | 27.082 | 27.082 | 27.082 | n/a | n/a |
| docker (PID 155288) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 155329) rss_mb | MB | 1 | 23.688 | 23.688 | 23.688 | 23.688 | n/a | n/a |
| docker (PID 155329) vms_mb | MB | 1 | 1524.203 | 1524.203 | 1524.203 | 1524.203 | n/a | n/a |
| docker (PID 155346) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 155346) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 155346) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 155346) rss_mb | MB | 2 | 17.238 | 8.719 | 25.758 | 25.758 | n/a | n/a |
| docker (PID 155346) vms_mb | MB | 2 | 1443.822 | 1227.434 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 155385) CPU | percent | 3 | 6.535 | 0.000 | 19.605 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 155385) rss_mb | MB | 4 | 3.624 | 0.633 | 12.598 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 155385) vms_mb | MB | 4 | 411.411 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 155398) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 155398) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [base_0000] (PID 155398) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 155408) rss_mb | MB | 1 | 27.117 | 27.117 | 27.117 | 27.117 | n/a | n/a |
| docker (PID 155408) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 155502) rss_mb | MB | 1 | 14.453 | 14.453 | 14.453 | 14.453 | n/a | n/a |
| docker (PID 155502) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 155510) rss_mb | MB | 1 | 25.980 | 25.980 | 25.980 | 25.980 | n/a | n/a |
| docker (PID 155510) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 155561) rss_mb | MB | 1 | 16.387 | 16.387 | 16.387 | 16.387 | n/a | n/a |
| docker (PID 155561) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 155569) rss_mb | MB | 1 | 25.707 | 25.707 | 25.707 | 25.707 | n/a | n/a |
| docker (PID 155569) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 155612) CPU | percent | 7 | 2.790 | 0.000 | 19.527 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 155612) rss_mb | MB | 8 | 1.955 | 0.633 | 11.211 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 155612) vms_mb | MB | 8 | 197.104 | 1.055 | 1569.445 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 155624) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 155624) rss_mb | MB | 7 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [base_0000] (PID 155624) vms_mb | MB | 7 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 155634) rss_mb | MB | 1 | 18.414 | 18.414 | 18.414 | 18.414 | n/a | n/a |
| docker (PID 155634) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 155661) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 155661) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 155661) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 155661) rss_mb | MB | 5 | 26.973 | 26.973 | 26.973 | 26.973 | n/a | n/a |
| docker (PID 155661) vms_mb | MB | 5 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 155682) CPU | percent | 4 | 4.857 | 0.000 | 19.429 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 155682) rss_mb | MB | 5 | 4.805 | 3.320 | 10.742 | 3.320 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 155682) vms_mb | MB | 5 | 317.429 | 4.391 | 1569.582 | 4.391 | n/a | n/a |
| python [base_0000] (PID 155691) CPU | percent | 3 | 97.906 | 87.785 | 117.662 | 88.272 | 0.300000 CPU seconds | n/a |
| python [base_0000] (PID 155691) rss_mb | MB | 4 | 26.517 | 15.496 | 34.797 | 34.797 | n/a | n/a |
| python [base_0000] (PID 155691) vms_mb | MB | 4 | 33.779 | 19.680 | 45.023 | 45.023 | n/a | n/a |
| docker (PID 155701) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 155701) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 155701) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 155701) rss_mb | MB | 2 | 25.859 | 25.859 | 25.859 | 25.859 | n/a | n/a |
| docker (PID 155701) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 155766) rss_mb | MB | 1 | 25.469 | 25.469 | 25.469 | 25.469 | n/a | n/a |
| docker (PID 155766) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 155781) CPU | percent | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 155781) io read MB/s | MB/s | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 155781) io write MB/s | MB/s | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 155781) rss_mb | MB | 41 | 26.941 | 26.941 | 26.941 | 26.941 | n/a | n/a |
| docker (PID 155781) vms_mb | MB | 41 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 155797) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 155797) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 155797) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 155797) rss_mb | MB | 2 | 25.527 | 25.527 | 25.527 | 25.527 | n/a | n/a |
| docker (PID 155797) vms_mb | MB | 2 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 155836) CPU | percent | 5 | 7.794 | 0.000 | 38.971 | 0.000 | 0.040000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 155836) rss_mb | MB | 6 | 2.410 | 0.633 | 11.293 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 155836) vms_mb | MB | 6 | 262.536 | 1.055 | 1569.945 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 155849) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 155849) rss_mb | MB | 5 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [base_0000] (PID 155849) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 155853) rss_mb | MB | 1 | 3.293 | 3.293 | 3.293 | 3.293 | n/a | n/a |
| docker (PID 155853) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 155863) rss_mb | MB | 1 | 27.352 | 27.352 | 27.352 | 27.352 | n/a | n/a |
| docker (PID 155863) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 155882) rss_mb | MB | 1 | 11.957 | 11.957 | 11.957 | 11.957 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 155882) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 155890) rss_mb | MB | 1 | 27.496 | 27.496 | 27.496 | 27.496 | n/a | n/a |
| docker (PID 155890) vms_mb | MB | 1 | 1733.027 | 1733.027 | 1733.027 | 1733.027 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 155908) rss_mb | MB | 1 | 11.598 | 11.598 | 11.598 | 11.598 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 155908) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 155925) rss_mb | MB | 1 | 27.633 | 27.633 | 27.633 | 27.633 | n/a | n/a |
| docker (PID 155925) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 155961) rss_mb | MB | 1 | 25.762 | 25.762 | 25.762 | 25.762 | n/a | n/a |
| docker (PID 155961) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 155996) rss_mb | MB | 1 | 9.281 | 9.281 | 9.281 | 9.281 | n/a | n/a |
| docker (PID 155996) vms_mb | MB | 1 | 1315.695 | 1315.695 | 1315.695 | 1315.695 | n/a | n/a |
| docker (PID 156040) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 156040) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 156040) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 156040) rss_mb | MB | 2 | 26.297 | 26.297 | 26.297 | 26.297 | n/a | n/a |
| docker (PID 156040) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 156081) CPU | percent | 3 | 3.248 | 0.000 | 9.745 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [beam_0000] (PID 156081) rss_mb | MB | 4 | 3.751 | 0.633 | 13.105 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 156081) vms_mb | MB | 4 | 393.535 | 1.055 | 1570.977 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 156093) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 156093) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [beam_0000] (PID 156093) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 156168) rss_mb | MB | 1 | 21.520 | 21.520 | 21.520 | 21.520 | n/a | n/a |
| docker (PID 156168) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 156208) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 156208) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 156208) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 156208) rss_mb | MB | 2 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| docker (PID 156208) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 156296) CPU | percent | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 156296) io read MB/s | MB/s | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 156296) io write MB/s | MB/s | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 156296) rss_mb | MB | 48 | 25.754 | 25.754 | 25.754 | 25.754 | n/a | n/a |
| docker (PID 156296) vms_mb | MB | 48 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 156304) rss_mb | MB | 1 | 19.113 | 19.113 | 19.113 | 19.113 | n/a | n/a |
| docker (PID 156304) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 156313) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 156313) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 156313) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 156313) rss_mb | MB | 2 | 27.094 | 27.094 | 27.094 | 27.094 | n/a | n/a |
| docker (PID 156313) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 156352) CPU | percent | 17 | 0.574 | 0.000 | 9.757 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [beam_0000] (PID 156352) rss_mb | MB | 18 | 1.324 | 0.633 | 13.070 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 156352) vms_mb | MB | 18 | 88.245 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 156364) CPU | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 156364) rss_mb | MB | 17 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [beam_0000] (PID 156364) vms_mb | MB | 17 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 156374) rss_mb | MB | 1 | 25.359 | 25.359 | 25.359 | 25.359 | n/a | n/a |
| docker (PID 156374) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 156399) CPU | percent | 14 | 0.680 | 0.000 | 9.516 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 156399) io read MB/s | MB/s | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 156399) io write MB/s | MB/s | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 156399) rss_mb | MB | 15 | 27.228 | 25.504 | 27.352 | 27.352 | n/a | n/a |
| docker (PID 156399) vms_mb | MB | 15 | 1660.736 | 1660.211 | 1660.773 | 1660.773 | n/a | n/a |
| bash [beam_0000] (PID 156420) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [beam_0000] (PID 156420) rss_mb | MB | 14 | 3.316 | 3.316 | 3.316 | 3.316 | n/a | n/a |
| bash [beam_0000] (PID 156420) vms_mb | MB | 14 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [beam_0000] (PID 156429) CPU | percent | 13 | 96.637 | 83.467 | 106.385 | 95.237 | 1.330000 CPU seconds | n/a |
| python [beam_0000] (PID 156429) rss_mb | MB | 14 | 31.769 | 9.762 | 41.715 | 41.715 | n/a | n/a |
| python [beam_0000] (PID 156429) vms_mb | MB | 14 | 38.897 | 13.531 | 51.238 | 51.238 | n/a | n/a |
| docker (PID 156439) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 156439) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 156439) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 156439) rss_mb | MB | 2 | 26.969 | 26.969 | 26.969 | 26.969 | n/a | n/a |
| docker (PID 156439) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 156496) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 156496) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 156496) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 156496) rss_mb | MB | 3 | 25.527 | 25.527 | 25.527 | 25.527 | n/a | n/a |
| docker (PID 156496) vms_mb | MB | 3 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 156537) CPU | percent | 4 | 7.142 | 0.000 | 28.566 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [beam_0000] (PID 156537) rss_mb | MB | 5 | 2.655 | 0.633 | 10.742 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 156537) vms_mb | MB | 5 | 314.683 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 156549) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 156549) rss_mb | MB | 4 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [beam_0000] (PID 156549) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 156559) rss_mb | MB | 1 | 26.934 | 26.934 | 26.934 | 26.934 | n/a | n/a |
| docker (PID 156559) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 156577) rss_mb | MB | 1 | 10.715 | 10.715 | 10.715 | 10.715 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 156577) vms_mb | MB | 1 | 1569.445 | 1569.445 | 1569.445 | 1569.445 | n/a | n/a |
| docker (PID 156623) rss_mb | MB | 1 | 27.215 | 27.215 | 27.215 | 27.215 | n/a | n/a |
| docker (PID 156623) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 156648) rss_mb | MB | 1 | 11.586 | 11.586 | 11.586 | 11.586 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 156648) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 156666) rss_mb | MB | 1 | 25.965 | 25.965 | 25.965 | 25.965 | n/a | n/a |
| docker (PID 156666) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 156687) rss_mb | MB | 1 | 6.512 | 6.512 | 6.512 | 6.512 | n/a | n/a |
| docker (PID 156687) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 156702) rss_mb | MB | 1 | 25.508 | 25.508 | 25.508 | 25.508 | n/a | n/a |
| docker (PID 156702) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 156724) rss_mb | MB | 1 | 10.395 | 10.395 | 10.395 | 10.395 | n/a | n/a |
| docker (PID 156724) vms_mb | MB | 1 | 1451.949 | 1451.949 | 1451.949 | 1451.949 | n/a | n/a |
| python3 (PID 156748) CPU | percent | 3 | 102.042 | 98.467 | 108.805 | 98.854 | 0.310000 CPU seconds | n/a |
| python3 (PID 156748) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 156748) io write MB/s | MB/s | 3 | 0.850 | 0.000 | 2.549 | 2.549 | 0.257812 MB | n/a |
| python3 (PID 156748) rss_mb | MB | 4 | 29.181 | 20.547 | 34.848 | 34.848 | n/a | n/a |
| python3 (PID 156748) vms_mb | MB | 4 | 52.523 | 45.242 | 57.441 | 57.441 | n/a | n/a |
| docker (PID 156768) rss_mb | MB | 1 | 19.387 | 19.387 | 19.387 | 19.387 | n/a | n/a |
| docker (PID 156768) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 156812) rss_mb | MB | 1 | 27.188 | 27.188 | 27.188 | 27.188 | n/a | n/a |
| docker (PID 156812) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 156820) CPU | percent | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 156820) io read MB/s | MB/s | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 156820) io write MB/s | MB/s | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 156820) rss_mb | MB | 46 | 27.188 | 27.188 | 27.188 | 27.188 | n/a | n/a |
| docker (PID 156820) vms_mb | MB | 46 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 156828) rss_mb | MB | 1 | 26.789 | 26.789 | 26.789 | 26.789 | n/a | n/a |
| docker (PID 156828) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 156842) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 156842) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 156842) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 156842) rss_mb | MB | 3 | 26.845 | 25.738 | 27.398 | 27.398 | n/a | n/a |
| docker (PID 156842) vms_mb | MB | 3 | 1660.586 | 1660.211 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[0:PARENT] (PID 156878) rss_mb | MB | 1 | 1.969 | 1.969 | 1.969 | 1.969 | n/a | n/a |
| runc:[0:PARENT] (PID 156878) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[1:CHILD] (PID 156879) rss_mb | MB | 1 | 0.793 | 0.793 | 0.793 | 0.793 | n/a | n/a |
| runc:[1:CHILD] (PID 156879) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| docker-init [bear_0000] (PID 156880) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bear_0000] (PID 156880) rss_mb | MB | 6 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bear_0000] (PID 156880) vms_mb | MB | 6 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 156893) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 156893) rss_mb | MB | 6 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [bear_0000] (PID 156893) vms_mb | MB | 6 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 156933) rss_mb | MB | 1 | 27.352 | 27.352 | 27.352 | 27.352 | n/a | n/a |
| docker (PID 156933) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 156951) rss_mb | MB | 1 | 12.375 | 12.375 | 12.375 | 12.375 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 156951) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 156958) rss_mb | MB | 1 | 27.793 | 27.793 | 27.793 | 27.793 | n/a | n/a |
| docker (PID 156958) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 156997) rss_mb | MB | 1 | 27.223 | 27.223 | 27.223 | 27.223 | n/a | n/a |
| docker (PID 156997) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 157018) rss_mb | MB | 1 | 10.617 | 10.617 | 10.617 | 10.617 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 157018) vms_mb | MB | 1 | 1569.445 | 1569.445 | 1569.445 | 1569.445 | n/a | n/a |
| docker (PID 157036) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 157036) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 157036) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 157036) rss_mb | MB | 2 | 25.160 | 23.500 | 26.820 | 26.820 | n/a | n/a |
| docker (PID 157036) vms_mb | MB | 2 | 1660.490 | 1588.203 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 157082) rss_mb | MB | 1 | 25.508 | 25.508 | 25.508 | 25.508 | n/a | n/a |
| docker (PID 157082) vms_mb | MB | 1 | 1596.211 | 1596.211 | 1596.211 | 1596.211 | n/a | n/a |
| docker (PID 157090) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 157090) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 157090) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 157090) rss_mb | MB | 2 | 25.848 | 25.848 | 25.848 | 25.848 | n/a | n/a |
| docker (PID 157090) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 157130) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 157130) rss_mb | MB | 5 | 3.042 | 0.633 | 12.680 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 157130) vms_mb | MB | 5 | 314.889 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 157142) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 157142) rss_mb | MB | 4 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bear_0000] (PID 157142) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 157153) rss_mb | MB | 1 | 26.996 | 26.996 | 26.996 | 26.996 | n/a | n/a |
| docker (PID 157153) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 157179) rss_mb | MB | 1 | 27.098 | 27.098 | 27.098 | 27.098 | n/a | n/a |
| docker (PID 157179) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 157214) rss_mb | MB | 1 | 23.656 | 23.656 | 23.656 | 23.656 | n/a | n/a |
| docker (PID 157214) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 157244) rss_mb | MB | 1 | 16.297 | 16.297 | 16.297 | 16.297 | n/a | n/a |
| docker (PID 157244) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 157252) rss_mb | MB | 1 | 26.043 | 26.043 | 26.043 | 26.043 | n/a | n/a |
| docker (PID 157252) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 157293) rss_mb | MB | 1 | 26.637 | 26.637 | 26.637 | 26.637 | n/a | n/a |
| docker (PID 157293) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 157302) rss_mb | MB | 1 | 26.402 | 26.402 | 26.402 | 26.402 | n/a | n/a |
| docker (PID 157302) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 157310) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 157310) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 157310) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 157310) rss_mb | MB | 2 | 25.922 | 25.922 | 25.922 | 25.922 | n/a | n/a |
| docker (PID 157310) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 157358) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 157358) rss_mb | MB | 4 | 3.661 | 0.633 | 12.746 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 157358) vms_mb | MB | 4 | 375.347 | 1.055 | 1498.223 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 157373) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 157373) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bear_0000] (PID 157373) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 157383) rss_mb | MB | 1 | 27.543 | 27.543 | 27.543 | 27.543 | n/a | n/a |
| docker (PID 157383) vms_mb | MB | 1 | 1733.027 | 1733.027 | 1733.027 | 1733.027 | n/a | n/a |
| docker (PID 157404) rss_mb | MB | 1 | 15.133 | 15.133 | 15.133 | 15.133 | n/a | n/a |
| docker (PID 157404) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 157405) rss_mb | MB | 1 | 11.445 | 11.445 | 11.445 | 11.445 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 157405) vms_mb | MB | 1 | 1570.090 | 1570.090 | 1570.090 | 1570.090 | n/a | n/a |
| docker (PID 157426) rss_mb | MB | 1 | 27.332 | 27.332 | 27.332 | 27.332 | n/a | n/a |
| docker (PID 157426) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 157437) rss_mb | MB | 1 | 25.801 | 25.801 | 25.801 | 25.801 | n/a | n/a |
| docker (PID 157437) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 157453) rss_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 157453) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 157487) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 157487) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 157487) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 157487) rss_mb | MB | 2 | 27.012 | 27.012 | 27.012 | 27.012 | n/a | n/a |
| docker (PID 157487) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 157492) CPU | percent | 4 | 96.003 | 88.972 | 108.759 | 89.014 | 0.390000 CPU seconds | n/a |
| python3 (PID 157492) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 157492) io write MB/s | MB/s | 4 | 0.686 | 0.000 | 2.743 | 2.743 | 0.277344 MB | n/a |
| python3 (PID 157492) rss_mb | MB | 5 | 24.346 | 9.820 | 34.684 | 34.684 | n/a | n/a |
| python3 (PID 157492) vms_mb | MB | 5 | 48.520 | 36.465 | 57.441 | 57.441 | n/a | n/a |
| docker (PID 157546) rss_mb | MB | 1 | 21.129 | 21.129 | 21.129 | 21.129 | n/a | n/a |
| docker (PID 157546) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 157582) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 157582) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 157582) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 157582) rss_mb | MB | 2 | 27.148 | 27.148 | 27.148 | 27.148 | n/a | n/a |
| docker (PID 157582) vms_mb | MB | 2 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 157625) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 157625) rss_mb | MB | 3 | 4.792 | 0.633 | 13.109 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 157625) vms_mb | MB | 3 | 548.197 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 157638) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 157638) rss_mb | MB | 2 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [bear_0000] (PID 157638) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 157648) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 157648) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 157718) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 157718) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 157718) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 157718) rss_mb | MB | 2 | 17.125 | 8.543 | 25.707 | 25.707 | n/a | n/a |
| docker (PID 157718) vms_mb | MB | 2 | 1443.822 | 1227.434 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 157780) rss_mb | MB | 1 | 26.473 | 26.473 | 26.473 | 26.473 | n/a | n/a |
| docker (PID 157780) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [bear_0000] (PID 157818) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bear_0000] (PID 157818) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bear_0000] (PID 157818) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 157833) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 157833) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bear_0000] (PID 157833) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 157835) rss_mb | MB | 1 | 18.180 | 18.180 | 18.180 | 18.180 | n/a | n/a |
| docker (PID 157835) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 157871) rss_mb | MB | 1 | 27.281 | 27.281 | 27.281 | 27.281 | n/a | n/a |
| docker (PID 157871) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 157908) rss_mb | MB | 1 | 27.348 | 27.348 | 27.348 | 27.348 | n/a | n/a |
| docker (PID 157908) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 157929) rss_mb | MB | 1 | 10.566 | 10.566 | 10.566 | 10.566 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 157929) vms_mb | MB | 1 | 1569.453 | 1569.453 | 1569.453 | 1569.453 | n/a | n/a |
| docker (PID 157945) rss_mb | MB | 1 | 27.148 | 27.148 | 27.148 | 27.148 | n/a | n/a |
| docker (PID 157945) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 157987) rss_mb | MB | 1 | 8.672 | 8.672 | 8.672 | 8.672 | n/a | n/a |
| docker (PID 157987) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 157997) rss_mb | MB | 1 | 27.172 | 27.172 | 27.172 | 27.172 | n/a | n/a |
| docker (PID 157997) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 158012) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 158012) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 158012) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 158012) rss_mb | MB | 2 | 27.570 | 27.570 | 27.570 | 27.570 | n/a | n/a |
| docker (PID 158012) vms_mb | MB | 2 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [beef_0000] (PID 158051) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beef_0000] (PID 158051) rss_mb | MB | 4 | 3.741 | 0.633 | 13.066 | 0.633 | n/a | n/a |
| docker-init [beef_0000] (PID 158051) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 158064) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 158064) rss_mb | MB | 3 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [beef_0000] (PID 158064) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 158095) rss_mb | MB | 1 | 8.680 | 8.680 | 8.680 | 8.680 | n/a | n/a |
| docker (PID 158095) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 158131) rss_mb | MB | 1 | 27.008 | 27.008 | 27.008 | 27.008 | n/a | n/a |
| docker (PID 158131) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 158166) rss_mb | MB | 1 | 26.828 | 26.828 | 26.828 | 26.828 | n/a | n/a |
| docker (PID 158166) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 158185) rss_mb | MB | 1 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 158185) vms_mb | MB | 1 | 1208.676 | 1208.676 | 1208.676 | 1208.676 | n/a | n/a |
| docker (PID 158201) rss_mb | MB | 1 | 25.742 | 25.742 | 25.742 | 25.742 | n/a | n/a |
| docker (PID 158201) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 158244) rss_mb | MB | 1 | 23.543 | 23.543 | 23.543 | 23.543 | n/a | n/a |
| docker (PID 158244) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 158262) rss_mb | MB | 1 | 26.973 | 26.973 | 26.973 | 26.973 | n/a | n/a |
| docker (PID 158262) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 158301) CPU | percent | 3 | 6.434 | 0.000 | 19.302 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [beef_0000] (PID 158301) rss_mb | MB | 4 | 1.474 | 0.633 | 3.996 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 158301) vms_mb | MB | 4 | 302.960 | 1.055 | 1208.676 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 158314) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 158314) rss_mb | MB | 3 | 1.684 | 1.684 | 1.684 | 1.684 | n/a | n/a |
| tail [beef_0000] (PID 158314) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 158324) rss_mb | MB | 1 | 8.848 | 8.848 | 8.848 | 8.848 | n/a | n/a |
| docker (PID 158324) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 158351) rss_mb | MB | 1 | 27.324 | 27.324 | 27.324 | 27.324 | n/a | n/a |
| docker (PID 158351) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 158371) rss_mb | MB | 1 | 10.660 | 10.660 | 10.660 | 10.660 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 158371) vms_mb | MB | 1 | 1569.582 | 1569.582 | 1569.582 | 1569.582 | n/a | n/a |
| docker (PID 158386) rss_mb | MB | 1 | 27.527 | 27.527 | 27.527 | 27.527 | n/a | n/a |
| docker (PID 158386) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 158405) rss_mb | MB | 1 | 11.855 | 11.855 | 11.855 | 11.855 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 158405) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 158421) rss_mb | MB | 1 | 25.848 | 25.848 | 25.848 | 25.848 | n/a | n/a |
| docker (PID 158421) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 158472) rss_mb | MB | 1 | 23.789 | 23.789 | 23.789 | 23.789 | n/a | n/a |
| docker (PID 158472) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 158504) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 158504) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 158504) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 158504) rss_mb | MB | 39 | 25.715 | 25.715 | 25.715 | 25.715 | n/a | n/a |
| docker (PID 158504) vms_mb | MB | 39 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 158520) rss_mb | MB | 1 | 25.629 | 25.629 | 25.629 | 25.629 | n/a | n/a |
| docker (PID 158520) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 158538) rss_mb | MB | 1 | 25.621 | 25.621 | 25.621 | 25.621 | n/a | n/a |
| docker (PID 158538) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 158570) CPU | percent | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 158570) io read MB/s | MB/s | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 158570) io write MB/s | MB/s | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 158570) rss_mb | MB | 48 | 26.875 | 26.875 | 26.875 | 26.875 | n/a | n/a |
| docker (PID 158570) vms_mb | MB | 48 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 158587) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 158587) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 158587) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 158587) rss_mb | MB | 3 | 18.122 | 0.000 | 27.184 | 0.000 | n/a | n/a |
| docker (PID 158587) vms_mb | MB | 3 | 1107.182 | 0.000 | 1660.773 | 0.000 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 158626) CPU | percent | 5 | 7.765 | 0.000 | 38.825 | 0.000 | 0.040000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 158626) rss_mb | MB | 6 | 2.518 | 0.633 | 11.941 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 158626) vms_mb | MB | 6 | 262.581 | 1.055 | 1570.211 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 158638) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 158638) rss_mb | MB | 5 | 1.809 | 1.809 | 1.809 | 1.809 | n/a | n/a |
| tail [bear_0000] (PID 158638) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 158649) rss_mb | MB | 1 | 27.387 | 27.387 | 27.387 | 27.387 | n/a | n/a |
| docker (PID 158649) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 158668) rss_mb | MB | 1 | 11.898 | 11.898 | 11.898 | 11.898 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 158668) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 158675) rss_mb | MB | 1 | 27.246 | 27.246 | 27.246 | 27.246 | n/a | n/a |
| docker (PID 158675) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| sh [bear_0000] (PID 158694) rss_mb | MB | 1 | 1.586 | 1.586 | 1.586 | 1.586 | n/a | n/a |
| sh [bear_0000] (PID 158694) vms_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| base64 [bear_0000] (PID 158700) rss_mb | MB | 1 | 1.297 | 1.297 | 1.297 | 1.297 | n/a | n/a |
| base64 [bear_0000] (PID 158700) vms_mb | MB | 1 | 2.590 | 2.590 | 2.590 | 2.590 | n/a | n/a |
| docker (PID 158710) rss_mb | MB | 1 | 27.285 | 27.285 | 27.285 | 27.285 | n/a | n/a |
| docker (PID 158710) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 158742) rss_mb | MB | 1 | 26.633 | 26.633 | 26.633 | 26.633 | n/a | n/a |
| docker (PID 158742) vms_mb | MB | 1 | 1732.277 | 1732.277 | 1732.277 | 1732.277 | n/a | n/a |
| docker (PID 158751) rss_mb | MB | 1 | 26.000 | 26.000 | 26.000 | 26.000 | n/a | n/a |
| docker (PID 158751) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 158811) CPU | percent | 2 | 4.907 | 0.000 | 9.813 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 158811) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 158811) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 158811) rss_mb | MB | 3 | 17.417 | 1.812 | 25.219 | 25.219 | n/a | n/a |
| docker (PID 158811) vms_mb | MB | 3 | 1117.728 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bear_0000] (PID 158849) CPU | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bear_0000] (PID 158849) rss_mb | MB | 16 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bear_0000] (PID 158849) vms_mb | MB | 16 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 158863) CPU | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 158863) rss_mb | MB | 16 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [bear_0000] (PID 158863) vms_mb | MB | 16 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 158873) rss_mb | MB | 1 | 27.469 | 27.469 | 27.469 | 27.469 | n/a | n/a |
| docker (PID 158873) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 158893) rss_mb | MB | 1 | 11.094 | 11.094 | 11.094 | 11.094 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 158893) vms_mb | MB | 1 | 1569.703 | 1569.703 | 1569.703 | 1569.703 | n/a | n/a |
| docker (PID 158901) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 158901) io read MB/s | MB/s | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 158901) io write MB/s | MB/s | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 158901) rss_mb | MB | 14 | 27.070 | 27.070 | 27.070 | 27.070 | n/a | n/a |
| docker (PID 158901) vms_mb | MB | 14 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 158920) CPU | percent | 13 | 1.448 | 0.000 | 18.824 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 158920) rss_mb | MB | 14 | 4.086 | 3.480 | 11.957 | 3.480 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 158920) vms_mb | MB | 14 | 116.254 | 4.391 | 1570.477 | 4.391 | n/a | n/a |
| python [bear_0000] (PID 158929) CPU | percent | 12 | 96.318 | 85.970 | 110.948 | 89.452 | 1.220000 CPU seconds | n/a |
| python [bear_0000] (PID 158929) rss_mb | MB | 13 | 31.628 | 12.078 | 41.156 | 40.176 | n/a | n/a |
| python [bear_0000] (PID 158929) vms_mb | MB | 13 | 38.701 | 16.277 | 51.340 | 50.340 | n/a | n/a |
| docker (PID 158939) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 158939) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 158939) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 158939) rss_mb | MB | 2 | 25.883 | 25.883 | 25.883 | 25.883 | n/a | n/a |
| docker (PID 158939) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 159009) rss_mb | MB | 1 | 27.008 | 27.008 | 27.008 | 27.008 | n/a | n/a |
| docker (PID 159009) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 159020) rss_mb | MB | 1 | 25.797 | 25.797 | 25.797 | 25.797 | n/a | n/a |
| docker (PID 159020) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 159028) rss_mb | MB | 1 | 25.457 | 25.457 | 25.457 | 25.457 | n/a | n/a |
| docker (PID 159028) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 159068) CPU | percent | 3 | 3.250 | 0.000 | 9.750 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [beef_0000] (PID 159068) rss_mb | MB | 4 | 3.507 | 0.633 | 12.129 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 159068) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 159081) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 159081) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [beef_0000] (PID 159081) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 159091) rss_mb | MB | 1 | 27.402 | 27.402 | 27.402 | 27.402 | n/a | n/a |
| docker (PID 159091) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 159118) rss_mb | MB | 1 | 27.578 | 27.578 | 27.578 | 27.578 | n/a | n/a |
| docker (PID 159118) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 159184) rss_mb | MB | 1 | 8.844 | 8.844 | 8.844 | 8.844 | n/a | n/a |
| docker (PID 159184) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 159193) rss_mb | MB | 1 | 26.691 | 26.691 | 26.691 | 26.691 | n/a | n/a |
| docker (PID 159193) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 159254) rss_mb | MB | 1 | 26.770 | 26.770 | 26.770 | 26.770 | n/a | n/a |
| docker (PID 159254) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| 6 [beef_0000] (PID 159289) rss_mb | MB | 1 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| 6 [beef_0000] (PID 159289) vms_mb | MB | 1 | 13.980 | 13.980 | 13.980 | 13.980 | n/a | n/a |
| docker-init [beef_0000] (PID 159293) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beef_0000] (PID 159293) rss_mb | MB | 14 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [beef_0000] (PID 159293) vms_mb | MB | 14 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 159305) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 159305) rss_mb | MB | 14 | 1.773 | 1.773 | 1.773 | 1.773 | n/a | n/a |
| tail [beef_0000] (PID 159305) vms_mb | MB | 14 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 159342) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 159342) io read MB/s | MB/s | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 159342) io write MB/s | MB/s | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 159342) rss_mb | MB | 12 | 27.168 | 27.168 | 27.168 | 27.168 | n/a | n/a |
| docker (PID 159342) vms_mb | MB | 12 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 159362) CPU | percent | 11 | 1.765 | 0.000 | 19.420 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [beef_0000] (PID 159362) rss_mb | MB | 12 | 3.670 | 3.340 | 7.301 | 3.340 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 159362) vms_mb | MB | 12 | 134.791 | 4.391 | 1569.195 | 4.391 | n/a | n/a |
| python [beef_0000] (PID 159371) CPU | percent | 10 | 97.499 | 84.177 | 107.858 | 98.063 | 1.080000 CPU seconds | n/a |
| python [beef_0000] (PID 159371) rss_mb | MB | 11 | 32.934 | 15.672 | 41.520 | 41.520 | n/a | n/a |
| python [beef_0000] (PID 159371) vms_mb | MB | 11 | 40.515 | 19.680 | 51.238 | 51.238 | n/a | n/a |
| docker (PID 159399) rss_mb | MB | 1 | 15.652 | 15.652 | 15.652 | 15.652 | n/a | n/a |
| docker (PID 159399) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 159408) CPU | percent | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 159408) io read MB/s | MB/s | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 159408) io write MB/s | MB/s | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 159408) rss_mb | MB | 45 | 25.852 | 25.852 | 25.852 | 25.852 | n/a | n/a |
| docker (PID 159408) vms_mb | MB | 45 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 159425) CPU | percent | 1 | 9.150 | 9.150 | 9.150 | 9.150 | 0.010000 CPU seconds | n/a |
| docker (PID 159425) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 159425) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 159425) rss_mb | MB | 2 | 13.871 | 1.742 | 26.000 | 26.000 | n/a | n/a |
| docker (PID 159425) vms_mb | MB | 2 | 846.486 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 159467) rss_mb | MB | 1 | 17.062 | 17.062 | 17.062 | 17.062 | n/a | n/a |
| docker (PID 159467) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 159484) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 159484) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 159484) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 159484) rss_mb | MB | 2 | 25.691 | 25.691 | 25.691 | 25.691 | n/a | n/a |
| docker (PID 159484) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 159523) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [beef_0000] (PID 159523) rss_mb | MB | 6 | 2.708 | 0.633 | 13.086 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 159523) vms_mb | MB | 6 | 274.709 | 1.055 | 1642.980 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 159537) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 159537) rss_mb | MB | 5 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [beef_0000] (PID 159537) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 159548) rss_mb | MB | 1 | 9.305 | 9.305 | 9.305 | 9.305 | n/a | n/a |
| docker (PID 159548) vms_mb | MB | 1 | 1315.695 | 1315.695 | 1315.695 | 1315.695 | n/a | n/a |
| docker (PID 159575) rss_mb | MB | 1 | 15.145 | 15.145 | 15.145 | 15.145 | n/a | n/a |
| docker (PID 159575) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 159602) rss_mb | MB | 1 | 4.480 | 4.480 | 4.480 | 4.480 | n/a | n/a |
| docker (PID 159602) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 159611) rss_mb | MB | 1 | 27.520 | 27.520 | 27.520 | 27.520 | n/a | n/a |
| docker (PID 159611) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 159629) rss_mb | MB | 1 | 11.590 | 11.590 | 11.590 | 11.590 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 159629) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 159646) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 159646) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 159646) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 159646) rss_mb | MB | 2 | 25.930 | 25.930 | 25.930 | 25.930 | n/a | n/a |
| docker (PID 159646) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 159706) rss_mb | MB | 1 | 26.418 | 26.418 | 26.418 | 26.418 | n/a | n/a |
| docker (PID 159706) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 159730) rss_mb | MB | 1 | 16.020 | 16.020 | 16.020 | 16.020 | n/a | n/a |
| docker (PID 159730) vms_mb | MB | 1 | 1587.703 | 1587.703 | 1587.703 | 1587.703 | n/a | n/a |
| python3 (PID 159737) CPU | percent | 3 | 98.738 | 98.436 | 98.907 | 98.907 | 0.300000 CPU seconds | n/a |
| python3 (PID 159737) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 159737) io write MB/s | MB/s | 3 | 0.914 | 0.000 | 2.743 | 2.743 | 0.277344 MB | n/a |
| python3 (PID 159737) rss_mb | MB | 4 | 28.207 | 17.855 | 34.621 | 34.621 | n/a | n/a |
| python3 (PID 159737) vms_mb | MB | 4 | 51.820 | 42.434 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 159755) rss_mb | MB | 1 | 26.809 | 26.809 | 26.809 | 26.809 | n/a | n/a |
| docker (PID 159755) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 159774) rss_mb | MB | 1 | 26.938 | 26.938 | 26.938 | 26.938 | n/a | n/a |
| docker (PID 159774) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 159788) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 159788) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 159788) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 159788) rss_mb | MB | 2 | 27.949 | 27.949 | 27.949 | 27.949 | n/a | n/a |
| docker (PID 159788) vms_mb | MB | 2 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [bell_0000] (PID 159828) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bell_0000] (PID 159828) rss_mb | MB | 4 | 3.675 | 0.633 | 12.801 | 0.633 | n/a | n/a |
| docker-init [bell_0000] (PID 159828) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 159841) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 159841) rss_mb | MB | 3 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [bell_0000] (PID 159841) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 159870) rss_mb | MB | 1 | 3.324 | 3.324 | 3.324 | 3.324 | n/a | n/a |
| docker (PID 159870) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 159905) rss_mb | MB | 1 | 25.676 | 25.676 | 25.676 | 25.676 | n/a | n/a |
| docker (PID 159905) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 159940) rss_mb | MB | 1 | 27.383 | 27.383 | 27.383 | 27.383 | n/a | n/a |
| docker (PID 159940) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 159976) rss_mb | MB | 1 | 26.840 | 26.840 | 26.840 | 26.840 | n/a | n/a |
| docker (PID 159976) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 160017) rss_mb | MB | 1 | 25.859 | 25.859 | 25.859 | 25.859 | n/a | n/a |
| docker (PID 160017) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 160033) rss_mb | MB | 1 | 26.930 | 26.930 | 26.930 | 26.930 | n/a | n/a |
| docker (PID 160033) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 160072) CPU | percent | 3 | 9.735 | 0.000 | 29.205 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [bell_0000] (PID 160072) rss_mb | MB | 4 | 3.045 | 0.562 | 10.492 | 0.562 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 160072) vms_mb | MB | 4 | 375.089 | 1.055 | 1497.191 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 160085) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 160085) rss_mb | MB | 3 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [bell_0000] (PID 160085) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 160095) rss_mb | MB | 1 | 9.230 | 9.230 | 9.230 | 9.230 | n/a | n/a |
| docker (PID 160095) vms_mb | MB | 1 | 1235.438 | 1235.438 | 1235.438 | 1235.438 | n/a | n/a |
| docker (PID 160123) rss_mb | MB | 1 | 27.535 | 27.535 | 27.535 | 27.535 | n/a | n/a |
| docker (PID 160123) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 160142) rss_mb | MB | 1 | 11.289 | 11.289 | 11.289 | 11.289 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 160142) vms_mb | MB | 1 | 1570.090 | 1570.090 | 1570.090 | 1570.090 | n/a | n/a |
| docker (PID 160157) rss_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| docker (PID 160157) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 160177) rss_mb | MB | 1 | 11.914 | 11.914 | 11.914 | 11.914 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 160177) vms_mb | MB | 1 | 1642.980 | 1642.980 | 1642.980 | 1642.980 | n/a | n/a |
| docker (PID 160194) rss_mb | MB | 1 | 27.102 | 27.102 | 27.102 | 27.102 | n/a | n/a |
| docker (PID 160194) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 160209) rss_mb | MB | 1 | 22.660 | 22.660 | 22.660 | 22.660 | n/a | n/a |
| docker (PID 160209) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 160278) rss_mb | MB | 1 | 27.027 | 27.027 | 27.027 | 27.027 | n/a | n/a |
| docker (PID 160278) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 160286) CPU | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 160286) io read MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 160286) io write MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 160286) rss_mb | MB | 40 | 25.473 | 25.473 | 25.473 | 25.473 | n/a | n/a |
| docker (PID 160286) vms_mb | MB | 40 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 160319) rss_mb | MB | 1 | 25.656 | 25.656 | 25.656 | 25.656 | n/a | n/a |
| docker (PID 160319) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| python3 (PID 160334) CPU | percent | 3 | 98.731 | 98.423 | 98.943 | 98.943 | 0.300000 CPU seconds | n/a |
| python3 (PID 160334) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 160334) io write MB/s | MB/s | 3 | 0.915 | 0.000 | 2.744 | 2.744 | 0.277344 MB | n/a |
| python3 (PID 160334) rss_mb | MB | 4 | 26.365 | 13.980 | 34.703 | 34.703 | n/a | n/a |
| python3 (PID 160334) vms_mb | MB | 4 | 50.380 | 39.570 | 57.441 | 57.441 | n/a | n/a |
| docker (PID 160353) rss_mb | MB | 1 | 26.035 | 26.035 | 26.035 | 26.035 | n/a | n/a |
| docker (PID 160353) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 160377) rss_mb | MB | 1 | 15.715 | 15.715 | 15.715 | 15.715 | n/a | n/a |
| docker (PID 160377) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 160399) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 160399) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 160399) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 160399) rss_mb | MB | 38 | 27.188 | 27.188 | 27.188 | 27.188 | n/a | n/a |
| docker (PID 160399) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 160441) rss_mb | MB | 1 | 26.938 | 26.938 | 26.938 | 26.938 | n/a | n/a |
| docker (PID 160441) vms_mb | MB | 1 | 1588.520 | 1588.520 | 1588.520 | 1588.520 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 160481) CPU | percent | 3 | 3.254 | 0.000 | 9.762 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bell_0000] (PID 160481) rss_mb | MB | 4 | 3.558 | 0.633 | 12.332 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 160481) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 160495) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 160495) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bell_0000] (PID 160495) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 160506) rss_mb | MB | 1 | 27.281 | 27.281 | 27.281 | 27.281 | n/a | n/a |
| docker (PID 160506) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 160560) rss_mb | MB | 1 | 2.031 | 2.031 | 2.031 | 2.031 | n/a | n/a |
| docker (PID 160560) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 160600) rss_mb | MB | 1 | 26.133 | 26.133 | 26.133 | 26.133 | n/a | n/a |
| docker (PID 160600) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 160608) rss_mb | MB | 1 | 25.816 | 25.816 | 25.816 | 25.816 | n/a | n/a |
| docker (PID 160608) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 160666) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 160666) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 160666) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 160666) rss_mb | MB | 2 | 25.699 | 25.699 | 25.699 | 25.699 | n/a | n/a |
| docker (PID 160666) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 160706) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bell_0000] (PID 160706) rss_mb | MB | 11 | 1.730 | 0.633 | 12.703 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 160706) vms_mb | MB | 11 | 143.707 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 160718) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 160718) rss_mb | MB | 10 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [bell_0000] (PID 160718) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 160728) rss_mb | MB | 1 | 27.066 | 27.066 | 27.066 | 27.066 | n/a | n/a |
| docker (PID 160728) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 160748) rss_mb | MB | 1 | 12.199 | 12.199 | 12.199 | 12.199 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 160748) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 160755) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 160755) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 160755) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 160755) rss_mb | MB | 8 | 27.098 | 27.082 | 27.207 | 27.207 | n/a | n/a |
| docker (PID 160755) vms_mb | MB | 8 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [bell_0000] (PID 160775) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bell_0000] (PID 160775) rss_mb | MB | 8 | 3.340 | 3.340 | 3.340 | 3.340 | n/a | n/a |
| bash [bell_0000] (PID 160775) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bell_0000] (PID 160785) CPU | percent | 7 | 100.651 | 88.155 | 107.904 | 107.904 | 0.720000 CPU seconds | n/a |
| python [bell_0000] (PID 160785) rss_mb | MB | 8 | 30.632 | 10.812 | 41.719 | 41.719 | n/a | n/a |
| python [bell_0000] (PID 160785) vms_mb | MB | 8 | 37.978 | 14.770 | 51.238 | 51.238 | n/a | n/a |
| docker (PID 160795) CPU | percent | 1 | 9.775 | 9.775 | 9.775 | 9.775 | 0.010000 CPU seconds | n/a |
| docker (PID 160795) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 160795) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 160795) rss_mb | MB | 2 | 16.275 | 6.617 | 25.934 | 25.934 | n/a | n/a |
| docker (PID 160795) vms_mb | MB | 2 | 846.486 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 160879) rss_mb | MB | 1 | 9.609 | 9.609 | 9.609 | 9.609 | n/a | n/a |
| docker (PID 160879) vms_mb | MB | 1 | 1459.953 | 1459.953 | 1459.953 | 1459.953 | n/a | n/a |
| docker (PID 160887) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 160887) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 160887) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 160887) rss_mb | MB | 39 | 25.344 | 25.344 | 25.344 | 25.344 | n/a | n/a |
| docker (PID 160887) vms_mb | MB | 39 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 160920) rss_mb | MB | 1 | 7.820 | 7.820 | 7.820 | 7.820 | n/a | n/a |
| docker (PID 160920) vms_mb | MB | 1 | 32.867 | 32.867 | 32.867 | 32.867 | n/a | n/a |
| python3 (PID 160936) CPU | percent | 3 | 102.003 | 98.434 | 108.773 | 108.773 | 0.310000 CPU seconds | n/a |
| python3 (PID 160936) io read MB/s | MB/s | 3 | 0.013 | 0.000 | 0.039 | 0.039 | 0.003906 MB | n/a |
| python3 (PID 160936) io write MB/s | MB/s | 3 | 0.914 | 0.000 | 2.743 | 2.743 | 0.277344 MB | n/a |
| python3 (PID 160936) rss_mb | MB | 4 | 24.580 | 10.609 | 34.535 | 34.535 | n/a | n/a |
| python3 (PID 160936) vms_mb | MB | 4 | 48.613 | 36.633 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 160955) rss_mb | MB | 1 | 2.676 | 2.676 | 2.676 | 2.676 | n/a | n/a |
| docker (PID 160955) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| sandbox alex_0000 CPU | percent | 32 | 52.416 | 3.423 | 100.962 | 33.750 | 1.744757 CPU seconds | n/a |
| sandbox alex_0000 io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox alex_0000 io write MB/s | MB/s | 37 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox alex_0000 memory | MB | 39 | 7.401 | 0.586 | 36.238 | 0.828 | n/a | n/a |
| sandbox alex_0000 net rx MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox alex_0000 net tx MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox andy_0000 CPU | percent | 23 | 56.750 | 15.298 | 100.874 | 29.649 | 1.342641 CPU seconds | n/a |
| sandbox andy_0000 io read MB/s | MB/s | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox andy_0000 io write MB/s | MB/s | 27 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox andy_0000 memory | MB | 29 | 9.529 | 0.633 | 35.633 | 0.664 | n/a | n/a |
| sandbox andy_0000 net rx MB/s | MB/s | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox andy_0000 net tx MB/s | MB/s | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox arch_0000 CPU | percent | 23 | 55.256 | 3.742 | 112.872 | 31.325 | 1.327792 CPU seconds | n/a |
| sandbox arch_0000 io read MB/s | MB/s | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox arch_0000 io write MB/s | MB/s | 26 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox arch_0000 memory | MB | 28 | 8.670 | 0.000 | 35.430 | 1.008 | n/a | n/a |
| sandbox arch_0000 net rx MB/s | MB/s | 26 | 5.110 | 0.000 | 132.862 | 0.000 | 3567.778607 MB | n/a |
| sandbox arch_0000 net tx MB/s | MB/s | 26 | 0.058 | 0.000 | 1.510 | 0.000 | 40.536980 MB | n/a |
| sandbox bake_0000 CPU | percent | 28 | 52.602 | 3.472 | 101.060 | 38.038 | 1.525172 CPU seconds | n/a |
| sandbox bake_0000 io read MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bake_0000 io write MB/s | MB/s | 32 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bake_0000 memory | MB | 34 | 8.304 | 0.633 | 35.695 | 4.094 | n/a | n/a |
| sandbox bake_0000 net rx MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bake_0000 net tx MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bale_0000 CPU | percent | 47 | 83.205 | 18.884 | 100.526 | 41.945 | 3.991573 CPU seconds | n/a |
| sandbox bale_0000 io read MB/s | MB/s | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bale_0000 io write MB/s | MB/s | 50 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bale_0000 memory | MB | 52 | 23.044 | 0.629 | 35.461 | 4.238 | n/a | n/a |
| sandbox bale_0000 net rx MB/s | MB/s | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bale_0000 net tx MB/s | MB/s | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox band_0000 CPU | percent | 20 | 60.499 | 24.852 | 100.759 | 46.495 | 1.245095 CPU seconds | n/a |
| sandbox band_0000 io read MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox band_0000 io write MB/s | MB/s | 23 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox band_0000 memory | MB | 25 | 9.721 | 0.625 | 35.531 | 4.043 | n/a | n/a |
| sandbox band_0000 net rx MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox band_0000 net tx MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bart_0000 CPU | percent | 35 | 47.340 | 0.000 | 100.107 | 31.595 | 1.719128 CPU seconds | n/a |
| sandbox bart_0000 io read MB/s | MB/s | 42 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bart_0000 io write MB/s | MB/s | 41 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bart_0000 memory | MB | 43 | 6.579 | 0.637 | 35.582 | 0.754 | n/a | n/a |
| sandbox bart_0000 net rx MB/s | MB/s | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bart_0000 net tx MB/s | MB/s | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox base_0000 CPU | percent | 38 | 58.500 | 2.575 | 100.848 | 41.514 | 2.286452 CPU seconds | n/a |
| sandbox base_0000 io read MB/s | MB/s | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox base_0000 io write MB/s | MB/s | 43 | 0.002 | 0.000 | 0.038 | 0.000 | 0.007812 MB | n/a |
| sandbox base_0000 memory | MB | 46 | 8.611 | 0.680 | 35.160 | 0.730 | n/a | n/a |
| sandbox base_0000 net rx MB/s | MB/s | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox base_0000 net tx MB/s | MB/s | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beam_0000 CPU | percent | 28 | 62.423 | 3.405 | 99.140 | 27.152 | 1.851459 CPU seconds | n/a |
| sandbox beam_0000 io read MB/s | MB/s | 32 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beam_0000 io write MB/s | MB/s | 31 | 0.001 | 0.000 | 0.037 | 0.000 | 0.003906 MB | n/a |
| sandbox beam_0000 memory | MB | 33 | 12.246 | 0.680 | 35.340 | 3.914 | n/a | n/a |
| sandbox beam_0000 net rx MB/s | MB/s | 32 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beam_0000 net tx MB/s | MB/s | 32 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bear_0000 CPU | percent | 34 | 54.896 | 0.872 | 101.583 | 88.932 | 1.989325 CPU seconds | n/a |
| sandbox bear_0000 io read MB/s | MB/s | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bear_0000 io write MB/s | MB/s | 40 | 0.001 | 0.000 | 0.036 | 0.000 | 0.003906 MB | n/a |
| sandbox bear_0000 memory | MB | 41 | 9.668 | 0.637 | 34.863 | 33.641 | n/a | n/a |
| sandbox bear_0000 net rx MB/s | MB/s | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bear_0000 net tx MB/s | MB/s | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beef_0000 CPU | percent | 26 | 61.180 | 3.790 | 105.087 | 15.665 | 1.721845 CPU seconds | n/a |
| sandbox beef_0000 io read MB/s | MB/s | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beef_0000 io write MB/s | MB/s | 29 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox beef_0000 memory | MB | 31 | 10.799 | 0.000 | 35.250 | 0.711 | n/a | n/a |
| sandbox beef_0000 net rx MB/s | MB/s | 29 | 64.202 | 0.000 | 1861.859 | 0.000 | 3571.712593 MB | n/a |
| sandbox beef_0000 net tx MB/s | MB/s | 29 | 0.764 | 0.000 | 22.157 | 0.000 | 42.504932 MB | n/a |
| sandbox bell_0000 CPU | percent | 17 | 66.138 | 18.353 | 100.044 | 70.323 | 1.152883 CPU seconds | n/a |
| sandbox bell_0000 io read MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bell_0000 io write MB/s | MB/s | 20 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bell_0000 memory | MB | 21 | 11.029 | 0.680 | 35.215 | 3.746 | n/a | n/a |
| sandbox bell_0000 net rx MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bell_0000 net tx MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| workload total CPU | percent | 4055 | 26.476 | 0.579 | 189.365 | 64.529 | 110.249813 CPU seconds | n/a |
| workload total io read MB/s | MB/s | 450 | 0.010 | 0.000 | 1.207 | 0.000 | 0.464844 MB | n/a |
| workload total io write MB/s | MB/s | 441 | 0.014 | 0.000 | 1.966 | 0.000 | 0.687500 MB | n/a |
| workload total memory | MB | 4056 | 515.488 | 395.660 | 579.250 | 531.734 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
