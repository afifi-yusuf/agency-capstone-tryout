# agprof summary

- Duration: **761.671 s**
- Runs: **24/24 completed**, 24 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.032 runs/s**
- LLM: **85 calls**, 85 succeeded, 0 failed, 0 interrupted, 0 retries, 551.652 s total wait
- Tools: **109/109 completed**, 4 failed, 0 interrupted
- Raw resource samples: **75592** at 9.88 Hz effective (10 Hz configured)
- GPU sampling: **unavailable** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 23683.963 / 58139.728 ms |
| LLM latency p50 / p95 | 3000.531 / 23118.791 ms |
| LLM TTFT p50 / p95 | 675.775 / 1173.575 ms |
| LLM input / output tokens | 460330 / 26661 |
| LLM output throughput | 54.202 tokens/s |
| LLM attempts | 85 total, 85 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 407.691 / 1144.410 ms |

### Tool outcomes

| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 15/15 | 15 | 0 | 0 | 1141.007 ms | 1993.310 ms |
| edit | 13/13 | 13 | 0 | 0 | 418.913 ms | 738.642 ms |
| glob | 3/3 | 3 | 0 | 0 | 330.028 ms | 339.668 ms |
| grep | 1/1 | 1 | 0 | 0 | 333.079 ms | 333.079 ms |
| read | 37/37 | 37 | 0 | 0 | 412.563 ms | 587.714 ms |
| return_plan | 12/12 | 12 | 0 | 0 | 0.325 ms | 0.500 ms |
| return_status | 12/12 | 12 | 0 | 0 | 0.289 ms | 0.463 ms |
| return_summary | 16/16 | 12 | 4 | 0 | 0.351 ms | 0.456 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 14.443% | 111.538% | 110.679 s | 482.466 MB | 539.820 MB | 0.015625 MB | 0.050781 MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python3 | 89845 |  | 7524 | 3.635% | 237.720% | 27.840 s | 688.011 MB | 705.445 MB | 3737.574 MB | 3768.191 MB | 21.882812 MB | 35.320312 MB |
| git | 89851 |  | 5 | 0.000% | 0.000% | 0.000 s | 3.963 MB | 4.738 MB | 11.583 MB | 12.516 MB | 0.015625 MB | 0.000000 MB |
| git | 89852 |  | 4 | 0.000% | 0.000% | 0.000 s | 3.461 MB | 3.461 MB | 11.273 MB | 11.273 MB | 0.000000 MB | 0.000000 MB |
| git-remote-http | 89853 |  | 4 | 3.291% | 9.873% | 0.010 s | 19.108 MB | 19.176 MB | 107.066 MB | 107.566 MB | 0.175781 MB | 0.000000 MB |
| git | 89857 |  | 1 | n/a% | n/a% | n/a s | 4.844 MB | 4.844 MB | 13.207 MB | 13.207 MB | n/a MB | n/a MB |
| python3 | 89859 |  | 99 | 99.978% | 109.030% | 9.890 s | 33.887 MB | 34.172 MB | 57.210 MB | 57.457 MB | 0.000000 MB | 0.015625 MB |
| python3 | 89862 |  | 4 | 98.848% | 108.954% | 0.300 s | 21.358 MB | 33.910 MB | 46.604 MB | 57.457 MB | 0.000000 MB | 0.015625 MB |
| python3 | 89863 |  | 4 | 99.002% | 99.028% | 0.300 s | 28.979 MB | 36.215 MB | 52.089 MB | 58.457 MB | 0.000000 MB | 0.242188 MB |
| python3 | 89864 |  | 4 | 95.737% | 98.920% | 0.290 s | 29.098 MB | 34.879 MB | 52.521 MB | 57.508 MB | 0.085938 MB | 0.242188 MB |
| python3 | 89865 |  | 25 | 99.389% | 109.023% | 2.410 s | 33.134 MB | 34.852 MB | 56.384 MB | 57.508 MB | 0.078125 MB | 0.242188 MB |
| python3 | 89866 |  | 83 | 99.886% | 108.976% | 8.290 s | 41.306 MB | 47.758 MB | 64.347 MB | 70.645 MB | 0.000000 MB | 0.246094 MB |
| python3 | 89867 |  | 4 | 98.968% | 99.041% | 0.300 s | 27.847 MB | 34.719 MB | 51.702 MB | 57.457 MB | 0.000000 MB | 0.250000 MB |
| python3 | 89868 |  | 100 | 99.861% | 109.024% | 9.980 s | 34.025 MB | 34.496 MB | 57.071 MB | 57.457 MB | 0.000000 MB | 0.015625 MB |
| python3 | 89869 |  | 4 | 102.309% | 108.947% | 0.310 s | 27.960 MB | 34.996 MB | 51.462 MB | 57.496 MB | 0.003906 MB | 0.250000 MB |
| python3 | 89870 |  | 5 | 101.482% | 108.906% | 0.410 s | 26.280 MB | 34.797 MB | 50.365 MB | 57.492 MB | 0.000000 MB | 0.250000 MB |
| python3 | 89871 |  | 4 | 102.294% | 108.953% | 0.310 s | 28.142 MB | 34.789 MB | 51.748 MB | 57.504 MB | 0.000000 MB | 0.250000 MB |
| python3 | 89872 |  | 4 | 99.027% | 99.102% | 0.300 s | 25.814 MB | 34.840 MB | 49.732 MB | 57.504 MB | 0.000000 MB | 0.250000 MB |
| docker | 89876 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| docker | 89911 |  | 1 | n/a% | n/a% | n/a s | 22.453 MB | 22.453 MB | 1524.203 MB | 1524.203 MB | n/a MB | n/a MB |
| docker | 89927 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.052 MB | 27.152 MB | 1756.779 MB | 1804.781 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 89968 | alex_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 90019 |  | 1 | n/a% | n/a% | n/a s | 6.461 MB | 6.461 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| tail | 89982 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.691 MB | 1.691 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 90047 |  | 1 | n/a% | n/a% | n/a s | 26.953 MB | 26.953 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 90065 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.410 MB | 11.410 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 90080 |  | 1 | n/a% | n/a% | n/a s | 27.375 MB | 27.375 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 90117 |  | 1 | n/a% | n/a% | n/a s | 25.918 MB | 25.918 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 90169 |  | 1 | n/a% | n/a% | n/a s | 25.734 MB | 25.734 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 90218 | alex_0000 | 4 | 6.555% | 19.666% | 0.020 s | 3.587 MB | 12.449 MB | 393.473 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 90177 |  | 1 | n/a% | n/a% | n/a s | 26.840 MB | 26.840 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 90261 | alex_0000 | 1 | n/a% | n/a% | n/a s | 10.438 MB | 10.438 MB | 1641.449 MB | 1641.449 MB | n/a MB | n/a MB |
| tail | 90231 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 90241 |  | 1 | n/a% | n/a% | n/a s | 27.254 MB | 27.254 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 90334 |  | 1 | n/a% | n/a% | n/a s | 23.180 MB | 23.180 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 90342 |  | 1 | n/a% | n/a% | n/a s | 26.844 MB | 26.844 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 90402 |  | 1 | n/a% | n/a% | n/a s | 18.309 MB | 18.309 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 90425 |  | 38 | 0.000% | 0.000% | 0.000 s | 25.848 MB | 25.848 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 90441 |  | 1 | n/a% | n/a% | n/a s | 25.383 MB | 25.383 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 90467 |  | 2 | 9.878% | 9.878% | 0.010 s | 13.193 MB | 25.973 MB | 846.480 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 90507 | alex_0000 | 4 | 3.277% | 9.831% | 0.010 s | 3.502 MB | 12.109 MB | 375.347 MB | 1498.223 MB | n/a MB | n/a MB |
| docker | 90528 |  | 1 | n/a% | n/a% | n/a s | 27.250 MB | 27.250 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| tail | 90518 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 90557 |  | 1 | n/a% | n/a% | n/a s | 27.070 MB | 27.070 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 90625 |  | 1 | n/a% | n/a% | n/a s | 20.414 MB | 20.414 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 90633 |  | 1 | n/a% | n/a% | n/a s | 25.812 MB | 25.812 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 90692 |  | 1 | n/a% | n/a% | n/a s | 25.824 MB | 25.824 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 90732 | alex_0000 | 11 | 2.945% | 29.450% | 0.030 s | 1.593 MB | 11.195 MB | 143.636 MB | 1569.445 MB | n/a MB | n/a MB |
| tail | 90744 | alex_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.727 MB | 1.727 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 90754 |  | 1 | n/a% | n/a% | n/a s | 16.207 MB | 16.207 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 90782 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.090 MB | 27.090 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 90802 | alex_0000 | 8 | 1.402% | 9.816% | 0.010 s | 4.395 MB | 11.836 MB | 209.152 MB | 1642.480 MB | n/a MB | n/a MB |
| python | 90812 | alex_0000 | 7 | 99.697% | 107.901% | 0.610 s | 32.075 MB | 41.938 MB | 38.586 MB | 51.238 MB | n/a MB | n/a MB |
| docker | 90814 |  | 1 | n/a% | n/a% | n/a s | 15.457 MB | 15.457 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 90822 |  | 1 | n/a% | n/a% | n/a s | 25.922 MB | 25.922 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 90881 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.047 MB | 27.047 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 90921 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 4.695 MB | 12.820 MB | 524.195 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 90970 |  | 1 | n/a% | n/a% | n/a s | 3.359 MB | 3.359 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| tail | 90934 | alex_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.688 MB | 1.688 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 91006 |  | 1 | n/a% | n/a% | n/a s | 27.195 MB | 27.195 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 91042 |  | 1 | n/a% | n/a% | n/a s | 26.137 MB | 26.137 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 91085 |  | 1 | n/a% | n/a% | n/a s | 15.102 MB | 15.102 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 91094 |  | 1 | n/a% | n/a% | n/a s | 9.090 MB | 9.090 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 91118 |  | 1 | n/a% | n/a% | n/a s | 25.691 MB | 25.691 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 91126 |  | 39 | 0.000% | 0.000% | 0.000 s | 26.820 MB | 26.820 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 91151 |  | 1 | n/a% | n/a% | n/a s | 23.812 MB | 23.812 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| python3 | 91175 |  | 3 | 98.858% | 98.956% | 0.200 s | 26.902 MB | 33.574 MB | 50.487 MB | 56.461 MB | 0.011719 MB | 0.000000 MB |
| docker | 91196 |  | 1 | n/a% | n/a% | n/a s | 26.004 MB | 26.004 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 91226 |  | 3 | 4.939% | 9.877% | 0.010 s | 20.579 MB | 27.590 MB | 1166.105 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 91267 | andy_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.675 MB | 12.801 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 91280 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 91308 |  | 1 | n/a% | n/a% | n/a s | 2.535 MB | 2.535 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 91343 |  | 1 | n/a% | n/a% | n/a s | 26.191 MB | 26.191 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 91378 |  | 1 | n/a% | n/a% | n/a s | 27.328 MB | 27.328 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 91398 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.023 MB | 11.023 MB | 1641.836 MB | 1641.836 MB | n/a MB | n/a MB |
| docker | 91415 |  | 1 | n/a% | n/a% | n/a s | 26.027 MB | 26.027 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 91515 | andy_0000 | 4 | 6.531% | 19.592% | 0.020 s | 3.301 MB | 11.305 MB | 393.215 MB | 1569.695 MB | n/a MB | n/a MB |
| docker | 91472 |  | 1 | n/a% | n/a% | n/a s | 25.551 MB | 25.551 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 91537 |  | 1 | n/a% | n/a% | n/a s | 26.359 MB | 26.359 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| tail | 91527 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 91583 | andy_0000 | 1 | n/a% | n/a% | n/a s | 12.199 MB | 12.199 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 91563 |  | 1 | n/a% | n/a% | n/a s | 27.395 MB | 27.395 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 91629 |  | 1 | n/a% | n/a% | n/a s | 1.879 MB | 1.879 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 91637 |  | 1 | n/a% | n/a% | n/a s | 26.074 MB | 26.074 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 91686 |  | 1 | n/a% | n/a% | n/a s | 25.633 MB | 25.633 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 91694 |  | 1 | n/a% | n/a% | n/a s | 26.645 MB | 26.645 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 91731 | andy_0000 | 3 | 4.898% | 9.797% | 0.010 s | 4.349 MB | 11.781 MB | 523.983 MB | 1569.840 MB | n/a MB | n/a MB |
| tail | 91744 | andy_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 91756 |  | 1 | n/a% | n/a% | n/a s | 27.094 MB | 27.094 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| bash | 91809 | andy_0000 | 1 | n/a% | n/a% | n/a s | 1.688 MB | 1.688 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 91783 |  | 1 | n/a% | n/a% | n/a s | 27.301 MB | 27.301 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| bash | 91802 | andy_0000 | 1 | n/a% | n/a% | n/a s | 3.375 MB | 3.375 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 91824 |  | 1 | n/a% | n/a% | n/a s | 26.121 MB | 26.121 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 91884 |  | 2 | 9.881% | 9.881% | 0.010 s | 17.943 MB | 27.055 MB | 1444.104 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 91921 | andy_0000 | 3 | 4.915% | 9.830% | 0.010 s | 4.633 MB | 12.633 MB | 524.279 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 91944 |  | 1 | n/a% | n/a% | n/a s | 27.367 MB | 27.367 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 91934 | andy_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| bash | 91991 | andy_0000 | 1 | n/a% | n/a% | n/a s | 3.320 MB | 3.320 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| rg | 92000 | andy_0000 | 1 | n/a% | n/a% | n/a s | 2.066 MB | 2.066 MB | 8.234 MB | 8.234 MB | n/a MB | n/a MB |
| docker | 91971 |  | 1 | n/a% | n/a% | n/a s | 27.207 MB | 27.207 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 92014 |  | 1 | n/a% | n/a% | n/a s | 26.152 MB | 26.152 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 92074 |  | 2 | 0.000% | 0.000% | 0.000 s | 23.086 MB | 25.852 MB | 1588.205 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 92114 | andy_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.681 MB | 12.824 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 92154 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.363 MB | 11.363 MB | 1570.098 MB | 1570.098 MB | n/a MB | n/a MB |
| tail | 92126 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 92136 |  | 1 | n/a% | n/a% | n/a s | 27.176 MB | 27.176 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 92188 |  | 1 | n/a% | n/a% | n/a s | 21.410 MB | 21.410 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 92232 |  | 1 | n/a% | n/a% | n/a s | 26.008 MB | 26.008 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 92299 |  | 1 | n/a% | n/a% | n/a s | 26.859 MB | 26.859 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 92313 |  | 37 | 0.000% | 0.000% | 0.000 s | 26.730 MB | 26.730 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 92329 |  | 1 | n/a% | n/a% | n/a s | 25.078 MB | 25.078 MB | 1587.957 MB | 1587.957 MB | n/a MB | n/a MB |
| docker | 92356 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.633 MB | 25.633 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 92396 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 92408 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 92445 |  | 1 | n/a% | n/a% | n/a s | 22.453 MB | 22.453 MB | 1524.203 MB | 1524.203 MB | n/a MB | n/a MB |
| docker | 92480 |  | 1 | n/a% | n/a% | n/a s | 27.199 MB | 27.199 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 92520 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.863 MB | 25.863 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 92571 |  | 1 | n/a% | n/a% | n/a s | 15.773 MB | 15.773 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 92579 |  | 1 | n/a% | n/a% | n/a s | 27.027 MB | 27.027 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| 6 | 92615 | andy_0000 | 1 | n/a% | n/a% | n/a s | 1.797 MB | 1.797 MB | 13.980 MB | 13.980 MB | n/a MB | n/a MB |
| docker | 92642 |  | 1 | n/a% | n/a% | n/a s | 2.621 MB | 2.621 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| tail | 92632 | andy_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 92619 | andy_0000 | 10 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 92689 | andy_0000 | 9 | 2.433% | 19.466% | 0.020 s | 4.277 MB | 10.648 MB | 178.301 MB | 1569.582 MB | n/a MB | n/a MB |
| docker | 92669 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.359 MB | 27.359 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 92698 | andy_0000 | 8 | 100.827% | 107.913% | 0.720 s | 32.916 MB | 41.770 MB | 39.968 MB | 51.238 MB | n/a MB | n/a MB |
| docker | 92708 |  | 1 | n/a% | n/a% | n/a s | 25.883 MB | 25.883 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 92770 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.648 MB | 25.648 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 92809 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 92821 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 92859 |  | 1 | n/a% | n/a% | n/a s | 18.613 MB | 18.613 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 92896 |  | 1 | n/a% | n/a% | n/a s | 27.457 MB | 27.457 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 92911 | andy_0000 | 1 | n/a% | n/a% | n/a s | 1.980 MB | 1.980 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 92933 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.133 MB | 27.133 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 93008 |  | 1 | n/a% | n/a% | n/a s | 25.527 MB | 25.527 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 93016 |  | 43 | 0.000% | 0.000% | 0.000 s | 27.133 MB | 27.133 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 93044 |  | 1 | n/a% | n/a% | n/a s | 25.223 MB | 25.223 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| python3 | 93067 |  | 4 | 95.574% | 98.949% | 0.290 s | 22.736 MB | 34.395 MB | 47.828 MB | 57.438 MB | 0.000000 MB | 0.218750 MB |
| docker | 93097 |  | 1 | n/a% | n/a% | n/a s | 24.727 MB | 24.727 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 93105 |  | 1 | n/a% | n/a% | n/a s | 19.891 MB | 19.891 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 93120 |  | 2 | 19.588% | 19.588% | 0.020 s | 27.340 MB | 27.621 MB | 1696.775 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 93161 | arch_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.541 MB | 12.266 MB | 411.411 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 93177 |  | 1 | n/a% | n/a% | n/a s | 27.117 MB | 27.117 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 93196 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| tail | 93175 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 93239 |  | 1 | n/a% | n/a% | n/a s | 17.004 MB | 17.004 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 93273 |  | 1 | n/a% | n/a% | n/a s | 27.352 MB | 27.352 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 93309 |  | 1 | n/a% | n/a% | n/a s | 26.141 MB | 26.141 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 93353 |  | 1 | n/a% | n/a% | n/a s | 7.848 MB | 7.848 MB | 32.867 MB | 32.867 MB | n/a MB | n/a MB |
| docker | 93370 |  | 1 | n/a% | n/a% | n/a s | 25.527 MB | 25.527 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| 6 | 93405 | arch_0000 | 1 | n/a% | n/a% | n/a s | 1.812 MB | 1.812 MB | 13.980 MB | 13.980 MB | n/a MB | n/a MB |
| docker | 93432 |  | 1 | n/a% | n/a% | n/a s | 6.574 MB | 6.574 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| tail | 93421 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 93408 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 93459 |  | 1 | n/a% | n/a% | n/a s | 27.434 MB | 27.434 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 93480 | arch_0000 | 1 | n/a% | n/a% | n/a s | 11.117 MB | 11.117 MB | 1569.840 MB | 1569.840 MB | n/a MB | n/a MB |
| docker | 93495 |  | 1 | n/a% | n/a% | n/a s | 26.875 MB | 26.875 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 93515 | arch_0000 | 1 | n/a% | n/a% | n/a s | 12.219 MB | 12.219 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 93532 |  | 1 | n/a% | n/a% | n/a s | 25.906 MB | 25.906 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 93592 |  | 1 | n/a% | n/a% | n/a s | 27.051 MB | 27.051 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 93614 |  | 38 | 0.000% | 0.000% | 0.000 s | 25.793 MB | 25.793 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 93630 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 93657 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.895 MB | 26.895 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| tail | 93708 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 93695 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 93746 |  | 1 | n/a% | n/a% | n/a s | 6.340 MB | 6.340 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 93783 |  | 1 | n/a% | n/a% | n/a s | 26.980 MB | 26.980 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 93821 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.012 MB | 26.012 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 93882 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.652 MB | 26.652 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 93921 | arch_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.729 MB | 12.695 MB | 137.161 MB | 1498.223 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 93963 | arch_0000 | 1 | n/a% | n/a% | n/a s | 12.418 MB | 12.418 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| tail | 93934 | arch_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 93944 |  | 1 | n/a% | n/a% | n/a s | 27.617 MB | 27.617 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| bash | 93990 | arch_0000 | 9 | 0.000% | 0.000% | 0.000 s | 3.340 MB | 3.340 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 93999 | arch_0000 | 9 | 100.398% | 107.824% | 0.820 s | 31.544 MB | 41.547 MB | 39.313 MB | 51.219 MB | n/a MB | n/a MB |
| docker | 93971 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.340 MB | 27.340 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 94009 |  | 1 | n/a% | n/a% | n/a s | 25.645 MB | 25.645 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 94061 |  | 1 | n/a% | n/a% | n/a s | 25.402 MB | 25.402 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker-init | 94101 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 94114 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.727 MB | 1.727 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 94117 |  | 1 | n/a% | n/a% | n/a s | 26.051 MB | 26.051 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 94171 | arch_0000 | 1 | n/a% | n/a% | n/a s | 10.781 MB | 10.781 MB | 1641.578 MB | 1641.578 MB | n/a MB | n/a MB |
| docker | 94151 |  | 1 | n/a% | n/a% | n/a s | 27.512 MB | 27.512 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 94206 | arch_0000 | 1 | n/a% | n/a% | n/a s | 11.484 MB | 11.484 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 94187 |  | 1 | n/a% | n/a% | n/a s | 27.527 MB | 27.527 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 94223 |  | 1 | n/a% | n/a% | n/a s | 26.129 MB | 26.129 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 94300 |  | 1 | n/a% | n/a% | n/a s | 25.371 MB | 25.371 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 94308 |  | 38 | 0.000% | 0.000% | 0.000 s | 25.602 MB | 25.602 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 94341 |  | 1 | n/a% | n/a% | n/a s | 25.656 MB | 25.656 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| python3 | 94357 |  | 4 | 102.122% | 108.529% | 0.310 s | 27.766 MB | 34.516 MB | 51.471 MB | 57.438 MB | 0.000000 MB | 0.238281 MB |
| docker | 94370 |  | 1 | n/a% | n/a% | n/a s | 8.543 MB | 8.543 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 94394 |  | 1 | n/a% | n/a% | n/a s | 26.699 MB | 26.699 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 94408 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.430 MB | 27.430 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 94450 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.704 MB | 12.918 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 94494 |  | 1 | n/a% | n/a% | n/a s | 26.496 MB | 26.496 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| tail | 94463 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 94529 |  | 1 | n/a% | n/a% | n/a s | 26.820 MB | 26.820 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 94549 | bake_0000 | 1 | n/a% | n/a% | n/a s | 10.164 MB | 10.164 MB | 1569.195 MB | 1569.195 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 94583 | bake_0000 | 1 | n/a% | n/a% | n/a s | 12.195 MB | 12.195 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 94564 |  | 1 | n/a% | n/a% | n/a s | 27.195 MB | 27.195 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 94599 |  | 1 | n/a% | n/a% | n/a s | 26.086 MB | 26.086 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 94657 |  | 2 | 0.000% | 0.000% | 0.000 s | 18.600 MB | 25.797 MB | 1555.955 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 94696 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.692 MB | 12.871 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 94720 |  | 1 | n/a% | n/a% | n/a s | 27.047 MB | 27.047 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 94740 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.574 MB | 11.574 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 94709 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 94773 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 94820 |  | 2 | 0.000% | 0.000% | 0.000 s | 23.631 MB | 26.902 MB | 1624.488 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 94870 |  | 1 | n/a% | n/a% | n/a s | 11.125 MB | 11.125 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 94878 |  | 3 | 0.000% | 0.000% | 0.000 s | 25.434 MB | 25.434 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 94916 | bake_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.020 MB | 12.570 MB | 300.488 MB | 1498.223 MB | n/a MB | n/a MB |
| docker | 94930 |  | 1 | n/a% | n/a% | n/a s | 21.504 MB | 21.504 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| tail | 94928 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 94938 |  | 1 | n/a% | n/a% | n/a s | 27.340 MB | 27.340 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 94957 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.578 MB | 11.578 MB | 1642.230 MB | 1642.230 MB | n/a MB | n/a MB |
| docker | 94991 |  | 1 | n/a% | n/a% | n/a s | 20.195 MB | 20.195 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 95029 |  | 1 | n/a% | n/a% | n/a s | 24.324 MB | 24.324 MB | 1588.270 MB | 1588.270 MB | n/a MB | n/a MB |
| docker | 95037 |  | 1 | n/a% | n/a% | n/a s | 27.086 MB | 27.086 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 95115 |  | 38 | 0.000% | 0.000% | 0.000 s | 27.004 MB | 27.004 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 95157 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.730 MB | 25.730 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 95198 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.742 MB | 13.070 MB | 411.411 MB | 1642.480 MB | n/a MB | n/a MB |
| sh | 95241 | bake_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.516 MB | 0.516 MB | n/a MB | n/a MB |
| tail | 95211 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 95221 |  | 1 | n/a% | n/a% | n/a s | 27.332 MB | 27.332 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 95285 |  | 1 | n/a% | n/a% | n/a s | 8.680 MB | 8.680 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 95325 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.059 MB | 26.059 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 95384 |  | 2 | 0.000% | 0.000% | 0.000 s | 15.840 MB | 25.465 MB | 846.486 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 95423 | bake_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.741 MB | 12.820 MB | 143.707 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 95446 |  | 1 | n/a% | n/a% | n/a s | 27.250 MB | 27.250 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 95465 | bake_0000 | 1 | n/a% | n/a% | n/a s | 12.039 MB | 12.039 MB | 1714.734 MB | 1714.734 MB | n/a MB | n/a MB |
| tail | 95436 | bake_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 95474 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.684 MB | 27.684 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| bash | 95495 | bake_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.359 MB | 3.359 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 95505 | bake_0000 | 8 | 99.358% | 107.954% | 0.710 s | 30.345 MB | 41.426 MB | 37.245 MB | 50.375 MB | n/a MB | n/a MB |
| docker | 95515 |  | 1 | n/a% | n/a% | n/a s | 25.883 MB | 25.883 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 95575 |  | 1 | n/a% | n/a% | n/a s | 26.816 MB | 26.816 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| tail | 95628 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 95616 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 95630 |  | 1 | n/a% | n/a% | n/a s | 25.633 MB | 25.633 MB | 1596.211 MB | 1596.211 MB | n/a MB | n/a MB |
| docker | 95667 |  | 1 | n/a% | n/a% | n/a s | 27.320 MB | 27.320 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 95703 |  | 1 | n/a% | n/a% | n/a s | 27.332 MB | 27.332 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 95721 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.488 MB | 11.488 MB | 1570.098 MB | 1570.098 MB | n/a MB | n/a MB |
| docker | 95737 |  | 1 | n/a% | n/a% | n/a s | 25.965 MB | 25.965 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 95795 |  | 1 | n/a% | n/a% | n/a s | 19.926 MB | 19.926 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 95813 |  | 1 | n/a% | n/a% | n/a s | 19.238 MB | 19.238 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 95830 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.672 MB | 25.672 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 95862 |  | 1 | n/a% | n/a% | n/a s | 20.289 MB | 20.289 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| python3 | 95878 |  | 4 | 98.814% | 108.561% | 0.300 s | 25.186 MB | 34.520 MB | 49.572 MB | 57.434 MB | 0.000000 MB | 0.238281 MB |
| docker | 95899 |  | 1 | n/a% | n/a% | n/a s | 25.855 MB | 25.855 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 95929 |  | 3 | 4.932% | 9.865% | 0.010 s | 19.318 MB | 27.199 MB | 1166.105 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 95969 | bale_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.723 MB | 12.992 MB | 411.411 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 96011 |  | 1 | n/a% | n/a% | n/a s | 23.023 MB | 23.023 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| tail | 95983 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 96048 |  | 1 | n/a% | n/a% | n/a s | 27.340 MB | 27.340 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 96102 | bale_0000 | 1 | n/a% | n/a% | n/a s | 11.867 MB | 11.867 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 96082 |  | 1 | n/a% | n/a% | n/a s | 27.520 MB | 27.520 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 96118 |  | 1 | n/a% | n/a% | n/a s | 26.086 MB | 26.086 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 96168 |  | 1 | n/a% | n/a% | n/a s | 17.812 MB | 17.812 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 96176 |  | 1 | n/a% | n/a% | n/a s | 25.590 MB | 25.590 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 96215 | bale_0000 | 4 | 6.522% | 19.565% | 0.020 s | 3.524 MB | 12.199 MB | 393.376 MB | 1570.340 MB | n/a MB | n/a MB |
| docker | 96240 |  | 1 | n/a% | n/a% | n/a s | 27.375 MB | 27.375 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 96229 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 96271 |  | 1 | n/a% | n/a% | n/a s | 27.477 MB | 27.477 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 96334 |  | 1 | n/a% | n/a% | n/a s | 3.781 MB | 3.781 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 96342 |  | 1 | n/a% | n/a% | n/a s | 27.188 MB | 27.188 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 96411 |  | 1 | n/a% | n/a% | n/a s | 16.621 MB | 16.621 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 96425 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.816 MB | 26.816 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 96460 |  | 1 | n/a% | n/a% | n/a s | 22.719 MB | 22.719 MB | 1524.203 MB | 1524.203 MB | n/a MB | n/a MB |
| docker | 96468 |  | 4 | 13.026% | 39.077% | 0.040 s | 23.403 MB | 25.664 MB | 1624.083 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[0:PARENT] | 96504 | bale_0000 | 1 | n/a% | n/a% | n/a s | 1.957 MB | 1.957 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| runc:[1:CHILD] | 96506 | bale_0000 | 1 | n/a% | n/a% | n/a s | 0.660 MB | 0.660 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 96507 | bale_0000 | 7 | 1.603% | 9.616% | 0.010 s | 2.379 MB | 12.855 MB | 225.258 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 96520 | bale_0000 | 6 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| run9:repair_bug | 96523 |  | 1 | n/a% | n/a% | n/a s | 687.434 MB | 687.434 MB | 3754.559 MB | 3754.559 MB | n/a MB | n/a MB |
| docker | 96532 |  | 2 | 58.700% | 58.700% | 0.060 s | 14.529 MB | 26.711 MB | 846.768 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 96550 | bale_0000 | 1 | n/a% | n/a% | n/a s | 10.285 MB | 10.285 MB | 1641.449 MB | 1641.449 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 96578 | bale_0000 | 1 | n/a% | n/a% | n/a s | 11.836 MB | 11.836 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 96559 |  | 1 | n/a% | n/a% | n/a s | 27.395 MB | 27.395 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 96595 |  | 1 | n/a% | n/a% | n/a s | 25.441 MB | 25.441 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 96625 |  | 1 | n/a% | n/a% | n/a s | 5.660 MB | 5.660 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 96633 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.875 MB | 26.875 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 96684 |  | 1 | n/a% | n/a% | n/a s | 19.500 MB | 19.500 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 96693 |  | 1 | n/a% | n/a% | n/a s | 26.973 MB | 26.973 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 96733 | bale_0000 | 38 | 0.528% | 19.525% | 0.020 s | 0.904 MB | 10.930 MB | 42.322 MB | 1569.195 MB | n/a MB | n/a MB |
| tail | 96746 | bale_0000 | 37 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 96756 |  | 1 | n/a% | n/a% | n/a s | 25.738 MB | 25.738 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 96785 |  | 35 | 0.000% | 0.000% | 0.000 s | 27.227 MB | 27.227 MB | 1661.023 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 96808 | bale_0000 | 35 | 0.576% | 19.599% | 0.020 s | 3.573 MB | 11.488 MB | 49.129 MB | 1570.227 MB | n/a MB | n/a MB |
| python | 96817 | bale_0000 | 34 | 99.804% | 107.960% | 3.370 s | 39.779 MB | 41.797 MB | 48.763 MB | 51.324 MB | n/a MB | n/a MB |
| docker | 96819 |  | 1 | n/a% | n/a% | n/a s | 24.059 MB | 24.059 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 96827 |  | 1 | n/a% | n/a% | n/a s | 25.996 MB | 25.996 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| 6 | 96925 | bale_0000 | 1 | n/a% | n/a% | n/a s | 1.789 MB | 1.789 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 96888 |  | 1 | n/a% | n/a% | n/a s | 26.594 MB | 26.594 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker-init | 96927 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 96942 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 96952 |  | 1 | n/a% | n/a% | n/a s | 3.230 MB | 3.230 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 97000 | bale_0000 | 1 | n/a% | n/a% | n/a s | 10.633 MB | 10.633 MB | 1569.445 MB | 1569.445 MB | n/a MB | n/a MB |
| docker | 96981 |  | 1 | n/a% | n/a% | n/a s | 27.355 MB | 27.355 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 97017 |  | 1 | n/a% | n/a% | n/a s | 27.039 MB | 27.039 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 97035 | bale_0000 | 1 | n/a% | n/a% | n/a s | 11.770 MB | 11.770 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 97052 |  | 1 | n/a% | n/a% | n/a s | 26.125 MB | 26.125 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 97119 |  | 1 | n/a% | n/a% | n/a s | 26.078 MB | 26.078 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 97135 |  | 39 | 0.000% | 0.000% | 0.000 s | 26.871 MB | 26.871 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 97161 |  | 1 | n/a% | n/a% | n/a s | 15.340 MB | 15.340 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| python3 | 97185 |  | 24 | 100.231% | 108.878% | 2.330 s | 33.229 MB | 34.598 MB | 56.739 MB | 57.461 MB | 0.000000 MB | 0.238281 MB |
| docker | 97190 |  | 1 | n/a% | n/a% | n/a s | 23.898 MB | 23.898 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 97237 |  | 2 | 9.868% | 9.868% | 0.010 s | 24.607 MB | 27.613 MB | 1624.488 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 97279 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 97291 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 97357 |  | 1 | n/a% | n/a% | n/a s | 27.434 MB | 27.434 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 97375 | band_0000 | 1 | n/a% | n/a% | n/a s | 9.090 MB | 9.090 MB | 1505.195 MB | 1505.195 MB | n/a MB | n/a MB |
| docker | 97391 |  | 1 | n/a% | n/a% | n/a s | 26.984 MB | 26.984 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 97412 | band_0000 | 1 | n/a% | n/a% | n/a s | 11.703 MB | 11.703 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 97429 |  | 1 | n/a% | n/a% | n/a s | 27.031 MB | 27.031 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 97489 |  | 2 | 0.000% | 0.000% | 0.000 s | 13.412 MB | 25.629 MB | 846.486 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 97529 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.681 MB | 12.824 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 97551 |  | 1 | n/a% | n/a% | n/a s | 27.133 MB | 27.133 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 97570 | band_0000 | 1 | n/a% | n/a% | n/a s | 11.156 MB | 11.156 MB | 1641.965 MB | 1641.965 MB | n/a MB | n/a MB |
| tail | 97541 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 97605 |  | 1 | n/a% | n/a% | n/a s | 21.613 MB | 21.613 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 97653 |  | 2 | 0.000% | 0.000% | 0.000 s | 14.205 MB | 26.184 MB | 846.486 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 97713 |  | 1 | n/a% | n/a% | n/a s | 14.375 MB | 14.375 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 97735 |  | 37 | 0.000% | 0.000% | 0.000 s | 26.566 MB | 26.566 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 97751 |  | 1 | n/a% | n/a% | n/a s | 25.914 MB | 25.914 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 97777 |  | 2 | 9.826% | 9.826% | 0.010 s | 14.592 MB | 25.652 MB | 846.486 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[1:CHILD] | 97818 | band_0000 | 1 | n/a% | n/a% | n/a s | 0.844 MB | 0.844 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 97819 | band_0000 | 5 | 9.712% | 38.846% | 0.040 s | 0.681 MB | 0.875 MB | 3.666 MB | 14.109 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 97816 | band_0000 | 1 | n/a% | n/a% | n/a s | 1.965 MB | 1.965 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| tail | 97833 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.723 MB | 1.723 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 97835 |  | 1 | n/a% | n/a% | n/a s | 2.641 MB | 2.641 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 97844 |  | 1 | n/a% | n/a% | n/a s | 27.293 MB | 27.293 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 97910 |  | 1 | n/a% | n/a% | n/a s | 20.234 MB | 20.234 MB | 1523.953 MB | 1523.953 MB | n/a MB | n/a MB |
| docker | 97949 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.699 MB | 26.699 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 98009 |  | 1 | n/a% | n/a% | n/a s | 26.707 MB | 26.707 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 98049 | band_0000 | 11 | 0.981% | 9.808% | 0.010 s | 1.711 MB | 12.492 MB | 150.298 MB | 1642.730 MB | n/a MB | n/a MB |
| tail | 98063 | band_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 98074 |  | 1 | n/a% | n/a% | n/a s | 27.535 MB | 27.535 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 98122 | band_0000 | 9 | 0.000% | 0.000% | 0.000 s | 4.359 MB | 11.984 MB | 186.401 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 98102 |  | 9 | 1.226% | 9.805% | 0.010 s | 27.387 MB | 27.387 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 98132 | band_0000 | 8 | 100.754% | 107.855% | 0.720 s | 32.968 MB | 40.871 MB | 40.033 MB | 50.324 MB | n/a MB | n/a MB |
| docker | 98142 |  | 1 | n/a% | n/a% | n/a s | 25.883 MB | 25.883 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 98183 |  | 1 | n/a% | n/a% | n/a s | 26.539 MB | 26.539 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 98201 |  | 2 | 0.000% | 0.000% | 0.000 s | 24.955 MB | 26.797 MB | 1624.488 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 98240 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.750 MB | 13.102 MB | 393.473 MB | 1570.727 MB | n/a MB | n/a MB |
| tail | 98254 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 98266 |  | 1 | n/a% | n/a% | n/a s | 27.219 MB | 27.219 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 98291 | band_0000 | 1 | n/a% | n/a% | n/a s | 12.371 MB | 12.371 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 98372 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.957 MB | 25.957 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 98439 |  | 1 | n/a% | n/a% | n/a s | 26.543 MB | 26.543 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 98455 |  | 39 | 0.000% | 0.000% | 0.000 s | 26.988 MB | 26.988 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 98480 |  | 1 | n/a% | n/a% | n/a s | 27.141 MB | 27.141 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 98503 |  | 3 | 98.733% | 108.797% | 0.200 s | 28.171 MB | 33.961 MB | 52.094 MB | 57.461 MB | 0.000000 MB | 0.000000 MB |
| docker | 98509 |  | 1 | n/a% | n/a% | n/a s | 19.426 MB | 19.426 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 98534 |  | 1 | n/a% | n/a% | n/a s | 26.332 MB | 26.332 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 98557 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.252 MB | 27.383 MB | 1696.775 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| tail | 98612 | bart_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 98614 |  | 1 | n/a% | n/a% | n/a s | 9.219 MB | 9.219 MB | 1251.695 MB | 1251.695 MB | n/a MB | n/a MB |
| docker-init | 98596 | bart_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 98649 |  | 1 | n/a% | n/a% | n/a s | 27.148 MB | 27.148 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 98677 |  | 1 | n/a% | n/a% | n/a s | 27.332 MB | 27.332 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 98740 |  | 1 | n/a% | n/a% | n/a s | 26.285 MB | 26.285 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 98748 |  | 1 | n/a% | n/a% | n/a s | 26.746 MB | 26.746 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 98809 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.527 MB | 25.527 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 98847 | bart_0000 | 4 | 3.272% | 9.816% | 0.010 s | 3.750 MB | 13.102 MB | 393.535 MB | 1570.977 MB | n/a MB | n/a MB |
| docker | 98870 |  | 1 | n/a% | n/a% | n/a s | 27.465 MB | 27.465 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 98889 | bart_0000 | 1 | n/a% | n/a% | n/a s | 12.160 MB | 12.160 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 98860 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 98934 |  | 1 | n/a% | n/a% | n/a s | 5.668 MB | 5.668 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 98969 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.824 MB | 25.824 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 99045 |  | 38 | 0.000% | 0.000% | 0.000 s | 25.406 MB | 25.406 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 99069 |  | 1 | n/a% | n/a% | n/a s | 1.031 MB | 1.031 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 99088 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.535 MB | 25.535 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 99128 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 99140 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 99179 |  | 1 | n/a% | n/a% | n/a s | 9.363 MB | 9.363 MB | 1323.699 MB | 1323.699 MB | n/a MB | n/a MB |
| docker | 99216 |  | 1 | n/a% | n/a% | n/a s | 27.223 MB | 27.223 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 99254 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.996 MB | 25.996 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 99313 |  | 1 | n/a% | n/a% | n/a s | 26.988 MB | 26.988 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker-init | 99351 | bart_0000 | 10 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 99367 |  | 1 | n/a% | n/a% | n/a s | 16.578 MB | 16.578 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| tail | 99365 | bart_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 99404 |  | 9 | 1.225% | 9.799% | 0.010 s | 25.010 MB | 27.141 MB | 1479.895 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 99433 | bart_0000 | 8 | 100.789% | 107.857% | 0.720 s | 31.821 MB | 41.820 MB | 38.916 MB | 51.324 MB | n/a MB | n/a MB |
| bash | 99424 | bart_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.391 MB | 3.391 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 99444 |  | 1 | n/a% | n/a% | n/a s | 27.102 MB | 27.102 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 99486 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 12.242 MB | 12.242 MB | n/a MB | n/a MB |
| docker | 99503 |  | 1 | n/a% | n/a% | n/a s | 26.609 MB | 26.609 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 99556 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 99543 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 99612 | bart_0000 | 1 | n/a% | n/a% | n/a s | 10.555 MB | 10.555 MB | 1569.324 MB | 1569.324 MB | n/a MB | n/a MB |
| docker | 99594 |  | 1 | n/a% | n/a% | n/a s | 27.301 MB | 27.301 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 99647 | bart_0000 | 1 | n/a% | n/a% | n/a s | 12.195 MB | 12.195 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 99627 |  | 1 | n/a% | n/a% | n/a s | 27.547 MB | 27.547 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 99663 |  | 1 | n/a% | n/a% | n/a s | 26.707 MB | 26.707 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 99739 |  | 1 | n/a% | n/a% | n/a s | 23.008 MB | 23.008 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 99747 |  | 47 | 0.000% | 0.000% | 0.000 s | 27.230 MB | 27.230 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 99774 |  | 1 | n/a% | n/a% | n/a s | 26.879 MB | 26.879 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 99798 |  | 4 | 98.844% | 108.811% | 0.300 s | 21.699 MB | 34.449 MB | 46.629 MB | 57.438 MB | 0.000000 MB | 0.234375 MB |
| docker | 99827 |  | 1 | n/a% | n/a% | n/a s | 13.391 MB | 13.391 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 99850 |  | 3 | 14.817% | 29.634% | 0.030 s | 21.536 MB | 27.664 MB | 1593.750 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 99889 | base_0000 | 4 | 3.282% | 9.845% | 0.010 s | 3.711 MB | 12.945 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 99903 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 99931 |  | 1 | n/a% | n/a% | n/a s | 25.633 MB | 25.633 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 99987 | base_0000 | 1 | n/a% | n/a% | n/a s | 4.340 MB | 4.340 MB | 1433.191 MB | 1433.191 MB | n/a MB | n/a MB |
| docker | 99968 |  | 1 | n/a% | n/a% | n/a s | 27.547 MB | 27.547 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 100002 |  | 1 | n/a% | n/a% | n/a s | 27.340 MB | 27.340 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 100022 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.984 MB | 11.984 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 100040 |  | 1 | n/a% | n/a% | n/a s | 25.969 MB | 25.969 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 100092 |  | 1 | n/a% | n/a% | n/a s | 26.188 MB | 26.188 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 100100 |  | 1 | n/a% | n/a% | n/a s | 25.570 MB | 25.570 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 100140 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.582 MB | 12.430 MB | 411.411 MB | 1642.480 MB | n/a MB | n/a MB |
| tail | 100154 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 100165 |  | 1 | n/a% | n/a% | n/a s | 27.016 MB | 27.016 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 100184 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.133 MB | 11.133 MB | 1641.836 MB | 1641.836 MB | n/a MB | n/a MB |
| docker | 100219 |  | 1 | n/a% | n/a% | n/a s | 16.180 MB | 16.180 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 100257 |  | 1 | n/a% | n/a% | n/a s | 26.348 MB | 26.348 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 100265 |  | 1 | n/a% | n/a% | n/a s | 27.055 MB | 27.055 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 100350 |  | 39 | 0.515% | 19.562% | 0.020 s | 26.082 MB | 26.578 MB | 1619.032 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 100374 |  | 1 | n/a% | n/a% | n/a s | 21.676 MB | 21.676 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 100393 |  | 1 | n/a% | n/a% | n/a s | 27.230 MB | 27.230 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 100444 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 100432 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 100446 |  | 1 | n/a% | n/a% | n/a s | 12.180 MB | 12.180 MB | 1451.699 MB | 1451.699 MB | n/a MB | n/a MB |
| docker | 100482 |  | 1 | n/a% | n/a% | n/a s | 26.906 MB | 26.906 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 100520 |  | 1 | n/a% | n/a% | n/a s | 27.453 MB | 27.453 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 100540 | base_0000 | 1 | n/a% | n/a% | n/a s | 8.930 MB | 8.930 MB | 1496.941 MB | 1496.941 MB | n/a MB | n/a MB |
| docker | 100557 |  | 1 | n/a% | n/a% | n/a s | 26.969 MB | 26.969 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 100600 |  | 1 | n/a% | n/a% | n/a s | 3.156 MB | 3.156 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 100619 |  | 1 | n/a% | n/a% | n/a s | 27.160 MB | 27.160 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 100671 | base_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 100658 | base_0000 | 11 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 100708 |  | 9 | 1.225% | 9.798% | 0.010 s | 25.867 MB | 27.168 MB | 1644.682 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 100737 | base_0000 | 8 | 100.754% | 107.828% | 0.720 s | 31.487 MB | 40.562 MB | 38.518 MB | 50.027 MB | n/a MB | n/a MB |
| bash | 100728 | base_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.418 MB | 3.418 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 100747 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.828 MB | 26.891 MB | 1660.648 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 100807 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.629 MB | 26.629 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 100848 | base_0000 | 3 | 4.855% | 9.711% | 0.010 s | 0.422 MB | 0.633 MB | 0.704 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 100859 | base_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 100898 |  | 1 | n/a% | n/a% | n/a s | 11.152 MB | 11.152 MB | 1451.699 MB | 1451.699 MB | n/a MB | n/a MB |
| docker | 100938 |  | 1 | n/a% | n/a% | n/a s | 27.180 MB | 27.180 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 100988 |  | 1 | n/a% | n/a% | n/a s | 15.340 MB | 15.340 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 100996 |  | 4 | 16.282% | 48.847% | 0.050 s | 24.249 MB | 27.141 MB | 1624.567 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 101034 | base_0000 | 5 | 7.311% | 29.243% | 0.030 s | 2.598 MB | 10.457 MB | 329.134 MB | 1641.449 MB | n/a MB | n/a MB |
| tail | 101048 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.672 MB | 1.672 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 101058 |  | 1 | n/a% | n/a% | n/a s | 27.324 MB | 27.324 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 101104 | base_0000 | 2 | 28.893% | 28.893% | 0.030 s | 3.053 MB | 3.414 MB | 606.502 MB | 1208.613 MB | n/a MB | n/a MB |
| docker | 101085 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.281 MB | 27.281 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 101113 | base_0000 | 1 | n/a% | n/a% | n/a s | 10.898 MB | 10.898 MB | 14.805 MB | 14.805 MB | n/a MB | n/a MB |
| docker | 101123 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.574 MB | 26.574 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 101186 |  | 1 | n/a% | n/a% | n/a s | 26.973 MB | 26.973 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker-init | 101225 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 101238 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 101275 |  | 1 | n/a% | n/a% | n/a s | 26.902 MB | 26.902 MB | 1588.520 MB | 1588.520 MB | n/a MB | n/a MB |
| docker | 101313 |  | 1 | n/a% | n/a% | n/a s | 27.391 MB | 27.391 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 101333 | base_0000 | 1 | n/a% | n/a% | n/a s | 10.258 MB | 10.258 MB | 1569.195 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 101351 |  | 1 | n/a% | n/a% | n/a s | 26.109 MB | 26.109 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 101395 |  | 1 | n/a% | n/a% | n/a s | 5.277 MB | 5.277 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 101451 | base_0000 | 7 | 1.632% | 9.790% | 0.010 s | 2.244 MB | 12.336 MB | 225.258 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 101413 |  | 1 | n/a% | n/a% | n/a s | 25.488 MB | 25.488 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 101463 | base_0000 | 6 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 101494 | base_0000 | 1 | n/a% | n/a% | n/a s | 10.164 MB | 10.164 MB | 1569.695 MB | 1569.695 MB | n/a MB | n/a MB |
| docker | 101474 |  | 1 | n/a% | n/a% | n/a s | 27.262 MB | 27.262 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| python | 101529 | base_0000 | 5 | 97.771% | 98.064% | 0.400 s | 23.949 MB | 34.871 MB | 30.894 MB | 45.023 MB | n/a MB | n/a MB |
| docker | 101501 |  | 5 | 0.000% | 0.000% | 0.000 s | 27.078 MB | 27.078 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| bash | 101521 | base_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.359 MB | 3.359 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 101540 |  | 1 | n/a% | n/a% | n/a s | 25.824 MB | 25.824 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 101599 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.438 MB | 25.438 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 101640 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.658 MB | 12.734 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 101662 |  | 1 | n/a% | n/a% | n/a s | 27.086 MB | 27.086 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 101652 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 101682 | base_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| docker | 101727 |  | 1 | n/a% | n/a% | n/a s | 15.059 MB | 15.059 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 101762 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.756 MB | 26.902 MB | 1700.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 101829 |  | 1 | n/a% | n/a% | n/a s | 26.418 MB | 26.418 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 101846 |  | 39 | 0.000% | 0.000% | 0.000 s | 26.918 MB | 26.918 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 101879 |  | 1 | n/a% | n/a% | n/a s | 26.598 MB | 26.598 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 101895 |  | 4 | 102.107% | 108.790% | 0.310 s | 25.821 MB | 34.500 MB | 50.001 MB | 57.438 MB | 0.000000 MB | 0.218750 MB |
| docker | 101924 |  | 1 | n/a% | n/a% | n/a s | 25.746 MB | 25.746 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 101946 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.242 MB | 27.426 MB | 1697.025 MB | 1733.027 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 101987 | beam_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 101999 | beam_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 102035 |  | 1 | n/a% | n/a% | n/a s | 20.918 MB | 20.918 MB | 1524.203 MB | 1524.203 MB | n/a MB | n/a MB |
| docker | 102061 |  | 1 | n/a% | n/a% | n/a s | 27.602 MB | 27.602 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 102080 | beam_0000 | 1 | n/a% | n/a% | n/a s | 11.863 MB | 11.863 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 102135 |  | 1 | n/a% | n/a% | n/a s | 25.883 MB | 25.883 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 102196 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.289 MB | 26.867 MB | 1624.488 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 102236 | beam_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.599 MB | 12.496 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 102279 | beam_0000 | 1 | n/a% | n/a% | n/a s | 12.227 MB | 12.227 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 102258 |  | 1 | n/a% | n/a% | n/a s | 27.004 MB | 27.004 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 102248 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 102321 |  | 1 | n/a% | n/a% | n/a s | 3.504 MB | 3.504 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 102359 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.992 MB | 25.992 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 102425 |  | 1 | n/a% | n/a% | n/a s | 11.109 MB | 11.109 MB | 1451.949 MB | 1451.949 MB | n/a MB | n/a MB |
| docker | 102439 |  | 37 | 0.000% | 0.000% | 0.000 s | 26.945 MB | 26.945 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 102455 |  | 1 | n/a% | n/a% | n/a s | 8.715 MB | 8.715 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 102473 |  | 1 | n/a% | n/a% | n/a s | 25.598 MB | 25.598 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 102481 |  | 1 | n/a% | n/a% | n/a s | 26.867 MB | 26.867 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 102521 | beam_0000 | 4 | 6.506% | 19.519% | 0.020 s | 3.531 MB | 12.227 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 102533 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 102563 | beam_0000 | 1 | n/a% | n/a% | n/a s | 3.898 MB | 3.898 MB | 1216.680 MB | 1216.680 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 102560 | beam_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 102544 |  | 1 | n/a% | n/a% | n/a s | 27.352 MB | 27.352 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 102597 |  | 1 | n/a% | n/a% | n/a s | 4.219 MB | 4.219 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 102634 |  | 1 | n/a% | n/a% | n/a s | 26.172 MB | 26.172 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 102642 |  | 1 | n/a% | n/a% | n/a s | 27.035 MB | 27.035 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 102701 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.160 MB | 27.160 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 102741 | beam_0000 | 10 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 102755 | beam_0000 | 9 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 102793 |  | 9 | 1.219% | 9.750% | 0.010 s | 24.339 MB | 27.133 MB | 1479.883 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| bash | 102812 | beam_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.246 MB | 3.246 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 102821 | beam_0000 | 8 | 100.715% | 108.026% | 0.720 s | 31.222 MB | 42.078 MB | 38.198 MB | 51.238 MB | n/a MB | n/a MB |
| docker | 102831 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.895 MB | 26.895 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 102889 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.668 MB | 26.668 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 102929 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 4.667 MB | 12.734 MB | 524.112 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 102983 |  | 1 | n/a% | n/a% | n/a s | 6.520 MB | 6.520 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| tail | 102942 | beam_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 103018 |  | 1 | n/a% | n/a% | n/a s | 27.121 MB | 27.121 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 103054 |  | 1 | n/a% | n/a% | n/a s | 25.973 MB | 25.973 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 103096 |  | 1 | n/a% | n/a% | n/a s | 0.164 MB | 0.164 MB | 30.570 MB | 30.570 MB | n/a MB | n/a MB |
| docker | 103113 |  | 1 | n/a% | n/a% | n/a s | 9.281 MB | 9.281 MB | 1371.691 MB | 1371.691 MB | n/a MB | n/a MB |
| docker | 103138 |  | 1 | n/a% | n/a% | n/a s | 26.730 MB | 26.730 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 103146 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.637 MB | 25.637 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 103178 |  | 1 | n/a% | n/a% | n/a s | 26.500 MB | 26.500 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 103193 |  | 4 | 98.772% | 98.968% | 0.300 s | 25.587 MB | 34.422 MB | 49.670 MB | 57.438 MB | 0.000000 MB | 0.234375 MB |
| docker | 103244 |  | 3 | 4.796% | 9.593% | 0.010 s | 18.297 MB | 27.445 MB | 1213.378 MB | 1804.781 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 103287 | bear_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.721 MB | 12.984 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 103300 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 103338 |  | 1 | n/a% | n/a% | n/a s | 15.738 MB | 15.738 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 103385 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.051 MB | 11.051 MB | 1569.840 MB | 1569.840 MB | n/a MB | n/a MB |
| docker | 103365 |  | 1 | n/a% | n/a% | n/a s | 27.262 MB | 27.262 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| sh | 103421 | bear_0000 | 1 | n/a% | n/a% | n/a s | 1.676 MB | 1.676 MB | 2.617 MB | 2.617 MB | n/a MB | n/a MB |
| docker | 103401 |  | 1 | n/a% | n/a% | n/a s | 27.273 MB | 27.273 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| sh | 103428 | bear_0000 | 1 | n/a% | n/a% | n/a s | 1.676 MB | 1.676 MB | 2.617 MB | 2.617 MB | n/a MB | n/a MB |
| docker | 103438 |  | 1 | n/a% | n/a% | n/a s | 27.066 MB | 27.066 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 103495 |  | 2 | 9.859% | 9.859% | 0.010 s | 21.729 MB | 25.520 MB | 1588.080 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 103535 | bear_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.733 MB | 13.035 MB | 393.473 MB | 1570.727 MB | n/a MB | n/a MB |
| tail | 103547 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 103557 |  | 1 | n/a% | n/a% | n/a s | 27.414 MB | 27.414 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 103577 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.859 MB | 11.859 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 103619 |  | 1 | n/a% | n/a% | n/a s | 17.984 MB | 17.984 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 103658 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.859 MB | 25.859 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 103707 |  | 1 | n/a% | n/a% | n/a s | 0.402 MB | 0.402 MB | 32.750 MB | 32.750 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 103755 | bear_0000 | 3 | 9.729% | 19.458% | 0.020 s | 4.044 MB | 11.008 MB | 523.768 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 103715 |  | 1 | n/a% | n/a% | n/a s | 25.633 MB | 25.633 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 103767 | bear_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.684 MB | 1.684 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 103777 |  | 1 | n/a% | n/a% | n/a s | 27.375 MB | 27.375 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 103804 |  | 1 | n/a% | n/a% | n/a s | 27.141 MB | 27.141 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| bash | 103828 | bear_0000 | 1 | n/a% | n/a% | n/a s | 0.152 MB | 0.152 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| bash | 103823 | bear_0000 | 1 | n/a% | n/a% | n/a s | 3.359 MB | 3.359 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 103845 |  | 1 | n/a% | n/a% | n/a s | 25.723 MB | 25.723 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 103905 |  | 1 | n/a% | n/a% | n/a s | 25.602 MB | 25.602 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker-init | 103945 | bear_0000 | 2 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 103959 |  | 1 | n/a% | n/a% | n/a s | 26.141 MB | 26.141 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| tail | 103957 | bear_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.809 MB | 1.809 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 103993 |  | 1 | n/a% | n/a% | n/a s | 27.676 MB | 27.676 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 104009 | bear_0000 | 1 | n/a% | n/a% | n/a s | 1.961 MB | 1.961 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| runc:[1:CHILD] | 104014 | bear_0000 | 1 | n/a% | n/a% | n/a s | 0.125 MB | 0.125 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| runc:[1:CHILD] | 104013 | bear_0000 | 1 | n/a% | n/a% | n/a s | 1.223 MB | 1.223 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 104037 |  | 1 | n/a% | n/a% | n/a s | 26.793 MB | 26.793 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 104081 |  | 1 | n/a% | n/a% | n/a s | 9.922 MB | 9.922 MB | 1387.949 MB | 1387.949 MB | n/a MB | n/a MB |
| docker | 104098 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.043 MB | 27.043 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 104137 | bear_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.606 MB | 13.160 MB | 411.147 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 104161 |  | 1 | n/a% | n/a% | n/a s | 27.453 MB | 27.453 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 104151 | bear_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 104227 |  | 1 | n/a% | n/a% | n/a s | 26.434 MB | 26.434 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| docker | 104264 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.090 MB | 27.090 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 104334 |  | 1 | n/a% | n/a% | n/a s | 25.656 MB | 25.656 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 104348 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.578 MB | 26.578 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 104373 |  | 1 | n/a% | n/a% | n/a s | 23.008 MB | 23.008 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 104392 |  | 1 | n/a% | n/a% | n/a s | 26.758 MB | 26.758 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 104433 | bear_0000 | 4 | 6.448% | 19.343% | 0.020 s | 1.549 MB | 4.297 MB | 375.089 MB | 1497.191 MB | n/a MB | n/a MB |
| tail | 104446 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 104457 |  | 1 | n/a% | n/a% | n/a s | 17.312 MB | 17.312 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 104503 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.188 MB | 11.188 MB | 1641.965 MB | 1641.965 MB | n/a MB | n/a MB |
| docker | 104483 |  | 1 | n/a% | n/a% | n/a s | 27.402 MB | 27.402 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 104521 |  | 1 | n/a% | n/a% | n/a s | 27.281 MB | 27.281 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 104540 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.992 MB | 11.992 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 104559 |  | 1 | n/a% | n/a% | n/a s | 26.004 MB | 26.004 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 104618 |  | 2 | 0.000% | 0.000% | 0.000 s | 23.094 MB | 25.973 MB | 1624.207 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 104657 | bear_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.726 MB | 12.660 MB | 143.707 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 104669 | bear_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.684 MB | 1.684 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 104699 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.770 MB | 11.770 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 104679 |  | 1 | n/a% | n/a% | n/a s | 27.023 MB | 27.023 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 104708 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.449 MB | 27.559 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| bash | 104728 | bear_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.328 MB | 3.328 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 104738 | bear_0000 | 8 | 100.699% | 107.924% | 0.720 s | 30.817 MB | 41.973 MB | 38.039 MB | 51.340 MB | n/a MB | n/a MB |
| docker | 104748 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.354 MB | 26.766 MB | 1628.492 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 104819 |  | 1 | n/a% | n/a% | n/a s | 23.000 MB | 23.000 MB | 1524.203 MB | 1524.203 MB | n/a MB | n/a MB |
| docker | 104835 |  | 39 | 0.000% | 0.000% | 0.000 s | 26.348 MB | 26.348 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 104868 |  | 1 | n/a% | n/a% | n/a s | 25.699 MB | 25.699 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| python3 | 104883 |  | 4 | 98.780% | 108.842% | 0.300 s | 26.160 MB | 34.523 MB | 50.343 MB | 57.434 MB | 0.000000 MB | 0.234375 MB |
| docker | 104888 |  | 1 | n/a% | n/a% | n/a s | 19.367 MB | 19.367 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 104912 |  | 1 | n/a% | n/a% | n/a s | 25.453 MB | 25.453 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 104920 |  | 1 | n/a% | n/a% | n/a s | 15.582 MB | 15.582 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 104934 |  | 2 | 19.527% | 19.527% | 0.020 s | 27.119 MB | 27.363 MB | 1696.775 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 104973 | beef_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.566 MB | 12.367 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 105009 |  | 1 | n/a% | n/a% | n/a s | 11.461 MB | 11.461 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 104989 |  | 1 | n/a% | n/a% | n/a s | 27.449 MB | 27.449 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 104987 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.809 MB | 1.809 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 105055 |  | 1 | n/a% | n/a% | n/a s | 1.613 MB | 1.613 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 105093 |  | 1 | n/a% | n/a% | n/a s | 26.582 MB | 26.582 MB | 1668.277 MB | 1668.277 MB | n/a MB | n/a MB |
| docker | 105131 |  | 1 | n/a% | n/a% | n/a s | 26.047 MB | 26.047 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 105175 |  | 1 | n/a% | n/a% | n/a s | 17.988 MB | 17.988 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 105231 | beef_0000 | 4 | 6.379% | 19.137% | 0.020 s | 1.574 MB | 4.398 MB | 325.025 MB | 1296.938 MB | n/a MB | n/a MB |
| docker | 105191 |  | 1 | n/a% | n/a% | n/a s | 25.527 MB | 25.527 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 105242 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 105252 |  | 1 | n/a% | n/a% | n/a s | 23.461 MB | 23.461 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 105280 |  | 1 | n/a% | n/a% | n/a s | 27.141 MB | 27.141 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 105300 | beef_0000 | 1 | n/a% | n/a% | n/a s | 12.000 MB | 12.000 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 105352 |  | 1 | n/a% | n/a% | n/a s | 26.832 MB | 26.832 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 105405 |  | 1 | n/a% | n/a% | n/a s | 3.449 MB | 3.449 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 105435 |  | 52 | 0.000% | 0.000% | 0.000 s | 26.543 MB | 26.543 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 105451 |  | 1 | n/a% | n/a% | n/a s | 25.574 MB | 25.574 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 105477 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.883 MB | 25.883 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| tail | 105527 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.408 MB | 1.703 MB | 2.803 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 105515 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 105566 |  | 1 | n/a% | n/a% | n/a s | 3.848 MB | 3.848 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 105602 |  | 1 | n/a% | n/a% | n/a s | 27.387 MB | 27.387 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 105642 |  | 1 | n/a% | n/a% | n/a s | 26.883 MB | 26.883 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 105683 |  | 1 | n/a% | n/a% | n/a s | 14.898 MB | 14.898 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 105700 |  | 1 | n/a% | n/a% | n/a s | 26.664 MB | 26.664 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| tail | 105752 | beef_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.809 MB | 1.809 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 105754 |  | 1 | n/a% | n/a% | n/a s | 25.691 MB | 25.691 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker-init | 105738 | beef_0000 | 10 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 105810 | beef_0000 | 9 | 2.428% | 19.422% | 0.020 s | 3.980 MB | 8.539 MB | 178.258 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 105791 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.477 MB | 27.477 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 105819 | beef_0000 | 8 | 100.740% | 107.616% | 0.720 s | 31.793 MB | 41.777 MB | 38.712 MB | 51.238 MB | n/a MB | n/a MB |
| docker | 105829 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.840 MB | 26.840 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 105890 |  | 2 | 0.000% | 0.000% | 0.000 s | 15.859 MB | 25.500 MB | 846.486 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 105929 | beef_0000 | 4 | 3.255% | 9.765% | 0.010 s | 3.712 MB | 12.949 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 105973 | beef_0000 | 1 | n/a% | n/a% | n/a s | 11.344 MB | 11.344 MB | 1570.098 MB | 1570.098 MB | n/a MB | n/a MB |
| docker | 105953 |  | 1 | n/a% | n/a% | n/a s | 27.273 MB | 27.273 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 105943 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 106006 |  | 1 | n/a% | n/a% | n/a s | 22.996 MB | 22.996 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 106052 |  | 2 | 9.759% | 9.759% | 0.010 s | 17.529 MB | 25.941 MB | 1443.822 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 106114 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 106140 |  | 1 | n/a% | n/a% | n/a s | 25.891 MB | 25.891 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 106148 |  | 38 | 0.000% | 0.000% | 0.000 s | 25.645 MB | 25.645 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 106164 |  | 1 | n/a% | n/a% | n/a s | 9.277 MB | 9.277 MB | 1315.945 MB | 1315.945 MB | n/a MB | n/a MB |
| docker | 106180 |  | 1 | n/a% | n/a% | n/a s | 26.957 MB | 26.957 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 106195 |  | 4 | 98.761% | 108.732% | 0.300 s | 26.986 MB | 34.691 MB | 51.015 MB | 57.438 MB | 0.000000 MB | 0.234375 MB |
| docker | 106200 |  | 1 | n/a% | n/a% | n/a s | 18.238 MB | 18.238 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 106224 |  | 1 | n/a% | n/a% | n/a s | 26.898 MB | 26.898 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 106247 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.045 MB | 27.340 MB | 1697.025 MB | 1733.027 MB | 0.000000 MB | 0.000000 MB |
| docker | 106300 |  | 1 | n/a% | n/a% | n/a s | 19.105 MB | 19.105 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker-init | 106286 | bell_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 106298 | bell_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 106337 |  | 1 | n/a% | n/a% | n/a s | 26.848 MB | 26.848 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 106363 |  | 1 | n/a% | n/a% | n/a s | 27.145 MB | 27.145 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 106431 |  | 1 | n/a% | n/a% | n/a s | 22.652 MB | 22.652 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 106440 |  | 1 | n/a% | n/a% | n/a s | 25.883 MB | 25.883 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 106497 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.762 MB | 26.762 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| tail | 106549 | bell_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 106537 | bell_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 106587 |  | 1 | n/a% | n/a% | n/a s | 9.285 MB | 9.285 MB | 1235.438 MB | 1235.438 MB | n/a MB | n/a MB |
| docker | 106622 |  | 1 | n/a% | n/a% | n/a s | 26.816 MB | 26.816 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 106658 |  | 1 | n/a% | n/a% | n/a s | 25.824 MB | 25.824 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 106701 |  | 1 | n/a% | n/a% | n/a s | 23.445 MB | 23.445 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 106726 |  | 1 | n/a% | n/a% | n/a s | 17.309 MB | 17.309 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 106740 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.457 MB | 26.457 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 106783 |  | 2 | 0.000% | 0.000% | 0.000 s | 22.846 MB | 25.715 MB | 1588.205 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 106823 | bell_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.803 MB | 13.312 MB | 411.411 MB | 1642.480 MB | n/a MB | n/a MB |
| tail | 106837 | bell_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 106868 | bell_0000 | 1 | n/a% | n/a% | n/a s | 11.918 MB | 11.918 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 106848 |  | 1 | n/a% | n/a% | n/a s | 27.391 MB | 27.391 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 106913 |  | 1 | n/a% | n/a% | n/a s | 0.945 MB | 0.945 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 106951 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.137 MB | 26.137 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 107009 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.645 MB | 25.645 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 107050 | bell_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.882 MB | 13.121 MB | 158.022 MB | 1570.727 MB | n/a MB | n/a MB |
| tail | 107062 | bell_0000 | 9 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| bash | 107118 | bell_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.324 MB | 3.324 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 107127 | bell_0000 | 8 | 99.321% | 107.904% | 0.710 s | 31.181 MB | 42.090 MB | 38.189 MB | 51.238 MB | n/a MB | n/a MB |
| docker | 107098 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.191 MB | 27.191 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 107137 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.898 MB | 26.898 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 107190 |  | 1 | n/a% | n/a% | n/a s | 27.008 MB | 27.008 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 107232 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.169 MB | 25.789 MB | 1618.481 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 107248 |  | 1 | n/a% | n/a% | n/a s | 2.773 MB | 2.773 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 107273 |  | 1 | n/a% | n/a% | n/a s | 5.016 MB | 5.016 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| python3 | 107280 |  | 4 | 102.034% | 108.824% | 0.310 s | 28.171 MB | 34.664 MB | 51.818 MB | 57.438 MB | 0.000000 MB | 0.234375 MB |
| docker | 107307 |  | 1 | n/a% | n/a% | n/a s | 16.441 MB | 16.441 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |

