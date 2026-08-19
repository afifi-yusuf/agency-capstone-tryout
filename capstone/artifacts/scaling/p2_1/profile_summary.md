# agprof summary

- Duration: **424.145 s**
- Runs: **24/24 completed**, 24 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.057 runs/s**
- LLM: **81 calls**, 81 succeeded, 0 failed, 0 interrupted, 0 retries, 509.932 s total wait
- Tools: **105/105 completed**, 3 failed, 0 interrupted
- Raw resource samples: **57502** at 9.82 Hz effective (10 Hz configured)
- GPU sampling: **unavailable** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 26707.786 / 52519.818 ms |
| LLM latency p50 / p95 | 3366.565 / 20604.375 ms |
| LLM TTFT p50 / p95 | 689.612 / 1260.477 ms |
| LLM input / output tokens | 406180 / 21999 |
| LLM output throughput | 48.943 tokens/s |
| LLM attempts | 81 total, 81 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 416.861 / 1681.452 ms |

### Tool outcomes

| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 13/13 | 13 | 0 | 0 | 1661.637 ms | 14509.032 ms |
| edit | 13/13 | 13 | 0 | 0 | 430.637 ms | 649.248 ms |
| glob | 3/3 | 3 | 0 | 0 | 329.303 ms | 361.145 ms |
| read | 37/37 | 37 | 0 | 0 | 559.879 ms | 864.576 ms |
| return_plan | 12/12 | 12 | 0 | 0 | 0.322 ms | 1.190 ms |
| return_status | 12/12 | 12 | 0 | 0 | 0.305 ms | 1.169 ms |
| return_summary | 15/15 | 12 | 3 | 0 | 0.379 ms | 0.670 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 31.804% | 199.983% | 136.779 s | 511.622 MB | 597.875 MB | 3.132812 MB | 9.128906 MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python3 | 107320 |  | 4165 | 5.129% | 136.087% | 22.080 s | 691.008 MB | 711.254 MB | 3947.035 MB | 4047.340 MB | 33.382812 MB | 34.718750 MB |
| python3 | 107325 |  | 1 | n/a% | n/a% | n/a s | 648.719 MB | 648.719 MB | 3444.871 MB | 3444.871 MB | n/a MB | n/a MB |
| git | 107326 |  | 5 | 0.000% | 0.000% | 0.000 s | 4.660 MB | 4.660 MB | 12.516 MB | 12.516 MB | 0.000000 MB | 0.000000 MB |
| git-remote-http | 107328 |  | 5 | 4.924% | 19.694% | 0.020 s | 18.977 MB | 19.027 MB | 107.166 MB | 107.566 MB | 0.140625 MB | 0.000000 MB |
| git | 107327 |  | 5 | 0.000% | 0.000% | 0.000 s | 3.309 MB | 3.309 MB | 11.273 MB | 11.273 MB | 0.000000 MB | 0.000000 MB |
| python3 | 107334 |  | 100 | 99.961% | 109.049% | 9.990 s | 33.824 MB | 34.211 MB | 57.104 MB | 57.457 MB | 0.000000 MB | 0.015625 MB |
| python3 | 107335 |  | 4 | 99.021% | 99.105% | 0.300 s | 28.578 MB | 34.871 MB | 51.865 MB | 57.500 MB | 0.000000 MB | 0.250000 MB |
| python3 | 107336 |  | 5 | 101.435% | 108.645% | 0.410 s | 27.402 MB | 36.602 MB | 51.341 MB | 59.516 MB | 0.000000 MB | 0.250000 MB |
| python3 | 107337 |  | 4 | 102.342% | 108.882% | 0.310 s | 27.581 MB | 34.766 MB | 51.413 MB | 57.496 MB | 0.000000 MB | 0.250000 MB |
| python3 | 107338 |  | 25 | 99.475% | 109.039% | 2.410 s | 32.941 MB | 34.863 MB | 56.209 MB | 57.457 MB | 0.000000 MB | 0.253906 MB |
| python3 | 107339 |  | 69 | 99.905% | 108.993% | 6.860 s | 41.568 MB | 47.484 MB | 64.559 MB | 70.645 MB | 0.000000 MB | 0.257812 MB |
| python3 | 107340 |  | 4 | 99.014% | 108.895% | 0.300 s | 28.857 MB | 34.957 MB | 52.188 MB | 57.504 MB | 0.000000 MB | 0.257812 MB |
| python3 | 107341 |  | 99 | 99.962% | 109.043% | 9.900 s | 34.163 MB | 34.512 MB | 57.156 MB | 57.457 MB | 0.000000 MB | 0.015625 MB |
| python3 | 107342 |  | 4 | 99.099% | 109.060% | 0.300 s | 26.755 MB | 34.988 MB | 50.665 MB | 57.492 MB | 0.058594 MB | 0.257812 MB |
| python3 | 107343 |  | 4 | 102.303% | 108.928% | 0.310 s | 29.039 MB | 34.730 MB | 52.522 MB | 57.457 MB | 0.000000 MB | 0.261719 MB |
| python3 | 107344 |  | 4 | 102.297% | 108.813% | 0.310 s | 26.364 MB | 34.945 MB | 50.354 MB | 57.508 MB | 0.000000 MB | 0.261719 MB |
| python3 | 107345 |  | 4 | 98.984% | 99.073% | 0.300 s | 29.466 MB | 34.871 MB | 53.125 MB | 57.508 MB | 0.000000 MB | 0.261719 MB |
| docker | 107349 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.912 MB | 26.828 MB | 1660.242 MB | 1660.273 MB | 9.113281 MB | 0.000000 MB |
| docker-trust | 107357 |  | 1 | n/a% | n/a% | n/a s | 6.129 MB | 6.129 MB | 1212.965 MB | 1212.965 MB | n/a MB | n/a MB |
| docker | 107368 |  | 1 | n/a% | n/a% | n/a s | 9.156 MB | 9.156 MB | 1315.695 MB | 1315.695 MB | n/a MB | n/a MB |
| docker | 107431 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.232 MB | 27.406 MB | 1709.026 MB | 1733.027 MB | 0.000000 MB | 0.000000 MB |
| docker | 107432 |  | 3 | 4.929% | 9.857% | 0.010 s | 27.007 MB | 27.113 MB | 1708.776 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 107511 | alex_0000 | 6 | 3.851% | 19.256% | 0.020 s | 2.562 MB | 12.207 MB | 262.583 MB | 1570.227 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 107518 | andy_0000 | 6 | 1.926% | 9.628% | 0.010 s | 2.575 MB | 12.285 MB | 262.625 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 107544 |  | 1 | n/a% | n/a% | n/a s | 27.141 MB | 27.141 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 107539 | andy_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.801 MB | 1.801 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| tail | 107538 | alex_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 107542 |  | 1 | n/a% | n/a% | n/a s | 27.199 MB | 27.199 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 107614 |  | 1 | n/a% | n/a% | n/a s | 8.844 MB | 8.844 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 107615 |  | 1 | n/a% | n/a% | n/a s | 5.945 MB | 5.945 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 107666 |  | 1 | n/a% | n/a% | n/a s | 25.281 MB | 25.281 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 107672 |  | 1 | n/a% | n/a% | n/a s | 9.242 MB | 9.242 MB | 1443.695 MB | 1443.695 MB | n/a MB | n/a MB |
| docker | 107721 |  | 1 | n/a% | n/a% | n/a s | 23.746 MB | 23.746 MB | 1660.207 MB | 1660.207 MB | n/a MB | n/a MB |
| docker | 107801 |  | 1 | n/a% | n/a% | n/a s | 27.035 MB | 27.035 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 107803 |  | 1 | n/a% | n/a% | n/a s | 27.070 MB | 27.070 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 107884 |  | 1 | n/a% | n/a% | n/a s | 24.016 MB | 24.016 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 107886 |  | 1 | n/a% | n/a% | n/a s | 23.496 MB | 23.496 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 107918 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.508 MB | 25.508 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 107916 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.988 MB | 26.988 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 107994 | andy_0000 | 5 | 2.366% | 9.464% | 0.010 s | 2.980 MB | 12.371 MB | 314.939 MB | 1570.477 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 108001 | alex_0000 | 6 | 1.893% | 9.464% | 0.010 s | 2.546 MB | 12.113 MB | 262.583 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 108027 |  | 1 | n/a% | n/a% | n/a s | 17.262 MB | 17.262 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 108025 |  | 1 | n/a% | n/a% | n/a s | 14.750 MB | 14.750 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 108022 | alex_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| tail | 108021 | andy_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 108041 |  | 1 | n/a% | n/a% | n/a s | 27.117 MB | 27.117 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 108043 |  | 1 | n/a% | n/a% | n/a s | 27.426 MB | 27.426 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 108143 | alex_0000 | 1 | n/a% | n/a% | n/a s | 12.055 MB | 12.055 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 108098 |  | 1 | n/a% | n/a% | n/a s | 27.555 MB | 27.555 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 108217 | alex_0000 | 1 | n/a% | n/a% | n/a s | 7.613 MB | 7.613 MB | 1569.195 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 108165 |  | 1 | n/a% | n/a% | n/a s | 27.551 MB | 27.551 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 108196 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.770 MB | 11.770 MB | 1642.602 MB | 1642.602 MB | n/a MB | n/a MB |
| docker | 108172 |  | 1 | n/a% | n/a% | n/a s | 26.992 MB | 26.992 MB | 1733.027 MB | 1733.027 MB | n/a MB | n/a MB |
| docker | 108250 |  | 2 | 0.000% | 0.000% | 0.000 s | 24.445 MB | 25.961 MB | 1588.205 MB | 1588.207 MB | 0.000000 MB | 0.000000 MB |
| docker | 108239 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.094 MB | 26.094 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 108357 |  | 1 | n/a% | n/a% | n/a s | 19.125 MB | 19.125 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 108371 |  | 52 | 0.000% | 0.000% | 0.000 s | 25.664 MB | 25.664 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 108395 |  | 1 | n/a% | n/a% | n/a s | 25.859 MB | 25.859 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 108410 |  | 52 | 0.000% | 0.000% | 0.000 s | 26.859 MB | 26.859 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 108427 |  | 1 | n/a% | n/a% | n/a s | 9.188 MB | 9.188 MB | 1443.695 MB | 1443.695 MB | n/a MB | n/a MB |
| docker | 108479 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.633 MB | 25.633 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 108519 | andy_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.693 MB | 13.074 MB | 393.473 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 108542 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| tail | 108532 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 108605 |  | 1 | n/a% | n/a% | n/a s | 26.117 MB | 26.117 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 108643 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.816 MB | 25.816 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| run2:repair_bug | 108658 |  | 2 | 9.617% | 9.617% | 0.010 s | 351.131 MB | 676.129 MB | 2817.936 MB | 3975.660 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 108704 | alex_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.705 MB | 12.922 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 108764 |  | 1 | n/a% | n/a% | n/a s | 25.754 MB | 25.754 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 108743 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.672 MB | 1.672 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 108811 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.832 MB | 11.832 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 108791 |  | 1 | n/a% | n/a% | n/a s | 27.031 MB | 27.031 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 108829 |  | 1 | n/a% | n/a% | n/a s | 26.941 MB | 26.941 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| sh | 108848 | alex_0000 | 1 | n/a% | n/a% | n/a s | 1.625 MB | 1.625 MB | 2.617 MB | 2.617 MB | n/a MB | n/a MB |
| docker | 108870 |  | 1 | n/a% | n/a% | n/a s | 27.066 MB | 27.066 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 108924 |  | 1 | n/a% | n/a% | n/a s | 25.512 MB | 25.512 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 108973 | andy_0000 | 16 | 1.308% | 19.624% | 0.020 s | 1.323 MB | 11.676 MB | 99.112 MB | 1569.969 MB | n/a MB | n/a MB |
| docker | 108933 |  | 1 | n/a% | n/a% | n/a s | 25.375 MB | 25.375 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 108986 | andy_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.605 MB | 1.605 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 108998 |  | 1 | n/a% | n/a% | n/a s | 24.090 MB | 24.090 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 109045 | andy_0000 | 13 | 0.817% | 9.805% | 0.010 s | 4.037 MB | 11.938 MB | 130.398 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 109025 |  | 13 | 0.000% | 0.000% | 0.000 s | 27.301 MB | 27.301 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 109066 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.098 MB | 27.098 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 109055 | andy_0000 | 12 | 92.931% | 113.305% | 1.110 s | 32.512 MB | 42.137 MB | 39.327 MB | 51.238 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 109106 | alex_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.464 MB | 13.094 MB | 105.683 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 109130 |  | 1 | n/a% | n/a% | n/a s | 27.109 MB | 27.109 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 109148 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.691 MB | 11.691 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 109118 | alex_0000 | 14 | 0.000% | 0.000% | 0.000 s | 1.613 MB | 1.613 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 109176 | alex_0000 | 12 | 0.847% | 9.320% | 0.010 s | 4.056 MB | 11.973 MB | 128.877 MB | 1498.223 MB | n/a MB | n/a MB |
| docker | 109157 |  | 12 | 0.000% | 0.000% | 0.000 s | 26.977 MB | 26.977 MB | 1733.027 MB | 1733.027 MB | 0.000000 MB | 0.000000 MB |
| python | 109184 | alex_0000 | 11 | 97.943% | 107.044% | 1.040 s | 32.532 MB | 42.672 MB | 39.370 MB | 52.238 MB | n/a MB | n/a MB |
| docker | 109194 |  | 2 | 9.186% | 9.186% | 0.010 s | 22.123 MB | 25.887 MB | 1587.955 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 109255 |  | 2 | 9.806% | 9.806% | 0.010 s | 24.055 MB | 25.707 MB | 1624.207 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 109324 |  | 2 | 0.000% | 0.000% | 0.000 s | 24.758 MB | 25.535 MB | 1628.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 109326 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.217 MB | 26.895 MB | 1624.488 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 109403 | alex_0000 | 5 | 7.151% | 28.604% | 0.030 s | 2.830 MB | 11.617 MB | 314.786 MB | 1569.711 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 109410 | andy_0000 | 5 | 9.535% | 38.139% | 0.040 s | 2.785 MB | 11.395 MB | 329.184 MB | 1641.699 MB | n/a MB | n/a MB |
| docker | 109440 |  | 1 | n/a% | n/a% | n/a s | 23.809 MB | 23.809 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| tail | 109431 | andy_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| tail | 109423 | alex_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 109452 |  | 1 | n/a% | n/a% | n/a s | 27.109 MB | 27.109 MB | 1733.027 MB | 1733.027 MB | n/a MB | n/a MB |
| run2:repair_bug | 109558 |  | 1 | n/a% | n/a% | n/a s | 679.254 MB | 679.254 MB | 3975.660 MB | 3975.660 MB | n/a MB | n/a MB |
| docker | 109505 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 109612 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.816 MB | 11.816 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 109576 |  | 1 | n/a% | n/a% | n/a s | 27.156 MB | 27.156 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 109619 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.668 MB | 11.668 MB | 1498.223 MB | 1498.223 MB | n/a MB | n/a MB |
| docker | 109578 |  | 1 | n/a% | n/a% | n/a s | 27.379 MB | 27.379 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 109651 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.996 MB | 26.996 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 109650 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.891 MB | 25.891 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 109759 |  | 1 | n/a% | n/a% | n/a s | 20.125 MB | 20.125 MB | 1524.203 MB | 1524.203 MB | n/a MB | n/a MB |
| docker | 109783 |  | 55 | 0.000% | 0.000% | 0.000 s | 26.629 MB | 26.629 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 109799 |  | 1 | n/a% | n/a% | n/a s | 5.625 MB | 5.625 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 109816 |  | 1 | n/a% | n/a% | n/a s | 25.734 MB | 25.734 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 109825 |  | 54 | 0.000% | 0.000% | 0.000 s | 25.816 MB | 25.816 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 109857 |  | 1 | n/a% | n/a% | n/a s | 17.004 MB | 17.004 MB | 1451.699 MB | 1451.699 MB | n/a MB | n/a MB |
| python3 | 109872 |  | 5 | 97.684% | 108.531% | 0.400 s | 27.737 MB | 34.531 MB | 51.343 MB | 57.457 MB | 0.000000 MB | 0.246094 MB |
| docker | 109890 |  | 1 | n/a% | n/a% | n/a s | 25.973 MB | 25.973 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 109906 |  | 1 | n/a% | n/a% | n/a s | 15.707 MB | 15.707 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| python3 | 109913 |  | 4 | 98.879% | 98.986% | 0.300 s | 24.787 MB | 34.305 MB | 49.062 MB | 57.438 MB | 0.000000 MB | 0.226562 MB |
| docker | 109940 |  | 1 | n/a% | n/a% | n/a s | 16.465 MB | 16.465 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 109955 |  | 1 | n/a% | n/a% | n/a s | 11.051 MB | 11.051 MB | 1451.949 MB | 1451.949 MB | n/a MB | n/a MB |
| docker | 109979 |  | 1 | n/a% | n/a% | n/a s | 25.281 MB | 25.281 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 109987 |  | 1 | n/a% | n/a% | n/a s | 26.965 MB | 26.965 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 110001 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.211 MB | 27.352 MB | 1708.776 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 110042 | arch_0000 | 6 | 5.836% | 29.182% | 0.030 s | 2.510 MB | 11.898 MB | 250.561 MB | 1498.094 MB | n/a MB | n/a MB |
| tail | 110053 | arch_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 110056 |  | 1 | n/a% | n/a% | n/a s | 27.301 MB | 27.301 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 110091 |  | 1 | n/a% | n/a% | n/a s | 27.441 MB | 27.441 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 110159 | arch_0000 | 1 | n/a% | n/a% | n/a s | 1.996 MB | 1.996 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 110134 |  | 1 | n/a% | n/a% | n/a s | 27.684 MB | 27.684 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 110135 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.056 MB | 27.262 MB | 1709.026 MB | 1733.027 MB | 0.000000 MB | 0.000000 MB |
| docker | 110179 |  | 1 | n/a% | n/a% | n/a s | 27.293 MB | 27.293 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 110237 | bake_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.632 MB | 12.625 MB | 262.583 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 110258 |  | 2 | 9.632% | 9.632% | 0.010 s | 18.094 MB | 26.949 MB | 1456.234 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| tail | 110268 | bake_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| mkdir | 110306 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.215 MB | 0.215 MB | n/a MB | n/a MB |
| docker | 110272 |  | 1 | n/a% | n/a% | n/a s | 27.250 MB | 27.250 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 110374 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.594 MB | 11.594 MB | 1642.230 MB | 1642.230 MB | n/a MB | n/a MB |
| docker | 110389 |  | 3 | 0.000% | 0.000% | 0.000 s | 17.069 MB | 25.477 MB | 1116.997 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 110342 |  | 1 | n/a% | n/a% | n/a s | 27.004 MB | 27.004 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 110397 |  | 1 | n/a% | n/a% | n/a s | 27.430 MB | 27.430 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 110454 | arch_0000 | 6 | 7.490% | 37.452% | 0.040 s | 1.967 MB | 8.637 MB | 262.453 MB | 1569.445 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 110436 | bake_0000 | 1 | n/a% | n/a% | n/a s | 12.039 MB | 12.039 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 110497 | bake_0000 | 1 | n/a% | n/a% | n/a s | 3.930 MB | 3.930 MB | 1216.680 MB | 1216.680 MB | n/a MB | n/a MB |
| tail | 110495 | arch_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 110470 |  | 1 | n/a% | n/a% | n/a s | 27.473 MB | 27.473 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 110539 | arch_0000 | 1 | n/a% | n/a% | n/a s | 2.570 MB | 2.570 MB | 1111.484 MB | 1111.484 MB | n/a MB | n/a MB |
| docker | 110514 |  | 1 | n/a% | n/a% | n/a s | 27.371 MB | 27.371 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 110546 |  | 1 | n/a% | n/a% | n/a s | 26.023 MB | 26.023 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 110557 |  | 1 | n/a% | n/a% | n/a s | 27.391 MB | 27.391 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 110619 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 110636 |  | 1 | n/a% | n/a% | n/a s | 26.930 MB | 26.930 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| docker | 110638 |  | 1 | n/a% | n/a% | n/a s | 27.203 MB | 27.203 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 110674 | arch_0000 | 1 | n/a% | n/a% | n/a s | 12.246 MB | 12.246 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 110700 | bake_0000 | 5 | 7.105% | 28.419% | 0.030 s | 2.654 MB | 10.738 MB | 300.282 MB | 1497.191 MB | n/a MB | n/a MB |
| tail | 110734 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 110715 |  | 1 | n/a% | n/a% | n/a s | 25.828 MB | 25.828 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 110737 |  | 1 | n/a% | n/a% | n/a s | 23.527 MB | 23.527 MB | 1660.207 MB | 1660.207 MB | n/a MB | n/a MB |
| docker | 110766 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 110844 |  | 1 | n/a% | n/a% | n/a s | 19.938 MB | 19.938 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 110883 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.016 MB | 27.016 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 110951 |  | 1 | n/a% | n/a% | n/a s | 25.902 MB | 25.902 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 110965 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.742 MB | 26.742 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 111008 |  | 1 | n/a% | n/a% | n/a s | 25.539 MB | 25.539 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 111060 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 111048 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 111062 |  | 1 | n/a% | n/a% | n/a s | 25.328 MB | 25.328 MB | 1596.211 MB | 1596.211 MB | n/a MB | n/a MB |
| docker | 111098 |  | 1 | n/a% | n/a% | n/a s | 27.414 MB | 27.414 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 111152 | bake_0000 | 1 | n/a% | n/a% | n/a s | 1.941 MB | 1.941 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 111135 |  | 1 | n/a% | n/a% | n/a s | 27.469 MB | 27.469 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 111154 | bake_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 111176 |  | 1 | n/a% | n/a% | n/a s | 26.125 MB | 26.125 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 111226 |  | 1 | n/a% | n/a% | n/a s | 14.938 MB | 14.938 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 111256 |  | 49 | 0.000% | 0.000% | 0.000 s | 25.359 MB | 25.359 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 111271 |  | 2 | 19.651% | 19.651% | 0.020 s | 22.502 MB | 27.043 MB | 1588.361 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 111310 | bake_0000 | 18 | 2.239% | 38.067% | 0.040 s | 1.146 MB | 9.863 MB | 88.174 MB | 1569.195 MB | n/a MB | n/a MB |
| tail | 111324 | bake_0000 | 17 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 111334 |  | 1 | n/a% | n/a% | n/a s | 27.574 MB | 27.574 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 111353 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.195 MB | 11.195 MB | 1570.082 MB | 1570.082 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 111380 | bake_0000 | 14 | 1.451% | 18.868% | 0.020 s | 4.025 MB | 11.922 MB | 111.700 MB | 1506.727 MB | n/a MB | n/a MB |
| docker | 111360 |  | 14 | 0.000% | 0.000% | 0.000 s | 27.348 MB | 27.348 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 111389 | bake_0000 | 13 | 97.578% | 106.433% | 1.220 s | 31.537 MB | 40.910 MB | 38.580 MB | 50.375 MB | n/a MB | n/a MB |
| docker | 111391 |  | 1 | n/a% | n/a% | n/a s | 24.059 MB | 24.059 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 111400 |  | 1 | n/a% | n/a% | n/a s | 25.996 MB | 25.996 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 111435 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 111452 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.527 MB | 25.527 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 111493 | bake_0000 | 6 | 3.798% | 18.990% | 0.020 s | 2.607 MB | 12.480 MB | 262.625 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 111505 | bake_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 111515 |  | 1 | n/a% | n/a% | n/a s | 20.684 MB | 20.684 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 111543 |  | 1 | n/a% | n/a% | n/a s | 24.070 MB | 24.070 MB | 1596.211 MB | 1596.211 MB | n/a MB | n/a MB |
| docker | 111570 |  | 1 | n/a% | n/a% | n/a s | 14.062 MB | 14.062 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 111598 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.586 MB | 11.586 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 111578 |  | 1 | n/a% | n/a% | n/a s | 26.754 MB | 26.754 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 111614 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.141 MB | 26.141 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 111701 |  | 1 | n/a% | n/a% | n/a s | 7.512 MB | 7.512 MB | 32.867 MB | 32.867 MB | n/a MB | n/a MB |
| docker | 111703 |  | 1 | n/a% | n/a% | n/a s | 2.535 MB | 2.535 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 111733 |  | 1 | n/a% | n/a% | n/a s | 25.438 MB | 25.438 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 111719 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.684 MB | 26.684 MB | 1660.523 MB | 1660.523 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 111777 | arch_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.091 MB | 12.922 MB | 314.939 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 111775 |  | 49 | 0.000% | 0.000% | 0.000 s | 27.016 MB | 27.016 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 111806 |  | 1 | n/a% | n/a% | n/a s | 17.809 MB | 17.809 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| tail | 111795 | arch_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 111834 |  | 1 | n/a% | n/a% | n/a s | 26.809 MB | 26.809 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 111869 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 111907 |  | 1 | n/a% | n/a% | n/a s | 25.859 MB | 25.859 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 111949 |  | 1 | n/a% | n/a% | n/a s | 9.242 MB | 9.242 MB | 1443.695 MB | 1443.695 MB | n/a MB | n/a MB |
| docker | 111966 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.566 MB | 25.566 MB | 1627.961 MB | 1659.961 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 112005 | arch_0000 | 18 | 1.728% | 29.382% | 0.030 s | 1.175 MB | 10.387 MB | 88.201 MB | 1569.695 MB | n/a MB | n/a MB |
| tail | 112019 | arch_0000 | 17 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 112021 |  | 1 | n/a% | n/a% | n/a s | 1.512 MB | 1.512 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 112030 |  | 1 | n/a% | n/a% | n/a s | 27.613 MB | 27.613 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 112049 | arch_0000 | 1 | n/a% | n/a% | n/a s | 11.676 MB | 11.676 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| bash | 112076 | arch_0000 | 14 | 0.752% | 9.771% | 0.010 s | 3.459 MB | 3.469 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 112056 |  | 14 | 0.000% | 0.000% | 0.000 s | 27.227 MB | 27.227 MB | 1661.023 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| python | 112085 | arch_0000 | 13 | 96.423% | 105.492% | 1.220 s | 33.330 MB | 42.738 MB | 40.643 MB | 52.219 MB | n/a MB | n/a MB |
| docker | 112095 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.000 MB | 26.000 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 112163 |  | 1 | n/a% | n/a% | n/a s | 24.488 MB | 24.488 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| python3 | 112178 |  | 4 | 95.529% | 98.910% | 0.290 s | 24.675 MB | 34.488 MB | 48.658 MB | 57.457 MB | 0.000000 MB | 0.246094 MB |
| docker | 112191 |  | 1 | n/a% | n/a% | n/a s | 20.414 MB | 20.414 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 112229 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.986 MB | 27.238 MB | 1696.775 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| tail | 112282 | bale_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.809 MB | 1.809 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 112269 | bale_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 112284 |  | 1 | n/a% | n/a% | n/a s | 24.133 MB | 24.133 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 112321 |  | 1 | n/a% | n/a% | n/a s | 27.375 MB | 27.375 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 112367 |  | 1 | n/a% | n/a% | n/a s | 27.516 MB | 27.516 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 112404 |  | 1 | n/a% | n/a% | n/a s | 27.219 MB | 27.219 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 112423 | bale_0000 | 1 | n/a% | n/a% | n/a s | 11.398 MB | 11.398 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 112440 |  | 1 | n/a% | n/a% | n/a s | 27.129 MB | 27.129 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 112491 |  | 1 | n/a% | n/a% | n/a s | 13.969 MB | 13.969 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 112538 | bale_0000 | 4 | 6.445% | 19.336% | 0.020 s | 2.967 MB | 10.086 MB | 393.090 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 112499 |  | 1 | n/a% | n/a% | n/a s | 25.371 MB | 25.371 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 112561 |  | 1 | n/a% | n/a% | n/a s | 26.020 MB | 26.020 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 112551 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 112587 |  | 1 | n/a% | n/a% | n/a s | 27.395 MB | 27.395 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 112605 | bale_0000 | 1 | n/a% | n/a% | n/a s | 11.410 MB | 11.410 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 112649 |  | 1 | n/a% | n/a% | n/a s | 2.062 MB | 2.062 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 112657 |  | 1 | n/a% | n/a% | n/a s | 25.875 MB | 25.875 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 112733 |  | 40 | 0.000% | 0.000% | 0.000 s | 25.240 MB | 25.848 MB | 1619.525 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 112749 |  | 1 | n/a% | n/a% | n/a s | 26.676 MB | 26.676 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 112773 |  | 1 | n/a% | n/a% | n/a s | 23.594 MB | 23.594 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| python3 | 112781 |  | 4 | 98.830% | 98.955% | 0.300 s | 28.366 MB | 34.773 MB | 51.818 MB | 57.438 MB | 0.000000 MB | 0.246094 MB |
| docker | 112800 |  | 1 | n/a% | n/a% | n/a s | 20.230 MB | 20.230 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 112833 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.408 MB | 27.551 MB | 1708.776 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| tail | 112885 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 112873 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 112923 |  | 1 | n/a% | n/a% | n/a s | 8.477 MB | 8.477 MB | 106.242 MB | 106.242 MB | n/a MB | n/a MB |
| docker | 112950 |  | 1 | n/a% | n/a% | n/a s | 27.371 MB | 27.371 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 112971 | band_0000 | 1 | n/a% | n/a% | n/a s | 10.816 MB | 10.816 MB | 1569.711 MB | 1569.711 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 113006 | band_0000 | 1 | n/a% | n/a% | n/a s | 12.375 MB | 12.375 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 112986 |  | 1 | n/a% | n/a% | n/a s | 27.328 MB | 27.328 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 113022 |  | 1 | n/a% | n/a% | n/a s | 27.148 MB | 27.148 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 113071 |  | 1 | n/a% | n/a% | n/a s | 13.910 MB | 13.910 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 113119 | band_0000 | 4 | 3.257% | 9.772% | 0.010 s | 3.492 MB | 12.070 MB | 393.315 MB | 1570.098 MB | n/a MB | n/a MB |
| docker | 113079 |  | 1 | n/a% | n/a% | n/a s | 25.512 MB | 25.512 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 113141 |  | 1 | n/a% | n/a% | n/a s | 27.059 MB | 27.059 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 113131 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 113168 |  | 1 | n/a% | n/a% | n/a s | 27.270 MB | 27.270 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| sh | 113187 | band_0000 | 1 | n/a% | n/a% | n/a s | 0.129 MB | 0.129 MB | 2.484 MB | 2.484 MB | n/a MB | n/a MB |
| docker | 113232 |  | 1 | n/a% | n/a% | n/a s | 15.992 MB | 15.992 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 113240 |  | 1 | n/a% | n/a% | n/a s | 25.977 MB | 25.977 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 113293 |  | 1 | n/a% | n/a% | n/a s | 23.371 MB | 23.371 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 113324 |  | 57 | 0.170% | 9.503% | 0.010 s | 26.383 MB | 26.465 MB | 1730.241 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 113345 |  | 1 | n/a% | n/a% | n/a s | 25.875 MB | 25.875 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 113371 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.555 MB | 26.555 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 113410 | bale_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.721 MB | 12.984 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 113432 |  | 1 | n/a% | n/a% | n/a s | 27.215 MB | 27.215 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 113422 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 113452 | bale_0000 | 1 | n/a% | n/a% | n/a s | 11.879 MB | 11.879 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 113488 |  | 1 | n/a% | n/a% | n/a s | 25.203 MB | 25.203 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 113536 |  | 2 | 0.000% | 0.000% | 0.000 s | 13.842 MB | 25.926 MB | 846.486 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 113596 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.031 MB | 27.031 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 113637 | bale_0000 | 38 | 0.000% | 0.000% | 0.000 s | 0.953 MB | 12.793 MB | 42.349 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 113650 | bale_0000 | 37 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 113679 | bale_0000 | 1 | n/a% | n/a% | n/a s | 11.941 MB | 11.941 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 113660 |  | 1 | n/a% | n/a% | n/a s | 27.078 MB | 27.078 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 113686 |  | 35 | 0.577% | 19.623% | 0.020 s | 27.512 MB | 27.512 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| bash | 113705 | bale_0000 | 35 | 0.000% | 0.000% | 0.000 s | 3.355 MB | 3.355 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 113715 | bale_0000 | 35 | 100.090% | 108.017% | 3.470 s | 38.833 MB | 41.266 MB | 48.259 MB | 51.324 MB | n/a MB | n/a MB |
| docker | 113725 |  | 2 | 0.000% | 0.000% | 0.000 s | 16.893 MB | 25.777 MB | 846.539 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 113786 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.637 MB | 25.637 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 113827 | bale_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.708 MB | 12.934 MB | 411.349 MB | 1642.230 MB | n/a MB | n/a MB |
| tail | 113840 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 113871 | bale_0000 | 1 | n/a% | n/a% | n/a s | 12.375 MB | 12.375 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 113851 |  | 1 | n/a% | n/a% | n/a s | 27.176 MB | 27.176 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 113915 |  | 1 | n/a% | n/a% | n/a s | 20.191 MB | 20.191 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 113955 |  | 1 | n/a% | n/a% | n/a s | 26.168 MB | 26.168 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 113995 |  | 1 | n/a% | n/a% | n/a s | 5.781 MB | 5.781 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 114036 |  | 44 | 0.000% | 0.000% | 0.000 s | 25.449 MB | 25.918 MB | 1623.223 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 114044 |  | 1 | n/a% | n/a% | n/a s | 8.992 MB | 8.992 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 114069 |  | 1 | n/a% | n/a% | n/a s | 18.945 MB | 18.945 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 114077 |  | 44 | 0.000% | 0.000% | 0.000 s | 26.633 MB | 26.633 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 114103 |  | 1 | n/a% | n/a% | n/a s | 17.598 MB | 17.598 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 114137 |  | 1 | n/a% | n/a% | n/a s | 26.027 MB | 26.027 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| python3 | 114152 |  | 28 | 96.266% | 108.910% | 2.670 s | 32.779 MB | 34.539 MB | 56.497 MB | 57.461 MB | 0.000000 MB | 0.246094 MB |
| docker | 114162 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.621 MB | 25.621 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 114201 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.627 MB | 12.609 MB | 375.347 MB | 1498.223 MB | n/a MB | n/a MB |
| tail | 114214 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 114225 |  | 1 | n/a% | n/a% | n/a s | 27.195 MB | 27.195 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 114243 | band_0000 | 1 | n/a% | n/a% | n/a s | 7.281 MB | 7.281 MB | 1569.195 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 114250 |  | 1 | n/a% | n/a% | n/a s | 26.996 MB | 26.996 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 114306 | band_0000 | 1 | n/a% | n/a% | n/a s | 12.449 MB | 12.449 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 114285 |  | 1 | n/a% | n/a% | n/a s | 27.348 MB | 27.348 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 114325 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.996 MB | 26.996 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 114385 |  | 1 | n/a% | n/a% | n/a s | 22.750 MB | 22.750 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 114422 |  | 2 | 0.000% | 0.000% | 0.000 s | 18.078 MB | 25.727 MB | 1524.080 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 114462 | band_0000 | 11 | 0.976% | 9.759% | 0.010 s | 1.748 MB | 12.898 MB | 150.275 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 114485 |  | 1 | n/a% | n/a% | n/a s | 27.441 MB | 27.441 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 114505 | band_0000 | 1 | n/a% | n/a% | n/a s | 10.590 MB | 10.590 MB | 1569.453 MB | 1569.453 MB | n/a MB | n/a MB |
| tail | 114475 | band_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| python | 114544 | band_0000 | 8 | 99.458% | 107.974% | 0.710 s | 29.539 MB | 41.828 MB | 36.250 MB | 51.324 MB | n/a MB | n/a MB |
| bash | 114534 | band_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.324 MB | 3.324 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 114514 |  | 8 | 0.000% | 0.000% | 0.000 s | 26.988 MB | 26.988 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 114546 |  | 1 | n/a% | n/a% | n/a s | 11.027 MB | 11.027 MB | 1387.949 MB | 1387.949 MB | n/a MB | n/a MB |
| docker | 114554 |  | 1 | n/a% | n/a% | n/a s | 26.027 MB | 26.027 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 114620 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.326 MB | 27.668 MB | 1732.777 MB | 1804.781 MB | 0.000000 MB | 0.000000 MB |
| docker | 114679 |  | 1 | n/a% | n/a% | n/a s | 27.320 MB | 27.320 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 114677 | bart_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 114663 | bart_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 114714 |  | 1 | n/a% | n/a% | n/a s | 27.129 MB | 27.129 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 114733 | bart_0000 | 1 | n/a% | n/a% | n/a s | 10.816 MB | 10.816 MB | 1641.578 MB | 1641.578 MB | n/a MB | n/a MB |
| docker | 114769 |  | 1 | n/a% | n/a% | n/a s | 19.574 MB | 19.574 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 114813 |  | 2 | 0.000% | 0.000% | 0.000 s | 20.895 MB | 26.883 MB | 1588.236 MB | 1660.523 MB | 0.000000 MB | 0.000000 MB |
| docker | 114870 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.535 MB | 26.535 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 114911 | bart_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.656 MB | 12.727 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 114934 |  | 1 | n/a% | n/a% | n/a s | 27.180 MB | 27.180 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| tail | 114923 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 114954 | bart_0000 | 1 | n/a% | n/a% | n/a s | 11.578 MB | 11.578 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 114996 |  | 1 | n/a% | n/a% | n/a s | 6.523 MB | 6.523 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 115033 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.711 MB | 26.711 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 115091 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.023 MB | 26.023 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 115131 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.475 MB | 0.633 MB | 1.021 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 115145 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 115155 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 115218 |  | 1 | n/a% | n/a% | n/a s | 25.363 MB | 25.363 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 115254 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.000 MB | 26.000 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 115312 |  | 1 | n/a% | n/a% | n/a s | 23.172 MB | 23.172 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 115336 |  | 40 | 0.000% | 0.000% | 0.000 s | 26.637 MB | 26.637 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 115368 |  | 1 | n/a% | n/a% | n/a s | 25.344 MB | 25.344 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| python3 | 115383 |  | 4 | 98.740% | 98.908% | 0.300 s | 25.848 MB | 34.430 MB | 50.024 MB | 57.438 MB | 0.000000 MB | 0.242188 MB |
| docker | 115435 |  | 2 | 9.872% | 9.872% | 0.010 s | 27.377 MB | 27.688 MB | 1696.775 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 115476 | base_0000 | 5 | 4.926% | 19.704% | 0.020 s | 2.709 MB | 11.016 MB | 314.683 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 115490 |  | 1 | n/a% | n/a% | n/a s | 27.141 MB | 27.141 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 115488 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 115510 |  | 1 | n/a% | n/a% | n/a s | 10.246 MB | 10.246 MB | 1569.695 MB | 1569.695 MB | n/a MB | n/a MB |
| docker | 115526 |  | 1 | n/a% | n/a% | n/a s | 27.164 MB | 27.164 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 115545 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.773 MB | 11.773 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 115589 |  | 1 | n/a% | n/a% | n/a s | 2.410 MB | 2.410 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 115626 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.941 MB | 25.941 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 115684 |  | 1 | n/a% | n/a% | n/a s | 26.590 MB | 26.590 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker-init | 115722 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 115736 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 115738 |  | 1 | n/a% | n/a% | n/a s | 15.590 MB | 15.590 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 115774 |  | 1 | n/a% | n/a% | n/a s | 27.234 MB | 27.234 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 115808 |  | 1 | n/a% | n/a% | n/a s | 27.242 MB | 27.242 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 115828 | base_0000 | 1 | n/a% | n/a% | n/a s | 10.938 MB | 10.938 MB | 1641.578 MB | 1641.578 MB | n/a MB | n/a MB |
| docker | 115847 |  | 1 | n/a% | n/a% | n/a s | 26.941 MB | 26.941 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| docker | 115889 |  | 1 | n/a% | n/a% | n/a s | 19.090 MB | 19.090 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 115906 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.027 MB | 27.027 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 115947 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 4.686 MB | 12.793 MB | 524.112 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 115970 |  | 1 | n/a% | n/a% | n/a s | 27.281 MB | 27.281 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 115960 | base_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.832 MB | 1.832 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| run13:diagnose_ | 116031 |  | 1 | n/a% | n/a% | n/a s | 695.254 MB | 695.254 MB | 3971.336 MB | 3971.336 MB | n/a MB | n/a MB |
| docker | 116039 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.969 MB | 26.969 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 116080 |  | 1 | n/a% | n/a% | n/a s | 21.836 MB | 21.836 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 116097 |  | 1 | n/a% | n/a% | n/a s | 26.777 MB | 26.777 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 116136 | base_0000 | 4 | 3.269% | 9.806% | 0.010 s | 3.577 MB | 12.410 MB | 393.535 MB | 1570.977 MB | n/a MB | n/a MB |
| docker | 116159 |  | 1 | n/a% | n/a% | n/a s | 27.195 MB | 27.195 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 116149 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 116252 |  | 1 | n/a% | n/a% | n/a s | 23.895 MB | 23.895 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 116261 |  | 1 | n/a% | n/a% | n/a s | 25.977 MB | 25.977 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 116320 |  | 1 | n/a% | n/a% | n/a s | 24.371 MB | 24.371 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 116342 |  | 39 | 0.000% | 0.000% | 0.000 s | 26.281 MB | 26.281 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| run12:diagnose_ | 116366 |  | 1 | n/a% | n/a% | n/a s | 695.879 MB | 695.879 MB | 3972.336 MB | 3972.336 MB | n/a MB | n/a MB |
| docker | 116376 |  | 1 | n/a% | n/a% | n/a s | 23.660 MB | 23.660 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 116423 | bart_0000 | 4 | 3.265% | 9.796% | 0.010 s | 3.562 MB | 12.348 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 116384 |  | 1 | n/a% | n/a% | n/a s | 25.773 MB | 25.773 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 116446 |  | 1 | n/a% | n/a% | n/a s | 27.277 MB | 27.277 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 116435 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.711 MB | 1.711 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| sh | 116490 | bart_0000 | 1 | n/a% | n/a% | n/a s | 1.582 MB | 1.582 MB | 2.617 MB | 2.617 MB | n/a MB | n/a MB |
| docker | 116470 |  | 1 | n/a% | n/a% | n/a s | 27.621 MB | 27.621 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 116539 |  | 1 | n/a% | n/a% | n/a s | 3.664 MB | 3.664 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 116547 |  | 1 | n/a% | n/a% | n/a s | 27.070 MB | 27.070 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 116648 | bart_0000 | 11 | 1.927% | 19.272% | 0.020 s | 1.382 MB | 8.875 MB | 143.613 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 116607 |  | 1 | n/a% | n/a% | n/a s | 25.793 MB | 25.793 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 116671 |  | 1 | n/a% | n/a% | n/a s | 16.438 MB | 16.438 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 116661 | bart_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.672 MB | 1.672 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 116701 |  | 9 | 0.000% | 0.000% | 0.000 s | 26.980 MB | 26.980 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 116721 | bart_0000 | 9 | 2.427% | 19.412% | 0.020 s | 4.160 MB | 10.812 MB | 178.300 MB | 1569.574 MB | n/a MB | n/a MB |
| python | 116730 | bart_0000 | 8 | 99.266% | 107.825% | 0.710 s | 33.281 MB | 41.965 MB | 40.536 MB | 52.289 MB | n/a MB | n/a MB |
| docker | 116741 |  | 1 | n/a% | n/a% | n/a s | 26.934 MB | 26.934 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 116800 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.734 MB | 25.734 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 116840 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 116852 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 116889 |  | 1 | n/a% | n/a% | n/a s | 18.102 MB | 18.102 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 116924 |  | 1 | n/a% | n/a% | n/a s | 27.055 MB | 27.055 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 116961 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.055 MB | 26.055 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 117015 |  | 1 | n/a% | n/a% | n/a s | 2.273 MB | 2.273 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 117039 |  | 1 | n/a% | n/a% | n/a s | 25.746 MB | 25.746 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 117047 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.633 MB | 25.633 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 117063 |  | 1 | n/a% | n/a% | n/a s | 25.828 MB | 25.828 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 117089 |  | 1 | n/a% | n/a% | n/a s | 26.703 MB | 26.703 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 117096 |  | 4 | 102.119% | 108.840% | 0.310 s | 28.589 MB | 34.617 MB | 52.136 MB | 57.438 MB | 0.000000 MB | 0.242188 MB |
| docker | 117114 |  | 1 | n/a% | n/a% | n/a s | 27.367 MB | 27.367 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 117147 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.318 MB | 27.469 MB | 1697.025 MB | 1733.027 MB | 0.000000 MB | 0.000000 MB |
| tail | 117199 | beam_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 117202 |  | 1 | n/a% | n/a% | n/a s | 17.285 MB | 17.285 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker-init | 117187 | beam_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 117238 |  | 1 | n/a% | n/a% | n/a s | 27.219 MB | 27.219 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 117285 | beam_0000 | 1 | n/a% | n/a% | n/a s | 12.371 MB | 12.371 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 117265 |  | 1 | n/a% | n/a% | n/a s | 27.332 MB | 27.332 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 117329 |  | 1 | n/a% | n/a% | n/a s | 3.719 MB | 3.719 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 117337 |  | 1 | n/a% | n/a% | n/a s | 27.023 MB | 27.023 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 117395 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.129 MB | 27.129 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 117435 | beam_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.728 MB | 13.012 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 117447 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 117457 |  | 1 | n/a% | n/a% | n/a s | 27.207 MB | 27.207 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 117519 |  | 1 | n/a% | n/a% | n/a s | 24.059 MB | 24.059 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 117558 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.867 MB | 26.867 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 117627 |  | 1 | n/a% | n/a% | n/a s | 26.863 MB | 26.863 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 117641 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.816 MB | 26.816 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 117684 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.336 MB | 25.336 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| tail | 117737 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.777 MB | 1.777 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 117724 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 117776 |  | 1 | n/a% | n/a% | n/a s | 15.660 MB | 15.660 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 117812 |  | 1 | n/a% | n/a% | n/a s | 27.617 MB | 27.617 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 117850 |  | 1 | n/a% | n/a% | n/a s | 26.840 MB | 26.840 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 117895 |  | 1 | n/a% | n/a% | n/a s | 19.098 MB | 19.098 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 117934 |  | 55 | 0.000% | 0.000% | 0.000 s | 25.675 MB | 25.766 MB | 1657.588 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 117951 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.344 MB | 25.344 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 117990 | base_0000 | 291 | 0.066% | 19.092% | 0.020 s | 0.672 MB | 12.074 MB | 6.446 MB | 1569.977 MB | n/a MB | n/a MB |
| docker | 118005 |  | 1 | n/a% | n/a% | n/a s | 20.051 MB | 20.051 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 118003 | base_0000 | 290 | 0.000% | 0.000% | 0.000 s | 1.711 MB | 1.711 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 118032 | base_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| docker | 118013 |  | 1 | n/a% | n/a% | n/a s | 27.375 MB | 27.375 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 118040 |  | 287 | 0.000% | 0.000% | 0.000 s | 27.492 MB | 27.492 MB | 1661.023 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| python | 118069 | base_0000 | 288 | 97.995% | 116.044% | 29.320 s | 40.169 MB | 40.531 MB | 49.577 MB | 50.027 MB | n/a MB | n/a MB |
| bash | 118060 | base_0000 | 288 | 0.000% | 0.000% | 0.000 s | 3.383 MB | 3.383 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 118079 |  | 1 | n/a% | n/a% | n/a s | 20.707 MB | 20.707 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 118106 |  | 3 | 0.000% | 0.000% | 0.000 s | 25.605 MB | 25.605 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 118147 | beam_0000 | 5 | 9.280% | 27.440% | 0.040 s | 5.181 MB | 13.059 MB | 628.617 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 118176 |  | 1 | n/a% | n/a% | n/a s | 27.453 MB | 27.453 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 118165 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.809 MB | 1.809 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 118220 | beam_0000 | 1 | n/a% | n/a% | n/a s | 10.410 MB | 10.410 MB | 1497.320 MB | 1497.320 MB | n/a MB | n/a MB |
| docker | 118202 |  | 1 | n/a% | n/a% | n/a s | 27.199 MB | 27.199 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 118236 |  | 1 | n/a% | n/a% | n/a s | 27.379 MB | 27.379 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 118254 | beam_0000 | 1 | n/a% | n/a% | n/a s | 1.949 MB | 1.949 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 118256 | beam_0000 | 1 | n/a% | n/a% | n/a s | 2.062 MB | 2.062 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 118274 |  | 1 | n/a% | n/a% | n/a s | 26.883 MB | 26.883 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 118317 |  | 1 | n/a% | n/a% | n/a s | 16.199 MB | 16.199 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 118336 |  | 2 | 9.785% | 9.785% | 0.010 s | 24.361 MB | 25.668 MB | 1624.207 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 118380 | beam_0000 | 15 | 1.357% | 9.552% | 0.020 s | 1.408 MB | 12.266 MB | 105.666 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 118392 | beam_0000 | 14 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 118402 |  | 1 | n/a% | n/a% | n/a s | 25.633 MB | 25.633 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 118428 |  | 12 | 0.000% | 0.000% | 0.000 s | 27.191 MB | 27.191 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| bash | 118445 | beam_0000 | 11 | 0.000% | 0.000% | 0.000 s | 3.426 MB | 3.426 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 118454 | beam_0000 | 11 | 99.650% | 112.622% | 1.070 s | 31.847 MB | 41.746 MB | 38.780 MB | 51.238 MB | n/a MB | n/a MB |
| docker | 118457 |  | 1 | n/a% | n/a% | n/a s | 3.031 MB | 3.031 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 118465 |  | 1 | n/a% | n/a% | n/a s | 25.859 MB | 25.859 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 118525 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.344 MB | 25.344 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 118562 | beam_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.475 MB | 0.633 MB | 1.021 MB | 1.055 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 118603 | beam_0000 | 1 | n/a% | n/a% | n/a s | 11.520 MB | 11.520 MB | 1498.223 MB | 1498.223 MB | n/a MB | n/a MB |
| docker | 118585 |  | 1 | n/a% | n/a% | n/a s | 27.430 MB | 27.430 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 118574 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 118609 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 118644 |  | 1 | n/a% | n/a% | n/a s | 27.277 MB | 27.277 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 118664 | beam_0000 | 1 | n/a% | n/a% | n/a s | 12.004 MB | 12.004 MB | 1498.223 MB | 1498.223 MB | n/a MB | n/a MB |
| docker | 118681 |  | 1 | n/a% | n/a% | n/a s | 26.195 MB | 26.195 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 118723 |  | 1 | n/a% | n/a% | n/a s | 23.316 MB | 23.316 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 118749 |  | 1 | n/a% | n/a% | n/a s | 26.387 MB | 26.387 MB | 1732.277 MB | 1732.277 MB | n/a MB | n/a MB |
| docker | 118766 |  | 55 | 0.000% | 0.000% | 0.000 s | 25.621 MB | 25.621 MB | 1588.207 MB | 1588.207 MB | 0.000000 MB | 0.000000 MB |
| docker | 118782 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 30.570 MB | 30.570 MB | n/a MB | n/a MB |
| docker | 118798 |  | 1 | n/a% | n/a% | n/a s | 25.633 MB | 25.633 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| python3 | 118813 |  | 6 | 96.570% | 105.750% | 0.500 s | 24.465 MB | 34.695 MB | 48.740 MB | 57.438 MB | 0.000000 MB | 0.242188 MB |
| docker | 118818 |  | 1 | n/a% | n/a% | n/a s | 23.855 MB | 23.855 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 118843 |  | 1 | n/a% | n/a% | n/a s | 20.121 MB | 20.121 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 118861 |  | 2 | 0.000% | 0.000% | 0.000 s | 17.641 MB | 26.000 MB | 1551.953 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 118913 |  | 1 | n/a% | n/a% | n/a s | 13.395 MB | 13.395 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 118961 | base_0000 | 4 | 9.781% | 29.343% | 0.030 s | 3.053 MB | 10.312 MB | 393.090 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 118921 |  | 1 | n/a% | n/a% | n/a s | 26.930 MB | 26.930 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 118984 |  | 1 | n/a% | n/a% | n/a s | 17.297 MB | 17.297 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 118974 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.809 MB | 1.809 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 119031 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.176 MB | 11.176 MB | 1641.965 MB | 1641.965 MB | n/a MB | n/a MB |
| docker | 119012 |  | 1 | n/a% | n/a% | n/a s | 27.188 MB | 27.188 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 119048 |  | 1 | n/a% | n/a% | n/a s | 27.258 MB | 27.258 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| sh | 119068 | base_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.516 MB | 0.516 MB | n/a MB | n/a MB |
| docker | 119085 |  | 1 | n/a% | n/a% | n/a s | 25.805 MB | 25.805 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 119135 |  | 1 | n/a% | n/a% | n/a s | 26.645 MB | 26.645 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 119150 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.312 MB | 27.312 MB | 1804.781 MB | 1804.781 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 119192 | bear_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.753 MB | 13.113 MB | 393.473 MB | 1570.727 MB | n/a MB | n/a MB |
| tail | 119204 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 119234 |  | 1 | n/a% | n/a% | n/a s | 25.848 MB | 25.848 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 119290 | bear_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 119270 |  | 1 | n/a% | n/a% | n/a s | 27.129 MB | 27.129 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 119287 | bear_0000 | 1 | n/a% | n/a% | n/a s | 1.945 MB | 1.945 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 119307 |  | 1 | n/a% | n/a% | n/a s | 27.281 MB | 27.281 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 119327 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.508 MB | 11.508 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 119344 |  | 1 | n/a% | n/a% | n/a s | 26.547 MB | 26.547 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 119394 |  | 1 | n/a% | n/a% | n/a s | 1.082 MB | 1.082 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 119402 |  | 1 | n/a% | n/a% | n/a s | 25.691 MB | 25.691 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 119443 | bear_0000 | 4 | 3.260% | 9.779% | 0.010 s | 3.488 MB | 12.055 MB | 411.439 MB | 1642.594 MB | n/a MB | n/a MB |
| docker | 119469 |  | 1 | n/a% | n/a% | n/a s | 26.531 MB | 26.531 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| tail | 119457 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 119496 |  | 1 | n/a% | n/a% | n/a s | 27.281 MB | 27.281 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 119516 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.875 MB | 11.875 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 119567 |  | 1 | n/a% | n/a% | n/a s | 26.926 MB | 26.926 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 119628 |  | 1 | n/a% | n/a% | n/a s | 25.637 MB | 25.637 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 119680 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.684 MB | 1.684 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 119682 |  | 1 | n/a% | n/a% | n/a s | 8.719 MB | 8.719 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker-init | 119667 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 119718 |  | 1 | n/a% | n/a% | n/a s | 27.004 MB | 27.004 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 119761 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.984 MB | 26.984 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 119820 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.699 MB | 25.699 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 119859 | bear_0000 | 3 | 4.881% | 9.761% | 0.010 s | 4.587 MB | 12.496 MB | 500.111 MB | 1498.223 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 119902 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.938 MB | 11.938 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 119882 |  | 1 | n/a% | n/a% | n/a s | 27.430 MB | 27.430 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 119871 | bear_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 119943 |  | 1 | n/a% | n/a% | n/a s | 26.176 MB | 26.176 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 119951 |  | 1 | n/a% | n/a% | n/a s | 27.070 MB | 27.070 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 120010 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.938 MB | 26.938 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 120050 | bear_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.712 MB | 12.949 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 120062 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 120094 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.641 MB | 11.641 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 120072 |  | 1 | n/a% | n/a% | n/a s | 27.371 MB | 27.371 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 120130 |  | 1 | n/a% | n/a% | n/a s | 25.094 MB | 25.094 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 120175 |  | 2 | 9.783% | 9.783% | 0.010 s | 18.117 MB | 26.992 MB | 1452.232 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 120236 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.637 MB | 26.637 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 120276 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.672 MB | 12.789 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 120289 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 120300 |  | 1 | n/a% | n/a% | n/a s | 27.281 MB | 27.281 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 120365 |  | 1 | n/a% | n/a% | n/a s | 16.207 MB | 16.207 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 120403 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.129 MB | 27.129 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 120463 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.465 MB | 25.465 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 120502 | base_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.392 MB | 12.949 MB | 225.294 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 120527 |  | 1 | n/a% | n/a% | n/a s | 27.164 MB | 27.164 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 120546 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.473 MB | 11.473 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 120516 | base_0000 | 6 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 120553 |  | 4 | 0.000% | 0.000% | 0.000 s | 27.547 MB | 27.547 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 120581 | base_0000 | 4 | 100.899% | 106.710% | 0.310 s | 22.961 MB | 34.645 MB | 28.985 MB | 45.023 MB | n/a MB | n/a MB |
| bash | 120572 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.426 MB | 3.426 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 120583 |  | 1 | n/a% | n/a% | n/a s | 18.652 MB | 18.652 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 120592 |  | 1 | n/a% | n/a% | n/a s | 25.699 MB | 25.699 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 120652 |  | 1 | n/a% | n/a% | n/a s | 26.414 MB | 26.414 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 120693 | base_0000 | 4 | 9.466% | 28.397% | 0.030 s | 3.067 MB | 10.371 MB | 375.214 MB | 1497.691 MB | n/a MB | n/a MB |
| docker | 120715 |  | 1 | n/a% | n/a% | n/a s | 16.574 MB | 16.574 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 120705 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 120742 |  | 1 | n/a% | n/a% | n/a s | 27.328 MB | 27.328 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 120762 | base_0000 | 1 | n/a% | n/a% | n/a s | 10.879 MB | 10.879 MB | 1641.707 MB | 1641.707 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 120798 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.891 MB | 11.891 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 120778 |  | 1 | n/a% | n/a% | n/a s | 27.430 MB | 27.430 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 120814 |  | 1 | n/a% | n/a% | n/a s | 26.023 MB | 26.023 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 120890 |  | 1 | n/a% | n/a% | n/a s | 25.348 MB | 25.348 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 120898 |  | 52 | 0.000% | 0.000% | 0.000 s | 26.805 MB | 26.805 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 120922 |  | 1 | n/a% | n/a% | n/a s | 1.656 MB | 1.656 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 120936 |  | 53 | 0.000% | 0.000% | 0.000 s | 27.121 MB | 27.121 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 120953 |  | 1 | n/a% | n/a% | n/a s | 13.793 MB | 13.793 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 120969 |  | 1 | n/a% | n/a% | n/a s | 25.918 MB | 25.918 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| python3 | 120985 |  | 5 | 98.779% | 101.765% | 0.410 s | 26.860 MB | 34.555 MB | 50.518 MB | 57.441 MB | 0.011719 MB | 0.226562 MB |
| docker | 120995 |  | 1 | n/a% | n/a% | n/a s | 26.832 MB | 26.832 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 121026 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.129 MB | 27.129 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| tail | 121079 | bear_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 121066 | bear_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 121115 |  | 1 | n/a% | n/a% | n/a s | 3.844 MB | 3.844 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 121151 |  | 1 | n/a% | n/a% | n/a s | 26.879 MB | 26.879 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 121189 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.930 MB | 26.930 MB | 1660.523 MB | 1660.523 MB | 0.000000 MB | 0.000000 MB |
| docker | 121240 |  | 1 | n/a% | n/a% | n/a s | 23.277 MB | 23.277 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 121248 |  | 1 | n/a% | n/a% | n/a s | 25.914 MB | 25.914 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 121287 | bear_0000 | 16 | 1.303% | 19.551% | 0.020 s | 1.351 MB | 12.121 MB | 103.628 MB | 1642.230 MB | n/a MB | n/a MB |
| docker | 121328 |  | 3 | 9.240% | 18.480% | 0.020 s | 24.876 MB | 27.855 MB | 1756.507 MB | 1876.785 MB | 0.000000 MB | 0.000000 MB |
| docker | 121330 |  | 1 | n/a% | n/a% | n/a s | 20.297 MB | 20.297 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| tail | 121303 | bear_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 121363 |  | 13 | 0.000% | 0.000% | 0.000 s | 27.160 MB | 27.230 MB | 1660.735 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 121429 | bear_0000 | 12 | 91.921% | 120.747% | 1.170 s | 31.628 MB | 41.738 MB | 38.969 MB | 51.340 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 121426 | beef_0000 | 6 | 3.506% | 17.528% | 0.020 s | 2.538 MB | 12.062 MB | 250.583 MB | 1498.223 MB | n/a MB | n/a MB |
| bash | 121386 | bear_0000 | 12 | 0.000% | 0.000% | 0.000 s | 3.281 MB | 3.281 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| tail | 121441 | beef_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 121462 |  | 1 | n/a% | n/a% | n/a s | 1.996 MB | 1.996 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 121443 |  | 1 | n/a% | n/a% | n/a s | 27.312 MB | 27.312 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 121480 |  | 1 | n/a% | n/a% | n/a s | 27.016 MB | 27.016 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 121505 |  | 1 | n/a% | n/a% | n/a s | 27.398 MB | 27.398 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 121524 | beef_0000 | 1 | n/a% | n/a% | n/a s | 11.148 MB | 11.148 MB | 1569.703 MB | 1569.703 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 121560 | beef_0000 | 1 | n/a% | n/a% | n/a s | 12.043 MB | 12.043 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 121540 |  | 1 | n/a% | n/a% | n/a s | 27.391 MB | 27.391 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 121576 |  | 1 | n/a% | n/a% | n/a s | 25.973 MB | 25.973 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 121618 |  | 1 | n/a% | n/a% | n/a s | 26.637 MB | 26.637 MB | 1732.277 MB | 1732.277 MB | n/a MB | n/a MB |
| docker | 121635 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.883 MB | 25.883 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 121674 | beef_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.475 MB | 0.633 MB | 1.021 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 121697 |  | 1 | n/a% | n/a% | n/a s | 27.430 MB | 27.430 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| tail | 121687 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 121717 | beef_0000 | 1 | n/a% | n/a% | n/a s | 11.434 MB | 11.434 MB | 1498.223 MB | 1498.223 MB | n/a MB | n/a MB |
| docker | 121723 |  | 1 | n/a% | n/a% | n/a s | 27.617 MB | 27.617 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 121759 |  | 1 | n/a% | n/a% | n/a s | 27.297 MB | 27.297 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 121779 | beef_0000 | 1 | n/a% | n/a% | n/a s | 11.977 MB | 11.977 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 121795 |  | 1 | n/a% | n/a% | n/a s | 26.219 MB | 26.219 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 121810 |  | 1 | n/a% | n/a% | n/a s | 1.070 MB | 1.070 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 121835 |  | 1 | n/a% | n/a% | n/a s | 26.977 MB | 26.977 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 121864 |  | 1 | n/a% | n/a% | n/a s | 6.344 MB | 6.344 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 121915 |  | 1 | n/a% | n/a% | n/a s | 11.211 MB | 11.211 MB | 1451.949 MB | 1451.949 MB | n/a MB | n/a MB |
| docker | 121940 |  | 1 | n/a% | n/a% | n/a s | 25.449 MB | 25.449 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 121948 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.984 MB | 25.984 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 121964 |  | 1 | n/a% | n/a% | n/a s | 8.805 MB | 8.805 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| python3 | 121995 |  | 3 | 98.651% | 98.900% | 0.200 s | 27.766 MB | 33.699 MB | 51.358 MB | 56.461 MB | 0.000000 MB | 0.000000 MB |
| docker | 122022 |  | 1 | n/a% | n/a% | n/a s | 26.879 MB | 26.879 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| docker | 122063 |  | 44 | 0.000% | 0.000% | 0.000 s | 26.449 MB | 26.449 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 122085 |  | 3 | 0.000% | 0.000% | 0.000 s | 26.980 MB | 27.652 MB | 1660.586 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 122125 | bell_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.594 MB | 12.398 MB | 262.625 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 122138 | bell_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 122140 |  | 1 | n/a% | n/a% | n/a s | 27.371 MB | 27.371 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 122175 |  | 1 | n/a% | n/a% | n/a s | 15.465 MB | 15.465 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 122200 |  | 1 | n/a% | n/a% | n/a s | 27.270 MB | 27.270 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 122218 | bell_0000 | 1 | n/a% | n/a% | n/a s | 10.438 MB | 10.438 MB | 1569.445 MB | 1569.445 MB | n/a MB | n/a MB |
| docker | 122235 |  | 1 | n/a% | n/a% | n/a s | 25.883 MB | 25.883 MB | 1659.961 MB | 1659.961 MB | n/a MB | n/a MB |
| docker | 122266 |  | 1 | n/a% | n/a% | n/a s | 26.320 MB | 26.320 MB | 1732.277 MB | 1732.277 MB | n/a MB | n/a MB |
| docker | 122275 |  | 1 | n/a% | n/a% | n/a s | 26.000 MB | 26.000 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 122315 |  | 1 | n/a% | n/a% | n/a s | 22.898 MB | 22.898 MB | 1523.953 MB | 1523.953 MB | n/a MB | n/a MB |
| docker | 122331 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.344 MB | 25.344 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 122372 | bell_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.096 MB | 12.949 MB | 314.989 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 122395 |  | 1 | n/a% | n/a% | n/a s | 26.234 MB | 26.234 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 122384 | bell_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 122423 |  | 1 | n/a% | n/a% | n/a s | 27.605 MB | 27.605 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 122447 |  | 1 | n/a% | n/a% | n/a s | 27.184 MB | 27.184 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 122494 |  | 1 | n/a% | n/a% | n/a s | 26.016 MB | 26.016 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 122536 |  | 1 | n/a% | n/a% | n/a s | 11.133 MB | 11.133 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 122555 |  | 1 | n/a% | n/a% | n/a s | 25.633 MB | 25.633 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 122583 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.773 MB | 26.773 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 122623 | beef_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.747 MB | 13.090 MB | 411.411 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 122646 |  | 1 | n/a% | n/a% | n/a s | 27.473 MB | 27.473 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 122636 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.146 MB | 1.719 MB | 1.990 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 122711 |  | 1 | n/a% | n/a% | n/a s | 26.223 MB | 26.223 MB | 1732.277 MB | 1732.277 MB | n/a MB | n/a MB |
| docker | 122751 |  | 1 | n/a% | n/a% | n/a s | 26.176 MB | 26.176 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 122793 |  | 1 | n/a% | n/a% | n/a s | 5.938 MB | 5.938 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 122810 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.016 MB | 27.016 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 122847 | beef_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.763 MB | 13.070 MB | 143.752 MB | 1570.727 MB | n/a MB | n/a MB |
| tail | 122860 | beef_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 122891 | beef_0000 | 1 | n/a% | n/a% | n/a s | 11.867 MB | 11.867 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 122871 |  | 1 | n/a% | n/a% | n/a s | 27.258 MB | 27.258 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python | 122928 | beef_0000 | 8 | 100.480% | 107.864% | 0.720 s | 30.627 MB | 42.551 MB | 37.905 MB | 52.238 MB | n/a MB | n/a MB |
| bash | 122919 | beef_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.328 MB | 3.328 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 122899 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.289 MB | 27.289 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 122930 |  | 1 | n/a% | n/a% | n/a s | 19.266 MB | 19.266 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 122938 |  | 1 | n/a% | n/a% | n/a s | 26.926 MB | 26.926 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 122991 |  | 1 | n/a% | n/a% | n/a s | 24.277 MB | 24.277 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 122999 |  | 1 | n/a% | n/a% | n/a s | 25.656 MB | 25.656 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 123039 | beef_0000 | 4 | 3.258% | 9.775% | 0.010 s | 3.573 MB | 12.395 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 123051 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 123061 |  | 1 | n/a% | n/a% | n/a s | 26.922 MB | 26.922 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 123090 |  | 1 | n/a% | n/a% | n/a s | 27.309 MB | 27.309 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 123154 |  | 1 | n/a% | n/a% | n/a s | 21.773 MB | 21.773 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 123162 |  | 1 | n/a% | n/a% | n/a s | 25.707 MB | 25.707 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 123223 |  | 1 | n/a% | n/a% | n/a s | 8.668 MB | 8.668 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 123248 |  | 43 | 0.000% | 0.000% | 0.000 s | 24.865 MB | 25.457 MB | 1621.601 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 123265 |  | 2 | 19.295% | 19.295% | 0.020 s | 23.719 MB | 27.258 MB | 1588.486 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 123306 | bell_0000 | 6 | 7.696% | 38.480% | 0.040 s | 1.136 MB | 3.652 MB | 202.325 MB | 1208.676 MB | n/a MB | n/a MB |
| tail | 123317 | bell_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.664 MB | 1.664 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 123346 | bell_0000 | 1 | n/a% | n/a% | n/a s | 11.938 MB | 11.938 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 123327 |  | 1 | n/a% | n/a% | n/a s | 27.383 MB | 27.383 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 123373 | bell_0000 | 1 | n/a% | n/a% | n/a s | 11.965 MB | 11.965 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 123353 |  | 1 | n/a% | n/a% | n/a s | 27.109 MB | 27.109 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 123390 |  | 1 | n/a% | n/a% | n/a s | 27.504 MB | 27.504 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 123410 | bell_0000 | 1 | n/a% | n/a% | n/a s | 4.348 MB | 4.348 MB | 1497.191 MB | 1497.191 MB | n/a MB | n/a MB |
| docker | 123427 |  | 2 | 9.205% | 9.205% | 0.010 s | 22.252 MB | 25.977 MB | 1624.082 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 123505 |  | 1 | n/a% | n/a% | n/a s | 25.922 MB | 25.922 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| python3 | 123521 |  | 4 | 98.791% | 98.978% | 0.300 s | 27.507 MB | 34.781 MB | 51.417 MB | 57.438 MB | 0.000000 MB | 0.242188 MB |
| docker | 123531 |  | 1 | n/a% | n/a% | n/a s | 26.512 MB | 26.512 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 123555 |  | 1 | n/a% | n/a% | n/a s | 8.801 MB | 8.801 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 123585 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.648 MB | 26.648 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 123609 |  | 1 | n/a% | n/a% | n/a s | 20.355 MB | 20.355 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 123628 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.184 MB | 27.184 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 123668 | bell_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.697 MB | 12.891 MB | 411.349 MB | 1642.230 MB | n/a MB | n/a MB |
| tail | 123682 | bell_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 123692 |  | 1 | n/a% | n/a% | n/a s | 27.379 MB | 27.379 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 123759 |  | 1 | n/a% | n/a% | n/a s | 25.832 MB | 25.832 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 123797 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.973 MB | 25.973 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 123849 |  | 1 | n/a% | n/a% | n/a s | 25.098 MB | 25.098 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 123857 |  | 1 | n/a% | n/a% | n/a s | 25.895 MB | 25.895 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 123895 | bell_0000 | 11 | 0.978% | 9.783% | 0.010 s | 1.690 MB | 12.262 MB | 143.707 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 123908 | bell_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.785 MB | 1.785 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 123918 |  | 1 | n/a% | n/a% | n/a s | 27.289 MB | 27.289 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 123938 | bell_0000 | 1 | n/a% | n/a% | n/a s | 10.535 MB | 10.535 MB | 1641.449 MB | 1641.449 MB | n/a MB | n/a MB |
| bash | 123968 | bell_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.426 MB | 3.426 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 123948 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.258 MB | 27.258 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| python | 123978 | bell_0000 | 8 | 100.683% | 107.875% | 0.720 s | 30.129 MB | 42.367 MB | 37.572 MB | 52.238 MB | n/a MB | n/a MB |
| docker | 123988 |  | 1 | n/a% | n/a% | n/a s | 25.918 MB | 25.918 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 124073 |  | 1 | n/a% | n/a% | n/a s | 4.570 MB | 4.570 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 124081 |  | 40 | 0.000% | 0.000% | 0.000 s | 25.738 MB | 25.738 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 124114 |  | 1 | n/a% | n/a% | n/a s | 26.691 MB | 26.691 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 124129 |  | 4 | 102.015% | 108.775% | 0.310 s | 26.477 MB | 34.547 MB | 50.429 MB | 57.438 MB | 0.000000 MB | 0.242188 MB |
| docker | 124132 |  | 1 | n/a% | n/a% | n/a s | 27.016 MB | 27.016 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 124189 |  | 1 | n/a% | n/a% | n/a s | 27.176 MB | 27.176 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |

