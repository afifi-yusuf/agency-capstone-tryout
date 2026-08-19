# agprof summary

- Duration: **409.655 s**
- Runs: **12/12 completed**, 12 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.029 runs/s**
- LLM: **39 calls**, 39 succeeded, 0 failed, 0 interrupted, 0 retries, 188.829 s total wait
- Tools: **51/51 completed**, 1 failed, 0 interrupted
- Raw resource samples: **44967** at 9.88 Hz effective (10 Hz configured)
- GPU sampling: **unavailable** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 21668.530 / 32829.017 ms |
| LLM latency p50 / p95 | 2790.181 / 15799.754 ms |
| LLM TTFT p50 / p95 | 624.382 / 1146.605 ms |
| LLM input / output tokens | 202734 / 9187 |
| LLM output throughput | 56.551 tokens/s |
| LLM attempts | 39 total, 39 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 444.825 / 1199.639 ms |

### Tool outcomes

| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 6/6 | 6 | 0 | 0 | 1199.639 ms | 3203.457 ms |
| edit | 6/6 | 6 | 0 | 0 | 459.192 ms | 469.381 ms |
| glob | 1/1 | 1 | 0 | 0 | 369.627 ms | 369.627 ms |
| read | 19/19 | 19 | 0 | 0 | 450.594 ms | 636.198 ms |
| return_plan | 6/6 | 6 | 0 | 0 | 0.327 ms | 0.411 ms |
| return_status | 6/6 | 6 | 0 | 0 | 0.314 ms | 0.325 ms |
| return_summary | 7/7 | 6 | 1 | 0 | 0.384 ms | 0.400 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 41.007% | 104.809% | 168.081 s | 446.490 MB | 505.438 MB | 0.132812 MB | 0.023438 MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python3 | 9098 |  | 4046 | 2.750% | 124.806% | 11.580 s | 671.538 MB | 691.383 MB | 3618.249 MB | 3757.148 MB | 15.355469 MB | 15.265625 MB |
| git | 9104 |  | 2 | 0.000% | 0.000% | 0.000 s | 4.910 MB | 4.910 MB | 12.516 MB | 12.516 MB | 0.000000 MB | 0.000000 MB |
| git-remote-http | 9106 |  | 2 | 39.512% | 39.512% | 0.040 s | 14.725 MB | 19.227 MB | 103.322 MB | 107.566 MB | 0.000000 MB | 0.000000 MB |
| git | 9105 |  | 2 | 0.000% | 0.000% | 0.000 s | 3.559 MB | 3.559 MB | 11.273 MB | 11.273 MB | 0.000000 MB | 0.000000 MB |
| python3 | 9112 |  | 1190 | 99.970% | 109.087% | 120.020 s | 33.987 MB | 34.020 MB | 56.473 MB | 56.500 MB | 0.179688 MB | 0.015625 MB |
| python3 | 9115 |  | 5 | 89.115% | 109.000% | 0.360 s | 26.147 MB | 34.582 MB | 49.952 MB | 57.512 MB | 1.191406 MB | 0.195312 MB |
| python3 | 9116 |  | 4 | 99.031% | 99.140% | 0.300 s | 26.113 MB | 35.789 MB | 50.231 MB | 58.500 MB | 0.000000 MB | 0.015625 MB |
| python3 | 9117 |  | 3 | 99.030% | 108.881% | 0.200 s | 27.665 MB | 34.066 MB | 51.302 MB | 56.504 MB | 0.000000 MB | 0.015625 MB |
| python3 | 9118 |  | 25 | 100.293% | 108.981% | 2.430 s | 33.295 MB | 34.918 MB | 56.644 MB | 57.512 MB | 0.000000 MB | 0.199219 MB |
| python3 | 9119 |  | 69 | 99.915% | 108.987% | 6.860 s | 41.318 MB | 47.430 MB | 64.575 MB | 70.637 MB | 0.000000 MB | 0.199219 MB |
| docker | 9123 |  | 1 | n/a% | n/a% | n/a s | 24.902 MB | 24.902 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker-trust | 9131 |  | 1 | n/a% | n/a% | n/a s | 12.184 MB | 12.184 MB | 1212.965 MB | 1212.965 MB | n/a MB | n/a MB |
| docker | 9173 |  | 3 | 9.883% | 9.912% | 0.020 s | 23.940 MB | 27.336 MB | 1636.417 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 9213 | alex_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.055 MB | 12.746 MB | 314.889 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 9241 | alex_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 9243 |  | 1 | n/a% | n/a% | n/a s | 27.336 MB | 27.336 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 9296 | alex_0000 | 1 | n/a% | n/a% | n/a s | 10.930 MB | 10.930 MB | 1569.711 MB | 1569.711 MB | n/a MB | n/a MB |
| docker | 9277 |  | 1 | n/a% | n/a% | n/a s | 27.266 MB | 27.266 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 9331 |  | 1 | n/a% | n/a% | n/a s | 26.434 MB | 26.434 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 9376 |  | 2 | 9.815% | 9.815% | 0.010 s | 24.652 MB | 26.660 MB | 1624.488 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 9443 |  | 1 | n/a% | n/a% | n/a s | 17.832 MB | 17.832 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 9491 | alex_0000 | 4 | 3.279% | 9.837% | 0.010 s | 3.514 MB | 12.156 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 9451 |  | 1 | n/a% | n/a% | n/a s | 26.934 MB | 26.934 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 9516 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 9553 |  | 1 | n/a% | n/a% | n/a s | 27.117 MB | 27.117 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| 6 | 9567 | alex_0000 | 1 | n/a% | n/a% | n/a s | 0.816 MB | 0.816 MB | 14.004 MB | 14.004 MB | n/a MB | n/a MB |
| docker | 9587 |  | 1 | n/a% | n/a% | n/a s | 27.266 MB | 27.266 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 9608 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.445 MB | 11.445 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 9625 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.238 MB | 26.238 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 9721 |  | 53 | 0.000% | 0.000% | 0.000 s | 25.844 MB | 25.844 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 9737 |  | 1 | n/a% | n/a% | n/a s | 25.539 MB | 25.539 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 9763 |  | 2 | 0.000% | 0.000% | 0.000 s | 24.133 MB | 25.438 MB | 1624.082 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 9803 | alex_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.628 MB | 12.613 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 9831 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.809 MB | 1.809 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 9888 | alex_0000 | 1 | n/a% | n/a% | n/a s | 9.668 MB | 9.668 MB | 1569.195 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 9867 |  | 1 | n/a% | n/a% | n/a s | 27.020 MB | 27.020 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 9904 |  | 1 | n/a% | n/a% | n/a s | 27.281 MB | 27.281 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 9924 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.500 MB | 11.500 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 9943 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.828 MB | 26.828 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 10006 |  | 1 | n/a% | n/a% | n/a s | 16.582 MB | 16.582 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 10053 | alex_0000 | 12 | 2.648% | 29.123% | 0.030 s | 1.592 MB | 12.148 MB | 131.828 MB | 1570.340 MB | n/a MB | n/a MB |
| docker | 10014 |  | 1 | n/a% | n/a% | n/a s | 26.855 MB | 26.855 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 10077 | alex_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.691 MB | 1.691 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 10079 |  | 1 | n/a% | n/a% | n/a s | 16.172 MB | 16.172 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 10116 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.312 MB | 27.312 MB | 1661.023 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| bash | 10136 | alex_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.305 MB | 3.305 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 10145 | alex_0000 | 8 | 99.436% | 108.016% | 0.710 s | 31.607 MB | 42.070 MB | 38.569 MB | 51.238 MB | n/a MB | n/a MB |
| docker | 10155 |  | 2 | 9.812% | 9.812% | 0.010 s | 17.352 MB | 25.977 MB | 1443.822 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 10229 |  | 2 | 9.909% | 9.909% | 0.010 s | 26.297 MB | 26.422 MB | 1660.648 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 10267 | alex_0000 | 4 | 3.285% | 9.854% | 0.010 s | 3.637 MB | 12.648 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 10302 |  | 1 | n/a% | n/a% | n/a s | 15.332 MB | 15.332 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 10292 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.539 MB | 1.539 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 10349 | alex_0000 | 1 | n/a% | n/a% | n/a s | 10.961 MB | 10.961 MB | 1569.711 MB | 1569.711 MB | n/a MB | n/a MB |
| docker | 10329 |  | 1 | n/a% | n/a% | n/a s | 27.309 MB | 27.309 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 10364 |  | 1 | n/a% | n/a% | n/a s | 27.145 MB | 27.145 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 10383 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.871 MB | 11.871 MB | 1570.977 MB | 1570.977 MB | n/a MB | n/a MB |
| docker | 10400 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.891 MB | 25.891 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 10488 |  | 1 | n/a% | n/a% | n/a s | 25.715 MB | 25.715 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 10496 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.652 MB | 25.652 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| python3 | 10544 |  | 4 | 98.855% | 99.005% | 0.300 s | 25.198 MB | 34.336 MB | 49.604 MB | 57.438 MB | 0.000000 MB | 0.167969 MB |
| docker | 10547 |  | 1 | n/a% | n/a% | n/a s | 18.223 MB | 18.223 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 10573 |  | 1 | n/a% | n/a% | n/a s | 25.746 MB | 25.746 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 10597 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.229 MB | 27.375 MB | 1708.776 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 10638 | andy_0000 | 5 | 7.377% | 29.507% | 0.030 s | 2.712 MB | 11.031 MB | 329.184 MB | 1641.699 MB | n/a MB | n/a MB |
| tail | 10667 | andy_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 10704 |  | 1 | n/a% | n/a% | n/a s | 20.547 MB | 20.547 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 10734 |  | 1 | n/a% | n/a% | n/a s | 27.234 MB | 27.234 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 10754 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.527 MB | 11.527 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 10769 |  | 1 | n/a% | n/a% | n/a s | 27.086 MB | 27.086 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| sh | 10788 | andy_0000 | 1 | n/a% | n/a% | n/a s | 1.676 MB | 1.676 MB | 2.617 MB | 2.617 MB | n/a MB | n/a MB |
| docker | 10806 |  | 1 | n/a% | n/a% | n/a s | 26.902 MB | 26.902 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 10863 |  | 1 | n/a% | n/a% | n/a s | 8.164 MB | 8.164 MB | 32.867 MB | 32.867 MB | n/a MB | n/a MB |
| docker | 10880 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.965 MB | 26.965 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 10920 | andy_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 10944 | andy_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 10982 |  | 1 | n/a% | n/a% | n/a s | 7.215 MB | 7.215 MB | 32.867 MB | 32.867 MB | n/a MB | n/a MB |
| docker | 11016 |  | 1 | n/a% | n/a% | n/a s | 23.934 MB | 23.934 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 11053 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.023 MB | 26.023 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 11128 |  | 1 | n/a% | n/a% | n/a s | 4.004 MB | 4.004 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 11150 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.332 MB | 26.332 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 11194 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.746 MB | 26.746 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 11233 | andy_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.642 MB | 12.668 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 11291 | andy_0000 | 1 | n/a% | n/a% | n/a s | 4.496 MB | 4.496 MB | 1432.941 MB | 1432.941 MB | n/a MB | n/a MB |
| docker | 11272 |  | 1 | n/a% | n/a% | n/a s | 27.199 MB | 27.199 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 11257 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.695 MB | 1.695 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 11364 |  | 1 | n/a% | n/a% | n/a s | 17.070 MB | 17.070 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 11372 |  | 1 | n/a% | n/a% | n/a s | 25.836 MB | 25.836 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 11430 |  | 1 | n/a% | n/a% | n/a s | 0.934 MB | 0.934 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 11447 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.727 MB | 26.727 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 11488 | andy_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.739 MB | 12.805 MB | 143.707 MB | 1570.227 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 11546 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.355 MB | 11.355 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 11525 |  | 1 | n/a% | n/a% | n/a s | 26.855 MB | 26.855 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 11513 | andy_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 11553 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.383 MB | 27.383 MB | 1733.027 MB | 1733.027 MB | 0.000000 MB | 0.000000 MB |
| python | 11583 | andy_0000 | 8 | 100.770% | 107.777% | 0.720 s | 30.569 MB | 42.672 MB | 37.748 MB | 52.238 MB | n/a MB | n/a MB |
| bash | 11574 | andy_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.379 MB | 3.379 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 11585 |  | 1 | n/a% | n/a% | n/a s | 24.566 MB | 24.566 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 11593 |  | 1 | n/a% | n/a% | n/a s | 26.309 MB | 26.309 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 11648 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 11709 | andy_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.590 MB | 12.461 MB | 393.473 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 11668 |  | 1 | n/a% | n/a% | n/a s | 26.918 MB | 26.918 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 11733 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 11770 |  | 1 | n/a% | n/a% | n/a s | 26.996 MB | 26.996 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 11790 | andy_0000 | 1 | n/a% | n/a% | n/a s | 4.000 MB | 4.000 MB | 1208.676 MB | 1208.676 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 11825 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.352 MB | 11.352 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 11805 |  | 1 | n/a% | n/a% | n/a s | 26.984 MB | 26.984 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 11842 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.582 MB | 26.582 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 11939 |  | 39 | 0.000% | 0.000% | 0.000 s | 26.797 MB | 26.797 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 11971 |  | 1 | n/a% | n/a% | n/a s | 26.816 MB | 26.816 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 11987 |  | 4 | 102.145% | 108.603% | 0.310 s | 26.089 MB | 33.406 MB | 49.882 MB | 56.375 MB | 0.000000 MB | 0.000000 MB |
| docker | 12007 |  | 1 | n/a% | n/a% | n/a s | 23.301 MB | 23.301 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 12038 |  | 4 | 6.159% | 18.478% | 0.020 s | 27.107 MB | 27.211 MB | 1714.776 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 12079 | arch_0000 | 6 | 7.829% | 39.146% | 0.040 s | 3.681 MB | 12.934 MB | 502.648 MB | 1570.477 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 12129 |  | 1 | n/a% | n/a% | n/a s | 3.703 MB | 3.703 MB | 1208.676 MB | 1208.676 MB | n/a MB | n/a MB |
| tail | 12107 | arch_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 12110 |  | 1 | n/a% | n/a% | n/a s | 26.719 MB | 26.719 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 12144 |  | 1 | n/a% | n/a% | n/a s | 27.258 MB | 27.258 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[1:CHILD] | 12162 | arch_0000 | 1 | n/a% | n/a% | n/a s | 1.309 MB | 1.309 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 12163 | arch_0000 | 1 | n/a% | n/a% | n/a s | 0.695 MB | 0.695 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 12161 | arch_0000 | 1 | n/a% | n/a% | n/a s | 1.996 MB | 1.996 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 12171 |  | 1 | n/a% | n/a% | n/a s | 27.422 MB | 27.422 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 12234 |  | 1 | n/a% | n/a% | n/a s | 19.969 MB | 19.969 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 12242 |  | 1 | n/a% | n/a% | n/a s | 25.941 MB | 25.941 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 12315 |  | 1 | n/a% | n/a% | n/a s | 9.293 MB | 9.293 MB | 1371.941 MB | 1371.941 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 12363 | arch_0000 | 4 | 6.536% | 19.609% | 0.020 s | 3.326 MB | 11.406 MB | 393.187 MB | 1569.582 MB | n/a MB | n/a MB |
| docker | 12323 |  | 1 | n/a% | n/a% | n/a s | 25.590 MB | 25.590 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 12386 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.691 MB | 1.691 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 12388 |  | 1 | n/a% | n/a% | n/a s | 8.605 MB | 8.605 MB | 1227.309 MB | 1227.309 MB | n/a MB | n/a MB |
| docker | 12423 |  | 1 | n/a% | n/a% | n/a s | 25.645 MB | 25.645 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| 6 | 12477 | arch_0000 | 1 | n/a% | n/a% | n/a s | 0.711 MB | 0.711 MB | 14.004 MB | 14.004 MB | n/a MB | n/a MB |
| docker | 12460 |  | 1 | n/a% | n/a% | n/a s | 26.996 MB | 26.996 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 12497 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.184 MB | 26.184 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 12571 |  | 1 | n/a% | n/a% | n/a s | 1.258 MB | 1.258 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 12593 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.344 MB | 26.344 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 12637 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.652 MB | 25.652 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 12675 | arch_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.707 MB | 12.930 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 12700 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 12733 | arch_0000 | 1 | n/a% | n/a% | n/a s | 11.570 MB | 11.570 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 12713 |  | 1 | n/a% | n/a% | n/a s | 27.266 MB | 27.266 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 12768 |  | 1 | n/a% | n/a% | n/a s | 25.801 MB | 25.801 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 12813 |  | 2 | 9.797% | 9.797% | 0.010 s | 17.816 MB | 26.906 MB | 1480.105 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 12891 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.336 MB | 25.336 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 12930 | arch_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.746 MB | 12.883 MB | 143.729 MB | 1570.477 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 12982 | arch_0000 | 1 | n/a% | n/a% | n/a s | 1.965 MB | 1.965 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 12984 | arch_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 12965 |  | 1 | n/a% | n/a% | n/a s | 27.363 MB | 27.363 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 12954 | arch_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| bash | 13016 | arch_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.418 MB | 3.418 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 12994 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.242 MB | 27.242 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 13026 | arch_0000 | 8 | 98.019% | 107.883% | 0.700 s | 29.400 MB | 42.035 MB | 36.951 MB | 51.219 MB | n/a MB | n/a MB |
| docker | 13028 |  | 1 | n/a% | n/a% | n/a s | 4.469 MB | 4.469 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 13036 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.098 MB | 27.098 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 13109 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.543 MB | 26.543 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 13148 | arch_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.614 MB | 12.559 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 13172 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.801 MB | 1.801 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 13202 | arch_0000 | 1 | n/a% | n/a% | n/a s | 11.336 MB | 11.336 MB | 1570.340 MB | 1570.340 MB | n/a MB | n/a MB |
| docker | 13182 |  | 1 | n/a% | n/a% | n/a s | 27.297 MB | 27.297 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 13238 |  | 1 | n/a% | n/a% | n/a s | 21.102 MB | 21.102 MB | 1524.203 MB | 1524.203 MB | n/a MB | n/a MB |
| docker | 13285 |  | 2 | 9.739% | 9.739% | 0.010 s | 19.342 MB | 26.754 MB | 1556.236 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 13349 |  | 1 | n/a% | n/a% | n/a s | 25.852 MB | 25.852 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 13381 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.134 MB | 25.609 MB | 1618.481 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 13406 |  | 1 | n/a% | n/a% | n/a s | 25.641 MB | 25.641 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| python3 | 13430 |  | 4 | 102.151% | 108.823% | 0.310 s | 25.051 MB | 34.316 MB | 49.563 MB | 57.438 MB | 0.000000 MB | 0.183594 MB |
| docker | 13433 |  | 1 | n/a% | n/a% | n/a s | 11.301 MB | 11.301 MB | 1451.949 MB | 1451.949 MB | n/a MB | n/a MB |
| docker | 13458 |  | 1 | n/a% | n/a% | n/a s | 25.648 MB | 25.648 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 13467 |  | 1 | n/a% | n/a% | n/a s | 25.680 MB | 25.680 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 13481 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.504 MB | 27.504 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 13521 | bake_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.025 MB | 12.594 MB | 314.889 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 13552 |  | 1 | n/a% | n/a% | n/a s | 27.414 MB | 27.414 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 13572 |  | 1 | n/a% | n/a% | n/a s | 11.574 MB | 11.574 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 13548 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 13654 |  | 1 | n/a% | n/a% | n/a s | 25.609 MB | 25.609 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 13692 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.941 MB | 25.941 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 13765 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.785 MB | 25.785 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 13804 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.614 MB | 12.559 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 13840 |  | 1 | n/a% | n/a% | n/a s | 27.156 MB | 27.156 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 13829 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 13867 |  | 1 | n/a% | n/a% | n/a s | 27.480 MB | 27.480 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| sh | 13887 | bake_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.516 MB | 0.516 MB | n/a MB | n/a MB |
| docker | 13933 |  | 1 | n/a% | n/a% | n/a s | 19.984 MB | 19.984 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 13941 |  | 1 | n/a% | n/a% | n/a s | 25.695 MB | 25.695 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 14014 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.730 MB | 25.730 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 14055 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 4.803 MB | 13.145 MB | 548.197 MB | 1642.480 MB | n/a MB | n/a MB |
| tail | 14080 | bake_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 14091 |  | 1 | n/a% | n/a% | n/a s | 25.703 MB | 25.703 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 14119 |  | 1 | n/a% | n/a% | n/a s | 27.250 MB | 27.250 MB | 1733.027 MB | 1733.027 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 14140 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.820 MB | 11.820 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 14162 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.879 MB | 25.879 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 14236 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.988 MB | 26.988 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 14275 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.723 MB | 12.992 MB | 411.411 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 14311 |  | 1 | n/a% | n/a% | n/a s | 26.969 MB | 26.969 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 14301 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 14337 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 14402 |  | 1 | n/a% | n/a% | n/a s | 23.789 MB | 23.789 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 14410 |  | 1 | n/a% | n/a% | n/a s | 27.086 MB | 27.086 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 14470 |  | 1 | n/a% | n/a% | n/a s | 25.285 MB | 25.285 MB | 1596.211 MB | 1596.211 MB | n/a MB | n/a MB |
| docker | 14496 |  | 1 | n/a% | n/a% | n/a s | 19.785 MB | 19.785 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 14510 |  | 47 | 0.000% | 0.000% | 0.000 s | 26.863 MB | 26.863 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 14526 |  | 1 | n/a% | n/a% | n/a s | 25.652 MB | 25.652 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 14553 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.934 MB | 26.934 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 14594 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.629 MB | 12.617 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 14655 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.816 MB | 11.816 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 14634 |  | 1 | n/a% | n/a% | n/a s | 26.676 MB | 26.676 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 14616 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 14700 |  | 1 | n/a% | n/a% | n/a s | 1.094 MB | 1.094 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 14739 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.926 MB | 26.836 MB | 1624.490 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 14806 |  | 1 | n/a% | n/a% | n/a s | 27.211 MB | 27.211 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 14853 | bake_0000 | 11 | 0.982% | 9.821% | 0.010 s | 1.692 MB | 12.281 MB | 143.707 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 14814 |  | 1 | n/a% | n/a% | n/a s | 26.621 MB | 26.621 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 14879 |  | 1 | n/a% | n/a% | n/a s | 23.730 MB | 23.730 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| tail | 14877 | bake_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 14916 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.020 MB | 27.020 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| bash | 14934 | bake_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.410 MB | 3.410 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 14944 | bake_0000 | 8 | 100.756% | 107.897% | 0.720 s | 33.553 MB | 42.762 MB | 40.627 MB | 52.285 MB | n/a MB | n/a MB |
| docker | 14954 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.848 MB | 25.848 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 15031 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.359 MB | 25.359 MB | 1624.209 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 15072 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.716 MB | 12.965 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 15095 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 15107 |  | 1 | n/a% | n/a% | n/a s | 26.699 MB | 26.699 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 15137 |  | 1 | n/a% | n/a% | n/a s | 27.484 MB | 27.484 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 15156 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.727 MB | 11.727 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 15199 |  | 1 | n/a% | n/a% | n/a s | 4.574 MB | 4.574 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 15207 |  | 1 | n/a% | n/a% | n/a s | 27.062 MB | 27.062 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 15263 |  | 1 | n/a% | n/a% | n/a s | 11.223 MB | 11.223 MB | 1451.949 MB | 1451.949 MB | n/a MB | n/a MB |
| docker | 15280 |  | 1 | n/a% | n/a% | n/a s | 8.668 MB | 8.668 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 15305 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.650 MB | 25.715 MB | 1660.204 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 15330 |  | 1 | n/a% | n/a% | n/a s | 27.012 MB | 27.012 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 15354 |  | 4 | 98.894% | 108.651% | 0.300 s | 25.327 MB | 34.363 MB | 49.612 MB | 57.465 MB | 0.000000 MB | 0.183594 MB |
| docker | 15357 |  | 1 | n/a% | n/a% | n/a s | 3.848 MB | 3.848 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 15383 |  | 1 | n/a% | n/a% | n/a s | 26.402 MB | 26.402 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 15406 |  | 2 | 9.778% | 9.778% | 0.010 s | 27.439 MB | 27.570 MB | 1696.775 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 15446 | bale_0000 | 5 | 2.456% | 9.823% | 0.010 s | 2.827 MB | 11.602 MB | 314.786 MB | 1569.711 MB | n/a MB | n/a MB |
| tail | 15472 | bale_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 15476 |  | 1 | n/a% | n/a% | n/a s | 19.543 MB | 19.543 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 15514 |  | 1 | n/a% | n/a% | n/a s | 27.152 MB | 27.152 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 15606 |  | 1 | n/a% | n/a% | n/a s | 22.914 MB | 22.914 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 15614 |  | 1 | n/a% | n/a% | n/a s | 25.996 MB | 25.996 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 15678 |  | 1 | n/a% | n/a% | n/a s | 3.156 MB | 3.156 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 15686 |  | 1 | n/a% | n/a% | n/a s | 26.156 MB | 26.156 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 15725 | bale_0000 | 4 | 3.266% | 9.798% | 0.010 s | 3.396 MB | 11.688 MB | 393.219 MB | 1569.711 MB | n/a MB | n/a MB |
| docker | 15751 |  | 1 | n/a% | n/a% | n/a s | 25.656 MB | 25.656 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| tail | 15747 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 15788 |  | 1 | n/a% | n/a% | n/a s | 27.344 MB | 27.344 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 15824 |  | 1 | n/a% | n/a% | n/a s | 27.117 MB | 27.117 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 15845 | bale_0000 | 1 | n/a% | n/a% | n/a s | 10.984 MB | 10.984 MB | 1641.707 MB | 1641.707 MB | n/a MB | n/a MB |
| docker | 15862 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.922 MB | 25.922 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 15959 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.612 MB | 26.793 MB | 1656.962 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 15975 |  | 1 | n/a% | n/a% | n/a s | 25.668 MB | 25.668 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 16001 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.641 MB | 25.641 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 16041 | bale_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.677 MB | 12.809 MB | 411.411 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 16081 |  | 1 | n/a% | n/a% | n/a s | 26.902 MB | 26.902 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 16103 | bale_0000 | 1 | n/a% | n/a% | n/a s | 11.855 MB | 11.855 MB | 1642.980 MB | 1642.980 MB | n/a MB | n/a MB |
| tail | 16071 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.691 MB | 1.691 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 16140 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 16190 |  | 2 | 0.000% | 0.000% | 0.000 s | 23.875 MB | 25.977 MB | 1624.207 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 16254 |  | 1 | n/a% | n/a% | n/a s | 16.488 MB | 16.488 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 16300 | bale_0000 | 38 | 0.794% | 29.378% | 0.030 s | 0.940 MB | 12.320 MB | 42.358 MB | 1570.598 MB | n/a MB | n/a MB |
| docker | 16262 |  | 1 | n/a% | n/a% | n/a s | 25.965 MB | 25.965 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 16321 | bale_0000 | 37 | 0.000% | 0.000% | 0.000 s | 1.730 MB | 1.730 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 16333 |  | 1 | n/a% | n/a% | n/a s | 0.129 MB | 0.129 MB | 30.570 MB | 30.570 MB | n/a MB | n/a MB |
| docker | 16361 |  | 35 | 0.000% | 0.000% | 0.000 s | 27.020 MB | 27.020 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| bash | 16379 | bale_0000 | 34 | 0.000% | 0.000% | 0.000 s | 3.395 MB | 3.395 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 16388 | bale_0000 | 34 | 99.578% | 108.015% | 3.350 s | 39.688 MB | 42.336 MB | 48.634 MB | 52.043 MB | n/a MB | n/a MB |
| docker | 16399 |  | 2 | 0.000% | 0.000% | 0.000 s | 15.668 MB | 25.922 MB | 846.486 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 16461 |  | 1 | n/a% | n/a% | n/a s | 23.715 MB | 23.715 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 16479 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.707 MB | 26.707 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 16518 | bale_0000 | 4 | 9.721% | 29.162% | 0.030 s | 3.148 MB | 10.695 MB | 393.090 MB | 1569.195 MB | n/a MB | n/a MB |
| tail | 16543 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 16582 |  | 1 | n/a% | n/a% | n/a s | 10.574 MB | 10.574 MB | 1387.949 MB | 1387.949 MB | n/a MB | n/a MB |
| docker | 16617 |  | 1 | n/a% | n/a% | n/a s | 27.398 MB | 27.398 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 16654 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.762 MB | 25.762 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 16730 |  | 1 | n/a% | n/a% | n/a s | 20.047 MB | 20.047 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 16756 |  | 1 | n/a% | n/a% | n/a s | 25.953 MB | 25.953 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 16764 |  | 39 | 0.000% | 0.000% | 0.000 s | 26.934 MB | 26.934 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python3 | 16812 |  | 24 | 99.743% | 108.816% | 2.320 s | 32.948 MB | 34.285 MB | 55.686 MB | 57.461 MB | 0.000000 MB | 0.167969 MB |
| docker | 16833 |  | 1 | n/a% | n/a% | n/a s | 26.953 MB | 26.953 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 16865 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.327 MB | 27.430 MB | 1708.776 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 16904 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.639 MB | 12.656 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 16929 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 16961 |  | 1 | n/a% | n/a% | n/a s | 26.398 MB | 26.398 MB | 1588.270 MB | 1588.270 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 17017 | band_0000 | 1 | n/a% | n/a% | n/a s | 7.617 MB | 7.617 MB | 1432.941 MB | 1432.941 MB | n/a MB | n/a MB |
| docker | 16998 |  | 1 | n/a% | n/a% | n/a s | 27.160 MB | 27.160 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 17031 |  | 1 | n/a% | n/a% | n/a s | 27.062 MB | 27.062 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 17051 | band_0000 | 1 | n/a% | n/a% | n/a s | 11.730 MB | 11.730 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 17068 |  | 1 | n/a% | n/a% | n/a s | 26.824 MB | 26.824 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 17123 |  | 1 | n/a% | n/a% | n/a s | 1.082 MB | 1.082 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 17139 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.867 MB | 26.867 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| tail | 17202 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 17178 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 17242 |  | 1 | n/a% | n/a% | n/a s | 18.258 MB | 18.258 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 17276 |  | 1 | n/a% | n/a% | n/a s | 27.270 MB | 27.270 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 17312 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.008 MB | 26.008 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 17408 |  | 38 | 0.000% | 0.000% | 0.000 s | 25.609 MB | 25.609 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 17451 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.641 MB | 26.641 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 17489 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.629 MB | 12.617 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 17516 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 17528 |  | 1 | n/a% | n/a% | n/a s | 21.445 MB | 21.445 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 17554 |  | 1 | n/a% | n/a% | n/a s | 27.383 MB | 27.383 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 17573 | band_0000 | 1 | n/a% | n/a% | n/a s | 11.691 MB | 11.691 MB | 1570.848 MB | 1570.848 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 17609 | band_0000 | 1 | n/a% | n/a% | n/a s | 12.496 MB | 12.496 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 17589 |  | 1 | n/a% | n/a% | n/a s | 27.098 MB | 27.098 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 17628 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.781 MB | 26.781 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 17695 |  | 1 | n/a% | n/a% | n/a s | 16.066 MB | 16.066 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 17703 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.590 MB | 25.590 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 17742 | band_0000 | 12 | 2.657% | 29.222% | 0.030 s | 1.521 MB | 11.285 MB | 131.775 MB | 1569.695 MB | n/a MB | n/a MB |
| tail | 17764 | band_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 17803 |  | 9 | 2.445% | 19.560% | 0.020 s | 25.050 MB | 27.285 MB | 1479.881 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| bash | 17823 | band_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.320 MB | 3.320 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 17833 | band_0000 | 8 | 100.674% | 107.901% | 0.720 s | 30.652 MB | 41.266 MB | 37.813 MB | 51.324 MB | n/a MB | n/a MB |
| docker | 17835 |  | 1 | n/a% | n/a% | n/a s | 7.391 MB | 7.391 MB | 32.867 MB | 32.867 MB | n/a MB | n/a MB |
| docker | 17843 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.973 MB | 26.973 MB | 1660.523 MB | 1660.523 MB | 0.000000 MB | 0.000000 MB |
| docker | 17917 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.793 MB | 25.793 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 17956 | band_0000 | 4 | 3.267% | 9.802% | 0.010 s | 3.659 MB | 12.738 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 17978 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 17993 |  | 1 | n/a% | n/a% | n/a s | 27.465 MB | 27.465 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 18013 | band_0000 | 1 | n/a% | n/a% | n/a s | 11.695 MB | 11.695 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 18093 |  | 2 | 0.000% | 0.000% | 0.000 s | 24.473 MB | 25.992 MB | 1624.207 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 18161 |  | 1 | n/a% | n/a% | n/a s | 24.090 MB | 24.090 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 18193 |  | 40 | 0.253% | 9.868% | 0.010 s | 26.282 MB | 26.793 MB | 1620.073 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 18226 |  | 1 | n/a% | n/a% | n/a s | 26.434 MB | 26.434 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 18241 |  | 4 | 98.788% | 108.701% | 0.300 s | 27.355 MB | 34.484 MB | 51.422 MB | 57.457 MB | 0.000000 MB | 0.183594 MB |
| docker | 18259 |  | 1 | n/a% | n/a% | n/a s | 26.996 MB | 26.996 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |

## GPU metrics

_No GPU samples were collected._

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| alex_0000 | 57.287% | 100.756% | 1.286 s | 9.330 MB | 35.195 MB | 0.007812 MB | 0.003906 MB | 0.001118 MB | 0.000200 MB |
| andy_0000 | 59.455% | 100.131% | 1.275 s | 9.143 MB | 36.215 MB | 0.000000 MB | 0.003906 MB | 0.000923 MB | 0.000080 MB |
| arch_0000 | 58.647% | 100.027% | 1.258 s | 8.832 MB | 35.309 MB | 0.000000 MB | 0.003906 MB | 0.000654 MB | 0.000120 MB |
| bake_0000 | 51.367% | 100.972% | 1.368 s | 8.243 MB | 36.344 MB | 0.000000 MB | 0.003906 MB | 0.001745 MB | 0.000160 MB |
| bale_0000 | 80.916% | 100.269% | 3.964 s | 22.175 MB | 36.090 MB | 0.000000 MB | 0.003906 MB | 0.001274 MB | 0.000200 MB |
| band_0000 | 59.836% | 100.477% | 1.284 s | 9.215 MB | 34.688 MB | 0.000000 MB | 0.003906 MB | 0.000845 MB | 0.000120 MB |

## Incomplete spans

_No spans were still open when profiling stopped._

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agsync:join | 6/6 | 0 | 0 | 274.094 | 0.001 | 274.093 | 45682.354 | 45247.600 | 55933.067 |
| sync:result_wait | 12/12 | 0 | 0 | 270.220 | 0.002 | 270.217 | 22518.303 | 21667.855 | 32828.398 |
| turn | 39/39 | 0 | 0 | 218.847 | 1.112 | 217.704 | 5611.456 | 3840.852 | 15821.091 |
| llm:attempt | 39/39 | 0 | 0 | 188.829 | 0.884 | 187.931 | 4841.775 | 2790.181 | 15799.754 |
| run:diagnose_bug | 6/6 | 0 | 0 | 151.820 | 0.575 | 151.227 | 25303.262 | 22509.638 | 33247.566 |
| capstone:prepare:bitcount | 1/1 | 0 | 0 | 120.132 | 0.030 | 120.102 | 120132.039 | 120132.039 | 120132.039 |
| run:repair_bug | 6/6 | 0 | 0 | 118.408 | 0.610 | 117.781 | 19734.668 | 17408.596 | 26121.778 |
| llm:diagnose_bug | 14/14 | 0 | 0 | 114.830 | 0.435 | 114.387 | 8202.143 | 3804.351 | 23128.806 |
| llm:repair_bug | 25/25 | 0 | 0 | 74.010 | 0.460 | 73.543 | 2960.414 | 2640.655 | 5504.083 |
| teardown:commit | 12/12 | 0 | 0 | 51.144 | 0.030 | 51.114 | 4262.030 | 4114.547 | 5225.507 |
| sandbox:commit | 12/12 | 0 | 0 | 50.891 | 0.023 | 50.867 | 4240.891 | 4094.738 | 5202.797 |
| capstone:plan:mergesort | 1/1 | 0 | 0 | 33.596 | 0.001 | 33.596 | 33596.416 | 33596.416 | 33596.416 |
| capstone:plan:bitcount | 1/1 | 0 | 0 | 32.202 | 0.001 | 32.201 | 32201.615 | 32201.615 | 32201.615 |
| capstone:build:levenshtein | 1/1 | 0 | 0 | 26.855 | 0.001 | 26.855 | 26855.483 | 26855.483 | 26855.483 |
| capstone:build:mergesort | 1/1 | 0 | 0 | 23.921 | 0.000 | 23.920 | 23920.899 | 23920.899 | 23920.899 |
| capstone:plan:gcd | 1/1 | 0 | 0 | 22.837 | 0.001 | 22.836 | 22837.228 | 22837.228 | 22837.228 |
| capstone:plan:is_valid_parenthesization | 1/1 | 0 | 0 | 22.182 | 0.001 | 22.182 | 22182.410 | 22182.410 | 22182.410 |
| capstone:plan:levenshtein | 1/1 | 0 | 0 | 21.155 | 0.001 | 21.155 | 21155.401 | 21155.401 | 21155.401 |
| capstone:plan:flatten | 1/1 | 0 | 0 | 19.848 | 0.001 | 19.847 | 19848.286 | 19848.286 | 19848.286 |
| tool_dispatch:repair_bug | 25/25 | 0 | 0 | 19.487 | 0.106 | 19.371 | 779.483 | 667.430 | 1454.851 |
| capstone:build:bitcount | 1/1 | 0 | 0 | 17.724 | 0.001 | 17.723 | 17723.507 | 17723.507 | 17723.507 |
| capstone:build:gcd | 1/1 | 0 | 0 | 17.094 | 0.000 | 17.093 | 17093.521 | 17093.521 | 17093.521 |
| capstone:build:flatten | 1/1 | 0 | 0 | 16.511 | 0.001 | 16.509 | 16510.522 | 16510.522 | 16510.522 |
| capstone:build:is_valid_parenthesization | 1/1 | 0 | 0 | 16.305 | 0.001 | 16.304 | 16304.531 | 16304.531 | 16304.531 |
| tool_dispatch:diagnose_bug | 14/14 | 0 | 0 | 10.496 | 0.087 | 10.402 | 749.710 | 636.476 | 1568.243 |
| sandbox:exec | 7/7 | 0 | 0 | 10.175 | 0.016 | 10.158 | 1453.633 | 1191.217 | 3071.317 |
| sandbox:start | 32/32 | 0 | 0 | 9.827 | 0.052 | 9.769 | 307.100 | 277.855 | 427.868 |
| tool:bash | 6/6 | 0 | 0 | 9.810 | 0.017 | 9.792 | 1634.975 | 1199.639 | 3203.457 |
| tool:read | 19/19 | 0 | 0 | 9.585 | 0.080 | 9.499 | 504.460 | 450.594 | 636.198 |
| sandbox:stop | 63/63 | 0 | 0 | 7.678 | 0.050 | 7.623 | 121.874 | 193.076 | 232.590 |
| capstone:prepare:mergesort | 1/1 | 0 | 0 | 7.070 | 0.040 | 7.030 | 7070.031 | 7070.031 | 7070.031 |
| sandbox:read_file | 25/25 | 0 | 0 | 3.877 | 0.035 | 3.837 | 155.076 | 88.062 | 372.934 |
| tool:edit | 6/6 | 0 | 0 | 2.768 | 0.024 | 2.738 | 461.251 | 459.192 | 469.381 |
| capstone:prepare:levenshtein | 1/1 | 0 | 0 | 2.529 | 0.031 | 2.499 | 2529.260 | 2529.260 | 2529.260 |
| capstone:verify:levenshtein | 1/1 | 0 | 0 | 2.490 | 0.001 | 2.489 | 2490.105 | 2490.105 | 2490.105 |
| agent:create | 6/6 | 0 | 0 | 1.908 | 0.485 | 1.423 | 317.950 | 137.214 | 951.200 |
| capstone:prepare:flatten | 1/1 | 0 | 0 | 0.815 | 0.075 | 0.740 | 814.805 | 814.805 | 814.805 |
| sandbox:destroy | 6/6 | 0 | 0 | 0.747 | 0.010 | 0.735 | 124.418 | 125.347 | 127.306 |
| sandbox:write_file | 6/6 | 0 | 0 | 0.547 | 0.006 | 0.541 | 91.193 | 91.128 | 92.862 |
| capstone:verify:flatten | 1/1 | 0 | 0 | 0.456 | 0.001 | 0.455 | 456.002 | 456.002 | 456.002 |
| capstone:prepare:gcd | 1/1 | 0 | 0 | 0.452 | 0.031 | 0.421 | 452.231 | 452.231 | 452.231 |
| capstone:prepare:is_valid_parenthesization | 1/1 | 0 | 0 | 0.417 | 0.031 | 0.385 | 416.914 | 416.914 | 416.914 |
| capstone:verify:mergesort | 1/1 | 0 | 0 | 0.392 | 0.001 | 0.390 | 391.872 | 391.872 | 391.872 |
| capstone:verify:bitcount | 1/1 | 0 | 0 | 0.385 | 0.001 | 0.384 | 384.807 | 384.807 | 384.807 |
| capstone:verify:is_valid_parenthesization | 1/1 | 0 | 0 | 0.384 | 0.002 | 0.382 | 383.894 | 383.894 | 383.894 |
| capstone:verify:gcd | 1/1 | 0 | 0 | 0.379 | 0.001 | 0.377 | 379.191 | 379.191 | 379.191 |
| tool:glob | 1/1 | 0 | 0 | 0.370 | 0.003 | 0.366 | 369.627 | 369.627 | 369.627 |
| sandbox:provision | 6/6 | 0 | 0 | 0.175 | 0.006 | 0.169 | 29.192 | 0.591 | 129.308 |
| sandbox:create | 6/6 | 0 | 0 | 0.174 | 0.005 | 0.169 | 29.022 | 0.405 | 129.144 |
| run:detect | 1/1 | 0 | 0 | 0.121 | 0.001 | 0.120 | 120.753 | 120.753 | 120.753 |
| sync:container | 427/427 | 0 | 0 | 0.048 | 0.048 | 0.001 | 0.113 | 0.130 | 0.201 |
| prune | 12/12 | 0 | 0 | 0.005 | 0.002 | 0.002 | 0.377 | 0.354 | 0.642 |
| tool:return_summary | 7/7 | 1 | 0 | 0.003 | 0.003 | 0.000 | 0.365 | 0.384 | 0.400 |
| llm:sync | 39/39 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.057 | 0.040 | 0.164 |
| tool:return_plan | 6/6 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.338 | 0.327 | 0.411 |
| tool:return_status | 6/6 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.311 | 0.314 | 0.325 |
| input:prepare | 12/12 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.118 | 0.105 | 0.206 |
| resolve | 12/12 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.098 | 0.081 | 0.174 |
| agprof:clock_sync | 1/1 | 0 | 0 | 0.001 | 0.001 | 0.000 | 1.007 | 1.007 | 1.007 |
| proc_wait | 12/12 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.071 | 0.067 | 0.092 |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 2693 | 28.044 | 0.000 | 155.248 | 4.873 | 76.677200 CPU seconds | n/a |
| docker (PID 10006) rss_mb | MB | 1 | 16.582 | 16.582 | 16.582 | 16.582 | n/a | n/a |
| docker (PID 10006) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 10014) rss_mb | MB | 1 | 26.855 | 26.855 | 26.855 | 26.855 | n/a | n/a |
| docker (PID 10014) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 10053) CPU | percent | 11 | 2.648 | 0.000 | 29.123 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 10053) rss_mb | MB | 12 | 1.592 | 0.633 | 12.148 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 10053) vms_mb | MB | 12 | 131.828 | 1.055 | 1570.340 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 10077) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 10077) rss_mb | MB | 11 | 1.691 | 1.691 | 1.691 | 1.691 | n/a | n/a |
| tail [alex_0000] (PID 10077) vms_mb | MB | 11 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 10079) rss_mb | MB | 1 | 16.172 | 16.172 | 16.172 | 16.172 | n/a | n/a |
| docker (PID 10079) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 10116) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 10116) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 10116) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 10116) rss_mb | MB | 9 | 27.312 | 27.312 | 27.312 | 27.312 | n/a | n/a |
| docker (PID 10116) vms_mb | MB | 9 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| bash [alex_0000] (PID 10136) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [alex_0000] (PID 10136) rss_mb | MB | 8 | 3.305 | 3.305 | 3.305 | 3.305 | n/a | n/a |
| bash [alex_0000] (PID 10136) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [alex_0000] (PID 10145) CPU | percent | 7 | 99.436 | 88.352 | 108.016 | 107.949 | 0.710000 CPU seconds | n/a |
| python [alex_0000] (PID 10145) rss_mb | MB | 8 | 31.607 | 13.117 | 42.070 | 42.070 | n/a | n/a |
| python [alex_0000] (PID 10145) vms_mb | MB | 8 | 38.569 | 16.613 | 51.238 | 51.238 | n/a | n/a |
| docker (PID 10155) CPU | percent | 1 | 9.812 | 9.812 | 9.812 | 9.812 | 0.010000 CPU seconds | n/a |
| docker (PID 10155) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 10155) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 10155) rss_mb | MB | 2 | 17.352 | 8.727 | 25.977 | 25.977 | n/a | n/a |
| docker (PID 10155) vms_mb | MB | 2 | 1443.822 | 1227.434 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 10229) CPU | percent | 1 | 9.909 | 9.909 | 9.909 | 9.909 | 0.010000 CPU seconds | n/a |
| docker (PID 10229) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 10229) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 10229) rss_mb | MB | 2 | 26.297 | 26.172 | 26.422 | 26.422 | n/a | n/a |
| docker (PID 10229) vms_mb | MB | 2 | 1660.648 | 1660.523 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 10267) CPU | percent | 3 | 3.285 | 0.000 | 9.854 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 10267) rss_mb | MB | 4 | 3.637 | 0.633 | 12.648 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 10267) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 10292) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 10292) rss_mb | MB | 3 | 1.539 | 1.539 | 1.539 | 1.539 | n/a | n/a |
| tail [alex_0000] (PID 10292) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 10302) rss_mb | MB | 1 | 15.332 | 15.332 | 15.332 | 15.332 | n/a | n/a |
| docker (PID 10302) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 10329) rss_mb | MB | 1 | 27.309 | 27.309 | 27.309 | 27.309 | n/a | n/a |
| docker (PID 10329) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 10349) rss_mb | MB | 1 | 10.961 | 10.961 | 10.961 | 10.961 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 10349) vms_mb | MB | 1 | 1569.711 | 1569.711 | 1569.711 | 1569.711 | n/a | n/a |
| docker (PID 10364) rss_mb | MB | 1 | 27.145 | 27.145 | 27.145 | 27.145 | n/a | n/a |
| docker (PID 10364) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 10383) rss_mb | MB | 1 | 11.871 | 11.871 | 11.871 | 11.871 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 10383) vms_mb | MB | 1 | 1570.977 | 1570.977 | 1570.977 | 1570.977 | n/a | n/a |
| docker (PID 10400) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 10400) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 10400) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 10400) rss_mb | MB | 2 | 25.891 | 25.891 | 25.891 | 25.891 | n/a | n/a |
| docker (PID 10400) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 10488) rss_mb | MB | 1 | 25.715 | 25.715 | 25.715 | 25.715 | n/a | n/a |
| docker (PID 10488) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 10496) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 10496) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 10496) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 10496) rss_mb | MB | 39 | 25.652 | 25.652 | 25.652 | 25.652 | n/a | n/a |
| docker (PID 10496) vms_mb | MB | 39 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| python3 (PID 10544) CPU | percent | 3 | 98.855 | 98.702 | 99.005 | 99.005 | 0.300000 CPU seconds | n/a |
| python3 (PID 10544) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 10544) io write MB/s | MB/s | 3 | 0.554 | 0.000 | 1.663 | 1.663 | 0.167969 MB | n/a |
| python3 (PID 10544) rss_mb | MB | 4 | 25.198 | 11.844 | 34.336 | 34.336 | n/a | n/a |
| python3 (PID 10544) vms_mb | MB | 4 | 49.604 | 38.035 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 10547) rss_mb | MB | 1 | 18.223 | 18.223 | 18.223 | 18.223 | n/a | n/a |
| docker (PID 10547) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 10573) rss_mb | MB | 1 | 25.746 | 25.746 | 25.746 | 25.746 | n/a | n/a |
| docker (PID 10573) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 10597) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 10597) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 10597) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 10597) rss_mb | MB | 3 | 27.229 | 26.938 | 27.375 | 27.375 | n/a | n/a |
| docker (PID 10597) vms_mb | MB | 3 | 1708.776 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [andy_0000] (PID 10638) CPU | percent | 4 | 7.377 | 0.000 | 29.507 | 0.000 | 0.030000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 10638) rss_mb | MB | 5 | 2.712 | 0.633 | 11.031 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 10638) vms_mb | MB | 5 | 329.184 | 1.055 | 1641.699 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 10667) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 10667) rss_mb | MB | 4 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [andy_0000] (PID 10667) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 10704) rss_mb | MB | 1 | 20.547 | 20.547 | 20.547 | 20.547 | n/a | n/a |
| docker (PID 10704) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 10734) rss_mb | MB | 1 | 27.234 | 27.234 | 27.234 | 27.234 | n/a | n/a |
| docker (PID 10734) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 10754) rss_mb | MB | 1 | 11.527 | 11.527 | 11.527 | 11.527 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 10754) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 10769) rss_mb | MB | 1 | 27.086 | 27.086 | 27.086 | 27.086 | n/a | n/a |
| docker (PID 10769) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| sh [andy_0000] (PID 10788) rss_mb | MB | 1 | 1.676 | 1.676 | 1.676 | 1.676 | n/a | n/a |
| sh [andy_0000] (PID 10788) vms_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| docker (PID 10806) rss_mb | MB | 1 | 26.902 | 26.902 | 26.902 | 26.902 | n/a | n/a |
| docker (PID 10806) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 10863) rss_mb | MB | 1 | 8.164 | 8.164 | 8.164 | 8.164 | n/a | n/a |
| docker (PID 10863) vms_mb | MB | 1 | 32.867 | 32.867 | 32.867 | 32.867 | n/a | n/a |
| docker (PID 10880) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 10880) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 10880) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 10880) rss_mb | MB | 2 | 26.965 | 26.965 | 26.965 | 26.965 | n/a | n/a |
| docker (PID 10880) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [andy_0000] (PID 10920) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 10920) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 10920) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 10944) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 10944) rss_mb | MB | 4 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [andy_0000] (PID 10944) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 10982) rss_mb | MB | 1 | 7.215 | 7.215 | 7.215 | 7.215 | n/a | n/a |
| docker (PID 10982) vms_mb | MB | 1 | 32.867 | 32.867 | 32.867 | 32.867 | n/a | n/a |
| docker (PID 11016) rss_mb | MB | 1 | 23.934 | 23.934 | 23.934 | 23.934 | n/a | n/a |
| docker (PID 11016) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 11053) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 11053) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 11053) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 11053) rss_mb | MB | 2 | 26.023 | 26.023 | 26.023 | 26.023 | n/a | n/a |
| docker (PID 11053) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 11128) rss_mb | MB | 1 | 4.004 | 4.004 | 4.004 | 4.004 | n/a | n/a |
| docker (PID 11128) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 11150) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 11150) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 11150) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 11150) rss_mb | MB | 38 | 26.332 | 26.332 | 26.332 | 26.332 | n/a | n/a |
| docker (PID 11150) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 11194) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 11194) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 11194) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 11194) rss_mb | MB | 2 | 26.746 | 26.746 | 26.746 | 26.746 | n/a | n/a |
| docker (PID 11194) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 11233) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 11233) rss_mb | MB | 4 | 3.642 | 0.633 | 12.668 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 11233) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 11257) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 11257) rss_mb | MB | 3 | 1.695 | 1.695 | 1.695 | 1.695 | n/a | n/a |
| tail [andy_0000] (PID 11257) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 11272) rss_mb | MB | 1 | 27.199 | 27.199 | 27.199 | 27.199 | n/a | n/a |
| docker (PID 11272) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 11291) rss_mb | MB | 1 | 4.496 | 4.496 | 4.496 | 4.496 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 11291) vms_mb | MB | 1 | 1432.941 | 1432.941 | 1432.941 | 1432.941 | n/a | n/a |
| docker (PID 11364) rss_mb | MB | 1 | 17.070 | 17.070 | 17.070 | 17.070 | n/a | n/a |
| docker (PID 11364) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 11372) rss_mb | MB | 1 | 25.836 | 25.836 | 25.836 | 25.836 | n/a | n/a |
| docker (PID 11372) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 11430) rss_mb | MB | 1 | 0.934 | 0.934 | 0.934 | 0.934 | n/a | n/a |
| docker (PID 11430) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 11447) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 11447) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 11447) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 11447) rss_mb | MB | 2 | 26.727 | 26.727 | 26.727 | 26.727 | n/a | n/a |
| docker (PID 11447) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 11488) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 11488) rss_mb | MB | 11 | 1.739 | 0.633 | 12.805 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 11488) vms_mb | MB | 11 | 143.707 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 11513) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 11513) rss_mb | MB | 10 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [andy_0000] (PID 11513) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 11525) rss_mb | MB | 1 | 26.855 | 26.855 | 26.855 | 26.855 | n/a | n/a |
| docker (PID 11525) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 11546) rss_mb | MB | 1 | 11.355 | 11.355 | 11.355 | 11.355 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 11546) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 11553) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 11553) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 11553) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 11553) rss_mb | MB | 8 | 27.383 | 27.383 | 27.383 | 27.383 | n/a | n/a |
| docker (PID 11553) vms_mb | MB | 8 | 1733.027 | 1733.027 | 1733.027 | 1733.027 | n/a | n/a |
| bash [andy_0000] (PID 11574) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [andy_0000] (PID 11574) rss_mb | MB | 8 | 3.379 | 3.379 | 3.379 | 3.379 | n/a | n/a |
| bash [andy_0000] (PID 11574) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [andy_0000] (PID 11583) CPU | percent | 7 | 100.770 | 97.945 | 107.777 | 98.005 | 0.720000 CPU seconds | n/a |
| python [andy_0000] (PID 11583) rss_mb | MB | 8 | 30.569 | 9.445 | 42.672 | 42.672 | n/a | n/a |
| python [andy_0000] (PID 11583) vms_mb | MB | 8 | 37.748 | 13.305 | 52.238 | 52.238 | n/a | n/a |
| docker (PID 11585) rss_mb | MB | 1 | 24.566 | 24.566 | 24.566 | 24.566 | n/a | n/a |
| docker (PID 11585) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 11593) rss_mb | MB | 1 | 26.309 | 26.309 | 26.309 | 26.309 | n/a | n/a |
| docker (PID 11593) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 11648) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 11648) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 11668) rss_mb | MB | 1 | 26.918 | 26.918 | 26.918 | 26.918 | n/a | n/a |
| docker (PID 11668) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 11709) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 11709) rss_mb | MB | 4 | 3.590 | 0.633 | 12.461 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 11709) vms_mb | MB | 4 | 393.473 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 11733) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 11733) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [andy_0000] (PID 11733) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 11770) rss_mb | MB | 1 | 26.996 | 26.996 | 26.996 | 26.996 | n/a | n/a |
| docker (PID 11770) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 11790) rss_mb | MB | 1 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 11790) vms_mb | MB | 1 | 1208.676 | 1208.676 | 1208.676 | 1208.676 | n/a | n/a |
| docker (PID 11805) rss_mb | MB | 1 | 26.984 | 26.984 | 26.984 | 26.984 | n/a | n/a |
| docker (PID 11805) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 11825) rss_mb | MB | 1 | 11.352 | 11.352 | 11.352 | 11.352 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 11825) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 11842) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 11842) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 11842) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 11842) rss_mb | MB | 2 | 26.582 | 26.582 | 26.582 | 26.582 | n/a | n/a |
| docker (PID 11842) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 11939) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 11939) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 11939) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 11939) rss_mb | MB | 39 | 26.797 | 26.797 | 26.797 | 26.797 | n/a | n/a |
| docker (PID 11939) vms_mb | MB | 39 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 11971) rss_mb | MB | 1 | 26.816 | 26.816 | 26.816 | 26.816 | n/a | n/a |
| docker (PID 11971) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 11987) CPU | percent | 3 | 102.145 | 98.893 | 108.603 | 98.893 | 0.310000 CPU seconds | n/a |
| python3 (PID 11987) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 11987) io write MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 11987) rss_mb | MB | 4 | 26.089 | 15.727 | 33.406 | 33.406 | n/a | n/a |
| python3 (PID 11987) vms_mb | MB | 4 | 49.882 | 41.043 | 56.375 | 56.375 | n/a | n/a |
| docker (PID 12007) rss_mb | MB | 1 | 23.301 | 23.301 | 23.301 | 23.301 | n/a | n/a |
| docker (PID 12007) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 12038) CPU | percent | 3 | 6.159 | 0.000 | 18.478 | 0.000 | 0.020000 CPU seconds | n/a |
| docker (PID 12038) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 12038) io write MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 12038) rss_mb | MB | 4 | 27.107 | 26.941 | 27.211 | 27.211 | n/a | n/a |
| docker (PID 12038) vms_mb | MB | 4 | 1714.776 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [arch_0000] (PID 12079) CPU | percent | 5 | 7.829 | 0.000 | 39.146 | 0.000 | 0.040000 CPU seconds | n/a |
| docker-init [arch_0000] (PID 12079) rss_mb | MB | 6 | 3.681 | 0.633 | 12.934 | 0.633 | n/a | n/a |
| docker-init [arch_0000] (PID 12079) vms_mb | MB | 6 | 502.648 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 12107) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 12107) rss_mb | MB | 4 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [arch_0000] (PID 12107) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 12110) rss_mb | MB | 1 | 26.719 | 26.719 | 26.719 | 26.719 | n/a | n/a |
| docker (PID 12110) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] (PID 12129) rss_mb | MB | 1 | 3.703 | 3.703 | 3.703 | 3.703 | n/a | n/a |
| runc:[2:INIT] (PID 12129) vms_mb | MB | 1 | 1208.676 | 1208.676 | 1208.676 | 1208.676 | n/a | n/a |
| docker (PID 12144) rss_mb | MB | 1 | 27.258 | 27.258 | 27.258 | 27.258 | n/a | n/a |
| docker (PID 12144) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[0:PARENT] [arch_0000] (PID 12161) rss_mb | MB | 1 | 1.996 | 1.996 | 1.996 | 1.996 | n/a | n/a |
| runc:[0:PARENT] [arch_0000] (PID 12161) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[1:CHILD] [arch_0000] (PID 12162) rss_mb | MB | 1 | 1.309 | 1.309 | 1.309 | 1.309 | n/a | n/a |
| runc:[1:CHILD] [arch_0000] (PID 12162) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 12163) rss_mb | MB | 1 | 0.695 | 0.695 | 0.695 | 0.695 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 12163) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| docker (PID 12171) rss_mb | MB | 1 | 27.422 | 27.422 | 27.422 | 27.422 | n/a | n/a |
| docker (PID 12171) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 12234) rss_mb | MB | 1 | 19.969 | 19.969 | 19.969 | 19.969 | n/a | n/a |
| docker (PID 12234) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 12242) rss_mb | MB | 1 | 25.941 | 25.941 | 25.941 | 25.941 | n/a | n/a |
| docker (PID 12242) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 12315) rss_mb | MB | 1 | 9.293 | 9.293 | 9.293 | 9.293 | n/a | n/a |
| docker (PID 12315) vms_mb | MB | 1 | 1371.941 | 1371.941 | 1371.941 | 1371.941 | n/a | n/a |
| docker (PID 12323) rss_mb | MB | 1 | 25.590 | 25.590 | 25.590 | 25.590 | n/a | n/a |
| docker (PID 12323) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 12363) CPU | percent | 3 | 6.536 | 0.000 | 19.609 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 12363) rss_mb | MB | 4 | 3.326 | 0.633 | 11.406 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 12363) vms_mb | MB | 4 | 393.187 | 1.055 | 1569.582 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 12386) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 12386) rss_mb | MB | 3 | 1.691 | 1.691 | 1.691 | 1.691 | n/a | n/a |
| tail [arch_0000] (PID 12386) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 12388) rss_mb | MB | 1 | 8.605 | 8.605 | 8.605 | 8.605 | n/a | n/a |
| docker (PID 12388) vms_mb | MB | 1 | 1227.309 | 1227.309 | 1227.309 | 1227.309 | n/a | n/a |
| docker (PID 12423) rss_mb | MB | 1 | 25.645 | 25.645 | 25.645 | 25.645 | n/a | n/a |
| docker (PID 12423) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 12460) rss_mb | MB | 1 | 26.996 | 26.996 | 26.996 | 26.996 | n/a | n/a |
| docker (PID 12460) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| 6 [arch_0000] (PID 12477) rss_mb | MB | 1 | 0.711 | 0.711 | 0.711 | 0.711 | n/a | n/a |
| 6 [arch_0000] (PID 12477) vms_mb | MB | 1 | 14.004 | 14.004 | 14.004 | 14.004 | n/a | n/a |
| docker (PID 12497) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 12497) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 12497) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 12497) rss_mb | MB | 2 | 26.184 | 26.184 | 26.184 | 26.184 | n/a | n/a |
| docker (PID 12497) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 12571) rss_mb | MB | 1 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| docker (PID 12571) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 12593) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 12593) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 12593) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 12593) rss_mb | MB | 38 | 26.344 | 26.344 | 26.344 | 26.344 | n/a | n/a |
| docker (PID 12593) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 12637) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 12637) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 12637) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 12637) rss_mb | MB | 2 | 25.652 | 25.652 | 25.652 | 25.652 | n/a | n/a |
| docker (PID 12637) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 12675) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 12675) rss_mb | MB | 4 | 3.707 | 0.633 | 12.930 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 12675) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 12700) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 12700) rss_mb | MB | 3 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [arch_0000] (PID 12700) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 12713) rss_mb | MB | 1 | 27.266 | 27.266 | 27.266 | 27.266 | n/a | n/a |
| docker (PID 12713) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 12733) rss_mb | MB | 1 | 11.570 | 11.570 | 11.570 | 11.570 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 12733) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 12768) rss_mb | MB | 1 | 25.801 | 25.801 | 25.801 | 25.801 | n/a | n/a |
| docker (PID 12768) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 12813) CPU | percent | 1 | 9.797 | 9.797 | 9.797 | 9.797 | 0.010000 CPU seconds | n/a |
| docker (PID 12813) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 12813) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 12813) rss_mb | MB | 2 | 17.816 | 8.727 | 26.906 | 26.906 | n/a | n/a |
| docker (PID 12813) vms_mb | MB | 2 | 1480.105 | 1227.434 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 12891) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 12891) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 12891) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 12891) rss_mb | MB | 2 | 25.336 | 25.336 | 25.336 | 25.336 | n/a | n/a |
| docker (PID 12891) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 12930) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 12930) rss_mb | MB | 11 | 1.746 | 0.633 | 12.883 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 12930) vms_mb | MB | 11 | 143.729 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 12954) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 12954) rss_mb | MB | 10 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [arch_0000] (PID 12954) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 12965) rss_mb | MB | 1 | 27.363 | 27.363 | 27.363 | 27.363 | n/a | n/a |
| docker (PID 12965) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[0:PARENT] [arch_0000] (PID 12982) rss_mb | MB | 1 | 1.965 | 1.965 | 1.965 | 1.965 | n/a | n/a |
| runc:[0:PARENT] [arch_0000] (PID 12982) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[0:PARENT] [arch_0000] (PID 12984) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[0:PARENT] [arch_0000] (PID 12984) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| docker (PID 12994) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 12994) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 12994) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 12994) rss_mb | MB | 8 | 27.242 | 27.242 | 27.242 | 27.242 | n/a | n/a |
| docker (PID 12994) vms_mb | MB | 8 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [arch_0000] (PID 13016) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [arch_0000] (PID 13016) rss_mb | MB | 8 | 3.418 | 3.418 | 3.418 | 3.418 | n/a | n/a |
| bash [arch_0000] (PID 13016) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [arch_0000] (PID 13026) CPU | percent | 7 | 98.019 | 88.211 | 107.883 | 98.023 | 0.700000 CPU seconds | n/a |
| python [arch_0000] (PID 13026) rss_mb | MB | 8 | 29.400 | 4.820 | 42.035 | 42.035 | n/a | n/a |
| python [arch_0000] (PID 13026) vms_mb | MB | 8 | 36.951 | 10.152 | 51.219 | 51.219 | n/a | n/a |
| docker (PID 13028) rss_mb | MB | 1 | 4.469 | 4.469 | 4.469 | 4.469 | n/a | n/a |
| docker (PID 13028) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 13036) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 13036) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 13036) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 13036) rss_mb | MB | 2 | 27.098 | 27.098 | 27.098 | 27.098 | n/a | n/a |
| docker (PID 13036) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 13109) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 13109) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 13109) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 13109) rss_mb | MB | 2 | 26.543 | 26.543 | 26.543 | 26.543 | n/a | n/a |
| docker (PID 13109) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 13148) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 13148) rss_mb | MB | 4 | 3.614 | 0.633 | 12.559 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 13148) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 13172) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 13172) rss_mb | MB | 3 | 1.801 | 1.801 | 1.801 | 1.801 | n/a | n/a |
| tail [arch_0000] (PID 13172) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 13182) rss_mb | MB | 1 | 27.297 | 27.297 | 27.297 | 27.297 | n/a | n/a |
| docker (PID 13182) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 13202) rss_mb | MB | 1 | 11.336 | 11.336 | 11.336 | 11.336 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 13202) vms_mb | MB | 1 | 1570.340 | 1570.340 | 1570.340 | 1570.340 | n/a | n/a |
| docker (PID 13238) rss_mb | MB | 1 | 21.102 | 21.102 | 21.102 | 21.102 | n/a | n/a |
| docker (PID 13238) vms_mb | MB | 1 | 1524.203 | 1524.203 | 1524.203 | 1524.203 | n/a | n/a |
| docker (PID 13285) CPU | percent | 1 | 9.739 | 9.739 | 9.739 | 9.739 | 0.010000 CPU seconds | n/a |
| docker (PID 13285) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 13285) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 13285) rss_mb | MB | 2 | 19.342 | 11.930 | 26.754 | 26.754 | n/a | n/a |
| docker (PID 13285) vms_mb | MB | 2 | 1556.236 | 1451.699 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 13349) rss_mb | MB | 1 | 25.852 | 25.852 | 25.852 | 25.852 | n/a | n/a |
| docker (PID 13349) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 13381) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 13381) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 13381) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 13381) rss_mb | MB | 39 | 25.134 | 7.062 | 25.609 | 25.609 | n/a | n/a |
| docker (PID 13381) vms_mb | MB | 39 | 1618.481 | 32.738 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 13406) rss_mb | MB | 1 | 25.641 | 25.641 | 25.641 | 25.641 | n/a | n/a |
| docker (PID 13406) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| python3 (PID 13430) CPU | percent | 3 | 102.151 | 89.024 | 108.823 | 108.823 | 0.310000 CPU seconds | n/a |
| python3 (PID 13430) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 13430) io write MB/s | MB/s | 3 | 0.605 | 0.000 | 1.816 | 1.816 | 0.183594 MB | n/a |
| python3 (PID 13430) rss_mb | MB | 4 | 25.051 | 11.578 | 34.316 | 34.316 | n/a | n/a |
| python3 (PID 13430) vms_mb | MB | 4 | 49.563 | 37.938 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 13433) rss_mb | MB | 1 | 11.301 | 11.301 | 11.301 | 11.301 | n/a | n/a |
| docker (PID 13433) vms_mb | MB | 1 | 1451.949 | 1451.949 | 1451.949 | 1451.949 | n/a | n/a |
| docker (PID 13458) rss_mb | MB | 1 | 25.648 | 25.648 | 25.648 | 25.648 | n/a | n/a |
| docker (PID 13458) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 13467) rss_mb | MB | 1 | 25.680 | 25.680 | 25.680 | 25.680 | n/a | n/a |
| docker (PID 13467) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 13481) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 13481) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 13481) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 13481) rss_mb | MB | 2 | 27.504 | 27.504 | 27.504 | 27.504 | n/a | n/a |
| docker (PID 13481) vms_mb | MB | 2 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [bake_0000] (PID 13521) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bake_0000] (PID 13521) rss_mb | MB | 5 | 3.025 | 0.633 | 12.594 | 0.633 | n/a | n/a |
| docker-init [bake_0000] (PID 13521) vms_mb | MB | 5 | 314.889 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 13548) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 13548) rss_mb | MB | 4 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bake_0000] (PID 13548) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 13552) rss_mb | MB | 1 | 27.414 | 27.414 | 27.414 | 27.414 | n/a | n/a |
| docker (PID 13552) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] (PID 13572) rss_mb | MB | 1 | 11.574 | 11.574 | 11.574 | 11.574 | n/a | n/a |
| runc:[2:INIT] (PID 13572) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 13654) rss_mb | MB | 1 | 25.609 | 25.609 | 25.609 | 25.609 | n/a | n/a |
| docker (PID 13654) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 13692) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 13692) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 13692) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 13692) rss_mb | MB | 2 | 25.941 | 25.941 | 25.941 | 25.941 | n/a | n/a |
| docker (PID 13692) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 13765) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 13765) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 13765) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 13765) rss_mb | MB | 2 | 25.785 | 25.785 | 25.785 | 25.785 | n/a | n/a |
| docker (PID 13765) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 13804) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 13804) rss_mb | MB | 4 | 3.614 | 0.633 | 12.559 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 13804) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 13829) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 13829) rss_mb | MB | 3 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [bake_0000] (PID 13829) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 13840) rss_mb | MB | 1 | 27.156 | 27.156 | 27.156 | 27.156 | n/a | n/a |
| docker (PID 13840) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 13867) rss_mb | MB | 1 | 27.480 | 27.480 | 27.480 | 27.480 | n/a | n/a |
| docker (PID 13867) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| sh [bake_0000] (PID 13887) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sh [bake_0000] (PID 13887) vms_mb | MB | 1 | 0.516 | 0.516 | 0.516 | 0.516 | n/a | n/a |
| docker (PID 13933) rss_mb | MB | 1 | 19.984 | 19.984 | 19.984 | 19.984 | n/a | n/a |
| docker (PID 13933) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 13941) rss_mb | MB | 1 | 25.695 | 25.695 | 25.695 | 25.695 | n/a | n/a |
| docker (PID 13941) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 14014) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 14014) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 14014) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 14014) rss_mb | MB | 2 | 25.730 | 25.730 | 25.730 | 25.730 | n/a | n/a |
| docker (PID 14014) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 14055) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 14055) rss_mb | MB | 3 | 4.803 | 0.633 | 13.145 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 14055) vms_mb | MB | 3 | 548.197 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 14080) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 14080) rss_mb | MB | 2 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [bake_0000] (PID 14080) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 14091) rss_mb | MB | 1 | 25.703 | 25.703 | 25.703 | 25.703 | n/a | n/a |
| docker (PID 14091) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 14119) rss_mb | MB | 1 | 27.250 | 27.250 | 27.250 | 27.250 | n/a | n/a |
| docker (PID 14119) vms_mb | MB | 1 | 1733.027 | 1733.027 | 1733.027 | 1733.027 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 14140) rss_mb | MB | 1 | 11.820 | 11.820 | 11.820 | 11.820 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 14140) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 14162) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 14162) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 14162) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 14162) rss_mb | MB | 2 | 25.879 | 25.879 | 25.879 | 25.879 | n/a | n/a |
| docker (PID 14162) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 14236) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 14236) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 14236) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 14236) rss_mb | MB | 2 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| docker (PID 14236) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 14275) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 14275) rss_mb | MB | 4 | 3.723 | 0.633 | 12.992 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 14275) vms_mb | MB | 4 | 411.411 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 14301) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 14301) rss_mb | MB | 3 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [bake_0000] (PID 14301) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 14311) rss_mb | MB | 1 | 26.969 | 26.969 | 26.969 | 26.969 | n/a | n/a |
| docker (PID 14311) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 14337) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 14337) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 14402) rss_mb | MB | 1 | 23.789 | 23.789 | 23.789 | 23.789 | n/a | n/a |
| docker (PID 14402) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 14410) rss_mb | MB | 1 | 27.086 | 27.086 | 27.086 | 27.086 | n/a | n/a |
| docker (PID 14410) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 14470) rss_mb | MB | 1 | 25.285 | 25.285 | 25.285 | 25.285 | n/a | n/a |
| docker (PID 14470) vms_mb | MB | 1 | 1596.211 | 1596.211 | 1596.211 | 1596.211 | n/a | n/a |
| docker (PID 14496) rss_mb | MB | 1 | 19.785 | 19.785 | 19.785 | 19.785 | n/a | n/a |
| docker (PID 14496) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 14510) CPU | percent | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 14510) io read MB/s | MB/s | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 14510) io write MB/s | MB/s | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 14510) rss_mb | MB | 47 | 26.863 | 26.863 | 26.863 | 26.863 | n/a | n/a |
| docker (PID 14510) vms_mb | MB | 47 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 14526) rss_mb | MB | 1 | 25.652 | 25.652 | 25.652 | 25.652 | n/a | n/a |
| docker (PID 14526) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 14553) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 14553) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 14553) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 14553) rss_mb | MB | 2 | 26.934 | 26.934 | 26.934 | 26.934 | n/a | n/a |
| docker (PID 14553) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 14594) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 14594) rss_mb | MB | 4 | 3.629 | 0.633 | 12.617 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 14594) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 14616) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 14616) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bake_0000] (PID 14616) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 14634) rss_mb | MB | 1 | 26.676 | 26.676 | 26.676 | 26.676 | n/a | n/a |
| docker (PID 14634) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 14655) rss_mb | MB | 1 | 11.816 | 11.816 | 11.816 | 11.816 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 14655) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 14700) rss_mb | MB | 1 | 1.094 | 1.094 | 1.094 | 1.094 | n/a | n/a |
| docker (PID 14700) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 14739) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 14739) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 14739) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 14739) rss_mb | MB | 2 | 25.926 | 25.016 | 26.836 | 26.836 | n/a | n/a |
| docker (PID 14739) vms_mb | MB | 2 | 1624.490 | 1588.207 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 14806) rss_mb | MB | 1 | 27.211 | 27.211 | 27.211 | 27.211 | n/a | n/a |
| docker (PID 14806) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 14814) rss_mb | MB | 1 | 26.621 | 26.621 | 26.621 | 26.621 | n/a | n/a |
| docker (PID 14814) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 14853) CPU | percent | 10 | 0.982 | 0.000 | 9.821 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 14853) rss_mb | MB | 11 | 1.692 | 0.633 | 12.281 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 14853) vms_mb | MB | 11 | 143.707 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 14877) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 14877) rss_mb | MB | 10 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bake_0000] (PID 14877) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 14879) rss_mb | MB | 1 | 23.730 | 23.730 | 23.730 | 23.730 | n/a | n/a |
| docker (PID 14879) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 14916) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 14916) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 14916) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 14916) rss_mb | MB | 9 | 27.020 | 27.020 | 27.020 | 27.020 | n/a | n/a |
| docker (PID 14916) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [bake_0000] (PID 14934) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bake_0000] (PID 14934) rss_mb | MB | 8 | 3.410 | 3.410 | 3.410 | 3.410 | n/a | n/a |
| bash [bake_0000] (PID 14934) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bake_0000] (PID 14944) CPU | percent | 7 | 100.756 | 97.680 | 107.897 | 98.079 | 0.720000 CPU seconds | n/a |
| python [bake_0000] (PID 14944) rss_mb | MB | 8 | 33.553 | 15.402 | 42.762 | 42.055 | n/a | n/a |
| python [bake_0000] (PID 14944) vms_mb | MB | 8 | 40.627 | 19.551 | 52.285 | 51.375 | n/a | n/a |
| docker (PID 14954) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 14954) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 14954) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 14954) rss_mb | MB | 2 | 25.848 | 25.848 | 25.848 | 25.848 | n/a | n/a |
| docker (PID 14954) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 15031) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 15031) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 15031) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 15031) rss_mb | MB | 2 | 25.359 | 25.359 | 25.359 | 25.359 | n/a | n/a |
| docker (PID 15031) vms_mb | MB | 2 | 1624.209 | 1588.207 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 15072) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 15072) rss_mb | MB | 4 | 3.716 | 0.633 | 12.965 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 15072) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 15095) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 15095) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bake_0000] (PID 15095) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 15107) rss_mb | MB | 1 | 26.699 | 26.699 | 26.699 | 26.699 | n/a | n/a |
| docker (PID 15107) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 15137) rss_mb | MB | 1 | 27.484 | 27.484 | 27.484 | 27.484 | n/a | n/a |
| docker (PID 15137) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 15156) rss_mb | MB | 1 | 11.727 | 11.727 | 11.727 | 11.727 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 15156) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 15199) rss_mb | MB | 1 | 4.574 | 4.574 | 4.574 | 4.574 | n/a | n/a |
| docker (PID 15199) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 15207) rss_mb | MB | 1 | 27.062 | 27.062 | 27.062 | 27.062 | n/a | n/a |
| docker (PID 15207) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 15263) rss_mb | MB | 1 | 11.223 | 11.223 | 11.223 | 11.223 | n/a | n/a |
| docker (PID 15263) vms_mb | MB | 1 | 1451.949 | 1451.949 | 1451.949 | 1451.949 | n/a | n/a |
| docker (PID 15280) rss_mb | MB | 1 | 8.668 | 8.668 | 8.668 | 8.668 | n/a | n/a |
| docker (PID 15280) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 15305) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 15305) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 15305) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 15305) rss_mb | MB | 39 | 25.650 | 23.180 | 25.715 | 25.715 | n/a | n/a |
| docker (PID 15305) vms_mb | MB | 39 | 1660.204 | 1659.957 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 15330) rss_mb | MB | 1 | 27.012 | 27.012 | 27.012 | 27.012 | n/a | n/a |
| docker (PID 15330) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 15354) CPU | percent | 3 | 98.894 | 89.045 | 108.651 | 98.985 | 0.300000 CPU seconds | n/a |
| python3 (PID 15354) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 15354) io write MB/s | MB/s | 3 | 0.606 | 0.000 | 1.817 | 1.817 | 0.183594 MB | n/a |
| python3 (PID 15354) rss_mb | MB | 4 | 25.327 | 11.961 | 34.363 | 34.363 | n/a | n/a |
| python3 (PID 15354) vms_mb | MB | 4 | 49.612 | 38.035 | 57.465 | 57.465 | n/a | n/a |
| docker (PID 15357) rss_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| docker (PID 15357) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 15383) rss_mb | MB | 1 | 26.402 | 26.402 | 26.402 | 26.402 | n/a | n/a |
| docker (PID 15383) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 15406) CPU | percent | 1 | 9.778 | 9.778 | 9.778 | 9.778 | 0.010000 CPU seconds | n/a |
| docker (PID 15406) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 15406) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 15406) rss_mb | MB | 2 | 27.439 | 27.309 | 27.570 | 27.570 | n/a | n/a |
| docker (PID 15406) vms_mb | MB | 2 | 1696.775 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [bale_0000] (PID 15446) CPU | percent | 4 | 2.456 | 0.000 | 9.823 | 0.000 | 0.010000 CPU seconds | n/a |
| docker-init [bale_0000] (PID 15446) rss_mb | MB | 5 | 2.827 | 0.633 | 11.602 | 0.633 | n/a | n/a |
| docker-init [bale_0000] (PID 15446) vms_mb | MB | 5 | 314.786 | 1.055 | 1569.711 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 15472) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 15472) rss_mb | MB | 4 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [bale_0000] (PID 15472) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 15476) rss_mb | MB | 1 | 19.543 | 19.543 | 19.543 | 19.543 | n/a | n/a |
| docker (PID 15476) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 15514) rss_mb | MB | 1 | 27.152 | 27.152 | 27.152 | 27.152 | n/a | n/a |
| docker (PID 15514) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 15606) rss_mb | MB | 1 | 22.914 | 22.914 | 22.914 | 22.914 | n/a | n/a |
| docker (PID 15606) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 15614) rss_mb | MB | 1 | 25.996 | 25.996 | 25.996 | 25.996 | n/a | n/a |
| docker (PID 15614) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 15678) rss_mb | MB | 1 | 3.156 | 3.156 | 3.156 | 3.156 | n/a | n/a |
| docker (PID 15678) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 15686) rss_mb | MB | 1 | 26.156 | 26.156 | 26.156 | 26.156 | n/a | n/a |
| docker (PID 15686) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 15725) CPU | percent | 3 | 3.266 | 0.000 | 9.798 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 15725) rss_mb | MB | 4 | 3.396 | 0.633 | 11.688 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 15725) vms_mb | MB | 4 | 393.219 | 1.055 | 1569.711 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 15747) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 15747) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bale_0000] (PID 15747) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 15751) rss_mb | MB | 1 | 25.656 | 25.656 | 25.656 | 25.656 | n/a | n/a |
| docker (PID 15751) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 15788) rss_mb | MB | 1 | 27.344 | 27.344 | 27.344 | 27.344 | n/a | n/a |
| docker (PID 15788) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 15824) rss_mb | MB | 1 | 27.117 | 27.117 | 27.117 | 27.117 | n/a | n/a |
| docker (PID 15824) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 15845) rss_mb | MB | 1 | 10.984 | 10.984 | 10.984 | 10.984 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 15845) vms_mb | MB | 1 | 1641.707 | 1641.707 | 1641.707 | 1641.707 | n/a | n/a |
| docker (PID 15862) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 15862) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 15862) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 15862) rss_mb | MB | 2 | 25.922 | 25.922 | 25.922 | 25.922 | n/a | n/a |
| docker (PID 15862) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 15959) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 15959) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 15959) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 15959) rss_mb | MB | 38 | 26.612 | 19.922 | 26.793 | 26.793 | n/a | n/a |
| docker (PID 15959) vms_mb | MB | 38 | 1656.962 | 1515.949 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 15975) rss_mb | MB | 1 | 25.668 | 25.668 | 25.668 | 25.668 | n/a | n/a |
| docker (PID 15975) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 16001) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 16001) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 16001) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 16001) rss_mb | MB | 2 | 25.641 | 25.641 | 25.641 | 25.641 | n/a | n/a |
| docker (PID 16001) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 16041) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 16041) rss_mb | MB | 4 | 3.677 | 0.633 | 12.809 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 16041) vms_mb | MB | 4 | 411.411 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 16071) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 16071) rss_mb | MB | 3 | 1.691 | 1.691 | 1.691 | 1.691 | n/a | n/a |
| tail [bale_0000] (PID 16071) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 16081) rss_mb | MB | 1 | 26.902 | 26.902 | 26.902 | 26.902 | n/a | n/a |
| docker (PID 16081) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 16103) rss_mb | MB | 1 | 11.855 | 11.855 | 11.855 | 11.855 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 16103) vms_mb | MB | 1 | 1642.980 | 1642.980 | 1642.980 | 1642.980 | n/a | n/a |
| docker (PID 16140) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 16140) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 16190) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 16190) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 16190) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 16190) rss_mb | MB | 2 | 23.875 | 21.773 | 25.977 | 25.977 | n/a | n/a |
| docker (PID 16190) vms_mb | MB | 2 | 1624.207 | 1588.203 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 16254) rss_mb | MB | 1 | 16.488 | 16.488 | 16.488 | 16.488 | n/a | n/a |
| docker (PID 16254) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 16262) rss_mb | MB | 1 | 25.965 | 25.965 | 25.965 | 25.965 | n/a | n/a |
| docker (PID 16262) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 16300) CPU | percent | 37 | 0.794 | 0.000 | 29.378 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 16300) rss_mb | MB | 38 | 0.940 | 0.633 | 12.320 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 16300) vms_mb | MB | 38 | 42.358 | 1.055 | 1570.598 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 16321) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 16321) rss_mb | MB | 37 | 1.730 | 1.730 | 1.730 | 1.730 | n/a | n/a |
| tail [bale_0000] (PID 16321) vms_mb | MB | 37 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 16333) rss_mb | MB | 1 | 0.129 | 0.129 | 0.129 | 0.129 | n/a | n/a |
| docker (PID 16333) vms_mb | MB | 1 | 30.570 | 30.570 | 30.570 | 30.570 | n/a | n/a |
| docker (PID 16361) CPU | percent | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 16361) io read MB/s | MB/s | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 16361) io write MB/s | MB/s | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 16361) rss_mb | MB | 35 | 27.020 | 27.020 | 27.020 | 27.020 | n/a | n/a |
| docker (PID 16361) vms_mb | MB | 35 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [bale_0000] (PID 16379) CPU | percent | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bale_0000] (PID 16379) rss_mb | MB | 34 | 3.395 | 3.395 | 3.395 | 3.395 | n/a | n/a |
| bash [bale_0000] (PID 16379) vms_mb | MB | 34 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bale_0000] (PID 16388) CPU | percent | 33 | 99.578 | 88.265 | 108.015 | 98.181 | 3.350000 CPU seconds | n/a |
| python [bale_0000] (PID 16388) rss_mb | MB | 34 | 39.688 | 14.820 | 42.336 | 41.793 | n/a | n/a |
| python [bale_0000] (PID 16388) vms_mb | MB | 34 | 48.634 | 18.508 | 52.043 | 51.324 | n/a | n/a |
| docker (PID 16399) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 16399) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 16399) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 16399) rss_mb | MB | 2 | 15.668 | 5.414 | 25.922 | 25.922 | n/a | n/a |
| docker (PID 16399) vms_mb | MB | 2 | 846.486 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 16461) rss_mb | MB | 1 | 23.715 | 23.715 | 23.715 | 23.715 | n/a | n/a |
| docker (PID 16461) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 16479) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 16479) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 16479) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 16479) rss_mb | MB | 2 | 26.707 | 26.707 | 26.707 | 26.707 | n/a | n/a |
| docker (PID 16479) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 16518) CPU | percent | 3 | 9.721 | 0.000 | 29.162 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 16518) rss_mb | MB | 4 | 3.148 | 0.633 | 10.695 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 16518) vms_mb | MB | 4 | 393.090 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 16543) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 16543) rss_mb | MB | 3 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [bale_0000] (PID 16543) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 16582) rss_mb | MB | 1 | 10.574 | 10.574 | 10.574 | 10.574 | n/a | n/a |
| docker (PID 16582) vms_mb | MB | 1 | 1387.949 | 1387.949 | 1387.949 | 1387.949 | n/a | n/a |
| docker (PID 16617) rss_mb | MB | 1 | 27.398 | 27.398 | 27.398 | 27.398 | n/a | n/a |
| docker (PID 16617) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 16654) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 16654) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 16654) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 16654) rss_mb | MB | 2 | 25.762 | 25.762 | 25.762 | 25.762 | n/a | n/a |
| docker (PID 16654) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 16730) rss_mb | MB | 1 | 20.047 | 20.047 | 20.047 | 20.047 | n/a | n/a |
| docker (PID 16730) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 16756) rss_mb | MB | 1 | 25.953 | 25.953 | 25.953 | 25.953 | n/a | n/a |
| docker (PID 16756) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 16764) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 16764) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 16764) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 16764) rss_mb | MB | 39 | 26.934 | 26.934 | 26.934 | 26.934 | n/a | n/a |
| docker (PID 16764) vms_mb | MB | 39 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 16812) CPU | percent | 23 | 99.743 | 98.457 | 108.816 | 98.945 | 2.320000 CPU seconds | n/a |
| python3 (PID 16812) io read MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 16812) io write MB/s | MB/s | 23 | 0.072 | 0.000 | 1.662 | 1.662 | 0.167969 MB | n/a |
| python3 (PID 16812) rss_mb | MB | 24 | 32.948 | 19.859 | 34.285 | 34.285 | n/a | n/a |
| python3 (PID 16812) vms_mb | MB | 24 | 55.686 | 44.188 | 57.461 | 57.461 | n/a | n/a |
| docker (PID 16833) rss_mb | MB | 1 | 26.953 | 26.953 | 26.953 | 26.953 | n/a | n/a |
| docker (PID 16833) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 16865) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 16865) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 16865) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 16865) rss_mb | MB | 3 | 27.327 | 27.121 | 27.430 | 27.430 | n/a | n/a |
| docker (PID 16865) vms_mb | MB | 3 | 1708.776 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [band_0000] (PID 16904) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [band_0000] (PID 16904) rss_mb | MB | 4 | 3.639 | 0.633 | 12.656 | 0.633 | n/a | n/a |
| docker-init [band_0000] (PID 16904) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 16929) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 16929) rss_mb | MB | 3 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [band_0000] (PID 16929) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 16961) rss_mb | MB | 1 | 26.398 | 26.398 | 26.398 | 26.398 | n/a | n/a |
| docker (PID 16961) vms_mb | MB | 1 | 1588.270 | 1588.270 | 1588.270 | 1588.270 | n/a | n/a |
| docker (PID 16998) rss_mb | MB | 1 | 27.160 | 27.160 | 27.160 | 27.160 | n/a | n/a |
| docker (PID 16998) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 17017) rss_mb | MB | 1 | 7.617 | 7.617 | 7.617 | 7.617 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 17017) vms_mb | MB | 1 | 1432.941 | 1432.941 | 1432.941 | 1432.941 | n/a | n/a |
| docker (PID 17031) rss_mb | MB | 1 | 27.062 | 27.062 | 27.062 | 27.062 | n/a | n/a |
| docker (PID 17031) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 17051) rss_mb | MB | 1 | 11.730 | 11.730 | 11.730 | 11.730 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 17051) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 17068) rss_mb | MB | 1 | 26.824 | 26.824 | 26.824 | 26.824 | n/a | n/a |
| docker (PID 17068) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 17123) rss_mb | MB | 1 | 1.082 | 1.082 | 1.082 | 1.082 | n/a | n/a |
| docker (PID 17123) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 17139) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 17139) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 17139) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 17139) rss_mb | MB | 2 | 26.867 | 26.867 | 26.867 | 26.867 | n/a | n/a |
| docker (PID 17139) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [band_0000] (PID 17178) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [band_0000] (PID 17178) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [band_0000] (PID 17178) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 17202) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 17202) rss_mb | MB | 3 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [band_0000] (PID 17202) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 17242) rss_mb | MB | 1 | 18.258 | 18.258 | 18.258 | 18.258 | n/a | n/a |
| docker (PID 17242) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 17276) rss_mb | MB | 1 | 27.270 | 27.270 | 27.270 | 27.270 | n/a | n/a |
| docker (PID 17276) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 17312) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 17312) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 17312) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 17312) rss_mb | MB | 2 | 26.008 | 26.008 | 26.008 | 26.008 | n/a | n/a |
| docker (PID 17312) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 17408) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 17408) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 17408) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 17408) rss_mb | MB | 38 | 25.609 | 25.609 | 25.609 | 25.609 | n/a | n/a |
| docker (PID 17408) vms_mb | MB | 38 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 17451) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 17451) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 17451) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 17451) rss_mb | MB | 2 | 26.641 | 26.641 | 26.641 | 26.641 | n/a | n/a |
| docker (PID 17451) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 17489) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 17489) rss_mb | MB | 4 | 3.629 | 0.633 | 12.617 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 17489) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 17516) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 17516) rss_mb | MB | 3 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [band_0000] (PID 17516) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 17528) rss_mb | MB | 1 | 21.445 | 21.445 | 21.445 | 21.445 | n/a | n/a |
| docker (PID 17528) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 17554) rss_mb | MB | 1 | 27.383 | 27.383 | 27.383 | 27.383 | n/a | n/a |
| docker (PID 17554) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 17573) rss_mb | MB | 1 | 11.691 | 11.691 | 11.691 | 11.691 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 17573) vms_mb | MB | 1 | 1570.848 | 1570.848 | 1570.848 | 1570.848 | n/a | n/a |
| docker (PID 17589) rss_mb | MB | 1 | 27.098 | 27.098 | 27.098 | 27.098 | n/a | n/a |
| docker (PID 17589) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 17609) rss_mb | MB | 1 | 12.496 | 12.496 | 12.496 | 12.496 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 17609) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 17628) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 17628) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 17628) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 17628) rss_mb | MB | 2 | 26.781 | 26.781 | 26.781 | 26.781 | n/a | n/a |
| docker (PID 17628) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 17695) rss_mb | MB | 1 | 16.066 | 16.066 | 16.066 | 16.066 | n/a | n/a |
| docker (PID 17695) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 17703) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 17703) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 17703) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 17703) rss_mb | MB | 2 | 25.590 | 25.590 | 25.590 | 25.590 | n/a | n/a |
| docker (PID 17703) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 17742) CPU | percent | 11 | 2.657 | 0.000 | 29.222 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 17742) rss_mb | MB | 12 | 1.521 | 0.633 | 11.285 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 17742) vms_mb | MB | 12 | 131.775 | 1.055 | 1569.695 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 17764) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 17764) rss_mb | MB | 11 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [band_0000] (PID 17764) vms_mb | MB | 11 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 17803) CPU | percent | 8 | 2.445 | 0.000 | 19.560 | 0.000 | 0.020000 CPU seconds | n/a |
| docker (PID 17803) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 17803) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 17803) rss_mb | MB | 9 | 25.050 | 7.172 | 27.285 | 27.285 | n/a | n/a |
| docker (PID 17803) vms_mb | MB | 9 | 1479.881 | 32.738 | 1660.773 | 1660.773 | n/a | n/a |
| bash [band_0000] (PID 17823) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [band_0000] (PID 17823) rss_mb | MB | 8 | 3.320 | 3.320 | 3.320 | 3.320 | n/a | n/a |
| bash [band_0000] (PID 17823) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [band_0000] (PID 17833) CPU | percent | 7 | 100.674 | 97.422 | 107.901 | 107.830 | 0.720000 CPU seconds | n/a |
| python [band_0000] (PID 17833) rss_mb | MB | 8 | 30.652 | 11.441 | 41.266 | 41.266 | n/a | n/a |
| python [band_0000] (PID 17833) vms_mb | MB | 8 | 37.813 | 15.039 | 51.324 | 51.324 | n/a | n/a |
| docker (PID 17835) rss_mb | MB | 1 | 7.391 | 7.391 | 7.391 | 7.391 | n/a | n/a |
| docker (PID 17835) vms_mb | MB | 1 | 32.867 | 32.867 | 32.867 | 32.867 | n/a | n/a |
| docker (PID 17843) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 17843) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 17843) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 17843) rss_mb | MB | 2 | 26.973 | 26.973 | 26.973 | 26.973 | n/a | n/a |
| docker (PID 17843) vms_mb | MB | 2 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 17917) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 17917) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 17917) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 17917) rss_mb | MB | 2 | 25.793 | 25.793 | 25.793 | 25.793 | n/a | n/a |
| docker (PID 17917) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 17956) CPU | percent | 3 | 3.267 | 0.000 | 9.802 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 17956) rss_mb | MB | 4 | 3.659 | 0.633 | 12.738 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 17956) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 17978) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 17978) rss_mb | MB | 3 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [band_0000] (PID 17978) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 17993) rss_mb | MB | 1 | 27.465 | 27.465 | 27.465 | 27.465 | n/a | n/a |
| docker (PID 17993) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 18013) rss_mb | MB | 1 | 11.695 | 11.695 | 11.695 | 11.695 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 18013) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 18093) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 18093) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 18093) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 18093) rss_mb | MB | 2 | 24.473 | 22.953 | 25.992 | 25.992 | n/a | n/a |
| docker (PID 18093) vms_mb | MB | 2 | 1624.207 | 1588.203 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 18161) rss_mb | MB | 1 | 24.090 | 24.090 | 24.090 | 24.090 | n/a | n/a |
| docker (PID 18161) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 18193) CPU | percent | 39 | 0.253 | 0.000 | 9.868 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 18193) io read MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 18193) io write MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 18193) rss_mb | MB | 40 | 26.282 | 6.344 | 26.793 | 26.793 | n/a | n/a |
| docker (PID 18193) vms_mb | MB | 40 | 1620.073 | 32.762 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 18226) rss_mb | MB | 1 | 26.434 | 26.434 | 26.434 | 26.434 | n/a | n/a |
| docker (PID 18226) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 18241) CPU | percent | 3 | 98.788 | 89.021 | 108.701 | 108.701 | 0.300000 CPU seconds | n/a |
| python3 (PID 18241) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 18241) io write MB/s | MB/s | 3 | 0.605 | 0.000 | 1.814 | 1.814 | 0.183594 MB | n/a |
| python3 (PID 18241) rss_mb | MB | 4 | 27.355 | 16.426 | 34.484 | 34.484 | n/a | n/a |
| python3 (PID 18241) vms_mb | MB | 4 | 51.422 | 41.172 | 57.457 | 57.457 | n/a | n/a |
| docker (PID 18259) rss_mb | MB | 1 | 26.996 | 26.996 | 26.996 | 26.996 | n/a | n/a |
| docker (PID 18259) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 9098) CPU | percent | 4045 | 2.750 | 0.000 | 124.806 | 9.888 | 11.580000 CPU seconds | n/a |
| python3 (PID 9098) io read MB/s | MB/s | 4045 | 0.037 | 0.000 | 68.668 | 0.000 | 15.355469 MB | n/a |
| python3 (PID 9098) io write MB/s | MB/s | 4045 | 0.037 | 0.000 | 22.148 | 3.631 | 15.265625 MB | n/a |
| python3 (PID 9098) rss_mb | MB | 4046 | 671.538 | 615.875 | 691.383 | 691.383 | n/a | n/a |
| python3 (PID 9098) vms_mb | MB | 4046 | 3618.249 | 3414.094 | 3757.148 | 3757.117 | n/a | n/a |
| git (PID 9104) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| git (PID 9104) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 9104) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 9104) rss_mb | MB | 2 | 4.910 | 4.910 | 4.910 | 4.910 | n/a | n/a |
| git (PID 9104) vms_mb | MB | 2 | 12.516 | 12.516 | 12.516 | 12.516 | n/a | n/a |
| git (PID 9105) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| git (PID 9105) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 9105) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 9105) rss_mb | MB | 2 | 3.559 | 3.559 | 3.559 | 3.559 | n/a | n/a |
| git (PID 9105) vms_mb | MB | 2 | 11.273 | 11.273 | 11.273 | 11.273 | n/a | n/a |
| git-remote-http (PID 9106) CPU | percent | 1 | 39.512 | 39.512 | 39.512 | 39.512 | 0.040000 CPU seconds | n/a |
| git-remote-http (PID 9106) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git-remote-http (PID 9106) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git-remote-http (PID 9106) rss_mb | MB | 2 | 14.725 | 10.223 | 19.227 | 19.227 | n/a | n/a |
| git-remote-http (PID 9106) vms_mb | MB | 2 | 103.322 | 99.078 | 107.566 | 107.566 | n/a | n/a |
| python3 (PID 9112) CPU | percent | 1189 | 99.970 | 89.049 | 109.087 | 99.032 | 120.020000 CPU seconds | n/a |
| python3 (PID 9112) io read MB/s | MB/s | 1189 | 0.001 | 0.000 | 1.780 | 0.000 | 0.179688 MB | n/a |
| python3 (PID 9112) io write MB/s | MB/s | 1189 | 0.000 | 0.000 | 0.155 | 0.000 | 0.015625 MB | n/a |
| python3 (PID 9112) rss_mb | MB | 1190 | 33.987 | 10.449 | 34.020 | 34.020 | n/a | n/a |
| python3 (PID 9112) vms_mb | MB | 1190 | 56.473 | 36.633 | 56.500 | 56.500 | n/a | n/a |
| python3 (PID 9115) CPU | percent | 4 | 89.115 | 59.390 | 109.000 | 109.000 | 0.360000 CPU seconds | n/a |
| python3 (PID 9115) io read MB/s | MB/s | 4 | 2.948 | 0.000 | 10.633 | 0.000 | 1.191406 MB | n/a |
| python3 (PID 9115) io write MB/s | MB/s | 4 | 0.484 | 0.000 | 1.897 | 1.897 | 0.195312 MB | n/a |
| python3 (PID 9115) rss_mb | MB | 5 | 26.147 | 14.332 | 34.582 | 34.582 | n/a | n/a |
| python3 (PID 9115) vms_mb | MB | 5 | 49.952 | 39.566 | 57.512 | 57.512 | n/a | n/a |
| python3 (PID 9116) CPU | percent | 3 | 99.031 | 98.872 | 99.140 | 99.140 | 0.300000 CPU seconds | n/a |
| python3 (PID 9116) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 9116) io write MB/s | MB/s | 3 | 0.052 | 0.000 | 0.155 | 0.155 | 0.015625 MB | n/a |
| python3 (PID 9116) rss_mb | MB | 4 | 26.113 | 12.871 | 35.789 | 35.789 | n/a | n/a |
| python3 (PID 9116) vms_mb | MB | 4 | 50.231 | 38.293 | 58.500 | 58.500 | n/a | n/a |
| python3 (PID 9117) CPU | percent | 2 | 99.030 | 89.179 | 108.881 | 89.179 | 0.200000 CPU seconds | n/a |
| python3 (PID 9117) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 9117) io write MB/s | MB/s | 2 | 0.077 | 0.000 | 0.155 | 0.155 | 0.015625 MB | n/a |
| python3 (PID 9117) rss_mb | MB | 3 | 27.665 | 20.715 | 34.066 | 34.066 | n/a | n/a |
| python3 (PID 9117) vms_mb | MB | 3 | 51.302 | 45.238 | 56.504 | 56.504 | n/a | n/a |
| python3 (PID 9118) CPU | percent | 24 | 100.293 | 98.935 | 108.981 | 99.006 | 2.430000 CPU seconds | n/a |
| python3 (PID 9118) io read MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 9118) io write MB/s | MB/s | 24 | 0.082 | 0.000 | 1.818 | 1.818 | 0.199219 MB | n/a |
| python3 (PID 9118) rss_mb | MB | 25 | 33.295 | 18.699 | 34.918 | 34.918 | n/a | n/a |
| python3 (PID 9118) vms_mb | MB | 25 | 56.644 | 43.699 | 57.512 | 57.512 | n/a | n/a |
| python3 (PID 9119) CPU | percent | 68 | 99.915 | 89.072 | 108.987 | 99.048 | 6.860000 CPU seconds | n/a |
| python3 (PID 9119) io read MB/s | MB/s | 68 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 9119) io write MB/s | MB/s | 68 | 0.029 | 0.000 | 1.819 | 0.000 | 0.199219 MB | n/a |
| python3 (PID 9119) rss_mb | MB | 69 | 41.318 | 17.949 | 47.430 | 47.430 | n/a | n/a |
| python3 (PID 9119) vms_mb | MB | 69 | 64.575 | 42.430 | 70.637 | 70.637 | n/a | n/a |
| docker (PID 9123) rss_mb | MB | 1 | 24.902 | 24.902 | 24.902 | 24.902 | n/a | n/a |
| docker (PID 9123) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-trust (PID 9131) rss_mb | MB | 1 | 12.184 | 12.184 | 12.184 | 12.184 | n/a | n/a |
| docker-trust (PID 9131) vms_mb | MB | 1 | 1212.965 | 1212.965 | 1212.965 | 1212.965 | n/a | n/a |
| docker (PID 9173) CPU | percent | 2 | 9.883 | 9.854 | 9.912 | 9.912 | 0.020000 CPU seconds | n/a |
| docker (PID 9173) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 9173) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 9173) rss_mb | MB | 3 | 23.940 | 17.852 | 27.336 | 27.336 | n/a | n/a |
| docker (PID 9173) vms_mb | MB | 3 | 1636.417 | 1515.699 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [alex_0000] (PID 9213) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [alex_0000] (PID 9213) rss_mb | MB | 5 | 3.055 | 0.633 | 12.746 | 0.633 | n/a | n/a |
| docker-init [alex_0000] (PID 9213) vms_mb | MB | 5 | 314.889 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 9241) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 9241) rss_mb | MB | 4 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [alex_0000] (PID 9241) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 9243) rss_mb | MB | 1 | 27.336 | 27.336 | 27.336 | 27.336 | n/a | n/a |
| docker (PID 9243) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 9277) rss_mb | MB | 1 | 27.266 | 27.266 | 27.266 | 27.266 | n/a | n/a |
| docker (PID 9277) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 9296) rss_mb | MB | 1 | 10.930 | 10.930 | 10.930 | 10.930 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 9296) vms_mb | MB | 1 | 1569.711 | 1569.711 | 1569.711 | 1569.711 | n/a | n/a |
| docker (PID 9331) rss_mb | MB | 1 | 26.434 | 26.434 | 26.434 | 26.434 | n/a | n/a |
| docker (PID 9331) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 9376) CPU | percent | 1 | 9.815 | 9.815 | 9.815 | 9.815 | 0.010000 CPU seconds | n/a |
| docker (PID 9376) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 9376) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 9376) rss_mb | MB | 2 | 24.652 | 22.645 | 26.660 | 26.660 | n/a | n/a |
| docker (PID 9376) vms_mb | MB | 2 | 1624.488 | 1588.203 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 9443) rss_mb | MB | 1 | 17.832 | 17.832 | 17.832 | 17.832 | n/a | n/a |
| docker (PID 9443) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 9451) rss_mb | MB | 1 | 26.934 | 26.934 | 26.934 | 26.934 | n/a | n/a |
| docker (PID 9451) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 9491) CPU | percent | 3 | 3.279 | 0.000 | 9.837 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 9491) rss_mb | MB | 4 | 3.514 | 0.633 | 12.156 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 9491) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 9516) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 9516) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [alex_0000] (PID 9516) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 9553) rss_mb | MB | 1 | 27.117 | 27.117 | 27.117 | 27.117 | n/a | n/a |
| docker (PID 9553) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| 6 [alex_0000] (PID 9567) rss_mb | MB | 1 | 0.816 | 0.816 | 0.816 | 0.816 | n/a | n/a |
| 6 [alex_0000] (PID 9567) vms_mb | MB | 1 | 14.004 | 14.004 | 14.004 | 14.004 | n/a | n/a |
| docker (PID 9587) rss_mb | MB | 1 | 27.266 | 27.266 | 27.266 | 27.266 | n/a | n/a |
| docker (PID 9587) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 9608) rss_mb | MB | 1 | 11.445 | 11.445 | 11.445 | 11.445 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 9608) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 9625) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 9625) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 9625) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 9625) rss_mb | MB | 2 | 26.238 | 26.238 | 26.238 | 26.238 | n/a | n/a |
| docker (PID 9625) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 9721) CPU | percent | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 9721) io read MB/s | MB/s | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 9721) io write MB/s | MB/s | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 9721) rss_mb | MB | 53 | 25.844 | 25.844 | 25.844 | 25.844 | n/a | n/a |
| docker (PID 9721) vms_mb | MB | 53 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 9737) rss_mb | MB | 1 | 25.539 | 25.539 | 25.539 | 25.539 | n/a | n/a |
| docker (PID 9737) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 9763) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 9763) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 9763) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 9763) rss_mb | MB | 2 | 24.133 | 22.828 | 25.438 | 25.438 | n/a | n/a |
| docker (PID 9763) vms_mb | MB | 2 | 1624.082 | 1587.953 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 9803) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 9803) rss_mb | MB | 4 | 3.628 | 0.633 | 12.613 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 9803) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 9831) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 9831) rss_mb | MB | 3 | 1.809 | 1.809 | 1.809 | 1.809 | n/a | n/a |
| tail [alex_0000] (PID 9831) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 9867) rss_mb | MB | 1 | 27.020 | 27.020 | 27.020 | 27.020 | n/a | n/a |
| docker (PID 9867) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 9888) rss_mb | MB | 1 | 9.668 | 9.668 | 9.668 | 9.668 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 9888) vms_mb | MB | 1 | 1569.195 | 1569.195 | 1569.195 | 1569.195 | n/a | n/a |
| docker (PID 9904) rss_mb | MB | 1 | 27.281 | 27.281 | 27.281 | 27.281 | n/a | n/a |
| docker (PID 9904) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 9924) rss_mb | MB | 1 | 11.500 | 11.500 | 11.500 | 11.500 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 9924) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 9943) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 9943) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 9943) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 9943) rss_mb | MB | 2 | 26.828 | 26.828 | 26.828 | 26.828 | n/a | n/a |
| docker (PID 9943) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| sandbox alex_0000 CPU | percent | 22 | 57.287 | 3.351 | 100.756 | 43.604 | 1.285844 CPU seconds | n/a |
| sandbox alex_0000 io read MB/s | MB/s | 25 | 0.003 | 0.000 | 0.077 | 0.000 | 0.007812 MB | n/a |
| sandbox alex_0000 io write MB/s | MB/s | 25 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox alex_0000 memory | MB | 27 | 9.330 | 0.758 | 35.195 | 4.266 | n/a | n/a |
| sandbox alex_0000 net rx MB/s | MB/s | 22 | 0.000 | 0.000 | 0.003 | 0.000 | 0.001118 MB | n/a |
| sandbox alex_0000 net tx MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000200 MB | n/a |
| sandbox andy_0000 CPU | percent | 21 | 59.455 | 6.307 | 100.131 | 47.821 | 1.275459 CPU seconds | n/a |
| sandbox andy_0000 io read MB/s | MB/s | 25 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox andy_0000 io write MB/s | MB/s | 24 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox andy_0000 memory | MB | 26 | 9.143 | 0.723 | 36.215 | 3.863 | n/a | n/a |
| sandbox andy_0000 net rx MB/s | MB/s | 22 | 0.000 | 0.000 | 0.002 | 0.000 | 0.000923 MB | n/a |
| sandbox andy_0000 net tx MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| sandbox arch_0000 CPU | percent | 21 | 58.647 | 4.382 | 100.027 | 31.827 | 1.257994 CPU seconds | n/a |
| sandbox arch_0000 io read MB/s | MB/s | 25 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox arch_0000 io write MB/s | MB/s | 24 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox arch_0000 memory | MB | 26 | 8.832 | 0.777 | 35.309 | 0.844 | n/a | n/a |
| sandbox arch_0000 net rx MB/s | MB/s | 22 | 0.000 | 0.000 | 0.002 | 0.000 | 0.000654 MB | n/a |
| sandbox arch_0000 net tx MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000120 MB | n/a |
| sandbox bake_0000 CPU | percent | 26 | 51.367 | 2.973 | 100.972 | 38.209 | 1.367714 CPU seconds | n/a |
| sandbox bake_0000 io read MB/s | MB/s | 32 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bake_0000 io write MB/s | MB/s | 31 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bake_0000 memory | MB | 33 | 8.243 | 0.594 | 36.344 | 0.820 | n/a | n/a |
| sandbox bake_0000 net rx MB/s | MB/s | 26 | 0.001 | 0.000 | 0.003 | 0.001 | 0.001745 MB | n/a |
| sandbox bake_0000 net tx MB/s | MB/s | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000160 MB | n/a |
| sandbox bale_0000 CPU | percent | 48 | 80.916 | 17.618 | 100.269 | 30.506 | 3.963602 CPU seconds | n/a |
| sandbox bale_0000 io read MB/s | MB/s | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bale_0000 io write MB/s | MB/s | 51 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bale_0000 memory | MB | 53 | 22.175 | 0.648 | 36.090 | 0.805 | n/a | n/a |
| sandbox bale_0000 net rx MB/s | MB/s | 48 | 0.000 | 0.000 | 0.002 | 0.000 | 0.001274 MB | n/a |
| sandbox bale_0000 net tx MB/s | MB/s | 49 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000200 MB | n/a |
| sandbox band_0000 CPU | percent | 21 | 59.836 | 3.427 | 100.477 | 31.323 | 1.284103 CPU seconds | n/a |
| sandbox band_0000 io read MB/s | MB/s | 25 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox band_0000 io write MB/s | MB/s | 24 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox band_0000 memory | MB | 26 | 9.215 | 0.000 | 34.688 | 0.676 | n/a | n/a |
| sandbox band_0000 net rx MB/s | MB/s | 20 | 0.000 | 0.000 | 0.003 | 0.000 | 0.000845 MB | n/a |
| sandbox band_0000 net tx MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000120 MB | n/a |
| workload total CPU | percent | 4045 | 41.007 | 0.530 | 104.809 | 101.824 | 168.081406 CPU seconds | n/a |
| workload total io read MB/s | MB/s | 214 | 0.006 | 0.000 | 1.230 | 0.000 | 0.132812 MB | n/a |
| workload total io write MB/s | MB/s | 210 | 0.001 | 0.000 | 0.038 | 0.000 | 0.023438 MB | n/a |
| workload total memory | MB | 4046 | 446.490 | 363.609 | 505.438 | 473.746 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