## GPU metrics

_No GPU samples were collected._

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| alex_0000 | 61.468% | 100.837% | 1.255 s | 8.967 MB | 35.605 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| andy_0000 | 56.533% | 101.139% | 1.444 s | 7.936 MB | 35.156 MB | 0.000000 MB | 0.003906 MB | 3548.441824 MB | 31.344033 MB |
| arch_0000 | 66.392% | 100.137% | 1.222 s | 11.477 MB | 35.430 MB | 0.000000 MB | 0.003906 MB | 3548.530525 MB | 31.434441 MB |
| bake_0000 | 56.313% | 100.081% | 1.326 s | 8.620 MB | 34.602 MB | 0.015625 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bale_0000 | 79.552% | 100.949% | 4.163 s | 21.234 MB | 35.512 MB | 0.000000 MB | 0.003906 MB | 3549.672672 MB | 32.024363 MB |
| band_0000 | 58.577% | 100.035% | 1.320 s | 9.601 MB | 34.453 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bart_0000 | 63.085% | 100.142% | 1.161 s | 10.221 MB | 35.535 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| base_0000 | 60.273% | 100.085% | 2.039 s | 8.499 MB | 34.277 MB | 0.000000 MB | 0.007812 MB | 0.000000 MB | 0.000000 MB |
| beam_0000 | 60.387% | 100.987% | 1.237 s | 9.700 MB | 35.355 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bear_0000 | 57.845% | 100.100% | 1.366 s | 8.475 MB | 35.641 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| beef_0000 | 61.589% | 100.965% | 1.199 s | 9.738 MB | 35.254 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bell_0000 | 65.821% | 100.156% | 1.078 s | 11.127 MB | 35.328 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |

## Incomplete spans

_No spans were still open when profiling stopped._

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sync:result_wait | 24/24 | 0 | 0 | 708.404 | 0.005 | 708.395 | 29516.838 | 23683.643 | 58140.213 |
| turn | 85/85 | 0 | 0 | 608.107 | 2.784 | 605.250 | 7154.198 | 4067.278 | 23611.435 |
| llm:attempt | 85/85 | 0 | 0 | 551.652 | 2.245 | 549.364 | 6490.023 | 3000.531 | 23118.791 |
| run:diagnose_bug | 12/12 | 0 | 0 | 388.492 | 1.434 | 387.006 | 32374.368 | 30052.726 | 48937.112 |
| run:repair_bug | 12/12 | 0 | 0 | 319.921 | 1.480 | 318.418 | 26660.095 | 19850.294 | 59048.711 |
| llm:diagnose_bug | 31/31 | 0 | 0 | 318.951 | 1.153 | 317.759 | 10288.749 | 4275.500 | 25120.102 |
| llm:repair_bug | 54/54 | 0 | 0 | 232.725 | 1.116 | 231.605 | 4309.721 | 2941.326 | 8046.933 |
| capstone:build:find_first_in_sorted | 1/1 | 0 | 0 | 101.680 | 0.000 | 101.679 | 101679.779 | 101679.779 | 101679.779 |
| teardown:commit | 24/24 | 0 | 0 | 100.124 | 0.059 | 100.063 | 4171.836 | 4113.884 | 4935.673 |
| sandbox:commit | 24/24 | 0 | 0 | 99.632 | 0.046 | 99.583 | 4151.321 | 4093.795 | 4916.577 |
| capstone:plan:find_first_in_sorted | 1/1 | 0 | 0 | 61.592 | 0.001 | 61.591 | 61592.057 | 61592.057 | 61592.057 |
| capstone:plan:flatten | 1/1 | 0 | 0 | 38.585 | 0.001 | 38.584 | 38584.696 | 38584.696 | 38584.696 |
| tool_dispatch:repair_bug | 54/54 | 0 | 0 | 36.135 | 0.274 | 35.844 | 669.169 | 587.719 | 1349.517 |
| capstone:plan:mergesort | 1/1 | 0 | 0 | 34.174 | 0.001 | 34.173 | 34173.659 | 34173.659 | 34173.659 |
| capstone:plan:rpn_eval | 1/1 | 0 | 0 | 34.118 | 0.001 | 34.117 | 34118.011 | 34118.011 | 34118.011 |
| capstone:plan:hanoi | 1/1 | 0 | 0 | 33.460 | 0.001 | 33.459 | 33459.857 | 33459.857 | 33459.857 |
| capstone:plan:next_palindrome | 1/1 | 0 | 0 | 30.628 | 0.001 | 30.628 | 30628.231 | 30628.231 | 30628.231 |
| capstone:plan:gcd | 1/1 | 0 | 0 | 29.478 | 0.001 | 29.477 | 29477.755 | 29477.755 | 29477.755 |
| capstone:plan:bitcount | 1/1 | 0 | 0 | 29.221 | 0.001 | 29.220 | 29221.466 | 29221.466 | 29221.466 |
| capstone:plan:powerset | 1/1 | 0 | 0 | 29.204 | 0.001 | 29.203 | 29203.859 | 29203.859 | 29203.859 |
| capstone:build:levenshtein | 1/1 | 0 | 0 | 24.169 | 0.001 | 24.168 | 24168.879 | 24168.879 | 24168.879 |
| capstone:plan:bucketsort | 1/1 | 0 | 0 | 23.947 | 0.001 | 23.947 | 23947.419 | 23947.419 | 23947.419 |
| capstone:plan:levenshtein | 1/1 | 0 | 0 | 23.421 | 0.001 | 23.420 | 23421.166 | 23421.166 | 23421.166 |
| capstone:build:mergesort | 1/1 | 0 | 0 | 23.175 | 0.000 | 23.174 | 23174.913 | 23174.913 | 23174.913 |
| capstone:build:hanoi | 1/1 | 0 | 0 | 22.438 | 0.001 | 22.438 | 22438.052 | 22438.052 | 22438.052 |
| capstone:build:powerset | 1/1 | 0 | 0 | 22.209 | 0.001 | 22.208 | 22209.283 | 22209.283 | 22209.283 |
| capstone:build:rpn_eval | 1/1 | 0 | 0 | 21.321 | 0.001 | 21.321 | 21321.342 | 21321.342 | 21321.342 |
| capstone:plan:is_valid_parenthesization | 1/1 | 0 | 0 | 20.667 | 0.001 | 20.667 | 20667.458 | 20667.458 | 20667.458 |
| tool_dispatch:diagnose_bug | 31/31 | 0 | 0 | 20.245 | 0.191 | 20.042 | 653.069 | 515.218 | 1335.405 |
| sandbox:exec | 19/19 | 0 | 0 | 19.632 | 0.046 | 19.581 | 1033.248 | 1128.076 | 1452.358 |
| sandbox:start | 69/69 | 0 | 0 | 19.283 | 0.148 | 19.126 | 279.469 | 238.646 | 426.094 |
| capstone:build:is_valid_parenthesization | 1/1 | 0 | 0 | 18.379 | 0.001 | 18.379 | 18379.385 | 18379.385 | 18379.385 |
| tool:bash | 15/15 | 0 | 0 | 18.312 | 0.046 | 18.261 | 1220.789 | 1141.007 | 1993.310 |
| capstone:build:flatten | 1/1 | 0 | 0 | 18.231 | 0.000 | 18.231 | 18231.012 | 18231.012 | 18231.012 |
| capstone:build:bucketsort | 1/1 | 0 | 0 | 17.686 | 0.001 | 17.686 | 17686.470 | 17686.470 | 17686.470 |
| capstone:build:gcd | 1/1 | 0 | 0 | 17.508 | 0.001 | 17.506 | 17507.975 | 17507.975 | 17507.975 |
| tool:read | 37/37 | 0 | 0 | 17.376 | 0.155 | 17.205 | 469.633 | 412.563 | 587.714 |
| capstone:build:bitcount | 1/1 | 0 | 0 | 17.301 | 0.000 | 17.300 | 17300.681 | 17300.681 | 17300.681 |
| capstone:build:next_palindrome | 1/1 | 0 | 0 | 15.824 | 0.000 | 15.822 | 15824.342 | 15824.342 | 15824.342 |
| sandbox:stop | 133/133 | 0 | 0 | 13.603 | 0.110 | 13.489 | 102.277 | 160.610 | 186.638 |
| capstone:prepare:bitcount | 1/1 | 0 | 0 | 10.161 | 0.045 | 10.116 | 10161.122 | 10161.122 | 10161.122 |
| capstone:prepare:find_first_in_sorted | 1/1 | 0 | 0 | 10.043 | 0.030 | 10.012 | 10042.771 | 10042.771 | 10042.771 |
| capstone:prepare:mergesort | 1/1 | 0 | 0 | 8.357 | 0.041 | 8.315 | 8356.581 | 8356.581 | 8356.581 |
| sandbox:read_file | 50/50 | 0 | 0 | 8.174 | 0.113 | 8.049 | 163.488 | 89.400 | 335.001 |
| tool:edit | 13/13 | 0 | 0 | 6.192 | 0.097 | 6.090 | 476.335 | 418.913 | 738.642 |
| capstone:scheduler:tick | 720/720 | 0 | 0 | 2.928 | 0.742 | 2.180 | 4.067 | 0.189 | 0.357 |
| agent:create | 12/12 | 0 | 0 | 2.742 | 0.573 | 2.169 | 228.530 | 138.074 | 661.754 |
| capstone:prepare:levenshtein | 1/1 | 0 | 0 | 2.662 | 0.042 | 2.619 | 2661.567 | 2661.567 | 2661.567 |
| capstone:verify:levenshtein | 1/1 | 0 | 0 | 2.451 | 0.001 | 2.450 | 2451.258 | 2451.258 | 2451.258 |
| sandbox:destroy | 12/12 | 0 | 0 | 1.428 | 0.020 | 1.408 | 119.018 | 118.124 | 123.850 |
| sandbox:write_file | 13/13 | 0 | 0 | 1.272 | 0.014 | 1.258 | 97.882 | 90.620 | 130.912 |
| tool:glob | 3/3 | 0 | 0 | 0.999 | 0.009 | 0.989 | 332.838 | 330.028 | 339.668 |
| capstone:prepare:gcd | 1/1 | 0 | 0 | 0.483 | 0.030 | 0.453 | 483.437 | 483.437 | 483.437 |
| capstone:prepare:bucketsort | 1/1 | 0 | 0 | 0.460 | 0.030 | 0.429 | 459.569 | 459.569 | 459.569 |
| capstone:prepare:next_palindrome | 1/1 | 0 | 0 | 0.457 | 0.032 | 0.424 | 456.885 | 456.885 | 456.885 |
| capstone:prepare:is_valid_parenthesization | 1/1 | 0 | 0 | 0.448 | 0.031 | 0.415 | 447.584 | 447.584 | 447.584 |
| capstone:prepare:hanoi | 1/1 | 0 | 0 | 0.446 | 0.031 | 0.415 | 445.637 | 445.637 | 445.637 |
| capstone:prepare:rpn_eval | 1/1 | 0 | 0 | 0.444 | 0.030 | 0.412 | 443.779 | 443.779 | 443.779 |
| capstone:prepare:flatten | 1/1 | 0 | 0 | 0.437 | 0.031 | 0.406 | 436.582 | 436.582 | 436.582 |
| capstone:prepare:powerset | 1/1 | 0 | 0 | 0.436 | 0.030 | 0.406 | 436.325 | 436.325 | 436.325 |
| capstone:verify:mergesort | 1/1 | 0 | 0 | 0.399 | 0.001 | 0.397 | 398.802 | 398.802 | 398.802 |
| capstone:verify:bitcount | 1/1 | 0 | 0 | 0.398 | 0.001 | 0.396 | 397.606 | 397.606 | 397.606 |
| capstone:verify:gcd | 1/1 | 0 | 0 | 0.392 | 0.001 | 0.390 | 391.597 | 391.597 | 391.597 |
| capstone:verify:hanoi | 1/1 | 0 | 0 | 0.391 | 0.001 | 0.390 | 390.968 | 390.968 | 390.968 |
| capstone:verify:flatten | 1/1 | 0 | 0 | 0.388 | 0.001 | 0.387 | 388.382 | 388.382 | 388.382 |
| capstone:verify:find_first_in_sorted | 1/1 | 0 | 0 | 0.385 | 0.001 | 0.384 | 385.139 | 385.139 | 385.139 |
| capstone:verify:next_palindrome | 1/1 | 0 | 0 | 0.384 | 0.001 | 0.383 | 383.679 | 383.679 | 383.679 |
| capstone:verify:rpn_eval | 1/1 | 0 | 0 | 0.379 | 0.001 | 0.378 | 379.311 | 379.311 | 379.311 |
| capstone:verify:is_valid_parenthesization | 1/1 | 0 | 0 | 0.378 | 0.001 | 0.377 | 378.039 | 378.039 | 378.039 |
| capstone:verify:powerset | 1/1 | 0 | 0 | 0.376 | 0.001 | 0.375 | 376.493 | 376.493 | 376.493 |
| capstone:verify:bucketsort | 1/1 | 0 | 0 | 0.374 | 0.001 | 0.372 | 373.676 | 373.676 | 373.676 |
| tool:grep | 1/1 | 0 | 0 | 0.333 | 0.003 | 0.330 | 333.079 | 333.079 | 333.079 |
| sync:container | 896/896 | 0 | 0 | 0.108 | 0.105 | 0.002 | 0.120 | 0.131 | 0.203 |
| sandbox:provision | 12/12 | 0 | 0 | 0.096 | 0.009 | 0.087 | 8.038 | 0.428 | 41.654 |
| sandbox:create | 12/12 | 0 | 0 | 0.094 | 0.006 | 0.087 | 7.811 | 0.303 | 40.871 |
| run:detect | 1/1 | 0 | 0 | 0.039 | 0.001 | 0.038 | 39.022 | 39.022 | 39.022 |
| prune | 24/24 | 0 | 0 | 0.007 | 0.004 | 0.003 | 0.294 | 0.276 | 0.392 |
| tool:return_summary | 16/16 | 4 | 0 | 0.006 | 0.006 | 0.000 | 0.355 | 0.351 | 0.456 |
| tool:return_plan | 12/12 | 0 | 0 | 0.004 | 0.004 | 0.000 | 0.352 | 0.325 | 0.500 |
| tool:return_status | 12/12 | 0 | 0 | 0.004 | 0.004 | 0.000 | 0.316 | 0.289 | 0.463 |
| llm:sync | 85/85 | 0 | 0 | 0.004 | 0.004 | 0.000 | 0.043 | 0.037 | 0.072 |
| agsync:join | 12/12 | 0 | 0 | 0.003 | 0.003 | 0.000 | 0.254 | 0.252 | 0.331 |
| input:prepare | 24/24 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.093 | 0.088 | 0.124 |
| resolve | 24/24 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.082 | 0.064 | 0.189 |
| proc_wait | 24/24 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.070 | 0.068 | 0.078 |
| agprof:clock_sync | 1/1 | 0 | 0 | 0.001 | 0.001 | 0.000 | 1.060 | 1.060 | 1.060 |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 7115 | 20.867 | 0.000 | 159.483 | 9.759 | 150.706013 CPU seconds | n/a |
| docker (PID 100002) rss_mb | MB | 1 | 27.340 | 27.340 | 27.340 | 27.340 | n/a | n/a |
| docker (PID 100002) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 100022) rss_mb | MB | 1 | 11.984 | 11.984 | 11.984 | 11.984 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 100022) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 100040) rss_mb | MB | 1 | 25.969 | 25.969 | 25.969 | 25.969 | n/a | n/a |
| docker (PID 100040) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 100092) rss_mb | MB | 1 | 26.188 | 26.188 | 26.188 | 26.188 | n/a | n/a |
| docker (PID 100092) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 100100) rss_mb | MB | 1 | 25.570 | 25.570 | 25.570 | 25.570 | n/a | n/a |
| docker (PID 100100) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 100140) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 100140) rss_mb | MB | 4 | 3.582 | 0.633 | 12.430 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 100140) vms_mb | MB | 4 | 411.411 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 100154) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 100154) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [base_0000] (PID 100154) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 100165) rss_mb | MB | 1 | 27.016 | 27.016 | 27.016 | 27.016 | n/a | n/a |
| docker (PID 100165) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 100184) rss_mb | MB | 1 | 11.133 | 11.133 | 11.133 | 11.133 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 100184) vms_mb | MB | 1 | 1641.836 | 1641.836 | 1641.836 | 1641.836 | n/a | n/a |
| docker (PID 100219) rss_mb | MB | 1 | 16.180 | 16.180 | 16.180 | 16.180 | n/a | n/a |
| docker (PID 100219) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 100257) rss_mb | MB | 1 | 26.348 | 26.348 | 26.348 | 26.348 | n/a | n/a |
| docker (PID 100257) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 100265) rss_mb | MB | 1 | 27.055 | 27.055 | 27.055 | 27.055 | n/a | n/a |
| docker (PID 100265) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 100350) CPU | percent | 38 | 0.515 | 0.000 | 19.562 | 0.000 | 0.020000 CPU seconds | n/a |
| docker (PID 100350) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 100350) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 100350) rss_mb | MB | 39 | 26.082 | 7.219 | 26.578 | 26.578 | n/a | n/a |
| docker (PID 100350) vms_mb | MB | 39 | 1619.032 | 32.867 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 100374) rss_mb | MB | 1 | 21.676 | 21.676 | 21.676 | 21.676 | n/a | n/a |
| docker (PID 100374) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 100393) rss_mb | MB | 1 | 27.230 | 27.230 | 27.230 | 27.230 | n/a | n/a |
| docker (PID 100393) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [base_0000] (PID 100432) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [base_0000] (PID 100432) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [base_0000] (PID 100432) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 100444) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 100444) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [base_0000] (PID 100444) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 100446) rss_mb | MB | 1 | 12.180 | 12.180 | 12.180 | 12.180 | n/a | n/a |
| docker (PID 100446) vms_mb | MB | 1 | 1451.699 | 1451.699 | 1451.699 | 1451.699 | n/a | n/a |
| docker (PID 100482) rss_mb | MB | 1 | 26.906 | 26.906 | 26.906 | 26.906 | n/a | n/a |
| docker (PID 100482) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 100520) rss_mb | MB | 1 | 27.453 | 27.453 | 27.453 | 27.453 | n/a | n/a |
| docker (PID 100520) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 100540) rss_mb | MB | 1 | 8.930 | 8.930 | 8.930 | 8.930 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 100540) vms_mb | MB | 1 | 1496.941 | 1496.941 | 1496.941 | 1496.941 | n/a | n/a |
| docker (PID 100557) rss_mb | MB | 1 | 26.969 | 26.969 | 26.969 | 26.969 | n/a | n/a |
| docker (PID 100557) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 100600) rss_mb | MB | 1 | 3.156 | 3.156 | 3.156 | 3.156 | n/a | n/a |
| docker (PID 100600) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 100619) rss_mb | MB | 1 | 27.160 | 27.160 | 27.160 | 27.160 | n/a | n/a |
| docker (PID 100619) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [base_0000] (PID 100658) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [base_0000] (PID 100658) rss_mb | MB | 11 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [base_0000] (PID 100658) vms_mb | MB | 11 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 100671) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 100671) rss_mb | MB | 11 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [base_0000] (PID 100671) vms_mb | MB | 11 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 100708) CPU | percent | 8 | 1.225 | 0.000 | 9.798 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 100708) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 100708) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 100708) rss_mb | MB | 9 | 25.867 | 15.457 | 27.168 | 27.168 | n/a | n/a |
| docker (PID 100708) vms_mb | MB | 9 | 1644.682 | 1515.949 | 1660.773 | 1660.773 | n/a | n/a |
| bash [base_0000] (PID 100728) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [base_0000] (PID 100728) rss_mb | MB | 8 | 3.418 | 3.418 | 3.418 | 3.418 | n/a | n/a |
| bash [base_0000] (PID 100728) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [base_0000] (PID 100737) CPU | percent | 7 | 100.754 | 97.980 | 107.828 | 98.066 | 0.720000 CPU seconds | n/a |
| python [base_0000] (PID 100737) rss_mb | MB | 8 | 31.487 | 12.730 | 40.562 | 40.562 | n/a | n/a |
| python [base_0000] (PID 100737) vms_mb | MB | 8 | 38.518 | 16.414 | 50.027 | 50.027 | n/a | n/a |
| docker (PID 100747) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 100747) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 100747) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 100747) rss_mb | MB | 2 | 26.828 | 26.766 | 26.891 | 26.891 | n/a | n/a |
| docker (PID 100747) vms_mb | MB | 2 | 1660.648 | 1660.523 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 100807) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 100807) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 100807) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 100807) rss_mb | MB | 2 | 26.629 | 26.629 | 26.629 | 26.629 | n/a | n/a |
| docker (PID 100807) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 100848) CPU | percent | 2 | 4.855 | 0.000 | 9.711 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 100848) rss_mb | MB | 3 | 0.422 | 0.000 | 0.633 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 100848) vms_mb | MB | 3 | 0.704 | 0.004 | 1.055 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 100859) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 100859) rss_mb | MB | 2 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [base_0000] (PID 100859) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 100898) rss_mb | MB | 1 | 11.152 | 11.152 | 11.152 | 11.152 | n/a | n/a |
| docker (PID 100898) vms_mb | MB | 1 | 1451.699 | 1451.699 | 1451.699 | 1451.699 | n/a | n/a |
| docker (PID 100938) rss_mb | MB | 1 | 27.180 | 27.180 | 27.180 | 27.180 | n/a | n/a |
| docker (PID 100938) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 100988) rss_mb | MB | 1 | 15.340 | 15.340 | 15.340 | 15.340 | n/a | n/a |
| docker (PID 100988) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 100996) CPU | percent | 3 | 16.282 | 0.000 | 48.847 | 0.000 | 0.050000 CPU seconds | n/a |
| docker (PID 100996) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 100996) io write MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 100996) rss_mb | MB | 4 | 24.249 | 15.574 | 27.141 | 27.141 | n/a | n/a |
| docker (PID 100996) vms_mb | MB | 4 | 1624.567 | 1515.949 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 101034) CPU | percent | 4 | 7.311 | 0.000 | 29.243 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 101034) rss_mb | MB | 5 | 2.598 | 0.633 | 10.457 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 101034) vms_mb | MB | 5 | 329.134 | 1.055 | 1641.449 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 101048) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 101048) rss_mb | MB | 4 | 1.672 | 1.672 | 1.672 | 1.672 | n/a | n/a |
| tail [base_0000] (PID 101048) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 101058) rss_mb | MB | 1 | 27.324 | 27.324 | 27.324 | 27.324 | n/a | n/a |
| docker (PID 101058) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 101085) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 101085) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 101085) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 101085) rss_mb | MB | 2 | 27.281 | 27.281 | 27.281 | 27.281 | n/a | n/a |
| docker (PID 101085) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 101104) CPU | percent | 1 | 28.893 | 28.893 | 28.893 | 28.893 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 101104) rss_mb | MB | 2 | 3.053 | 2.691 | 3.414 | 3.414 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 101104) vms_mb | MB | 2 | 606.502 | 4.391 | 1208.613 | 4.391 | n/a | n/a |
| python [base_0000] (PID 101113) rss_mb | MB | 1 | 10.898 | 10.898 | 10.898 | 10.898 | n/a | n/a |
| python [base_0000] (PID 101113) vms_mb | MB | 1 | 14.805 | 14.805 | 14.805 | 14.805 | n/a | n/a |
| docker (PID 101123) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 101123) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 101123) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 101123) rss_mb | MB | 2 | 26.574 | 26.574 | 26.574 | 26.574 | n/a | n/a |
| docker (PID 101123) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 101186) rss_mb | MB | 1 | 26.973 | 26.973 | 26.973 | 26.973 | n/a | n/a |
| docker (PID 101186) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [base_0000] (PID 101225) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [base_0000] (PID 101225) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [base_0000] (PID 101225) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 101238) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 101238) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [base_0000] (PID 101238) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 101275) rss_mb | MB | 1 | 26.902 | 26.902 | 26.902 | 26.902 | n/a | n/a |
| docker (PID 101275) vms_mb | MB | 1 | 1588.520 | 1588.520 | 1588.520 | 1588.520 | n/a | n/a |
| docker (PID 101313) rss_mb | MB | 1 | 27.391 | 27.391 | 27.391 | 27.391 | n/a | n/a |
| docker (PID 101313) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 101333) rss_mb | MB | 1 | 10.258 | 10.258 | 10.258 | 10.258 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 101333) vms_mb | MB | 1 | 1569.195 | 1569.195 | 1569.195 | 1569.195 | n/a | n/a |
| docker (PID 101351) rss_mb | MB | 1 | 26.109 | 26.109 | 26.109 | 26.109 | n/a | n/a |
| docker (PID 101351) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 101395) rss_mb | MB | 1 | 5.277 | 5.277 | 5.277 | 5.277 | n/a | n/a |
| docker (PID 101395) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 101413) rss_mb | MB | 1 | 25.488 | 25.488 | 25.488 | 25.488 | n/a | n/a |
| docker (PID 101413) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 101451) CPU | percent | 6 | 1.632 | 0.000 | 9.790 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 101451) rss_mb | MB | 7 | 2.244 | 0.562 | 12.336 | 0.562 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 101451) vms_mb | MB | 7 | 225.258 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 101463) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 101463) rss_mb | MB | 6 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [base_0000] (PID 101463) vms_mb | MB | 6 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 101474) rss_mb | MB | 1 | 27.262 | 27.262 | 27.262 | 27.262 | n/a | n/a |
| docker (PID 101474) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 101494) rss_mb | MB | 1 | 10.164 | 10.164 | 10.164 | 10.164 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 101494) vms_mb | MB | 1 | 1569.695 | 1569.695 | 1569.695 | 1569.695 | n/a | n/a |
| docker (PID 101501) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 101501) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 101501) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 101501) rss_mb | MB | 5 | 27.078 | 27.078 | 27.078 | 27.078 | n/a | n/a |
| docker (PID 101501) vms_mb | MB | 5 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [base_0000] (PID 101521) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [base_0000] (PID 101521) rss_mb | MB | 5 | 3.359 | 3.359 | 3.359 | 3.359 | n/a | n/a |
| bash [base_0000] (PID 101521) vms_mb | MB | 5 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [base_0000] (PID 101529) CPU | percent | 4 | 97.771 | 97.151 | 98.064 | 97.969 | 0.400000 CPU seconds | n/a |
| python [base_0000] (PID 101529) rss_mb | MB | 5 | 23.949 | 6.168 | 34.871 | 34.871 | n/a | n/a |
| python [base_0000] (PID 101529) vms_mb | MB | 5 | 30.894 | 11.809 | 45.023 | 45.023 | n/a | n/a |
| docker (PID 101540) rss_mb | MB | 1 | 25.824 | 25.824 | 25.824 | 25.824 | n/a | n/a |
| docker (PID 101540) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 101599) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 101599) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 101599) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 101599) rss_mb | MB | 2 | 25.438 | 25.438 | 25.438 | 25.438 | n/a | n/a |
| docker (PID 101599) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 101640) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 101640) rss_mb | MB | 4 | 3.658 | 0.633 | 12.734 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 101640) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 101652) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 101652) rss_mb | MB | 3 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [base_0000] (PID 101652) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 101662) rss_mb | MB | 1 | 27.086 | 27.086 | 27.086 | 27.086 | n/a | n/a |
| docker (PID 101662) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 101682) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 101682) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| docker (PID 101727) rss_mb | MB | 1 | 15.059 | 15.059 | 15.059 | 15.059 | n/a | n/a |
| docker (PID 101727) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 101762) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 101762) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 101762) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 101762) rss_mb | MB | 2 | 26.756 | 26.609 | 26.902 | 26.902 | n/a | n/a |
| docker (PID 101762) vms_mb | MB | 2 | 1700.777 | 1668.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 101829) rss_mb | MB | 1 | 26.418 | 26.418 | 26.418 | 26.418 | n/a | n/a |
| docker (PID 101829) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 101846) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 101846) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 101846) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 101846) rss_mb | MB | 39 | 26.918 | 26.918 | 26.918 | 26.918 | n/a | n/a |
| docker (PID 101846) vms_mb | MB | 39 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 101879) rss_mb | MB | 1 | 26.598 | 26.598 | 26.598 | 26.598 | n/a | n/a |
| docker (PID 101879) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 101895) CPU | percent | 3 | 102.107 | 98.558 | 108.790 | 98.973 | 0.310000 CPU seconds | n/a |
| python3 (PID 101895) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 101895) io write MB/s | MB/s | 3 | 0.722 | 0.000 | 2.165 | 2.165 | 0.218750 MB | n/a |
| python3 (PID 101895) rss_mb | MB | 4 | 25.821 | 12.926 | 34.500 | 34.500 | n/a | n/a |
| python3 (PID 101895) vms_mb | MB | 4 | 50.001 | 38.297 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 101924) rss_mb | MB | 1 | 25.746 | 25.746 | 25.746 | 25.746 | n/a | n/a |
| docker (PID 101924) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 101946) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 101946) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 101946) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 101946) rss_mb | MB | 2 | 27.242 | 27.059 | 27.426 | 27.426 | n/a | n/a |
| docker (PID 101946) vms_mb | MB | 2 | 1697.025 | 1661.023 | 1733.027 | 1733.027 | n/a | n/a |
| docker-init [beam_0000] (PID 101987) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beam_0000] (PID 101987) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [beam_0000] (PID 101987) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 101999) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 101999) rss_mb | MB | 4 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [beam_0000] (PID 101999) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 102035) rss_mb | MB | 1 | 20.918 | 20.918 | 20.918 | 20.918 | n/a | n/a |
| docker (PID 102035) vms_mb | MB | 1 | 1524.203 | 1524.203 | 1524.203 | 1524.203 | n/a | n/a |
| docker (PID 102061) rss_mb | MB | 1 | 27.602 | 27.602 | 27.602 | 27.602 | n/a | n/a |
| docker (PID 102061) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 102080) rss_mb | MB | 1 | 11.863 | 11.863 | 11.863 | 11.863 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 102080) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 102135) rss_mb | MB | 1 | 25.883 | 25.883 | 25.883 | 25.883 | n/a | n/a |
| docker (PID 102135) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 102196) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 102196) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 102196) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 102196) rss_mb | MB | 2 | 25.289 | 23.711 | 26.867 | 26.867 | n/a | n/a |
| docker (PID 102196) vms_mb | MB | 2 | 1624.488 | 1588.203 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 102236) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [beam_0000] (PID 102236) rss_mb | MB | 4 | 3.599 | 0.633 | 12.496 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 102236) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 102248) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 102248) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [beam_0000] (PID 102248) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 102258) rss_mb | MB | 1 | 27.004 | 27.004 | 27.004 | 27.004 | n/a | n/a |
| docker (PID 102258) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 102279) rss_mb | MB | 1 | 12.227 | 12.227 | 12.227 | 12.227 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 102279) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 102321) rss_mb | MB | 1 | 3.504 | 3.504 | 3.504 | 3.504 | n/a | n/a |
| docker (PID 102321) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 102359) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 102359) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 102359) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 102359) rss_mb | MB | 2 | 25.992 | 25.992 | 25.992 | 25.992 | n/a | n/a |
| docker (PID 102359) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 102425) rss_mb | MB | 1 | 11.109 | 11.109 | 11.109 | 11.109 | n/a | n/a |
| docker (PID 102425) vms_mb | MB | 1 | 1451.949 | 1451.949 | 1451.949 | 1451.949 | n/a | n/a |
| docker (PID 102439) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 102439) io read MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 102439) io write MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 102439) rss_mb | MB | 37 | 26.945 | 26.945 | 26.945 | 26.945 | n/a | n/a |
| docker (PID 102439) vms_mb | MB | 37 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 102455) rss_mb | MB | 1 | 8.715 | 8.715 | 8.715 | 8.715 | n/a | n/a |
| docker (PID 102455) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 102473) rss_mb | MB | 1 | 25.598 | 25.598 | 25.598 | 25.598 | n/a | n/a |
| docker (PID 102473) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 102481) rss_mb | MB | 1 | 26.867 | 26.867 | 26.867 | 26.867 | n/a | n/a |
| docker (PID 102481) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 102521) CPU | percent | 3 | 6.506 | 0.000 | 19.519 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [beam_0000] (PID 102521) rss_mb | MB | 4 | 3.531 | 0.633 | 12.227 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 102521) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 102533) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 102533) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [beam_0000] (PID 102533) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 102544) rss_mb | MB | 1 | 27.352 | 27.352 | 27.352 | 27.352 | n/a | n/a |
| docker (PID 102544) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[0:PARENT] [beam_0000] (PID 102560) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[0:PARENT] [beam_0000] (PID 102560) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 102563) rss_mb | MB | 1 | 3.898 | 3.898 | 3.898 | 3.898 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 102563) vms_mb | MB | 1 | 1216.680 | 1216.680 | 1216.680 | 1216.680 | n/a | n/a |
| docker (PID 102597) rss_mb | MB | 1 | 4.219 | 4.219 | 4.219 | 4.219 | n/a | n/a |
| docker (PID 102597) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 102634) rss_mb | MB | 1 | 26.172 | 26.172 | 26.172 | 26.172 | n/a | n/a |
| docker (PID 102634) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 102642) rss_mb | MB | 1 | 27.035 | 27.035 | 27.035 | 27.035 | n/a | n/a |
| docker (PID 102642) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 102701) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 102701) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 102701) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 102701) rss_mb | MB | 2 | 27.160 | 27.160 | 27.160 | 27.160 | n/a | n/a |
| docker (PID 102701) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [beam_0000] (PID 102741) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beam_0000] (PID 102741) rss_mb | MB | 10 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [beam_0000] (PID 102741) vms_mb | MB | 10 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 102755) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 102755) rss_mb | MB | 9 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [beam_0000] (PID 102755) vms_mb | MB | 9 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 102793) CPU | percent | 8 | 1.219 | 0.000 | 9.750 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 102793) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 102793) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 102793) rss_mb | MB | 9 | 24.339 | 1.992 | 27.133 | 27.133 | n/a | n/a |
| docker (PID 102793) vms_mb | MB | 9 | 1479.883 | 32.762 | 1660.773 | 1660.773 | n/a | n/a |
| bash [beam_0000] (PID 102812) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [beam_0000] (PID 102812) rss_mb | MB | 8 | 3.246 | 3.246 | 3.246 | 3.246 | n/a | n/a |
| bash [beam_0000] (PID 102812) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [beam_0000] (PID 102821) CPU | percent | 7 | 100.715 | 88.189 | 108.026 | 107.982 | 0.720000 CPU seconds | n/a |
| python [beam_0000] (PID 102821) rss_mb | MB | 8 | 31.222 | 12.363 | 42.078 | 42.078 | n/a | n/a |
| python [beam_0000] (PID 102821) vms_mb | MB | 8 | 38.198 | 16.277 | 51.238 | 51.238 | n/a | n/a |
| docker (PID 102831) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 102831) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 102831) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 102831) rss_mb | MB | 2 | 26.895 | 26.895 | 26.895 | 26.895 | n/a | n/a |
| docker (PID 102831) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 102889) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 102889) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 102889) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 102889) rss_mb | MB | 2 | 26.668 | 26.668 | 26.668 | 26.668 | n/a | n/a |
| docker (PID 102889) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 102929) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [beam_0000] (PID 102929) rss_mb | MB | 3 | 4.667 | 0.633 | 12.734 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 102929) vms_mb | MB | 3 | 524.112 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 102942) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 102942) rss_mb | MB | 2 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [beam_0000] (PID 102942) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 102983) rss_mb | MB | 1 | 6.520 | 6.520 | 6.520 | 6.520 | n/a | n/a |
| docker (PID 102983) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 103018) rss_mb | MB | 1 | 27.121 | 27.121 | 27.121 | 27.121 | n/a | n/a |
| docker (PID 103018) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 103054) rss_mb | MB | 1 | 25.973 | 25.973 | 25.973 | 25.973 | n/a | n/a |
| docker (PID 103054) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 103096) rss_mb | MB | 1 | 0.164 | 0.164 | 0.164 | 0.164 | n/a | n/a |
| docker (PID 103096) vms_mb | MB | 1 | 30.570 | 30.570 | 30.570 | 30.570 | n/a | n/a |
| docker (PID 103113) rss_mb | MB | 1 | 9.281 | 9.281 | 9.281 | 9.281 | n/a | n/a |
| docker (PID 103113) vms_mb | MB | 1 | 1371.691 | 1371.691 | 1371.691 | 1371.691 | n/a | n/a |
| docker (PID 103138) rss_mb | MB | 1 | 26.730 | 26.730 | 26.730 | 26.730 | n/a | n/a |
| docker (PID 103138) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 103146) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 103146) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 103146) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 103146) rss_mb | MB | 39 | 25.637 | 25.637 | 25.637 | 25.637 | n/a | n/a |
| docker (PID 103146) vms_mb | MB | 39 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 103178) rss_mb | MB | 1 | 26.500 | 26.500 | 26.500 | 26.500 | n/a | n/a |
| docker (PID 103178) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 103193) CPU | percent | 3 | 98.772 | 98.448 | 98.968 | 98.968 | 0.300000 CPU seconds | n/a |
| python3 (PID 103193) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 103193) io write MB/s | MB/s | 3 | 0.773 | 0.000 | 2.320 | 2.320 | 0.234375 MB | n/a |
| python3 (PID 103193) rss_mb | MB | 4 | 25.587 | 12.898 | 34.422 | 34.422 | n/a | n/a |
| python3 (PID 103193) vms_mb | MB | 4 | 49.670 | 38.297 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 103244) CPU | percent | 2 | 4.796 | 0.000 | 9.593 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 103244) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 103244) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 103244) rss_mb | MB | 3 | 18.297 | 0.000 | 27.445 | 27.445 | n/a | n/a |
| docker (PID 103244) vms_mb | MB | 3 | 1213.378 | 30.570 | 1804.781 | 1804.781 | n/a | n/a |
| docker-init [bear_0000] (PID 103287) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bear_0000] (PID 103287) rss_mb | MB | 4 | 3.721 | 0.633 | 12.984 | 0.633 | n/a | n/a |
| docker-init [bear_0000] (PID 103287) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 103300) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 103300) rss_mb | MB | 3 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [bear_0000] (PID 103300) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 103338) rss_mb | MB | 1 | 15.738 | 15.738 | 15.738 | 15.738 | n/a | n/a |
| docker (PID 103338) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 103365) rss_mb | MB | 1 | 27.262 | 27.262 | 27.262 | 27.262 | n/a | n/a |
| docker (PID 103365) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 103385) rss_mb | MB | 1 | 11.051 | 11.051 | 11.051 | 11.051 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 103385) vms_mb | MB | 1 | 1569.840 | 1569.840 | 1569.840 | 1569.840 | n/a | n/a |
| docker (PID 103401) rss_mb | MB | 1 | 27.273 | 27.273 | 27.273 | 27.273 | n/a | n/a |
| docker (PID 103401) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| sh [bear_0000] (PID 103421) rss_mb | MB | 1 | 1.676 | 1.676 | 1.676 | 1.676 | n/a | n/a |
| sh [bear_0000] (PID 103421) vms_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| sh [bear_0000] (PID 103428) rss_mb | MB | 1 | 1.676 | 1.676 | 1.676 | 1.676 | n/a | n/a |
| sh [bear_0000] (PID 103428) vms_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| docker (PID 103438) rss_mb | MB | 1 | 27.066 | 27.066 | 27.066 | 27.066 | n/a | n/a |
| docker (PID 103438) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 103495) CPU | percent | 1 | 9.859 | 9.859 | 9.859 | 9.859 | 0.010000 CPU seconds | n/a |
| docker (PID 103495) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 103495) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 103495) rss_mb | MB | 2 | 21.729 | 17.938 | 25.520 | 25.520 | n/a | n/a |
| docker (PID 103495) vms_mb | MB | 2 | 1588.080 | 1515.949 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 103535) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 103535) rss_mb | MB | 4 | 3.733 | 0.633 | 13.035 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 103535) vms_mb | MB | 4 | 393.473 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 103547) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 103547) rss_mb | MB | 3 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [bear_0000] (PID 103547) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 103557) rss_mb | MB | 1 | 27.414 | 27.414 | 27.414 | 27.414 | n/a | n/a |
| docker (PID 103557) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 103577) rss_mb | MB | 1 | 11.859 | 11.859 | 11.859 | 11.859 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 103577) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 103619) rss_mb | MB | 1 | 17.984 | 17.984 | 17.984 | 17.984 | n/a | n/a |
| docker (PID 103619) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 103658) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 103658) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 103658) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 103658) rss_mb | MB | 2 | 25.859 | 25.859 | 25.859 | 25.859 | n/a | n/a |
| docker (PID 103658) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 103707) rss_mb | MB | 1 | 0.402 | 0.402 | 0.402 | 0.402 | n/a | n/a |
| docker (PID 103707) vms_mb | MB | 1 | 32.750 | 32.750 | 32.750 | 32.750 | n/a | n/a |
| docker (PID 103715) rss_mb | MB | 1 | 25.633 | 25.633 | 25.633 | 25.633 | n/a | n/a |
| docker (PID 103715) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 103755) CPU | percent | 2 | 9.729 | 0.000 | 19.458 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 103755) rss_mb | MB | 3 | 4.044 | 0.562 | 11.008 | 0.562 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 103755) vms_mb | MB | 3 | 523.768 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 103767) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 103767) rss_mb | MB | 2 | 1.684 | 1.684 | 1.684 | 1.684 | n/a | n/a |
| tail [bear_0000] (PID 103767) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 103777) rss_mb | MB | 1 | 27.375 | 27.375 | 27.375 | 27.375 | n/a | n/a |
| docker (PID 103777) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 103804) rss_mb | MB | 1 | 27.141 | 27.141 | 27.141 | 27.141 | n/a | n/a |
| docker (PID 103804) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| bash [bear_0000] (PID 103823) rss_mb | MB | 1 | 3.359 | 3.359 | 3.359 | 3.359 | n/a | n/a |
| bash [bear_0000] (PID 103823) vms_mb | MB | 1 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| bash [bear_0000] (PID 103828) rss_mb | MB | 1 | 0.152 | 0.152 | 0.152 | 0.152 | n/a | n/a |
| bash [bear_0000] (PID 103828) vms_mb | MB | 1 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| docker (PID 103845) rss_mb | MB | 1 | 25.723 | 25.723 | 25.723 | 25.723 | n/a | n/a |
| docker (PID 103845) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 103905) rss_mb | MB | 1 | 25.602 | 25.602 | 25.602 | 25.602 | n/a | n/a |
| docker (PID 103905) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bear_0000] (PID 103945) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bear_0000] (PID 103945) rss_mb | MB | 2 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bear_0000] (PID 103945) vms_mb | MB | 2 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 103957) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 103957) rss_mb | MB | 2 | 1.809 | 1.809 | 1.809 | 1.809 | n/a | n/a |
| tail [bear_0000] (PID 103957) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 103959) rss_mb | MB | 1 | 26.141 | 26.141 | 26.141 | 26.141 | n/a | n/a |
| docker (PID 103959) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 103993) rss_mb | MB | 1 | 27.676 | 27.676 | 27.676 | 27.676 | n/a | n/a |
| docker (PID 103993) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[0:PARENT] [bear_0000] (PID 104009) rss_mb | MB | 1 | 1.961 | 1.961 | 1.961 | 1.961 | n/a | n/a |
| runc:[0:PARENT] [bear_0000] (PID 104009) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[1:CHILD] [bear_0000] (PID 104013) rss_mb | MB | 1 | 1.223 | 1.223 | 1.223 | 1.223 | n/a | n/a |
| runc:[1:CHILD] [bear_0000] (PID 104013) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[1:CHILD] [bear_0000] (PID 104014) rss_mb | MB | 1 | 0.125 | 0.125 | 0.125 | 0.125 | n/a | n/a |
| runc:[1:CHILD] [bear_0000] (PID 104014) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| docker (PID 104037) rss_mb | MB | 1 | 26.793 | 26.793 | 26.793 | 26.793 | n/a | n/a |
| docker (PID 104037) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 104081) rss_mb | MB | 1 | 9.922 | 9.922 | 9.922 | 9.922 | n/a | n/a |
| docker (PID 104081) vms_mb | MB | 1 | 1387.949 | 1387.949 | 1387.949 | 1387.949 | n/a | n/a |
| docker (PID 104098) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 104098) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 104098) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 104098) rss_mb | MB | 2 | 27.043 | 27.043 | 27.043 | 27.043 | n/a | n/a |
| docker (PID 104098) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 104137) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 104137) rss_mb | MB | 4 | 3.606 | 0.000 | 13.160 | 0.000 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 104137) vms_mb | MB | 4 | 411.147 | 0.000 | 1642.480 | 0.000 | n/a | n/a |
| tail [bear_0000] (PID 104151) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 104151) rss_mb | MB | 2 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [bear_0000] (PID 104151) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 104161) rss_mb | MB | 1 | 27.453 | 27.453 | 27.453 | 27.453 | n/a | n/a |
| docker (PID 104161) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 104227) rss_mb | MB | 1 | 26.434 | 26.434 | 26.434 | 26.434 | n/a | n/a |
| docker (PID 104227) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 104264) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 104264) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 104264) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 104264) rss_mb | MB | 2 | 27.090 | 27.090 | 27.090 | 27.090 | n/a | n/a |
| docker (PID 104264) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 104334) rss_mb | MB | 1 | 25.656 | 25.656 | 25.656 | 25.656 | n/a | n/a |
| docker (PID 104334) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 104348) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 104348) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 104348) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 104348) rss_mb | MB | 38 | 26.578 | 26.578 | 26.578 | 26.578 | n/a | n/a |
| docker (PID 104348) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 104373) rss_mb | MB | 1 | 23.008 | 23.008 | 23.008 | 23.008 | n/a | n/a |
| docker (PID 104373) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 104392) rss_mb | MB | 1 | 26.758 | 26.758 | 26.758 | 26.758 | n/a | n/a |
| docker (PID 104392) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 104433) CPU | percent | 3 | 6.448 | 0.000 | 19.343 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 104433) rss_mb | MB | 4 | 1.549 | 0.633 | 4.297 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 104433) vms_mb | MB | 4 | 375.089 | 1.055 | 1497.191 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 104446) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 104446) rss_mb | MB | 3 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [bear_0000] (PID 104446) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 104457) rss_mb | MB | 1 | 17.312 | 17.312 | 17.312 | 17.312 | n/a | n/a |
| docker (PID 104457) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 104483) rss_mb | MB | 1 | 27.402 | 27.402 | 27.402 | 27.402 | n/a | n/a |
| docker (PID 104483) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 104503) rss_mb | MB | 1 | 11.188 | 11.188 | 11.188 | 11.188 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 104503) vms_mb | MB | 1 | 1641.965 | 1641.965 | 1641.965 | 1641.965 | n/a | n/a |
| docker (PID 104521) rss_mb | MB | 1 | 27.281 | 27.281 | 27.281 | 27.281 | n/a | n/a |
| docker (PID 104521) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 104540) rss_mb | MB | 1 | 11.992 | 11.992 | 11.992 | 11.992 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 104540) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 104559) rss_mb | MB | 1 | 26.004 | 26.004 | 26.004 | 26.004 | n/a | n/a |
| docker (PID 104559) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 104618) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 104618) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 104618) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 104618) rss_mb | MB | 2 | 23.094 | 20.215 | 25.973 | 25.973 | n/a | n/a |
| docker (PID 104618) vms_mb | MB | 2 | 1624.207 | 1588.203 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 104657) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 104657) rss_mb | MB | 11 | 1.726 | 0.633 | 12.660 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 104657) vms_mb | MB | 11 | 143.707 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 104669) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 104669) rss_mb | MB | 10 | 1.684 | 1.684 | 1.684 | 1.684 | n/a | n/a |
| tail [bear_0000] (PID 104669) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 104679) rss_mb | MB | 1 | 27.023 | 27.023 | 27.023 | 27.023 | n/a | n/a |
| docker (PID 104679) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 104699) rss_mb | MB | 1 | 11.770 | 11.770 | 11.770 | 11.770 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 104699) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 104708) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 104708) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 104708) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 104708) rss_mb | MB | 8 | 27.449 | 27.434 | 27.559 | 27.559 | n/a | n/a |
| docker (PID 104708) vms_mb | MB | 8 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [bear_0000] (PID 104728) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bear_0000] (PID 104728) rss_mb | MB | 8 | 3.328 | 3.328 | 3.328 | 3.328 | n/a | n/a |
| bash [bear_0000] (PID 104728) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bear_0000] (PID 104738) CPU | percent | 7 | 100.699 | 96.951 | 107.924 | 98.088 | 0.720000 CPU seconds | n/a |
| python [bear_0000] (PID 104738) rss_mb | MB | 8 | 30.817 | 9.684 | 41.973 | 41.973 | n/a | n/a |
| python [bear_0000] (PID 104738) vms_mb | MB | 8 | 38.039 | 13.434 | 51.340 | 51.340 | n/a | n/a |
| docker (PID 104748) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 104748) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 104748) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 104748) rss_mb | MB | 2 | 25.354 | 23.941 | 26.766 | 26.766 | n/a | n/a |
| docker (PID 104748) vms_mb | MB | 2 | 1628.492 | 1596.211 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 104819) rss_mb | MB | 1 | 23.000 | 23.000 | 23.000 | 23.000 | n/a | n/a |
| docker (PID 104819) vms_mb | MB | 1 | 1524.203 | 1524.203 | 1524.203 | 1524.203 | n/a | n/a |
| docker (PID 104835) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 104835) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 104835) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 104835) rss_mb | MB | 39 | 26.348 | 26.348 | 26.348 | 26.348 | n/a | n/a |
| docker (PID 104835) vms_mb | MB | 39 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 104868) rss_mb | MB | 1 | 25.699 | 25.699 | 25.699 | 25.699 | n/a | n/a |
| docker (PID 104868) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| python3 (PID 104883) CPU | percent | 3 | 98.780 | 88.627 | 108.842 | 108.842 | 0.300000 CPU seconds | n/a |
| python3 (PID 104883) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 104883) io write MB/s | MB/s | 3 | 0.773 | 0.000 | 2.319 | 2.319 | 0.234375 MB | n/a |
| python3 (PID 104883) rss_mb | MB | 4 | 26.160 | 13.273 | 34.523 | 34.523 | n/a | n/a |
| python3 (PID 104883) vms_mb | MB | 4 | 50.343 | 39.430 | 57.434 | 57.434 | n/a | n/a |
| docker (PID 104888) rss_mb | MB | 1 | 19.367 | 19.367 | 19.367 | 19.367 | n/a | n/a |
| docker (PID 104888) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 104912) rss_mb | MB | 1 | 25.453 | 25.453 | 25.453 | 25.453 | n/a | n/a |
| docker (PID 104912) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 104920) rss_mb | MB | 1 | 15.582 | 15.582 | 15.582 | 15.582 | n/a | n/a |
| docker (PID 104920) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 104934) CPU | percent | 1 | 19.527 | 19.527 | 19.527 | 19.527 | 0.020000 CPU seconds | n/a |
| docker (PID 104934) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 104934) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 104934) rss_mb | MB | 2 | 27.119 | 26.875 | 27.363 | 27.363 | n/a | n/a |
| docker (PID 104934) vms_mb | MB | 2 | 1696.775 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [beef_0000] (PID 104973) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beef_0000] (PID 104973) rss_mb | MB | 4 | 3.566 | 0.633 | 12.367 | 0.633 | n/a | n/a |
| docker-init [beef_0000] (PID 104973) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 104987) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 104987) rss_mb | MB | 3 | 1.809 | 1.809 | 1.809 | 1.809 | n/a | n/a |
| tail [beef_0000] (PID 104987) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 104989) rss_mb | MB | 1 | 27.449 | 27.449 | 27.449 | 27.449 | n/a | n/a |
| docker (PID 104989) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] (PID 105009) rss_mb | MB | 1 | 11.461 | 11.461 | 11.461 | 11.461 | n/a | n/a |
| runc:[2:INIT] (PID 105009) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 105055) rss_mb | MB | 1 | 1.613 | 1.613 | 1.613 | 1.613 | n/a | n/a |
| docker (PID 105055) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 105093) rss_mb | MB | 1 | 26.582 | 26.582 | 26.582 | 26.582 | n/a | n/a |
| docker (PID 105093) vms_mb | MB | 1 | 1668.277 | 1668.277 | 1668.277 | 1668.277 | n/a | n/a |
| docker (PID 105131) rss_mb | MB | 1 | 26.047 | 26.047 | 26.047 | 26.047 | n/a | n/a |
| docker (PID 105131) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 105175) rss_mb | MB | 1 | 17.988 | 17.988 | 17.988 | 17.988 | n/a | n/a |
| docker (PID 105175) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 105191) rss_mb | MB | 1 | 25.527 | 25.527 | 25.527 | 25.527 | n/a | n/a |
| docker (PID 105191) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 105231) CPU | percent | 3 | 6.379 | 0.000 | 19.137 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [beef_0000] (PID 105231) rss_mb | MB | 4 | 1.574 | 0.633 | 4.398 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 105231) vms_mb | MB | 4 | 325.025 | 1.055 | 1296.938 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 105242) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 105242) rss_mb | MB | 3 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [beef_0000] (PID 105242) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 105252) rss_mb | MB | 1 | 23.461 | 23.461 | 23.461 | 23.461 | n/a | n/a |
| docker (PID 105252) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 105280) rss_mb | MB | 1 | 27.141 | 27.141 | 27.141 | 27.141 | n/a | n/a |
| docker (PID 105280) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 105300) rss_mb | MB | 1 | 12.000 | 12.000 | 12.000 | 12.000 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 105300) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 105352) rss_mb | MB | 1 | 26.832 | 26.832 | 26.832 | 26.832 | n/a | n/a |
| docker (PID 105352) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 105405) rss_mb | MB | 1 | 3.449 | 3.449 | 3.449 | 3.449 | n/a | n/a |
| docker (PID 105405) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 105435) CPU | percent | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 105435) io read MB/s | MB/s | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 105435) io write MB/s | MB/s | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 105435) rss_mb | MB | 52 | 26.543 | 26.543 | 26.543 | 26.543 | n/a | n/a |
| docker (PID 105435) vms_mb | MB | 52 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 105451) rss_mb | MB | 1 | 25.574 | 25.574 | 25.574 | 25.574 | n/a | n/a |
| docker (PID 105451) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 105477) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 105477) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 105477) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 105477) rss_mb | MB | 2 | 25.883 | 25.883 | 25.883 | 25.883 | n/a | n/a |
| docker (PID 105477) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [beef_0000] (PID 105515) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beef_0000] (PID 105515) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [beef_0000] (PID 105515) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 105527) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 105527) rss_mb | MB | 3 | 1.408 | 0.816 | 1.703 | 1.703 | n/a | n/a |
| tail [beef_0000] (PID 105527) vms_mb | MB | 3 | 2.803 | 2.441 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 105566) rss_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| docker (PID 105566) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 105602) rss_mb | MB | 1 | 27.387 | 27.387 | 27.387 | 27.387 | n/a | n/a |
| docker (PID 105602) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 105642) rss_mb | MB | 1 | 26.883 | 26.883 | 26.883 | 26.883 | n/a | n/a |
| docker (PID 105642) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 105683) rss_mb | MB | 1 | 14.898 | 14.898 | 14.898 | 14.898 | n/a | n/a |
| docker (PID 105683) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 105700) rss_mb | MB | 1 | 26.664 | 26.664 | 26.664 | 26.664 | n/a | n/a |
| docker (PID 105700) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [beef_0000] (PID 105738) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beef_0000] (PID 105738) rss_mb | MB | 10 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [beef_0000] (PID 105738) vms_mb | MB | 10 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 105752) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 105752) rss_mb | MB | 10 | 1.809 | 1.809 | 1.809 | 1.809 | n/a | n/a |
| tail [beef_0000] (PID 105752) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 105754) rss_mb | MB | 1 | 25.691 | 25.691 | 25.691 | 25.691 | n/a | n/a |
| docker (PID 105754) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 105791) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 105791) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 105791) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 105791) rss_mb | MB | 9 | 27.477 | 27.477 | 27.477 | 27.477 | n/a | n/a |
| docker (PID 105791) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 105810) CPU | percent | 8 | 2.428 | 0.000 | 19.422 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [beef_0000] (PID 105810) rss_mb | MB | 9 | 3.980 | 3.410 | 8.539 | 3.410 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 105810) vms_mb | MB | 9 | 178.258 | 4.391 | 1569.195 | 4.391 | n/a | n/a |
| python [beef_0000] (PID 105819) CPU | percent | 7 | 100.740 | 98.035 | 107.616 | 107.616 | 0.720000 CPU seconds | n/a |
| python [beef_0000] (PID 105819) rss_mb | MB | 8 | 31.793 | 14.641 | 41.777 | 41.777 | n/a | n/a |
| python [beef_0000] (PID 105819) vms_mb | MB | 8 | 38.712 | 18.430 | 51.238 | 51.238 | n/a | n/a |
| docker (PID 105829) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 105829) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 105829) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 105829) rss_mb | MB | 2 | 26.840 | 26.840 | 26.840 | 26.840 | n/a | n/a |
| docker (PID 105829) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 105890) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 105890) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 105890) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 105890) rss_mb | MB | 2 | 15.859 | 6.219 | 25.500 | 25.500 | n/a | n/a |
| docker (PID 105890) vms_mb | MB | 2 | 846.486 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 105929) CPU | percent | 3 | 3.255 | 0.000 | 9.765 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [beef_0000] (PID 105929) rss_mb | MB | 4 | 3.712 | 0.633 | 12.949 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 105929) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 105943) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 105943) rss_mb | MB | 3 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [beef_0000] (PID 105943) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 105953) rss_mb | MB | 1 | 27.273 | 27.273 | 27.273 | 27.273 | n/a | n/a |
| docker (PID 105953) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 105973) rss_mb | MB | 1 | 11.344 | 11.344 | 11.344 | 11.344 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 105973) vms_mb | MB | 1 | 1570.098 | 1570.098 | 1570.098 | 1570.098 | n/a | n/a |
| docker (PID 106006) rss_mb | MB | 1 | 22.996 | 22.996 | 22.996 | 22.996 | n/a | n/a |
| docker (PID 106006) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 106052) CPU | percent | 1 | 9.759 | 9.759 | 9.759 | 9.759 | 0.010000 CPU seconds | n/a |
| docker (PID 106052) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 106052) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 106052) rss_mb | MB | 2 | 17.529 | 9.117 | 25.941 | 25.941 | n/a | n/a |
| docker (PID 106052) vms_mb | MB | 2 | 1443.822 | 1227.434 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 106114) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 106114) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 106140) rss_mb | MB | 1 | 25.891 | 25.891 | 25.891 | 25.891 | n/a | n/a |
| docker (PID 106140) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 106148) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 106148) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 106148) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 106148) rss_mb | MB | 38 | 25.645 | 25.645 | 25.645 | 25.645 | n/a | n/a |
| docker (PID 106148) vms_mb | MB | 38 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 106164) rss_mb | MB | 1 | 9.277 | 9.277 | 9.277 | 9.277 | n/a | n/a |
| docker (PID 106164) vms_mb | MB | 1 | 1315.945 | 1315.945 | 1315.945 | 1315.945 | n/a | n/a |
| docker (PID 106180) rss_mb | MB | 1 | 26.957 | 26.957 | 26.957 | 26.957 | n/a | n/a |
| docker (PID 106180) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 106195) CPU | percent | 3 | 98.761 | 89.078 | 108.732 | 108.732 | 0.300000 CPU seconds | n/a |
| python3 (PID 106195) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 106195) io write MB/s | MB/s | 3 | 0.772 | 0.000 | 2.317 | 2.317 | 0.234375 MB | n/a |
| python3 (PID 106195) rss_mb | MB | 4 | 26.986 | 15.254 | 34.691 | 34.691 | n/a | n/a |
| python3 (PID 106195) vms_mb | MB | 4 | 51.015 | 40.898 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 106200) rss_mb | MB | 1 | 18.238 | 18.238 | 18.238 | 18.238 | n/a | n/a |
| docker (PID 106200) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 106224) rss_mb | MB | 1 | 26.898 | 26.898 | 26.898 | 26.898 | n/a | n/a |
| docker (PID 106224) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 106247) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 106247) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 106247) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 106247) rss_mb | MB | 2 | 27.045 | 26.750 | 27.340 | 27.340 | n/a | n/a |
| docker (PID 106247) vms_mb | MB | 2 | 1697.025 | 1661.023 | 1733.027 | 1733.027 | n/a | n/a |
| docker-init [bell_0000] (PID 106286) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bell_0000] (PID 106286) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bell_0000] (PID 106286) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 106298) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 106298) rss_mb | MB | 4 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [bell_0000] (PID 106298) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 106300) rss_mb | MB | 1 | 19.105 | 19.105 | 19.105 | 19.105 | n/a | n/a |
| docker (PID 106300) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 106337) rss_mb | MB | 1 | 26.848 | 26.848 | 26.848 | 26.848 | n/a | n/a |
| docker (PID 106337) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 106363) rss_mb | MB | 1 | 27.145 | 27.145 | 27.145 | 27.145 | n/a | n/a |
| docker (PID 106363) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 106431) rss_mb | MB | 1 | 22.652 | 22.652 | 22.652 | 22.652 | n/a | n/a |
| docker (PID 106431) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 106440) rss_mb | MB | 1 | 25.883 | 25.883 | 25.883 | 25.883 | n/a | n/a |
| docker (PID 106440) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 106497) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 106497) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 106497) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 106497) rss_mb | MB | 2 | 26.762 | 26.762 | 26.762 | 26.762 | n/a | n/a |
| docker (PID 106497) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [bell_0000] (PID 106537) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bell_0000] (PID 106537) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bell_0000] (PID 106537) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 106549) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 106549) rss_mb | MB | 3 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [bell_0000] (PID 106549) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 106587) rss_mb | MB | 1 | 9.285 | 9.285 | 9.285 | 9.285 | n/a | n/a |
| docker (PID 106587) vms_mb | MB | 1 | 1235.438 | 1235.438 | 1235.438 | 1235.438 | n/a | n/a |
| docker (PID 106622) rss_mb | MB | 1 | 26.816 | 26.816 | 26.816 | 26.816 | n/a | n/a |
| docker (PID 106622) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 106658) rss_mb | MB | 1 | 25.824 | 25.824 | 25.824 | 25.824 | n/a | n/a |
| docker (PID 106658) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 106701) rss_mb | MB | 1 | 23.445 | 23.445 | 23.445 | 23.445 | n/a | n/a |
| docker (PID 106701) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 106726) rss_mb | MB | 1 | 17.309 | 17.309 | 17.309 | 17.309 | n/a | n/a |
| docker (PID 106726) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 106740) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 106740) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 106740) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 106740) rss_mb | MB | 38 | 26.457 | 26.457 | 26.457 | 26.457 | n/a | n/a |
| docker (PID 106740) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 106783) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 106783) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 106783) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 106783) rss_mb | MB | 2 | 22.846 | 19.977 | 25.715 | 25.715 | n/a | n/a |
| docker (PID 106783) vms_mb | MB | 2 | 1588.205 | 1516.199 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 106823) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bell_0000] (PID 106823) rss_mb | MB | 4 | 3.803 | 0.633 | 13.312 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 106823) vms_mb | MB | 4 | 411.411 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 106837) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 106837) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bell_0000] (PID 106837) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 106848) rss_mb | MB | 1 | 27.391 | 27.391 | 27.391 | 27.391 | n/a | n/a |
| docker (PID 106848) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 106868) rss_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 106868) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 106913) rss_mb | MB | 1 | 0.945 | 0.945 | 0.945 | 0.945 | n/a | n/a |
| docker (PID 106913) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 106951) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 106951) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 106951) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 106951) rss_mb | MB | 2 | 26.137 | 26.137 | 26.137 | 26.137 | n/a | n/a |
| docker (PID 106951) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 107009) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 107009) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 107009) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 107009) rss_mb | MB | 2 | 25.645 | 25.645 | 25.645 | 25.645 | n/a | n/a |
| docker (PID 107009) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 107050) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bell_0000] (PID 107050) rss_mb | MB | 10 | 1.882 | 0.633 | 13.121 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 107050) vms_mb | MB | 10 | 158.022 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 107062) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 107062) rss_mb | MB | 9 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [bell_0000] (PID 107062) vms_mb | MB | 9 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 107098) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 107098) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 107098) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 107098) rss_mb | MB | 8 | 27.191 | 27.191 | 27.191 | 27.191 | n/a | n/a |
| docker (PID 107098) vms_mb | MB | 8 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [bell_0000] (PID 107118) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bell_0000] (PID 107118) rss_mb | MB | 8 | 3.324 | 3.324 | 3.324 | 3.324 | n/a | n/a |
| bash [bell_0000] (PID 107118) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bell_0000] (PID 107127) CPU | percent | 7 | 99.321 | 88.374 | 107.904 | 88.374 | 0.710000 CPU seconds | n/a |
| python [bell_0000] (PID 107127) rss_mb | MB | 8 | 31.181 | 11.766 | 42.090 | 42.090 | n/a | n/a |
| python [bell_0000] (PID 107127) vms_mb | MB | 8 | 38.189 | 16.207 | 51.238 | 51.238 | n/a | n/a |
| docker (PID 107137) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 107137) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 107137) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 107137) rss_mb | MB | 2 | 26.898 | 26.898 | 26.898 | 26.898 | n/a | n/a |
| docker (PID 107137) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 107190) rss_mb | MB | 1 | 27.008 | 27.008 | 27.008 | 27.008 | n/a | n/a |
| docker (PID 107190) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 107232) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 107232) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 107232) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 107232) rss_mb | MB | 39 | 25.169 | 1.617 | 25.789 | 25.789 | n/a | n/a |
| docker (PID 107232) vms_mb | MB | 39 | 1618.481 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 107248) rss_mb | MB | 1 | 2.773 | 2.773 | 2.773 | 2.773 | n/a | n/a |
| docker (PID 107248) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 107273) rss_mb | MB | 1 | 5.016 | 5.016 | 5.016 | 5.016 | n/a | n/a |
| docker (PID 107273) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| python3 (PID 107280) CPU | percent | 3 | 102.034 | 98.427 | 108.824 | 98.852 | 0.310000 CPU seconds | n/a |
| python3 (PID 107280) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 107280) io write MB/s | MB/s | 3 | 0.772 | 0.000 | 2.317 | 2.317 | 0.234375 MB | n/a |
| python3 (PID 107280) rss_mb | MB | 4 | 28.171 | 17.691 | 34.664 | 34.664 | n/a | n/a |
| python3 (PID 107280) vms_mb | MB | 4 | 51.818 | 42.434 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 107307) rss_mb | MB | 1 | 16.441 | 16.441 | 16.441 | 16.441 | n/a | n/a |
| docker (PID 107307) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| python3 (PID 89845) CPU | percent | 7523 | 3.635 | 0.000 | 237.720 | 18.225 | 27.840000 CPU seconds | n/a |
| python3 (PID 89845) io read MB/s | MB/s | 7523 | 0.028 | 0.000 | 29.038 | 0.000 | 21.882812 MB | n/a |
| python3 (PID 89845) io write MB/s | MB/s | 7523 | 0.046 | 0.000 | 22.640 | 4.948 | 35.320312 MB | n/a |
| python3 (PID 89845) rss_mb | MB | 7524 | 688.011 | 616.426 | 705.445 | 705.445 | n/a | n/a |
| python3 (PID 89845) vms_mb | MB | 7524 | 3737.574 | 3414.109 | 3768.191 | 3768.160 | n/a | n/a |
| git (PID 89851) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| git (PID 89851) io read MB/s | MB/s | 4 | 0.038 | 0.000 | 0.154 | 0.000 | 0.015625 MB | n/a |
| git (PID 89851) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 89851) rss_mb | MB | 5 | 3.963 | 0.863 | 4.738 | 4.738 | n/a | n/a |
| git (PID 89851) vms_mb | MB | 5 | 11.583 | 7.852 | 12.516 | 12.516 | n/a | n/a |
| git (PID 89852) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| git (PID 89852) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 89852) io write MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 89852) rss_mb | MB | 4 | 3.461 | 3.461 | 3.461 | 3.461 | n/a | n/a |
| git (PID 89852) vms_mb | MB | 4 | 11.273 | 11.273 | 11.273 | 11.273 | n/a | n/a |
| git-remote-http (PID 89853) CPU | percent | 3 | 3.291 | 0.000 | 9.873 | 0.000 | 0.010000 CPU seconds | n/a |
| git-remote-http (PID 89853) io read MB/s | MB/s | 3 | 0.579 | 0.000 | 1.543 | 0.000 | 0.175781 MB | n/a |
| git-remote-http (PID 89853) io write MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git-remote-http (PID 89853) rss_mb | MB | 4 | 19.108 | 18.906 | 19.176 | 19.176 | n/a | n/a |
| git-remote-http (PID 89853) vms_mb | MB | 4 | 107.066 | 106.566 | 107.566 | 107.566 | n/a | n/a |
| git (PID 89857) rss_mb | MB | 1 | 4.844 | 4.844 | 4.844 | 4.844 | n/a | n/a |
| git (PID 89857) vms_mb | MB | 1 | 13.207 | 13.207 | 13.207 | 13.207 | n/a | n/a |
| python3 (PID 89859) CPU | percent | 98 | 99.978 | 98.920 | 109.030 | 99.120 | 9.890000 CPU seconds | n/a |
| python3 (PID 89859) io read MB/s | MB/s | 98 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 89859) io write MB/s | MB/s | 98 | 0.002 | 0.000 | 0.155 | 0.000 | 0.015625 MB | n/a |
| python3 (PID 89859) rss_mb | MB | 99 | 33.887 | 15.801 | 34.172 | 34.172 | n/a | n/a |
| python3 (PID 89859) vms_mb | MB | 99 | 57.210 | 41.035 | 57.457 | 57.457 | n/a | n/a |
| python3 (PID 89862) CPU | percent | 3 | 98.848 | 88.621 | 108.954 | 108.954 | 0.300000 CPU seconds | n/a |
| python3 (PID 89862) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 89862) io write MB/s | MB/s | 3 | 0.052 | 0.000 | 0.155 | 0.155 | 0.015625 MB | n/a |
| python3 (PID 89862) rss_mb | MB | 4 | 21.358 | 0.910 | 33.910 | 33.910 | n/a | n/a |
| python3 (PID 89862) vms_mb | MB | 4 | 46.604 | 30.125 | 57.457 | 57.457 | n/a | n/a |
| python3 (PID 89863) CPU | percent | 3 | 99.002 | 98.953 | 99.028 | 99.028 | 0.300000 CPU seconds | n/a |
| python3 (PID 89863) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 89863) io write MB/s | MB/s | 3 | 0.799 | 0.000 | 2.360 | 2.360 | 0.242188 MB | n/a |
| python3 (PID 89863) rss_mb | MB | 4 | 28.979 | 18.492 | 36.215 | 36.215 | n/a | n/a |
| python3 (PID 89863) vms_mb | MB | 4 | 52.089 | 42.566 | 58.457 | 58.457 | n/a | n/a |
| python3 (PID 89864) CPU | percent | 3 | 95.737 | 89.392 | 98.920 | 98.920 | 0.290000 CPU seconds | n/a |
| python3 (PID 89864) io read MB/s | MB/s | 3 | 0.284 | 0.000 | 0.621 | 0.000 | 0.085938 MB | n/a |
| python3 (PID 89864) io write MB/s | MB/s | 3 | 0.799 | 0.000 | 2.357 | 2.357 | 0.242188 MB | n/a |
| python3 (PID 89864) rss_mb | MB | 4 | 29.098 | 20.305 | 34.879 | 34.879 | n/a | n/a |
| python3 (PID 89864) vms_mb | MB | 4 | 52.521 | 45.238 | 57.508 | 57.508 | n/a | n/a |
| python3 (PID 89865) CPU | percent | 24 | 99.389 | 87.641 | 109.023 | 99.049 | 2.410000 CPU seconds | n/a |
| python3 (PID 89865) io read MB/s | MB/s | 24 | 0.032 | 0.000 | 0.761 | 0.000 | 0.078125 MB | n/a |
| python3 (PID 89865) io write MB/s | MB/s | 24 | 0.100 | 0.000 | 2.244 | 2.244 | 0.242188 MB | n/a |
| python3 (PID 89865) rss_mb | MB | 25 | 33.134 | 16.480 | 34.852 | 34.852 | n/a | n/a |
| python3 (PID 89865) vms_mb | MB | 25 | 56.384 | 41.164 | 57.508 | 57.508 | n/a | n/a |
| python3 (PID 89866) CPU | percent | 82 | 99.886 | 88.956 | 108.976 | 99.002 | 8.290000 CPU seconds | n/a |
| python3 (PID 89866) io read MB/s | MB/s | 82 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 89866) io write MB/s | MB/s | 82 | 0.030 | 0.000 | 2.283 | 0.000 | 0.246094 MB | n/a |
| python3 (PID 89866) rss_mb | MB | 83 | 41.306 | 10.523 | 47.758 | 47.758 | n/a | n/a |
| python3 (PID 89866) vms_mb | MB | 83 | 64.347 | 36.633 | 70.645 | 70.645 | n/a | n/a |
| python3 (PID 89867) CPU | percent | 3 | 98.968 | 98.898 | 99.041 | 99.041 | 0.300000 CPU seconds | n/a |
| python3 (PID 89867) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 89867) io write MB/s | MB/s | 3 | 0.825 | 0.000 | 2.476 | 2.476 | 0.250000 MB | n/a |
| python3 (PID 89867) rss_mb | MB | 4 | 27.847 | 17.320 | 34.719 | 34.719 | n/a | n/a |
| python3 (PID 89867) vms_mb | MB | 4 | 51.702 | 42.301 | 57.457 | 57.457 | n/a | n/a |
| python3 (PID 89868) CPU | percent | 99 | 99.861 | 89.107 | 109.024 | 99.130 | 9.980000 CPU seconds | n/a |
| python3 (PID 89868) io read MB/s | MB/s | 99 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 89868) io write MB/s | MB/s | 99 | 0.002 | 0.000 | 0.155 | 0.000 | 0.015625 MB | n/a |
| python3 (PID 89868) rss_mb | MB | 100 | 34.025 | 5.594 | 34.496 | 34.496 | n/a | n/a |
| python3 (PID 89868) vms_mb | MB | 100 | 57.071 | 34.922 | 57.457 | 57.457 | n/a | n/a |
| python3 (PID 89869) CPU | percent | 3 | 102.309 | 89.142 | 108.947 | 108.947 | 0.310000 CPU seconds | n/a |
| python3 (PID 89869) io read MB/s | MB/s | 3 | 0.013 | 0.000 | 0.039 | 0.039 | 0.003906 MB | n/a |
| python3 (PID 89869) io write MB/s | MB/s | 3 | 0.825 | 0.000 | 2.437 | 2.437 | 0.250000 MB | n/a |
| python3 (PID 89869) rss_mb | MB | 4 | 27.960 | 16.609 | 34.996 | 34.996 | n/a | n/a |
| python3 (PID 89869) vms_mb | MB | 4 | 51.462 | 41.164 | 57.496 | 57.496 | n/a | n/a |
| python3 (PID 89870) CPU | percent | 4 | 101.482 | 98.952 | 108.906 | 108.906 | 0.410000 CPU seconds | n/a |
| python3 (PID 89870) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 89870) io write MB/s | MB/s | 4 | 0.619 | 0.000 | 2.320 | 2.320 | 0.250000 MB | n/a |
| python3 (PID 89870) rss_mb | MB | 5 | 26.280 | 9.898 | 34.797 | 34.797 | n/a | n/a |
| python3 (PID 89870) vms_mb | MB | 5 | 50.365 | 36.465 | 57.492 | 57.492 | n/a | n/a |
| python3 (PID 89871) CPU | percent | 3 | 102.294 | 98.950 | 108.953 | 108.953 | 0.310000 CPU seconds | n/a |
| python3 (PID 89871) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 89871) io write MB/s | MB/s | 3 | 0.825 | 0.000 | 2.438 | 2.438 | 0.250000 MB | n/a |
| python3 (PID 89871) rss_mb | MB | 4 | 28.142 | 17.449 | 34.789 | 34.789 | n/a | n/a |
| python3 (PID 89871) vms_mb | MB | 4 | 51.748 | 42.301 | 57.504 | 57.504 | n/a | n/a |
| python3 (PID 89872) CPU | percent | 3 | 99.027 | 98.954 | 99.102 | 99.102 | 0.300000 CPU seconds | n/a |
| python3 (PID 89872) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 89872) io write MB/s | MB/s | 3 | 0.826 | 0.000 | 2.478 | 2.478 | 0.250000 MB | n/a |
| python3 (PID 89872) rss_mb | MB | 4 | 25.814 | 12.594 | 34.840 | 34.840 | n/a | n/a |
| python3 (PID 89872) vms_mb | MB | 4 | 49.732 | 38.293 | 57.504 | 57.504 | n/a | n/a |
| docker (PID 89876) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 89876) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| docker (PID 89911) rss_mb | MB | 1 | 22.453 | 22.453 | 22.453 | 22.453 | n/a | n/a |
| docker (PID 89911) vms_mb | MB | 1 | 1524.203 | 1524.203 | 1524.203 | 1524.203 | n/a | n/a |
| docker (PID 89927) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 89927) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 89927) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 89927) rss_mb | MB | 3 | 27.052 | 26.852 | 27.152 | 27.152 | n/a | n/a |
| docker (PID 89927) vms_mb | MB | 3 | 1756.779 | 1660.773 | 1804.781 | 1804.781 | n/a | n/a |
| docker-init [alex_0000] (PID 89968) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [alex_0000] (PID 89968) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [alex_0000] (PID 89968) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 89982) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 89982) rss_mb | MB | 3 | 1.691 | 1.691 | 1.691 | 1.691 | n/a | n/a |
| tail [alex_0000] (PID 89982) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 90019) rss_mb | MB | 1 | 6.461 | 6.461 | 6.461 | 6.461 | n/a | n/a |
| docker (PID 90019) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 90047) rss_mb | MB | 1 | 26.953 | 26.953 | 26.953 | 26.953 | n/a | n/a |
| docker (PID 90047) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 90065) rss_mb | MB | 1 | 11.410 | 11.410 | 11.410 | 11.410 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 90065) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 90080) rss_mb | MB | 1 | 27.375 | 27.375 | 27.375 | 27.375 | n/a | n/a |
| docker (PID 90080) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 90117) rss_mb | MB | 1 | 25.918 | 25.918 | 25.918 | 25.918 | n/a | n/a |
| docker (PID 90117) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 90169) rss_mb | MB | 1 | 25.734 | 25.734 | 25.734 | 25.734 | n/a | n/a |
| docker (PID 90169) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 90177) rss_mb | MB | 1 | 26.840 | 26.840 | 26.840 | 26.840 | n/a | n/a |
| docker (PID 90177) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 90218) CPU | percent | 3 | 6.555 | 0.000 | 19.666 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 90218) rss_mb | MB | 4 | 3.587 | 0.633 | 12.449 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 90218) vms_mb | MB | 4 | 393.473 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 90231) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 90231) rss_mb | MB | 3 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [alex_0000] (PID 90231) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 90241) rss_mb | MB | 1 | 27.254 | 27.254 | 27.254 | 27.254 | n/a | n/a |
| docker (PID 90241) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 90261) rss_mb | MB | 1 | 10.438 | 10.438 | 10.438 | 10.438 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 90261) vms_mb | MB | 1 | 1641.449 | 1641.449 | 1641.449 | 1641.449 | n/a | n/a |
| docker (PID 90334) rss_mb | MB | 1 | 23.180 | 23.180 | 23.180 | 23.180 | n/a | n/a |
| docker (PID 90334) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 90342) rss_mb | MB | 1 | 26.844 | 26.844 | 26.844 | 26.844 | n/a | n/a |
| docker (PID 90342) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 90402) rss_mb | MB | 1 | 18.309 | 18.309 | 18.309 | 18.309 | n/a | n/a |
| docker (PID 90402) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 90425) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 90425) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 90425) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 90425) rss_mb | MB | 38 | 25.848 | 25.848 | 25.848 | 25.848 | n/a | n/a |
| docker (PID 90425) vms_mb | MB | 38 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 90441) rss_mb | MB | 1 | 25.383 | 25.383 | 25.383 | 25.383 | n/a | n/a |
| docker (PID 90441) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 90467) CPU | percent | 1 | 9.878 | 9.878 | 9.878 | 9.878 | 0.010000 CPU seconds | n/a |
| docker (PID 90467) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 90467) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 90467) rss_mb | MB | 2 | 13.193 | 0.414 | 25.973 | 25.973 | n/a | n/a |
| docker (PID 90467) vms_mb | MB | 2 | 846.480 | 32.750 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 90507) CPU | percent | 3 | 3.277 | 0.000 | 9.831 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 90507) rss_mb | MB | 4 | 3.502 | 0.633 | 12.109 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 90507) vms_mb | MB | 4 | 375.347 | 1.055 | 1498.223 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 90518) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 90518) rss_mb | MB | 3 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [alex_0000] (PID 90518) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 90528) rss_mb | MB | 1 | 27.250 | 27.250 | 27.250 | 27.250 | n/a | n/a |
| docker (PID 90528) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 90557) rss_mb | MB | 1 | 27.070 | 27.070 | 27.070 | 27.070 | n/a | n/a |
| docker (PID 90557) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 90625) rss_mb | MB | 1 | 20.414 | 20.414 | 20.414 | 20.414 | n/a | n/a |
| docker (PID 90625) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 90633) rss_mb | MB | 1 | 25.812 | 25.812 | 25.812 | 25.812 | n/a | n/a |
| docker (PID 90633) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 90692) rss_mb | MB | 1 | 25.824 | 25.824 | 25.824 | 25.824 | n/a | n/a |
| docker (PID 90692) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 90732) CPU | percent | 10 | 2.945 | 0.000 | 29.450 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 90732) rss_mb | MB | 11 | 1.593 | 0.633 | 11.195 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 90732) vms_mb | MB | 11 | 143.636 | 1.055 | 1569.445 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 90744) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 90744) rss_mb | MB | 10 | 1.727 | 1.727 | 1.727 | 1.727 | n/a | n/a |
| tail [alex_0000] (PID 90744) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 90754) rss_mb | MB | 1 | 16.207 | 16.207 | 16.207 | 16.207 | n/a | n/a |
| docker (PID 90754) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 90782) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 90782) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 90782) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 90782) rss_mb | MB | 8 | 27.090 | 27.090 | 27.090 | 27.090 | n/a | n/a |
| docker (PID 90782) vms_mb | MB | 8 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 90802) CPU | percent | 7 | 1.402 | 0.000 | 9.816 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 90802) rss_mb | MB | 8 | 4.395 | 3.332 | 11.836 | 3.332 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 90802) vms_mb | MB | 8 | 209.152 | 4.391 | 1642.480 | 4.391 | n/a | n/a |
| python [alex_0000] (PID 90812) CPU | percent | 6 | 99.697 | 88.209 | 107.901 | 107.901 | 0.610000 CPU seconds | n/a |
| python [alex_0000] (PID 90812) rss_mb | MB | 7 | 32.075 | 18.371 | 41.938 | 41.938 | n/a | n/a |
| python [alex_0000] (PID 90812) vms_mb | MB | 7 | 38.586 | 23.074 | 51.238 | 51.238 | n/a | n/a |
| docker (PID 90814) rss_mb | MB | 1 | 15.457 | 15.457 | 15.457 | 15.457 | n/a | n/a |
| docker (PID 90814) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 90822) rss_mb | MB | 1 | 25.922 | 25.922 | 25.922 | 25.922 | n/a | n/a |
| docker (PID 90822) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 90881) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 90881) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 90881) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 90881) rss_mb | MB | 2 | 27.047 | 27.047 | 27.047 | 27.047 | n/a | n/a |
| docker (PID 90881) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 90921) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 90921) rss_mb | MB | 3 | 4.695 | 0.633 | 12.820 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 90921) vms_mb | MB | 3 | 524.195 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 90934) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 90934) rss_mb | MB | 2 | 1.688 | 1.688 | 1.688 | 1.688 | n/a | n/a |
| tail [alex_0000] (PID 90934) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 90970) rss_mb | MB | 1 | 3.359 | 3.359 | 3.359 | 3.359 | n/a | n/a |
| docker (PID 90970) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 91006) rss_mb | MB | 1 | 27.195 | 27.195 | 27.195 | 27.195 | n/a | n/a |
| docker (PID 91006) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 91042) rss_mb | MB | 1 | 26.137 | 26.137 | 26.137 | 26.137 | n/a | n/a |
| docker (PID 91042) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 91085) rss_mb | MB | 1 | 15.102 | 15.102 | 15.102 | 15.102 | n/a | n/a |
| docker (PID 91085) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 91094) rss_mb | MB | 1 | 9.090 | 9.090 | 9.090 | 9.090 | n/a | n/a |
| docker (PID 91094) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 91118) rss_mb | MB | 1 | 25.691 | 25.691 | 25.691 | 25.691 | n/a | n/a |
| docker (PID 91118) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 91126) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 91126) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 91126) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 91126) rss_mb | MB | 39 | 26.820 | 26.820 | 26.820 | 26.820 | n/a | n/a |
| docker (PID 91126) vms_mb | MB | 39 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 91151) rss_mb | MB | 1 | 23.812 | 23.812 | 23.812 | 23.812 | n/a | n/a |
| docker (PID 91151) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| python3 (PID 91175) CPU | percent | 2 | 98.858 | 98.760 | 98.956 | 98.956 | 0.200000 CPU seconds | n/a |
| python3 (PID 91175) io read MB/s | MB/s | 2 | 0.058 | 0.000 | 0.116 | 0.116 | 0.011719 MB | n/a |
| python3 (PID 91175) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 91175) rss_mb | MB | 3 | 26.902 | 19.602 | 33.574 | 33.574 | n/a | n/a |
| python3 (PID 91175) vms_mb | MB | 3 | 50.487 | 44.059 | 56.461 | 56.461 | n/a | n/a |
| docker (PID 91196) rss_mb | MB | 1 | 26.004 | 26.004 | 26.004 | 26.004 | n/a | n/a |
| docker (PID 91196) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 91226) CPU | percent | 2 | 4.939 | 0.000 | 9.877 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 91226) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 91226) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 91226) rss_mb | MB | 3 | 20.579 | 6.559 | 27.590 | 27.590 | n/a | n/a |
| docker (PID 91226) vms_mb | MB | 3 | 1166.105 | 32.762 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [andy_0000] (PID 91267) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 91267) rss_mb | MB | 4 | 3.675 | 0.633 | 12.801 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 91267) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 91280) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 91280) rss_mb | MB | 3 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [andy_0000] (PID 91280) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 91308) rss_mb | MB | 1 | 2.535 | 2.535 | 2.535 | 2.535 | n/a | n/a |
| docker (PID 91308) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 91343) rss_mb | MB | 1 | 26.191 | 26.191 | 26.191 | 26.191 | n/a | n/a |
| docker (PID 91343) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 91378) rss_mb | MB | 1 | 27.328 | 27.328 | 27.328 | 27.328 | n/a | n/a |
| docker (PID 91378) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 91398) rss_mb | MB | 1 | 11.023 | 11.023 | 11.023 | 11.023 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 91398) vms_mb | MB | 1 | 1641.836 | 1641.836 | 1641.836 | 1641.836 | n/a | n/a |
| docker (PID 91415) rss_mb | MB | 1 | 26.027 | 26.027 | 26.027 | 26.027 | n/a | n/a |
| docker (PID 91415) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 91472) rss_mb | MB | 1 | 25.551 | 25.551 | 25.551 | 25.551 | n/a | n/a |
| docker (PID 91472) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 91515) CPU | percent | 3 | 6.531 | 0.000 | 19.592 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 91515) rss_mb | MB | 4 | 3.301 | 0.633 | 11.305 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 91515) vms_mb | MB | 4 | 393.215 | 1.055 | 1569.695 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 91527) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 91527) rss_mb | MB | 3 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [andy_0000] (PID 91527) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 91537) rss_mb | MB | 1 | 26.359 | 26.359 | 26.359 | 26.359 | n/a | n/a |
| docker (PID 91537) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 91563) rss_mb | MB | 1 | 27.395 | 27.395 | 27.395 | 27.395 | n/a | n/a |
| docker (PID 91563) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 91583) rss_mb | MB | 1 | 12.199 | 12.199 | 12.199 | 12.199 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 91583) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 91629) rss_mb | MB | 1 | 1.879 | 1.879 | 1.879 | 1.879 | n/a | n/a |
| docker (PID 91629) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 91637) rss_mb | MB | 1 | 26.074 | 26.074 | 26.074 | 26.074 | n/a | n/a |
| docker (PID 91637) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 91686) rss_mb | MB | 1 | 25.633 | 25.633 | 25.633 | 25.633 | n/a | n/a |
| docker (PID 91686) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 91694) rss_mb | MB | 1 | 26.645 | 26.645 | 26.645 | 26.645 | n/a | n/a |
| docker (PID 91694) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 91731) CPU | percent | 2 | 4.898 | 0.000 | 9.797 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 91731) rss_mb | MB | 3 | 4.349 | 0.633 | 11.781 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 91731) vms_mb | MB | 3 | 523.983 | 1.055 | 1569.840 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 91744) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 91744) rss_mb | MB | 2 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [andy_0000] (PID 91744) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 91756) rss_mb | MB | 1 | 27.094 | 27.094 | 27.094 | 27.094 | n/a | n/a |
| docker (PID 91756) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 91783) rss_mb | MB | 1 | 27.301 | 27.301 | 27.301 | 27.301 | n/a | n/a |
| docker (PID 91783) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [andy_0000] (PID 91802) rss_mb | MB | 1 | 3.375 | 3.375 | 3.375 | 3.375 | n/a | n/a |
| bash [andy_0000] (PID 91802) vms_mb | MB | 1 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| bash [andy_0000] (PID 91809) rss_mb | MB | 1 | 1.688 | 1.688 | 1.688 | 1.688 | n/a | n/a |
| bash [andy_0000] (PID 91809) vms_mb | MB | 1 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| docker (PID 91824) rss_mb | MB | 1 | 26.121 | 26.121 | 26.121 | 26.121 | n/a | n/a |
| docker (PID 91824) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 91884) CPU | percent | 1 | 9.881 | 9.881 | 9.881 | 9.881 | 0.010000 CPU seconds | n/a |
| docker (PID 91884) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 91884) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 91884) rss_mb | MB | 2 | 17.943 | 8.832 | 27.055 | 27.055 | n/a | n/a |
| docker (PID 91884) vms_mb | MB | 2 | 1444.104 | 1227.434 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 91921) CPU | percent | 2 | 4.915 | 0.000 | 9.830 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 91921) rss_mb | MB | 3 | 4.633 | 0.633 | 12.633 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 91921) vms_mb | MB | 3 | 524.279 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 91934) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 91934) rss_mb | MB | 2 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [andy_0000] (PID 91934) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 91944) rss_mb | MB | 1 | 27.367 | 27.367 | 27.367 | 27.367 | n/a | n/a |
| docker (PID 91944) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 91971) rss_mb | MB | 1 | 27.207 | 27.207 | 27.207 | 27.207 | n/a | n/a |
| docker (PID 91971) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| bash [andy_0000] (PID 91991) rss_mb | MB | 1 | 3.320 | 3.320 | 3.320 | 3.320 | n/a | n/a |
| bash [andy_0000] (PID 91991) vms_mb | MB | 1 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| rg [andy_0000] (PID 92000) rss_mb | MB | 1 | 2.066 | 2.066 | 2.066 | 2.066 | n/a | n/a |
| rg [andy_0000] (PID 92000) vms_mb | MB | 1 | 8.234 | 8.234 | 8.234 | 8.234 | n/a | n/a |
| docker (PID 92014) rss_mb | MB | 1 | 26.152 | 26.152 | 26.152 | 26.152 | n/a | n/a |
| docker (PID 92014) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 92074) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 92074) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 92074) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 92074) rss_mb | MB | 2 | 23.086 | 20.320 | 25.852 | 25.852 | n/a | n/a |
| docker (PID 92074) vms_mb | MB | 2 | 1588.205 | 1516.199 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 92114) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 92114) rss_mb | MB | 4 | 3.681 | 0.633 | 12.824 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 92114) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 92126) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 92126) rss_mb | MB | 3 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [andy_0000] (PID 92126) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 92136) rss_mb | MB | 1 | 27.176 | 27.176 | 27.176 | 27.176 | n/a | n/a |
| docker (PID 92136) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 92154) rss_mb | MB | 1 | 11.363 | 11.363 | 11.363 | 11.363 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 92154) vms_mb | MB | 1 | 1570.098 | 1570.098 | 1570.098 | 1570.098 | n/a | n/a |
| docker (PID 92188) rss_mb | MB | 1 | 21.410 | 21.410 | 21.410 | 21.410 | n/a | n/a |
| docker (PID 92188) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 92232) rss_mb | MB | 1 | 26.008 | 26.008 | 26.008 | 26.008 | n/a | n/a |
| docker (PID 92232) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 92299) rss_mb | MB | 1 | 26.859 | 26.859 | 26.859 | 26.859 | n/a | n/a |
| docker (PID 92299) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 92313) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 92313) io read MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 92313) io write MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 92313) rss_mb | MB | 37 | 26.730 | 26.730 | 26.730 | 26.730 | n/a | n/a |
| docker (PID 92313) vms_mb | MB | 37 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 92329) rss_mb | MB | 1 | 25.078 | 25.078 | 25.078 | 25.078 | n/a | n/a |
| docker (PID 92329) vms_mb | MB | 1 | 1587.957 | 1587.957 | 1587.957 | 1587.957 | n/a | n/a |
| docker (PID 92356) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 92356) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 92356) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 92356) rss_mb | MB | 2 | 25.633 | 25.633 | 25.633 | 25.633 | n/a | n/a |
| docker (PID 92356) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [andy_0000] (PID 92396) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 92396) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 92396) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 92408) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 92408) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [andy_0000] (PID 92408) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 92445) rss_mb | MB | 1 | 22.453 | 22.453 | 22.453 | 22.453 | n/a | n/a |
| docker (PID 92445) vms_mb | MB | 1 | 1524.203 | 1524.203 | 1524.203 | 1524.203 | n/a | n/a |
| docker (PID 92480) rss_mb | MB | 1 | 27.199 | 27.199 | 27.199 | 27.199 | n/a | n/a |
| docker (PID 92480) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 92520) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 92520) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 92520) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 92520) rss_mb | MB | 2 | 25.863 | 25.863 | 25.863 | 25.863 | n/a | n/a |
| docker (PID 92520) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 92571) rss_mb | MB | 1 | 15.773 | 15.773 | 15.773 | 15.773 | n/a | n/a |
| docker (PID 92571) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 92579) rss_mb | MB | 1 | 27.027 | 27.027 | 27.027 | 27.027 | n/a | n/a |
| docker (PID 92579) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| 6 [andy_0000] (PID 92615) rss_mb | MB | 1 | 1.797 | 1.797 | 1.797 | 1.797 | n/a | n/a |
| 6 [andy_0000] (PID 92615) vms_mb | MB | 1 | 13.980 | 13.980 | 13.980 | 13.980 | n/a | n/a |
| docker-init [andy_0000] (PID 92619) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 92619) rss_mb | MB | 10 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 92619) vms_mb | MB | 10 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 92632) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 92632) rss_mb | MB | 10 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [andy_0000] (PID 92632) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 92642) rss_mb | MB | 1 | 2.621 | 2.621 | 2.621 | 2.621 | n/a | n/a |
| docker (PID 92642) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 92669) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 92669) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 92669) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 92669) rss_mb | MB | 9 | 27.359 | 27.359 | 27.359 | 27.359 | n/a | n/a |
| docker (PID 92669) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 92689) CPU | percent | 8 | 2.433 | 0.000 | 19.466 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 92689) rss_mb | MB | 9 | 4.277 | 3.480 | 10.648 | 3.480 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 92689) vms_mb | MB | 9 | 178.301 | 4.391 | 1569.582 | 4.391 | n/a | n/a |
| python [andy_0000] (PID 92698) CPU | percent | 7 | 100.827 | 97.932 | 107.913 | 107.913 | 0.720000 CPU seconds | n/a |
| python [andy_0000] (PID 92698) rss_mb | MB | 8 | 32.916 | 17.016 | 41.770 | 41.770 | n/a | n/a |
| python [andy_0000] (PID 92698) vms_mb | MB | 8 | 39.968 | 21.480 | 51.238 | 51.238 | n/a | n/a |
| docker (PID 92708) rss_mb | MB | 1 | 25.883 | 25.883 | 25.883 | 25.883 | n/a | n/a |
| docker (PID 92708) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 92770) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 92770) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 92770) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 92770) rss_mb | MB | 2 | 25.648 | 25.648 | 25.648 | 25.648 | n/a | n/a |
| docker (PID 92770) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [andy_0000] (PID 92809) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 92809) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 92809) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 92821) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 92821) rss_mb | MB | 3 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [andy_0000] (PID 92821) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 92859) rss_mb | MB | 1 | 18.613 | 18.613 | 18.613 | 18.613 | n/a | n/a |
| docker (PID 92859) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 92896) rss_mb | MB | 1 | 27.457 | 27.457 | 27.457 | 27.457 | n/a | n/a |
| docker (PID 92896) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[0:PARENT] [andy_0000] (PID 92911) rss_mb | MB | 1 | 1.980 | 1.980 | 1.980 | 1.980 | n/a | n/a |
| runc:[0:PARENT] [andy_0000] (PID 92911) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| docker (PID 92933) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 92933) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 92933) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 92933) rss_mb | MB | 2 | 27.133 | 27.133 | 27.133 | 27.133 | n/a | n/a |
| docker (PID 92933) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 93008) rss_mb | MB | 1 | 25.527 | 25.527 | 25.527 | 25.527 | n/a | n/a |
| docker (PID 93008) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 93016) CPU | percent | 42 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 93016) io read MB/s | MB/s | 42 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 93016) io write MB/s | MB/s | 42 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 93016) rss_mb | MB | 43 | 27.133 | 27.133 | 27.133 | 27.133 | n/a | n/a |
| docker (PID 93016) vms_mb | MB | 43 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 93044) rss_mb | MB | 1 | 25.223 | 25.223 | 25.223 | 25.223 | n/a | n/a |
| docker (PID 93044) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| python3 (PID 93067) CPU | percent | 3 | 95.574 | 88.943 | 98.949 | 98.949 | 0.290000 CPU seconds | n/a |
| python3 (PID 93067) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 93067) io write MB/s | MB/s | 3 | 0.722 | 0.000 | 2.165 | 2.165 | 0.218750 MB | n/a |
| python3 (PID 93067) rss_mb | MB | 4 | 22.736 | 5.242 | 34.395 | 34.395 | n/a | n/a |
| python3 (PID 93067) vms_mb | MB | 4 | 47.828 | 34.922 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 93097) rss_mb | MB | 1 | 24.727 | 24.727 | 24.727 | 24.727 | n/a | n/a |
| docker (PID 93097) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 93105) rss_mb | MB | 1 | 19.891 | 19.891 | 19.891 | 19.891 | n/a | n/a |
| docker (PID 93105) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 93120) CPU | percent | 1 | 19.588 | 19.588 | 19.588 | 19.588 | 0.020000 CPU seconds | n/a |
| docker (PID 93120) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 93120) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 93120) rss_mb | MB | 2 | 27.340 | 27.059 | 27.621 | 27.621 | n/a | n/a |
| docker (PID 93120) vms_mb | MB | 2 | 1696.775 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [arch_0000] (PID 93161) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [arch_0000] (PID 93161) rss_mb | MB | 4 | 3.541 | 0.633 | 12.266 | 0.633 | n/a | n/a |
| docker-init [arch_0000] (PID 93161) vms_mb | MB | 4 | 411.411 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 93175) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 93175) rss_mb | MB | 3 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [arch_0000] (PID 93175) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 93177) rss_mb | MB | 1 | 27.117 | 27.117 | 27.117 | 27.117 | n/a | n/a |
| docker (PID 93177) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] (PID 93196) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[2:INIT] (PID 93196) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| docker (PID 93239) rss_mb | MB | 1 | 17.004 | 17.004 | 17.004 | 17.004 | n/a | n/a |
| docker (PID 93239) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 93273) rss_mb | MB | 1 | 27.352 | 27.352 | 27.352 | 27.352 | n/a | n/a |
| docker (PID 93273) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 93309) rss_mb | MB | 1 | 26.141 | 26.141 | 26.141 | 26.141 | n/a | n/a |
| docker (PID 93309) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 93353) rss_mb | MB | 1 | 7.848 | 7.848 | 7.848 | 7.848 | n/a | n/a |
| docker (PID 93353) vms_mb | MB | 1 | 32.867 | 32.867 | 32.867 | 32.867 | n/a | n/a |
| docker (PID 93370) rss_mb | MB | 1 | 25.527 | 25.527 | 25.527 | 25.527 | n/a | n/a |
| docker (PID 93370) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| 6 [arch_0000] (PID 93405) rss_mb | MB | 1 | 1.812 | 1.812 | 1.812 | 1.812 | n/a | n/a |
| 6 [arch_0000] (PID 93405) vms_mb | MB | 1 | 13.980 | 13.980 | 13.980 | 13.980 | n/a | n/a |
| docker-init [arch_0000] (PID 93408) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [arch_0000] (PID 93408) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [arch_0000] (PID 93408) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 93421) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 93421) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [arch_0000] (PID 93421) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 93432) rss_mb | MB | 1 | 6.574 | 6.574 | 6.574 | 6.574 | n/a | n/a |
| docker (PID 93432) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 93459) rss_mb | MB | 1 | 27.434 | 27.434 | 27.434 | 27.434 | n/a | n/a |
| docker (PID 93459) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 93480) rss_mb | MB | 1 | 11.117 | 11.117 | 11.117 | 11.117 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 93480) vms_mb | MB | 1 | 1569.840 | 1569.840 | 1569.840 | 1569.840 | n/a | n/a |
| docker (PID 93495) rss_mb | MB | 1 | 26.875 | 26.875 | 26.875 | 26.875 | n/a | n/a |
| docker (PID 93495) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 93515) rss_mb | MB | 1 | 12.219 | 12.219 | 12.219 | 12.219 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 93515) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 93532) rss_mb | MB | 1 | 25.906 | 25.906 | 25.906 | 25.906 | n/a | n/a |
| docker (PID 93532) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 93592) rss_mb | MB | 1 | 27.051 | 27.051 | 27.051 | 27.051 | n/a | n/a |
| docker (PID 93592) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 93614) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 93614) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 93614) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 93614) rss_mb | MB | 38 | 25.793 | 25.793 | 25.793 | 25.793 | n/a | n/a |
| docker (PID 93614) vms_mb | MB | 38 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 93630) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 93630) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 93657) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 93657) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 93657) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 93657) rss_mb | MB | 2 | 26.895 | 26.895 | 26.895 | 26.895 | n/a | n/a |
| docker (PID 93657) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [arch_0000] (PID 93695) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [arch_0000] (PID 93695) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [arch_0000] (PID 93695) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 93708) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 93708) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [arch_0000] (PID 93708) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 93746) rss_mb | MB | 1 | 6.340 | 6.340 | 6.340 | 6.340 | n/a | n/a |
| docker (PID 93746) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 93783) rss_mb | MB | 1 | 26.980 | 26.980 | 26.980 | 26.980 | n/a | n/a |
| docker (PID 93783) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 93821) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 93821) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 93821) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 93821) rss_mb | MB | 2 | 26.012 | 26.012 | 26.012 | 26.012 | n/a | n/a |
| docker (PID 93821) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 93882) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 93882) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 93882) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 93882) rss_mb | MB | 2 | 26.652 | 26.652 | 26.652 | 26.652 | n/a | n/a |
| docker (PID 93882) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 93921) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 93921) rss_mb | MB | 11 | 1.729 | 0.633 | 12.695 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 93921) vms_mb | MB | 11 | 137.161 | 1.055 | 1498.223 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 93934) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 93934) rss_mb | MB | 10 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [arch_0000] (PID 93934) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 93944) rss_mb | MB | 1 | 27.617 | 27.617 | 27.617 | 27.617 | n/a | n/a |
| docker (PID 93944) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 93963) rss_mb | MB | 1 | 12.418 | 12.418 | 12.418 | 12.418 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 93963) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 93971) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 93971) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 93971) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 93971) rss_mb | MB | 9 | 27.340 | 27.340 | 27.340 | 27.340 | n/a | n/a |
| docker (PID 93971) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [arch_0000] (PID 93990) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [arch_0000] (PID 93990) rss_mb | MB | 9 | 3.340 | 3.340 | 3.340 | 3.340 | n/a | n/a |
| bash [arch_0000] (PID 93990) vms_mb | MB | 9 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [arch_0000] (PID 93999) CPU | percent | 8 | 100.398 | 97.432 | 107.824 | 107.824 | 0.820000 CPU seconds | n/a |
| python [arch_0000] (PID 93999) rss_mb | MB | 9 | 31.544 | 10.844 | 41.547 | 41.547 | n/a | n/a |
| python [arch_0000] (PID 93999) vms_mb | MB | 9 | 39.313 | 14.766 | 51.219 | 51.219 | n/a | n/a |
| docker (PID 94009) rss_mb | MB | 1 | 25.645 | 25.645 | 25.645 | 25.645 | n/a | n/a |
| docker (PID 94009) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 94061) rss_mb | MB | 1 | 25.402 | 25.402 | 25.402 | 25.402 | n/a | n/a |
| docker (PID 94061) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [arch_0000] (PID 94101) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [arch_0000] (PID 94101) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [arch_0000] (PID 94101) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 94114) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 94114) rss_mb | MB | 3 | 1.727 | 1.727 | 1.727 | 1.727 | n/a | n/a |
| tail [arch_0000] (PID 94114) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 94117) rss_mb | MB | 1 | 26.051 | 26.051 | 26.051 | 26.051 | n/a | n/a |
| docker (PID 94117) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 94151) rss_mb | MB | 1 | 27.512 | 27.512 | 27.512 | 27.512 | n/a | n/a |
| docker (PID 94151) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 94171) rss_mb | MB | 1 | 10.781 | 10.781 | 10.781 | 10.781 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 94171) vms_mb | MB | 1 | 1641.578 | 1641.578 | 1641.578 | 1641.578 | n/a | n/a |
| docker (PID 94187) rss_mb | MB | 1 | 27.527 | 27.527 | 27.527 | 27.527 | n/a | n/a |
| docker (PID 94187) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 94206) rss_mb | MB | 1 | 11.484 | 11.484 | 11.484 | 11.484 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 94206) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 94223) rss_mb | MB | 1 | 26.129 | 26.129 | 26.129 | 26.129 | n/a | n/a |
| docker (PID 94223) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 94300) rss_mb | MB | 1 | 25.371 | 25.371 | 25.371 | 25.371 | n/a | n/a |
| docker (PID 94300) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 94308) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 94308) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 94308) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 94308) rss_mb | MB | 38 | 25.602 | 25.602 | 25.602 | 25.602 | n/a | n/a |
| docker (PID 94308) vms_mb | MB | 38 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 94341) rss_mb | MB | 1 | 25.656 | 25.656 | 25.656 | 25.656 | n/a | n/a |
| docker (PID 94341) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| python3 (PID 94357) CPU | percent | 3 | 102.122 | 98.906 | 108.529 | 98.906 | 0.310000 CPU seconds | n/a |
| python3 (PID 94357) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 94357) io write MB/s | MB/s | 3 | 0.786 | 0.000 | 2.357 | 2.357 | 0.238281 MB | n/a |
| python3 (PID 94357) rss_mb | MB | 4 | 27.766 | 16.836 | 34.516 | 34.516 | n/a | n/a |
| python3 (PID 94357) vms_mb | MB | 4 | 51.471 | 41.168 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 94370) rss_mb | MB | 1 | 8.543 | 8.543 | 8.543 | 8.543 | n/a | n/a |
| docker (PID 94370) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 94394) rss_mb | MB | 1 | 26.699 | 26.699 | 26.699 | 26.699 | n/a | n/a |
| docker (PID 94394) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 94408) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 94408) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 94408) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 94408) rss_mb | MB | 2 | 27.430 | 27.430 | 27.430 | 27.430 | n/a | n/a |
| docker (PID 94408) vms_mb | MB | 2 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [bake_0000] (PID 94450) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bake_0000] (PID 94450) rss_mb | MB | 4 | 3.704 | 0.633 | 12.918 | 0.633 | n/a | n/a |
| docker-init [bake_0000] (PID 94450) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 94463) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 94463) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [bake_0000] (PID 94463) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 94494) rss_mb | MB | 1 | 26.496 | 26.496 | 26.496 | 26.496 | n/a | n/a |
| docker (PID 94494) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 94529) rss_mb | MB | 1 | 26.820 | 26.820 | 26.820 | 26.820 | n/a | n/a |
| docker (PID 94529) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 94549) rss_mb | MB | 1 | 10.164 | 10.164 | 10.164 | 10.164 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 94549) vms_mb | MB | 1 | 1569.195 | 1569.195 | 1569.195 | 1569.195 | n/a | n/a |
| docker (PID 94564) rss_mb | MB | 1 | 27.195 | 27.195 | 27.195 | 27.195 | n/a | n/a |
| docker (PID 94564) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 94583) rss_mb | MB | 1 | 12.195 | 12.195 | 12.195 | 12.195 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 94583) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 94599) rss_mb | MB | 1 | 26.086 | 26.086 | 26.086 | 26.086 | n/a | n/a |
| docker (PID 94599) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 94657) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 94657) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 94657) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 94657) rss_mb | MB | 2 | 18.600 | 11.402 | 25.797 | 25.797 | n/a | n/a |
| docker (PID 94657) vms_mb | MB | 2 | 1555.955 | 1451.699 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 94696) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 94696) rss_mb | MB | 4 | 3.692 | 0.633 | 12.871 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 94696) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 94709) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 94709) rss_mb | MB | 3 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [bake_0000] (PID 94709) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 94720) rss_mb | MB | 1 | 27.047 | 27.047 | 27.047 | 27.047 | n/a | n/a |
| docker (PID 94720) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 94740) rss_mb | MB | 1 | 11.574 | 11.574 | 11.574 | 11.574 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 94740) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 94773) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 94773) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 94820) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 94820) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 94820) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 94820) rss_mb | MB | 2 | 23.631 | 20.359 | 26.902 | 26.902 | n/a | n/a |
| docker (PID 94820) vms_mb | MB | 2 | 1624.488 | 1588.203 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 94870) rss_mb | MB | 1 | 11.125 | 11.125 | 11.125 | 11.125 | n/a | n/a |
| docker (PID 94870) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 94878) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 94878) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 94878) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 94878) rss_mb | MB | 3 | 25.434 | 25.434 | 25.434 | 25.434 | n/a | n/a |
| docker (PID 94878) vms_mb | MB | 3 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 94916) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 94916) rss_mb | MB | 5 | 3.020 | 0.633 | 12.570 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 94916) vms_mb | MB | 5 | 300.488 | 1.055 | 1498.223 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 94928) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 94928) rss_mb | MB | 4 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [bake_0000] (PID 94928) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 94930) rss_mb | MB | 1 | 21.504 | 21.504 | 21.504 | 21.504 | n/a | n/a |
| docker (PID 94930) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 94938) rss_mb | MB | 1 | 27.340 | 27.340 | 27.340 | 27.340 | n/a | n/a |
| docker (PID 94938) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 94957) rss_mb | MB | 1 | 11.578 | 11.578 | 11.578 | 11.578 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 94957) vms_mb | MB | 1 | 1642.230 | 1642.230 | 1642.230 | 1642.230 | n/a | n/a |
| docker (PID 94991) rss_mb | MB | 1 | 20.195 | 20.195 | 20.195 | 20.195 | n/a | n/a |
| docker (PID 94991) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 95029) rss_mb | MB | 1 | 24.324 | 24.324 | 24.324 | 24.324 | n/a | n/a |
| docker (PID 95029) vms_mb | MB | 1 | 1588.270 | 1588.270 | 1588.270 | 1588.270 | n/a | n/a |
| docker (PID 95037) rss_mb | MB | 1 | 27.086 | 27.086 | 27.086 | 27.086 | n/a | n/a |
| docker (PID 95037) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 95115) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 95115) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 95115) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 95115) rss_mb | MB | 38 | 27.004 | 27.004 | 27.004 | 27.004 | n/a | n/a |
| docker (PID 95115) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 95157) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 95157) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 95157) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 95157) rss_mb | MB | 2 | 25.730 | 25.730 | 25.730 | 25.730 | n/a | n/a |
| docker (PID 95157) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 95198) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 95198) rss_mb | MB | 4 | 3.742 | 0.633 | 13.070 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 95198) vms_mb | MB | 4 | 411.411 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 95211) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 95211) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bake_0000] (PID 95211) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 95221) rss_mb | MB | 1 | 27.332 | 27.332 | 27.332 | 27.332 | n/a | n/a |
| docker (PID 95221) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| sh [bake_0000] (PID 95241) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sh [bake_0000] (PID 95241) vms_mb | MB | 1 | 0.516 | 0.516 | 0.516 | 0.516 | n/a | n/a |
| docker (PID 95285) rss_mb | MB | 1 | 8.680 | 8.680 | 8.680 | 8.680 | n/a | n/a |
| docker (PID 95285) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 95325) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 95325) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 95325) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 95325) rss_mb | MB | 2 | 26.059 | 26.059 | 26.059 | 26.059 | n/a | n/a |
| docker (PID 95325) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 95384) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 95384) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 95384) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 95384) rss_mb | MB | 2 | 15.840 | 6.215 | 25.465 | 25.465 | n/a | n/a |
| docker (PID 95384) vms_mb | MB | 2 | 846.486 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 95423) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 95423) rss_mb | MB | 11 | 1.741 | 0.633 | 12.820 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 95423) vms_mb | MB | 11 | 143.707 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 95436) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 95436) rss_mb | MB | 10 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [bake_0000] (PID 95436) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 95446) rss_mb | MB | 1 | 27.250 | 27.250 | 27.250 | 27.250 | n/a | n/a |
| docker (PID 95446) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 95465) rss_mb | MB | 1 | 12.039 | 12.039 | 12.039 | 12.039 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 95465) vms_mb | MB | 1 | 1714.734 | 1714.734 | 1714.734 | 1714.734 | n/a | n/a |
| docker (PID 95474) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 95474) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 95474) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 95474) rss_mb | MB | 8 | 27.684 | 27.684 | 27.684 | 27.684 | n/a | n/a |
| docker (PID 95474) vms_mb | MB | 8 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| bash [bake_0000] (PID 95495) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bake_0000] (PID 95495) rss_mb | MB | 8 | 3.359 | 3.359 | 3.359 | 3.359 | n/a | n/a |
| bash [bake_0000] (PID 95495) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bake_0000] (PID 95505) CPU | percent | 7 | 99.358 | 97.349 | 107.954 | 98.104 | 0.710000 CPU seconds | n/a |
| python [bake_0000] (PID 95505) rss_mb | MB | 8 | 30.345 | 7.887 | 41.426 | 41.426 | n/a | n/a |
| python [bake_0000] (PID 95505) vms_mb | MB | 8 | 37.245 | 12.070 | 50.375 | 50.375 | n/a | n/a |
| docker (PID 95515) rss_mb | MB | 1 | 25.883 | 25.883 | 25.883 | 25.883 | n/a | n/a |
| docker (PID 95515) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 95575) rss_mb | MB | 1 | 26.816 | 26.816 | 26.816 | 26.816 | n/a | n/a |
| docker (PID 95575) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker-init [bake_0000] (PID 95616) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bake_0000] (PID 95616) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bake_0000] (PID 95616) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 95628) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 95628) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [bake_0000] (PID 95628) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 95630) rss_mb | MB | 1 | 25.633 | 25.633 | 25.633 | 25.633 | n/a | n/a |
| docker (PID 95630) vms_mb | MB | 1 | 1596.211 | 1596.211 | 1596.211 | 1596.211 | n/a | n/a |
| docker (PID 95667) rss_mb | MB | 1 | 27.320 | 27.320 | 27.320 | 27.320 | n/a | n/a |
| docker (PID 95667) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 95703) rss_mb | MB | 1 | 27.332 | 27.332 | 27.332 | 27.332 | n/a | n/a |
| docker (PID 95703) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 95721) rss_mb | MB | 1 | 11.488 | 11.488 | 11.488 | 11.488 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 95721) vms_mb | MB | 1 | 1570.098 | 1570.098 | 1570.098 | 1570.098 | n/a | n/a |
| docker (PID 95737) rss_mb | MB | 1 | 25.965 | 25.965 | 25.965 | 25.965 | n/a | n/a |
| docker (PID 95737) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 95795) rss_mb | MB | 1 | 19.926 | 19.926 | 19.926 | 19.926 | n/a | n/a |
| docker (PID 95795) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 95813) rss_mb | MB | 1 | 19.238 | 19.238 | 19.238 | 19.238 | n/a | n/a |
| docker (PID 95813) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 95830) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 95830) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 95830) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 95830) rss_mb | MB | 39 | 25.672 | 25.672 | 25.672 | 25.672 | n/a | n/a |
| docker (PID 95830) vms_mb | MB | 39 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 95862) rss_mb | MB | 1 | 20.289 | 20.289 | 20.289 | 20.289 | n/a | n/a |
| docker (PID 95862) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| python3 (PID 95878) CPU | percent | 3 | 98.814 | 89.021 | 108.561 | 98.860 | 0.300000 CPU seconds | n/a |
| python3 (PID 95878) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 95878) io write MB/s | MB/s | 3 | 0.785 | 0.000 | 2.356 | 2.356 | 0.238281 MB | n/a |
| python3 (PID 95878) rss_mb | MB | 4 | 25.186 | 11.738 | 34.520 | 34.520 | n/a | n/a |
| python3 (PID 95878) vms_mb | MB | 4 | 49.572 | 38.035 | 57.434 | 57.434 | n/a | n/a |
| docker (PID 95899) rss_mb | MB | 1 | 25.855 | 25.855 | 25.855 | 25.855 | n/a | n/a |
| docker (PID 95899) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 95929) CPU | percent | 2 | 4.932 | 0.000 | 9.865 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 95929) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 95929) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 95929) rss_mb | MB | 3 | 19.318 | 3.555 | 27.199 | 27.199 | n/a | n/a |
| docker (PID 95929) vms_mb | MB | 3 | 1166.105 | 32.762 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [bale_0000] (PID 95969) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bale_0000] (PID 95969) rss_mb | MB | 4 | 3.723 | 0.633 | 12.992 | 0.633 | n/a | n/a |
| docker-init [bale_0000] (PID 95969) vms_mb | MB | 4 | 411.411 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 95983) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 95983) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [bale_0000] (PID 95983) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 96011) rss_mb | MB | 1 | 23.023 | 23.023 | 23.023 | 23.023 | n/a | n/a |
| docker (PID 96011) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 96048) rss_mb | MB | 1 | 27.340 | 27.340 | 27.340 | 27.340 | n/a | n/a |
| docker (PID 96048) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 96082) rss_mb | MB | 1 | 27.520 | 27.520 | 27.520 | 27.520 | n/a | n/a |
| docker (PID 96082) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 96102) rss_mb | MB | 1 | 11.867 | 11.867 | 11.867 | 11.867 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 96102) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 96118) rss_mb | MB | 1 | 26.086 | 26.086 | 26.086 | 26.086 | n/a | n/a |
| docker (PID 96118) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 96168) rss_mb | MB | 1 | 17.812 | 17.812 | 17.812 | 17.812 | n/a | n/a |
| docker (PID 96168) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 96176) rss_mb | MB | 1 | 25.590 | 25.590 | 25.590 | 25.590 | n/a | n/a |
| docker (PID 96176) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 96215) CPU | percent | 3 | 6.522 | 0.000 | 19.565 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 96215) rss_mb | MB | 4 | 3.524 | 0.633 | 12.199 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 96215) vms_mb | MB | 4 | 393.376 | 1.055 | 1570.340 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 96229) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 96229) rss_mb | MB | 3 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [bale_0000] (PID 96229) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 96240) rss_mb | MB | 1 | 27.375 | 27.375 | 27.375 | 27.375 | n/a | n/a |
| docker (PID 96240) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 96271) rss_mb | MB | 1 | 27.477 | 27.477 | 27.477 | 27.477 | n/a | n/a |
| docker (PID 96271) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 96334) rss_mb | MB | 1 | 3.781 | 3.781 | 3.781 | 3.781 | n/a | n/a |
| docker (PID 96334) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 96342) rss_mb | MB | 1 | 27.188 | 27.188 | 27.188 | 27.188 | n/a | n/a |
| docker (PID 96342) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 96411) rss_mb | MB | 1 | 16.621 | 16.621 | 16.621 | 16.621 | n/a | n/a |
| docker (PID 96411) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 96425) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 96425) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 96425) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 96425) rss_mb | MB | 38 | 26.816 | 26.816 | 26.816 | 26.816 | n/a | n/a |
| docker (PID 96425) vms_mb | MB | 38 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 96460) rss_mb | MB | 1 | 22.719 | 22.719 | 22.719 | 22.719 | n/a | n/a |
| docker (PID 96460) vms_mb | MB | 1 | 1524.203 | 1524.203 | 1524.203 | 1524.203 | n/a | n/a |
| docker (PID 96468) CPU | percent | 3 | 13.026 | 0.000 | 39.077 | 0.000 | 0.040000 CPU seconds | n/a |
| docker (PID 96468) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 96468) io write MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 96468) rss_mb | MB | 4 | 23.403 | 16.621 | 25.664 | 25.664 | n/a | n/a |
| docker (PID 96468) vms_mb | MB | 4 | 1624.083 | 1515.699 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[0:PARENT] [bale_0000] (PID 96504) rss_mb | MB | 1 | 1.957 | 1.957 | 1.957 | 1.957 | n/a | n/a |
| runc:[0:PARENT] [bale_0000] (PID 96504) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[1:CHILD] [bale_0000] (PID 96506) rss_mb | MB | 1 | 0.660 | 0.660 | 0.660 | 0.660 | n/a | n/a |
| runc:[1:CHILD] [bale_0000] (PID 96506) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 96507) CPU | percent | 6 | 1.603 | 0.000 | 9.616 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 96507) rss_mb | MB | 7 | 2.379 | 0.633 | 12.855 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 96507) vms_mb | MB | 7 | 225.258 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 96520) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 96520) rss_mb | MB | 6 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bale_0000] (PID 96520) vms_mb | MB | 6 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| run9:repair_bug (PID 96523) rss_mb | MB | 1 | 687.434 | 687.434 | 687.434 | 687.434 | n/a | n/a |
| run9:repair_bug (PID 96523) vms_mb | MB | 1 | 3754.559 | 3754.559 | 3754.559 | 3754.559 | n/a | n/a |
| docker (PID 96532) CPU | percent | 1 | 58.700 | 58.700 | 58.700 | 58.700 | 0.060000 CPU seconds | n/a |
| docker (PID 96532) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 96532) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 96532) rss_mb | MB | 2 | 14.529 | 2.348 | 26.711 | 26.711 | n/a | n/a |
| docker (PID 96532) vms_mb | MB | 2 | 846.768 | 32.762 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 96550) rss_mb | MB | 1 | 10.285 | 10.285 | 10.285 | 10.285 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 96550) vms_mb | MB | 1 | 1641.449 | 1641.449 | 1641.449 | 1641.449 | n/a | n/a |
| docker (PID 96559) rss_mb | MB | 1 | 27.395 | 27.395 | 27.395 | 27.395 | n/a | n/a |
| docker (PID 96559) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 96578) rss_mb | MB | 1 | 11.836 | 11.836 | 11.836 | 11.836 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 96578) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 96595) rss_mb | MB | 1 | 25.441 | 25.441 | 25.441 | 25.441 | n/a | n/a |
| docker (PID 96595) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 96625) rss_mb | MB | 1 | 5.660 | 5.660 | 5.660 | 5.660 | n/a | n/a |
| docker (PID 96625) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 96633) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 96633) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 96633) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 96633) rss_mb | MB | 2 | 26.875 | 26.875 | 26.875 | 26.875 | n/a | n/a |
| docker (PID 96633) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 96684) rss_mb | MB | 1 | 19.500 | 19.500 | 19.500 | 19.500 | n/a | n/a |
| docker (PID 96684) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 96693) rss_mb | MB | 1 | 26.973 | 26.973 | 26.973 | 26.973 | n/a | n/a |
| docker (PID 96693) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 96733) CPU | percent | 37 | 0.528 | 0.000 | 19.525 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 96733) rss_mb | MB | 38 | 0.904 | 0.633 | 10.930 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 96733) vms_mb | MB | 38 | 42.322 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 96746) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 96746) rss_mb | MB | 37 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bale_0000] (PID 96746) vms_mb | MB | 37 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 96756) rss_mb | MB | 1 | 25.738 | 25.738 | 25.738 | 25.738 | n/a | n/a |
| docker (PID 96756) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 96785) CPU | percent | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 96785) io read MB/s | MB/s | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 96785) io write MB/s | MB/s | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 96785) rss_mb | MB | 35 | 27.227 | 27.227 | 27.227 | 27.227 | n/a | n/a |
| docker (PID 96785) vms_mb | MB | 35 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 96808) CPU | percent | 34 | 0.576 | 0.000 | 19.599 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 96808) rss_mb | MB | 35 | 3.573 | 3.340 | 11.488 | 3.340 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 96808) vms_mb | MB | 35 | 49.129 | 4.391 | 1570.227 | 4.391 | n/a | n/a |
| python [bale_0000] (PID 96817) CPU | percent | 33 | 99.804 | 97.121 | 107.960 | 97.792 | 3.370000 CPU seconds | n/a |
| python [bale_0000] (PID 96817) rss_mb | MB | 34 | 39.779 | 18.273 | 41.797 | 41.797 | n/a | n/a |
| python [bale_0000] (PID 96817) vms_mb | MB | 34 | 48.763 | 23.297 | 51.324 | 51.324 | n/a | n/a |
| docker (PID 96819) rss_mb | MB | 1 | 24.059 | 24.059 | 24.059 | 24.059 | n/a | n/a |
| docker (PID 96819) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 96827) rss_mb | MB | 1 | 25.996 | 25.996 | 25.996 | 25.996 | n/a | n/a |
| docker (PID 96827) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 96888) rss_mb | MB | 1 | 26.594 | 26.594 | 26.594 | 26.594 | n/a | n/a |
| docker (PID 96888) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| 6 [bale_0000] (PID 96925) rss_mb | MB | 1 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| 6 [bale_0000] (PID 96925) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| docker-init [bale_0000] (PID 96927) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bale_0000] (PID 96927) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bale_0000] (PID 96927) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 96942) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 96942) rss_mb | MB | 3 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [bale_0000] (PID 96942) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 96952) rss_mb | MB | 1 | 3.230 | 3.230 | 3.230 | 3.230 | n/a | n/a |
| docker (PID 96952) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 96981) rss_mb | MB | 1 | 27.355 | 27.355 | 27.355 | 27.355 | n/a | n/a |
| docker (PID 96981) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 97000) rss_mb | MB | 1 | 10.633 | 10.633 | 10.633 | 10.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 97000) vms_mb | MB | 1 | 1569.445 | 1569.445 | 1569.445 | 1569.445 | n/a | n/a |
| docker (PID 97017) rss_mb | MB | 1 | 27.039 | 27.039 | 27.039 | 27.039 | n/a | n/a |
| docker (PID 97017) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 97035) rss_mb | MB | 1 | 11.770 | 11.770 | 11.770 | 11.770 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 97035) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 97052) rss_mb | MB | 1 | 26.125 | 26.125 | 26.125 | 26.125 | n/a | n/a |
| docker (PID 97052) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 97119) rss_mb | MB | 1 | 26.078 | 26.078 | 26.078 | 26.078 | n/a | n/a |
| docker (PID 97119) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 97135) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 97135) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 97135) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 97135) rss_mb | MB | 39 | 26.871 | 26.871 | 26.871 | 26.871 | n/a | n/a |
| docker (PID 97135) vms_mb | MB | 39 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 97161) rss_mb | MB | 1 | 15.340 | 15.340 | 15.340 | 15.340 | n/a | n/a |
| docker (PID 97161) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| python3 (PID 97185) CPU | percent | 23 | 100.231 | 89.030 | 108.878 | 108.695 | 2.330000 CPU seconds | n/a |
| python3 (PID 97185) io read MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 97185) io write MB/s | MB/s | 23 | 0.102 | 0.000 | 2.355 | 2.355 | 0.238281 MB | n/a |
| python3 (PID 97185) rss_mb | MB | 24 | 33.229 | 21.336 | 34.598 | 34.598 | n/a | n/a |
| python3 (PID 97185) vms_mb | MB | 24 | 56.739 | 45.445 | 57.461 | 57.438 | n/a | n/a |
| docker (PID 97190) rss_mb | MB | 1 | 23.898 | 23.898 | 23.898 | 23.898 | n/a | n/a |
| docker (PID 97190) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 97237) CPU | percent | 1 | 9.868 | 9.868 | 9.868 | 9.868 | 0.010000 CPU seconds | n/a |
| docker (PID 97237) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 97237) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 97237) rss_mb | MB | 2 | 24.607 | 21.602 | 27.613 | 27.613 | n/a | n/a |
| docker (PID 97237) vms_mb | MB | 2 | 1624.488 | 1516.199 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [band_0000] (PID 97279) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [band_0000] (PID 97279) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [band_0000] (PID 97279) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 97291) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 97291) rss_mb | MB | 4 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [band_0000] (PID 97291) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 97357) rss_mb | MB | 1 | 27.434 | 27.434 | 27.434 | 27.434 | n/a | n/a |
| docker (PID 97357) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 97375) rss_mb | MB | 1 | 9.090 | 9.090 | 9.090 | 9.090 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 97375) vms_mb | MB | 1 | 1505.195 | 1505.195 | 1505.195 | 1505.195 | n/a | n/a |
| docker (PID 97391) rss_mb | MB | 1 | 26.984 | 26.984 | 26.984 | 26.984 | n/a | n/a |
| docker (PID 97391) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 97412) rss_mb | MB | 1 | 11.703 | 11.703 | 11.703 | 11.703 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 97412) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 97429) rss_mb | MB | 1 | 27.031 | 27.031 | 27.031 | 27.031 | n/a | n/a |
| docker (PID 97429) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 97489) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 97489) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 97489) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 97489) rss_mb | MB | 2 | 13.412 | 1.195 | 25.629 | 25.629 | n/a | n/a |
| docker (PID 97489) vms_mb | MB | 2 | 846.486 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 97529) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 97529) rss_mb | MB | 4 | 3.681 | 0.633 | 12.824 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 97529) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 97541) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 97541) rss_mb | MB | 3 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [band_0000] (PID 97541) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 97551) rss_mb | MB | 1 | 27.133 | 27.133 | 27.133 | 27.133 | n/a | n/a |
| docker (PID 97551) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 97570) rss_mb | MB | 1 | 11.156 | 11.156 | 11.156 | 11.156 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 97570) vms_mb | MB | 1 | 1641.965 | 1641.965 | 1641.965 | 1641.965 | n/a | n/a |
| docker (PID 97605) rss_mb | MB | 1 | 21.613 | 21.613 | 21.613 | 21.613 | n/a | n/a |
| docker (PID 97605) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 97653) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 97653) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 97653) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 97653) rss_mb | MB | 2 | 14.205 | 2.227 | 26.184 | 26.184 | n/a | n/a |
| docker (PID 97653) vms_mb | MB | 2 | 846.486 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 97713) rss_mb | MB | 1 | 14.375 | 14.375 | 14.375 | 14.375 | n/a | n/a |
| docker (PID 97713) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 97735) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 97735) io read MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 97735) io write MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 97735) rss_mb | MB | 37 | 26.566 | 26.566 | 26.566 | 26.566 | n/a | n/a |
| docker (PID 97735) vms_mb | MB | 37 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 97751) rss_mb | MB | 1 | 25.914 | 25.914 | 25.914 | 25.914 | n/a | n/a |
| docker (PID 97751) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 97777) CPU | percent | 1 | 9.826 | 9.826 | 9.826 | 9.826 | 0.010000 CPU seconds | n/a |
| docker (PID 97777) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 97777) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 97777) rss_mb | MB | 2 | 14.592 | 3.531 | 25.652 | 25.652 | n/a | n/a |
| docker (PID 97777) vms_mb | MB | 2 | 846.486 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[0:PARENT] [band_0000] (PID 97816) rss_mb | MB | 1 | 1.965 | 1.965 | 1.965 | 1.965 | n/a | n/a |
| runc:[0:PARENT] [band_0000] (PID 97816) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[1:CHILD] [band_0000] (PID 97818) rss_mb | MB | 1 | 0.844 | 0.844 | 0.844 | 0.844 | n/a | n/a |
| runc:[1:CHILD] [band_0000] (PID 97818) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 97819) CPU | percent | 4 | 9.712 | 0.000 | 38.846 | 0.000 | 0.040000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 97819) rss_mb | MB | 5 | 0.681 | 0.633 | 0.875 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 97819) vms_mb | MB | 5 | 3.666 | 1.055 | 14.109 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 97833) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 97833) rss_mb | MB | 4 | 1.723 | 1.723 | 1.723 | 1.723 | n/a | n/a |
| tail [band_0000] (PID 97833) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 97835) rss_mb | MB | 1 | 2.641 | 2.641 | 2.641 | 2.641 | n/a | n/a |
| docker (PID 97835) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 97844) rss_mb | MB | 1 | 27.293 | 27.293 | 27.293 | 27.293 | n/a | n/a |
| docker (PID 97844) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 97910) rss_mb | MB | 1 | 20.234 | 20.234 | 20.234 | 20.234 | n/a | n/a |
| docker (PID 97910) vms_mb | MB | 1 | 1523.953 | 1523.953 | 1523.953 | 1523.953 | n/a | n/a |
| docker (PID 97949) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 97949) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 97949) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 97949) rss_mb | MB | 2 | 26.699 | 26.699 | 26.699 | 26.699 | n/a | n/a |
| docker (PID 97949) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 98009) rss_mb | MB | 1 | 26.707 | 26.707 | 26.707 | 26.707 | n/a | n/a |
| docker (PID 98009) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 98049) CPU | percent | 10 | 0.981 | 0.000 | 9.808 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 98049) rss_mb | MB | 11 | 1.711 | 0.633 | 12.492 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 98049) vms_mb | MB | 11 | 150.298 | 1.055 | 1642.730 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 98063) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 98063) rss_mb | MB | 10 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [band_0000] (PID 98063) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 98074) rss_mb | MB | 1 | 27.535 | 27.535 | 27.535 | 27.535 | n/a | n/a |
| docker (PID 98074) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 98102) CPU | percent | 8 | 1.226 | 0.000 | 9.805 | 9.805 | 0.010000 CPU seconds | n/a |
| docker (PID 98102) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 98102) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 98102) rss_mb | MB | 9 | 27.387 | 27.387 | 27.387 | 27.387 | n/a | n/a |
| docker (PID 98102) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 98122) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 98122) rss_mb | MB | 9 | 4.359 | 3.406 | 11.984 | 3.406 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 98122) vms_mb | MB | 9 | 186.401 | 4.391 | 1642.480 | 4.391 | n/a | n/a |
| python [band_0000] (PID 98132) CPU | percent | 7 | 100.754 | 97.678 | 107.855 | 107.855 | 0.720000 CPU seconds | n/a |
| python [band_0000] (PID 98132) rss_mb | MB | 8 | 32.968 | 18.426 | 40.871 | 40.871 | n/a | n/a |
| python [band_0000] (PID 98132) vms_mb | MB | 8 | 40.033 | 23.066 | 50.324 | 50.324 | n/a | n/a |
| docker (PID 98142) rss_mb | MB | 1 | 25.883 | 25.883 | 25.883 | 25.883 | n/a | n/a |
| docker (PID 98142) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 98183) rss_mb | MB | 1 | 26.539 | 26.539 | 26.539 | 26.539 | n/a | n/a |
| docker (PID 98183) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 98201) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 98201) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 98201) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 98201) rss_mb | MB | 2 | 24.955 | 23.113 | 26.797 | 26.797 | n/a | n/a |
| docker (PID 98201) vms_mb | MB | 2 | 1624.488 | 1588.203 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 98240) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 98240) rss_mb | MB | 4 | 3.750 | 0.633 | 13.102 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 98240) vms_mb | MB | 4 | 393.473 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 98254) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 98254) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [band_0000] (PID 98254) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 98266) rss_mb | MB | 1 | 27.219 | 27.219 | 27.219 | 27.219 | n/a | n/a |
| docker (PID 98266) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 98291) rss_mb | MB | 1 | 12.371 | 12.371 | 12.371 | 12.371 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 98291) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 98372) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 98372) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 98372) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 98372) rss_mb | MB | 2 | 25.957 | 25.957 | 25.957 | 25.957 | n/a | n/a |
| docker (PID 98372) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 98439) rss_mb | MB | 1 | 26.543 | 26.543 | 26.543 | 26.543 | n/a | n/a |
| docker (PID 98439) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 98455) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 98455) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 98455) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 98455) rss_mb | MB | 39 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| docker (PID 98455) vms_mb | MB | 39 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 98480) rss_mb | MB | 1 | 27.141 | 27.141 | 27.141 | 27.141 | n/a | n/a |
| docker (PID 98480) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 98503) CPU | percent | 2 | 98.733 | 88.670 | 108.797 | 108.797 | 0.200000 CPU seconds | n/a |
| python3 (PID 98503) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 98503) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 98503) rss_mb | MB | 3 | 28.171 | 21.836 | 33.961 | 33.961 | n/a | n/a |
| python3 (PID 98503) vms_mb | MB | 3 | 52.094 | 46.652 | 57.461 | 57.461 | n/a | n/a |
| docker (PID 98509) rss_mb | MB | 1 | 19.426 | 19.426 | 19.426 | 19.426 | n/a | n/a |
| docker (PID 98509) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 98534) rss_mb | MB | 1 | 26.332 | 26.332 | 26.332 | 26.332 | n/a | n/a |
| docker (PID 98534) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 98557) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 98557) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 98557) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 98557) rss_mb | MB | 2 | 27.252 | 27.121 | 27.383 | 27.383 | n/a | n/a |
| docker (PID 98557) vms_mb | MB | 2 | 1696.775 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [bart_0000] (PID 98596) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bart_0000] (PID 98596) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bart_0000] (PID 98596) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 98612) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 98612) rss_mb | MB | 4 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [bart_0000] (PID 98612) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 98614) rss_mb | MB | 1 | 9.219 | 9.219 | 9.219 | 9.219 | n/a | n/a |
| docker (PID 98614) vms_mb | MB | 1 | 1251.695 | 1251.695 | 1251.695 | 1251.695 | n/a | n/a |
| docker (PID 98649) rss_mb | MB | 1 | 27.148 | 27.148 | 27.148 | 27.148 | n/a | n/a |
| docker (PID 98649) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 98677) rss_mb | MB | 1 | 27.332 | 27.332 | 27.332 | 27.332 | n/a | n/a |
| docker (PID 98677) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 98740) rss_mb | MB | 1 | 26.285 | 26.285 | 26.285 | 26.285 | n/a | n/a |
| docker (PID 98740) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 98748) rss_mb | MB | 1 | 26.746 | 26.746 | 26.746 | 26.746 | n/a | n/a |
| docker (PID 98748) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 98809) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 98809) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 98809) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 98809) rss_mb | MB | 2 | 25.527 | 25.527 | 25.527 | 25.527 | n/a | n/a |
| docker (PID 98809) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 98847) CPU | percent | 3 | 3.272 | 0.000 | 9.816 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 98847) rss_mb | MB | 4 | 3.750 | 0.633 | 13.102 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 98847) vms_mb | MB | 4 | 393.535 | 1.055 | 1570.977 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 98860) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 98860) rss_mb | MB | 3 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [bart_0000] (PID 98860) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 98870) rss_mb | MB | 1 | 27.465 | 27.465 | 27.465 | 27.465 | n/a | n/a |
| docker (PID 98870) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 98889) rss_mb | MB | 1 | 12.160 | 12.160 | 12.160 | 12.160 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 98889) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 98934) rss_mb | MB | 1 | 5.668 | 5.668 | 5.668 | 5.668 | n/a | n/a |
| docker (PID 98934) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 98969) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 98969) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 98969) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 98969) rss_mb | MB | 2 | 25.824 | 25.824 | 25.824 | 25.824 | n/a | n/a |
| docker (PID 98969) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 99045) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 99045) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 99045) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 99045) rss_mb | MB | 38 | 25.406 | 25.406 | 25.406 | 25.406 | n/a | n/a |
| docker (PID 99045) vms_mb | MB | 38 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 99069) rss_mb | MB | 1 | 1.031 | 1.031 | 1.031 | 1.031 | n/a | n/a |
| docker (PID 99069) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 99088) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 99088) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 99088) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 99088) rss_mb | MB | 2 | 25.535 | 25.535 | 25.535 | 25.535 | n/a | n/a |
| docker (PID 99088) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bart_0000] (PID 99128) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bart_0000] (PID 99128) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bart_0000] (PID 99128) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 99140) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 99140) rss_mb | MB | 3 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [bart_0000] (PID 99140) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 99179) rss_mb | MB | 1 | 9.363 | 9.363 | 9.363 | 9.363 | n/a | n/a |
| docker (PID 99179) vms_mb | MB | 1 | 1323.699 | 1323.699 | 1323.699 | 1323.699 | n/a | n/a |
| docker (PID 99216) rss_mb | MB | 1 | 27.223 | 27.223 | 27.223 | 27.223 | n/a | n/a |
| docker (PID 99216) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 99254) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 99254) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 99254) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 99254) rss_mb | MB | 2 | 25.996 | 25.996 | 25.996 | 25.996 | n/a | n/a |
| docker (PID 99254) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 99313) rss_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| docker (PID 99313) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [bart_0000] (PID 99351) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bart_0000] (PID 99351) rss_mb | MB | 10 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bart_0000] (PID 99351) vms_mb | MB | 10 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 99365) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 99365) rss_mb | MB | 10 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [bart_0000] (PID 99365) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 99367) rss_mb | MB | 1 | 16.578 | 16.578 | 16.578 | 16.578 | n/a | n/a |
| docker (PID 99367) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 99404) CPU | percent | 8 | 1.225 | 0.000 | 9.799 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 99404) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 99404) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 99404) rss_mb | MB | 9 | 25.010 | 7.969 | 27.141 | 27.141 | n/a | n/a |
| docker (PID 99404) vms_mb | MB | 9 | 1479.895 | 32.867 | 1660.773 | 1660.773 | n/a | n/a |
| bash [bart_0000] (PID 99424) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bart_0000] (PID 99424) rss_mb | MB | 8 | 3.391 | 3.391 | 3.391 | 3.391 | n/a | n/a |
| bash [bart_0000] (PID 99424) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bart_0000] (PID 99433) CPU | percent | 7 | 100.789 | 98.011 | 107.857 | 98.081 | 0.720000 CPU seconds | n/a |
| python [bart_0000] (PID 99433) rss_mb | MB | 8 | 31.821 | 12.496 | 41.820 | 41.820 | n/a | n/a |
| python [bart_0000] (PID 99433) vms_mb | MB | 8 | 38.916 | 16.328 | 51.324 | 51.324 | n/a | n/a |
| docker (PID 99444) rss_mb | MB | 1 | 27.102 | 27.102 | 27.102 | 27.102 | n/a | n/a |
| docker (PID 99444) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 99486) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 99486) vms_mb | MB | 1 | 12.242 | 12.242 | 12.242 | 12.242 | n/a | n/a |
| docker (PID 99503) rss_mb | MB | 1 | 26.609 | 26.609 | 26.609 | 26.609 | n/a | n/a |
| docker (PID 99503) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [bart_0000] (PID 99543) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bart_0000] (PID 99543) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bart_0000] (PID 99543) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 99556) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 99556) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bart_0000] (PID 99556) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 99594) rss_mb | MB | 1 | 27.301 | 27.301 | 27.301 | 27.301 | n/a | n/a |
| docker (PID 99594) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 99612) rss_mb | MB | 1 | 10.555 | 10.555 | 10.555 | 10.555 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 99612) vms_mb | MB | 1 | 1569.324 | 1569.324 | 1569.324 | 1569.324 | n/a | n/a |
| docker (PID 99627) rss_mb | MB | 1 | 27.547 | 27.547 | 27.547 | 27.547 | n/a | n/a |
| docker (PID 99627) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 99647) rss_mb | MB | 1 | 12.195 | 12.195 | 12.195 | 12.195 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 99647) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 99663) rss_mb | MB | 1 | 26.707 | 26.707 | 26.707 | 26.707 | n/a | n/a |
| docker (PID 99663) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 99739) rss_mb | MB | 1 | 23.008 | 23.008 | 23.008 | 23.008 | n/a | n/a |
| docker (PID 99739) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 99747) CPU | percent | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 99747) io read MB/s | MB/s | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 99747) io write MB/s | MB/s | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 99747) rss_mb | MB | 47 | 27.230 | 27.230 | 27.230 | 27.230 | n/a | n/a |
| docker (PID 99747) vms_mb | MB | 47 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 99774) rss_mb | MB | 1 | 26.879 | 26.879 | 26.879 | 26.879 | n/a | n/a |
| docker (PID 99774) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 99798) CPU | percent | 3 | 98.844 | 88.716 | 108.811 | 99.006 | 0.300000 CPU seconds | n/a |
| python3 (PID 99798) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 99798) io write MB/s | MB/s | 3 | 0.773 | 0.000 | 2.320 | 2.320 | 0.234375 MB | n/a |
| python3 (PID 99798) rss_mb | MB | 4 | 21.699 | 0.988 | 34.449 | 34.449 | n/a | n/a |
| python3 (PID 99798) vms_mb | MB | 4 | 46.629 | 30.125 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 99827) rss_mb | MB | 1 | 13.391 | 13.391 | 13.391 | 13.391 | n/a | n/a |
| docker (PID 99827) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 99850) CPU | percent | 2 | 14.817 | 0.000 | 29.634 | 0.000 | 0.030000 CPU seconds | n/a |
| docker (PID 99850) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 99850) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 99850) rss_mb | MB | 3 | 21.536 | 9.281 | 27.664 | 27.664 | n/a | n/a |
| docker (PID 99850) vms_mb | MB | 3 | 1593.750 | 1315.695 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [base_0000] (PID 99889) CPU | percent | 3 | 3.282 | 0.000 | 9.845 | 0.000 | 0.010000 CPU seconds | n/a |
| docker-init [base_0000] (PID 99889) rss_mb | MB | 4 | 3.711 | 0.633 | 12.945 | 0.633 | n/a | n/a |
| docker-init [base_0000] (PID 99889) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 99903) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 99903) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [base_0000] (PID 99903) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 99931) rss_mb | MB | 1 | 25.633 | 25.633 | 25.633 | 25.633 | n/a | n/a |
| docker (PID 99931) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 99968) rss_mb | MB | 1 | 27.547 | 27.547 | 27.547 | 27.547 | n/a | n/a |
| docker (PID 99968) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 99987) rss_mb | MB | 1 | 4.340 | 4.340 | 4.340 | 4.340 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 99987) vms_mb | MB | 1 | 1433.191 | 1433.191 | 1433.191 | 1433.191 | n/a | n/a |
| sandbox alex_0000 CPU | percent | 20 | 61.468 | 15.170 | 100.837 | 30.474 | 1.255099 CPU seconds | n/a |
| sandbox alex_0000 io read MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox alex_0000 io write MB/s | MB/s | 23 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox alex_0000 memory | MB | 25 | 8.967 | 0.691 | 35.605 | 0.918 | n/a | n/a |
| sandbox alex_0000 net rx MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox alex_0000 net tx MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox andy_0000 CPU | percent | 25 | 56.533 | 15.324 | 101.139 | 31.532 | 1.443895 CPU seconds | n/a |
| sandbox andy_0000 io read MB/s | MB/s | 32 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox andy_0000 io write MB/s | MB/s | 31 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox andy_0000 memory | MB | 33 | 7.936 | 0.000 | 35.156 | 1.125 | n/a | n/a |
| sandbox andy_0000 net rx MB/s | MB/s | 31 | 56.657 | 0.000 | 1756.352 | 0.000 | 3548.441824 MB | n/a |
| sandbox andy_0000 net tx MB/s | MB/s | 31 | 0.500 | 0.000 | 15.514 | 0.000 | 31.344033 MB | n/a |
| sandbox arch_0000 CPU | percent | 18 | 66.392 | 29.968 | 100.137 | 43.935 | 1.222056 CPU seconds | n/a |
| sandbox arch_0000 io read MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox arch_0000 io write MB/s | MB/s | 21 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox arch_0000 memory | MB | 23 | 11.477 | 0.000 | 35.430 | 3.820 | n/a | n/a |
| sandbox arch_0000 net rx MB/s | MB/s | 21 | 553.865 | 0.000 | 11631.167 | 0.000 | 3548.530525 MB | n/a |
| sandbox arch_0000 net tx MB/s | MB/s | 21 | 4.906 | 0.000 | 103.034 | 0.000 | 31.434441 MB | n/a |
| sandbox bake_0000 CPU | percent | 23 | 56.313 | 6.882 | 100.081 | 45.786 | 1.325986 CPU seconds | n/a |
| sandbox bake_0000 io read MB/s | MB/s | 27 | 0.006 | 0.000 | 0.153 | 0.000 | 0.015625 MB | n/a |
| sandbox bake_0000 io write MB/s | MB/s | 27 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bake_0000 memory | MB | 29 | 8.620 | 0.703 | 34.602 | 4.094 | n/a | n/a |
| sandbox bake_0000 net rx MB/s | MB/s | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bake_0000 net tx MB/s | MB/s | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bale_0000 CPU | percent | 51 | 79.552 | 0.000 | 100.949 | 44.457 | 4.163045 CPU seconds | n/a |
| sandbox bale_0000 io read MB/s | MB/s | 55 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bale_0000 io write MB/s | MB/s | 54 | 0.001 | 0.000 | 0.034 | 0.000 | 0.003906 MB | n/a |
| sandbox bale_0000 memory | MB | 56 | 21.234 | 0.250 | 35.512 | 4.379 | n/a | n/a |
| sandbox bale_0000 net rx MB/s | MB/s | 54 | 34.270 | 0.000 | 1850.606 | 0.000 | 3549.672672 MB | n/a |
| sandbox bale_0000 net tx MB/s | MB/s | 54 | 0.309 | 0.000 | 16.696 | 0.000 | 32.024363 MB | n/a |
| sandbox band_0000 CPU | percent | 22 | 58.577 | 14.163 | 100.035 | 31.557 | 1.319544 CPU seconds | n/a |
| sandbox band_0000 io read MB/s | MB/s | 26 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox band_0000 io write MB/s | MB/s | 25 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox band_0000 memory | MB | 27 | 9.601 | 0.715 | 34.453 | 0.961 | n/a | n/a |
| sandbox band_0000 net rx MB/s | MB/s | 26 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox band_0000 net tx MB/s | MB/s | 26 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bart_0000 CPU | percent | 18 | 63.085 | 29.297 | 100.142 | 48.662 | 1.161320 CPU seconds | n/a |
| sandbox bart_0000 io read MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bart_0000 io write MB/s | MB/s | 21 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bart_0000 memory | MB | 23 | 10.221 | 0.594 | 35.535 | 4.031 | n/a | n/a |
| sandbox bart_0000 net rx MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bart_0000 net tx MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox base_0000 CPU | percent | 33 | 60.273 | 0.000 | 100.085 | 32.414 | 2.038801 CPU seconds | n/a |
| sandbox base_0000 io read MB/s | MB/s | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox base_0000 io write MB/s | MB/s | 39 | 0.002 | 0.000 | 0.038 | 0.000 | 0.007812 MB | n/a |
| sandbox base_0000 memory | MB | 42 | 8.499 | 0.727 | 34.277 | 0.906 | n/a | n/a |
| sandbox base_0000 net rx MB/s | MB/s | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox base_0000 net tx MB/s | MB/s | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beam_0000 CPU | percent | 20 | 60.387 | 16.752 | 100.987 | 29.338 | 1.236689 CPU seconds | n/a |
| sandbox beam_0000 io read MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beam_0000 io write MB/s | MB/s | 22 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox beam_0000 memory | MB | 24 | 9.700 | 0.621 | 35.355 | 0.855 | n/a | n/a |
| sandbox beam_0000 net rx MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beam_0000 net tx MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bear_0000 CPU | percent | 23 | 57.845 | 20.332 | 100.100 | 62.922 | 1.365648 CPU seconds | n/a |
| sandbox bear_0000 io read MB/s | MB/s | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bear_0000 io write MB/s | MB/s | 29 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bear_0000 memory | MB | 30 | 8.475 | 0.652 | 35.641 | 3.660 | n/a | n/a |
| sandbox bear_0000 net rx MB/s | MB/s | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bear_0000 net tx MB/s | MB/s | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beef_0000 CPU | percent | 19 | 61.589 | 16.981 | 100.965 | 31.590 | 1.199226 CPU seconds | n/a |
| sandbox beef_0000 io read MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beef_0000 io write MB/s | MB/s | 22 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox beef_0000 memory | MB | 24 | 9.738 | 0.719 | 35.254 | 0.754 | n/a | n/a |
| sandbox beef_0000 net rx MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beef_0000 net tx MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bell_0000 CPU | percent | 16 | 65.821 | 27.126 | 100.156 | 100.156 | 1.077587 CPU seconds | n/a |
| sandbox bell_0000 io read MB/s | MB/s | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bell_0000 io write MB/s | MB/s | 19 | 0.002 | 0.000 | 0.038 | 0.038 | 0.003906 MB | n/a |
| sandbox bell_0000 memory | MB | 20 | 11.127 | 0.633 | 35.328 | 35.328 | n/a | n/a |
| sandbox bell_0000 net rx MB/s | MB/s | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bell_0000 net tx MB/s | MB/s | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| workload total CPU | percent | 7523 | 14.443 | 0.542 | 111.538 | 86.644 | 110.678935 CPU seconds | n/a |
| workload total io read MB/s | MB/s | 409 | 0.000 | 0.000 | 0.153 | 0.000 | 0.015625 MB | n/a |
| workload total io write MB/s | MB/s | 398 | 0.001 | 0.000 | 0.038 | 0.000 | 0.050781 MB | n/a |
| workload total memory | MB | 7524 | 482.466 | 383.578 | 539.820 | 501.531 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