## GPU metrics

_No GPU samples were collected._

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| alex_0000 | 56.799% | 103.178% | 1.741 s | 10.031 MB | 36.133 MB | 0.000000 MB | 1.703125 MB | 0.000000 MB | 0.000000 MB |
| andy_0000 | 58.916% | 118.797% | 1.826 s | 10.585 MB | 35.410 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| arch_0000 | 61.063% | 99.137% | 1.862 s | 11.904 MB | 36.293 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bake_0000 | 58.144% | 99.441% | 1.894 s | 10.645 MB | 34.555 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bale_0000 | 82.507% | 100.169% | 4.040 s | 22.251 MB | 34.848 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| band_0000 | 59.663% | 100.099% | 1.298 s | 8.949 MB | 35.379 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bart_0000 | 60.672% | 100.952% | 1.244 s | 10.000 MB | 35.594 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| base_0000 | 93.403% | 133.618% | 30.752 s | 30.133 MB | 34.176 MB | 0.000000 MB | 1.832031 MB | 0.000000 MB | 0.000000 MB |
| beam_0000 | 62.234% | 113.451% | 1.733 s | 10.771 MB | 35.270 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bear_0000 | 59.143% | 116.922% | 1.902 s | 10.060 MB | 35.664 MB | 0.023438 MB | 0.812500 MB | 0.000000 MB | 0.000000 MB |
| beef_0000 | 60.437% | 100.010% | 1.320 s | 9.462 MB | 36.422 MB | 0.015625 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bell_0000 | 54.202% | 100.038% | 1.410 s | 8.090 MB | 36.539 MB | 0.011719 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |

## Incomplete spans

_No spans were still open when profiling stopped._

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sync:result_wait | 24/24 | 0 | 0 | 720.918 | 0.004 | 720.911 | 30038.265 | 26707.516 | 52519.410 |
| turn | 81/81 | 0 | 0 | 602.597 | 2.700 | 599.427 | 7439.467 | 4408.391 | 24479.667 |
| llm:attempt | 81/81 | 0 | 0 | 509.932 | 2.210 | 507.394 | 6295.454 | 3366.565 | 20604.375 |
| run:diagnose_bug | 12/12 | 0 | 0 | 410.679 | 1.478 | 408.861 | 34223.238 | 30752.478 | 50505.404 |
| llm:diagnose_bug | 30/30 | 0 | 0 | 327.752 | 1.182 | 326.322 | 10925.069 | 4871.041 | 26619.718 |
| run:repair_bug | 12/12 | 0 | 0 | 310.247 | 1.360 | 308.717 | 25853.932 | 20505.727 | 49971.962 |
| llm:repair_bug | 51/51 | 0 | 0 | 182.211 | 1.054 | 181.076 | 3572.758 | 2966.920 | 6560.778 |
| teardown:commit | 24/24 | 0 | 0 | 117.956 | 0.061 | 117.864 | 4914.816 | 4741.771 | 6003.291 |
| sandbox:commit | 24/24 | 0 | 0 | 117.394 | 0.047 | 117.322 | 4891.408 | 4721.089 | 5981.030 |
| capstone:build:find_first_in_sorted | 1/1 | 0 | 0 | 80.655 | 0.000 | 80.654 | 80655.260 | 80655.260 | 80655.260 |
| tool_dispatch:repair_bug | 51/51 | 0 | 0 | 69.017 | 0.217 | 68.732 | 1353.275 | 609.024 | 2128.682 |
| capstone:plan:find_first_in_sorted | 1/1 | 0 | 0 | 53.275 | 0.001 | 53.275 | 53275.468 | 53275.468 | 53275.468 |
| sandbox:exec | 16/16 | 0 | 0 | 51.269 | 0.039 | 51.210 | 3204.319 | 1404.345 | 10530.673 |
| tool:bash | 13/13 | 0 | 0 | 50.257 | 0.038 | 50.198 | 3865.935 | 1661.637 | 14509.032 |
| capstone:plan:next_palindrome | 1/1 | 0 | 0 | 48.240 | 0.001 | 48.239 | 48239.739 | 48239.739 | 48239.739 |
| capstone:plan:rpn_eval | 1/1 | 0 | 0 | 40.664 | 0.001 | 40.663 | 40663.885 | 40663.885 | 40663.885 |
| capstone:plan:mergesort | 1/1 | 0 | 0 | 36.742 | 0.001 | 36.741 | 36742.283 | 36742.283 | 36742.283 |
| capstone:plan:bucketsort | 1/1 | 0 | 0 | 33.127 | 0.001 | 33.126 | 33126.573 | 33126.573 | 33126.573 |
| capstone:plan:hanoi | 1/1 | 0 | 0 | 31.398 | 0.001 | 31.398 | 31398.366 | 31398.366 | 31398.366 |
| capstone:plan:powerset | 1/1 | 0 | 0 | 30.107 | 0.001 | 30.106 | 30106.603 | 30106.603 | 30106.603 |
| capstone:plan:bitcount | 1/1 | 0 | 0 | 29.911 | 0.001 | 29.910 | 29911.067 | 29911.067 | 29911.067 |
| capstone:plan:gcd | 1/1 | 0 | 0 | 29.486 | 0.001 | 29.485 | 29486.075 | 29486.075 | 29486.075 |
| capstone:plan:flatten | 1/1 | 0 | 0 | 29.355 | 0.001 | 29.354 | 29355.471 | 29355.471 | 29355.471 |
| capstone:plan:levenshtein | 1/1 | 0 | 0 | 28.548 | 0.001 | 28.547 | 28547.889 | 28547.889 | 28547.889 |
| capstone:build:mergesort | 1/1 | 0 | 0 | 24.868 | 0.001 | 24.868 | 24868.311 | 24868.311 | 24868.311 |
| capstone:build:levenshtein | 1/1 | 0 | 0 | 24.418 | 0.000 | 24.417 | 24418.092 | 24418.092 | 24418.092 |
| tool_dispatch:diagnose_bug | 30/30 | 0 | 0 | 23.561 | 0.196 | 23.295 | 785.367 | 603.948 | 1972.968 |
| capstone:build:gcd | 1/1 | 0 | 0 | 22.085 | 0.000 | 22.084 | 22084.982 | 22084.982 | 22084.982 |
| capstone:build:next_palindrome | 1/1 | 0 | 0 | 21.892 | 0.000 | 21.892 | 21892.301 | 21892.301 | 21892.301 |
| tool:read | 37/37 | 0 | 0 | 21.110 | 0.159 | 20.888 | 570.535 | 559.879 | 864.576 |
| sandbox:start | 66/66 | 0 | 0 | 20.894 | 0.106 | 20.746 | 316.569 | 266.156 | 523.117 |
| capstone:build:bitcount | 1/1 | 0 | 0 | 20.521 | 0.001 | 20.520 | 20521.230 | 20521.230 | 20521.230 |
| capstone:build:flatten | 1/1 | 0 | 0 | 20.492 | 0.000 | 20.491 | 20491.867 | 20491.867 | 20491.867 |
| capstone:build:rpn_eval | 1/1 | 0 | 0 | 20.057 | 0.001 | 20.056 | 20056.562 | 20056.562 | 20056.562 |
| capstone:plan:is_valid_parenthesization | 1/1 | 0 | 0 | 19.829 | 0.001 | 19.828 | 19828.812 | 19828.812 | 19828.812 |
| capstone:build:hanoi | 1/1 | 0 | 0 | 19.807 | 0.000 | 19.806 | 19807.006 | 19807.006 | 19807.006 |
| capstone:build:bucketsort | 1/1 | 0 | 0 | 18.900 | 0.000 | 18.899 | 18899.636 | 18899.636 | 18899.636 |
| capstone:build:is_valid_parenthesization | 1/1 | 0 | 0 | 18.407 | 0.000 | 18.407 | 18407.462 | 18407.462 | 18407.462 |
| capstone:build:powerset | 1/1 | 0 | 0 | 18.148 | 0.001 | 18.147 | 18147.905 | 18147.905 | 18147.905 |
| sandbox:stop | 129/129 | 0 | 0 | 14.517 | 0.108 | 14.365 | 112.532 | 166.200 | 229.808 |
| capstone:prepare:bitcount | 1/1 | 0 | 0 | 10.043 | 0.030 | 10.013 | 10042.657 | 10042.657 | 10042.657 |
| capstone:prepare:find_first_in_sorted | 1/1 | 0 | 0 | 10.043 | 0.030 | 10.013 | 10042.513 | 10042.513 | 10042.513 |
| sandbox:read_file | 50/50 | 0 | 0 | 8.852 | 0.073 | 8.749 | 177.033 | 129.448 | 419.557 |
| capstone:prepare:mergesort | 1/1 | 0 | 0 | 7.039 | 0.040 | 6.998 | 7038.994 | 7038.994 | 7038.994 |
| tool:edit | 13/13 | 0 | 0 | 6.168 | 0.051 | 6.104 | 474.446 | 430.637 | 649.248 |
| capstone:verify:levenshtein | 1/1 | 0 | 0 | 2.855 | 0.001 | 2.853 | 2854.617 | 2854.617 | 2854.617 |
| capstone:scheduler:tick | 385/385 | 0 | 0 | 2.523 | 0.671 | 1.846 | 6.554 | 0.195 | 0.587 |
| capstone:prepare:levenshtein | 1/1 | 0 | 0 | 2.503 | 0.030 | 2.472 | 2502.652 | 2502.652 | 2502.652 |
| agent:create | 12/12 | 0 | 0 | 2.425 | 0.582 | 1.839 | 202.054 | 138.699 | 485.788 |
| sandbox:destroy | 12/12 | 0 | 0 | 1.465 | 0.020 | 1.442 | 122.098 | 120.608 | 137.616 |
| sandbox:write_file | 13/13 | 0 | 0 | 1.335 | 0.012 | 1.320 | 102.699 | 94.093 | 137.474 |
| tool:glob | 3/3 | 0 | 0 | 1.022 | 0.010 | 1.012 | 340.601 | 329.303 | 361.145 |
| capstone:prepare:hanoi | 1/1 | 0 | 0 | 0.619 | 0.049 | 0.569 | 618.771 | 618.771 | 618.771 |
| capstone:verify:flatten | 1/1 | 0 | 0 | 0.570 | 0.001 | 0.568 | 569.906 | 569.906 | 569.906 |
| capstone:verify:hanoi | 1/1 | 0 | 0 | 0.557 | 0.001 | 0.556 | 557.190 | 557.190 | 557.190 |
| capstone:verify:find_first_in_sorted | 1/1 | 0 | 0 | 0.526 | 0.001 | 0.524 | 525.726 | 525.726 | 525.726 |
| capstone:prepare:gcd | 1/1 | 0 | 0 | 0.477 | 0.031 | 0.446 | 477.402 | 477.402 | 477.402 |
| capstone:prepare:rpn_eval | 1/1 | 0 | 0 | 0.464 | 0.031 | 0.432 | 463.568 | 463.568 | 463.568 |
| capstone:prepare:powerset | 1/1 | 0 | 0 | 0.451 | 0.031 | 0.421 | 451.286 | 451.286 | 451.286 |
| capstone:prepare:next_palindrome | 1/1 | 0 | 0 | 0.450 | 0.031 | 0.419 | 450.441 | 450.441 | 450.441 |
| capstone:prepare:bucketsort | 1/1 | 0 | 0 | 0.449 | 0.031 | 0.418 | 448.584 | 448.584 | 448.584 |
| capstone:prepare:flatten | 1/1 | 0 | 0 | 0.444 | 0.030 | 0.414 | 443.981 | 443.981 | 443.981 |
| capstone:prepare:is_valid_parenthesization | 1/1 | 0 | 0 | 0.434 | 0.030 | 0.404 | 433.699 | 433.699 | 433.699 |
| capstone:verify:bitcount | 1/1 | 0 | 0 | 0.419 | 0.001 | 0.417 | 418.524 | 418.524 | 418.524 |
| capstone:verify:mergesort | 1/1 | 0 | 0 | 0.404 | 0.001 | 0.402 | 403.905 | 403.905 | 403.905 |
| capstone:verify:rpn_eval | 1/1 | 0 | 0 | 0.396 | 0.001 | 0.395 | 395.758 | 395.758 | 395.758 |
| capstone:verify:gcd | 1/1 | 0 | 0 | 0.394 | 0.001 | 0.392 | 393.784 | 393.784 | 393.784 |
| capstone:verify:bucketsort | 1/1 | 0 | 0 | 0.390 | 0.001 | 0.389 | 389.847 | 389.847 | 389.847 |
| capstone:verify:next_palindrome | 1/1 | 0 | 0 | 0.387 | 0.001 | 0.385 | 387.238 | 387.238 | 387.238 |
| capstone:verify:is_valid_parenthesization | 1/1 | 0 | 0 | 0.386 | 0.001 | 0.385 | 385.521 | 385.521 | 385.521 |
| capstone:verify:powerset | 1/1 | 0 | 0 | 0.384 | 0.001 | 0.383 | 384.086 | 384.086 | 384.086 |
| sandbox:provision | 12/12 | 0 | 0 | 0.274 | 0.011 | 0.261 | 22.820 | 0.493 | 124.865 |
| sandbox:create | 12/12 | 0 | 0 | 0.270 | 0.007 | 0.261 | 22.485 | 0.315 | 124.701 |
| run:detect | 2/2 | 0 | 0 | 0.196 | 0.002 | 0.194 | 98.227 | 98.227 | 144.463 |
| sync:container | 871/871 | 0 | 0 | 0.112 | 0.101 | 0.006 | 0.128 | 0.135 | 0.226 |
| prune | 24/24 | 0 | 0 | 0.007 | 0.003 | 0.002 | 0.271 | 0.221 | 0.769 |
| tool:return_summary | 15/15 | 3 | 0 | 0.006 | 0.006 | 0.000 | 0.418 | 0.379 | 0.670 |
| tool:return_status | 12/12 | 0 | 0 | 0.006 | 0.004 | 0.001 | 0.486 | 0.305 | 1.169 |
| tool:return_plan | 12/12 | 0 | 0 | 0.006 | 0.006 | 0.000 | 0.481 | 0.322 | 1.190 |
| llm:sync | 81/81 | 0 | 0 | 0.005 | 0.004 | 0.000 | 0.056 | 0.040 | 0.116 |
| agsync:join | 12/12 | 0 | 0 | 0.003 | 0.003 | 0.000 | 0.214 | 0.221 | 0.261 |
| input:prepare | 24/24 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.101 | 0.093 | 0.156 |
| resolve | 24/24 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.084 | 0.061 | 0.105 |
| proc_wait | 24/24 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.076 | 0.070 | 0.102 |
| agprof:clock_sync | 1/1 | 0 | 0 | 0.002 | 0.001 | 0.001 | 1.809 | 1.809 | 1.809 |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 3767 | 38.860 | 0.000 | 202.079 | 13.111 | 149.878034 CPU seconds | n/a |
| python3 (PID 107320) CPU | percent | 4164 | 5.129 | 0.000 | 136.087 | 0.000 | 22.080000 CPU seconds | n/a |
| python3 (PID 107320) io read MB/s | MB/s | 4164 | 0.076 | 0.000 | 89.507 | 0.000 | 33.382812 MB | n/a |
| python3 (PID 107320) io write MB/s | MB/s | 4164 | 0.082 | 0.000 | 22.735 | 0.000 | 34.718750 MB | n/a |
| python3 (PID 107320) rss_mb | MB | 4165 | 691.008 | 612.723 | 711.254 | 711.254 | n/a | n/a |
| python3 (PID 107320) vms_mb | MB | 4165 | 3947.035 | 3407.559 | 4047.340 | 4017.246 | n/a | n/a |
| python3 (PID 107325) rss_mb | MB | 1 | 648.719 | 648.719 | 648.719 | 648.719 | n/a | n/a |
| python3 (PID 107325) vms_mb | MB | 1 | 3444.871 | 3444.871 | 3444.871 | 3444.871 | n/a | n/a |
| git (PID 107326) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| git (PID 107326) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 107326) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 107326) rss_mb | MB | 5 | 4.660 | 4.660 | 4.660 | 4.660 | n/a | n/a |
| git (PID 107326) vms_mb | MB | 5 | 12.516 | 12.516 | 12.516 | 12.516 | n/a | n/a |
| git (PID 107327) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| git (PID 107327) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 107327) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 107327) rss_mb | MB | 5 | 3.309 | 3.309 | 3.309 | 3.309 | n/a | n/a |
| git (PID 107327) vms_mb | MB | 5 | 11.273 | 11.273 | 11.273 | 11.273 | n/a | n/a |
| git-remote-http (PID 107328) CPU | percent | 4 | 4.924 | 0.000 | 19.694 | 0.000 | 0.020000 CPU seconds | n/a |
| git-remote-http (PID 107328) io read MB/s | MB/s | 4 | 0.347 | 0.000 | 1.154 | 0.000 | 0.140625 MB | n/a |
| git-remote-http (PID 107328) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git-remote-http (PID 107328) rss_mb | MB | 5 | 18.977 | 18.777 | 19.027 | 19.027 | n/a | n/a |
| git-remote-http (PID 107328) vms_mb | MB | 5 | 107.166 | 106.566 | 107.566 | 107.566 | n/a | n/a |
| python3 (PID 107334) CPU | percent | 99 | 99.961 | 98.936 | 109.049 | 99.038 | 9.990000 CPU seconds | n/a |
| python3 (PID 107334) io read MB/s | MB/s | 99 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 107334) io write MB/s | MB/s | 99 | 0.002 | 0.000 | 0.155 | 0.000 | 0.015625 MB | n/a |
| python3 (PID 107334) rss_mb | MB | 100 | 33.824 | 10.758 | 34.211 | 34.211 | n/a | n/a |
| python3 (PID 107334) vms_mb | MB | 100 | 57.104 | 36.633 | 57.457 | 57.457 | n/a | n/a |
| python3 (PID 107335) CPU | percent | 3 | 99.021 | 98.922 | 99.105 | 99.035 | 0.300000 CPU seconds | n/a |
| python3 (PID 107335) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 107335) io write MB/s | MB/s | 3 | 0.825 | 0.000 | 2.437 | 2.437 | 0.250000 MB | n/a |
| python3 (PID 107335) rss_mb | MB | 4 | 28.578 | 18.105 | 34.871 | 34.871 | n/a | n/a |
| python3 (PID 107335) vms_mb | MB | 4 | 51.865 | 42.566 | 57.500 | 57.500 | n/a | n/a |
| python3 (PID 107336) CPU | percent | 4 | 101.435 | 99.025 | 108.645 | 99.032 | 0.410000 CPU seconds | n/a |
| python3 (PID 107336) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 107336) io write MB/s | MB/s | 4 | 0.619 | 0.000 | 2.321 | 2.321 | 0.250000 MB | n/a |
| python3 (PID 107336) rss_mb | MB | 5 | 27.402 | 12.000 | 36.602 | 36.602 | n/a | n/a |
| python3 (PID 107336) vms_mb | MB | 5 | 51.341 | 38.164 | 59.516 | 59.516 | n/a | n/a |
| python3 (PID 107337) CPU | percent | 3 | 102.342 | 99.052 | 108.882 | 99.092 | 0.310000 CPU seconds | n/a |
| python3 (PID 107337) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 107337) io write MB/s | MB/s | 3 | 0.826 | 0.000 | 2.477 | 2.477 | 0.250000 MB | n/a |
| python3 (PID 107337) rss_mb | MB | 4 | 27.581 | 16.809 | 34.766 | 34.766 | n/a | n/a |
| python3 (PID 107337) vms_mb | MB | 4 | 51.413 | 41.164 | 57.496 | 57.496 | n/a | n/a |
| python3 (PID 107338) CPU | percent | 24 | 99.475 | 89.149 | 109.039 | 89.202 | 2.410000 CPU seconds | n/a |
| python3 (PID 107338) io read MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 107338) io write MB/s | MB/s | 24 | 0.105 | 0.000 | 2.362 | 2.362 | 0.253906 MB | n/a |
| python3 (PID 107338) rss_mb | MB | 25 | 32.941 | 11.980 | 34.863 | 34.863 | n/a | n/a |
| python3 (PID 107338) vms_mb | MB | 25 | 56.209 | 38.164 | 57.457 | 57.457 | n/a | n/a |
| python3 (PID 107339) CPU | percent | 68 | 99.905 | 89.097 | 108.993 | 99.010 | 6.860000 CPU seconds | n/a |
| python3 (PID 107339) io read MB/s | MB/s | 68 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 107339) io write MB/s | MB/s | 68 | 0.038 | 0.000 | 2.400 | 0.000 | 0.257812 MB | n/a |
| python3 (PID 107339) rss_mb | MB | 69 | 41.568 | 15.820 | 47.484 | 47.484 | n/a | n/a |
| python3 (PID 107339) vms_mb | MB | 69 | 64.559 | 41.035 | 70.645 | 70.645 | n/a | n/a |
| python3 (PID 107340) CPU | percent | 3 | 99.014 | 89.063 | 108.895 | 89.063 | 0.300000 CPU seconds | n/a |
| python3 (PID 107340) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 107340) io write MB/s | MB/s | 3 | 0.850 | 0.000 | 2.513 | 2.513 | 0.257812 MB | n/a |
| python3 (PID 107340) rss_mb | MB | 4 | 28.857 | 19.113 | 34.957 | 34.957 | n/a | n/a |
| python3 (PID 107340) vms_mb | MB | 4 | 52.188 | 43.855 | 57.504 | 57.504 | n/a | n/a |
| python3 (PID 107341) CPU | percent | 98 | 99.962 | 96.927 | 109.043 | 99.039 | 9.900000 CPU seconds | n/a |
| python3 (PID 107341) io read MB/s | MB/s | 98 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 107341) io write MB/s | MB/s | 98 | 0.002 | 0.000 | 0.155 | 0.000 | 0.015625 MB | n/a |
| python3 (PID 107341) rss_mb | MB | 99 | 34.163 | 13.062 | 34.512 | 34.512 | n/a | n/a |
| python3 (PID 107341) vms_mb | MB | 99 | 57.156 | 38.422 | 57.457 | 57.457 | n/a | n/a |
| python3 (PID 107342) CPU | percent | 3 | 99.099 | 89.083 | 109.060 | 109.060 | 0.300000 CPU seconds | n/a |
| python3 (PID 107342) io read MB/s | MB/s | 3 | 0.194 | 0.000 | 0.581 | 0.000 | 0.058594 MB | n/a |
| python3 (PID 107342) io write MB/s | MB/s | 3 | 0.852 | 0.000 | 2.556 | 2.556 | 0.257812 MB | n/a |
| python3 (PID 107342) rss_mb | MB | 4 | 26.755 | 15.914 | 34.988 | 34.988 | n/a | n/a |
| python3 (PID 107342) vms_mb | MB | 4 | 50.665 | 41.035 | 57.492 | 57.492 | n/a | n/a |
| python3 (PID 107343) CPU | percent | 3 | 102.303 | 98.963 | 108.928 | 108.928 | 0.310000 CPU seconds | n/a |
| python3 (PID 107343) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 107343) io write MB/s | MB/s | 3 | 0.864 | 0.000 | 2.553 | 2.553 | 0.261719 MB | n/a |
| python3 (PID 107343) rss_mb | MB | 4 | 29.039 | 19.801 | 34.730 | 34.730 | n/a | n/a |
| python3 (PID 107343) vms_mb | MB | 4 | 52.522 | 44.238 | 57.457 | 57.457 | n/a | n/a |
| python3 (PID 107344) CPU | percent | 3 | 102.297 | 98.968 | 108.813 | 99.110 | 0.310000 CPU seconds | n/a |
| python3 (PID 107344) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 107344) io write MB/s | MB/s | 3 | 0.865 | 0.000 | 2.594 | 2.594 | 0.261719 MB | n/a |
| python3 (PID 107344) rss_mb | MB | 4 | 26.364 | 13.922 | 34.945 | 34.945 | n/a | n/a |
| python3 (PID 107344) vms_mb | MB | 4 | 50.354 | 39.566 | 57.508 | 57.508 | n/a | n/a |
| python3 (PID 107345) CPU | percent | 3 | 98.984 | 98.848 | 99.073 | 99.031 | 0.300000 CPU seconds | n/a |
| python3 (PID 107345) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 107345) io write MB/s | MB/s | 3 | 0.864 | 0.000 | 2.553 | 2.553 | 0.261719 MB | n/a |
| python3 (PID 107345) rss_mb | MB | 4 | 29.466 | 20.762 | 34.871 | 34.871 | n/a | n/a |
| python3 (PID 107345) vms_mb | MB | 4 | 53.125 | 45.371 | 57.508 | 57.508 | n/a | n/a |
| docker (PID 107349) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 107349) io read MB/s | MB/s | 1 | 90.240 | 90.240 | 90.240 | 90.240 | 9.113281 MB | n/a |
| docker (PID 107349) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 107349) rss_mb | MB | 2 | 25.912 | 24.996 | 26.828 | 26.828 | n/a | n/a |
| docker (PID 107349) vms_mb | MB | 2 | 1660.242 | 1660.211 | 1660.273 | 1660.273 | n/a | n/a |
| docker-trust (PID 107357) rss_mb | MB | 1 | 6.129 | 6.129 | 6.129 | 6.129 | n/a | n/a |
| docker-trust (PID 107357) vms_mb | MB | 1 | 1212.965 | 1212.965 | 1212.965 | 1212.965 | n/a | n/a |
| docker (PID 107368) rss_mb | MB | 1 | 9.156 | 9.156 | 9.156 | 9.156 | n/a | n/a |
| docker (PID 107368) vms_mb | MB | 1 | 1315.695 | 1315.695 | 1315.695 | 1315.695 | n/a | n/a |
| docker (PID 107431) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 107431) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 107431) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 107431) rss_mb | MB | 3 | 27.232 | 26.883 | 27.406 | 27.406 | n/a | n/a |
| docker (PID 107431) vms_mb | MB | 3 | 1709.026 | 1661.023 | 1733.027 | 1733.027 | n/a | n/a |
| docker (PID 107432) CPU | percent | 2 | 4.929 | 0.000 | 9.857 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 107432) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 107432) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 107432) rss_mb | MB | 3 | 27.007 | 26.793 | 27.113 | 27.113 | n/a | n/a |
| docker (PID 107432) vms_mb | MB | 3 | 1708.776 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [alex_0000] (PID 107511) CPU | percent | 5 | 3.851 | 0.000 | 19.256 | 0.000 | 0.020000 CPU seconds | n/a |
| docker-init [alex_0000] (PID 107511) rss_mb | MB | 6 | 2.562 | 0.633 | 12.207 | 0.633 | n/a | n/a |
| docker-init [alex_0000] (PID 107511) vms_mb | MB | 6 | 262.583 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| docker-init [andy_0000] (PID 107518) CPU | percent | 5 | 1.926 | 0.000 | 9.628 | 0.000 | 0.010000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 107518) rss_mb | MB | 6 | 2.575 | 0.633 | 12.285 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 107518) vms_mb | MB | 6 | 262.625 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 107538) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 107538) rss_mb | MB | 5 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [alex_0000] (PID 107538) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| tail [andy_0000] (PID 107539) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 107539) rss_mb | MB | 5 | 1.801 | 1.801 | 1.801 | 1.801 | n/a | n/a |
| tail [andy_0000] (PID 107539) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 107542) rss_mb | MB | 1 | 27.199 | 27.199 | 27.199 | 27.199 | n/a | n/a |
| docker (PID 107542) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 107544) rss_mb | MB | 1 | 27.141 | 27.141 | 27.141 | 27.141 | n/a | n/a |
| docker (PID 107544) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 107614) rss_mb | MB | 1 | 8.844 | 8.844 | 8.844 | 8.844 | n/a | n/a |
| docker (PID 107614) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 107615) rss_mb | MB | 1 | 5.945 | 5.945 | 5.945 | 5.945 | n/a | n/a |
| docker (PID 107615) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 107666) rss_mb | MB | 1 | 25.281 | 25.281 | 25.281 | 25.281 | n/a | n/a |
| docker (PID 107666) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 107672) rss_mb | MB | 1 | 9.242 | 9.242 | 9.242 | 9.242 | n/a | n/a |
| docker (PID 107672) vms_mb | MB | 1 | 1443.695 | 1443.695 | 1443.695 | 1443.695 | n/a | n/a |
| docker (PID 107721) rss_mb | MB | 1 | 23.746 | 23.746 | 23.746 | 23.746 | n/a | n/a |
| docker (PID 107721) vms_mb | MB | 1 | 1660.207 | 1660.207 | 1660.207 | 1660.207 | n/a | n/a |
| docker (PID 107801) rss_mb | MB | 1 | 27.035 | 27.035 | 27.035 | 27.035 | n/a | n/a |
| docker (PID 107801) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 107803) rss_mb | MB | 1 | 27.070 | 27.070 | 27.070 | 27.070 | n/a | n/a |
| docker (PID 107803) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 107884) rss_mb | MB | 1 | 24.016 | 24.016 | 24.016 | 24.016 | n/a | n/a |
| docker (PID 107884) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 107886) rss_mb | MB | 1 | 23.496 | 23.496 | 23.496 | 23.496 | n/a | n/a |
| docker (PID 107886) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 107916) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 107916) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 107916) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 107916) rss_mb | MB | 2 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| docker (PID 107916) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 107918) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 107918) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 107918) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 107918) rss_mb | MB | 2 | 25.508 | 25.508 | 25.508 | 25.508 | n/a | n/a |
| docker (PID 107918) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 107994) CPU | percent | 4 | 2.366 | 0.000 | 9.464 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 107994) rss_mb | MB | 5 | 2.980 | 0.633 | 12.371 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 107994) vms_mb | MB | 5 | 314.939 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 108001) CPU | percent | 5 | 1.893 | 0.000 | 9.464 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 108001) rss_mb | MB | 6 | 2.546 | 0.633 | 12.113 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 108001) vms_mb | MB | 6 | 262.583 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 108021) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 108021) rss_mb | MB | 4 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [andy_0000] (PID 108021) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| tail [alex_0000] (PID 108022) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 108022) rss_mb | MB | 5 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [alex_0000] (PID 108022) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 108025) rss_mb | MB | 1 | 14.750 | 14.750 | 14.750 | 14.750 | n/a | n/a |
| docker (PID 108025) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 108027) rss_mb | MB | 1 | 17.262 | 17.262 | 17.262 | 17.262 | n/a | n/a |
| docker (PID 108027) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 108041) rss_mb | MB | 1 | 27.117 | 27.117 | 27.117 | 27.117 | n/a | n/a |
| docker (PID 108041) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 108043) rss_mb | MB | 1 | 27.426 | 27.426 | 27.426 | 27.426 | n/a | n/a |
| docker (PID 108043) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 108098) rss_mb | MB | 1 | 27.555 | 27.555 | 27.555 | 27.555 | n/a | n/a |
| docker (PID 108098) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 108143) rss_mb | MB | 1 | 12.055 | 12.055 | 12.055 | 12.055 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 108143) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 108165) rss_mb | MB | 1 | 27.551 | 27.551 | 27.551 | 27.551 | n/a | n/a |
| docker (PID 108165) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 108172) rss_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| docker (PID 108172) vms_mb | MB | 1 | 1733.027 | 1733.027 | 1733.027 | 1733.027 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 108196) rss_mb | MB | 1 | 11.770 | 11.770 | 11.770 | 11.770 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 108196) vms_mb | MB | 1 | 1642.602 | 1642.602 | 1642.602 | 1642.602 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 108217) rss_mb | MB | 1 | 7.613 | 7.613 | 7.613 | 7.613 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 108217) vms_mb | MB | 1 | 1569.195 | 1569.195 | 1569.195 | 1569.195 | n/a | n/a |
| docker (PID 108239) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 108239) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 108239) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 108239) rss_mb | MB | 2 | 26.094 | 26.094 | 26.094 | 26.094 | n/a | n/a |
| docker (PID 108239) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 108250) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 108250) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 108250) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 108250) rss_mb | MB | 2 | 24.445 | 22.930 | 25.961 | 25.961 | n/a | n/a |
| docker (PID 108250) vms_mb | MB | 2 | 1588.205 | 1588.203 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 108357) rss_mb | MB | 1 | 19.125 | 19.125 | 19.125 | 19.125 | n/a | n/a |
| docker (PID 108357) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 108371) CPU | percent | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 108371) io read MB/s | MB/s | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 108371) io write MB/s | MB/s | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 108371) rss_mb | MB | 52 | 25.664 | 25.664 | 25.664 | 25.664 | n/a | n/a |
| docker (PID 108371) vms_mb | MB | 52 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 108395) rss_mb | MB | 1 | 25.859 | 25.859 | 25.859 | 25.859 | n/a | n/a |
| docker (PID 108395) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 108410) CPU | percent | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 108410) io read MB/s | MB/s | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 108410) io write MB/s | MB/s | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 108410) rss_mb | MB | 52 | 26.859 | 26.859 | 26.859 | 26.859 | n/a | n/a |
| docker (PID 108410) vms_mb | MB | 52 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 108427) rss_mb | MB | 1 | 9.188 | 9.188 | 9.188 | 9.188 | n/a | n/a |
| docker (PID 108427) vms_mb | MB | 1 | 1443.695 | 1443.695 | 1443.695 | 1443.695 | n/a | n/a |
| docker (PID 108479) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 108479) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 108479) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 108479) rss_mb | MB | 2 | 25.633 | 25.633 | 25.633 | 25.633 | n/a | n/a |
| docker (PID 108479) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 108519) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 108519) rss_mb | MB | 4 | 3.693 | 0.566 | 13.074 | 0.566 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 108519) vms_mb | MB | 4 | 393.473 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 108532) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 108532) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [andy_0000] (PID 108532) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 108542) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 108542) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 108605) rss_mb | MB | 1 | 26.117 | 26.117 | 26.117 | 26.117 | n/a | n/a |
| docker (PID 108605) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 108643) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 108643) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 108643) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 108643) rss_mb | MB | 2 | 25.816 | 25.816 | 25.816 | 25.816 | n/a | n/a |
| docker (PID 108643) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| run2:repair_bug (PID 108658) CPU | percent | 1 | 9.617 | 9.617 | 9.617 | 9.617 | 0.010000 CPU seconds | n/a |
| run2:repair_bug (PID 108658) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| run2:repair_bug (PID 108658) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| run2:repair_bug (PID 108658) rss_mb | MB | 2 | 351.131 | 26.133 | 676.129 | 26.133 | n/a | n/a |
| run2:repair_bug (PID 108658) vms_mb | MB | 2 | 2817.936 | 1660.211 | 3975.660 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 108704) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 108704) rss_mb | MB | 4 | 3.705 | 0.633 | 12.922 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 108704) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 108743) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 108743) rss_mb | MB | 3 | 1.672 | 1.672 | 1.672 | 1.672 | n/a | n/a |
| tail [alex_0000] (PID 108743) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 108764) rss_mb | MB | 1 | 25.754 | 25.754 | 25.754 | 25.754 | n/a | n/a |
| docker (PID 108764) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 108791) rss_mb | MB | 1 | 27.031 | 27.031 | 27.031 | 27.031 | n/a | n/a |
| docker (PID 108791) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 108811) rss_mb | MB | 1 | 11.832 | 11.832 | 11.832 | 11.832 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 108811) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 108829) rss_mb | MB | 1 | 26.941 | 26.941 | 26.941 | 26.941 | n/a | n/a |
| docker (PID 108829) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| sh [alex_0000] (PID 108848) rss_mb | MB | 1 | 1.625 | 1.625 | 1.625 | 1.625 | n/a | n/a |
| sh [alex_0000] (PID 108848) vms_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| docker (PID 108870) rss_mb | MB | 1 | 27.066 | 27.066 | 27.066 | 27.066 | n/a | n/a |
| docker (PID 108870) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 108924) rss_mb | MB | 1 | 25.512 | 25.512 | 25.512 | 25.512 | n/a | n/a |
| docker (PID 108924) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 108933) rss_mb | MB | 1 | 25.375 | 25.375 | 25.375 | 25.375 | n/a | n/a |
| docker (PID 108933) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 108973) CPU | percent | 15 | 1.308 | 0.000 | 19.624 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 108973) rss_mb | MB | 16 | 1.323 | 0.633 | 11.676 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 108973) vms_mb | MB | 16 | 99.112 | 1.055 | 1569.969 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 108986) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 108986) rss_mb | MB | 15 | 1.605 | 1.605 | 1.605 | 1.605 | n/a | n/a |
| tail [andy_0000] (PID 108986) vms_mb | MB | 15 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 108998) rss_mb | MB | 1 | 24.090 | 24.090 | 24.090 | 24.090 | n/a | n/a |
| docker (PID 108998) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 109025) CPU | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 109025) io read MB/s | MB/s | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109025) io write MB/s | MB/s | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109025) rss_mb | MB | 13 | 27.301 | 27.301 | 27.301 | 27.301 | n/a | n/a |
| docker (PID 109025) vms_mb | MB | 13 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 109045) CPU | percent | 12 | 0.817 | 0.000 | 9.805 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 109045) rss_mb | MB | 13 | 4.037 | 3.379 | 11.938 | 3.379 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 109045) vms_mb | MB | 13 | 130.398 | 4.391 | 1642.480 | 4.391 | n/a | n/a |
| python [andy_0000] (PID 109055) CPU | percent | 11 | 92.931 | 69.378 | 113.305 | 95.130 | 1.110000 CPU seconds | n/a |
| python [andy_0000] (PID 109055) rss_mb | MB | 12 | 32.512 | 14.809 | 42.137 | 42.137 | n/a | n/a |
| python [andy_0000] (PID 109055) vms_mb | MB | 12 | 39.327 | 18.395 | 51.238 | 51.238 | n/a | n/a |
| docker (PID 109066) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 109066) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109066) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109066) rss_mb | MB | 2 | 27.098 | 27.098 | 27.098 | 27.098 | n/a | n/a |
| docker (PID 109066) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 109106) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 109106) rss_mb | MB | 15 | 1.464 | 0.633 | 13.094 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 109106) vms_mb | MB | 15 | 105.683 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 109118) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 109118) rss_mb | MB | 14 | 1.613 | 1.613 | 1.613 | 1.613 | n/a | n/a |
| tail [alex_0000] (PID 109118) vms_mb | MB | 14 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 109130) rss_mb | MB | 1 | 27.109 | 27.109 | 27.109 | 27.109 | n/a | n/a |
| docker (PID 109130) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 109148) rss_mb | MB | 1 | 11.691 | 11.691 | 11.691 | 11.691 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 109148) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 109157) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 109157) io read MB/s | MB/s | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109157) io write MB/s | MB/s | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109157) rss_mb | MB | 12 | 26.977 | 26.977 | 26.977 | 26.977 | n/a | n/a |
| docker (PID 109157) vms_mb | MB | 12 | 1733.027 | 1733.027 | 1733.027 | 1733.027 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 109176) CPU | percent | 11 | 0.847 | 0.000 | 9.320 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 109176) rss_mb | MB | 12 | 4.056 | 3.336 | 11.973 | 3.336 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 109176) vms_mb | MB | 12 | 128.877 | 4.391 | 1498.223 | 4.391 | n/a | n/a |
| python [alex_0000] (PID 109184) CPU | percent | 10 | 97.943 | 82.673 | 107.044 | 93.328 | 1.040000 CPU seconds | n/a |
| python [alex_0000] (PID 109184) rss_mb | MB | 11 | 32.532 | 14.848 | 42.672 | 42.672 | n/a | n/a |
| python [alex_0000] (PID 109184) vms_mb | MB | 11 | 39.370 | 18.395 | 52.238 | 52.238 | n/a | n/a |
| docker (PID 109194) CPU | percent | 1 | 9.186 | 9.186 | 9.186 | 9.186 | 0.010000 CPU seconds | n/a |
| docker (PID 109194) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109194) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109194) rss_mb | MB | 2 | 22.123 | 18.359 | 25.887 | 25.887 | n/a | n/a |
| docker (PID 109194) vms_mb | MB | 2 | 1587.955 | 1515.699 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 109255) CPU | percent | 1 | 9.806 | 9.806 | 9.806 | 9.806 | 0.010000 CPU seconds | n/a |
| docker (PID 109255) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109255) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109255) rss_mb | MB | 2 | 24.055 | 22.402 | 25.707 | 25.707 | n/a | n/a |
| docker (PID 109255) vms_mb | MB | 2 | 1624.207 | 1588.203 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 109324) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 109324) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109324) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109324) rss_mb | MB | 2 | 24.758 | 23.980 | 25.535 | 25.535 | n/a | n/a |
| docker (PID 109324) vms_mb | MB | 2 | 1628.211 | 1596.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 109326) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 109326) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109326) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109326) rss_mb | MB | 2 | 25.217 | 23.539 | 26.895 | 26.895 | n/a | n/a |
| docker (PID 109326) vms_mb | MB | 2 | 1624.488 | 1588.203 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 109403) CPU | percent | 4 | 7.151 | 0.000 | 28.604 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 109403) rss_mb | MB | 5 | 2.830 | 0.633 | 11.617 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 109403) vms_mb | MB | 5 | 314.786 | 1.055 | 1569.711 | 1.055 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 109410) CPU | percent | 4 | 9.535 | 0.000 | 38.139 | 0.000 | 0.040000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 109410) rss_mb | MB | 5 | 2.785 | 0.633 | 11.395 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 109410) vms_mb | MB | 5 | 329.184 | 1.055 | 1641.699 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 109423) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 109423) rss_mb | MB | 4 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [alex_0000] (PID 109423) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| tail [andy_0000] (PID 109431) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 109431) rss_mb | MB | 4 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [andy_0000] (PID 109431) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 109440) rss_mb | MB | 1 | 23.809 | 23.809 | 23.809 | 23.809 | n/a | n/a |
| docker (PID 109440) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 109452) rss_mb | MB | 1 | 27.109 | 27.109 | 27.109 | 27.109 | n/a | n/a |
| docker (PID 109452) vms_mb | MB | 1 | 1733.027 | 1733.027 | 1733.027 | 1733.027 | n/a | n/a |
| docker (PID 109505) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 109505) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| run2:repair_bug (PID 109558) rss_mb | MB | 1 | 679.254 | 679.254 | 679.254 | 679.254 | n/a | n/a |
| run2:repair_bug (PID 109558) vms_mb | MB | 1 | 3975.660 | 3975.660 | 3975.660 | 3975.660 | n/a | n/a |
| docker (PID 109576) rss_mb | MB | 1 | 27.156 | 27.156 | 27.156 | 27.156 | n/a | n/a |
| docker (PID 109576) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 109578) rss_mb | MB | 1 | 27.379 | 27.379 | 27.379 | 27.379 | n/a | n/a |
| docker (PID 109578) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 109612) rss_mb | MB | 1 | 11.816 | 11.816 | 11.816 | 11.816 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 109612) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 109619) rss_mb | MB | 1 | 11.668 | 11.668 | 11.668 | 11.668 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 109619) vms_mb | MB | 1 | 1498.223 | 1498.223 | 1498.223 | 1498.223 | n/a | n/a |
| docker (PID 109650) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 109650) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109650) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109650) rss_mb | MB | 2 | 25.891 | 25.891 | 25.891 | 25.891 | n/a | n/a |
| docker (PID 109650) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 109651) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 109651) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109651) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109651) rss_mb | MB | 2 | 26.996 | 26.996 | 26.996 | 26.996 | n/a | n/a |
| docker (PID 109651) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 109759) rss_mb | MB | 1 | 20.125 | 20.125 | 20.125 | 20.125 | n/a | n/a |
| docker (PID 109759) vms_mb | MB | 1 | 1524.203 | 1524.203 | 1524.203 | 1524.203 | n/a | n/a |
| docker (PID 109783) CPU | percent | 54 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 109783) io read MB/s | MB/s | 54 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109783) io write MB/s | MB/s | 54 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109783) rss_mb | MB | 55 | 26.629 | 26.629 | 26.629 | 26.629 | n/a | n/a |
| docker (PID 109783) vms_mb | MB | 55 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 109799) rss_mb | MB | 1 | 5.625 | 5.625 | 5.625 | 5.625 | n/a | n/a |
| docker (PID 109799) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 109816) rss_mb | MB | 1 | 25.734 | 25.734 | 25.734 | 25.734 | n/a | n/a |
| docker (PID 109816) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 109825) CPU | percent | 53 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 109825) io read MB/s | MB/s | 53 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109825) io write MB/s | MB/s | 53 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 109825) rss_mb | MB | 54 | 25.816 | 25.816 | 25.816 | 25.816 | n/a | n/a |
| docker (PID 109825) vms_mb | MB | 54 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 109857) rss_mb | MB | 1 | 17.004 | 17.004 | 17.004 | 17.004 | n/a | n/a |
| docker (PID 109857) vms_mb | MB | 1 | 1451.699 | 1451.699 | 1451.699 | 1451.699 | n/a | n/a |
| python3 (PID 109872) CPU | percent | 4 | 97.684 | 85.578 | 108.531 | 88.228 | 0.400000 CPU seconds | n/a |
| python3 (PID 109872) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 109872) io write MB/s | MB/s | 4 | 0.603 | 0.000 | 2.412 | 2.412 | 0.246094 MB | n/a |
| python3 (PID 109872) rss_mb | MB | 5 | 27.737 | 16.996 | 34.531 | 34.531 | n/a | n/a |
| python3 (PID 109872) vms_mb | MB | 5 | 51.343 | 41.172 | 57.457 | 57.457 | n/a | n/a |
| docker (PID 109890) rss_mb | MB | 1 | 25.973 | 25.973 | 25.973 | 25.973 | n/a | n/a |
| docker (PID 109890) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 109906) rss_mb | MB | 1 | 15.707 | 15.707 | 15.707 | 15.707 | n/a | n/a |
| docker (PID 109906) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| python3 (PID 109913) CPU | percent | 3 | 98.879 | 98.766 | 98.986 | 98.885 | 0.300000 CPU seconds | n/a |
| python3 (PID 109913) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 109913) io write MB/s | MB/s | 3 | 0.747 | 0.000 | 2.240 | 2.240 | 0.226562 MB | n/a |
| python3 (PID 109913) rss_mb | MB | 4 | 24.787 | 12.602 | 34.305 | 34.305 | n/a | n/a |
| python3 (PID 109913) vms_mb | MB | 4 | 49.062 | 38.426 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 109940) rss_mb | MB | 1 | 16.465 | 16.465 | 16.465 | 16.465 | n/a | n/a |
| docker (PID 109940) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 109955) rss_mb | MB | 1 | 11.051 | 11.051 | 11.051 | 11.051 | n/a | n/a |
| docker (PID 109955) vms_mb | MB | 1 | 1451.949 | 1451.949 | 1451.949 | 1451.949 | n/a | n/a |
| docker (PID 109979) rss_mb | MB | 1 | 25.281 | 25.281 | 25.281 | 25.281 | n/a | n/a |
| docker (PID 109979) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 109987) rss_mb | MB | 1 | 26.965 | 26.965 | 26.965 | 26.965 | n/a | n/a |
| docker (PID 109987) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 110001) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 110001) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 110001) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 110001) rss_mb | MB | 3 | 27.211 | 26.930 | 27.352 | 27.352 | n/a | n/a |
| docker (PID 110001) vms_mb | MB | 3 | 1708.776 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [arch_0000] (PID 110042) CPU | percent | 5 | 5.836 | 0.000 | 29.182 | 0.000 | 0.030000 CPU seconds | n/a |
| docker-init [arch_0000] (PID 110042) rss_mb | MB | 6 | 2.510 | 0.633 | 11.898 | 0.633 | n/a | n/a |
| docker-init [arch_0000] (PID 110042) vms_mb | MB | 6 | 250.561 | 1.055 | 1498.094 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 110053) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 110053) rss_mb | MB | 5 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [arch_0000] (PID 110053) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 110056) rss_mb | MB | 1 | 27.301 | 27.301 | 27.301 | 27.301 | n/a | n/a |
| docker (PID 110056) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 110091) rss_mb | MB | 1 | 27.441 | 27.441 | 27.441 | 27.441 | n/a | n/a |
| docker (PID 110091) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 110134) rss_mb | MB | 1 | 27.684 | 27.684 | 27.684 | 27.684 | n/a | n/a |
| docker (PID 110134) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 110135) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 110135) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 110135) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 110135) rss_mb | MB | 3 | 27.056 | 26.645 | 27.262 | 27.262 | n/a | n/a |
| docker (PID 110135) vms_mb | MB | 3 | 1709.026 | 1661.023 | 1733.027 | 1733.027 | n/a | n/a |
| runc:[0:PARENT] [arch_0000] (PID 110159) rss_mb | MB | 1 | 1.996 | 1.996 | 1.996 | 1.996 | n/a | n/a |
| runc:[0:PARENT] [arch_0000] (PID 110159) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| docker (PID 110179) rss_mb | MB | 1 | 27.293 | 27.293 | 27.293 | 27.293 | n/a | n/a |
| docker (PID 110179) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [bake_0000] (PID 110237) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bake_0000] (PID 110237) rss_mb | MB | 6 | 2.632 | 0.633 | 12.625 | 0.633 | n/a | n/a |
| docker-init [bake_0000] (PID 110237) vms_mb | MB | 6 | 262.583 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| docker (PID 110258) CPU | percent | 1 | 9.632 | 9.632 | 9.632 | 9.632 | 0.010000 CPU seconds | n/a |
| docker (PID 110258) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 110258) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 110258) rss_mb | MB | 2 | 18.094 | 9.238 | 26.949 | 26.949 | n/a | n/a |
| docker (PID 110258) vms_mb | MB | 2 | 1456.234 | 1251.695 | 1660.773 | 1660.773 | n/a | n/a |
| tail [bake_0000] (PID 110268) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 110268) rss_mb | MB | 5 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [bake_0000] (PID 110268) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 110272) rss_mb | MB | 1 | 27.250 | 27.250 | 27.250 | 27.250 | n/a | n/a |
| docker (PID 110272) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| mkdir (PID 110306) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| mkdir (PID 110306) vms_mb | MB | 1 | 0.215 | 0.215 | 0.215 | 0.215 | n/a | n/a |
| docker (PID 110342) rss_mb | MB | 1 | 27.004 | 27.004 | 27.004 | 27.004 | n/a | n/a |
| docker (PID 110342) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 110374) rss_mb | MB | 1 | 11.594 | 11.594 | 11.594 | 11.594 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 110374) vms_mb | MB | 1 | 1642.230 | 1642.230 | 1642.230 | 1642.230 | n/a | n/a |
| docker (PID 110389) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 110389) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 110389) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 110389) rss_mb | MB | 3 | 17.069 | 0.254 | 25.477 | 25.477 | n/a | n/a |
| docker (PID 110389) vms_mb | MB | 3 | 1116.997 | 30.570 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 110397) rss_mb | MB | 1 | 27.430 | 27.430 | 27.430 | 27.430 | n/a | n/a |
| docker (PID 110397) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 110436) rss_mb | MB | 1 | 12.039 | 12.039 | 12.039 | 12.039 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 110436) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 110454) CPU | percent | 5 | 7.490 | 0.000 | 37.452 | 0.000 | 0.040000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 110454) rss_mb | MB | 6 | 1.967 | 0.633 | 8.637 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 110454) vms_mb | MB | 6 | 262.453 | 1.055 | 1569.445 | 1.055 | n/a | n/a |
| docker (PID 110470) rss_mb | MB | 1 | 27.473 | 27.473 | 27.473 | 27.473 | n/a | n/a |
| docker (PID 110470) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| tail [arch_0000] (PID 110495) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 110495) rss_mb | MB | 5 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [arch_0000] (PID 110495) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 110497) rss_mb | MB | 1 | 3.930 | 3.930 | 3.930 | 3.930 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 110497) vms_mb | MB | 1 | 1216.680 | 1216.680 | 1216.680 | 1216.680 | n/a | n/a |
| docker (PID 110514) rss_mb | MB | 1 | 27.371 | 27.371 | 27.371 | 27.371 | n/a | n/a |
| docker (PID 110514) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 110539) rss_mb | MB | 1 | 2.570 | 2.570 | 2.570 | 2.570 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 110539) vms_mb | MB | 1 | 1111.484 | 1111.484 | 1111.484 | 1111.484 | n/a | n/a |
| docker (PID 110546) rss_mb | MB | 1 | 26.023 | 26.023 | 26.023 | 26.023 | n/a | n/a |
| docker (PID 110546) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 110557) rss_mb | MB | 1 | 27.391 | 27.391 | 27.391 | 27.391 | n/a | n/a |
| docker (PID 110557) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 110619) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 110619) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 110636) rss_mb | MB | 1 | 26.930 | 26.930 | 26.930 | 26.930 | n/a | n/a |
| docker (PID 110636) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 110638) rss_mb | MB | 1 | 27.203 | 27.203 | 27.203 | 27.203 | n/a | n/a |
| docker (PID 110638) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 110674) rss_mb | MB | 1 | 12.246 | 12.246 | 12.246 | 12.246 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 110674) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 110700) CPU | percent | 4 | 7.105 | 0.000 | 28.419 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 110700) rss_mb | MB | 5 | 2.654 | 0.633 | 10.738 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 110700) vms_mb | MB | 5 | 300.282 | 1.055 | 1497.191 | 1.055 | n/a | n/a |
| docker (PID 110715) rss_mb | MB | 1 | 25.828 | 25.828 | 25.828 | 25.828 | n/a | n/a |
| docker (PID 110715) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| tail [bake_0000] (PID 110734) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 110734) rss_mb | MB | 4 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [bake_0000] (PID 110734) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 110737) rss_mb | MB | 1 | 23.527 | 23.527 | 23.527 | 23.527 | n/a | n/a |
| docker (PID 110737) vms_mb | MB | 1 | 1660.207 | 1660.207 | 1660.207 | 1660.207 | n/a | n/a |
| docker (PID 110766) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 110766) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 110844) rss_mb | MB | 1 | 19.938 | 19.938 | 19.938 | 19.938 | n/a | n/a |
| docker (PID 110844) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 110883) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 110883) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 110883) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 110883) rss_mb | MB | 2 | 27.016 | 27.016 | 27.016 | 27.016 | n/a | n/a |
| docker (PID 110883) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 110951) rss_mb | MB | 1 | 25.902 | 25.902 | 25.902 | 25.902 | n/a | n/a |
| docker (PID 110951) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 110965) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 110965) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 110965) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 110965) rss_mb | MB | 38 | 26.742 | 26.742 | 26.742 | 26.742 | n/a | n/a |
| docker (PID 110965) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 111008) rss_mb | MB | 1 | 25.539 | 25.539 | 25.539 | 25.539 | n/a | n/a |
| docker (PID 111008) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bake_0000] (PID 111048) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bake_0000] (PID 111048) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bake_0000] (PID 111048) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 111060) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 111060) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [bake_0000] (PID 111060) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 111062) rss_mb | MB | 1 | 25.328 | 25.328 | 25.328 | 25.328 | n/a | n/a |
| docker (PID 111062) vms_mb | MB | 1 | 1596.211 | 1596.211 | 1596.211 | 1596.211 | n/a | n/a |
| docker (PID 111098) rss_mb | MB | 1 | 27.414 | 27.414 | 27.414 | 27.414 | n/a | n/a |
| docker (PID 111098) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 111135) rss_mb | MB | 1 | 27.469 | 27.469 | 27.469 | 27.469 | n/a | n/a |
| docker (PID 111135) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[0:PARENT] [bake_0000] (PID 111152) rss_mb | MB | 1 | 1.941 | 1.941 | 1.941 | 1.941 | n/a | n/a |
| runc:[0:PARENT] [bake_0000] (PID 111152) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[0:PARENT] [bake_0000] (PID 111154) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[0:PARENT] [bake_0000] (PID 111154) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| docker (PID 111176) rss_mb | MB | 1 | 26.125 | 26.125 | 26.125 | 26.125 | n/a | n/a |
| docker (PID 111176) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 111226) rss_mb | MB | 1 | 14.938 | 14.938 | 14.938 | 14.938 | n/a | n/a |
| docker (PID 111226) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 111256) CPU | percent | 48 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 111256) io read MB/s | MB/s | 48 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 111256) io write MB/s | MB/s | 48 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 111256) rss_mb | MB | 49 | 25.359 | 25.359 | 25.359 | 25.359 | n/a | n/a |
| docker (PID 111256) vms_mb | MB | 49 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 111271) CPU | percent | 1 | 19.651 | 19.651 | 19.651 | 19.651 | 0.020000 CPU seconds | n/a |
| docker (PID 111271) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 111271) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 111271) rss_mb | MB | 2 | 22.502 | 17.961 | 27.043 | 27.043 | n/a | n/a |
| docker (PID 111271) vms_mb | MB | 2 | 1588.361 | 1515.949 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 111310) CPU | percent | 17 | 2.239 | 0.000 | 38.067 | 0.000 | 0.040000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 111310) rss_mb | MB | 18 | 1.146 | 0.633 | 9.863 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 111310) vms_mb | MB | 18 | 88.174 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 111324) CPU | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 111324) rss_mb | MB | 17 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bake_0000] (PID 111324) vms_mb | MB | 17 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 111334) rss_mb | MB | 1 | 27.574 | 27.574 | 27.574 | 27.574 | n/a | n/a |
| docker (PID 111334) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 111353) rss_mb | MB | 1 | 11.195 | 11.195 | 11.195 | 11.195 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 111353) vms_mb | MB | 1 | 1570.082 | 1570.082 | 1570.082 | 1570.082 | n/a | n/a |
| docker (PID 111360) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 111360) io read MB/s | MB/s | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 111360) io write MB/s | MB/s | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 111360) rss_mb | MB | 14 | 27.348 | 27.348 | 27.348 | 27.348 | n/a | n/a |
| docker (PID 111360) vms_mb | MB | 14 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 111380) CPU | percent | 13 | 1.451 | 0.000 | 18.868 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 111380) rss_mb | MB | 14 | 4.025 | 3.418 | 11.922 | 3.418 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 111380) vms_mb | MB | 14 | 111.700 | 4.391 | 1506.727 | 4.391 | n/a | n/a |
| python [bake_0000] (PID 111389) CPU | percent | 12 | 97.578 | 93.873 | 106.433 | 95.872 | 1.220000 CPU seconds | n/a |
| python [bake_0000] (PID 111389) rss_mb | MB | 13 | 31.537 | 11.875 | 40.910 | 40.910 | n/a | n/a |
| python [bake_0000] (PID 111389) vms_mb | MB | 13 | 38.580 | 16.207 | 50.375 | 50.375 | n/a | n/a |
| docker (PID 111391) rss_mb | MB | 1 | 24.059 | 24.059 | 24.059 | 24.059 | n/a | n/a |
| docker (PID 111391) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 111400) rss_mb | MB | 1 | 25.996 | 25.996 | 25.996 | 25.996 | n/a | n/a |
| docker (PID 111400) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 111435) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 111435) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 111452) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 111452) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 111452) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 111452) rss_mb | MB | 2 | 25.527 | 25.527 | 25.527 | 25.527 | n/a | n/a |
| docker (PID 111452) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 111493) CPU | percent | 5 | 3.798 | 0.000 | 18.990 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 111493) rss_mb | MB | 6 | 2.607 | 0.633 | 12.480 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 111493) vms_mb | MB | 6 | 262.625 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 111505) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 111505) rss_mb | MB | 5 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [bake_0000] (PID 111505) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 111515) rss_mb | MB | 1 | 20.684 | 20.684 | 20.684 | 20.684 | n/a | n/a |
| docker (PID 111515) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 111543) rss_mb | MB | 1 | 24.070 | 24.070 | 24.070 | 24.070 | n/a | n/a |
| docker (PID 111543) vms_mb | MB | 1 | 1596.211 | 1596.211 | 1596.211 | 1596.211 | n/a | n/a |
| docker (PID 111570) rss_mb | MB | 1 | 14.062 | 14.062 | 14.062 | 14.062 | n/a | n/a |
| docker (PID 111570) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 111578) rss_mb | MB | 1 | 26.754 | 26.754 | 26.754 | 26.754 | n/a | n/a |
| docker (PID 111578) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 111598) rss_mb | MB | 1 | 11.586 | 11.586 | 11.586 | 11.586 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 111598) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 111614) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 111614) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 111614) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 111614) rss_mb | MB | 2 | 26.141 | 26.141 | 26.141 | 26.141 | n/a | n/a |
| docker (PID 111614) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 111701) rss_mb | MB | 1 | 7.512 | 7.512 | 7.512 | 7.512 | n/a | n/a |
| docker (PID 111701) vms_mb | MB | 1 | 32.867 | 32.867 | 32.867 | 32.867 | n/a | n/a |
| docker (PID 111703) rss_mb | MB | 1 | 2.535 | 2.535 | 2.535 | 2.535 | n/a | n/a |
| docker (PID 111703) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 111719) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 111719) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 111719) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 111719) rss_mb | MB | 2 | 26.684 | 26.684 | 26.684 | 26.684 | n/a | n/a |
| docker (PID 111719) vms_mb | MB | 2 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 111733) rss_mb | MB | 1 | 25.438 | 25.438 | 25.438 | 25.438 | n/a | n/a |
| docker (PID 111733) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 111775) CPU | percent | 48 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 111775) io read MB/s | MB/s | 48 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 111775) io write MB/s | MB/s | 48 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 111775) rss_mb | MB | 49 | 27.016 | 27.016 | 27.016 | 27.016 | n/a | n/a |
| docker (PID 111775) vms_mb | MB | 49 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 111777) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 111777) rss_mb | MB | 5 | 3.091 | 0.633 | 12.922 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 111777) vms_mb | MB | 5 | 314.939 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 111795) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 111795) rss_mb | MB | 4 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [arch_0000] (PID 111795) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 111806) rss_mb | MB | 1 | 17.809 | 17.809 | 17.809 | 17.809 | n/a | n/a |
| docker (PID 111806) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 111834) rss_mb | MB | 1 | 26.809 | 26.809 | 26.809 | 26.809 | n/a | n/a |
| docker (PID 111834) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 111869) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 111869) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 111907) rss_mb | MB | 1 | 25.859 | 25.859 | 25.859 | 25.859 | n/a | n/a |
| docker (PID 111907) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 111949) rss_mb | MB | 1 | 9.242 | 9.242 | 9.242 | 9.242 | n/a | n/a |
| docker (PID 111949) vms_mb | MB | 1 | 1443.695 | 1443.695 | 1443.695 | 1443.695 | n/a | n/a |
| docker (PID 111966) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 111966) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 111966) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 111966) rss_mb | MB | 2 | 25.566 | 25.566 | 25.566 | 25.566 | n/a | n/a |
| docker (PID 111966) vms_mb | MB | 2 | 1627.961 | 1595.961 | 1659.961 | 1659.961 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 112005) CPU | percent | 17 | 1.728 | 0.000 | 29.382 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 112005) rss_mb | MB | 18 | 1.175 | 0.633 | 10.387 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 112005) vms_mb | MB | 18 | 88.201 | 1.055 | 1569.695 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 112019) CPU | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 112019) rss_mb | MB | 17 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [arch_0000] (PID 112019) vms_mb | MB | 17 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 112021) rss_mb | MB | 1 | 1.512 | 1.512 | 1.512 | 1.512 | n/a | n/a |
| docker (PID 112021) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 112030) rss_mb | MB | 1 | 27.613 | 27.613 | 27.613 | 27.613 | n/a | n/a |
| docker (PID 112030) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 112049) rss_mb | MB | 1 | 11.676 | 11.676 | 11.676 | 11.676 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 112049) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 112056) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 112056) io read MB/s | MB/s | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 112056) io write MB/s | MB/s | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 112056) rss_mb | MB | 14 | 27.227 | 27.227 | 27.227 | 27.227 | n/a | n/a |
| docker (PID 112056) vms_mb | MB | 14 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| bash [arch_0000] (PID 112076) CPU | percent | 13 | 0.752 | 0.000 | 9.771 | 0.000 | 0.010000 CPU seconds | n/a |
| bash [arch_0000] (PID 112076) rss_mb | MB | 14 | 3.459 | 3.332 | 3.469 | 3.469 | n/a | n/a |
| bash [arch_0000] (PID 112076) vms_mb | MB | 14 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [arch_0000] (PID 112085) CPU | percent | 12 | 96.423 | 85.625 | 105.492 | 94.634 | 1.220000 CPU seconds | n/a |
| python [arch_0000] (PID 112085) rss_mb | MB | 13 | 33.330 | 14.723 | 42.738 | 42.738 | n/a | n/a |
| python [arch_0000] (PID 112085) vms_mb | MB | 13 | 40.643 | 18.387 | 52.219 | 52.219 | n/a | n/a |
| docker (PID 112095) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 112095) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 112095) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 112095) rss_mb | MB | 2 | 26.000 | 26.000 | 26.000 | 26.000 | n/a | n/a |
| docker (PID 112095) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 112163) rss_mb | MB | 1 | 24.488 | 24.488 | 24.488 | 24.488 | n/a | n/a |
| docker (PID 112163) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| python3 (PID 112178) CPU | percent | 3 | 95.529 | 88.960 | 98.910 | 88.960 | 0.290000 CPU seconds | n/a |
| python3 (PID 112178) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 112178) io write MB/s | MB/s | 3 | 0.811 | 0.000 | 2.433 | 2.433 | 0.246094 MB | n/a |
| python3 (PID 112178) rss_mb | MB | 4 | 24.675 | 10.730 | 34.488 | 34.488 | n/a | n/a |
| python3 (PID 112178) vms_mb | MB | 4 | 48.658 | 36.633 | 57.457 | 57.457 | n/a | n/a |
| docker (PID 112191) rss_mb | MB | 1 | 20.414 | 20.414 | 20.414 | 20.414 | n/a | n/a |
| docker (PID 112191) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 112229) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 112229) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 112229) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 112229) rss_mb | MB | 2 | 26.986 | 26.734 | 27.238 | 27.238 | n/a | n/a |
| docker (PID 112229) vms_mb | MB | 2 | 1696.775 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [bale_0000] (PID 112269) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bale_0000] (PID 112269) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bale_0000] (PID 112269) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 112282) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 112282) rss_mb | MB | 4 | 1.809 | 1.809 | 1.809 | 1.809 | n/a | n/a |
| tail [bale_0000] (PID 112282) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 112284) rss_mb | MB | 1 | 24.133 | 24.133 | 24.133 | 24.133 | n/a | n/a |
| docker (PID 112284) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 112321) rss_mb | MB | 1 | 27.375 | 27.375 | 27.375 | 27.375 | n/a | n/a |
| docker (PID 112321) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 112367) rss_mb | MB | 1 | 27.516 | 27.516 | 27.516 | 27.516 | n/a | n/a |
| docker (PID 112367) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 112404) rss_mb | MB | 1 | 27.219 | 27.219 | 27.219 | 27.219 | n/a | n/a |
| docker (PID 112404) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 112423) rss_mb | MB | 1 | 11.398 | 11.398 | 11.398 | 11.398 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 112423) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 112440) rss_mb | MB | 1 | 27.129 | 27.129 | 27.129 | 27.129 | n/a | n/a |
| docker (PID 112440) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 112491) rss_mb | MB | 1 | 13.969 | 13.969 | 13.969 | 13.969 | n/a | n/a |
| docker (PID 112491) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 112499) rss_mb | MB | 1 | 25.371 | 25.371 | 25.371 | 25.371 | n/a | n/a |
| docker (PID 112499) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 112538) CPU | percent | 3 | 6.445 | 0.000 | 19.336 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 112538) rss_mb | MB | 4 | 2.967 | 0.594 | 10.086 | 0.594 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 112538) vms_mb | MB | 4 | 393.090 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 112551) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 112551) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bale_0000] (PID 112551) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 112561) rss_mb | MB | 1 | 26.020 | 26.020 | 26.020 | 26.020 | n/a | n/a |
| docker (PID 112561) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 112587) rss_mb | MB | 1 | 27.395 | 27.395 | 27.395 | 27.395 | n/a | n/a |
| docker (PID 112587) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 112605) rss_mb | MB | 1 | 11.410 | 11.410 | 11.410 | 11.410 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 112605) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 112649) rss_mb | MB | 1 | 2.062 | 2.062 | 2.062 | 2.062 | n/a | n/a |
| docker (PID 112649) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 112657) rss_mb | MB | 1 | 25.875 | 25.875 | 25.875 | 25.875 | n/a | n/a |
| docker (PID 112657) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 112733) CPU | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 112733) io read MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 112733) io write MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 112733) rss_mb | MB | 40 | 25.240 | 1.555 | 25.848 | 25.848 | n/a | n/a |
| docker (PID 112733) vms_mb | MB | 40 | 1619.525 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 112749) rss_mb | MB | 1 | 26.676 | 26.676 | 26.676 | 26.676 | n/a | n/a |
| docker (PID 112749) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 112773) rss_mb | MB | 1 | 23.594 | 23.594 | 23.594 | 23.594 | n/a | n/a |
| docker (PID 112773) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| python3 (PID 112781) CPU | percent | 3 | 98.830 | 98.599 | 98.955 | 98.937 | 0.300000 CPU seconds | n/a |
| python3 (PID 112781) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 112781) io write MB/s | MB/s | 3 | 0.812 | 0.000 | 2.435 | 2.435 | 0.246094 MB | n/a |
| python3 (PID 112781) rss_mb | MB | 4 | 28.366 | 17.938 | 34.773 | 34.773 | n/a | n/a |
| python3 (PID 112781) vms_mb | MB | 4 | 51.818 | 42.434 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 112800) rss_mb | MB | 1 | 20.230 | 20.230 | 20.230 | 20.230 | n/a | n/a |
| docker (PID 112800) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 112833) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 112833) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 112833) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 112833) rss_mb | MB | 3 | 27.408 | 27.121 | 27.551 | 27.551 | n/a | n/a |
| docker (PID 112833) vms_mb | MB | 3 | 1708.776 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [band_0000] (PID 112873) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [band_0000] (PID 112873) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [band_0000] (PID 112873) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 112885) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 112885) rss_mb | MB | 4 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [band_0000] (PID 112885) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 112923) rss_mb | MB | 1 | 8.477 | 8.477 | 8.477 | 8.477 | n/a | n/a |
| docker (PID 112923) vms_mb | MB | 1 | 106.242 | 106.242 | 106.242 | 106.242 | n/a | n/a |
| docker (PID 112950) rss_mb | MB | 1 | 27.371 | 27.371 | 27.371 | 27.371 | n/a | n/a |
| docker (PID 112950) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 112971) rss_mb | MB | 1 | 10.816 | 10.816 | 10.816 | 10.816 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 112971) vms_mb | MB | 1 | 1569.711 | 1569.711 | 1569.711 | 1569.711 | n/a | n/a |
| docker (PID 112986) rss_mb | MB | 1 | 27.328 | 27.328 | 27.328 | 27.328 | n/a | n/a |
| docker (PID 112986) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 113006) rss_mb | MB | 1 | 12.375 | 12.375 | 12.375 | 12.375 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 113006) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 113022) rss_mb | MB | 1 | 27.148 | 27.148 | 27.148 | 27.148 | n/a | n/a |
| docker (PID 113022) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 113071) rss_mb | MB | 1 | 13.910 | 13.910 | 13.910 | 13.910 | n/a | n/a |
| docker (PID 113071) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 113079) rss_mb | MB | 1 | 25.512 | 25.512 | 25.512 | 25.512 | n/a | n/a |
| docker (PID 113079) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 113119) CPU | percent | 3 | 3.257 | 0.000 | 9.772 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 113119) rss_mb | MB | 4 | 3.492 | 0.633 | 12.070 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 113119) vms_mb | MB | 4 | 393.315 | 1.055 | 1570.098 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 113131) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 113131) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [band_0000] (PID 113131) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 113141) rss_mb | MB | 1 | 27.059 | 27.059 | 27.059 | 27.059 | n/a | n/a |
| docker (PID 113141) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 113168) rss_mb | MB | 1 | 27.270 | 27.270 | 27.270 | 27.270 | n/a | n/a |
| docker (PID 113168) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| sh [band_0000] (PID 113187) rss_mb | MB | 1 | 0.129 | 0.129 | 0.129 | 0.129 | n/a | n/a |
| sh [band_0000] (PID 113187) vms_mb | MB | 1 | 2.484 | 2.484 | 2.484 | 2.484 | n/a | n/a |
| docker (PID 113232) rss_mb | MB | 1 | 15.992 | 15.992 | 15.992 | 15.992 | n/a | n/a |
| docker (PID 113232) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 113240) rss_mb | MB | 1 | 25.977 | 25.977 | 25.977 | 25.977 | n/a | n/a |
| docker (PID 113240) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 113293) rss_mb | MB | 1 | 23.371 | 23.371 | 23.371 | 23.371 | n/a | n/a |
| docker (PID 113293) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 113324) CPU | percent | 56 | 0.170 | 0.000 | 9.503 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 113324) io read MB/s | MB/s | 56 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 113324) io write MB/s | MB/s | 56 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 113324) rss_mb | MB | 57 | 26.383 | 21.785 | 26.465 | 26.465 | n/a | n/a |
| docker (PID 113324) vms_mb | MB | 57 | 1730.241 | 1588.203 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 113345) rss_mb | MB | 1 | 25.875 | 25.875 | 25.875 | 25.875 | n/a | n/a |
| docker (PID 113345) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 113371) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 113371) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 113371) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 113371) rss_mb | MB | 2 | 26.555 | 26.555 | 26.555 | 26.555 | n/a | n/a |
| docker (PID 113371) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 113410) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 113410) rss_mb | MB | 4 | 3.721 | 0.633 | 12.984 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 113410) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 113422) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 113422) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bale_0000] (PID 113422) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 113432) rss_mb | MB | 1 | 27.215 | 27.215 | 27.215 | 27.215 | n/a | n/a |
| docker (PID 113432) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 113452) rss_mb | MB | 1 | 11.879 | 11.879 | 11.879 | 11.879 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 113452) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 113488) rss_mb | MB | 1 | 25.203 | 25.203 | 25.203 | 25.203 | n/a | n/a |
| docker (PID 113488) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 113536) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 113536) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 113536) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 113536) rss_mb | MB | 2 | 13.842 | 1.758 | 25.926 | 25.926 | n/a | n/a |
| docker (PID 113536) vms_mb | MB | 2 | 846.486 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 113596) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 113596) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 113596) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 113596) rss_mb | MB | 2 | 27.031 | 27.031 | 27.031 | 27.031 | n/a | n/a |
| docker (PID 113596) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 113637) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 113637) rss_mb | MB | 38 | 0.953 | 0.633 | 12.793 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 113637) vms_mb | MB | 38 | 42.349 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 113650) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 113650) rss_mb | MB | 37 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [bale_0000] (PID 113650) vms_mb | MB | 37 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 113660) rss_mb | MB | 1 | 27.078 | 27.078 | 27.078 | 27.078 | n/a | n/a |
| docker (PID 113660) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 113679) rss_mb | MB | 1 | 11.941 | 11.941 | 11.941 | 11.941 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 113679) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 113686) CPU | percent | 34 | 0.577 | 0.000 | 19.623 | 19.623 | 0.020000 CPU seconds | n/a |
| docker (PID 113686) io read MB/s | MB/s | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 113686) io write MB/s | MB/s | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 113686) rss_mb | MB | 35 | 27.512 | 27.512 | 27.512 | 27.512 | n/a | n/a |
| docker (PID 113686) vms_mb | MB | 35 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [bale_0000] (PID 113705) CPU | percent | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bale_0000] (PID 113705) rss_mb | MB | 35 | 3.355 | 3.355 | 3.355 | 3.355 | n/a | n/a |
| bash [bale_0000] (PID 113705) vms_mb | MB | 35 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bale_0000] (PID 113715) CPU | percent | 34 | 100.090 | 88.236 | 108.017 | 98.116 | 3.470000 CPU seconds | n/a |
| python [bale_0000] (PID 113715) rss_mb | MB | 35 | 38.833 | 10.172 | 41.266 | 41.266 | n/a | n/a |
| python [bale_0000] (PID 113715) vms_mb | MB | 35 | 48.259 | 14.531 | 51.324 | 51.324 | n/a | n/a |
| docker (PID 113725) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 113725) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 113725) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 113725) rss_mb | MB | 2 | 16.893 | 8.008 | 25.777 | 25.777 | n/a | n/a |
| docker (PID 113725) vms_mb | MB | 2 | 846.539 | 32.867 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 113786) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 113786) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 113786) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 113786) rss_mb | MB | 2 | 25.637 | 25.637 | 25.637 | 25.637 | n/a | n/a |
| docker (PID 113786) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 113827) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 113827) rss_mb | MB | 4 | 3.708 | 0.633 | 12.934 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 113827) vms_mb | MB | 4 | 411.349 | 1.055 | 1642.230 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 113840) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 113840) rss_mb | MB | 3 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [bale_0000] (PID 113840) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 113851) rss_mb | MB | 1 | 27.176 | 27.176 | 27.176 | 27.176 | n/a | n/a |
| docker (PID 113851) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 113871) rss_mb | MB | 1 | 12.375 | 12.375 | 12.375 | 12.375 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 113871) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 113915) rss_mb | MB | 1 | 20.191 | 20.191 | 20.191 | 20.191 | n/a | n/a |
| docker (PID 113915) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 113955) rss_mb | MB | 1 | 26.168 | 26.168 | 26.168 | 26.168 | n/a | n/a |
| docker (PID 113955) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 113995) rss_mb | MB | 1 | 5.781 | 5.781 | 5.781 | 5.781 | n/a | n/a |
| docker (PID 113995) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 114036) CPU | percent | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 114036) io read MB/s | MB/s | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 114036) io write MB/s | MB/s | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 114036) rss_mb | MB | 44 | 25.449 | 5.289 | 25.918 | 25.918 | n/a | n/a |
| docker (PID 114036) vms_mb | MB | 44 | 1623.223 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 114044) rss_mb | MB | 1 | 8.992 | 8.992 | 8.992 | 8.992 | n/a | n/a |
| docker (PID 114044) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 114069) rss_mb | MB | 1 | 18.945 | 18.945 | 18.945 | 18.945 | n/a | n/a |
| docker (PID 114069) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 114077) CPU | percent | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 114077) io read MB/s | MB/s | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 114077) io write MB/s | MB/s | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 114077) rss_mb | MB | 44 | 26.633 | 26.633 | 26.633 | 26.633 | n/a | n/a |
| docker (PID 114077) vms_mb | MB | 44 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 114103) rss_mb | MB | 1 | 17.598 | 17.598 | 17.598 | 17.598 | n/a | n/a |
| docker (PID 114103) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 114137) rss_mb | MB | 1 | 26.027 | 26.027 | 26.027 | 26.027 | n/a | n/a |
| docker (PID 114137) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| python3 (PID 114152) CPU | percent | 27 | 96.266 | 77.124 | 108.910 | 98.870 | 2.670000 CPU seconds | n/a |
| python3 (PID 114152) io read MB/s | MB/s | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 114152) io write MB/s | MB/s | 27 | 0.090 | 0.000 | 2.433 | 2.433 | 0.246094 MB | n/a |
| python3 (PID 114152) rss_mb | MB | 28 | 32.779 | 15.531 | 34.539 | 34.539 | n/a | n/a |
| python3 (PID 114152) vms_mb | MB | 28 | 56.497 | 40.898 | 57.461 | 57.438 | n/a | n/a |
| docker (PID 114162) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 114162) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 114162) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 114162) rss_mb | MB | 2 | 25.621 | 25.621 | 25.621 | 25.621 | n/a | n/a |
| docker (PID 114162) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 114201) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 114201) rss_mb | MB | 4 | 3.627 | 0.633 | 12.609 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 114201) vms_mb | MB | 4 | 375.347 | 1.055 | 1498.223 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 114214) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 114214) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [band_0000] (PID 114214) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 114225) rss_mb | MB | 1 | 27.195 | 27.195 | 27.195 | 27.195 | n/a | n/a |
| docker (PID 114225) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 114243) rss_mb | MB | 1 | 7.281 | 7.281 | 7.281 | 7.281 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 114243) vms_mb | MB | 1 | 1569.195 | 1569.195 | 1569.195 | 1569.195 | n/a | n/a |
| docker (PID 114250) rss_mb | MB | 1 | 26.996 | 26.996 | 26.996 | 26.996 | n/a | n/a |
| docker (PID 114250) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 114285) rss_mb | MB | 1 | 27.348 | 27.348 | 27.348 | 27.348 | n/a | n/a |
| docker (PID 114285) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 114306) rss_mb | MB | 1 | 12.449 | 12.449 | 12.449 | 12.449 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 114306) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 114325) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 114325) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 114325) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 114325) rss_mb | MB | 2 | 26.996 | 26.996 | 26.996 | 26.996 | n/a | n/a |
| docker (PID 114325) vms_mb | MB | 2 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 114385) rss_mb | MB | 1 | 22.750 | 22.750 | 22.750 | 22.750 | n/a | n/a |
| docker (PID 114385) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 114422) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 114422) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 114422) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 114422) rss_mb | MB | 2 | 18.078 | 10.430 | 25.727 | 25.727 | n/a | n/a |
| docker (PID 114422) vms_mb | MB | 2 | 1524.080 | 1387.949 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 114462) CPU | percent | 10 | 0.976 | 0.000 | 9.759 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 114462) rss_mb | MB | 11 | 1.748 | 0.633 | 12.898 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 114462) vms_mb | MB | 11 | 150.275 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 114475) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 114475) rss_mb | MB | 10 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [band_0000] (PID 114475) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 114485) rss_mb | MB | 1 | 27.441 | 27.441 | 27.441 | 27.441 | n/a | n/a |
| docker (PID 114485) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 114505) rss_mb | MB | 1 | 10.590 | 10.590 | 10.590 | 10.590 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 114505) vms_mb | MB | 1 | 1569.453 | 1569.453 | 1569.453 | 1569.453 | n/a | n/a |
| docker (PID 114514) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 114514) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 114514) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 114514) rss_mb | MB | 8 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| docker (PID 114514) vms_mb | MB | 8 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [band_0000] (PID 114534) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [band_0000] (PID 114534) rss_mb | MB | 8 | 3.324 | 3.324 | 3.324 | 3.324 | n/a | n/a |
| bash [band_0000] (PID 114534) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [band_0000] (PID 114544) CPU | percent | 7 | 99.458 | 88.293 | 107.974 | 97.982 | 0.710000 CPU seconds | n/a |
| python [band_0000] (PID 114544) rss_mb | MB | 8 | 29.539 | 7.426 | 41.828 | 41.828 | n/a | n/a |
| python [band_0000] (PID 114544) vms_mb | MB | 8 | 36.250 | 11.938 | 51.324 | 51.324 | n/a | n/a |
| docker (PID 114546) rss_mb | MB | 1 | 11.027 | 11.027 | 11.027 | 11.027 | n/a | n/a |
| docker (PID 114546) vms_mb | MB | 1 | 1387.949 | 1387.949 | 1387.949 | 1387.949 | n/a | n/a |
| docker (PID 114554) rss_mb | MB | 1 | 26.027 | 26.027 | 26.027 | 26.027 | n/a | n/a |
| docker (PID 114554) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 114620) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 114620) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 114620) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 114620) rss_mb | MB | 2 | 27.326 | 26.984 | 27.668 | 27.668 | n/a | n/a |
| docker (PID 114620) vms_mb | MB | 2 | 1732.777 | 1660.773 | 1804.781 | 1804.781 | n/a | n/a |
| docker-init [bart_0000] (PID 114663) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bart_0000] (PID 114663) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bart_0000] (PID 114663) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 114677) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 114677) rss_mb | MB | 4 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [bart_0000] (PID 114677) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 114679) rss_mb | MB | 1 | 27.320 | 27.320 | 27.320 | 27.320 | n/a | n/a |
| docker (PID 114679) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 114714) rss_mb | MB | 1 | 27.129 | 27.129 | 27.129 | 27.129 | n/a | n/a |
| docker (PID 114714) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 114733) rss_mb | MB | 1 | 10.816 | 10.816 | 10.816 | 10.816 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 114733) vms_mb | MB | 1 | 1641.578 | 1641.578 | 1641.578 | 1641.578 | n/a | n/a |
| docker (PID 114769) rss_mb | MB | 1 | 19.574 | 19.574 | 19.574 | 19.574 | n/a | n/a |
| docker (PID 114769) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 114813) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 114813) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 114813) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 114813) rss_mb | MB | 2 | 20.895 | 14.906 | 26.883 | 26.883 | n/a | n/a |
| docker (PID 114813) vms_mb | MB | 2 | 1588.236 | 1515.949 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 114870) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 114870) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 114870) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 114870) rss_mb | MB | 2 | 26.535 | 26.535 | 26.535 | 26.535 | n/a | n/a |
| docker (PID 114870) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 114911) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 114911) rss_mb | MB | 4 | 3.656 | 0.633 | 12.727 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 114911) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 114923) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 114923) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [bart_0000] (PID 114923) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 114934) rss_mb | MB | 1 | 27.180 | 27.180 | 27.180 | 27.180 | n/a | n/a |
| docker (PID 114934) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 114954) rss_mb | MB | 1 | 11.578 | 11.578 | 11.578 | 11.578 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 114954) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 114996) rss_mb | MB | 1 | 6.523 | 6.523 | 6.523 | 6.523 | n/a | n/a |
| docker (PID 114996) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 115033) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 115033) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 115033) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 115033) rss_mb | MB | 2 | 26.711 | 26.711 | 26.711 | 26.711 | n/a | n/a |
| docker (PID 115033) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 115091) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 115091) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 115091) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 115091) rss_mb | MB | 2 | 26.023 | 26.023 | 26.023 | 26.023 | n/a | n/a |
| docker (PID 115091) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [band_0000] (PID 115131) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [band_0000] (PID 115131) rss_mb | MB | 4 | 0.475 | 0.000 | 0.633 | 0.633 | n/a | n/a |
| docker-init [band_0000] (PID 115131) vms_mb | MB | 4 | 1.021 | 0.922 | 1.055 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 115145) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 115145) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [band_0000] (PID 115145) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 115155) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 115155) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 115218) rss_mb | MB | 1 | 25.363 | 25.363 | 25.363 | 25.363 | n/a | n/a |
| docker (PID 115218) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 115254) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 115254) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 115254) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 115254) rss_mb | MB | 2 | 26.000 | 26.000 | 26.000 | 26.000 | n/a | n/a |
| docker (PID 115254) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 115312) rss_mb | MB | 1 | 23.172 | 23.172 | 23.172 | 23.172 | n/a | n/a |
| docker (PID 115312) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 115336) CPU | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 115336) io read MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 115336) io write MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 115336) rss_mb | MB | 40 | 26.637 | 26.637 | 26.637 | 26.637 | n/a | n/a |
| docker (PID 115336) vms_mb | MB | 40 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 115368) rss_mb | MB | 1 | 25.344 | 25.344 | 25.344 | 25.344 | n/a | n/a |
| docker (PID 115368) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| python3 (PID 115383) CPU | percent | 3 | 98.740 | 98.556 | 98.908 | 98.908 | 0.300000 CPU seconds | n/a |
| python3 (PID 115383) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 115383) io write MB/s | MB/s | 3 | 0.798 | 0.000 | 2.395 | 2.395 | 0.242188 MB | n/a |
| python3 (PID 115383) rss_mb | MB | 4 | 25.848 | 13.277 | 34.430 | 34.430 | n/a | n/a |
| python3 (PID 115383) vms_mb | MB | 4 | 50.024 | 39.430 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 115435) CPU | percent | 1 | 9.872 | 9.872 | 9.872 | 9.872 | 0.010000 CPU seconds | n/a |
| docker (PID 115435) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 115435) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 115435) rss_mb | MB | 2 | 27.377 | 27.066 | 27.688 | 27.688 | n/a | n/a |
| docker (PID 115435) vms_mb | MB | 2 | 1696.775 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [base_0000] (PID 115476) CPU | percent | 4 | 4.926 | 0.000 | 19.704 | 0.000 | 0.020000 CPU seconds | n/a |
| docker-init [base_0000] (PID 115476) rss_mb | MB | 5 | 2.709 | 0.633 | 11.016 | 0.633 | n/a | n/a |
| docker-init [base_0000] (PID 115476) vms_mb | MB | 5 | 314.683 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 115488) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 115488) rss_mb | MB | 4 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [base_0000] (PID 115488) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 115490) rss_mb | MB | 1 | 27.141 | 27.141 | 27.141 | 27.141 | n/a | n/a |
| docker (PID 115490) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] (PID 115510) rss_mb | MB | 1 | 10.246 | 10.246 | 10.246 | 10.246 | n/a | n/a |
| runc:[2:INIT] (PID 115510) vms_mb | MB | 1 | 1569.695 | 1569.695 | 1569.695 | 1569.695 | n/a | n/a |
| docker (PID 115526) rss_mb | MB | 1 | 27.164 | 27.164 | 27.164 | 27.164 | n/a | n/a |
| docker (PID 115526) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 115545) rss_mb | MB | 1 | 11.773 | 11.773 | 11.773 | 11.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 115545) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 115589) rss_mb | MB | 1 | 2.410 | 2.410 | 2.410 | 2.410 | n/a | n/a |
| docker (PID 115589) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 115626) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 115626) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 115626) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 115626) rss_mb | MB | 2 | 25.941 | 25.941 | 25.941 | 25.941 | n/a | n/a |
| docker (PID 115626) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 115684) rss_mb | MB | 1 | 26.590 | 26.590 | 26.590 | 26.590 | n/a | n/a |
| docker (PID 115684) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [base_0000] (PID 115722) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [base_0000] (PID 115722) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [base_0000] (PID 115722) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 115736) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 115736) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [base_0000] (PID 115736) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 115738) rss_mb | MB | 1 | 15.590 | 15.590 | 15.590 | 15.590 | n/a | n/a |
| docker (PID 115738) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 115774) rss_mb | MB | 1 | 27.234 | 27.234 | 27.234 | 27.234 | n/a | n/a |
| docker (PID 115774) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 115808) rss_mb | MB | 1 | 27.242 | 27.242 | 27.242 | 27.242 | n/a | n/a |
| docker (PID 115808) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 115828) rss_mb | MB | 1 | 10.938 | 10.938 | 10.938 | 10.938 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 115828) vms_mb | MB | 1 | 1641.578 | 1641.578 | 1641.578 | 1641.578 | n/a | n/a |
| docker (PID 115847) rss_mb | MB | 1 | 26.941 | 26.941 | 26.941 | 26.941 | n/a | n/a |
| docker (PID 115847) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 115889) rss_mb | MB | 1 | 19.090 | 19.090 | 19.090 | 19.090 | n/a | n/a |
| docker (PID 115889) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 115906) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 115906) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 115906) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 115906) rss_mb | MB | 2 | 27.027 | 27.027 | 27.027 | 27.027 | n/a | n/a |
| docker (PID 115906) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 115947) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 115947) rss_mb | MB | 3 | 4.686 | 0.633 | 12.793 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 115947) vms_mb | MB | 3 | 524.112 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 115960) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 115960) rss_mb | MB | 2 | 1.832 | 1.832 | 1.832 | 1.832 | n/a | n/a |
| tail [base_0000] (PID 115960) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 115970) rss_mb | MB | 1 | 27.281 | 27.281 | 27.281 | 27.281 | n/a | n/a |
| docker (PID 115970) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| run13:diagnose_ (PID 116031) rss_mb | MB | 1 | 695.254 | 695.254 | 695.254 | 695.254 | n/a | n/a |
| run13:diagnose_ (PID 116031) vms_mb | MB | 1 | 3971.336 | 3971.336 | 3971.336 | 3971.336 | n/a | n/a |
| docker (PID 116039) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 116039) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 116039) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 116039) rss_mb | MB | 2 | 26.969 | 26.969 | 26.969 | 26.969 | n/a | n/a |
| docker (PID 116039) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 116080) rss_mb | MB | 1 | 21.836 | 21.836 | 21.836 | 21.836 | n/a | n/a |
| docker (PID 116080) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 116097) rss_mb | MB | 1 | 26.777 | 26.777 | 26.777 | 26.777 | n/a | n/a |
| docker (PID 116097) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 116136) CPU | percent | 3 | 3.269 | 0.000 | 9.806 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 116136) rss_mb | MB | 4 | 3.577 | 0.633 | 12.410 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 116136) vms_mb | MB | 4 | 393.535 | 1.055 | 1570.977 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 116149) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 116149) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [base_0000] (PID 116149) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 116159) rss_mb | MB | 1 | 27.195 | 27.195 | 27.195 | 27.195 | n/a | n/a |
| docker (PID 116159) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 116252) rss_mb | MB | 1 | 23.895 | 23.895 | 23.895 | 23.895 | n/a | n/a |
| docker (PID 116252) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 116261) rss_mb | MB | 1 | 25.977 | 25.977 | 25.977 | 25.977 | n/a | n/a |
| docker (PID 116261) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 116320) rss_mb | MB | 1 | 24.371 | 24.371 | 24.371 | 24.371 | n/a | n/a |
| docker (PID 116320) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 116342) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 116342) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 116342) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 116342) rss_mb | MB | 39 | 26.281 | 26.281 | 26.281 | 26.281 | n/a | n/a |
| docker (PID 116342) vms_mb | MB | 39 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| run12:diagnose_ (PID 116366) rss_mb | MB | 1 | 695.879 | 695.879 | 695.879 | 695.879 | n/a | n/a |
| run12:diagnose_ (PID 116366) vms_mb | MB | 1 | 3972.336 | 3972.336 | 3972.336 | 3972.336 | n/a | n/a |
| docker (PID 116376) rss_mb | MB | 1 | 23.660 | 23.660 | 23.660 | 23.660 | n/a | n/a |
| docker (PID 116376) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 116384) rss_mb | MB | 1 | 25.773 | 25.773 | 25.773 | 25.773 | n/a | n/a |
| docker (PID 116384) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 116423) CPU | percent | 3 | 3.265 | 0.000 | 9.796 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 116423) rss_mb | MB | 4 | 3.562 | 0.633 | 12.348 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 116423) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 116435) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 116435) rss_mb | MB | 3 | 1.711 | 1.711 | 1.711 | 1.711 | n/a | n/a |
| tail [bart_0000] (PID 116435) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 116446) rss_mb | MB | 1 | 27.277 | 27.277 | 27.277 | 27.277 | n/a | n/a |
| docker (PID 116446) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 116470) rss_mb | MB | 1 | 27.621 | 27.621 | 27.621 | 27.621 | n/a | n/a |
| docker (PID 116470) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| sh [bart_0000] (PID 116490) rss_mb | MB | 1 | 1.582 | 1.582 | 1.582 | 1.582 | n/a | n/a |
| sh [bart_0000] (PID 116490) vms_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| docker (PID 116539) rss_mb | MB | 1 | 3.664 | 3.664 | 3.664 | 3.664 | n/a | n/a |
| docker (PID 116539) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 116547) rss_mb | MB | 1 | 27.070 | 27.070 | 27.070 | 27.070 | n/a | n/a |
| docker (PID 116547) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 116607) rss_mb | MB | 1 | 25.793 | 25.793 | 25.793 | 25.793 | n/a | n/a |
| docker (PID 116607) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 116648) CPU | percent | 10 | 1.927 | 0.000 | 19.272 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 116648) rss_mb | MB | 11 | 1.382 | 0.633 | 8.875 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 116648) vms_mb | MB | 11 | 143.613 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 116661) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 116661) rss_mb | MB | 10 | 1.672 | 1.672 | 1.672 | 1.672 | n/a | n/a |
| tail [bart_0000] (PID 116661) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 116671) rss_mb | MB | 1 | 16.438 | 16.438 | 16.438 | 16.438 | n/a | n/a |
| docker (PID 116671) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 116701) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 116701) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 116701) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 116701) rss_mb | MB | 9 | 26.980 | 26.980 | 26.980 | 26.980 | n/a | n/a |
| docker (PID 116701) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 116721) CPU | percent | 8 | 2.427 | 0.000 | 19.412 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 116721) rss_mb | MB | 9 | 4.160 | 3.328 | 10.812 | 3.328 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 116721) vms_mb | MB | 9 | 178.300 | 4.391 | 1569.574 | 4.391 | n/a | n/a |
| python [bart_0000] (PID 116730) CPU | percent | 7 | 99.266 | 88.211 | 107.825 | 98.004 | 0.710000 CPU seconds | n/a |
| python [bart_0000] (PID 116730) rss_mb | MB | 8 | 33.281 | 16.516 | 41.965 | 41.172 | n/a | n/a |
| python [bart_0000] (PID 116730) vms_mb | MB | 8 | 40.536 | 21.043 | 52.289 | 51.324 | n/a | n/a |
| docker (PID 116741) rss_mb | MB | 1 | 26.934 | 26.934 | 26.934 | 26.934 | n/a | n/a |
| docker (PID 116741) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 116800) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 116800) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 116800) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 116800) rss_mb | MB | 2 | 25.734 | 25.734 | 25.734 | 25.734 | n/a | n/a |
| docker (PID 116800) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bart_0000] (PID 116840) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bart_0000] (PID 116840) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bart_0000] (PID 116840) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 116852) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 116852) rss_mb | MB | 3 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [bart_0000] (PID 116852) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 116889) rss_mb | MB | 1 | 18.102 | 18.102 | 18.102 | 18.102 | n/a | n/a |
| docker (PID 116889) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 116924) rss_mb | MB | 1 | 27.055 | 27.055 | 27.055 | 27.055 | n/a | n/a |
| docker (PID 116924) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 116961) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 116961) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 116961) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 116961) rss_mb | MB | 2 | 26.055 | 26.055 | 26.055 | 26.055 | n/a | n/a |
| docker (PID 116961) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 117015) rss_mb | MB | 1 | 2.273 | 2.273 | 2.273 | 2.273 | n/a | n/a |
| docker (PID 117015) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 117039) rss_mb | MB | 1 | 25.746 | 25.746 | 25.746 | 25.746 | n/a | n/a |
| docker (PID 117039) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 117047) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 117047) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 117047) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 117047) rss_mb | MB | 39 | 25.633 | 25.633 | 25.633 | 25.633 | n/a | n/a |
| docker (PID 117047) vms_mb | MB | 39 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 117063) rss_mb | MB | 1 | 25.828 | 25.828 | 25.828 | 25.828 | n/a | n/a |
| docker (PID 117063) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 117089) rss_mb | MB | 1 | 26.703 | 26.703 | 26.703 | 26.703 | n/a | n/a |
| docker (PID 117089) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 117096) CPU | percent | 3 | 102.119 | 98.597 | 108.840 | 108.840 | 0.310000 CPU seconds | n/a |
| python3 (PID 117096) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 117096) io write MB/s | MB/s | 3 | 0.799 | 0.000 | 2.396 | 2.396 | 0.242188 MB | n/a |
| python3 (PID 117096) rss_mb | MB | 4 | 28.589 | 18.750 | 34.617 | 34.617 | n/a | n/a |
| python3 (PID 117096) vms_mb | MB | 4 | 52.136 | 43.703 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 117114) rss_mb | MB | 1 | 27.367 | 27.367 | 27.367 | 27.367 | n/a | n/a |
| docker (PID 117114) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 117147) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 117147) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 117147) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 117147) rss_mb | MB | 2 | 27.318 | 27.168 | 27.469 | 27.469 | n/a | n/a |
| docker (PID 117147) vms_mb | MB | 2 | 1697.025 | 1661.023 | 1733.027 | 1733.027 | n/a | n/a |
| docker-init [beam_0000] (PID 117187) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beam_0000] (PID 117187) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [beam_0000] (PID 117187) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 117199) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 117199) rss_mb | MB | 4 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [beam_0000] (PID 117199) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 117202) rss_mb | MB | 1 | 17.285 | 17.285 | 17.285 | 17.285 | n/a | n/a |
| docker (PID 117202) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 117238) rss_mb | MB | 1 | 27.219 | 27.219 | 27.219 | 27.219 | n/a | n/a |
| docker (PID 117238) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 117265) rss_mb | MB | 1 | 27.332 | 27.332 | 27.332 | 27.332 | n/a | n/a |
| docker (PID 117265) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 117285) rss_mb | MB | 1 | 12.371 | 12.371 | 12.371 | 12.371 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 117285) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 117329) rss_mb | MB | 1 | 3.719 | 3.719 | 3.719 | 3.719 | n/a | n/a |
| docker (PID 117329) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 117337) rss_mb | MB | 1 | 27.023 | 27.023 | 27.023 | 27.023 | n/a | n/a |
| docker (PID 117337) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 117395) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 117395) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 117395) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 117395) rss_mb | MB | 2 | 27.129 | 27.129 | 27.129 | 27.129 | n/a | n/a |
| docker (PID 117395) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 117435) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [beam_0000] (PID 117435) rss_mb | MB | 4 | 3.728 | 0.633 | 13.012 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 117435) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 117447) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 117447) rss_mb | MB | 3 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [beam_0000] (PID 117447) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 117457) rss_mb | MB | 1 | 27.207 | 27.207 | 27.207 | 27.207 | n/a | n/a |
| docker (PID 117457) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 117519) rss_mb | MB | 1 | 24.059 | 24.059 | 24.059 | 24.059 | n/a | n/a |
| docker (PID 117519) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 117558) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 117558) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 117558) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 117558) rss_mb | MB | 2 | 26.867 | 26.867 | 26.867 | 26.867 | n/a | n/a |
| docker (PID 117558) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 117627) rss_mb | MB | 1 | 26.863 | 26.863 | 26.863 | 26.863 | n/a | n/a |
| docker (PID 117627) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 117641) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 117641) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 117641) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 117641) rss_mb | MB | 38 | 26.816 | 26.816 | 26.816 | 26.816 | n/a | n/a |
| docker (PID 117641) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 117684) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 117684) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 117684) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 117684) rss_mb | MB | 2 | 25.336 | 25.336 | 25.336 | 25.336 | n/a | n/a |
| docker (PID 117684) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [base_0000] (PID 117724) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [base_0000] (PID 117724) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [base_0000] (PID 117724) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 117737) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 117737) rss_mb | MB | 3 | 1.777 | 1.777 | 1.777 | 1.777 | n/a | n/a |
| tail [base_0000] (PID 117737) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 117776) rss_mb | MB | 1 | 15.660 | 15.660 | 15.660 | 15.660 | n/a | n/a |
| docker (PID 117776) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 117812) rss_mb | MB | 1 | 27.617 | 27.617 | 27.617 | 27.617 | n/a | n/a |
| docker (PID 117812) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 117850) rss_mb | MB | 1 | 26.840 | 26.840 | 26.840 | 26.840 | n/a | n/a |
| docker (PID 117850) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 117895) rss_mb | MB | 1 | 19.098 | 19.098 | 19.098 | 19.098 | n/a | n/a |
| docker (PID 117895) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 117934) CPU | percent | 54 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 117934) io read MB/s | MB/s | 54 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 117934) io write MB/s | MB/s | 54 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 117934) rss_mb | MB | 55 | 25.675 | 20.785 | 25.766 | 25.766 | n/a | n/a |
| docker (PID 117934) vms_mb | MB | 55 | 1657.588 | 1515.949 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 117951) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 117951) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 117951) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 117951) rss_mb | MB | 2 | 25.344 | 25.344 | 25.344 | 25.344 | n/a | n/a |
| docker (PID 117951) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 117990) CPU | percent | 290 | 0.066 | 0.000 | 19.092 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 117990) rss_mb | MB | 291 | 0.672 | 0.633 | 12.074 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 117990) vms_mb | MB | 291 | 6.446 | 1.055 | 1569.977 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 118003) CPU | percent | 289 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 118003) rss_mb | MB | 290 | 1.711 | 1.711 | 1.711 | 1.711 | n/a | n/a |
| tail [base_0000] (PID 118003) vms_mb | MB | 290 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 118005) rss_mb | MB | 1 | 20.051 | 20.051 | 20.051 | 20.051 | n/a | n/a |
| docker (PID 118005) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 118013) rss_mb | MB | 1 | 27.375 | 27.375 | 27.375 | 27.375 | n/a | n/a |
| docker (PID 118013) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 118032) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 118032) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| docker (PID 118040) CPU | percent | 286 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 118040) io read MB/s | MB/s | 286 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 118040) io write MB/s | MB/s | 286 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 118040) rss_mb | MB | 287 | 27.492 | 27.492 | 27.492 | 27.492 | n/a | n/a |
| docker (PID 118040) vms_mb | MB | 287 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| bash [base_0000] (PID 118060) CPU | percent | 287 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [base_0000] (PID 118060) rss_mb | MB | 288 | 3.383 | 3.383 | 3.383 | 3.383 | n/a | n/a |
| bash [base_0000] (PID 118060) vms_mb | MB | 288 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [base_0000] (PID 118069) CPU | percent | 287 | 97.995 | 54.001 | 116.044 | 98.202 | 29.320000 CPU seconds | n/a |
| python [base_0000] (PID 118069) rss_mb | MB | 288 | 40.169 | 13.945 | 40.531 | 40.531 | n/a | n/a |
| python [base_0000] (PID 118069) vms_mb | MB | 288 | 49.577 | 18.293 | 50.027 | 50.027 | n/a | n/a |
| docker (PID 118079) rss_mb | MB | 1 | 20.707 | 20.707 | 20.707 | 20.707 | n/a | n/a |
| docker (PID 118079) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 118106) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 118106) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 118106) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 118106) rss_mb | MB | 3 | 25.605 | 25.605 | 25.605 | 25.605 | n/a | n/a |
| docker (PID 118106) vms_mb | MB | 3 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 118147) CPU | percent | 4 | 9.280 | 0.000 | 27.440 | 0.000 | 0.040000 CPU seconds | n/a |
| runc:[2:INIT] [beam_0000] (PID 118147) rss_mb | MB | 5 | 5.181 | 0.633 | 13.059 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 118147) vms_mb | MB | 5 | 628.617 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 118165) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 118165) rss_mb | MB | 3 | 1.809 | 1.809 | 1.809 | 1.809 | n/a | n/a |
| tail [beam_0000] (PID 118165) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 118176) rss_mb | MB | 1 | 27.453 | 27.453 | 27.453 | 27.453 | n/a | n/a |
| docker (PID 118176) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 118202) rss_mb | MB | 1 | 27.199 | 27.199 | 27.199 | 27.199 | n/a | n/a |
| docker (PID 118202) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 118220) rss_mb | MB | 1 | 10.410 | 10.410 | 10.410 | 10.410 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 118220) vms_mb | MB | 1 | 1497.320 | 1497.320 | 1497.320 | 1497.320 | n/a | n/a |
| docker (PID 118236) rss_mb | MB | 1 | 27.379 | 27.379 | 27.379 | 27.379 | n/a | n/a |
| docker (PID 118236) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[0:PARENT] [beam_0000] (PID 118254) rss_mb | MB | 1 | 1.949 | 1.949 | 1.949 | 1.949 | n/a | n/a |
| runc:[0:PARENT] [beam_0000] (PID 118254) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 118256) rss_mb | MB | 1 | 2.062 | 2.062 | 2.062 | 2.062 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 118256) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| docker (PID 118274) rss_mb | MB | 1 | 26.883 | 26.883 | 26.883 | 26.883 | n/a | n/a |
| docker (PID 118274) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 118317) rss_mb | MB | 1 | 16.199 | 16.199 | 16.199 | 16.199 | n/a | n/a |
| docker (PID 118317) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 118336) CPU | percent | 1 | 9.785 | 9.785 | 9.785 | 9.785 | 0.010000 CPU seconds | n/a |
| docker (PID 118336) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 118336) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 118336) rss_mb | MB | 2 | 24.361 | 23.055 | 25.668 | 25.668 | n/a | n/a |
| docker (PID 118336) vms_mb | MB | 2 | 1624.207 | 1588.203 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 118380) CPU | percent | 14 | 1.357 | 0.000 | 9.552 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [beam_0000] (PID 118380) rss_mb | MB | 15 | 1.408 | 0.633 | 12.266 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 118380) vms_mb | MB | 15 | 105.666 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 118392) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 118392) rss_mb | MB | 14 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [beam_0000] (PID 118392) vms_mb | MB | 14 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 118402) rss_mb | MB | 1 | 25.633 | 25.633 | 25.633 | 25.633 | n/a | n/a |
| docker (PID 118402) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 118428) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 118428) io read MB/s | MB/s | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 118428) io write MB/s | MB/s | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 118428) rss_mb | MB | 12 | 27.191 | 27.191 | 27.191 | 27.191 | n/a | n/a |
| docker (PID 118428) vms_mb | MB | 12 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [beam_0000] (PID 118445) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [beam_0000] (PID 118445) rss_mb | MB | 11 | 3.426 | 3.426 | 3.426 | 3.426 | n/a | n/a |
| bash [beam_0000] (PID 118445) vms_mb | MB | 11 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [beam_0000] (PID 118454) CPU | percent | 10 | 99.650 | 90.488 | 112.622 | 95.285 | 1.070000 CPU seconds | n/a |
| python [beam_0000] (PID 118454) rss_mb | MB | 11 | 31.847 | 12.480 | 41.746 | 41.746 | n/a | n/a |
| python [beam_0000] (PID 118454) vms_mb | MB | 11 | 38.780 | 16.277 | 51.238 | 51.238 | n/a | n/a |
| docker (PID 118457) rss_mb | MB | 1 | 3.031 | 3.031 | 3.031 | 3.031 | n/a | n/a |
| docker (PID 118457) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 118465) rss_mb | MB | 1 | 25.859 | 25.859 | 25.859 | 25.859 | n/a | n/a |
| docker (PID 118465) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 118525) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 118525) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 118525) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 118525) rss_mb | MB | 2 | 25.344 | 25.344 | 25.344 | 25.344 | n/a | n/a |
| docker (PID 118525) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [beam_0000] (PID 118562) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beam_0000] (PID 118562) rss_mb | MB | 4 | 0.475 | 0.000 | 0.633 | 0.633 | n/a | n/a |
| docker-init [beam_0000] (PID 118562) vms_mb | MB | 4 | 1.021 | 0.922 | 1.055 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 118574) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 118574) rss_mb | MB | 3 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [beam_0000] (PID 118574) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 118585) rss_mb | MB | 1 | 27.430 | 27.430 | 27.430 | 27.430 | n/a | n/a |
| docker (PID 118585) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 118603) rss_mb | MB | 1 | 11.520 | 11.520 | 11.520 | 11.520 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 118603) vms_mb | MB | 1 | 1498.223 | 1498.223 | 1498.223 | 1498.223 | n/a | n/a |
| docker (PID 118609) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 118609) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 118644) rss_mb | MB | 1 | 27.277 | 27.277 | 27.277 | 27.277 | n/a | n/a |
| docker (PID 118644) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 118664) rss_mb | MB | 1 | 12.004 | 12.004 | 12.004 | 12.004 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 118664) vms_mb | MB | 1 | 1498.223 | 1498.223 | 1498.223 | 1498.223 | n/a | n/a |
| docker (PID 118681) rss_mb | MB | 1 | 26.195 | 26.195 | 26.195 | 26.195 | n/a | n/a |
| docker (PID 118681) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 118723) rss_mb | MB | 1 | 23.316 | 23.316 | 23.316 | 23.316 | n/a | n/a |
| docker (PID 118723) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 118749) rss_mb | MB | 1 | 26.387 | 26.387 | 26.387 | 26.387 | n/a | n/a |
| docker (PID 118749) vms_mb | MB | 1 | 1732.277 | 1732.277 | 1732.277 | 1732.277 | n/a | n/a |
| docker (PID 118766) CPU | percent | 54 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 118766) io read MB/s | MB/s | 54 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 118766) io write MB/s | MB/s | 54 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 118766) rss_mb | MB | 55 | 25.621 | 25.621 | 25.621 | 25.621 | n/a | n/a |
| docker (PID 118766) vms_mb | MB | 55 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 118782) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 118782) vms_mb | MB | 1 | 30.570 | 30.570 | 30.570 | 30.570 | n/a | n/a |
| docker (PID 118798) rss_mb | MB | 1 | 25.633 | 25.633 | 25.633 | 25.633 | n/a | n/a |
| docker (PID 118798) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| python3 (PID 118813) CPU | percent | 5 | 96.570 | 85.466 | 105.750 | 98.175 | 0.500000 CPU seconds | n/a |
| python3 (PID 118813) io read MB/s | MB/s | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 118813) io write MB/s | MB/s | 5 | 0.476 | 0.000 | 2.378 | 2.378 | 0.242188 MB | n/a |
| python3 (PID 118813) rss_mb | MB | 6 | 24.465 | 2.207 | 34.695 | 34.695 | n/a | n/a |
| python3 (PID 118813) vms_mb | MB | 6 | 48.740 | 30.102 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 118818) rss_mb | MB | 1 | 23.855 | 23.855 | 23.855 | 23.855 | n/a | n/a |
| docker (PID 118818) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 118843) rss_mb | MB | 1 | 20.121 | 20.121 | 20.121 | 20.121 | n/a | n/a |
| docker (PID 118843) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 118861) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 118861) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 118861) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 118861) rss_mb | MB | 2 | 17.641 | 9.281 | 26.000 | 26.000 | n/a | n/a |
| docker (PID 118861) vms_mb | MB | 2 | 1551.953 | 1443.695 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 118913) rss_mb | MB | 1 | 13.395 | 13.395 | 13.395 | 13.395 | n/a | n/a |
| docker (PID 118913) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 118921) rss_mb | MB | 1 | 26.930 | 26.930 | 26.930 | 26.930 | n/a | n/a |
| docker (PID 118921) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 118961) CPU | percent | 3 | 9.781 | 0.000 | 29.343 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 118961) rss_mb | MB | 4 | 3.053 | 0.633 | 10.312 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 118961) vms_mb | MB | 4 | 393.090 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 118974) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 118974) rss_mb | MB | 3 | 1.809 | 1.809 | 1.809 | 1.809 | n/a | n/a |
| tail [base_0000] (PID 118974) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 118984) rss_mb | MB | 1 | 17.297 | 17.297 | 17.297 | 17.297 | n/a | n/a |
| docker (PID 118984) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 119012) rss_mb | MB | 1 | 27.188 | 27.188 | 27.188 | 27.188 | n/a | n/a |
| docker (PID 119012) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 119031) rss_mb | MB | 1 | 11.176 | 11.176 | 11.176 | 11.176 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 119031) vms_mb | MB | 1 | 1641.965 | 1641.965 | 1641.965 | 1641.965 | n/a | n/a |
| docker (PID 119048) rss_mb | MB | 1 | 27.258 | 27.258 | 27.258 | 27.258 | n/a | n/a |
| docker (PID 119048) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| sh [base_0000] (PID 119068) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sh [base_0000] (PID 119068) vms_mb | MB | 1 | 0.516 | 0.516 | 0.516 | 0.516 | n/a | n/a |
| docker (PID 119085) rss_mb | MB | 1 | 25.805 | 25.805 | 25.805 | 25.805 | n/a | n/a |
| docker (PID 119085) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 119135) rss_mb | MB | 1 | 26.645 | 26.645 | 26.645 | 26.645 | n/a | n/a |
| docker (PID 119135) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 119150) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 119150) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 119150) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 119150) rss_mb | MB | 2 | 27.312 | 27.312 | 27.312 | 27.312 | n/a | n/a |
| docker (PID 119150) vms_mb | MB | 2 | 1804.781 | 1804.781 | 1804.781 | 1804.781 | n/a | n/a |
| docker-init [bear_0000] (PID 119192) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bear_0000] (PID 119192) rss_mb | MB | 4 | 3.753 | 0.633 | 13.113 | 0.633 | n/a | n/a |
| docker-init [bear_0000] (PID 119192) vms_mb | MB | 4 | 393.473 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 119204) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 119204) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [bear_0000] (PID 119204) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 119234) rss_mb | MB | 1 | 25.848 | 25.848 | 25.848 | 25.848 | n/a | n/a |
| docker (PID 119234) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 119270) rss_mb | MB | 1 | 27.129 | 27.129 | 27.129 | 27.129 | n/a | n/a |
| docker (PID 119270) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[0:PARENT] [bear_0000] (PID 119287) rss_mb | MB | 1 | 1.945 | 1.945 | 1.945 | 1.945 | n/a | n/a |
| runc:[0:PARENT] [bear_0000] (PID 119287) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[0:PARENT] [bear_0000] (PID 119290) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[0:PARENT] [bear_0000] (PID 119290) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| docker (PID 119307) rss_mb | MB | 1 | 27.281 | 27.281 | 27.281 | 27.281 | n/a | n/a |
| docker (PID 119307) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 119327) rss_mb | MB | 1 | 11.508 | 11.508 | 11.508 | 11.508 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 119327) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 119344) rss_mb | MB | 1 | 26.547 | 26.547 | 26.547 | 26.547 | n/a | n/a |
| docker (PID 119344) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 119394) rss_mb | MB | 1 | 1.082 | 1.082 | 1.082 | 1.082 | n/a | n/a |
| docker (PID 119394) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 119402) rss_mb | MB | 1 | 25.691 | 25.691 | 25.691 | 25.691 | n/a | n/a |
| docker (PID 119402) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 119443) CPU | percent | 3 | 3.260 | 0.000 | 9.779 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 119443) rss_mb | MB | 4 | 3.488 | 0.633 | 12.055 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 119443) vms_mb | MB | 4 | 411.439 | 1.055 | 1642.594 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 119457) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 119457) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [bear_0000] (PID 119457) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 119469) rss_mb | MB | 1 | 26.531 | 26.531 | 26.531 | 26.531 | n/a | n/a |
| docker (PID 119469) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 119496) rss_mb | MB | 1 | 27.281 | 27.281 | 27.281 | 27.281 | n/a | n/a |
| docker (PID 119496) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 119516) rss_mb | MB | 1 | 11.875 | 11.875 | 11.875 | 11.875 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 119516) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 119567) rss_mb | MB | 1 | 26.926 | 26.926 | 26.926 | 26.926 | n/a | n/a |
| docker (PID 119567) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 119628) rss_mb | MB | 1 | 25.637 | 25.637 | 25.637 | 25.637 | n/a | n/a |
| docker (PID 119628) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bear_0000] (PID 119667) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bear_0000] (PID 119667) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bear_0000] (PID 119667) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 119680) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 119680) rss_mb | MB | 3 | 1.684 | 1.684 | 1.684 | 1.684 | n/a | n/a |
| tail [bear_0000] (PID 119680) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 119682) rss_mb | MB | 1 | 8.719 | 8.719 | 8.719 | 8.719 | n/a | n/a |
| docker (PID 119682) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 119718) rss_mb | MB | 1 | 27.004 | 27.004 | 27.004 | 27.004 | n/a | n/a |
| docker (PID 119718) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 119761) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 119761) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 119761) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 119761) rss_mb | MB | 2 | 26.984 | 26.984 | 26.984 | 26.984 | n/a | n/a |
| docker (PID 119761) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 119820) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 119820) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 119820) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 119820) rss_mb | MB | 2 | 25.699 | 25.699 | 25.699 | 25.699 | n/a | n/a |
| docker (PID 119820) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 119859) CPU | percent | 2 | 4.881 | 0.000 | 9.761 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 119859) rss_mb | MB | 3 | 4.587 | 0.633 | 12.496 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 119859) vms_mb | MB | 3 | 500.111 | 1.055 | 1498.223 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 119871) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 119871) rss_mb | MB | 2 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bear_0000] (PID 119871) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 119882) rss_mb | MB | 1 | 27.430 | 27.430 | 27.430 | 27.430 | n/a | n/a |
| docker (PID 119882) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 119902) rss_mb | MB | 1 | 11.938 | 11.938 | 11.938 | 11.938 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 119902) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 119943) rss_mb | MB | 1 | 26.176 | 26.176 | 26.176 | 26.176 | n/a | n/a |
| docker (PID 119943) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 119951) rss_mb | MB | 1 | 27.070 | 27.070 | 27.070 | 27.070 | n/a | n/a |
| docker (PID 119951) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 120010) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 120010) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 120010) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 120010) rss_mb | MB | 2 | 26.938 | 26.938 | 26.938 | 26.938 | n/a | n/a |
| docker (PID 120010) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 120050) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 120050) rss_mb | MB | 4 | 3.712 | 0.633 | 12.949 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 120050) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 120062) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 120062) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [bear_0000] (PID 120062) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 120072) rss_mb | MB | 1 | 27.371 | 27.371 | 27.371 | 27.371 | n/a | n/a |
| docker (PID 120072) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 120094) rss_mb | MB | 1 | 11.641 | 11.641 | 11.641 | 11.641 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 120094) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 120130) rss_mb | MB | 1 | 25.094 | 25.094 | 25.094 | 25.094 | n/a | n/a |
| docker (PID 120130) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 120175) CPU | percent | 1 | 9.783 | 9.783 | 9.783 | 9.783 | 0.010000 CPU seconds | n/a |
| docker (PID 120175) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 120175) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 120175) rss_mb | MB | 2 | 18.117 | 9.242 | 26.992 | 26.992 | n/a | n/a |
| docker (PID 120175) vms_mb | MB | 2 | 1452.232 | 1243.691 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 120236) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 120236) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 120236) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 120236) rss_mb | MB | 2 | 26.637 | 26.637 | 26.637 | 26.637 | n/a | n/a |
| docker (PID 120236) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 120276) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 120276) rss_mb | MB | 4 | 3.672 | 0.633 | 12.789 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 120276) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 120289) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 120289) rss_mb | MB | 3 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [base_0000] (PID 120289) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 120300) rss_mb | MB | 1 | 27.281 | 27.281 | 27.281 | 27.281 | n/a | n/a |
| docker (PID 120300) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 120365) rss_mb | MB | 1 | 16.207 | 16.207 | 16.207 | 16.207 | n/a | n/a |
| docker (PID 120365) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 120403) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 120403) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 120403) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 120403) rss_mb | MB | 2 | 27.129 | 27.129 | 27.129 | 27.129 | n/a | n/a |
| docker (PID 120403) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 120463) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 120463) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 120463) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 120463) rss_mb | MB | 2 | 25.465 | 25.465 | 25.465 | 25.465 | n/a | n/a |
| docker (PID 120463) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 120502) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 120502) rss_mb | MB | 7 | 2.392 | 0.633 | 12.949 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 120502) vms_mb | MB | 7 | 225.294 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 120516) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 120516) rss_mb | MB | 6 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [base_0000] (PID 120516) vms_mb | MB | 6 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 120527) rss_mb | MB | 1 | 27.164 | 27.164 | 27.164 | 27.164 | n/a | n/a |
| docker (PID 120527) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 120546) rss_mb | MB | 1 | 11.473 | 11.473 | 11.473 | 11.473 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 120546) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 120553) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 120553) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 120553) io write MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 120553) rss_mb | MB | 4 | 27.547 | 27.547 | 27.547 | 27.547 | n/a | n/a |
| docker (PID 120553) vms_mb | MB | 4 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [base_0000] (PID 120572) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [base_0000] (PID 120572) rss_mb | MB | 4 | 3.426 | 3.426 | 3.426 | 3.426 | n/a | n/a |
| bash [base_0000] (PID 120572) vms_mb | MB | 4 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [base_0000] (PID 120581) CPU | percent | 3 | 100.899 | 97.983 | 106.710 | 97.983 | 0.310000 CPU seconds | n/a |
| python [base_0000] (PID 120581) rss_mb | MB | 4 | 22.961 | 9.828 | 34.645 | 34.645 | n/a | n/a |
| python [base_0000] (PID 120581) vms_mb | MB | 4 | 28.985 | 13.602 | 45.023 | 45.023 | n/a | n/a |
| docker (PID 120583) rss_mb | MB | 1 | 18.652 | 18.652 | 18.652 | 18.652 | n/a | n/a |
| docker (PID 120583) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 120592) rss_mb | MB | 1 | 25.699 | 25.699 | 25.699 | 25.699 | n/a | n/a |
| docker (PID 120592) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 120652) rss_mb | MB | 1 | 26.414 | 26.414 | 26.414 | 26.414 | n/a | n/a |
| docker (PID 120652) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 120693) CPU | percent | 3 | 9.466 | 0.000 | 28.397 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 120693) rss_mb | MB | 4 | 3.067 | 0.633 | 10.371 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 120693) vms_mb | MB | 4 | 375.214 | 1.055 | 1497.691 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 120705) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 120705) rss_mb | MB | 3 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [base_0000] (PID 120705) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 120715) rss_mb | MB | 1 | 16.574 | 16.574 | 16.574 | 16.574 | n/a | n/a |
| docker (PID 120715) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 120742) rss_mb | MB | 1 | 27.328 | 27.328 | 27.328 | 27.328 | n/a | n/a |
| docker (PID 120742) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 120762) rss_mb | MB | 1 | 10.879 | 10.879 | 10.879 | 10.879 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 120762) vms_mb | MB | 1 | 1641.707 | 1641.707 | 1641.707 | 1641.707 | n/a | n/a |
| docker (PID 120778) rss_mb | MB | 1 | 27.430 | 27.430 | 27.430 | 27.430 | n/a | n/a |
| docker (PID 120778) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 120798) rss_mb | MB | 1 | 11.891 | 11.891 | 11.891 | 11.891 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 120798) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 120814) rss_mb | MB | 1 | 26.023 | 26.023 | 26.023 | 26.023 | n/a | n/a |
| docker (PID 120814) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 120890) rss_mb | MB | 1 | 25.348 | 25.348 | 25.348 | 25.348 | n/a | n/a |
| docker (PID 120890) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 120898) CPU | percent | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 120898) io read MB/s | MB/s | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 120898) io write MB/s | MB/s | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 120898) rss_mb | MB | 52 | 26.805 | 26.805 | 26.805 | 26.805 | n/a | n/a |
| docker (PID 120898) vms_mb | MB | 52 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 120922) rss_mb | MB | 1 | 1.656 | 1.656 | 1.656 | 1.656 | n/a | n/a |
| docker (PID 120922) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 120936) CPU | percent | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 120936) io read MB/s | MB/s | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 120936) io write MB/s | MB/s | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 120936) rss_mb | MB | 53 | 27.121 | 27.121 | 27.121 | 27.121 | n/a | n/a |
| docker (PID 120936) vms_mb | MB | 53 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 120953) rss_mb | MB | 1 | 13.793 | 13.793 | 13.793 | 13.793 | n/a | n/a |
| docker (PID 120953) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 120969) rss_mb | MB | 1 | 25.918 | 25.918 | 25.918 | 25.918 | n/a | n/a |
| docker (PID 120969) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| python3 (PID 120985) CPU | percent | 4 | 98.779 | 96.640 | 101.765 | 98.031 | 0.410000 CPU seconds | n/a |
| python3 (PID 120985) io read MB/s | MB/s | 4 | 0.029 | 0.000 | 0.115 | 0.115 | 0.011719 MB | n/a |
| python3 (PID 120985) io write MB/s | MB/s | 4 | 0.555 | 0.000 | 2.221 | 2.221 | 0.226562 MB | n/a |
| python3 (PID 120985) rss_mb | MB | 5 | 26.860 | 14.191 | 34.555 | 34.555 | n/a | n/a |
| python3 (PID 120985) vms_mb | MB | 5 | 50.518 | 39.570 | 57.441 | 57.441 | n/a | n/a |
| docker (PID 120995) rss_mb | MB | 1 | 26.832 | 26.832 | 26.832 | 26.832 | n/a | n/a |
| docker (PID 120995) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 121026) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 121026) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 121026) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 121026) rss_mb | MB | 2 | 27.129 | 27.129 | 27.129 | 27.129 | n/a | n/a |
| docker (PID 121026) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [bear_0000] (PID 121066) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bear_0000] (PID 121066) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bear_0000] (PID 121066) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 121079) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 121079) rss_mb | MB | 4 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [bear_0000] (PID 121079) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 121115) rss_mb | MB | 1 | 3.844 | 3.844 | 3.844 | 3.844 | n/a | n/a |
| docker (PID 121115) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 121151) rss_mb | MB | 1 | 26.879 | 26.879 | 26.879 | 26.879 | n/a | n/a |
| docker (PID 121151) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 121189) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 121189) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 121189) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 121189) rss_mb | MB | 2 | 26.930 | 26.930 | 26.930 | 26.930 | n/a | n/a |
| docker (PID 121189) vms_mb | MB | 2 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 121240) rss_mb | MB | 1 | 23.277 | 23.277 | 23.277 | 23.277 | n/a | n/a |
| docker (PID 121240) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 121248) rss_mb | MB | 1 | 25.914 | 25.914 | 25.914 | 25.914 | n/a | n/a |
| docker (PID 121248) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 121287) CPU | percent | 15 | 1.303 | 0.000 | 19.551 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 121287) rss_mb | MB | 16 | 1.351 | 0.633 | 12.121 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 121287) vms_mb | MB | 16 | 103.628 | 1.055 | 1642.230 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 121303) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 121303) rss_mb | MB | 15 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bear_0000] (PID 121303) vms_mb | MB | 15 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 121328) CPU | percent | 2 | 9.240 | 0.000 | 18.480 | 0.000 | 0.020000 CPU seconds | n/a |
| docker (PID 121328) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 121328) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 121328) rss_mb | MB | 3 | 24.876 | 18.918 | 27.855 | 27.855 | n/a | n/a |
| docker (PID 121328) vms_mb | MB | 3 | 1756.507 | 1515.949 | 1876.785 | 1876.785 | n/a | n/a |
| docker (PID 121330) rss_mb | MB | 1 | 20.297 | 20.297 | 20.297 | 20.297 | n/a | n/a |
| docker (PID 121330) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 121363) CPU | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 121363) io read MB/s | MB/s | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 121363) io write MB/s | MB/s | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 121363) rss_mb | MB | 13 | 27.160 | 26.312 | 27.230 | 27.230 | n/a | n/a |
| docker (PID 121363) vms_mb | MB | 13 | 1660.735 | 1660.273 | 1660.773 | 1660.773 | n/a | n/a |
| bash [bear_0000] (PID 121386) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bear_0000] (PID 121386) rss_mb | MB | 12 | 3.281 | 3.281 | 3.281 | 3.281 | n/a | n/a |
| bash [bear_0000] (PID 121386) vms_mb | MB | 12 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| docker-init [beef_0000] (PID 121426) CPU | percent | 5 | 3.506 | 0.000 | 17.528 | 0.000 | 0.020000 CPU seconds | n/a |
| docker-init [beef_0000] (PID 121426) rss_mb | MB | 6 | 2.538 | 0.633 | 12.062 | 0.633 | n/a | n/a |
| docker-init [beef_0000] (PID 121426) vms_mb | MB | 6 | 250.583 | 1.055 | 1498.223 | 1.055 | n/a | n/a |
| python [bear_0000] (PID 121429) CPU | percent | 11 | 91.921 | 76.437 | 120.747 | 92.564 | 1.170000 CPU seconds | n/a |
| python [bear_0000] (PID 121429) rss_mb | MB | 12 | 31.628 | 10.359 | 41.738 | 41.738 | n/a | n/a |
| python [bear_0000] (PID 121429) vms_mb | MB | 12 | 38.969 | 14.660 | 51.340 | 51.340 | n/a | n/a |
| tail [beef_0000] (PID 121441) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 121441) rss_mb | MB | 5 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [beef_0000] (PID 121441) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 121443) rss_mb | MB | 1 | 27.312 | 27.312 | 27.312 | 27.312 | n/a | n/a |
| docker (PID 121443) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[0:PARENT] (PID 121462) rss_mb | MB | 1 | 1.996 | 1.996 | 1.996 | 1.996 | n/a | n/a |
| runc:[0:PARENT] (PID 121462) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| docker (PID 121480) rss_mb | MB | 1 | 27.016 | 27.016 | 27.016 | 27.016 | n/a | n/a |
| docker (PID 121480) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 121505) rss_mb | MB | 1 | 27.398 | 27.398 | 27.398 | 27.398 | n/a | n/a |
| docker (PID 121505) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 121524) rss_mb | MB | 1 | 11.148 | 11.148 | 11.148 | 11.148 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 121524) vms_mb | MB | 1 | 1569.703 | 1569.703 | 1569.703 | 1569.703 | n/a | n/a |
| docker (PID 121540) rss_mb | MB | 1 | 27.391 | 27.391 | 27.391 | 27.391 | n/a | n/a |
| docker (PID 121540) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 121560) rss_mb | MB | 1 | 12.043 | 12.043 | 12.043 | 12.043 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 121560) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 121576) rss_mb | MB | 1 | 25.973 | 25.973 | 25.973 | 25.973 | n/a | n/a |
| docker (PID 121576) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 121618) rss_mb | MB | 1 | 26.637 | 26.637 | 26.637 | 26.637 | n/a | n/a |
| docker (PID 121618) vms_mb | MB | 1 | 1732.277 | 1732.277 | 1732.277 | 1732.277 | n/a | n/a |
| docker (PID 121635) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 121635) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 121635) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 121635) rss_mb | MB | 2 | 25.883 | 25.883 | 25.883 | 25.883 | n/a | n/a |
| docker (PID 121635) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [beef_0000] (PID 121674) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beef_0000] (PID 121674) rss_mb | MB | 4 | 0.475 | 0.000 | 0.633 | 0.633 | n/a | n/a |
| docker-init [beef_0000] (PID 121674) vms_mb | MB | 4 | 1.021 | 0.922 | 1.055 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 121687) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 121687) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [beef_0000] (PID 121687) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 121697) rss_mb | MB | 1 | 27.430 | 27.430 | 27.430 | 27.430 | n/a | n/a |
| docker (PID 121697) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 121717) rss_mb | MB | 1 | 11.434 | 11.434 | 11.434 | 11.434 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 121717) vms_mb | MB | 1 | 1498.223 | 1498.223 | 1498.223 | 1498.223 | n/a | n/a |
| docker (PID 121723) rss_mb | MB | 1 | 27.617 | 27.617 | 27.617 | 27.617 | n/a | n/a |
| docker (PID 121723) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 121759) rss_mb | MB | 1 | 27.297 | 27.297 | 27.297 | 27.297 | n/a | n/a |
| docker (PID 121759) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 121779) rss_mb | MB | 1 | 11.977 | 11.977 | 11.977 | 11.977 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 121779) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 121795) rss_mb | MB | 1 | 26.219 | 26.219 | 26.219 | 26.219 | n/a | n/a |
| docker (PID 121795) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 121810) rss_mb | MB | 1 | 1.070 | 1.070 | 1.070 | 1.070 | n/a | n/a |
| docker (PID 121810) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 121835) rss_mb | MB | 1 | 26.977 | 26.977 | 26.977 | 26.977 | n/a | n/a |
| docker (PID 121835) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 121864) rss_mb | MB | 1 | 6.344 | 6.344 | 6.344 | 6.344 | n/a | n/a |
| docker (PID 121864) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 121915) rss_mb | MB | 1 | 11.211 | 11.211 | 11.211 | 11.211 | n/a | n/a |
| docker (PID 121915) vms_mb | MB | 1 | 1451.949 | 1451.949 | 1451.949 | 1451.949 | n/a | n/a |
| docker (PID 121940) rss_mb | MB | 1 | 25.449 | 25.449 | 25.449 | 25.449 | n/a | n/a |
| docker (PID 121940) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 121948) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 121948) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 121948) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 121948) rss_mb | MB | 39 | 25.984 | 25.984 | 25.984 | 25.984 | n/a | n/a |
| docker (PID 121948) vms_mb | MB | 39 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 121964) rss_mb | MB | 1 | 8.805 | 8.805 | 8.805 | 8.805 | n/a | n/a |
| docker (PID 121964) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| python3 (PID 121995) CPU | percent | 2 | 98.651 | 98.402 | 98.900 | 98.900 | 0.200000 CPU seconds | n/a |
| python3 (PID 121995) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 121995) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 121995) rss_mb | MB | 3 | 27.766 | 21.059 | 33.699 | 33.699 | n/a | n/a |
| python3 (PID 121995) vms_mb | MB | 3 | 51.358 | 45.445 | 56.461 | 56.461 | n/a | n/a |
| docker (PID 122022) rss_mb | MB | 1 | 26.879 | 26.879 | 26.879 | 26.879 | n/a | n/a |
| docker (PID 122022) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 122063) CPU | percent | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 122063) io read MB/s | MB/s | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 122063) io write MB/s | MB/s | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 122063) rss_mb | MB | 44 | 26.449 | 26.449 | 26.449 | 26.449 | n/a | n/a |
| docker (PID 122063) vms_mb | MB | 44 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 122085) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 122085) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 122085) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 122085) rss_mb | MB | 3 | 26.980 | 25.637 | 27.652 | 27.652 | n/a | n/a |
| docker (PID 122085) vms_mb | MB | 3 | 1660.586 | 1660.211 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [bell_0000] (PID 122125) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bell_0000] (PID 122125) rss_mb | MB | 6 | 2.594 | 0.633 | 12.398 | 0.633 | n/a | n/a |
| docker-init [bell_0000] (PID 122125) vms_mb | MB | 6 | 262.625 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 122138) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 122138) rss_mb | MB | 5 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [bell_0000] (PID 122138) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 122140) rss_mb | MB | 1 | 27.371 | 27.371 | 27.371 | 27.371 | n/a | n/a |
| docker (PID 122140) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 122175) rss_mb | MB | 1 | 15.465 | 15.465 | 15.465 | 15.465 | n/a | n/a |
| docker (PID 122175) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 122200) rss_mb | MB | 1 | 27.270 | 27.270 | 27.270 | 27.270 | n/a | n/a |
| docker (PID 122200) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 122218) rss_mb | MB | 1 | 10.438 | 10.438 | 10.438 | 10.438 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 122218) vms_mb | MB | 1 | 1569.445 | 1569.445 | 1569.445 | 1569.445 | n/a | n/a |
| docker (PID 122235) rss_mb | MB | 1 | 25.883 | 25.883 | 25.883 | 25.883 | n/a | n/a |
| docker (PID 122235) vms_mb | MB | 1 | 1659.961 | 1659.961 | 1659.961 | 1659.961 | n/a | n/a |
| docker (PID 122266) rss_mb | MB | 1 | 26.320 | 26.320 | 26.320 | 26.320 | n/a | n/a |
| docker (PID 122266) vms_mb | MB | 1 | 1732.277 | 1732.277 | 1732.277 | 1732.277 | n/a | n/a |
| docker (PID 122275) rss_mb | MB | 1 | 26.000 | 26.000 | 26.000 | 26.000 | n/a | n/a |
| docker (PID 122275) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 122315) rss_mb | MB | 1 | 22.898 | 22.898 | 22.898 | 22.898 | n/a | n/a |
| docker (PID 122315) vms_mb | MB | 1 | 1523.953 | 1523.953 | 1523.953 | 1523.953 | n/a | n/a |
| docker (PID 122331) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 122331) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 122331) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 122331) rss_mb | MB | 2 | 25.344 | 25.344 | 25.344 | 25.344 | n/a | n/a |
| docker (PID 122331) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 122372) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bell_0000] (PID 122372) rss_mb | MB | 5 | 3.096 | 0.633 | 12.949 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 122372) vms_mb | MB | 5 | 314.989 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 122384) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 122384) rss_mb | MB | 4 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bell_0000] (PID 122384) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 122395) rss_mb | MB | 1 | 26.234 | 26.234 | 26.234 | 26.234 | n/a | n/a |
| docker (PID 122395) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 122423) rss_mb | MB | 1 | 27.605 | 27.605 | 27.605 | 27.605 | n/a | n/a |
| docker (PID 122423) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 122447) rss_mb | MB | 1 | 27.184 | 27.184 | 27.184 | 27.184 | n/a | n/a |
| docker (PID 122447) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 122494) rss_mb | MB | 1 | 26.016 | 26.016 | 26.016 | 26.016 | n/a | n/a |
| docker (PID 122494) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 122536) rss_mb | MB | 1 | 11.133 | 11.133 | 11.133 | 11.133 | n/a | n/a |
| docker (PID 122536) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 122555) rss_mb | MB | 1 | 25.633 | 25.633 | 25.633 | 25.633 | n/a | n/a |
| docker (PID 122555) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 122583) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 122583) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 122583) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 122583) rss_mb | MB | 2 | 26.773 | 26.773 | 26.773 | 26.773 | n/a | n/a |
| docker (PID 122583) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 122623) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [beef_0000] (PID 122623) rss_mb | MB | 4 | 3.747 | 0.633 | 13.090 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 122623) vms_mb | MB | 4 | 411.411 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 122636) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 122636) rss_mb | MB | 3 | 1.146 | 0.000 | 1.719 | 0.000 | n/a | n/a |
| tail [beef_0000] (PID 122636) vms_mb | MB | 3 | 1.990 | 0.000 | 2.984 | 0.000 | n/a | n/a |
| docker (PID 122646) rss_mb | MB | 1 | 27.473 | 27.473 | 27.473 | 27.473 | n/a | n/a |
| docker (PID 122646) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 122711) rss_mb | MB | 1 | 26.223 | 26.223 | 26.223 | 26.223 | n/a | n/a |
| docker (PID 122711) vms_mb | MB | 1 | 1732.277 | 1732.277 | 1732.277 | 1732.277 | n/a | n/a |
| docker (PID 122751) rss_mb | MB | 1 | 26.176 | 26.176 | 26.176 | 26.176 | n/a | n/a |
| docker (PID 122751) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 122793) rss_mb | MB | 1 | 5.938 | 5.938 | 5.938 | 5.938 | n/a | n/a |
| docker (PID 122793) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 122810) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 122810) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 122810) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 122810) rss_mb | MB | 2 | 27.016 | 27.016 | 27.016 | 27.016 | n/a | n/a |
| docker (PID 122810) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 122847) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [beef_0000] (PID 122847) rss_mb | MB | 11 | 1.763 | 0.633 | 13.070 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 122847) vms_mb | MB | 11 | 143.752 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 122860) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 122860) rss_mb | MB | 10 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [beef_0000] (PID 122860) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 122871) rss_mb | MB | 1 | 27.258 | 27.258 | 27.258 | 27.258 | n/a | n/a |
| docker (PID 122871) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 122891) rss_mb | MB | 1 | 11.867 | 11.867 | 11.867 | 11.867 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 122891) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 122899) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 122899) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 122899) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 122899) rss_mb | MB | 8 | 27.289 | 27.289 | 27.289 | 27.289 | n/a | n/a |
| docker (PID 122899) vms_mb | MB | 8 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [beef_0000] (PID 122919) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [beef_0000] (PID 122919) rss_mb | MB | 8 | 3.328 | 3.328 | 3.328 | 3.328 | n/a | n/a |
| bash [beef_0000] (PID 122919) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [beef_0000] (PID 122928) CPU | percent | 7 | 100.480 | 88.232 | 107.864 | 107.805 | 0.720000 CPU seconds | n/a |
| python [beef_0000] (PID 122928) rss_mb | MB | 8 | 30.627 | 10.043 | 42.551 | 42.551 | n/a | n/a |
| python [beef_0000] (PID 122928) vms_mb | MB | 8 | 37.905 | 14.531 | 52.238 | 52.238 | n/a | n/a |
| docker (PID 122930) rss_mb | MB | 1 | 19.266 | 19.266 | 19.266 | 19.266 | n/a | n/a |
| docker (PID 122930) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 122938) rss_mb | MB | 1 | 26.926 | 26.926 | 26.926 | 26.926 | n/a | n/a |
| docker (PID 122938) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 122991) rss_mb | MB | 1 | 24.277 | 24.277 | 24.277 | 24.277 | n/a | n/a |
| docker (PID 122991) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 122999) rss_mb | MB | 1 | 25.656 | 25.656 | 25.656 | 25.656 | n/a | n/a |
| docker (PID 122999) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 123039) CPU | percent | 3 | 3.258 | 0.000 | 9.775 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [beef_0000] (PID 123039) rss_mb | MB | 4 | 3.573 | 0.633 | 12.395 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 123039) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 123051) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 123051) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [beef_0000] (PID 123051) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 123061) rss_mb | MB | 1 | 26.922 | 26.922 | 26.922 | 26.922 | n/a | n/a |
| docker (PID 123061) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 123090) rss_mb | MB | 1 | 27.309 | 27.309 | 27.309 | 27.309 | n/a | n/a |
| docker (PID 123090) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 123154) rss_mb | MB | 1 | 21.773 | 21.773 | 21.773 | 21.773 | n/a | n/a |
| docker (PID 123154) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 123162) rss_mb | MB | 1 | 25.707 | 25.707 | 25.707 | 25.707 | n/a | n/a |
| docker (PID 123162) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 123223) rss_mb | MB | 1 | 8.668 | 8.668 | 8.668 | 8.668 | n/a | n/a |
| docker (PID 123223) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 123248) CPU | percent | 42 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 123248) io read MB/s | MB/s | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 123248) io write MB/s | MB/s | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 123248) rss_mb | MB | 43 | 24.865 | 0.000 | 25.457 | 0.000 | n/a | n/a |
| docker (PID 123248) vms_mb | MB | 43 | 1621.601 | 0.000 | 1660.211 | 0.000 | n/a | n/a |
| docker (PID 123265) CPU | percent | 1 | 19.295 | 19.295 | 19.295 | 19.295 | 0.020000 CPU seconds | n/a |
| docker (PID 123265) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 123265) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 123265) rss_mb | MB | 2 | 23.719 | 20.180 | 27.258 | 27.258 | n/a | n/a |
| docker (PID 123265) vms_mb | MB | 2 | 1588.486 | 1516.199 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 123306) CPU | percent | 5 | 7.696 | 0.000 | 38.480 | 0.000 | 0.040000 CPU seconds | n/a |
| runc:[2:INIT] [bell_0000] (PID 123306) rss_mb | MB | 6 | 1.136 | 0.633 | 3.652 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 123306) vms_mb | MB | 6 | 202.325 | 1.055 | 1208.676 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 123317) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 123317) rss_mb | MB | 5 | 1.664 | 1.664 | 1.664 | 1.664 | n/a | n/a |
| tail [bell_0000] (PID 123317) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 123327) rss_mb | MB | 1 | 27.383 | 27.383 | 27.383 | 27.383 | n/a | n/a |
| docker (PID 123327) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 123346) rss_mb | MB | 1 | 11.938 | 11.938 | 11.938 | 11.938 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 123346) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 123353) rss_mb | MB | 1 | 27.109 | 27.109 | 27.109 | 27.109 | n/a | n/a |
| docker (PID 123353) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 123373) rss_mb | MB | 1 | 11.965 | 11.965 | 11.965 | 11.965 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 123373) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 123390) rss_mb | MB | 1 | 27.504 | 27.504 | 27.504 | 27.504 | n/a | n/a |
| docker (PID 123390) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 123410) rss_mb | MB | 1 | 4.348 | 4.348 | 4.348 | 4.348 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 123410) vms_mb | MB | 1 | 1497.191 | 1497.191 | 1497.191 | 1497.191 | n/a | n/a |
| docker (PID 123427) CPU | percent | 1 | 9.205 | 9.205 | 9.205 | 9.205 | 0.010000 CPU seconds | n/a |
| docker (PID 123427) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 123427) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 123427) rss_mb | MB | 2 | 22.252 | 18.527 | 25.977 | 25.977 | n/a | n/a |
| docker (PID 123427) vms_mb | MB | 2 | 1624.082 | 1587.953 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 123505) rss_mb | MB | 1 | 25.922 | 25.922 | 25.922 | 25.922 | n/a | n/a |
| docker (PID 123505) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| python3 (PID 123521) CPU | percent | 3 | 98.791 | 98.538 | 98.978 | 98.978 | 0.300000 CPU seconds | n/a |
| python3 (PID 123521) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 123521) io write MB/s | MB/s | 3 | 0.799 | 0.000 | 2.397 | 2.397 | 0.242188 MB | n/a |
| python3 (PID 123521) rss_mb | MB | 4 | 27.507 | 16.484 | 34.781 | 34.781 | n/a | n/a |
| python3 (PID 123521) vms_mb | MB | 4 | 51.417 | 41.172 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 123531) rss_mb | MB | 1 | 26.512 | 26.512 | 26.512 | 26.512 | n/a | n/a |
| docker (PID 123531) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 123555) rss_mb | MB | 1 | 8.801 | 8.801 | 8.801 | 8.801 | n/a | n/a |
| docker (PID 123555) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 123585) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 123585) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 123585) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 123585) rss_mb | MB | 38 | 26.648 | 26.648 | 26.648 | 26.648 | n/a | n/a |
| docker (PID 123585) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 123609) rss_mb | MB | 1 | 20.355 | 20.355 | 20.355 | 20.355 | n/a | n/a |
| docker (PID 123609) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 123628) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 123628) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 123628) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 123628) rss_mb | MB | 2 | 27.184 | 27.184 | 27.184 | 27.184 | n/a | n/a |
| docker (PID 123628) vms_mb | MB | 2 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 123668) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bell_0000] (PID 123668) rss_mb | MB | 4 | 3.697 | 0.633 | 12.891 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 123668) vms_mb | MB | 4 | 411.349 | 1.055 | 1642.230 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 123682) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 123682) rss_mb | MB | 3 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [bell_0000] (PID 123682) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 123692) rss_mb | MB | 1 | 27.379 | 27.379 | 27.379 | 27.379 | n/a | n/a |
| docker (PID 123692) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 123759) rss_mb | MB | 1 | 25.832 | 25.832 | 25.832 | 25.832 | n/a | n/a |
| docker (PID 123759) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 123797) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 123797) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 123797) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 123797) rss_mb | MB | 2 | 25.973 | 25.973 | 25.973 | 25.973 | n/a | n/a |
| docker (PID 123797) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 123849) rss_mb | MB | 1 | 25.098 | 25.098 | 25.098 | 25.098 | n/a | n/a |
| docker (PID 123849) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 123857) rss_mb | MB | 1 | 25.895 | 25.895 | 25.895 | 25.895 | n/a | n/a |
| docker (PID 123857) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 123895) CPU | percent | 10 | 0.978 | 0.000 | 9.783 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bell_0000] (PID 123895) rss_mb | MB | 11 | 1.690 | 0.633 | 12.262 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 123895) vms_mb | MB | 11 | 143.707 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 123908) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 123908) rss_mb | MB | 10 | 1.785 | 1.785 | 1.785 | 1.785 | n/a | n/a |
| tail [bell_0000] (PID 123908) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 123918) rss_mb | MB | 1 | 27.289 | 27.289 | 27.289 | 27.289 | n/a | n/a |
| docker (PID 123918) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 123938) rss_mb | MB | 1 | 10.535 | 10.535 | 10.535 | 10.535 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 123938) vms_mb | MB | 1 | 1641.449 | 1641.449 | 1641.449 | 1641.449 | n/a | n/a |
| docker (PID 123948) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 123948) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 123948) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 123948) rss_mb | MB | 8 | 27.258 | 27.258 | 27.258 | 27.258 | n/a | n/a |
| docker (PID 123948) vms_mb | MB | 8 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| bash [bell_0000] (PID 123968) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bell_0000] (PID 123968) rss_mb | MB | 8 | 3.426 | 3.426 | 3.426 | 3.426 | n/a | n/a |
| bash [bell_0000] (PID 123968) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bell_0000] (PID 123978) CPU | percent | 7 | 100.683 | 96.929 | 107.875 | 98.095 | 0.720000 CPU seconds | n/a |
| python [bell_0000] (PID 123978) rss_mb | MB | 8 | 30.129 | 7.980 | 42.367 | 42.367 | n/a | n/a |
| python [bell_0000] (PID 123978) vms_mb | MB | 8 | 37.572 | 13.070 | 52.238 | 52.238 | n/a | n/a |
| docker (PID 123988) rss_mb | MB | 1 | 25.918 | 25.918 | 25.918 | 25.918 | n/a | n/a |
| docker (PID 123988) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 124073) rss_mb | MB | 1 | 4.570 | 4.570 | 4.570 | 4.570 | n/a | n/a |
| docker (PID 124073) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 124081) CPU | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 124081) io read MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 124081) io write MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 124081) rss_mb | MB | 40 | 25.738 | 25.738 | 25.738 | 25.738 | n/a | n/a |
| docker (PID 124081) vms_mb | MB | 40 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 124114) rss_mb | MB | 1 | 26.691 | 26.691 | 26.691 | 26.691 | n/a | n/a |
| docker (PID 124114) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 124129) CPU | percent | 3 | 102.015 | 98.371 | 108.775 | 108.775 | 0.310000 CPU seconds | n/a |
| python3 (PID 124129) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 124129) io write MB/s | MB/s | 3 | 0.798 | 0.000 | 2.395 | 2.395 | 0.242188 MB | n/a |
| python3 (PID 124129) rss_mb | MB | 4 | 26.477 | 14.598 | 34.547 | 34.547 | n/a | n/a |
| python3 (PID 124129) vms_mb | MB | 4 | 50.429 | 39.770 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 124132) rss_mb | MB | 1 | 27.016 | 27.016 | 27.016 | 27.016 | n/a | n/a |
| docker (PID 124132) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 124189) rss_mb | MB | 1 | 27.176 | 27.176 | 27.176 | 27.176 | n/a | n/a |
| docker (PID 124189) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| sandbox alex_0000 CPU | percent | 29 | 56.799 | 3.265 | 103.178 | 30.484 | 1.741368 CPU seconds | n/a |
| sandbox alex_0000 io read MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox alex_0000 io write MB/s | MB/s | 32 | 0.497 | 0.000 | 15.895 | 0.000 | 1.703125 MB | n/a |
| sandbox alex_0000 memory | MB | 34 | 10.031 | 0.582 | 36.133 | 4.289 | n/a | n/a |
| sandbox alex_0000 net rx MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox alex_0000 net tx MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox andy_0000 CPU | percent | 29 | 58.916 | 9.920 | 118.797 | 34.599 | 1.825827 CPU seconds | n/a |
| sandbox andy_0000 io read MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox andy_0000 io write MB/s | MB/s | 32 | 0.001 | 0.000 | 0.037 | 0.000 | 0.003906 MB | n/a |
| sandbox andy_0000 memory | MB | 34 | 10.585 | 0.656 | 35.410 | 1.422 | n/a | n/a |
| sandbox andy_0000 net rx MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox andy_0000 net tx MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox arch_0000 CPU | percent | 29 | 61.063 | 3.599 | 99.137 | 27.564 | 1.862428 CPU seconds | n/a |
| sandbox arch_0000 io read MB/s | MB/s | 32 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox arch_0000 io write MB/s | MB/s | 32 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox arch_0000 memory | MB | 33 | 11.904 | 0.586 | 36.293 | 3.695 | n/a | n/a |
| sandbox arch_0000 net rx MB/s | MB/s | 32 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox arch_0000 net tx MB/s | MB/s | 32 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bake_0000 CPU | percent | 31 | 58.144 | 6.748 | 99.441 | 14.066 | 1.893651 CPU seconds | n/a |
| sandbox bake_0000 io read MB/s | MB/s | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bake_0000 io write MB/s | MB/s | 34 | 0.001 | 0.000 | 0.037 | 0.000 | 0.003906 MB | n/a |
| sandbox bake_0000 memory | MB | 36 | 10.645 | 0.582 | 34.555 | 0.953 | n/a | n/a |
| sandbox bake_0000 net rx MB/s | MB/s | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bake_0000 net tx MB/s | MB/s | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bale_0000 CPU | percent | 48 | 82.507 | 22.338 | 100.169 | 31.026 | 4.039803 CPU seconds | n/a |
| sandbox bale_0000 io read MB/s | MB/s | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bale_0000 io write MB/s | MB/s | 51 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bale_0000 memory | MB | 53 | 22.251 | 0.613 | 34.848 | 0.680 | n/a | n/a |
| sandbox bale_0000 net rx MB/s | MB/s | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bale_0000 net tx MB/s | MB/s | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox band_0000 CPU | percent | 21 | 59.663 | 10.807 | 100.099 | 31.293 | 1.298403 CPU seconds | n/a |
| sandbox band_0000 io read MB/s | MB/s | 25 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox band_0000 io write MB/s | MB/s | 24 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox band_0000 memory | MB | 26 | 8.949 | 0.734 | 35.379 | 0.914 | n/a | n/a |
| sandbox band_0000 net rx MB/s | MB/s | 25 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox band_0000 net tx MB/s | MB/s | 25 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bart_0000 CPU | percent | 20 | 60.672 | 14.225 | 100.952 | 29.258 | 1.244032 CPU seconds | n/a |
| sandbox bart_0000 io read MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bart_0000 io write MB/s | MB/s | 23 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bart_0000 memory | MB | 25 | 10.000 | 0.648 | 35.594 | 0.684 | n/a | n/a |
| sandbox bart_0000 net rx MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bart_0000 net tx MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox base_0000 CPU | percent | 316 | 93.403 | 13.036 | 133.618 | 48.323 | 30.751874 CPU seconds | n/a |
| sandbox base_0000 io read MB/s | MB/s | 325 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox base_0000 io write MB/s | MB/s | 323 | 0.047 | 0.000 | 15.084 | 0.000 | 1.832031 MB | n/a |
| sandbox base_0000 memory | MB | 326 | 30.133 | 0.664 | 34.176 | 4.281 | n/a | n/a |
| sandbox base_0000 net rx MB/s | MB/s | 325 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox base_0000 net tx MB/s | MB/s | 325 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beam_0000 CPU | percent | 26 | 62.234 | 3.998 | 113.451 | 31.918 | 1.733356 CPU seconds | n/a |
| sandbox beam_0000 io read MB/s | MB/s | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beam_0000 io write MB/s | MB/s | 29 | 0.001 | 0.000 | 0.037 | 0.000 | 0.003906 MB | n/a |
| sandbox beam_0000 memory | MB | 31 | 10.771 | 0.602 | 35.270 | 1.152 | n/a | n/a |
| sandbox beam_0000 net rx MB/s | MB/s | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beam_0000 net tx MB/s | MB/s | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bear_0000 CPU | percent | 29 | 59.143 | 15.774 | 116.922 | 78.783 | 1.901694 CPU seconds | n/a |
| sandbox bear_0000 io read MB/s | MB/s | 34 | 0.006 | 0.000 | 0.145 | 0.000 | 0.023438 MB | n/a |
| sandbox bear_0000 io write MB/s | MB/s | 35 | 0.167 | 0.000 | 5.808 | 0.000 | 0.812500 MB | n/a |
| sandbox bear_0000 memory | MB | 36 | 10.060 | 0.613 | 35.664 | 3.703 | n/a | n/a |
| sandbox bear_0000 net rx MB/s | MB/s | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bear_0000 net tx MB/s | MB/s | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beef_0000 CPU | percent | 21 | 60.437 | 14.919 | 100.010 | 30.636 | 1.319582 CPU seconds | n/a |
| sandbox beef_0000 io read MB/s | MB/s | 24 | 0.006 | 0.000 | 0.153 | 0.000 | 0.015625 MB | n/a |
| sandbox beef_0000 io write MB/s | MB/s | 24 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox beef_0000 memory | MB | 26 | 9.462 | 0.613 | 36.422 | 0.613 | n/a | n/a |
| sandbox beef_0000 net rx MB/s | MB/s | 25 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beef_0000 net tx MB/s | MB/s | 25 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bell_0000 CPU | percent | 25 | 54.202 | 2.107 | 100.038 | 95.535 | 1.410210 CPU seconds | n/a |
| sandbox bell_0000 io read MB/s | MB/s | 29 | 0.004 | 0.000 | 0.115 | 0.000 | 0.011719 MB | n/a |
| sandbox bell_0000 io write MB/s | MB/s | 29 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bell_0000 memory | MB | 30 | 8.090 | 0.762 | 36.539 | 3.938 | n/a | n/a |
| sandbox bell_0000 net rx MB/s | MB/s | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bell_0000 net tx MB/s | MB/s | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| workload total CPU | percent | 4164 | 31.804 | 0.620 | 199.983 | 85.708 | 136.779466 CPU seconds | n/a |
| workload total io read MB/s | MB/s | 657 | 0.045 | 0.000 | 27.873 | 0.000 | 3.132812 MB | n/a |
| workload total io write MB/s | MB/s | 652 | 0.125 | 0.000 | 33.066 | 0.000 | 9.128906 MB | n/a |
| workload total memory | MB | 4165 | 511.622 | 415.227 | 597.875 | 512.633 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
