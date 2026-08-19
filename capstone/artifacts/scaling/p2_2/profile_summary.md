# agprof summary

- Duration: **413.601 s**
- Runs: **24/24 completed**, 24 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.058 runs/s**
- LLM: **80 calls**, 80 succeeded, 0 failed, 0 interrupted, 0 retries, 521.162 s total wait
- Tools: **104/104 completed**, 3 failed, 0 interrupted
- Raw resource samples: **49086** at 9.853 Hz effective (10 Hz configured)
- GPU sampling: **unavailable** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 27080.462 / 44772.934 ms |
| LLM latency p50 / p95 | 3716.637 / 25668.916 ms |
| LLM TTFT p50 / p95 | 742.995 / 1147.220 ms |
| LLM input / output tokens | 415044 / 22940 |
| LLM output throughput | 49.790 tokens/s |
| LLM attempts | 80 total, 80 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 421.908 / 1219.553 ms |

### Tool outcomes

| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 13/13 | 13 | 0 | 0 | 1172.054 ms | 2670.177 ms |
| edit | 13/13 | 13 | 0 | 0 | 427.947 ms | 751.980 ms |
| glob | 2/2 | 2 | 0 | 0 | 334.894 ms | 337.203 ms |
| read | 37/37 | 37 | 0 | 0 | 559.707 ms | 979.752 ms |
| return_plan | 12/12 | 12 | 0 | 0 | 0.305 ms | 0.548 ms |
| return_status | 12/12 | 12 | 0 | 0 | 0.271 ms | 0.355 ms |
| return_summary | 15/15 | 12 | 3 | 0 | 0.338 ms | 0.467 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 26.332% | 199.784% | 109.799 s | 495.179 MB | 551.711 MB | 4.386719 MB | 2.500000 MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python3 | 124202 |  | 4075 | 5.361% | 107.355% | 22.440 s | 689.733 MB | 706.297 MB | 3937.487 MB | 4046.309 MB | 22.195312 MB | 35.070312 MB |
| git | 124209 |  | 2 | 0.000% | 0.000% | 0.000 s | 3.391 MB | 3.391 MB | 11.273 MB | 11.273 MB | 0.000000 MB | 0.000000 MB |
| git | 124208 |  | 2 | 0.000% | 0.000% | 0.000 s | 4.742 MB | 4.742 MB | 12.516 MB | 12.516 MB | 0.000000 MB | 0.000000 MB |
| git-remote-http | 124210 |  | 2 | 19.758% | 19.758% | 0.020 s | 19.021 MB | 19.102 MB | 106.566 MB | 106.566 MB | 0.296875 MB | 0.000000 MB |
| python3 | 124216 |  | 99 | 99.879% | 109.034% | 9.880 s | 33.903 MB | 34.223 MB | 57.171 MB | 57.457 MB | 0.242188 MB | 0.015625 MB |
| python3 | 124217 |  | 4 | 98.995% | 99.069% | 0.300 s | 29.606 MB | 34.965 MB | 53.112 MB | 57.457 MB | 0.000000 MB | 0.261719 MB |
| python3 | 124218 |  | 4 | 102.031% | 108.878% | 0.310 s | 28.198 MB | 36.312 MB | 52.201 MB | 59.516 MB | 0.000000 MB | 0.261719 MB |
| python3 | 124219 |  | 4 | 102.328% | 108.986% | 0.310 s | 29.744 MB | 35.098 MB | 53.162 MB | 57.496 MB | 0.000000 MB | 0.261719 MB |
| python3 | 124220 |  | 25 | 99.869% | 108.999% | 2.420 s | 33.437 MB | 34.926 MB | 56.563 MB | 57.508 MB | 0.000000 MB | 0.261719 MB |
| python3 | 124221 |  | 85 | 99.883% | 108.958% | 8.490 s | 40.742 MB | 47.484 MB | 63.670 MB | 70.586 MB | 0.000000 MB | 0.269531 MB |
| python3 | 124222 |  | 4 | 99.003% | 99.067% | 0.300 s | 28.827 MB | 35.117 MB | 52.150 MB | 57.508 MB | 0.000000 MB | 0.269531 MB |
| python3 | 124223 |  | 99 | 99.972% | 109.050% | 9.890 s | 34.028 MB | 34.426 MB | 57.100 MB | 57.457 MB | 0.000000 MB | 0.015625 MB |
| python3 | 124224 |  | 4 | 99.023% | 108.969% | 0.300 s | 28.747 MB | 35.027 MB | 51.864 MB | 57.496 MB | 0.000000 MB | 0.269531 MB |
| python3 | 124225 |  | 4 | 99.022% | 99.058% | 0.300 s | 25.085 MB | 34.863 MB | 49.001 MB | 57.496 MB | 0.000000 MB | 0.269531 MB |
| python3 | 124226 |  | 4 | 102.297% | 108.849% | 0.310 s | 29.481 MB | 35.070 MB | 52.818 MB | 57.508 MB | 0.000000 MB | 0.269531 MB |
| python3 | 124227 |  | 4 | 102.299% | 108.838% | 0.310 s | 25.538 MB | 34.801 MB | 49.624 MB | 57.457 MB | 0.000000 MB | 0.269531 MB |
| docker | 124231 |  | 1 | n/a% | n/a% | n/a s | 4.160 MB | 4.160 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 124287 |  | 4 | 6.591% | 19.772% | 0.020 s | 27.152 MB | 27.496 MB | 1696.775 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 124311 |  | 3 | 4.943% | 9.886% | 0.010 s | 27.600 MB | 27.758 MB | 1708.776 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 124380 | andy_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.390 MB | 12.930 MB | 225.258 MB | 1570.477 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 124391 | alex_0000 | 6 | 1.966% | 9.830% | 0.010 s | 2.600 MB | 12.434 MB | 262.583 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 124404 | andy_0000 | 6 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 124408 |  | 1 | n/a% | n/a% | n/a s | 27.219 MB | 27.219 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 124413 | alex_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.809 MB | 1.809 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 124415 |  | 1 | n/a% | n/a% | n/a s | 27.234 MB | 27.234 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 124488 |  | 1 | n/a% | n/a% | n/a s | 13.324 MB | 13.324 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 124486 |  | 1 | n/a% | n/a% | n/a s | 18.461 MB | 18.461 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 124543 |  | 1 | n/a% | n/a% | n/a s | 17.891 MB | 17.891 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 124541 |  | 1 | n/a% | n/a% | n/a s | 23.852 MB | 23.852 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 124596 |  | 1 | n/a% | n/a% | n/a s | 23.703 MB | 23.703 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 124594 |  | 1 | n/a% | n/a% | n/a s | 23.738 MB | 23.738 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 124611 |  | 1 | n/a% | n/a% | n/a s | 27.199 MB | 27.199 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 124659 | andy_0000 | 1 | n/a% | n/a% | n/a s | 10.684 MB | 10.684 MB | 1569.582 MB | 1569.582 MB | n/a MB | n/a MB |
| docker | 124613 |  | 1 | n/a% | n/a% | n/a s | 27.109 MB | 27.109 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 124642 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.805 MB | 11.805 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 124684 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.145 MB | 27.145 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 124693 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.742 MB | 26.742 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 124785 |  | 1 | n/a% | n/a% | n/a s | 26.844 MB | 26.844 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 124879 | alex_0000 | 5 | 7.256% | 29.023% | 0.030 s | 1.297 MB | 3.953 MB | 242.579 MB | 1208.676 MB | n/a MB | n/a MB |
| docker | 124801 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.402 MB | 25.402 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 124799 |  | 1 | n/a% | n/a% | n/a s | 25.742 MB | 25.742 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 124908 | andy_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.672 MB | 1.672 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 124886 | andy_0000 | 5 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 124899 | alex_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.574 MB | 1.574 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 124907 |  | 1 | n/a% | n/a% | n/a s | 17.727 MB | 17.727 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 124973 | andy_0000 | 1 | n/a% | n/a% | n/a s | 10.863 MB | 10.863 MB | 1497.707 MB | 1497.707 MB | n/a MB | n/a MB |
| docker | 124934 |  | 1 | n/a% | n/a% | n/a s | 27.055 MB | 27.055 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 124993 |  | 1 | n/a% | n/a% | n/a s | 27.180 MB | 27.180 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 125026 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.703 MB | 11.703 MB | 1570.219 MB | 1570.219 MB | n/a MB | n/a MB |
| docker | 125033 |  | 1 | n/a% | n/a% | n/a s | 2.941 MB | 2.941 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 125061 |  | 1 | n/a% | n/a% | n/a s | 26.645 MB | 26.645 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 125043 |  | 1 | n/a% | n/a% | n/a s | 27.613 MB | 27.613 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 125076 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.988 MB | 11.988 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 125130 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.168 MB | 25.816 MB | 1624.209 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 125116 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.129 MB | 26.129 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 125256 |  | 38 | 0.000% | 0.000% | 0.000 s | 27.059 MB | 27.059 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 125272 |  | 1 | n/a% | n/a% | n/a s | 26.828 MB | 26.828 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 125299 |  | 1 | n/a% | n/a% | n/a s | 27.211 MB | 27.211 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 125353 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 125355 |  | 1 | n/a% | n/a% | n/a s | 16.441 MB | 16.441 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker-init | 125339 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.590 MB | 0.590 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 125391 |  | 1 | n/a% | n/a% | n/a s | 27.410 MB | 27.410 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 125445 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.121 MB | 11.121 MB | 1641.965 MB | 1641.965 MB | n/a MB | n/a MB |
| docker | 125426 |  | 1 | n/a% | n/a% | n/a s | 27.383 MB | 27.383 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 125464 |  | 1 | n/a% | n/a% | n/a s | 26.012 MB | 26.012 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 125522 |  | 1 | n/a% | n/a% | n/a s | 27.184 MB | 27.184 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker-init | 125561 | alex_0000 | 12 | 0.000% | 0.000% | 0.000 s | 0.594 MB | 0.594 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 125573 | alex_0000 | 12 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 125576 |  | 1 | n/a% | n/a% | n/a s | 22.004 MB | 22.004 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 125611 |  | 11 | 0.000% | 0.000% | 0.000 s | 27.156 MB | 27.156 MB | 1661.023 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| bash | 125629 | alex_0000 | 10 | 0.000% | 0.000% | 0.000 s | 3.422 MB | 3.422 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 125638 | alex_0000 | 10 | 100.937% | 107.871% | 0.930 s | 32.030 MB | 41.648 MB | 39.243 MB | 51.238 MB | n/a MB | n/a MB |
| docker | 125648 |  | 1 | n/a% | n/a% | n/a s | 26.227 MB | 26.227 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 125690 |  | 1 | n/a% | n/a% | n/a s | 25.371 MB | 25.371 MB | 1596.211 MB | 1596.211 MB | n/a MB | n/a MB |
| docker | 125699 |  | 1 | n/a% | n/a% | n/a s | 15.773 MB | 15.773 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 125707 |  | 2 | 97.958% | 97.958% | 0.100 s | 16.020 MB | 23.359 MB | 1407.693 MB | 1587.953 MB | 0.000000 MB | 0.000000 MB |
| docker | 125717 |  | 2 | 80.947% | 80.947% | 0.100 s | 0.818 MB | 1.637 MB | 16.381 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 125715 |  | 2 | 64.757% | 64.757% | 0.080 s | 17.637 MB | 27.008 MB | 846.820 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 125739 |  | 45 | 0.180% | 7.919% | 0.010 s | 26.508 MB | 26.535 MB | 1660.761 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 125736 |  | 4 | 0.000% | 0.000% | 0.000 s | 26.828 MB | 26.828 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 125786 | alex_0000 | 8 | 8.435% | 59.043% | 0.070 s | 3.513 MB | 13.086 MB | 393.219 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 125799 | alex_0000 | 6 | 0.000% | 0.000% | 0.000 s | 1.723 MB | 1.723 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 125801 |  | 1 | n/a% | n/a% | n/a s | 8.238 MB | 8.238 MB | 32.867 MB | 32.867 MB | n/a MB | n/a MB |
| docker | 125809 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.178 MB | 27.016 MB | 1628.492 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 125827 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.746 MB | 11.746 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 125856 | alex_0000 | 1 | n/a% | n/a% | n/a s | 10.344 MB | 10.344 MB | 1569.945 MB | 1569.945 MB | n/a MB | n/a MB |
| docker | 125837 |  | 1 | n/a% | n/a% | n/a s | 25.406 MB | 25.406 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 125872 |  | 1 | n/a% | n/a% | n/a s | 19.113 MB | 19.113 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 125899 |  | 1 | n/a% | n/a% | n/a s | 23.531 MB | 23.531 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 125908 |  | 1 | n/a% | n/a% | n/a s | 26.945 MB | 26.945 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 125950 |  | 1 | n/a% | n/a% | n/a s | 17.852 MB | 17.852 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 125967 |  | 1 | n/a% | n/a% | n/a s | 26.668 MB | 26.668 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 125986 |  | 1 | n/a% | n/a% | n/a s | 4.152 MB | 4.152 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 126011 |  | 1 | n/a% | n/a% | n/a s | 25.652 MB | 25.652 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 126019 |  | 43 | 0.000% | 0.000% | 0.000 s | 26.941 MB | 26.941 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 126035 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.918 MB | 25.918 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 126076 | andy_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.708 MB | 13.082 MB | 274.626 MB | 1642.480 MB | n/a MB | n/a MB |
| tail | 126089 | andy_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 126100 |  | 1 | n/a% | n/a% | n/a s | 1.500 MB | 1.500 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 126127 |  | 1 | n/a% | n/a% | n/a s | 8.547 MB | 8.547 MB | 1227.309 MB | 1227.309 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 126185 | andy_0000 | 1 | n/a% | n/a% | n/a s | 12.078 MB | 12.078 MB | 1714.984 MB | 1714.984 MB | n/a MB | n/a MB |
| docker | 126165 |  | 1 | n/a% | n/a% | n/a s | 27.180 MB | 27.180 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 126205 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.867 MB | 25.867 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 126261 |  | 1 | n/a% | n/a% | n/a s | 18.398 MB | 18.398 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 126273 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.035 MB | 27.035 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| tail | 126340 | andy_0000 | 14 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 126314 | andy_0000 | 14 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 126329 |  | 1 | n/a% | n/a% | n/a s | 25.891 MB | 25.891 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 126384 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.520 MB | 11.520 MB | 1570.098 MB | 1570.098 MB | n/a MB | n/a MB |
| docker | 126373 |  | 1 | n/a% | n/a% | n/a s | 24.902 MB | 24.902 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 126359 |  | 1 | n/a% | n/a% | n/a s | 27.352 MB | 27.352 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 126420 | andy_0000 | 11 | 1.885% | 18.852% | 0.020 s | 4.110 MB | 11.895 MB | 146.808 MB | 1570.977 MB | n/a MB | n/a MB |
| python3 | 126403 |  | 6 | 97.640% | 105.571% | 0.510 s | 26.258 MB | 34.523 MB | 50.310 MB | 57.438 MB | 0.039062 MB | 0.238281 MB |
| docker | 126398 |  | 11 | 0.000% | 0.000% | 0.000 s | 27.176 MB | 27.176 MB | 1661.023 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| python | 126429 | andy_0000 | 10 | 98.904% | 107.136% | 0.920 s | 31.401 MB | 42.633 MB | 38.066 MB | 52.238 MB | n/a MB | n/a MB |
| docker | 126439 |  | 1 | n/a% | n/a% | n/a s | 2.789 MB | 2.789 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 126456 |  | 1 | n/a% | n/a% | n/a s | 25.309 MB | 25.309 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 126475 |  | 2 | 9.811% | 9.811% | 0.010 s | 17.537 MB | 25.957 MB | 1443.822 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 126530 |  | 1 | n/a% | n/a% | n/a s | 0.559 MB | 0.559 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 126578 | andy_0000 | 4 | 6.452% | 19.355% | 0.020 s | 2.473 MB | 7.992 MB | 393.090 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 126538 |  | 1 | n/a% | n/a% | n/a s | 27.113 MB | 27.113 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 126591 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 126630 |  | 1 | n/a% | n/a% | n/a s | 26.980 MB | 26.980 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| 6 | 126647 | andy_0000 | 1 | n/a% | n/a% | n/a s | 0.707 MB | 0.707 MB | 14.004 MB | 14.004 MB | n/a MB | n/a MB |
| docker | 126664 |  | 1 | n/a% | n/a% | n/a s | 27.188 MB | 27.188 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 126685 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.832 MB | 11.832 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 126703 |  | 1 | n/a% | n/a% | n/a s | 25.816 MB | 25.816 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 126770 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.959 MB | 27.242 MB | 1696.775 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 126812 | arch_0000 | 4 | 3.284% | 9.852% | 0.010 s | 3.622 MB | 12.590 MB | 411.474 MB | 1642.730 MB | n/a MB | n/a MB |
| docker | 126827 |  | 1 | n/a% | n/a% | n/a s | 27.469 MB | 27.469 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 126848 |  | 1 | n/a% | n/a% | n/a s | 11.797 MB | 11.797 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 126825 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 126925 |  | 1 | n/a% | n/a% | n/a s | 24.242 MB | 24.242 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 126962 |  | 1 | n/a% | n/a% | n/a s | 25.945 MB | 25.945 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 127002 |  | 1 | n/a% | n/a% | n/a s | 21.254 MB | 21.254 MB | 1524.203 MB | 1524.203 MB | n/a MB | n/a MB |
| runc:[1:CHILD] | 127056 | arch_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 127019 |  | 1 | n/a% | n/a% | n/a s | 26.434 MB | 26.434 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 127053 | arch_0000 | 1 | n/a% | n/a% | n/a s | 1.902 MB | 1.902 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker-init | 127057 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 127072 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 127082 |  | 1 | n/a% | n/a% | n/a s | 17.414 MB | 17.414 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 127109 |  | 1 | n/a% | n/a% | n/a s | 26.926 MB | 26.926 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 127128 | arch_0000 | 1 | n/a% | n/a% | n/a s | 10.316 MB | 10.316 MB | 1569.195 MB | 1569.195 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 127164 | arch_0000 | 1 | n/a% | n/a% | n/a s | 11.961 MB | 11.961 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 127145 |  | 1 | n/a% | n/a% | n/a s | 27.332 MB | 27.332 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 127180 |  | 1 | n/a% | n/a% | n/a s | 26.883 MB | 26.883 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 127254 |  | 1 | n/a% | n/a% | n/a s | 25.281 MB | 25.281 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 127262 |  | 39 | 0.000% | 0.000% | 0.000 s | 26.914 MB | 26.914 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 127278 |  | 1 | n/a% | n/a% | n/a s | 26.570 MB | 26.570 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| docker | 127302 |  | 1 | n/a% | n/a% | n/a s | 9.152 MB | 9.152 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| python3 | 127309 |  | 4 | 102.218% | 108.864% | 0.310 s | 28.146 MB | 34.762 MB | 51.818 MB | 57.438 MB | 0.000000 MB | 0.257812 MB |
| docker | 127327 |  | 1 | n/a% | n/a% | n/a s | 26.852 MB | 26.852 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 127361 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.828 MB | 27.828 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 127403 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.711 MB | 12.945 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 127445 |  | 1 | n/a% | n/a% | n/a s | 23.707 MB | 23.707 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| tail | 127416 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 127498 | bake_0000 | 1 | n/a% | n/a% | n/a s | 1.992 MB | 1.992 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 127481 |  | 1 | n/a% | n/a% | n/a s | 27.254 MB | 27.254 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[1:CHILD] | 127499 | bake_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 127515 |  | 1 | n/a% | n/a% | n/a s | 27.168 MB | 27.168 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 127535 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.551 MB | 11.551 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 127551 |  | 1 | n/a% | n/a% | n/a s | 25.828 MB | 25.828 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 127608 |  | 2 | 9.851% | 9.851% | 0.010 s | 13.746 MB | 27.082 MB | 845.562 MB | 1660.523 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 127649 | bake_0000 | 4 | 3.251% | 9.752% | 0.010 s | 3.524 MB | 12.199 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 127691 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.105 MB | 11.105 MB | 1569.840 MB | 1569.840 MB | n/a MB | n/a MB |
| docker | 127672 |  | 1 | n/a% | n/a% | n/a s | 27.320 MB | 27.320 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 127662 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 127725 |  | 1 | n/a% | n/a% | n/a s | 18.184 MB | 18.184 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 127768 |  | 2 | 9.697% | 9.697% | 0.010 s | 13.174 MB | 25.895 MB | 846.480 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 127821 |  | 1 | n/a% | n/a% | n/a s | 25.039 MB | 25.039 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 127851 |  | 41 | 0.000% | 0.000% | 0.000 s | 26.641 MB | 26.641 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 127859 |  | 1 | n/a% | n/a% | n/a s | 26.664 MB | 26.664 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 127868 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.754 MB | 25.754 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| 6 | 127902 | bake_0000 | 1 | n/a% | n/a% | n/a s | 1.762 MB | 1.762 MB | 13.980 MB | 13.980 MB | n/a MB | n/a MB |
| tail | 127921 | bake_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 127909 | bake_0000 | 5 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 127932 |  | 1 | n/a% | n/a% | n/a s | 27.305 MB | 27.305 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 127951 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.473 MB | 11.473 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 127958 |  | 1 | n/a% | n/a% | n/a s | 27.199 MB | 27.199 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 127977 | bake_0000 | 1 | n/a% | n/a% | n/a s | 10.840 MB | 10.840 MB | 1497.578 MB | 1497.578 MB | n/a MB | n/a MB |
| docker | 127991 |  | 1 | n/a% | n/a% | n/a s | 22.461 MB | 22.461 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 128027 |  | 1 | n/a% | n/a% | n/a s | 25.883 MB | 25.883 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 128093 |  | 1 | n/a% | n/a% | n/a s | 26.332 MB | 26.332 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| docker | 128112 |  | 1 | n/a% | n/a% | n/a s | 26.781 MB | 26.781 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| docker-init | 128153 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 128166 |  | 1 | n/a% | n/a% | n/a s | 19.840 MB | 19.840 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 128164 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 128200 |  | 1 | n/a% | n/a% | n/a s | 25.969 MB | 25.969 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 128235 |  | 1 | n/a% | n/a% | n/a s | 27.352 MB | 27.352 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 128275 |  | 1 | n/a% | n/a% | n/a s | 26.871 MB | 26.871 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 128317 |  | 1 | n/a% | n/a% | n/a s | 4.965 MB | 4.965 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 128334 |  | 2 | 0.000% | 0.000% | 0.000 s | 24.133 MB | 26.762 MB | 1624.488 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 128377 | arch_0000 | 11 | 0.980% | 9.803% | 0.010 s | 1.727 MB | 12.668 MB | 143.707 MB | 1570.227 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 128418 | arch_0000 | 1 | n/a% | n/a% | n/a s | 10.793 MB | 10.793 MB | 1641.586 MB | 1641.586 MB | n/a MB | n/a MB |
| tail | 128389 | arch_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.676 MB | 1.676 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 128399 |  | 1 | n/a% | n/a% | n/a s | 27.258 MB | 27.258 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| bash | 128445 | arch_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.324 MB | 3.324 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 128455 | arch_0000 | 8 | 99.134% | 107.818% | 0.710 s | 30.207 MB | 42.754 MB | 37.428 MB | 52.219 MB | n/a MB | n/a MB |
| docker | 128426 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.258 MB | 27.258 MB | 1661.023 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| docker | 128468 |  | 1 | n/a% | n/a% | n/a s | 26.266 MB | 26.266 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 128548 |  | 41 | 0.000% | 0.000% | 0.000 s | 25.762 MB | 25.762 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 128557 |  | 1 | n/a% | n/a% | n/a s | 17.191 MB | 17.191 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 128566 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.766 MB | 25.766 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 128605 | arch_0000 | 5 | 2.438% | 9.753% | 0.010 s | 3.122 MB | 13.078 MB | 314.989 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 128629 |  | 1 | n/a% | n/a% | n/a s | 27.543 MB | 27.543 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 128618 | arch_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 128654 |  | 1 | n/a% | n/a% | n/a s | 26.180 MB | 26.180 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 128689 |  | 1 | n/a% | n/a% | n/a s | 3.430 MB | 3.430 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 128716 |  | 1 | n/a% | n/a% | n/a s | 3.684 MB | 3.684 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 128726 |  | 1 | n/a% | n/a% | n/a s | 25.859 MB | 25.859 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 128768 |  | 1 | n/a% | n/a% | n/a s | 25.281 MB | 25.281 MB | 1595.961 MB | 1595.961 MB | n/a MB | n/a MB |
| docker | 128785 |  | 1 | n/a% | n/a% | n/a s | 11.125 MB | 11.125 MB | 1387.949 MB | 1387.949 MB | n/a MB | n/a MB |
| docker | 128828 |  | 1 | n/a% | n/a% | n/a s | 10.344 MB | 10.344 MB | 1387.949 MB | 1387.949 MB | n/a MB | n/a MB |
| docker | 128837 |  | 49 | 0.000% | 0.000% | 0.000 s | 25.652 MB | 25.652 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 128845 |  | 1 | n/a% | n/a% | n/a s | 23.824 MB | 23.824 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 128853 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.211 MB | 27.211 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 128895 | bake_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.091 MB | 12.922 MB | 300.538 MB | 1498.473 MB | n/a MB | n/a MB |
| docker | 128916 |  | 1 | n/a% | n/a% | n/a s | 15.941 MB | 15.941 MB | 1387.949 MB | 1387.949 MB | n/a MB | n/a MB |
| tail | 128906 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 128942 |  | 1 | n/a% | n/a% | n/a s | 27.336 MB | 27.336 MB | 1733.027 MB | 1733.027 MB | n/a MB | n/a MB |
| docker | 128980 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 129018 |  | 1 | n/a% | n/a% | n/a s | 25.816 MB | 25.816 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 129059 |  | 1 | n/a% | n/a% | n/a s | 4.582 MB | 4.582 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 129076 |  | 3 | 4.778% | 9.556% | 0.010 s | 18.016 MB | 25.641 MB | 1117.728 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| 6 | 129113 | bake_0000 | 1 | n/a% | n/a% | n/a s | 1.770 MB | 1.770 MB | 13.980 MB | 13.980 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 129116 | bake_0000 | 16 | 0.000% | 0.000% | 0.000 s | 1.397 MB | 12.855 MB | 99.128 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 129139 |  | 1 | n/a% | n/a% | n/a s | 27.113 MB | 27.113 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 129128 | bake_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 129156 | bake_0000 | 1 | n/a% | n/a% | n/a s | 8.938 MB | 8.938 MB | 1569.445 MB | 1569.445 MB | n/a MB | n/a MB |
| docker | 129167 |  | 14 | 0.000% | 0.000% | 0.000 s | 27.248 MB | 27.355 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| python | 129195 | bake_0000 | 13 | 98.462% | 124.100% | 1.250 s | 32.337 MB | 41.391 MB | 39.607 MB | 50.375 MB | n/a MB | n/a MB |
| bash | 129186 | bake_0000 | 13 | 0.000% | 0.000% | 0.000 s | 3.258 MB | 3.258 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 129209 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.887 MB | 26.887 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 129278 |  | 1 | n/a% | n/a% | n/a s | 25.699 MB | 25.699 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| python3 | 129293 |  | 4 | 102.116% | 108.840% | 0.310 s | 25.889 MB | 34.348 MB | 50.038 MB | 57.457 MB | 0.000000 MB | 0.257812 MB |
| docker | 129304 |  | 1 | n/a% | n/a% | n/a s | 19.230 MB | 19.230 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 129332 |  | 2 | 97.813% | 97.813% | 0.100 s | 12.143 MB | 23.426 MB | 810.357 MB | 1587.953 MB | 0.000000 MB | 0.000000 MB |
| docker | 129342 |  | 1 | n/a% | n/a% | n/a s | 26.934 MB | 26.934 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 129381 | bake_0000 | 4 | 6.520% | 19.561% | 0.020 s | 3.243 MB | 11.074 MB | 393.152 MB | 1569.445 MB | n/a MB | n/a MB |
| tail | 129395 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 129405 |  | 1 | n/a% | n/a% | n/a s | 18.234 MB | 18.234 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 129453 | bake_0000 | 1 | n/a% | n/a% | n/a s | 12.012 MB | 12.012 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 129433 |  | 1 | n/a% | n/a% | n/a s | 27.375 MB | 27.375 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 129468 |  | 1 | n/a% | n/a% | n/a s | 27.320 MB | 27.320 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 129504 |  | 1 | n/a% | n/a% | n/a s | 26.773 MB | 26.773 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 129552 |  | 1 | n/a% | n/a% | n/a s | 25.633 MB | 25.633 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 129566 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.555 MB | 27.555 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 129606 | bale_0000 | 4 | 3.273% | 9.818% | 0.010 s | 3.631 MB | 12.625 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 129647 |  | 1 | n/a% | n/a% | n/a s | 15.824 MB | 15.824 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 129618 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 129682 |  | 1 | n/a% | n/a% | n/a s | 27.180 MB | 27.180 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 129717 |  | 1 | n/a% | n/a% | n/a s | 27.184 MB | 27.184 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 129736 | bale_0000 | 1 | n/a% | n/a% | n/a s | 12.082 MB | 12.082 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 129752 |  | 1 | n/a% | n/a% | n/a s | 26.930 MB | 26.930 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 129802 |  | 1 | n/a% | n/a% | n/a s | 25.988 MB | 25.988 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 129810 |  | 1 | n/a% | n/a% | n/a s | 27.043 MB | 27.043 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 129850 | bale_0000 | 4 | 6.538% | 19.613% | 0.020 s | 3.466 MB | 11.965 MB | 375.347 MB | 1498.223 MB | n/a MB | n/a MB |
| docker | 129889 |  | 1 | n/a% | n/a% | n/a s | 22.340 MB | 22.340 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| tail | 129868 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 129920 |  | 1 | n/a% | n/a% | n/a s | 27.477 MB | 27.477 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 129940 | bale_0000 | 1 | n/a% | n/a% | n/a s | 11.277 MB | 11.277 MB | 1570.340 MB | 1570.340 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 129978 | bale_0000 | 1 | n/a% | n/a% | n/a s | 11.922 MB | 11.922 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 129955 |  | 1 | n/a% | n/a% | n/a s | 27.457 MB | 27.457 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 129995 |  | 1 | n/a% | n/a% | n/a s | 25.832 MB | 25.832 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 130062 |  | 1 | n/a% | n/a% | n/a s | 27.137 MB | 27.137 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 130070 |  | 39 | 0.000% | 0.000% | 0.000 s | 26.441 MB | 26.441 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 130095 |  | 1 | n/a% | n/a% | n/a s | 0.129 MB | 0.129 MB | 30.570 MB | 30.570 MB | n/a MB | n/a MB |
| python3 | 130119 |  | 3 | 103.771% | 108.873% | 0.210 s | 26.816 MB | 33.625 MB | 50.487 MB | 56.461 MB | 0.000000 MB | 0.000000 MB |
| docker | 130137 |  | 1 | n/a% | n/a% | n/a s | 24.281 MB | 24.281 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 130171 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.318 MB | 27.684 MB | 1696.775 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| 6 | 130207 |  | 1 | n/a% | n/a% | n/a s | 1.789 MB | 1.789 MB | 13.980 MB | 13.980 MB | n/a MB | n/a MB |
| docker-init | 130209 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 130224 |  | 1 | n/a% | n/a% | n/a s | 27.238 MB | 27.238 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 130222 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 130259 |  | 1 | n/a% | n/a% | n/a s | 27.141 MB | 27.141 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 130280 | band_0000 | 1 | n/a% | n/a% | n/a s | 10.312 MB | 10.312 MB | 1569.195 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 130315 |  | 1 | n/a% | n/a% | n/a s | 13.363 MB | 13.363 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 130359 |  | 1 | n/a% | n/a% | n/a s | 25.996 MB | 25.996 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 130418 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.879 MB | 26.879 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 130458 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.672 MB | 12.789 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 130471 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 130503 | band_0000 | 1 | n/a% | n/a% | n/a s | 11.547 MB | 11.547 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 130482 |  | 1 | n/a% | n/a% | n/a s | 27.262 MB | 27.262 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 130581 |  | 2 | 0.000% | 0.000% | 0.000 s | 23.611 MB | 25.879 MB | 1588.080 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 130648 |  | 1 | n/a% | n/a% | n/a s | 25.859 MB | 25.859 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 130662 |  | 38 | 0.000% | 0.000% | 0.000 s | 27.098 MB | 27.098 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 130679 |  | 1 | n/a% | n/a% | n/a s | 27.000 MB | 27.000 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 130705 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.031 MB | 27.031 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 130744 | bale_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.725 MB | 13.000 MB | 411.474 MB | 1642.730 MB | n/a MB | n/a MB |
| docker | 130767 |  | 1 | n/a% | n/a% | n/a s | 27.371 MB | 27.371 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 130787 | bale_0000 | 1 | n/a% | n/a% | n/a s | 11.492 MB | 11.492 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 130757 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.539 MB | 1.539 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 130825 |  | 1 | n/a% | n/a% | n/a s | 25.883 MB | 25.883 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 130871 |  | 2 | 0.000% | 0.000% | 0.000 s | 17.367 MB | 26.066 MB | 1443.822 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 130930 |  | 1 | n/a% | n/a% | n/a s | 25.859 MB | 25.859 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker-init | 130971 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 130984 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 130986 |  | 1 | n/a% | n/a% | n/a s | 18.125 MB | 18.125 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 131021 |  | 1 | n/a% | n/a% | n/a s | 27.250 MB | 27.250 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 131077 | band_0000 | 1 | n/a% | n/a% | n/a s | 10.902 MB | 10.902 MB | 1569.703 MB | 1569.703 MB | n/a MB | n/a MB |
| docker | 131058 |  | 1 | n/a% | n/a% | n/a s | 27.328 MB | 27.328 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 131094 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.773 MB | 26.773 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 131155 |  | 1 | n/a% | n/a% | n/a s | 26.984 MB | 26.984 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| docker-init | 131195 | bale_0000 | 37 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 131208 | bale_0000 | 37 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 131210 |  | 1 | n/a% | n/a% | n/a s | 26.379 MB | 26.379 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 131266 | bale_0000 | 36 | 0.557% | 19.489% | 0.020 s | 3.294 MB | 3.359 MB | 4.661 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 131246 |  | 36 | 0.000% | 0.000% | 0.000 s | 27.219 MB | 27.219 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 131275 | bale_0000 | 35 | 100.065% | 107.959% | 3.470 s | 39.044 MB | 41.629 MB | 47.990 MB | 51.410 MB | n/a MB | n/a MB |
| docker | 131285 |  | 1 | n/a% | n/a% | n/a s | 25.797 MB | 25.797 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 131345 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.984 MB | 26.984 MB | 1588.520 MB | 1588.520 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 131387 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.422 MB | 0.633 MB | 1.010 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 131400 | bale_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 131439 |  | 1 | n/a% | n/a% | n/a s | 4.988 MB | 4.988 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 131474 |  | 1 | n/a% | n/a% | n/a s | 27.383 MB | 27.383 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 131510 |  | 1 | n/a% | n/a% | n/a s | 25.707 MB | 25.707 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 131551 |  | 1 | n/a% | n/a% | n/a s | 15.414 MB | 15.414 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 131585 |  | 1 | n/a% | n/a% | n/a s | 17.492 MB | 17.492 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 131594 |  | 49 | 0.000% | 0.000% | 0.000 s | 26.707 MB | 26.707 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 131618 |  | 1 | n/a% | n/a% | n/a s | 25.469 MB | 25.469 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 131632 |  | 55 | 0.000% | 0.000% | 0.000 s | 26.738 MB | 26.738 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 131657 |  | 1 | n/a% | n/a% | n/a s | 13.938 MB | 13.938 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 131665 |  | 1 | n/a% | n/a% | n/a s | 26.578 MB | 26.578 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 131680 |  | 34 | 98.695% | 108.767% | 3.310 s | 32.318 MB | 34.473 MB | 55.937 MB | 57.461 MB | 0.003906 MB | 0.257812 MB |
| docker | 131698 |  | 1 | n/a% | n/a% | n/a s | 23.672 MB | 23.672 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 131725 |  | 1 | n/a% | n/a% | n/a s | 2.793 MB | 2.793 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 131753 |  | 3 | 18.416% | 36.833% | 0.040 s | 18.539 MB | 26.957 MB | 1118.103 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 131791 | band_0000 | 7 | 3.225% | 19.350% | 0.020 s | 2.292 MB | 12.246 MB | 225.222 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 131805 |  | 1 | n/a% | n/a% | n/a s | 8.426 MB | 8.426 MB | 42.242 MB | 42.242 MB | n/a MB | n/a MB |
| tail | 131803 | band_0000 | 6 | 0.000% | 0.000% | 0.000 s | 1.711 MB | 1.711 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 131813 |  | 1 | n/a% | n/a% | n/a s | 26.836 MB | 26.836 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 131839 |  | 1 | n/a% | n/a% | n/a s | 27.367 MB | 27.367 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| sh | 131859 | band_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 131876 |  | 1 | n/a% | n/a% | n/a s | 27.211 MB | 27.211 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 131908 |  | 1 | n/a% | n/a% | n/a s | 22.664 MB | 22.664 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 131916 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.789 MB | 25.789 MB | 1659.961 MB | 1659.961 MB | 0.000000 MB | 0.000000 MB |
| docker | 131966 |  | 1 | n/a% | n/a% | n/a s | 18.234 MB | 18.234 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 131981 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.881 MB | 27.098 MB | 1732.777 MB | 1804.781 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 132024 | bart_0000 | 5 | 7.359% | 29.435% | 0.030 s | 2.679 MB | 10.863 MB | 314.733 MB | 1569.445 MB | n/a MB | n/a MB |
| docker | 132038 |  | 1 | n/a% | n/a% | n/a s | 18.414 MB | 18.414 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 132036 | bart_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.637 MB | 1.637 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 132073 |  | 1 | n/a% | n/a% | n/a s | 25.789 MB | 25.789 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 132101 |  | 1 | n/a% | n/a% | n/a s | 27.395 MB | 27.395 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 132122 | bart_0000 | 1 | n/a% | n/a% | n/a s | 11.488 MB | 11.488 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 132137 |  | 1 | n/a% | n/a% | n/a s | 27.203 MB | 27.203 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| sh | 132157 | bart_0000 | 1 | n/a% | n/a% | n/a s | 1.535 MB | 1.535 MB | 2.617 MB | 2.617 MB | n/a MB | n/a MB |
| docker | 132173 |  | 1 | n/a% | n/a% | n/a s | 26.934 MB | 26.934 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 132230 |  | 2 | 0.000% | 0.000% | 0.000 s | 13.932 MB | 25.637 MB | 846.486 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 132270 | bart_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.584 MB | 12.438 MB | 411.474 MB | 1642.730 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 132314 | bart_0000 | 1 | n/a% | n/a% | n/a s | 10.051 MB | 10.051 MB | 1569.195 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 132295 |  | 1 | n/a% | n/a% | n/a s | 27.281 MB | 27.281 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 132284 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 132387 |  | 1 | n/a% | n/a% | n/a s | 23.031 MB | 23.031 MB | 1524.203 MB | 1524.203 MB | n/a MB | n/a MB |
| docker | 132395 |  | 1 | n/a% | n/a% | n/a s | 26.039 MB | 26.039 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 132453 |  | 1 | n/a% | n/a% | n/a s | 25.344 MB | 25.344 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker-init | 132493 | band_0000 | 11 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 132507 |  | 1 | n/a% | n/a% | n/a s | 19.809 MB | 19.809 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 132505 | band_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 132542 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.371 MB | 27.371 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| bash | 132562 | band_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.383 MB | 3.383 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 132571 | band_0000 | 8 | 99.288% | 107.944% | 0.710 s | 31.106 MB | 42.094 MB | 38.137 MB | 51.324 MB | n/a MB | n/a MB |
| docker | 132573 |  | 1 | n/a% | n/a% | n/a s | 5.656 MB | 5.656 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 132582 |  | 1 | n/a% | n/a% | n/a s | 26.871 MB | 26.871 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 132642 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.770 MB | 26.770 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 132681 | band_0000 | 4 | 3.253% | 9.760% | 0.010 s | 3.719 MB | 12.977 MB | 393.473 MB | 1570.727 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 132722 | band_0000 | 1 | n/a% | n/a% | n/a s | 11.957 MB | 11.957 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 132702 |  | 1 | n/a% | n/a% | n/a s | 27.590 MB | 27.590 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 132692 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 132757 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 132803 |  | 2 | 0.000% | 0.000% | 0.000 s | 21.486 MB | 26.012 MB | 1588.080 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 132852 |  | 1 | n/a% | n/a% | n/a s | 25.621 MB | 25.621 MB | 1596.211 MB | 1596.211 MB | n/a MB | n/a MB |
| docker | 132887 |  | 40 | 0.000% | 0.000% | 0.000 s | 24.953 MB | 25.457 MB | 1619.525 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 132903 |  | 1 | n/a% | n/a% | n/a s | 8.680 MB | 8.680 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 132919 |  | 1 | n/a% | n/a% | n/a s | 27.094 MB | 27.094 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 132934 |  | 4 | 102.095% | 108.878% | 0.310 s | 26.706 MB | 34.637 MB | 50.429 MB | 57.438 MB | 0.000000 MB | 0.253906 MB |
| docker | 132945 |  | 1 | n/a% | n/a% | n/a s | 9.277 MB | 9.277 MB | 1307.691 MB | 1307.691 MB | n/a MB | n/a MB |
| docker | 132988 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.535 MB | 27.535 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 133028 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.725 MB | 13.000 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 133043 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 133073 |  | 1 | n/a% | n/a% | n/a s | 8.543 MB | 8.543 MB | 1226.309 MB | 1226.309 MB | n/a MB | n/a MB |
| docker | 133108 |  | 1 | n/a% | n/a% | n/a s | 27.578 MB | 27.578 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 133165 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.449 MB | 11.449 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 133144 |  | 1 | n/a% | n/a% | n/a s | 27.422 MB | 27.422 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 133192 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.035 MB | 27.035 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 133212 |  | 1 | n/a% | n/a% | n/a s | 23.668 MB | 23.668 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 133239 |  | 41 | 0.000% | 0.000% | 0.000 s | 26.492 MB | 26.492 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 133278 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.516 MB | 25.516 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 133318 | base_0000 | 6 | 3.925% | 19.623% | 0.020 s | 2.568 MB | 12.242 MB | 262.583 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 133330 | base_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 133342 |  | 2 | 19.527% | 19.527% | 0.020 s | 15.430 MB | 27.457 MB | 846.768 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 133422 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.363 MB | 11.363 MB | 1497.844 MB | 1497.844 MB | n/a MB | n/a MB |
| docker | 133402 |  | 1 | n/a% | n/a% | n/a s | 26.992 MB | 26.992 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 133440 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.957 MB | 25.957 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 133497 |  | 1 | n/a% | n/a% | n/a s | 1.512 MB | 1.512 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 133524 |  | 2 | 9.785% | 9.785% | 0.010 s | 13.068 MB | 26.137 MB | 845.660 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 133564 | bart_0000 | 4 | 3.273% | 9.820% | 0.010 s | 3.504 MB | 12.117 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 133586 |  | 1 | n/a% | n/a% | n/a s | 27.516 MB | 27.516 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 133576 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 133613 |  | 1 | n/a% | n/a% | n/a s | 27.375 MB | 27.375 MB | 1733.027 MB | 1733.027 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 133634 | bart_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| docker | 133679 |  | 1 | n/a% | n/a% | n/a s | 1.074 MB | 1.074 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 133688 |  | 1 | n/a% | n/a% | n/a s | 26.934 MB | 26.934 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 133747 |  | 1 | n/a% | n/a% | n/a s | 26.543 MB | 26.543 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 133802 | bart_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 133805 |  | 1 | n/a% | n/a% | n/a s | 23.574 MB | 23.574 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker-init | 133790 | bart_0000 | 11 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 133840 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.410 MB | 27.410 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 133869 | bart_0000 | 8 | 100.761% | 107.939% | 0.720 s | 31.774 MB | 40.977 MB | 38.745 MB | 50.324 MB | n/a MB | n/a MB |
| bash | 133860 | bart_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.277 MB | 3.277 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 133879 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.176 MB | 26.176 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 133931 |  | 1 | n/a% | n/a% | n/a s | 21.184 MB | 21.184 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 133939 |  | 1 | n/a% | n/a% | n/a s | 27.211 MB | 27.211 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 133978 | bart_0000 | 4 | 6.411% | 19.232% | 0.020 s | 3.255 MB | 11.121 MB | 393.090 MB | 1569.195 MB | n/a MB | n/a MB |
| tail | 133990 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 134000 |  | 1 | n/a% | n/a% | n/a s | 18.359 MB | 18.359 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 134027 |  | 1 | n/a% | n/a% | n/a s | 27.535 MB | 27.535 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 134047 | bart_0000 | 1 | n/a% | n/a% | n/a s | 10.816 MB | 10.816 MB | 1497.707 MB | 1497.707 MB | n/a MB | n/a MB |
| docker | 134062 |  | 1 | n/a% | n/a% | n/a s | 27.250 MB | 27.250 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 134082 | bart_0000 | 1 | n/a% | n/a% | n/a s | 11.398 MB | 11.398 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 134098 |  | 1 | n/a% | n/a% | n/a s | 25.723 MB | 25.723 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 134174 |  | 1 | n/a% | n/a% | n/a s | 22.836 MB | 22.836 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 134182 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.609 MB | 25.609 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 134207 |  | 1 | n/a% | n/a% | n/a s | 26.762 MB | 26.762 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 134230 |  | 3 | 98.790% | 98.973% | 0.200 s | 28.156 MB | 33.918 MB | 51.427 MB | 56.461 MB | 0.000000 MB | 0.000000 MB |
| docker | 134232 |  | 1 | n/a% | n/a% | n/a s | 10.230 MB | 10.230 MB | 1451.949 MB | 1451.949 MB | n/a MB | n/a MB |
| docker | 134256 |  | 1 | n/a% | n/a% | n/a s | 26.898 MB | 26.898 MB | 1588.770 MB | 1588.770 MB | n/a MB | n/a MB |
| docker | 134280 |  | 2 | 9.873% | 9.873% | 0.010 s | 26.980 MB | 27.402 MB | 1732.777 MB | 1804.781 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 134323 | beam_0000 | 5 | 7.353% | 29.413% | 0.030 s | 2.748 MB | 11.207 MB | 314.733 MB | 1569.445 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 134357 |  | 1 | n/a% | n/a% | n/a s | 10.637 MB | 10.637 MB | 1569.582 MB | 1569.582 MB | n/a MB | n/a MB |
| tail | 134337 | beam_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 134339 |  | 1 | n/a% | n/a% | n/a s | 27.234 MB | 27.234 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 134394 | beam_0000 | 1 | n/a% | n/a% | n/a s | 11.520 MB | 11.520 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 134372 |  | 1 | n/a% | n/a% | n/a s | 27.414 MB | 27.414 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 134437 |  | 1 | n/a% | n/a% | n/a s | 3.645 MB | 3.645 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 134473 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.988 MB | 26.988 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 134534 |  | 1 | n/a% | n/a% | n/a s | 25.441 MB | 25.441 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 134586 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 134588 |  | 1 | n/a% | n/a% | n/a s | 22.559 MB | 22.559 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker-init | 134573 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 134623 |  | 1 | n/a% | n/a% | n/a s | 27.500 MB | 27.500 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 134678 | beam_0000 | 1 | n/a% | n/a% | n/a s | 10.273 MB | 10.273 MB | 1569.195 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 134658 |  | 1 | n/a% | n/a% | n/a s | 27.371 MB | 27.371 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 134694 |  | 1 | n/a% | n/a% | n/a s | 26.059 MB | 26.059 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 134776 |  | 47 | 0.000% | 0.000% | 0.000 s | 25.621 MB | 25.621 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 134801 |  | 1 | n/a% | n/a% | n/a s | 25.551 MB | 25.551 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 134816 |  | 47 | 0.000% | 0.000% | 0.000 s | 25.652 MB | 25.652 MB | 1659.961 MB | 1659.961 MB | 0.000000 MB | 0.000000 MB |
| docker | 134832 |  | 1 | n/a% | n/a% | n/a s | 20.020 MB | 20.020 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 134868 |  | 1 | n/a% | n/a% | n/a s | 25.992 MB | 25.992 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 134878 |  | 1 | n/a% | n/a% | n/a s | 8.844 MB | 8.844 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 134926 | base_0000 | 4 | 9.714% | 29.143% | 0.030 s | 3.241 MB | 11.066 MB | 393.215 MB | 1569.695 MB | n/a MB | n/a MB |
| docker | 134887 |  | 1 | n/a% | n/a% | n/a s | 26.984 MB | 26.984 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 134939 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 134949 |  | 1 | n/a% | n/a% | n/a s | 20.762 MB | 20.762 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 134996 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.949 MB | 11.949 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 134976 |  | 1 | n/a% | n/a% | n/a s | 27.023 MB | 27.023 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 135012 |  | 1 | n/a% | n/a% | n/a s | 26.980 MB | 26.980 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| sh | 135032 | base_0000 | 1 | n/a% | n/a% | n/a s | 1.719 MB | 1.719 MB | 2.617 MB | 2.617 MB | n/a MB | n/a MB |
| docker | 135052 |  | 1 | n/a% | n/a% | n/a s | 26.922 MB | 26.922 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| docker | 135112 |  | 1 | n/a% | n/a% | n/a s | 25.633 MB | 25.633 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 135165 |  | 1 | n/a% | n/a% | n/a s | 23.621 MB | 23.621 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker-init | 135152 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 135163 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 135200 |  | 1 | n/a% | n/a% | n/a s | 26.945 MB | 26.945 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 135237 |  | 1 | n/a% | n/a% | n/a s | 27.254 MB | 27.254 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 135258 | beam_0000 | 1 | n/a% | n/a% | n/a s | 11.781 MB | 11.781 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 135277 |  | 1 | n/a% | n/a% | n/a s | 26.180 MB | 26.180 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 135334 |  | 2 | 9.849% | 9.849% | 0.010 s | 15.770 MB | 26.602 MB | 846.768 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 135373 | base_0000 | 11 | 0.981% | 9.805% | 0.010 s | 1.714 MB | 12.523 MB | 143.752 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 135398 |  | 1 | n/a% | n/a% | n/a s | 27.363 MB | 27.363 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 135417 | base_0000 | 1 | n/a% | n/a% | n/a s | 10.918 MB | 10.918 MB | 1641.707 MB | 1641.707 MB | n/a MB | n/a MB |
| tail | 135388 | base_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| bash | 135445 | base_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.387 MB | 3.387 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 135454 | base_0000 | 8 | 99.337% | 107.909% | 0.710 s | 30.225 MB | 41.605 MB | 37.340 MB | 51.027 MB | n/a MB | n/a MB |
| docker | 135425 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.684 MB | 27.684 MB | 1661.023 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| docker | 135456 |  | 1 | n/a% | n/a% | n/a s | 3.219 MB | 3.219 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 135464 |  | 1 | n/a% | n/a% | n/a s | 27.293 MB | 27.293 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 135523 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.941 MB | 26.941 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 135564 | beam_0000 | 10 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 135576 | beam_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 135611 |  | 9 | 1.219% | 9.751% | 0.010 s | 26.311 MB | 27.527 MB | 1644.682 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 135640 | beam_0000 | 8 | 99.417% | 107.995% | 0.710 s | 31.719 MB | 41.977 MB | 38.858 MB | 52.238 MB | n/a MB | n/a MB |
| bash | 135631 | beam_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.320 MB | 3.320 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 135650 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.918 MB | 25.918 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 135710 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.664 MB | 25.664 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 135750 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 4.737 MB | 12.945 MB | 524.195 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 135763 | beam_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.773 MB | 1.773 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 135839 |  | 1 | n/a% | n/a% | n/a s | 25.598 MB | 25.598 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 135877 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.211 MB | 27.211 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 135928 |  | 1 | n/a% | n/a% | n/a s | 25.203 MB | 25.203 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 135961 |  | 40 | 0.253% | 9.864% | 0.010 s | 25.030 MB | 25.320 MB | 1656.604 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 135985 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.875 MB | 26.875 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 136042 |  | 1 | n/a% | n/a% | n/a s | 27.004 MB | 27.004 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 136027 | base_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.139 MB | 13.164 MB | 329.440 MB | 1642.980 MB | n/a MB | n/a MB |
| docker | 136064 |  | 1 | n/a% | n/a% | n/a s | 25.785 MB | 25.785 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 136072 |  | 1 | n/a% | n/a% | n/a s | 27.242 MB | 27.242 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 136056 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.699 MB | 1.699 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 136108 |  | 1 | n/a% | n/a% | n/a s | 27.316 MB | 27.316 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| python3 | 136127 |  | 5 | 86.327% | 98.194% | 0.360 s | 26.868 MB | 34.535 MB | 50.529 MB | 57.438 MB | 0.000000 MB | 0.253906 MB |
| docker | 136145 |  | 1 | n/a% | n/a% | n/a s | 26.051 MB | 26.051 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 136176 |  | 1 | n/a% | n/a% | n/a s | 15.598 MB | 15.598 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 136184 |  | 1 | n/a% | n/a% | n/a s | 27.035 MB | 27.035 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 136225 |  | 1 | n/a% | n/a% | n/a s | 26.621 MB | 26.621 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 136271 |  | 1 | n/a% | n/a% | n/a s | 1.797 MB | 1.797 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 136257 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.555 MB | 26.867 MB | 1660.523 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 136317 | base_0000 | 8 | 4.175% | 29.223% | 0.030 s | 1.975 MB | 11.371 MB | 197.166 MB | 1569.945 MB | n/a MB | n/a MB |
| docker | 136308 |  | 1 | n/a% | n/a% | n/a s | 27.062 MB | 27.062 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 136332 |  | 1 | n/a% | n/a% | n/a s | 25.719 MB | 25.719 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| tail | 136330 | base_0000 | 7 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 136367 |  | 5 | 0.000% | 0.000% | 0.000 s | 27.484 MB | 27.484 MB | 1661.023 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| bash | 136390 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.355 MB | 3.355 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 136399 | base_0000 | 4 | 97.362% | 97.430% | 0.300 s | 25.762 MB | 35.133 MB | 33.103 MB | 45.023 MB | n/a MB | n/a MB |
| docker | 136409 |  | 2 | 9.630% | 9.630% | 0.010 s | 21.230 MB | 27.016 MB | 1588.236 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 136462 |  | 1 | n/a% | n/a% | n/a s | 26.504 MB | 26.504 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 136477 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.281 MB | 27.281 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 136486 |  | 1 | n/a% | n/a% | n/a s | 8.598 MB | 8.598 MB | 1226.309 MB | 1226.309 MB | n/a MB | n/a MB |
| docker | 136520 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.832 MB | 25.832 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 136534 | bear_0000 | 6 | 3.793% | 18.966% | 0.020 s | 2.544 MB | 12.098 MB | 262.583 MB | 1570.227 MB | n/a MB | n/a MB |
| docker-init | 136576 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 136615 |  | 1 | n/a% | n/a% | n/a s | 11.039 MB | 11.039 MB | 1570.211 MB | 1570.211 MB | n/a MB | n/a MB |
| tail | 136588 | bear_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| tail | 136616 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 136590 |  | 1 | n/a% | n/a% | n/a s | 27.293 MB | 27.293 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 136665 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.898 MB | 11.898 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 136638 |  | 1 | n/a% | n/a% | n/a s | 27.336 MB | 27.336 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 136648 |  | 1 | n/a% | n/a% | n/a s | 26.625 MB | 26.625 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 136692 |  | 1 | n/a% | n/a% | n/a s | 27.523 MB | 27.523 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 136700 |  | 1 | n/a% | n/a% | n/a s | 27.234 MB | 27.234 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 136718 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.547 MB | 11.547 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 136785 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.922 MB | 11.922 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 136784 |  | 1 | n/a% | n/a% | n/a s | 8.719 MB | 8.719 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 136754 |  | 1 | n/a% | n/a% | n/a s | 27.324 MB | 27.324 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 136827 |  | 1 | n/a% | n/a% | n/a s | 27.000 MB | 27.000 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 136850 |  | 2 | 17.006% | 17.006% | 0.020 s | 22.713 MB | 27.020 MB | 1588.236 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 136904 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 136944 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.570 MB | 26.570 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 136982 | bear_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.646 MB | 12.684 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 136994 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 137005 |  | 1 | n/a% | n/a% | n/a s | 27.473 MB | 27.473 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 137070 |  | 1 | n/a% | n/a% | n/a s | 22.398 MB | 22.398 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 137107 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.094 MB | 26.094 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 137169 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.148 MB | 27.148 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 137208 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 4.810 MB | 13.164 MB | 548.197 MB | 1642.480 MB | n/a MB | n/a MB |
| tail | 137224 | bear_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 137255 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.801 MB | 11.801 MB | 1498.223 MB | 1498.223 MB | n/a MB | n/a MB |
| docker | 137234 |  | 1 | n/a% | n/a% | n/a s | 27.336 MB | 27.336 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 137299 |  | 1 | n/a% | n/a% | n/a s | 26.488 MB | 26.488 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 137307 |  | 1 | n/a% | n/a% | n/a s | 25.820 MB | 25.820 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 137369 |  | 1 | n/a% | n/a% | n/a s | 25.762 MB | 25.762 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker-init | 137410 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 137422 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 137424 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 30.523 MB | 30.523 MB | n/a MB | n/a MB |
| docker | 137457 |  | 1 | n/a% | n/a% | n/a s | 19.523 MB | 19.523 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 137499 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.088 MB | 27.188 MB | 1660.492 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 137557 |  | 2 | 9.738% | 9.738% | 0.010 s | 17.561 MB | 27.000 MB | 846.820 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 137607 | bear_0000 | 6 | 5.731% | 28.656% | 0.030 s | 2.419 MB | 11.348 MB | 250.475 MB | 1497.578 MB | n/a MB | n/a MB |
| tail | 137643 | bear_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 137630 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 137645 |  | 1 | n/a% | n/a% | n/a s | 25.426 MB | 25.426 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 137653 |  | 42 | 0.000% | 0.000% | 0.000 s | 26.859 MB | 26.859 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 137679 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.707 MB | 11.707 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 137658 |  | 1 | n/a% | n/a% | n/a s | 26.914 MB | 26.914 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 137686 |  | 1 | n/a% | n/a% | n/a s | 27.000 MB | 27.000 MB | 1733.027 MB | 1733.027 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 137706 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.828 MB | 11.828 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 137722 |  | 1 | n/a% | n/a% | n/a s | 27.121 MB | 27.121 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 137757 |  | 3 | 24.435% | 48.869% | 0.050 s | 25.771 MB | 26.926 MB | 1636.583 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 137833 |  | 1 | n/a% | n/a% | n/a s | 27.234 MB | 27.234 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 137849 |  | 4 | 98.693% | 108.757% | 0.300 s | 26.604 MB | 34.648 MB | 50.421 MB | 57.438 MB | 0.000000 MB | 0.238281 MB |
| docker | 137867 |  | 1 | n/a% | n/a% | n/a s | 27.145 MB | 27.145 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 137887 |  | 1 | n/a% | n/a% | n/a s | 26.938 MB | 26.938 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 137901 |  | 6 | 0.000% | 0.000% | 0.000 s | 27.046 MB | 27.273 MB | 1756.779 MB | 1804.781 MB | 0.000000 MB | 0.000000 MB |
| runc:[0:PARENT] | 137945 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 137944 |  | 1 | n/a% | n/a% | n/a s | 1.949 MB | 1.949 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 137946 | beef_0000 | 7 | 4.844% | 29.062% | 0.030 s | 3.999 MB | 13.164 MB | 449.385 MB | 1570.727 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 137982 |  | 1 | n/a% | n/a% | n/a s | 11.207 MB | 11.207 MB | 1641.965 MB | 1641.965 MB | n/a MB | n/a MB |
| docker | 137962 |  | 1 | n/a% | n/a% | n/a s | 27.055 MB | 27.055 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 137960 | beef_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 138000 |  | 1 | n/a% | n/a% | n/a s | 26.992 MB | 26.992 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 138049 | beef_0000 | 1 | n/a% | n/a% | n/a s | 9.457 MB | 9.457 MB | 1496.941 MB | 1496.941 MB | n/a MB | n/a MB |
| docker | 138029 |  | 1 | n/a% | n/a% | n/a s | 26.820 MB | 26.820 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 138063 |  | 1 | n/a% | n/a% | n/a s | 27.195 MB | 27.195 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 138100 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.176 MB | 26.176 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 138160 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.555 MB | 26.555 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 138199 | beef_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.768 MB | 13.172 MB | 411.411 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 138224 |  | 1 | n/a% | n/a% | n/a s | 27.191 MB | 27.191 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 138243 | beef_0000 | 1 | n/a% | n/a% | n/a s | 11.480 MB | 11.480 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 138212 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 138322 |  | 2 | 0.000% | 0.000% | 0.000 s | 21.947 MB | 25.965 MB | 1587.955 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 138388 |  | 1 | n/a% | n/a% | n/a s | 20.539 MB | 20.539 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 138402 |  | 38 | 0.000% | 0.000% | 0.000 s | 27.055 MB | 27.055 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 138444 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.090 MB | 27.090 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 138482 | bear_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.634 MB | 12.637 MB | 375.347 MB | 1498.223 MB | n/a MB | n/a MB |
| docker | 138505 |  | 1 | n/a% | n/a% | n/a s | 27.559 MB | 27.559 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 138494 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 138525 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.645 MB | 11.645 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 138569 |  | 1 | n/a% | n/a% | n/a s | 1.117 MB | 1.117 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 138607 |  | 2 | 0.000% | 0.000% | 0.000 s | 23.869 MB | 25.859 MB | 1588.080 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 138660 |  | 1 | n/a% | n/a% | n/a s | 25.520 MB | 25.520 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 138714 |  | 1 | n/a% | n/a% | n/a s | 10.305 MB | 10.305 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 138712 | bear_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.680 MB | 1.680 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 138699 | bear_0000 | 11 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 138749 |  | 9 | 1.228% | 9.821% | 0.010 s | 27.194 MB | 27.250 MB | 1660.746 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| bash | 138769 | bear_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.480 MB | 3.480 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 138778 | bear_0000 | 8 | 100.701% | 107.803% | 0.720 s | 31.477 MB | 41.004 MB | 38.655 MB | 50.340 MB | n/a MB | n/a MB |
| docker | 138788 |  | 2 | 0.000% | 0.000% | 0.000 s | 24.965 MB | 26.082 MB | 1624.207 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 138887 |  | 44 | 0.000% | 0.000% | 0.000 s | 27.016 MB | 27.016 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 138895 |  | 1 | n/a% | n/a% | n/a s | 3.332 MB | 3.332 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 138912 |  | 1 | n/a% | n/a% | n/a s | 25.445 MB | 25.445 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 138921 |  | 45 | 0.000% | 0.000% | 0.000 s | 26.762 MB | 26.762 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 138937 |  | 1 | n/a% | n/a% | n/a s | 25.703 MB | 25.703 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 138981 |  | 1 | n/a% | n/a% | n/a s | 26.883 MB | 26.883 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 138997 |  | 4 | 98.755% | 98.983% | 0.300 s | 25.642 MB | 34.613 MB | 49.703 MB | 57.434 MB | 0.000000 MB | 0.253906 MB |
| docker | 139023 |  | 1 | n/a% | n/a% | n/a s | 3.324 MB | 3.324 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 139043 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.828 MB | 25.828 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 139081 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.422 MB | 0.633 MB | 1.010 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 139096 | beef_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 139135 |  | 1 | n/a% | n/a% | n/a s | 5.656 MB | 5.656 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 139170 |  | 1 | n/a% | n/a% | n/a s | 27.484 MB | 27.484 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 139208 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.641 MB | 26.641 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 139319 |  | 1 | n/a% | n/a% | n/a s | 23.852 MB | 23.852 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 139312 | beef_0000 | 17 | 1.168% | 18.687% | 0.020 s | 1.320 MB | 12.309 MB | 93.359 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 139271 |  | 1 | n/a% | n/a% | n/a s | 25.797 MB | 25.797 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 139356 |  | 1 | n/a% | n/a% | n/a s | 4.469 MB | 4.469 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 139333 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.479 MB | 27.680 MB | 1708.776 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| tail | 139344 | beef_0000 | 16 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 139418 |  | 15 | 1.356% | 18.983% | 0.020 s | 25.570 MB | 27.215 MB | 1552.473 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 139424 | bell_0000 | 5 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| bash | 139446 | beef_0000 | 14 | 0.000% | 0.000% | 0.000 s | 3.410 MB | 3.410 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| tail | 139462 | bell_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.681 MB | 1.738 MB | 2.910 MB | 2.984 MB | n/a MB | n/a MB |
| python | 139458 | beef_0000 | 14 | 89.066% | 104.562% | 1.230 s | 31.075 MB | 42.648 MB | 38.332 MB | 52.238 MB | n/a MB | n/a MB |
| docker | 139492 |  | 1 | n/a% | n/a% | n/a s | 6.344 MB | 6.344 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 139555 |  | 1 | n/a% | n/a% | n/a s | 14.133 MB | 14.133 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 139601 |  | 1 | n/a% | n/a% | n/a s | 25.891 MB | 25.891 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 139647 |  | 1 | n/a% | n/a% | n/a s | 19.527 MB | 19.527 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 139655 |  | 1 | n/a% | n/a% | n/a s | 27.000 MB | 27.000 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 139692 | bell_0000 | 5 | 9.532% | 38.126% | 0.040 s | 2.725 MB | 11.094 MB | 314.683 MB | 1569.195 MB | n/a MB | n/a MB |
| tail | 139707 | bell_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 139709 |  | 1 | n/a% | n/a% | n/a s | 25.527 MB | 25.527 MB | 1596.211 MB | 1596.211 MB | n/a MB | n/a MB |
| docker | 139771 |  | 1 | n/a% | n/a% | n/a s | 6.219 MB | 6.219 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 139780 |  | 1 | n/a% | n/a% | n/a s | 27.727 MB | 27.727 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| sh | 139799 | bell_0000 | 1 | n/a% | n/a% | n/a s | 1.422 MB | 1.422 MB | 2.617 MB | 2.617 MB | n/a MB | n/a MB |
| docker | 139815 |  | 1 | n/a% | n/a% | n/a s | 25.984 MB | 25.984 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 139854 |  | 1 | n/a% | n/a% | n/a s | 15.562 MB | 15.562 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 139873 |  | 1 | n/a% | n/a% | n/a s | 26.828 MB | 26.828 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 139932 |  | 1 | n/a% | n/a% | n/a s | 26.949 MB | 26.949 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 139985 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.809 MB | 1.809 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 139973 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 140023 |  | 1 | n/a% | n/a% | n/a s | 22.508 MB | 22.508 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 140059 |  | 1 | n/a% | n/a% | n/a s | 27.402 MB | 27.402 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 140078 | beef_0000 | 1 | n/a% | n/a% | n/a s | 9.480 MB | 9.480 MB | 1569.195 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 140094 |  | 1 | n/a% | n/a% | n/a s | 26.043 MB | 26.043 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 140179 |  | 40 | 0.000% | 0.000% | 0.000 s | 26.664 MB | 26.664 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 140204 |  | 1 | n/a% | n/a% | n/a s | 0.129 MB | 0.129 MB | 30.570 MB | 30.570 MB | n/a MB | n/a MB |
| docker | 140220 |  | 1 | n/a% | n/a% | n/a s | 23.387 MB | 23.387 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| python3 | 140227 |  | 4 | 101.815% | 108.189% | 0.310 s | 28.144 MB | 34.742 MB | 51.767 MB | 57.438 MB | 0.000000 MB | 0.253906 MB |
| docker | 140229 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.129 MB | 0.129 MB | n/a MB | n/a MB |
| docker | 140254 |  | 1 | n/a% | n/a% | n/a s | 25.469 MB | 25.469 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 140292 |  | 38 | 0.265% | 9.819% | 0.010 s | 26.373 MB | 26.965 MB | 1617.931 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 140308 |  | 1 | n/a% | n/a% | n/a s | 26.594 MB | 26.594 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 140335 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.293 MB | 25.293 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 140376 | bell_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 140388 | bell_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 140428 |  | 1 | n/a% | n/a% | n/a s | 16.238 MB | 16.238 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 140465 |  | 1 | n/a% | n/a% | n/a s | 27.543 MB | 27.543 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 140504 |  | 1 | n/a% | n/a% | n/a s | 26.043 MB | 26.043 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 140546 |  | 1 | n/a% | n/a% | n/a s | 25.816 MB | 25.816 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 140563 |  | 1 | n/a% | n/a% | n/a s | 25.457 MB | 25.457 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker-init | 140603 | bell_0000 | 10 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 140614 | bell_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 140618 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 140672 | bell_0000 | 9 | 2.417% | 19.339% | 0.020 s | 4.031 MB | 10.562 MB | 178.286 MB | 1569.445 MB | n/a MB | n/a MB |
| docker | 140652 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.598 MB | 27.598 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 140681 | bell_0000 | 8 | 99.359% | 107.829% | 0.710 s | 33.029 MB | 42.582 MB | 40.125 MB | 52.238 MB | n/a MB | n/a MB |
| docker | 140691 |  | 1 | n/a% | n/a% | n/a s | 27.074 MB | 27.074 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 140778 |  | 1 | n/a% | n/a% | n/a s | 25.977 MB | 25.977 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 140787 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.605 MB | 26.605 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 140804 |  | 1 | n/a% | n/a% | n/a s | 6.406 MB | 6.406 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| run23:repair_bu | 140830 |  | 1 | n/a% | n/a% | n/a s | 706.172 MB | 706.172 MB | 4032.445 MB | 4032.445 MB | n/a MB | n/a MB |
| python3 | 140837 |  | 4 | 98.679% | 98.912% | 0.300 s | 28.044 MB | 34.598 MB | 51.786 MB | 57.438 MB | 0.000000 MB | 0.253906 MB |
| docker | 140839 |  | 1 | n/a% | n/a% | n/a s | 16.395 MB | 16.395 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 140864 |  | 1 | n/a% | n/a% | n/a s | 25.656 MB | 25.656 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |

## GPU metrics

_No GPU samples were collected._

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| alex_0000 | 57.352% | 101.807% | 1.612 s | 9.393 MB | 35.281 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| andy_0000 | 53.935% | 100.154% | 1.630 s | 9.092 MB | 36.281 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| arch_0000 | 58.737% | 100.295% | 1.208 s | 9.117 MB | 36.211 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bake_0000 | 59.225% | 118.189% | 1.994 s | 10.190 MB | 34.648 MB | 0.000000 MB | 0.003906 MB | 7123.655673 MB | 75.223331 MB |
| bale_0000 | 85.331% | 100.978% | 3.920 s | 23.667 MB | 35.156 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| band_0000 | 55.838% | 100.777% | 1.490 s | 7.746 MB | 35.586 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bart_0000 | 61.484% | 100.072% | 1.324 s | 9.468 MB | 34.594 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| base_0000 | 57.627% | 100.308% | 1.960 s | 8.419 MB | 35.184 MB | 0.000000 MB | 0.007812 MB | 0.000000 MB | 0.000000 MB |
| beam_0000 | 62.600% | 100.153% | 1.153 s | 10.179 MB | 35.461 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bear_0000 | 51.834% | 99.994% | 1.499 s | 7.289 MB | 34.289 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| beef_0000 | 61.920% | 98.906% | 1.698 s | 12.394 MB | 36.289 MB | 0.000000 MB | 1.843750 MB | 0.000000 MB | 0.000000 MB |
| bell_0000 | 64.694% | 100.028% | 1.133 s | 11.145 MB | 36.215 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |

## Incomplete spans

_No spans were still open when profiling stopped._

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sync:result_wait | 24/24 | 0 | 0 | 691.606 | 0.005 | 691.597 | 28816.898 | 27079.774 | 44772.209 |
| turn | 80/80 | 0 | 0 | 583.092 | 2.650 | 579.922 | 7288.652 | 4588.657 | 25702.702 |
| llm:attempt | 80/80 | 0 | 0 | 521.162 | 2.159 | 518.644 | 6514.525 | 3716.637 | 25668.916 |
| run:diagnose_bug | 12/12 | 0 | 0 | 419.929 | 1.442 | 418.154 | 34994.100 | 34210.172 | 49351.404 |
| llm:diagnose_bug | 29/29 | 0 | 0 | 342.695 | 1.136 | 341.331 | 11817.080 | 4948.225 | 31921.729 |
| run:repair_bug | 12/12 | 0 | 0 | 271.686 | 1.364 | 270.107 | 22640.524 | 20154.792 | 32448.267 |
| llm:repair_bug | 51/51 | 0 | 0 | 178.490 | 1.046 | 177.314 | 3499.811 | 3093.036 | 5966.527 |
| teardown:commit | 24/24 | 0 | 0 | 108.329 | 0.086 | 108.220 | 4513.697 | 4302.429 | 5259.667 |
| sandbox:commit | 24/24 | 0 | 0 | 107.774 | 0.073 | 107.685 | 4490.601 | 4277.456 | 5232.377 |
| capstone:plan:find_first_in_sorted | 1/1 | 0 | 0 | 54.552 | 0.001 | 54.551 | 54551.819 | 54551.819 | 54551.819 |
| capstone:plan:flatten | 1/1 | 0 | 0 | 45.097 | 0.001 | 45.096 | 45096.672 | 45096.672 | 45096.672 |
| capstone:plan:mergesort | 1/1 | 0 | 0 | 42.939 | 0.001 | 42.938 | 42938.954 | 42938.954 | 42938.954 |
| tool_dispatch:repair_bug | 51/51 | 0 | 0 | 39.105 | 0.223 | 38.816 | 766.769 | 609.426 | 1886.744 |
| capstone:build:find_first_in_sorted | 1/1 | 0 | 0 | 38.378 | 0.001 | 38.377 | 38377.824 | 38377.824 | 38377.824 |
| capstone:plan:powerset | 1/1 | 0 | 0 | 37.215 | 0.001 | 37.213 | 37214.588 | 37214.588 | 37214.588 |
| capstone:plan:bucketsort | 1/1 | 0 | 0 | 35.223 | 0.001 | 35.222 | 35222.657 | 35222.657 | 35222.657 |
| capstone:plan:rpn_eval | 1/1 | 0 | 0 | 34.759 | 0.001 | 34.758 | 34759.128 | 34759.128 | 34759.128 |
| capstone:plan:next_palindrome | 1/1 | 0 | 0 | 33.662 | 0.001 | 33.661 | 33661.721 | 33661.721 | 33661.721 |
| capstone:plan:bitcount | 1/1 | 0 | 0 | 31.743 | 0.001 | 31.742 | 31743.116 | 31743.116 | 31743.116 |
| capstone:plan:levenshtein | 1/1 | 0 | 0 | 28.339 | 0.001 | 28.338 | 28339.119 | 28339.119 | 28339.119 |
| capstone:plan:hanoi | 1/1 | 0 | 0 | 28.114 | 0.001 | 28.113 | 28113.709 | 28113.709 | 28113.709 |
| capstone:build:mergesort | 1/1 | 0 | 0 | 27.598 | 0.000 | 27.597 | 27597.538 | 27597.538 | 27597.538 |
| capstone:build:levenshtein | 1/1 | 0 | 0 | 26.563 | 0.001 | 26.562 | 26562.995 | 26562.995 | 26562.995 |
| capstone:plan:gcd | 1/1 | 0 | 0 | 24.817 | 0.001 | 24.817 | 24817.403 | 24817.403 | 24817.403 |
| capstone:plan:is_valid_parenthesization | 1/1 | 0 | 0 | 23.474 | 0.001 | 23.473 | 23474.015 | 23474.015 | 23474.015 |
| capstone:build:next_palindrome | 1/1 | 0 | 0 | 22.854 | 0.001 | 22.852 | 22853.636 | 22853.636 | 22853.636 |
| tool_dispatch:diagnose_bug | 29/29 | 0 | 0 | 22.735 | 0.189 | 22.458 | 783.978 | 603.647 | 1959.578 |
| capstone:build:is_valid_parenthesization | 1/1 | 0 | 0 | 21.538 | 0.000 | 21.537 | 21538.296 | 21538.296 | 21538.296 |
| tool:read | 37/37 | 0 | 0 | 21.408 | 0.167 | 21.163 | 578.583 | 559.707 | 979.752 |
| sandbox:start | 65/65 | 0 | 0 | 20.963 | 0.110 | 20.790 | 322.500 | 257.664 | 531.995 |
| capstone:build:rpn_eval | 1/1 | 0 | 0 | 20.211 | 0.000 | 20.210 | 20210.745 | 20210.745 | 20210.745 |
| capstone:build:powerset | 1/1 | 0 | 0 | 20.099 | 0.001 | 20.099 | 20099.283 | 20099.283 | 20099.283 |
| sandbox:exec | 15/15 | 0 | 0 | 20.090 | 0.035 | 20.042 | 1339.366 | 1167.456 | 2468.096 |
| tool:bash | 13/13 | 0 | 0 | 19.429 | 0.038 | 19.378 | 1494.516 | 1172.054 | 2670.177 |
| capstone:build:hanoi | 1/1 | 0 | 0 | 19.413 | 0.001 | 19.412 | 19412.734 | 19412.734 | 19412.734 |
| capstone:build:bitcount | 1/1 | 0 | 0 | 19.400 | 0.000 | 19.400 | 19400.405 | 19400.405 | 19400.405 |
| capstone:build:flatten | 1/1 | 0 | 0 | 18.998 | 0.001 | 18.998 | 18998.136 | 18998.136 | 18998.136 |
| capstone:build:gcd | 1/1 | 0 | 0 | 18.505 | 0.001 | 18.504 | 18504.696 | 18504.696 | 18504.696 |
| capstone:build:bucketsort | 1/1 | 0 | 0 | 18.132 | 0.001 | 18.131 | 18131.741 | 18131.741 | 18131.741 |
| sandbox:stop | 128/128 | 0 | 0 | 14.244 | 0.106 | 14.088 | 111.282 | 163.259 | 237.594 |
| capstone:prepare:bitcount | 1/1 | 0 | 0 | 10.182 | 0.048 | 10.134 | 10182.152 | 10182.152 | 10182.152 |
| capstone:prepare:find_first_in_sorted | 1/1 | 0 | 0 | 10.044 | 0.033 | 10.011 | 10044.401 | 10044.401 | 10044.401 |
| sandbox:read_file | 50/50 | 0 | 0 | 9.072 | 0.076 | 8.964 | 181.449 | 121.409 | 471.587 |
| capstone:prepare:mergesort | 1/1 | 0 | 0 | 8.632 | 0.042 | 8.588 | 8631.769 | 8631.769 | 8631.769 |
| tool:edit | 13/13 | 0 | 0 | 6.589 | 0.056 | 6.516 | 506.878 | 427.947 | 751.980 |
| capstone:verify:levenshtein | 1/1 | 0 | 0 | 3.428 | 0.001 | 3.427 | 3428.419 | 3428.419 | 3428.419 |
| capstone:scheduler:tick | 372/372 | 0 | 0 | 2.874 | 0.662 | 2.209 | 7.725 | 0.195 | 0.590 |
| agent:create | 12/12 | 0 | 0 | 2.748 | 0.579 | 2.167 | 228.966 | 138.175 | 667.669 |
| capstone:prepare:levenshtein | 1/1 | 0 | 0 | 2.582 | 0.030 | 2.552 | 2581.614 | 2581.614 | 2581.614 |
| sandbox:destroy | 12/12 | 0 | 0 | 1.505 | 0.019 | 1.480 | 125.451 | 119.070 | 162.835 |
| sandbox:write_file | 13/13 | 0 | 0 | 1.424 | 0.014 | 1.404 | 109.512 | 93.052 | 155.750 |
| tool:glob | 2/2 | 0 | 0 | 0.670 | 0.005 | 0.664 | 334.894 | 334.894 | 337.203 |
| capstone:verify:bitcount | 1/1 | 0 | 0 | 0.639 | 0.001 | 0.637 | 638.629 | 638.629 | 638.629 |
| capstone:verify:hanoi | 1/1 | 0 | 0 | 0.572 | 0.001 | 0.569 | 571.584 | 571.584 | 571.584 |
| capstone:prepare:gcd | 1/1 | 0 | 0 | 0.468 | 0.030 | 0.437 | 467.598 | 467.598 | 467.598 |
| capstone:prepare:powerset | 1/1 | 0 | 0 | 0.466 | 0.032 | 0.434 | 466.180 | 466.180 | 466.180 |
| capstone:prepare:bucketsort | 1/1 | 0 | 0 | 0.462 | 0.032 | 0.430 | 462.248 | 462.248 | 462.248 |
| capstone:prepare:hanoi | 1/1 | 0 | 0 | 0.453 | 0.030 | 0.423 | 453.044 | 453.044 | 453.044 |
| capstone:prepare:flatten | 1/1 | 0 | 0 | 0.438 | 0.031 | 0.407 | 438.039 | 438.039 | 438.039 |
| capstone:prepare:next_palindrome | 1/1 | 0 | 0 | 0.436 | 0.030 | 0.406 | 436.276 | 436.276 | 436.276 |
| capstone:prepare:is_valid_parenthesization | 1/1 | 0 | 0 | 0.433 | 0.032 | 0.400 | 433.382 | 433.382 | 433.382 |
| capstone:prepare:rpn_eval | 1/1 | 0 | 0 | 0.430 | 0.030 | 0.400 | 430.298 | 430.298 | 430.298 |
| capstone:verify:find_first_in_sorted | 1/1 | 0 | 0 | 0.405 | 0.001 | 0.403 | 404.760 | 404.760 | 404.760 |
| capstone:verify:gcd | 1/1 | 0 | 0 | 0.403 | 0.001 | 0.402 | 403.239 | 403.239 | 403.239 |
| capstone:verify:powerset | 1/1 | 0 | 0 | 0.402 | 0.001 | 0.401 | 401.947 | 401.947 | 401.947 |
| capstone:verify:mergesort | 1/1 | 0 | 0 | 0.400 | 0.001 | 0.399 | 400.346 | 400.346 | 400.346 |
| capstone:verify:flatten | 1/1 | 0 | 0 | 0.391 | 0.001 | 0.390 | 391.290 | 391.290 | 391.290 |
| capstone:verify:rpn_eval | 1/1 | 0 | 0 | 0.390 | 0.001 | 0.389 | 390.031 | 390.031 | 390.031 |
| capstone:verify:bucketsort | 1/1 | 0 | 0 | 0.386 | 0.001 | 0.384 | 385.651 | 385.651 | 385.651 |
| capstone:verify:next_palindrome | 1/1 | 0 | 0 | 0.382 | 0.001 | 0.380 | 381.546 | 381.546 | 381.546 |
| capstone:verify:is_valid_parenthesization | 1/1 | 0 | 0 | 0.377 | 0.001 | 0.376 | 377.459 | 377.459 | 377.459 |
| sync:container | 863/863 | 0 | 0 | 0.134 | 0.121 | 0.007 | 0.155 | 0.133 | 0.250 |
| sandbox:provision | 12/12 | 0 | 0 | 0.101 | 0.009 | 0.092 | 8.416 | 0.436 | 43.461 |
| sandbox:create | 12/12 | 0 | 0 | 0.098 | 0.006 | 0.092 | 8.179 | 0.309 | 42.875 |
| run:detect | 1/1 | 0 | 0 | 0.040 | 0.001 | 0.039 | 39.966 | 39.966 | 39.966 |
| prune | 24/24 | 0 | 0 | 0.007 | 0.004 | 0.004 | 0.309 | 0.248 | 0.579 |
| tool:return_summary | 15/15 | 3 | 0 | 0.005 | 0.005 | 0.000 | 0.351 | 0.338 | 0.467 |
| tool:return_plan | 12/12 | 0 | 0 | 0.004 | 0.004 | 0.000 | 0.338 | 0.305 | 0.548 |
| llm:sync | 80/80 | 0 | 0 | 0.004 | 0.004 | 0.000 | 0.049 | 0.039 | 0.092 |
| tool:return_status | 12/12 | 0 | 0 | 0.003 | 0.003 | 0.000 | 0.282 | 0.271 | 0.355 |
| agsync:join | 12/12 | 0 | 0 | 0.003 | 0.003 | 0.000 | 0.228 | 0.227 | 0.255 |
| proc_wait | 24/24 | 0 | 0 | 0.003 | 0.002 | 0.000 | 0.114 | 0.068 | 0.100 |
| input:prepare | 24/24 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.092 | 0.088 | 0.127 |
| agprof:clock_sync | 1/1 | 0 | 0 | 0.002 | 0.001 | 0.001 | 1.933 | 1.933 | 1.933 |
| resolve | 24/24 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.071 | 0.066 | 0.097 |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 3656 | 39.771 | 0.000 | 199.943 | 23.916 | 148.106485 CPU seconds | n/a |
| python3 (PID 124202) CPU | percent | 4074 | 5.361 | 0.000 | 107.355 | 9.781 | 22.440000 CPU seconds | n/a |
| python3 (PID 124202) io read MB/s | MB/s | 4074 | 0.052 | 0.000 | 27.713 | 0.000 | 22.195312 MB | n/a |
| python3 (PID 124202) io write MB/s | MB/s | 4074 | 0.085 | 0.000 | 22.836 | 0.000 | 35.070312 MB | n/a |
| python3 (PID 124202) rss_mb | MB | 4075 | 689.733 | 612.539 | 706.297 | 706.297 | n/a | n/a |
| python3 (PID 124202) vms_mb | MB | 4075 | 3937.487 | 3407.562 | 4046.309 | 4016.406 | n/a | n/a |
| git (PID 124208) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| git (PID 124208) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 124208) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 124208) rss_mb | MB | 2 | 4.742 | 4.742 | 4.742 | 4.742 | n/a | n/a |
| git (PID 124208) vms_mb | MB | 2 | 12.516 | 12.516 | 12.516 | 12.516 | n/a | n/a |
| git (PID 124209) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| git (PID 124209) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 124209) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 124209) rss_mb | MB | 2 | 3.391 | 3.391 | 3.391 | 3.391 | n/a | n/a |
| git (PID 124209) vms_mb | MB | 2 | 11.273 | 11.273 | 11.273 | 11.273 | n/a | n/a |
| git-remote-http (PID 124210) CPU | percent | 1 | 19.758 | 19.758 | 19.758 | 19.758 | 0.020000 CPU seconds | n/a |
| git-remote-http (PID 124210) io read MB/s | MB/s | 1 | 2.933 | 2.933 | 2.933 | 2.933 | 0.296875 MB | n/a |
| git-remote-http (PID 124210) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git-remote-http (PID 124210) rss_mb | MB | 2 | 19.021 | 18.941 | 19.102 | 19.102 | n/a | n/a |
| git-remote-http (PID 124210) vms_mb | MB | 2 | 106.566 | 106.566 | 106.566 | 106.566 | n/a | n/a |
| python3 (PID 124216) CPU | percent | 98 | 99.879 | 98.845 | 109.034 | 99.150 | 9.880000 CPU seconds | n/a |
| python3 (PID 124216) io read MB/s | MB/s | 98 | 0.024 | 0.000 | 2.399 | 0.000 | 0.242188 MB | n/a |
| python3 (PID 124216) io write MB/s | MB/s | 98 | 0.002 | 0.000 | 0.155 | 0.000 | 0.015625 MB | n/a |
| python3 (PID 124216) rss_mb | MB | 99 | 33.903 | 14.070 | 34.223 | 34.223 | n/a | n/a |
| python3 (PID 124216) vms_mb | MB | 99 | 57.171 | 39.566 | 57.457 | 57.457 | n/a | n/a |
| python3 (PID 124217) CPU | percent | 3 | 98.995 | 98.943 | 99.069 | 98.943 | 0.300000 CPU seconds | n/a |
| python3 (PID 124217) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 124217) io write MB/s | MB/s | 3 | 0.863 | 0.000 | 2.435 | 2.435 | 0.261719 MB | n/a |
| python3 (PID 124217) rss_mb | MB | 4 | 29.606 | 20.887 | 34.965 | 34.965 | n/a | n/a |
| python3 (PID 124217) vms_mb | MB | 4 | 53.112 | 45.371 | 57.457 | 57.457 | n/a | n/a |
| python3 (PID 124218) CPU | percent | 3 | 102.031 | 89.111 | 108.878 | 108.104 | 0.310000 CPU seconds | n/a |
| python3 (PID 124218) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 124218) io write MB/s | MB/s | 3 | 0.857 | 0.000 | 2.572 | 2.572 | 0.261719 MB | n/a |
| python3 (PID 124218) rss_mb | MB | 4 | 28.198 | 17.254 | 36.312 | 36.312 | n/a | n/a |
| python3 (PID 124218) vms_mb | MB | 4 | 52.201 | 42.301 | 59.516 | 59.516 | n/a | n/a |
| python3 (PID 124219) CPU | percent | 3 | 102.328 | 98.921 | 108.986 | 108.986 | 0.310000 CPU seconds | n/a |
| python3 (PID 124219) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 124219) io write MB/s | MB/s | 3 | 0.864 | 0.000 | 2.438 | 2.438 | 0.261719 MB | n/a |
| python3 (PID 124219) rss_mb | MB | 4 | 29.744 | 21.277 | 35.098 | 35.098 | n/a | n/a |
| python3 (PID 124219) vms_mb | MB | 4 | 53.162 | 45.531 | 57.496 | 57.496 | n/a | n/a |
| python3 (PID 124220) CPU | percent | 24 | 99.869 | 98.879 | 108.999 | 99.020 | 2.420000 CPU seconds | n/a |
| python3 (PID 124220) io read MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 124220) io write MB/s | MB/s | 24 | 0.108 | 0.000 | 2.437 | 2.437 | 0.261719 MB | n/a |
| python3 (PID 124220) rss_mb | MB | 25 | 33.437 | 18.082 | 34.926 | 34.926 | n/a | n/a |
| python3 (PID 124220) vms_mb | MB | 25 | 56.563 | 42.566 | 57.508 | 57.508 | n/a | n/a |
| python3 (PID 124221) CPU | percent | 84 | 99.883 | 88.614 | 108.958 | 99.056 | 8.490000 CPU seconds | n/a |
| python3 (PID 124221) io read MB/s | MB/s | 84 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 124221) io write MB/s | MB/s | 84 | 0.032 | 0.000 | 2.515 | 0.000 | 0.269531 MB | n/a |
| python3 (PID 124221) rss_mb | MB | 85 | 40.742 | 9.086 | 47.484 | 47.414 | n/a | n/a |
| python3 (PID 124221) vms_mb | MB | 85 | 63.670 | 35.328 | 70.586 | 70.586 | n/a | n/a |
| python3 (PID 124222) CPU | percent | 3 | 99.003 | 98.949 | 99.067 | 99.067 | 0.300000 CPU seconds | n/a |
| python3 (PID 124222) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 124222) io write MB/s | MB/s | 3 | 0.890 | 0.000 | 2.631 | 2.631 | 0.269531 MB | n/a |
| python3 (PID 124222) rss_mb | MB | 4 | 28.827 | 18.711 | 35.117 | 35.117 | n/a | n/a |
| python3 (PID 124222) vms_mb | MB | 4 | 52.150 | 43.699 | 57.508 | 57.508 | n/a | n/a |
| python3 (PID 124223) CPU | percent | 98 | 99.972 | 98.676 | 109.050 | 99.128 | 9.890000 CPU seconds | n/a |
| python3 (PID 124223) io read MB/s | MB/s | 98 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 124223) io write MB/s | MB/s | 98 | 0.002 | 0.000 | 0.155 | 0.000 | 0.015625 MB | n/a |
| python3 (PID 124223) rss_mb | MB | 99 | 34.028 | 10.852 | 34.426 | 34.426 | n/a | n/a |
| python3 (PID 124223) vms_mb | MB | 99 | 57.100 | 36.633 | 57.457 | 57.457 | n/a | n/a |
| python3 (PID 124224) CPU | percent | 3 | 99.023 | 89.153 | 108.969 | 89.153 | 0.300000 CPU seconds | n/a |
| python3 (PID 124224) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 124224) io write MB/s | MB/s | 3 | 0.890 | 0.000 | 2.631 | 2.631 | 0.269531 MB | n/a |
| python3 (PID 124224) rss_mb | MB | 4 | 28.747 | 18.516 | 35.027 | 35.027 | n/a | n/a |
| python3 (PID 124224) vms_mb | MB | 4 | 51.864 | 42.566 | 57.496 | 57.496 | n/a | n/a |
| python3 (PID 124225) CPU | percent | 3 | 99.022 | 98.953 | 99.058 | 99.058 | 0.300000 CPU seconds | n/a |
| python3 (PID 124225) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 124225) io write MB/s | MB/s | 3 | 0.890 | 0.000 | 2.670 | 2.670 | 0.269531 MB | n/a |
| python3 (PID 124225) rss_mb | MB | 4 | 25.085 | 11.633 | 34.863 | 34.863 | n/a | n/a |
| python3 (PID 124225) vms_mb | MB | 4 | 49.001 | 37.938 | 57.496 | 57.496 | n/a | n/a |
| python3 (PID 124226) CPU | percent | 3 | 102.297 | 99.017 | 108.849 | 99.017 | 0.310000 CPU seconds | n/a |
| python3 (PID 124226) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 124226) io write MB/s | MB/s | 3 | 0.890 | 0.000 | 2.630 | 2.630 | 0.269531 MB | n/a |
| python3 (PID 124226) rss_mb | MB | 4 | 29.481 | 21.012 | 35.070 | 35.070 | n/a | n/a |
| python3 (PID 124226) vms_mb | MB | 4 | 52.818 | 45.371 | 57.508 | 57.508 | n/a | n/a |
| python3 (PID 124227) CPU | percent | 3 | 102.299 | 98.929 | 108.838 | 99.130 | 0.310000 CPU seconds | n/a |
| python3 (PID 124227) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 124227) io write MB/s | MB/s | 3 | 0.891 | 0.000 | 2.672 | 2.672 | 0.269531 MB | n/a |
| python3 (PID 124227) rss_mb | MB | 4 | 25.538 | 12.258 | 34.801 | 34.801 | n/a | n/a |
| python3 (PID 124227) vms_mb | MB | 4 | 49.624 | 38.164 | 57.457 | 57.457 | n/a | n/a |
| docker (PID 124231) rss_mb | MB | 1 | 4.160 | 4.160 | 4.160 | 4.160 | n/a | n/a |
| docker (PID 124231) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 124287) CPU | percent | 3 | 6.591 | 0.000 | 19.772 | 0.000 | 0.020000 CPU seconds | n/a |
| docker (PID 124287) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 124287) io write MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 124287) rss_mb | MB | 4 | 27.152 | 26.809 | 27.496 | 27.496 | n/a | n/a |
| docker (PID 124287) vms_mb | MB | 4 | 1696.775 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 124311) CPU | percent | 2 | 4.943 | 0.000 | 9.886 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 124311) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 124311) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 124311) rss_mb | MB | 3 | 27.600 | 27.285 | 27.758 | 27.758 | n/a | n/a |
| docker (PID 124311) vms_mb | MB | 3 | 1708.776 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [andy_0000] (PID 124380) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 124380) rss_mb | MB | 7 | 2.390 | 0.633 | 12.930 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 124380) vms_mb | MB | 7 | 225.258 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| docker-init [alex_0000] (PID 124391) CPU | percent | 5 | 1.966 | 0.000 | 9.830 | 0.000 | 0.010000 CPU seconds | n/a |
| docker-init [alex_0000] (PID 124391) rss_mb | MB | 6 | 2.600 | 0.633 | 12.434 | 0.633 | n/a | n/a |
| docker-init [alex_0000] (PID 124391) vms_mb | MB | 6 | 262.583 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 124404) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 124404) rss_mb | MB | 6 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [andy_0000] (PID 124404) vms_mb | MB | 6 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 124408) rss_mb | MB | 1 | 27.219 | 27.219 | 27.219 | 27.219 | n/a | n/a |
| docker (PID 124408) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| tail [alex_0000] (PID 124413) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 124413) rss_mb | MB | 5 | 1.809 | 1.809 | 1.809 | 1.809 | n/a | n/a |
| tail [alex_0000] (PID 124413) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 124415) rss_mb | MB | 1 | 27.234 | 27.234 | 27.234 | 27.234 | n/a | n/a |
| docker (PID 124415) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 124486) rss_mb | MB | 1 | 18.461 | 18.461 | 18.461 | 18.461 | n/a | n/a |
| docker (PID 124486) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 124488) rss_mb | MB | 1 | 13.324 | 13.324 | 13.324 | 13.324 | n/a | n/a |
| docker (PID 124488) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 124541) rss_mb | MB | 1 | 23.852 | 23.852 | 23.852 | 23.852 | n/a | n/a |
| docker (PID 124541) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 124543) rss_mb | MB | 1 | 17.891 | 17.891 | 17.891 | 17.891 | n/a | n/a |
| docker (PID 124543) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 124594) rss_mb | MB | 1 | 23.738 | 23.738 | 23.738 | 23.738 | n/a | n/a |
| docker (PID 124594) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 124596) rss_mb | MB | 1 | 23.703 | 23.703 | 23.703 | 23.703 | n/a | n/a |
| docker (PID 124596) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 124611) rss_mb | MB | 1 | 27.199 | 27.199 | 27.199 | 27.199 | n/a | n/a |
| docker (PID 124611) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 124613) rss_mb | MB | 1 | 27.109 | 27.109 | 27.109 | 27.109 | n/a | n/a |
| docker (PID 124613) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 124642) rss_mb | MB | 1 | 11.805 | 11.805 | 11.805 | 11.805 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 124642) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 124659) rss_mb | MB | 1 | 10.684 | 10.684 | 10.684 | 10.684 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 124659) vms_mb | MB | 1 | 1569.582 | 1569.582 | 1569.582 | 1569.582 | n/a | n/a |
| docker (PID 124684) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 124684) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 124684) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 124684) rss_mb | MB | 2 | 27.145 | 27.145 | 27.145 | 27.145 | n/a | n/a |
| docker (PID 124684) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 124693) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 124693) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 124693) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 124693) rss_mb | MB | 2 | 26.742 | 26.742 | 26.742 | 26.742 | n/a | n/a |
| docker (PID 124693) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 124785) rss_mb | MB | 1 | 26.844 | 26.844 | 26.844 | 26.844 | n/a | n/a |
| docker (PID 124785) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 124799) rss_mb | MB | 1 | 25.742 | 25.742 | 25.742 | 25.742 | n/a | n/a |
| docker (PID 124799) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 124801) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 124801) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 124801) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 124801) rss_mb | MB | 2 | 25.402 | 25.402 | 25.402 | 25.402 | n/a | n/a |
| docker (PID 124801) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 124879) CPU | percent | 4 | 7.256 | 0.000 | 29.023 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 124879) rss_mb | MB | 5 | 1.297 | 0.633 | 3.953 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 124879) vms_mb | MB | 5 | 242.579 | 1.055 | 1208.676 | 1.055 | n/a | n/a |
| docker-init [andy_0000] (PID 124886) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 124886) rss_mb | MB | 5 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 124886) vms_mb | MB | 5 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 124899) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 124899) rss_mb | MB | 4 | 1.574 | 1.574 | 1.574 | 1.574 | n/a | n/a |
| tail [alex_0000] (PID 124899) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 124907) rss_mb | MB | 1 | 17.727 | 17.727 | 17.727 | 17.727 | n/a | n/a |
| docker (PID 124907) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| tail [andy_0000] (PID 124908) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 124908) rss_mb | MB | 5 | 1.672 | 1.672 | 1.672 | 1.672 | n/a | n/a |
| tail [andy_0000] (PID 124908) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 124934) rss_mb | MB | 1 | 27.055 | 27.055 | 27.055 | 27.055 | n/a | n/a |
| docker (PID 124934) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 124973) rss_mb | MB | 1 | 10.863 | 10.863 | 10.863 | 10.863 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 124973) vms_mb | MB | 1 | 1497.707 | 1497.707 | 1497.707 | 1497.707 | n/a | n/a |
| docker (PID 124993) rss_mb | MB | 1 | 27.180 | 27.180 | 27.180 | 27.180 | n/a | n/a |
| docker (PID 124993) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 125026) rss_mb | MB | 1 | 11.703 | 11.703 | 11.703 | 11.703 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 125026) vms_mb | MB | 1 | 1570.219 | 1570.219 | 1570.219 | 1570.219 | n/a | n/a |
| docker (PID 125033) rss_mb | MB | 1 | 2.941 | 2.941 | 2.941 | 2.941 | n/a | n/a |
| docker (PID 125033) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 125043) rss_mb | MB | 1 | 27.613 | 27.613 | 27.613 | 27.613 | n/a | n/a |
| docker (PID 125043) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 125061) rss_mb | MB | 1 | 26.645 | 26.645 | 26.645 | 26.645 | n/a | n/a |
| docker (PID 125061) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 125076) rss_mb | MB | 1 | 11.988 | 11.988 | 11.988 | 11.988 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 125076) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 125116) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 125116) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 125116) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 125116) rss_mb | MB | 2 | 26.129 | 26.129 | 26.129 | 26.129 | n/a | n/a |
| docker (PID 125116) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 125130) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 125130) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 125130) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 125130) rss_mb | MB | 2 | 25.168 | 24.520 | 25.816 | 25.816 | n/a | n/a |
| docker (PID 125130) vms_mb | MB | 2 | 1624.209 | 1588.207 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 125256) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 125256) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 125256) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 125256) rss_mb | MB | 38 | 27.059 | 27.059 | 27.059 | 27.059 | n/a | n/a |
| docker (PID 125256) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 125272) rss_mb | MB | 1 | 26.828 | 26.828 | 26.828 | 26.828 | n/a | n/a |
| docker (PID 125272) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 125299) rss_mb | MB | 1 | 27.211 | 27.211 | 27.211 | 27.211 | n/a | n/a |
| docker (PID 125299) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [alex_0000] (PID 125339) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [alex_0000] (PID 125339) rss_mb | MB | 3 | 0.590 | 0.590 | 0.590 | 0.590 | n/a | n/a |
| docker-init [alex_0000] (PID 125339) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 125353) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 125353) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [alex_0000] (PID 125353) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 125355) rss_mb | MB | 1 | 16.441 | 16.441 | 16.441 | 16.441 | n/a | n/a |
| docker (PID 125355) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 125391) rss_mb | MB | 1 | 27.410 | 27.410 | 27.410 | 27.410 | n/a | n/a |
| docker (PID 125391) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 125426) rss_mb | MB | 1 | 27.383 | 27.383 | 27.383 | 27.383 | n/a | n/a |
| docker (PID 125426) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 125445) rss_mb | MB | 1 | 11.121 | 11.121 | 11.121 | 11.121 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 125445) vms_mb | MB | 1 | 1641.965 | 1641.965 | 1641.965 | 1641.965 | n/a | n/a |
| docker (PID 125464) rss_mb | MB | 1 | 26.012 | 26.012 | 26.012 | 26.012 | n/a | n/a |
| docker (PID 125464) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 125522) rss_mb | MB | 1 | 27.184 | 27.184 | 27.184 | 27.184 | n/a | n/a |
| docker (PID 125522) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [alex_0000] (PID 125561) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [alex_0000] (PID 125561) rss_mb | MB | 12 | 0.594 | 0.594 | 0.594 | 0.594 | n/a | n/a |
| docker-init [alex_0000] (PID 125561) vms_mb | MB | 12 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 125573) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 125573) rss_mb | MB | 12 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [alex_0000] (PID 125573) vms_mb | MB | 12 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 125576) rss_mb | MB | 1 | 22.004 | 22.004 | 22.004 | 22.004 | n/a | n/a |
| docker (PID 125576) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 125611) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 125611) io read MB/s | MB/s | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 125611) io write MB/s | MB/s | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 125611) rss_mb | MB | 11 | 27.156 | 27.156 | 27.156 | 27.156 | n/a | n/a |
| docker (PID 125611) vms_mb | MB | 11 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| bash [alex_0000] (PID 125629) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [alex_0000] (PID 125629) rss_mb | MB | 10 | 3.422 | 3.422 | 3.422 | 3.422 | n/a | n/a |
| bash [alex_0000] (PID 125629) vms_mb | MB | 10 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [alex_0000] (PID 125638) CPU | percent | 9 | 100.937 | 87.692 | 107.871 | 97.788 | 0.930000 CPU seconds | n/a |
| python [alex_0000] (PID 125638) rss_mb | MB | 10 | 32.030 | 13.270 | 41.648 | 41.648 | n/a | n/a |
| python [alex_0000] (PID 125638) vms_mb | MB | 10 | 39.243 | 17.613 | 51.238 | 51.238 | n/a | n/a |
| docker (PID 125648) rss_mb | MB | 1 | 26.227 | 26.227 | 26.227 | 26.227 | n/a | n/a |
| docker (PID 125648) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 125690) rss_mb | MB | 1 | 25.371 | 25.371 | 25.371 | 25.371 | n/a | n/a |
| docker (PID 125690) vms_mb | MB | 1 | 1596.211 | 1596.211 | 1596.211 | 1596.211 | n/a | n/a |
| docker (PID 125699) rss_mb | MB | 1 | 15.773 | 15.773 | 15.773 | 15.773 | n/a | n/a |
| docker (PID 125699) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 125707) CPU | percent | 1 | 97.958 | 97.958 | 97.958 | 97.958 | 0.100000 CPU seconds | n/a |
| docker (PID 125707) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 125707) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 125707) rss_mb | MB | 2 | 16.020 | 8.680 | 23.359 | 23.359 | n/a | n/a |
| docker (PID 125707) vms_mb | MB | 2 | 1407.693 | 1227.434 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 125715) CPU | percent | 1 | 64.757 | 64.757 | 64.757 | 64.757 | 0.080000 CPU seconds | n/a |
| docker (PID 125715) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 125715) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 125715) rss_mb | MB | 2 | 17.637 | 8.266 | 27.008 | 27.008 | n/a | n/a |
| docker (PID 125715) vms_mb | MB | 2 | 846.820 | 32.867 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 125717) CPU | percent | 1 | 80.947 | 80.947 | 80.947 | 80.947 | 0.100000 CPU seconds | n/a |
| docker (PID 125717) rss_mb | MB | 2 | 0.818 | 0.000 | 1.637 | 0.000 | n/a | n/a |
| docker (PID 125717) vms_mb | MB | 2 | 16.381 | 0.000 | 32.762 | 0.000 | n/a | n/a |
| docker (PID 125736) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 125736) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 125736) io write MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 125736) rss_mb | MB | 4 | 26.828 | 26.828 | 26.828 | 26.828 | n/a | n/a |
| docker (PID 125736) vms_mb | MB | 4 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 125739) CPU | percent | 44 | 0.180 | 0.000 | 7.919 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 125739) io read MB/s | MB/s | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 125739) io write MB/s | MB/s | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 125739) rss_mb | MB | 45 | 26.508 | 25.312 | 26.535 | 26.535 | n/a | n/a |
| docker (PID 125739) vms_mb | MB | 45 | 1660.761 | 1660.211 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 125786) CPU | percent | 7 | 8.435 | 0.000 | 59.043 | 0.000 | 0.070000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 125786) rss_mb | MB | 8 | 3.513 | 0.633 | 13.086 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 125786) vms_mb | MB | 8 | 393.219 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 125799) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 125799) rss_mb | MB | 6 | 1.723 | 1.723 | 1.723 | 1.723 | n/a | n/a |
| tail [alex_0000] (PID 125799) vms_mb | MB | 6 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 125801) rss_mb | MB | 1 | 8.238 | 8.238 | 8.238 | 8.238 | n/a | n/a |
| docker (PID 125801) vms_mb | MB | 1 | 32.867 | 32.867 | 32.867 | 32.867 | n/a | n/a |
| docker (PID 125809) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 125809) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 125809) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 125809) rss_mb | MB | 2 | 26.178 | 25.340 | 27.016 | 27.016 | n/a | n/a |
| docker (PID 125809) vms_mb | MB | 2 | 1628.492 | 1596.211 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 125827) rss_mb | MB | 1 | 11.746 | 11.746 | 11.746 | 11.746 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 125827) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 125837) rss_mb | MB | 1 | 25.406 | 25.406 | 25.406 | 25.406 | n/a | n/a |
| docker (PID 125837) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 125856) rss_mb | MB | 1 | 10.344 | 10.344 | 10.344 | 10.344 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 125856) vms_mb | MB | 1 | 1569.945 | 1569.945 | 1569.945 | 1569.945 | n/a | n/a |
| docker (PID 125872) rss_mb | MB | 1 | 19.113 | 19.113 | 19.113 | 19.113 | n/a | n/a |
| docker (PID 125872) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 125899) rss_mb | MB | 1 | 23.531 | 23.531 | 23.531 | 23.531 | n/a | n/a |
| docker (PID 125899) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 125908) rss_mb | MB | 1 | 26.945 | 26.945 | 26.945 | 26.945 | n/a | n/a |
| docker (PID 125908) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 125950) rss_mb | MB | 1 | 17.852 | 17.852 | 17.852 | 17.852 | n/a | n/a |
| docker (PID 125950) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 125967) rss_mb | MB | 1 | 26.668 | 26.668 | 26.668 | 26.668 | n/a | n/a |
| docker (PID 125967) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 125986) rss_mb | MB | 1 | 4.152 | 4.152 | 4.152 | 4.152 | n/a | n/a |
| docker (PID 125986) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 126011) rss_mb | MB | 1 | 25.652 | 25.652 | 25.652 | 25.652 | n/a | n/a |
| docker (PID 126011) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 126019) CPU | percent | 42 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 126019) io read MB/s | MB/s | 42 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 126019) io write MB/s | MB/s | 42 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 126019) rss_mb | MB | 43 | 26.941 | 26.941 | 26.941 | 26.941 | n/a | n/a |
| docker (PID 126019) vms_mb | MB | 43 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 126035) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 126035) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 126035) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 126035) rss_mb | MB | 2 | 25.918 | 25.918 | 25.918 | 25.918 | n/a | n/a |
| docker (PID 126035) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 126076) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 126076) rss_mb | MB | 6 | 2.708 | 0.633 | 13.082 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 126076) vms_mb | MB | 6 | 274.626 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 126089) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 126089) rss_mb | MB | 5 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [andy_0000] (PID 126089) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 126100) rss_mb | MB | 1 | 1.500 | 1.500 | 1.500 | 1.500 | n/a | n/a |
| docker (PID 126100) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 126127) rss_mb | MB | 1 | 8.547 | 8.547 | 8.547 | 8.547 | n/a | n/a |
| docker (PID 126127) vms_mb | MB | 1 | 1227.309 | 1227.309 | 1227.309 | 1227.309 | n/a | n/a |
| docker (PID 126165) rss_mb | MB | 1 | 27.180 | 27.180 | 27.180 | 27.180 | n/a | n/a |
| docker (PID 126165) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 126185) rss_mb | MB | 1 | 12.078 | 12.078 | 12.078 | 12.078 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 126185) vms_mb | MB | 1 | 1714.984 | 1714.984 | 1714.984 | 1714.984 | n/a | n/a |
| docker (PID 126205) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 126205) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 126205) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 126205) rss_mb | MB | 2 | 25.867 | 25.867 | 25.867 | 25.867 | n/a | n/a |
| docker (PID 126205) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 126261) rss_mb | MB | 1 | 18.398 | 18.398 | 18.398 | 18.398 | n/a | n/a |
| docker (PID 126261) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 126273) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 126273) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 126273) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 126273) rss_mb | MB | 2 | 27.035 | 27.035 | 27.035 | 27.035 | n/a | n/a |
| docker (PID 126273) vms_mb | MB | 2 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [andy_0000] (PID 126314) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 126314) rss_mb | MB | 14 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 126314) vms_mb | MB | 14 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| docker (PID 126329) rss_mb | MB | 1 | 25.891 | 25.891 | 25.891 | 25.891 | n/a | n/a |
| docker (PID 126329) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| tail [andy_0000] (PID 126340) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 126340) rss_mb | MB | 14 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [andy_0000] (PID 126340) vms_mb | MB | 14 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 126359) rss_mb | MB | 1 | 27.352 | 27.352 | 27.352 | 27.352 | n/a | n/a |
| docker (PID 126359) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 126373) rss_mb | MB | 1 | 24.902 | 24.902 | 24.902 | 24.902 | n/a | n/a |
| docker (PID 126373) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 126384) rss_mb | MB | 1 | 11.520 | 11.520 | 11.520 | 11.520 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 126384) vms_mb | MB | 1 | 1570.098 | 1570.098 | 1570.098 | 1570.098 | n/a | n/a |
| docker (PID 126398) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 126398) io read MB/s | MB/s | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 126398) io write MB/s | MB/s | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 126398) rss_mb | MB | 11 | 27.176 | 27.176 | 27.176 | 27.176 | n/a | n/a |
| docker (PID 126398) vms_mb | MB | 11 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| python3 (PID 126403) CPU | percent | 5 | 97.640 | 94.259 | 105.571 | 96.063 | 0.510000 CPU seconds | n/a |
| python3 (PID 126403) io read MB/s | MB/s | 5 | 0.074 | 0.000 | 0.368 | 0.000 | 0.039062 MB | n/a |
| python3 (PID 126403) io write MB/s | MB/s | 5 | 0.458 | 0.000 | 2.289 | 2.289 | 0.238281 MB | n/a |
| python3 (PID 126403) rss_mb | MB | 6 | 26.258 | 11.609 | 34.523 | 34.523 | n/a | n/a |
| python3 (PID 126403) vms_mb | MB | 6 | 50.310 | 38.074 | 57.438 | 57.438 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 126420) CPU | percent | 10 | 1.885 | 0.000 | 18.852 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 126420) rss_mb | MB | 11 | 4.110 | 3.332 | 11.895 | 3.332 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 126420) vms_mb | MB | 11 | 146.808 | 4.391 | 1570.977 | 4.391 | n/a | n/a |
| python [andy_0000] (PID 126429) CPU | percent | 9 | 98.904 | 87.150 | 107.136 | 87.150 | 0.920000 CPU seconds | n/a |
| python [andy_0000] (PID 126429) rss_mb | MB | 10 | 31.401 | 13.617 | 42.633 | 42.633 | n/a | n/a |
| python [andy_0000] (PID 126429) vms_mb | MB | 10 | 38.066 | 17.824 | 52.238 | 52.238 | n/a | n/a |
| docker (PID 126439) rss_mb | MB | 1 | 2.789 | 2.789 | 2.789 | 2.789 | n/a | n/a |
| docker (PID 126439) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 126456) rss_mb | MB | 1 | 25.309 | 25.309 | 25.309 | 25.309 | n/a | n/a |
| docker (PID 126456) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 126475) CPU | percent | 1 | 9.811 | 9.811 | 9.811 | 9.811 | 0.010000 CPU seconds | n/a |
| docker (PID 126475) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 126475) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 126475) rss_mb | MB | 2 | 17.537 | 9.117 | 25.957 | 25.957 | n/a | n/a |
| docker (PID 126475) vms_mb | MB | 2 | 1443.822 | 1227.434 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 126530) rss_mb | MB | 1 | 0.559 | 0.559 | 0.559 | 0.559 | n/a | n/a |
| docker (PID 126530) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 126538) rss_mb | MB | 1 | 27.113 | 27.113 | 27.113 | 27.113 | n/a | n/a |
| docker (PID 126538) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 126578) CPU | percent | 3 | 6.452 | 0.000 | 19.355 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 126578) rss_mb | MB | 4 | 2.473 | 0.633 | 7.992 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 126578) vms_mb | MB | 4 | 393.090 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 126591) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 126591) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [andy_0000] (PID 126591) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 126630) rss_mb | MB | 1 | 26.980 | 26.980 | 26.980 | 26.980 | n/a | n/a |
| docker (PID 126630) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| 6 [andy_0000] (PID 126647) rss_mb | MB | 1 | 0.707 | 0.707 | 0.707 | 0.707 | n/a | n/a |
| 6 [andy_0000] (PID 126647) vms_mb | MB | 1 | 14.004 | 14.004 | 14.004 | 14.004 | n/a | n/a |
| docker (PID 126664) rss_mb | MB | 1 | 27.188 | 27.188 | 27.188 | 27.188 | n/a | n/a |
| docker (PID 126664) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 126685) rss_mb | MB | 1 | 11.832 | 11.832 | 11.832 | 11.832 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 126685) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 126703) rss_mb | MB | 1 | 25.816 | 25.816 | 25.816 | 25.816 | n/a | n/a |
| docker (PID 126703) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 126770) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 126770) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 126770) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 126770) rss_mb | MB | 2 | 26.959 | 26.676 | 27.242 | 27.242 | n/a | n/a |
| docker (PID 126770) vms_mb | MB | 2 | 1696.775 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [arch_0000] (PID 126812) CPU | percent | 3 | 3.284 | 0.000 | 9.852 | 0.000 | 0.010000 CPU seconds | n/a |
| docker-init [arch_0000] (PID 126812) rss_mb | MB | 4 | 3.622 | 0.633 | 12.590 | 0.633 | n/a | n/a |
| docker-init [arch_0000] (PID 126812) vms_mb | MB | 4 | 411.474 | 1.055 | 1642.730 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 126825) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 126825) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [arch_0000] (PID 126825) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 126827) rss_mb | MB | 1 | 27.469 | 27.469 | 27.469 | 27.469 | n/a | n/a |
| docker (PID 126827) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] (PID 126848) rss_mb | MB | 1 | 11.797 | 11.797 | 11.797 | 11.797 | n/a | n/a |
| runc:[2:INIT] (PID 126848) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 126925) rss_mb | MB | 1 | 24.242 | 24.242 | 24.242 | 24.242 | n/a | n/a |
| docker (PID 126925) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 126962) rss_mb | MB | 1 | 25.945 | 25.945 | 25.945 | 25.945 | n/a | n/a |
| docker (PID 126962) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 127002) rss_mb | MB | 1 | 21.254 | 21.254 | 21.254 | 21.254 | n/a | n/a |
| docker (PID 127002) vms_mb | MB | 1 | 1524.203 | 1524.203 | 1524.203 | 1524.203 | n/a | n/a |
| docker (PID 127019) rss_mb | MB | 1 | 26.434 | 26.434 | 26.434 | 26.434 | n/a | n/a |
| docker (PID 127019) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[0:PARENT] [arch_0000] (PID 127053) rss_mb | MB | 1 | 1.902 | 1.902 | 1.902 | 1.902 | n/a | n/a |
| runc:[0:PARENT] [arch_0000] (PID 127053) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[1:CHILD] [arch_0000] (PID 127056) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[1:CHILD] [arch_0000] (PID 127056) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker-init [arch_0000] (PID 127057) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [arch_0000] (PID 127057) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [arch_0000] (PID 127057) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 127072) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 127072) rss_mb | MB | 3 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [arch_0000] (PID 127072) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 127082) rss_mb | MB | 1 | 17.414 | 17.414 | 17.414 | 17.414 | n/a | n/a |
| docker (PID 127082) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 127109) rss_mb | MB | 1 | 26.926 | 26.926 | 26.926 | 26.926 | n/a | n/a |
| docker (PID 127109) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 127128) rss_mb | MB | 1 | 10.316 | 10.316 | 10.316 | 10.316 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 127128) vms_mb | MB | 1 | 1569.195 | 1569.195 | 1569.195 | 1569.195 | n/a | n/a |
| docker (PID 127145) rss_mb | MB | 1 | 27.332 | 27.332 | 27.332 | 27.332 | n/a | n/a |
| docker (PID 127145) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 127164) rss_mb | MB | 1 | 11.961 | 11.961 | 11.961 | 11.961 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 127164) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 127180) rss_mb | MB | 1 | 26.883 | 26.883 | 26.883 | 26.883 | n/a | n/a |
| docker (PID 127180) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 127254) rss_mb | MB | 1 | 25.281 | 25.281 | 25.281 | 25.281 | n/a | n/a |
| docker (PID 127254) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 127262) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 127262) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 127262) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 127262) rss_mb | MB | 39 | 26.914 | 26.914 | 26.914 | 26.914 | n/a | n/a |
| docker (PID 127262) vms_mb | MB | 39 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 127278) rss_mb | MB | 1 | 26.570 | 26.570 | 26.570 | 26.570 | n/a | n/a |
| docker (PID 127278) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 127302) rss_mb | MB | 1 | 9.152 | 9.152 | 9.152 | 9.152 | n/a | n/a |
| docker (PID 127302) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| python3 (PID 127309) CPU | percent | 3 | 102.218 | 98.775 | 108.864 | 108.864 | 0.310000 CPU seconds | n/a |
| python3 (PID 127309) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 127309) io write MB/s | MB/s | 3 | 0.850 | 0.000 | 2.551 | 2.551 | 0.257812 MB | n/a |
| python3 (PID 127309) rss_mb | MB | 4 | 28.146 | 17.691 | 34.762 | 34.762 | n/a | n/a |
| python3 (PID 127309) vms_mb | MB | 4 | 51.818 | 42.434 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 127327) rss_mb | MB | 1 | 26.852 | 26.852 | 26.852 | 26.852 | n/a | n/a |
| docker (PID 127327) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 127361) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 127361) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 127361) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 127361) rss_mb | MB | 2 | 27.828 | 27.828 | 27.828 | 27.828 | n/a | n/a |
| docker (PID 127361) vms_mb | MB | 2 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [bake_0000] (PID 127403) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bake_0000] (PID 127403) rss_mb | MB | 4 | 3.711 | 0.633 | 12.945 | 0.633 | n/a | n/a |
| docker-init [bake_0000] (PID 127403) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 127416) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 127416) rss_mb | MB | 3 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [bake_0000] (PID 127416) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 127445) rss_mb | MB | 1 | 23.707 | 23.707 | 23.707 | 23.707 | n/a | n/a |
| docker (PID 127445) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 127481) rss_mb | MB | 1 | 27.254 | 27.254 | 27.254 | 27.254 | n/a | n/a |
| docker (PID 127481) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[0:PARENT] [bake_0000] (PID 127498) rss_mb | MB | 1 | 1.992 | 1.992 | 1.992 | 1.992 | n/a | n/a |
| runc:[0:PARENT] [bake_0000] (PID 127498) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[1:CHILD] [bake_0000] (PID 127499) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[1:CHILD] [bake_0000] (PID 127499) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 127515) rss_mb | MB | 1 | 27.168 | 27.168 | 27.168 | 27.168 | n/a | n/a |
| docker (PID 127515) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 127535) rss_mb | MB | 1 | 11.551 | 11.551 | 11.551 | 11.551 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 127535) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 127551) rss_mb | MB | 1 | 25.828 | 25.828 | 25.828 | 25.828 | n/a | n/a |
| docker (PID 127551) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 127608) CPU | percent | 1 | 9.851 | 9.851 | 9.851 | 9.851 | 0.010000 CPU seconds | n/a |
| docker (PID 127608) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 127608) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 127608) rss_mb | MB | 2 | 13.746 | 0.410 | 27.082 | 27.082 | n/a | n/a |
| docker (PID 127608) vms_mb | MB | 2 | 845.562 | 30.602 | 1660.523 | 1660.523 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 127649) CPU | percent | 3 | 3.251 | 0.000 | 9.752 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 127649) rss_mb | MB | 4 | 3.524 | 0.633 | 12.199 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 127649) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 127662) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 127662) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bake_0000] (PID 127662) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 127672) rss_mb | MB | 1 | 27.320 | 27.320 | 27.320 | 27.320 | n/a | n/a |
| docker (PID 127672) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 127691) rss_mb | MB | 1 | 11.105 | 11.105 | 11.105 | 11.105 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 127691) vms_mb | MB | 1 | 1569.840 | 1569.840 | 1569.840 | 1569.840 | n/a | n/a |
| docker (PID 127725) rss_mb | MB | 1 | 18.184 | 18.184 | 18.184 | 18.184 | n/a | n/a |
| docker (PID 127725) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 127768) CPU | percent | 1 | 9.697 | 9.697 | 9.697 | 9.697 | 0.010000 CPU seconds | n/a |
| docker (PID 127768) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 127768) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 127768) rss_mb | MB | 2 | 13.174 | 0.453 | 25.895 | 25.895 | n/a | n/a |
| docker (PID 127768) vms_mb | MB | 2 | 846.480 | 32.750 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 127821) rss_mb | MB | 1 | 25.039 | 25.039 | 25.039 | 25.039 | n/a | n/a |
| docker (PID 127821) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 127851) CPU | percent | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 127851) io read MB/s | MB/s | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 127851) io write MB/s | MB/s | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 127851) rss_mb | MB | 41 | 26.641 | 26.641 | 26.641 | 26.641 | n/a | n/a |
| docker (PID 127851) vms_mb | MB | 41 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 127859) rss_mb | MB | 1 | 26.664 | 26.664 | 26.664 | 26.664 | n/a | n/a |
| docker (PID 127859) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 127868) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 127868) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 127868) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 127868) rss_mb | MB | 2 | 25.754 | 25.754 | 25.754 | 25.754 | n/a | n/a |
| docker (PID 127868) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| 6 [bake_0000] (PID 127902) rss_mb | MB | 1 | 1.762 | 1.762 | 1.762 | 1.762 | n/a | n/a |
| 6 [bake_0000] (PID 127902) vms_mb | MB | 1 | 13.980 | 13.980 | 13.980 | 13.980 | n/a | n/a |
| docker-init [bake_0000] (PID 127909) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bake_0000] (PID 127909) rss_mb | MB | 5 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bake_0000] (PID 127909) vms_mb | MB | 5 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 127921) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 127921) rss_mb | MB | 5 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [bake_0000] (PID 127921) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 127932) rss_mb | MB | 1 | 27.305 | 27.305 | 27.305 | 27.305 | n/a | n/a |
| docker (PID 127932) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 127951) rss_mb | MB | 1 | 11.473 | 11.473 | 11.473 | 11.473 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 127951) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 127958) rss_mb | MB | 1 | 27.199 | 27.199 | 27.199 | 27.199 | n/a | n/a |
| docker (PID 127958) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 127977) rss_mb | MB | 1 | 10.840 | 10.840 | 10.840 | 10.840 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 127977) vms_mb | MB | 1 | 1497.578 | 1497.578 | 1497.578 | 1497.578 | n/a | n/a |
| docker (PID 127991) rss_mb | MB | 1 | 22.461 | 22.461 | 22.461 | 22.461 | n/a | n/a |
| docker (PID 127991) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 128027) rss_mb | MB | 1 | 25.883 | 25.883 | 25.883 | 25.883 | n/a | n/a |
| docker (PID 128027) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 128093) rss_mb | MB | 1 | 26.332 | 26.332 | 26.332 | 26.332 | n/a | n/a |
| docker (PID 128093) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 128112) rss_mb | MB | 1 | 26.781 | 26.781 | 26.781 | 26.781 | n/a | n/a |
| docker (PID 128112) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker-init [arch_0000] (PID 128153) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [arch_0000] (PID 128153) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [arch_0000] (PID 128153) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 128164) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 128164) rss_mb | MB | 3 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [arch_0000] (PID 128164) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 128166) rss_mb | MB | 1 | 19.840 | 19.840 | 19.840 | 19.840 | n/a | n/a |
| docker (PID 128166) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 128200) rss_mb | MB | 1 | 25.969 | 25.969 | 25.969 | 25.969 | n/a | n/a |
| docker (PID 128200) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 128235) rss_mb | MB | 1 | 27.352 | 27.352 | 27.352 | 27.352 | n/a | n/a |
| docker (PID 128235) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 128275) rss_mb | MB | 1 | 26.871 | 26.871 | 26.871 | 26.871 | n/a | n/a |
| docker (PID 128275) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 128317) rss_mb | MB | 1 | 4.965 | 4.965 | 4.965 | 4.965 | n/a | n/a |
| docker (PID 128317) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 128334) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 128334) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 128334) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 128334) rss_mb | MB | 2 | 24.133 | 21.504 | 26.762 | 26.762 | n/a | n/a |
| docker (PID 128334) vms_mb | MB | 2 | 1624.488 | 1588.203 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 128377) CPU | percent | 10 | 0.980 | 0.000 | 9.803 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 128377) rss_mb | MB | 11 | 1.727 | 0.633 | 12.668 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 128377) vms_mb | MB | 11 | 143.707 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 128389) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 128389) rss_mb | MB | 10 | 1.676 | 1.676 | 1.676 | 1.676 | n/a | n/a |
| tail [arch_0000] (PID 128389) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 128399) rss_mb | MB | 1 | 27.258 | 27.258 | 27.258 | 27.258 | n/a | n/a |
| docker (PID 128399) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 128418) rss_mb | MB | 1 | 10.793 | 10.793 | 10.793 | 10.793 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 128418) vms_mb | MB | 1 | 1641.586 | 1641.586 | 1641.586 | 1641.586 | n/a | n/a |
| docker (PID 128426) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 128426) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 128426) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 128426) rss_mb | MB | 8 | 27.258 | 27.258 | 27.258 | 27.258 | n/a | n/a |
| docker (PID 128426) vms_mb | MB | 8 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| bash [arch_0000] (PID 128445) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [arch_0000] (PID 128445) rss_mb | MB | 8 | 3.324 | 3.324 | 3.324 | 3.324 | n/a | n/a |
| bash [arch_0000] (PID 128445) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [arch_0000] (PID 128455) CPU | percent | 7 | 99.134 | 88.228 | 107.818 | 97.283 | 0.710000 CPU seconds | n/a |
| python [arch_0000] (PID 128455) rss_mb | MB | 8 | 30.207 | 7.270 | 42.754 | 42.754 | n/a | n/a |
| python [arch_0000] (PID 128455) vms_mb | MB | 8 | 37.428 | 11.938 | 52.219 | 52.219 | n/a | n/a |
| docker (PID 128468) rss_mb | MB | 1 | 26.266 | 26.266 | 26.266 | 26.266 | n/a | n/a |
| docker (PID 128468) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 128548) CPU | percent | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 128548) io read MB/s | MB/s | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 128548) io write MB/s | MB/s | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 128548) rss_mb | MB | 41 | 25.762 | 25.762 | 25.762 | 25.762 | n/a | n/a |
| docker (PID 128548) vms_mb | MB | 41 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 128557) rss_mb | MB | 1 | 17.191 | 17.191 | 17.191 | 17.191 | n/a | n/a |
| docker (PID 128557) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 128566) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 128566) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 128566) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 128566) rss_mb | MB | 2 | 25.766 | 25.766 | 25.766 | 25.766 | n/a | n/a |
| docker (PID 128566) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 128605) CPU | percent | 4 | 2.438 | 0.000 | 9.753 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 128605) rss_mb | MB | 5 | 3.122 | 0.633 | 13.078 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 128605) vms_mb | MB | 5 | 314.989 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 128618) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 128618) rss_mb | MB | 4 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [arch_0000] (PID 128618) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 128629) rss_mb | MB | 1 | 27.543 | 27.543 | 27.543 | 27.543 | n/a | n/a |
| docker (PID 128629) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 128654) rss_mb | MB | 1 | 26.180 | 26.180 | 26.180 | 26.180 | n/a | n/a |
| docker (PID 128654) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 128689) rss_mb | MB | 1 | 3.430 | 3.430 | 3.430 | 3.430 | n/a | n/a |
| docker (PID 128689) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 128716) rss_mb | MB | 1 | 3.684 | 3.684 | 3.684 | 3.684 | n/a | n/a |
| docker (PID 128716) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 128726) rss_mb | MB | 1 | 25.859 | 25.859 | 25.859 | 25.859 | n/a | n/a |
| docker (PID 128726) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 128768) rss_mb | MB | 1 | 25.281 | 25.281 | 25.281 | 25.281 | n/a | n/a |
| docker (PID 128768) vms_mb | MB | 1 | 1595.961 | 1595.961 | 1595.961 | 1595.961 | n/a | n/a |
| docker (PID 128785) rss_mb | MB | 1 | 11.125 | 11.125 | 11.125 | 11.125 | n/a | n/a |
| docker (PID 128785) vms_mb | MB | 1 | 1387.949 | 1387.949 | 1387.949 | 1387.949 | n/a | n/a |
| docker (PID 128828) rss_mb | MB | 1 | 10.344 | 10.344 | 10.344 | 10.344 | n/a | n/a |
| docker (PID 128828) vms_mb | MB | 1 | 1387.949 | 1387.949 | 1387.949 | 1387.949 | n/a | n/a |
| docker (PID 128837) CPU | percent | 48 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 128837) io read MB/s | MB/s | 48 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 128837) io write MB/s | MB/s | 48 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 128837) rss_mb | MB | 49 | 25.652 | 25.652 | 25.652 | 25.652 | n/a | n/a |
| docker (PID 128837) vms_mb | MB | 49 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 128845) rss_mb | MB | 1 | 23.824 | 23.824 | 23.824 | 23.824 | n/a | n/a |
| docker (PID 128845) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 128853) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 128853) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 128853) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 128853) rss_mb | MB | 2 | 27.211 | 27.211 | 27.211 | 27.211 | n/a | n/a |
| docker (PID 128853) vms_mb | MB | 2 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 128895) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 128895) rss_mb | MB | 5 | 3.091 | 0.633 | 12.922 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 128895) vms_mb | MB | 5 | 300.538 | 1.055 | 1498.473 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 128906) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 128906) rss_mb | MB | 4 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [bake_0000] (PID 128906) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 128916) rss_mb | MB | 1 | 15.941 | 15.941 | 15.941 | 15.941 | n/a | n/a |
| docker (PID 128916) vms_mb | MB | 1 | 1387.949 | 1387.949 | 1387.949 | 1387.949 | n/a | n/a |
| docker (PID 128942) rss_mb | MB | 1 | 27.336 | 27.336 | 27.336 | 27.336 | n/a | n/a |
| docker (PID 128942) vms_mb | MB | 1 | 1733.027 | 1733.027 | 1733.027 | 1733.027 | n/a | n/a |
| docker (PID 128980) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 128980) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 129018) rss_mb | MB | 1 | 25.816 | 25.816 | 25.816 | 25.816 | n/a | n/a |
| docker (PID 129018) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 129059) rss_mb | MB | 1 | 4.582 | 4.582 | 4.582 | 4.582 | n/a | n/a |
| docker (PID 129059) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 129076) CPU | percent | 2 | 4.778 | 0.000 | 9.556 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 129076) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 129076) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 129076) rss_mb | MB | 3 | 18.016 | 2.766 | 25.641 | 25.641 | n/a | n/a |
| docker (PID 129076) vms_mb | MB | 3 | 1117.728 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| 6 [bake_0000] (PID 129113) rss_mb | MB | 1 | 1.770 | 1.770 | 1.770 | 1.770 | n/a | n/a |
| 6 [bake_0000] (PID 129113) vms_mb | MB | 1 | 13.980 | 13.980 | 13.980 | 13.980 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 129116) CPU | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 129116) rss_mb | MB | 16 | 1.397 | 0.633 | 12.855 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 129116) vms_mb | MB | 16 | 99.128 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 129128) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 129128) rss_mb | MB | 15 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [bake_0000] (PID 129128) vms_mb | MB | 15 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 129139) rss_mb | MB | 1 | 27.113 | 27.113 | 27.113 | 27.113 | n/a | n/a |
| docker (PID 129139) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 129156) rss_mb | MB | 1 | 8.938 | 8.938 | 8.938 | 8.938 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 129156) vms_mb | MB | 1 | 1569.445 | 1569.445 | 1569.445 | 1569.445 | n/a | n/a |
| docker (PID 129167) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 129167) io read MB/s | MB/s | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 129167) io write MB/s | MB/s | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 129167) rss_mb | MB | 14 | 27.248 | 27.230 | 27.355 | 27.355 | n/a | n/a |
| docker (PID 129167) vms_mb | MB | 14 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| bash [bake_0000] (PID 129186) CPU | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bake_0000] (PID 129186) rss_mb | MB | 13 | 3.258 | 3.258 | 3.258 | 3.258 | n/a | n/a |
| bash [bake_0000] (PID 129186) vms_mb | MB | 13 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bake_0000] (PID 129195) CPU | percent | 12 | 98.462 | 85.118 | 124.100 | 105.509 | 1.250000 CPU seconds | n/a |
| python [bake_0000] (PID 129195) rss_mb | MB | 13 | 32.337 | 10.766 | 41.391 | 41.391 | n/a | n/a |
| python [bake_0000] (PID 129195) vms_mb | MB | 13 | 39.607 | 14.770 | 50.375 | 50.375 | n/a | n/a |
| docker (PID 129209) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 129209) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 129209) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 129209) rss_mb | MB | 2 | 26.887 | 26.887 | 26.887 | 26.887 | n/a | n/a |
| docker (PID 129209) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 129278) rss_mb | MB | 1 | 25.699 | 25.699 | 25.699 | 25.699 | n/a | n/a |
| docker (PID 129278) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| python3 (PID 129293) CPU | percent | 3 | 102.116 | 98.688 | 108.840 | 108.840 | 0.310000 CPU seconds | n/a |
| python3 (PID 129293) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 129293) io write MB/s | MB/s | 3 | 0.850 | 0.000 | 2.551 | 2.551 | 0.257812 MB | n/a |
| python3 (PID 129293) rss_mb | MB | 4 | 25.889 | 13.031 | 34.348 | 34.348 | n/a | n/a |
| python3 (PID 129293) vms_mb | MB | 4 | 50.038 | 38.430 | 57.457 | 57.457 | n/a | n/a |
| docker (PID 129304) rss_mb | MB | 1 | 19.230 | 19.230 | 19.230 | 19.230 | n/a | n/a |
| docker (PID 129304) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 129332) CPU | percent | 1 | 97.813 | 97.813 | 97.813 | 97.813 | 0.100000 CPU seconds | n/a |
| docker (PID 129332) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 129332) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 129332) rss_mb | MB | 2 | 12.143 | 0.859 | 23.426 | 23.426 | n/a | n/a |
| docker (PID 129332) vms_mb | MB | 2 | 810.357 | 32.762 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 129342) rss_mb | MB | 1 | 26.934 | 26.934 | 26.934 | 26.934 | n/a | n/a |
| docker (PID 129342) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 129381) CPU | percent | 3 | 6.520 | 0.000 | 19.561 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 129381) rss_mb | MB | 4 | 3.243 | 0.633 | 11.074 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 129381) vms_mb | MB | 4 | 393.152 | 1.055 | 1569.445 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 129395) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 129395) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [bake_0000] (PID 129395) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 129405) rss_mb | MB | 1 | 18.234 | 18.234 | 18.234 | 18.234 | n/a | n/a |
| docker (PID 129405) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 129433) rss_mb | MB | 1 | 27.375 | 27.375 | 27.375 | 27.375 | n/a | n/a |
| docker (PID 129433) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 129453) rss_mb | MB | 1 | 12.012 | 12.012 | 12.012 | 12.012 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 129453) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 129468) rss_mb | MB | 1 | 27.320 | 27.320 | 27.320 | 27.320 | n/a | n/a |
| docker (PID 129468) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 129504) rss_mb | MB | 1 | 26.773 | 26.773 | 26.773 | 26.773 | n/a | n/a |
| docker (PID 129504) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 129552) rss_mb | MB | 1 | 25.633 | 25.633 | 25.633 | 25.633 | n/a | n/a |
| docker (PID 129552) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 129566) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 129566) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 129566) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 129566) rss_mb | MB | 2 | 27.555 | 27.555 | 27.555 | 27.555 | n/a | n/a |
| docker (PID 129566) vms_mb | MB | 2 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [bale_0000] (PID 129606) CPU | percent | 3 | 3.273 | 0.000 | 9.818 | 0.000 | 0.010000 CPU seconds | n/a |
| docker-init [bale_0000] (PID 129606) rss_mb | MB | 4 | 3.631 | 0.633 | 12.625 | 0.633 | n/a | n/a |
| docker-init [bale_0000] (PID 129606) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 129618) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 129618) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bale_0000] (PID 129618) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 129647) rss_mb | MB | 1 | 15.824 | 15.824 | 15.824 | 15.824 | n/a | n/a |
| docker (PID 129647) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 129682) rss_mb | MB | 1 | 27.180 | 27.180 | 27.180 | 27.180 | n/a | n/a |
| docker (PID 129682) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 129717) rss_mb | MB | 1 | 27.184 | 27.184 | 27.184 | 27.184 | n/a | n/a |
| docker (PID 129717) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 129736) rss_mb | MB | 1 | 12.082 | 12.082 | 12.082 | 12.082 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 129736) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 129752) rss_mb | MB | 1 | 26.930 | 26.930 | 26.930 | 26.930 | n/a | n/a |
| docker (PID 129752) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 129802) rss_mb | MB | 1 | 25.988 | 25.988 | 25.988 | 25.988 | n/a | n/a |
| docker (PID 129802) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 129810) rss_mb | MB | 1 | 27.043 | 27.043 | 27.043 | 27.043 | n/a | n/a |
| docker (PID 129810) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 129850) CPU | percent | 3 | 6.538 | 0.000 | 19.613 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 129850) rss_mb | MB | 4 | 3.466 | 0.633 | 11.965 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 129850) vms_mb | MB | 4 | 375.347 | 1.055 | 1498.223 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 129868) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 129868) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bale_0000] (PID 129868) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 129889) rss_mb | MB | 1 | 22.340 | 22.340 | 22.340 | 22.340 | n/a | n/a |
| docker (PID 129889) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 129920) rss_mb | MB | 1 | 27.477 | 27.477 | 27.477 | 27.477 | n/a | n/a |
| docker (PID 129920) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 129940) rss_mb | MB | 1 | 11.277 | 11.277 | 11.277 | 11.277 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 129940) vms_mb | MB | 1 | 1570.340 | 1570.340 | 1570.340 | 1570.340 | n/a | n/a |
| docker (PID 129955) rss_mb | MB | 1 | 27.457 | 27.457 | 27.457 | 27.457 | n/a | n/a |
| docker (PID 129955) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 129978) rss_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 129978) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 129995) rss_mb | MB | 1 | 25.832 | 25.832 | 25.832 | 25.832 | n/a | n/a |
| docker (PID 129995) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 130062) rss_mb | MB | 1 | 27.137 | 27.137 | 27.137 | 27.137 | n/a | n/a |
| docker (PID 130062) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 130070) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 130070) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 130070) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 130070) rss_mb | MB | 39 | 26.441 | 26.441 | 26.441 | 26.441 | n/a | n/a |
| docker (PID 130070) vms_mb | MB | 39 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 130095) rss_mb | MB | 1 | 0.129 | 0.129 | 0.129 | 0.129 | n/a | n/a |
| docker (PID 130095) vms_mb | MB | 1 | 30.570 | 30.570 | 30.570 | 30.570 | n/a | n/a |
| python3 (PID 130119) CPU | percent | 2 | 103.771 | 98.669 | 108.873 | 108.873 | 0.210000 CPU seconds | n/a |
| python3 (PID 130119) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 130119) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 130119) rss_mb | MB | 3 | 26.816 | 19.387 | 33.625 | 33.625 | n/a | n/a |
| python3 (PID 130119) vms_mb | MB | 3 | 50.487 | 44.059 | 56.461 | 56.461 | n/a | n/a |
| docker (PID 130137) rss_mb | MB | 1 | 24.281 | 24.281 | 24.281 | 24.281 | n/a | n/a |
| docker (PID 130137) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 130171) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 130171) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 130171) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 130171) rss_mb | MB | 2 | 27.318 | 26.953 | 27.684 | 27.684 | n/a | n/a |
| docker (PID 130171) vms_mb | MB | 2 | 1696.775 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| 6 (PID 130207) rss_mb | MB | 1 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| 6 (PID 130207) vms_mb | MB | 1 | 13.980 | 13.980 | 13.980 | 13.980 | n/a | n/a |
| docker-init [band_0000] (PID 130209) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [band_0000] (PID 130209) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [band_0000] (PID 130209) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 130222) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 130222) rss_mb | MB | 4 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [band_0000] (PID 130222) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 130224) rss_mb | MB | 1 | 27.238 | 27.238 | 27.238 | 27.238 | n/a | n/a |
| docker (PID 130224) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 130259) rss_mb | MB | 1 | 27.141 | 27.141 | 27.141 | 27.141 | n/a | n/a |
| docker (PID 130259) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 130280) rss_mb | MB | 1 | 10.312 | 10.312 | 10.312 | 10.312 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 130280) vms_mb | MB | 1 | 1569.195 | 1569.195 | 1569.195 | 1569.195 | n/a | n/a |
| docker (PID 130315) rss_mb | MB | 1 | 13.363 | 13.363 | 13.363 | 13.363 | n/a | n/a |
| docker (PID 130315) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 130359) rss_mb | MB | 1 | 25.996 | 25.996 | 25.996 | 25.996 | n/a | n/a |
| docker (PID 130359) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 130418) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 130418) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 130418) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 130418) rss_mb | MB | 2 | 26.879 | 26.879 | 26.879 | 26.879 | n/a | n/a |
| docker (PID 130418) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 130458) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 130458) rss_mb | MB | 4 | 3.672 | 0.633 | 12.789 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 130458) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 130471) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 130471) rss_mb | MB | 3 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [band_0000] (PID 130471) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 130482) rss_mb | MB | 1 | 27.262 | 27.262 | 27.262 | 27.262 | n/a | n/a |
| docker (PID 130482) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 130503) rss_mb | MB | 1 | 11.547 | 11.547 | 11.547 | 11.547 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 130503) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 130581) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 130581) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 130581) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 130581) rss_mb | MB | 2 | 23.611 | 21.344 | 25.879 | 25.879 | n/a | n/a |
| docker (PID 130581) vms_mb | MB | 2 | 1588.080 | 1515.949 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 130648) rss_mb | MB | 1 | 25.859 | 25.859 | 25.859 | 25.859 | n/a | n/a |
| docker (PID 130648) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 130662) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 130662) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 130662) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 130662) rss_mb | MB | 38 | 27.098 | 27.098 | 27.098 | 27.098 | n/a | n/a |
| docker (PID 130662) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 130679) rss_mb | MB | 1 | 27.000 | 27.000 | 27.000 | 27.000 | n/a | n/a |
| docker (PID 130679) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 130705) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 130705) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 130705) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 130705) rss_mb | MB | 2 | 27.031 | 27.031 | 27.031 | 27.031 | n/a | n/a |
| docker (PID 130705) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 130744) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 130744) rss_mb | MB | 4 | 3.725 | 0.633 | 13.000 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 130744) vms_mb | MB | 4 | 411.474 | 1.055 | 1642.730 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 130757) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 130757) rss_mb | MB | 3 | 1.539 | 1.539 | 1.539 | 1.539 | n/a | n/a |
| tail [bale_0000] (PID 130757) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 130767) rss_mb | MB | 1 | 27.371 | 27.371 | 27.371 | 27.371 | n/a | n/a |
| docker (PID 130767) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 130787) rss_mb | MB | 1 | 11.492 | 11.492 | 11.492 | 11.492 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 130787) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 130825) rss_mb | MB | 1 | 25.883 | 25.883 | 25.883 | 25.883 | n/a | n/a |
| docker (PID 130825) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 130871) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 130871) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 130871) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 130871) rss_mb | MB | 2 | 17.367 | 8.668 | 26.066 | 26.066 | n/a | n/a |
| docker (PID 130871) vms_mb | MB | 2 | 1443.822 | 1227.434 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 130930) rss_mb | MB | 1 | 25.859 | 25.859 | 25.859 | 25.859 | n/a | n/a |
| docker (PID 130930) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [band_0000] (PID 130971) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [band_0000] (PID 130971) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [band_0000] (PID 130971) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 130984) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 130984) rss_mb | MB | 3 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [band_0000] (PID 130984) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 130986) rss_mb | MB | 1 | 18.125 | 18.125 | 18.125 | 18.125 | n/a | n/a |
| docker (PID 130986) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 131021) rss_mb | MB | 1 | 27.250 | 27.250 | 27.250 | 27.250 | n/a | n/a |
| docker (PID 131021) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 131058) rss_mb | MB | 1 | 27.328 | 27.328 | 27.328 | 27.328 | n/a | n/a |
| docker (PID 131058) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 131077) rss_mb | MB | 1 | 10.902 | 10.902 | 10.902 | 10.902 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 131077) vms_mb | MB | 1 | 1569.703 | 1569.703 | 1569.703 | 1569.703 | n/a | n/a |
| docker (PID 131094) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 131094) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 131094) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 131094) rss_mb | MB | 2 | 26.773 | 26.773 | 26.773 | 26.773 | n/a | n/a |
| docker (PID 131094) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 131155) rss_mb | MB | 1 | 26.984 | 26.984 | 26.984 | 26.984 | n/a | n/a |
| docker (PID 131155) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker-init [bale_0000] (PID 131195) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bale_0000] (PID 131195) rss_mb | MB | 37 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bale_0000] (PID 131195) vms_mb | MB | 37 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 131208) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 131208) rss_mb | MB | 37 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [bale_0000] (PID 131208) vms_mb | MB | 37 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 131210) rss_mb | MB | 1 | 26.379 | 26.379 | 26.379 | 26.379 | n/a | n/a |
| docker (PID 131210) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 131246) CPU | percent | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 131246) io read MB/s | MB/s | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 131246) io write MB/s | MB/s | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 131246) rss_mb | MB | 36 | 27.219 | 27.219 | 27.219 | 27.219 | n/a | n/a |
| docker (PID 131246) vms_mb | MB | 36 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 131266) CPU | percent | 35 | 0.557 | 0.000 | 19.489 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 131266) rss_mb | MB | 36 | 3.294 | 1.004 | 3.359 | 3.359 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 131266) vms_mb | MB | 36 | 4.661 | 4.391 | 14.109 | 4.391 | n/a | n/a |
| python [bale_0000] (PID 131275) CPU | percent | 34 | 100.065 | 97.558 | 107.959 | 107.939 | 3.470000 CPU seconds | n/a |
| python [bale_0000] (PID 131275) rss_mb | MB | 35 | 39.044 | 15.508 | 41.629 | 40.859 | n/a | n/a |
| python [bale_0000] (PID 131275) vms_mb | MB | 35 | 47.990 | 19.637 | 51.410 | 50.324 | n/a | n/a |
| docker (PID 131285) rss_mb | MB | 1 | 25.797 | 25.797 | 25.797 | 25.797 | n/a | n/a |
| docker (PID 131285) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 131345) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 131345) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 131345) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 131345) rss_mb | MB | 2 | 26.984 | 26.984 | 26.984 | 26.984 | n/a | n/a |
| docker (PID 131345) vms_mb | MB | 2 | 1588.520 | 1588.520 | 1588.520 | 1588.520 | n/a | n/a |
| docker-init [bale_0000] (PID 131387) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bale_0000] (PID 131387) rss_mb | MB | 3 | 0.422 | 0.000 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bale_0000] (PID 131387) vms_mb | MB | 3 | 1.010 | 0.922 | 1.055 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 131400) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 131400) rss_mb | MB | 2 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bale_0000] (PID 131400) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 131439) rss_mb | MB | 1 | 4.988 | 4.988 | 4.988 | 4.988 | n/a | n/a |
| docker (PID 131439) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 131474) rss_mb | MB | 1 | 27.383 | 27.383 | 27.383 | 27.383 | n/a | n/a |
| docker (PID 131474) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 131510) rss_mb | MB | 1 | 25.707 | 25.707 | 25.707 | 25.707 | n/a | n/a |
| docker (PID 131510) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 131551) rss_mb | MB | 1 | 15.414 | 15.414 | 15.414 | 15.414 | n/a | n/a |
| docker (PID 131551) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 131585) rss_mb | MB | 1 | 17.492 | 17.492 | 17.492 | 17.492 | n/a | n/a |
| docker (PID 131585) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 131594) CPU | percent | 48 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 131594) io read MB/s | MB/s | 48 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 131594) io write MB/s | MB/s | 48 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 131594) rss_mb | MB | 49 | 26.707 | 26.707 | 26.707 | 26.707 | n/a | n/a |
| docker (PID 131594) vms_mb | MB | 49 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 131618) rss_mb | MB | 1 | 25.469 | 25.469 | 25.469 | 25.469 | n/a | n/a |
| docker (PID 131618) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 131632) CPU | percent | 54 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 131632) io read MB/s | MB/s | 54 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 131632) io write MB/s | MB/s | 54 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 131632) rss_mb | MB | 55 | 26.738 | 26.738 | 26.738 | 26.738 | n/a | n/a |
| docker (PID 131632) vms_mb | MB | 55 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 131657) rss_mb | MB | 1 | 13.938 | 13.938 | 13.938 | 13.938 | n/a | n/a |
| docker (PID 131657) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 131665) rss_mb | MB | 1 | 26.578 | 26.578 | 26.578 | 26.578 | n/a | n/a |
| docker (PID 131665) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 131680) CPU | percent | 33 | 98.695 | 87.961 | 108.767 | 98.980 | 3.310000 CPU seconds | n/a |
| python3 (PID 131680) io read MB/s | MB/s | 33 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| python3 (PID 131680) io write MB/s | MB/s | 33 | 0.077 | 0.000 | 2.552 | 2.552 | 0.257812 MB | n/a |
| python3 (PID 131680) rss_mb | MB | 34 | 32.318 | 8.793 | 34.473 | 34.473 | n/a | n/a |
| python3 (PID 131680) vms_mb | MB | 34 | 55.937 | 35.199 | 57.461 | 57.438 | n/a | n/a |
| docker (PID 131698) rss_mb | MB | 1 | 23.672 | 23.672 | 23.672 | 23.672 | n/a | n/a |
| docker (PID 131698) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 131725) rss_mb | MB | 1 | 2.793 | 2.793 | 2.793 | 2.793 | n/a | n/a |
| docker (PID 131725) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 131753) CPU | percent | 2 | 18.416 | 0.000 | 36.833 | 0.000 | 0.040000 CPU seconds | n/a |
| docker (PID 131753) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 131753) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 131753) rss_mb | MB | 3 | 18.539 | 1.703 | 26.957 | 26.957 | n/a | n/a |
| docker (PID 131753) vms_mb | MB | 3 | 1118.103 | 32.762 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 131791) CPU | percent | 6 | 3.225 | 0.000 | 19.350 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 131791) rss_mb | MB | 7 | 2.292 | 0.633 | 12.246 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 131791) vms_mb | MB | 7 | 225.222 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 131803) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 131803) rss_mb | MB | 6 | 1.711 | 1.711 | 1.711 | 1.711 | n/a | n/a |
| tail [band_0000] (PID 131803) vms_mb | MB | 6 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 131805) rss_mb | MB | 1 | 8.426 | 8.426 | 8.426 | 8.426 | n/a | n/a |
| docker (PID 131805) vms_mb | MB | 1 | 42.242 | 42.242 | 42.242 | 42.242 | n/a | n/a |
| docker (PID 131813) rss_mb | MB | 1 | 26.836 | 26.836 | 26.836 | 26.836 | n/a | n/a |
| docker (PID 131813) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 131839) rss_mb | MB | 1 | 27.367 | 27.367 | 27.367 | 27.367 | n/a | n/a |
| docker (PID 131839) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| sh [band_0000] (PID 131859) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sh [band_0000] (PID 131859) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 131876) rss_mb | MB | 1 | 27.211 | 27.211 | 27.211 | 27.211 | n/a | n/a |
| docker (PID 131876) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 131908) rss_mb | MB | 1 | 22.664 | 22.664 | 22.664 | 22.664 | n/a | n/a |
| docker (PID 131908) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 131916) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 131916) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 131916) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 131916) rss_mb | MB | 2 | 25.789 | 25.789 | 25.789 | 25.789 | n/a | n/a |
| docker (PID 131916) vms_mb | MB | 2 | 1659.961 | 1659.961 | 1659.961 | 1659.961 | n/a | n/a |
| docker (PID 131966) rss_mb | MB | 1 | 18.234 | 18.234 | 18.234 | 18.234 | n/a | n/a |
| docker (PID 131966) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 131981) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 131981) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 131981) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 131981) rss_mb | MB | 2 | 26.881 | 26.664 | 27.098 | 27.098 | n/a | n/a |
| docker (PID 131981) vms_mb | MB | 2 | 1732.777 | 1660.773 | 1804.781 | 1804.781 | n/a | n/a |
| docker-init [bart_0000] (PID 132024) CPU | percent | 4 | 7.359 | 0.000 | 29.435 | 0.000 | 0.030000 CPU seconds | n/a |
| docker-init [bart_0000] (PID 132024) rss_mb | MB | 5 | 2.679 | 0.633 | 10.863 | 0.633 | n/a | n/a |
| docker-init [bart_0000] (PID 132024) vms_mb | MB | 5 | 314.733 | 1.055 | 1569.445 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 132036) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 132036) rss_mb | MB | 4 | 1.637 | 1.637 | 1.637 | 1.637 | n/a | n/a |
| tail [bart_0000] (PID 132036) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 132038) rss_mb | MB | 1 | 18.414 | 18.414 | 18.414 | 18.414 | n/a | n/a |
| docker (PID 132038) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 132073) rss_mb | MB | 1 | 25.789 | 25.789 | 25.789 | 25.789 | n/a | n/a |
| docker (PID 132073) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 132101) rss_mb | MB | 1 | 27.395 | 27.395 | 27.395 | 27.395 | n/a | n/a |
| docker (PID 132101) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 132122) rss_mb | MB | 1 | 11.488 | 11.488 | 11.488 | 11.488 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 132122) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 132137) rss_mb | MB | 1 | 27.203 | 27.203 | 27.203 | 27.203 | n/a | n/a |
| docker (PID 132137) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| sh [bart_0000] (PID 132157) rss_mb | MB | 1 | 1.535 | 1.535 | 1.535 | 1.535 | n/a | n/a |
| sh [bart_0000] (PID 132157) vms_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| docker (PID 132173) rss_mb | MB | 1 | 26.934 | 26.934 | 26.934 | 26.934 | n/a | n/a |
| docker (PID 132173) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 132230) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 132230) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 132230) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 132230) rss_mb | MB | 2 | 13.932 | 2.227 | 25.637 | 25.637 | n/a | n/a |
| docker (PID 132230) vms_mb | MB | 2 | 846.486 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 132270) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 132270) rss_mb | MB | 4 | 3.584 | 0.633 | 12.438 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 132270) vms_mb | MB | 4 | 411.474 | 1.055 | 1642.730 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 132284) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 132284) rss_mb | MB | 3 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [bart_0000] (PID 132284) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 132295) rss_mb | MB | 1 | 27.281 | 27.281 | 27.281 | 27.281 | n/a | n/a |
| docker (PID 132295) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 132314) rss_mb | MB | 1 | 10.051 | 10.051 | 10.051 | 10.051 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 132314) vms_mb | MB | 1 | 1569.195 | 1569.195 | 1569.195 | 1569.195 | n/a | n/a |
| docker (PID 132387) rss_mb | MB | 1 | 23.031 | 23.031 | 23.031 | 23.031 | n/a | n/a |
| docker (PID 132387) vms_mb | MB | 1 | 1524.203 | 1524.203 | 1524.203 | 1524.203 | n/a | n/a |
| docker (PID 132395) rss_mb | MB | 1 | 26.039 | 26.039 | 26.039 | 26.039 | n/a | n/a |
| docker (PID 132395) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 132453) rss_mb | MB | 1 | 25.344 | 25.344 | 25.344 | 25.344 | n/a | n/a |
| docker (PID 132453) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [band_0000] (PID 132493) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [band_0000] (PID 132493) rss_mb | MB | 11 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [band_0000] (PID 132493) vms_mb | MB | 11 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 132505) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 132505) rss_mb | MB | 11 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [band_0000] (PID 132505) vms_mb | MB | 11 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 132507) rss_mb | MB | 1 | 19.809 | 19.809 | 19.809 | 19.809 | n/a | n/a |
| docker (PID 132507) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 132542) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 132542) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 132542) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 132542) rss_mb | MB | 9 | 27.371 | 27.371 | 27.371 | 27.371 | n/a | n/a |
| docker (PID 132542) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [band_0000] (PID 132562) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [band_0000] (PID 132562) rss_mb | MB | 8 | 3.383 | 3.383 | 3.383 | 3.383 | n/a | n/a |
| bash [band_0000] (PID 132562) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [band_0000] (PID 132571) CPU | percent | 7 | 99.288 | 88.114 | 107.944 | 88.118 | 0.710000 CPU seconds | n/a |
| python [band_0000] (PID 132571) rss_mb | MB | 8 | 31.106 | 12.586 | 42.094 | 42.094 | n/a | n/a |
| python [band_0000] (PID 132571) vms_mb | MB | 8 | 38.137 | 16.328 | 51.324 | 51.324 | n/a | n/a |
| docker (PID 132573) rss_mb | MB | 1 | 5.656 | 5.656 | 5.656 | 5.656 | n/a | n/a |
| docker (PID 132573) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 132582) rss_mb | MB | 1 | 26.871 | 26.871 | 26.871 | 26.871 | n/a | n/a |
| docker (PID 132582) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 132642) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 132642) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 132642) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 132642) rss_mb | MB | 2 | 26.770 | 26.770 | 26.770 | 26.770 | n/a | n/a |
| docker (PID 132642) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 132681) CPU | percent | 3 | 3.253 | 0.000 | 9.760 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 132681) rss_mb | MB | 4 | 3.719 | 0.633 | 12.977 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 132681) vms_mb | MB | 4 | 393.473 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 132692) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 132692) rss_mb | MB | 3 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [band_0000] (PID 132692) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 132702) rss_mb | MB | 1 | 27.590 | 27.590 | 27.590 | 27.590 | n/a | n/a |
| docker (PID 132702) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 132722) rss_mb | MB | 1 | 11.957 | 11.957 | 11.957 | 11.957 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 132722) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 132757) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 132757) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 132803) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 132803) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 132803) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 132803) rss_mb | MB | 2 | 21.486 | 16.961 | 26.012 | 26.012 | n/a | n/a |
| docker (PID 132803) vms_mb | MB | 2 | 1588.080 | 1515.949 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 132852) rss_mb | MB | 1 | 25.621 | 25.621 | 25.621 | 25.621 | n/a | n/a |
| docker (PID 132852) vms_mb | MB | 1 | 1596.211 | 1596.211 | 1596.211 | 1596.211 | n/a | n/a |
| docker (PID 132887) CPU | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 132887) io read MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 132887) io write MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 132887) rss_mb | MB | 40 | 24.953 | 5.281 | 25.457 | 25.457 | n/a | n/a |
| docker (PID 132887) vms_mb | MB | 40 | 1619.525 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 132903) rss_mb | MB | 1 | 8.680 | 8.680 | 8.680 | 8.680 | n/a | n/a |
| docker (PID 132903) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 132919) rss_mb | MB | 1 | 27.094 | 27.094 | 27.094 | 27.094 | n/a | n/a |
| docker (PID 132919) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 132934) CPU | percent | 3 | 102.095 | 88.970 | 108.878 | 108.878 | 0.310000 CPU seconds | n/a |
| python3 (PID 132934) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 132934) io write MB/s | MB/s | 3 | 0.838 | 0.000 | 2.513 | 2.513 | 0.253906 MB | n/a |
| python3 (PID 132934) rss_mb | MB | 4 | 26.706 | 14.855 | 34.637 | 34.637 | n/a | n/a |
| python3 (PID 132934) vms_mb | MB | 4 | 50.429 | 39.770 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 132945) rss_mb | MB | 1 | 9.277 | 9.277 | 9.277 | 9.277 | n/a | n/a |
| docker (PID 132945) vms_mb | MB | 1 | 1307.691 | 1307.691 | 1307.691 | 1307.691 | n/a | n/a |
| docker (PID 132988) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 132988) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 132988) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 132988) rss_mb | MB | 2 | 27.535 | 27.535 | 27.535 | 27.535 | n/a | n/a |
| docker (PID 132988) vms_mb | MB | 2 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [base_0000] (PID 133028) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [base_0000] (PID 133028) rss_mb | MB | 4 | 3.725 | 0.633 | 13.000 | 0.633 | n/a | n/a |
| docker-init [base_0000] (PID 133028) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 133043) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 133043) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [base_0000] (PID 133043) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 133073) rss_mb | MB | 1 | 8.543 | 8.543 | 8.543 | 8.543 | n/a | n/a |
| docker (PID 133073) vms_mb | MB | 1 | 1226.309 | 1226.309 | 1226.309 | 1226.309 | n/a | n/a |
| docker (PID 133108) rss_mb | MB | 1 | 27.578 | 27.578 | 27.578 | 27.578 | n/a | n/a |
| docker (PID 133108) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 133144) rss_mb | MB | 1 | 27.422 | 27.422 | 27.422 | 27.422 | n/a | n/a |
| docker (PID 133144) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 133165) rss_mb | MB | 1 | 11.449 | 11.449 | 11.449 | 11.449 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 133165) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 133192) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 133192) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 133192) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 133192) rss_mb | MB | 2 | 27.035 | 27.035 | 27.035 | 27.035 | n/a | n/a |
| docker (PID 133192) vms_mb | MB | 2 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 133212) rss_mb | MB | 1 | 23.668 | 23.668 | 23.668 | 23.668 | n/a | n/a |
| docker (PID 133212) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 133239) CPU | percent | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 133239) io read MB/s | MB/s | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 133239) io write MB/s | MB/s | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 133239) rss_mb | MB | 41 | 26.492 | 26.492 | 26.492 | 26.492 | n/a | n/a |
| docker (PID 133239) vms_mb | MB | 41 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 133278) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 133278) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 133278) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 133278) rss_mb | MB | 2 | 25.516 | 25.516 | 25.516 | 25.516 | n/a | n/a |
| docker (PID 133278) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 133318) CPU | percent | 5 | 3.925 | 0.000 | 19.623 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 133318) rss_mb | MB | 6 | 2.568 | 0.633 | 12.242 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 133318) vms_mb | MB | 6 | 262.583 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 133330) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 133330) rss_mb | MB | 5 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [base_0000] (PID 133330) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 133342) CPU | percent | 1 | 19.527 | 19.527 | 19.527 | 19.527 | 0.020000 CPU seconds | n/a |
| docker (PID 133342) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 133342) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 133342) rss_mb | MB | 2 | 15.430 | 3.402 | 27.457 | 27.457 | n/a | n/a |
| docker (PID 133342) vms_mb | MB | 2 | 846.768 | 32.762 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 133402) rss_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| docker (PID 133402) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 133422) rss_mb | MB | 1 | 11.363 | 11.363 | 11.363 | 11.363 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 133422) vms_mb | MB | 1 | 1497.844 | 1497.844 | 1497.844 | 1497.844 | n/a | n/a |
| docker (PID 133440) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 133440) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 133440) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 133440) rss_mb | MB | 2 | 25.957 | 25.957 | 25.957 | 25.957 | n/a | n/a |
| docker (PID 133440) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 133497) rss_mb | MB | 1 | 1.512 | 1.512 | 1.512 | 1.512 | n/a | n/a |
| docker (PID 133497) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 133524) CPU | percent | 1 | 9.785 | 9.785 | 9.785 | 9.785 | 0.010000 CPU seconds | n/a |
| docker (PID 133524) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 133524) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 133524) rss_mb | MB | 2 | 13.068 | 0.000 | 26.137 | 26.137 | n/a | n/a |
| docker (PID 133524) vms_mb | MB | 2 | 845.660 | 30.547 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 133564) CPU | percent | 3 | 3.273 | 0.000 | 9.820 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 133564) rss_mb | MB | 4 | 3.504 | 0.633 | 12.117 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 133564) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 133576) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 133576) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [bart_0000] (PID 133576) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 133586) rss_mb | MB | 1 | 27.516 | 27.516 | 27.516 | 27.516 | n/a | n/a |
| docker (PID 133586) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 133613) rss_mb | MB | 1 | 27.375 | 27.375 | 27.375 | 27.375 | n/a | n/a |
| docker (PID 133613) vms_mb | MB | 1 | 1733.027 | 1733.027 | 1733.027 | 1733.027 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 133634) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 133634) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| docker (PID 133679) rss_mb | MB | 1 | 1.074 | 1.074 | 1.074 | 1.074 | n/a | n/a |
| docker (PID 133679) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 133688) rss_mb | MB | 1 | 26.934 | 26.934 | 26.934 | 26.934 | n/a | n/a |
| docker (PID 133688) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 133747) rss_mb | MB | 1 | 26.543 | 26.543 | 26.543 | 26.543 | n/a | n/a |
| docker (PID 133747) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [bart_0000] (PID 133790) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bart_0000] (PID 133790) rss_mb | MB | 11 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bart_0000] (PID 133790) vms_mb | MB | 11 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 133802) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 133802) rss_mb | MB | 11 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bart_0000] (PID 133802) vms_mb | MB | 11 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 133805) rss_mb | MB | 1 | 23.574 | 23.574 | 23.574 | 23.574 | n/a | n/a |
| docker (PID 133805) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 133840) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 133840) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 133840) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 133840) rss_mb | MB | 9 | 27.410 | 27.410 | 27.410 | 27.410 | n/a | n/a |
| docker (PID 133840) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [bart_0000] (PID 133860) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bart_0000] (PID 133860) rss_mb | MB | 8 | 3.277 | 3.277 | 3.277 | 3.277 | n/a | n/a |
| bash [bart_0000] (PID 133860) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bart_0000] (PID 133869) CPU | percent | 7 | 100.761 | 97.564 | 107.939 | 107.939 | 0.720000 CPU seconds | n/a |
| python [bart_0000] (PID 133869) rss_mb | MB | 8 | 31.774 | 14.797 | 40.977 | 40.977 | n/a | n/a |
| python [bart_0000] (PID 133869) vms_mb | MB | 8 | 38.745 | 18.508 | 50.324 | 50.324 | n/a | n/a |
| docker (PID 133879) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 133879) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 133879) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 133879) rss_mb | MB | 2 | 26.176 | 26.176 | 26.176 | 26.176 | n/a | n/a |
| docker (PID 133879) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 133931) rss_mb | MB | 1 | 21.184 | 21.184 | 21.184 | 21.184 | n/a | n/a |
| docker (PID 133931) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 133939) rss_mb | MB | 1 | 27.211 | 27.211 | 27.211 | 27.211 | n/a | n/a |
| docker (PID 133939) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 133978) CPU | percent | 3 | 6.411 | 0.000 | 19.232 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 133978) rss_mb | MB | 4 | 3.255 | 0.633 | 11.121 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 133978) vms_mb | MB | 4 | 393.090 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 133990) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 133990) rss_mb | MB | 3 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [bart_0000] (PID 133990) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 134000) rss_mb | MB | 1 | 18.359 | 18.359 | 18.359 | 18.359 | n/a | n/a |
| docker (PID 134000) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 134027) rss_mb | MB | 1 | 27.535 | 27.535 | 27.535 | 27.535 | n/a | n/a |
| docker (PID 134027) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 134047) rss_mb | MB | 1 | 10.816 | 10.816 | 10.816 | 10.816 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 134047) vms_mb | MB | 1 | 1497.707 | 1497.707 | 1497.707 | 1497.707 | n/a | n/a |
| docker (PID 134062) rss_mb | MB | 1 | 27.250 | 27.250 | 27.250 | 27.250 | n/a | n/a |
| docker (PID 134062) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 134082) rss_mb | MB | 1 | 11.398 | 11.398 | 11.398 | 11.398 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 134082) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 134098) rss_mb | MB | 1 | 25.723 | 25.723 | 25.723 | 25.723 | n/a | n/a |
| docker (PID 134098) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 134174) rss_mb | MB | 1 | 22.836 | 22.836 | 22.836 | 22.836 | n/a | n/a |
| docker (PID 134174) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 134182) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 134182) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 134182) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 134182) rss_mb | MB | 39 | 25.609 | 25.609 | 25.609 | 25.609 | n/a | n/a |
| docker (PID 134182) vms_mb | MB | 39 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 134207) rss_mb | MB | 1 | 26.762 | 26.762 | 26.762 | 26.762 | n/a | n/a |
| docker (PID 134207) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 134230) CPU | percent | 2 | 98.790 | 98.608 | 98.973 | 98.973 | 0.200000 CPU seconds | n/a |
| python3 (PID 134230) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 134230) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 134230) rss_mb | MB | 3 | 28.156 | 21.898 | 33.918 | 33.918 | n/a | n/a |
| python3 (PID 134230) vms_mb | MB | 3 | 51.427 | 45.652 | 56.461 | 56.461 | n/a | n/a |
| docker (PID 134232) rss_mb | MB | 1 | 10.230 | 10.230 | 10.230 | 10.230 | n/a | n/a |
| docker (PID 134232) vms_mb | MB | 1 | 1451.949 | 1451.949 | 1451.949 | 1451.949 | n/a | n/a |
| docker (PID 134256) rss_mb | MB | 1 | 26.898 | 26.898 | 26.898 | 26.898 | n/a | n/a |
| docker (PID 134256) vms_mb | MB | 1 | 1588.770 | 1588.770 | 1588.770 | 1588.770 | n/a | n/a |
| docker (PID 134280) CPU | percent | 1 | 9.873 | 9.873 | 9.873 | 9.873 | 0.010000 CPU seconds | n/a |
| docker (PID 134280) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 134280) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 134280) rss_mb | MB | 2 | 26.980 | 26.559 | 27.402 | 27.402 | n/a | n/a |
| docker (PID 134280) vms_mb | MB | 2 | 1732.777 | 1660.773 | 1804.781 | 1804.781 | n/a | n/a |
| docker-init [beam_0000] (PID 134323) CPU | percent | 4 | 7.353 | 0.000 | 29.413 | 0.000 | 0.030000 CPU seconds | n/a |
| docker-init [beam_0000] (PID 134323) rss_mb | MB | 5 | 2.748 | 0.633 | 11.207 | 0.633 | n/a | n/a |
| docker-init [beam_0000] (PID 134323) vms_mb | MB | 5 | 314.733 | 1.055 | 1569.445 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 134337) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 134337) rss_mb | MB | 4 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [beam_0000] (PID 134337) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 134339) rss_mb | MB | 1 | 27.234 | 27.234 | 27.234 | 27.234 | n/a | n/a |
| docker (PID 134339) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] (PID 134357) rss_mb | MB | 1 | 10.637 | 10.637 | 10.637 | 10.637 | n/a | n/a |
| runc:[2:INIT] (PID 134357) vms_mb | MB | 1 | 1569.582 | 1569.582 | 1569.582 | 1569.582 | n/a | n/a |
| docker (PID 134372) rss_mb | MB | 1 | 27.414 | 27.414 | 27.414 | 27.414 | n/a | n/a |
| docker (PID 134372) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 134394) rss_mb | MB | 1 | 11.520 | 11.520 | 11.520 | 11.520 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 134394) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 134437) rss_mb | MB | 1 | 3.645 | 3.645 | 3.645 | 3.645 | n/a | n/a |
| docker (PID 134437) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 134473) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 134473) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 134473) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 134473) rss_mb | MB | 2 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| docker (PID 134473) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 134534) rss_mb | MB | 1 | 25.441 | 25.441 | 25.441 | 25.441 | n/a | n/a |
| docker (PID 134534) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [beam_0000] (PID 134573) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beam_0000] (PID 134573) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [beam_0000] (PID 134573) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 134586) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 134586) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [beam_0000] (PID 134586) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 134588) rss_mb | MB | 1 | 22.559 | 22.559 | 22.559 | 22.559 | n/a | n/a |
| docker (PID 134588) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 134623) rss_mb | MB | 1 | 27.500 | 27.500 | 27.500 | 27.500 | n/a | n/a |
| docker (PID 134623) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 134658) rss_mb | MB | 1 | 27.371 | 27.371 | 27.371 | 27.371 | n/a | n/a |
| docker (PID 134658) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 134678) rss_mb | MB | 1 | 10.273 | 10.273 | 10.273 | 10.273 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 134678) vms_mb | MB | 1 | 1569.195 | 1569.195 | 1569.195 | 1569.195 | n/a | n/a |
| docker (PID 134694) rss_mb | MB | 1 | 26.059 | 26.059 | 26.059 | 26.059 | n/a | n/a |
| docker (PID 134694) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 134776) CPU | percent | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 134776) io read MB/s | MB/s | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 134776) io write MB/s | MB/s | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 134776) rss_mb | MB | 47 | 25.621 | 25.621 | 25.621 | 25.621 | n/a | n/a |
| docker (PID 134776) vms_mb | MB | 47 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 134801) rss_mb | MB | 1 | 25.551 | 25.551 | 25.551 | 25.551 | n/a | n/a |
| docker (PID 134801) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 134816) CPU | percent | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 134816) io read MB/s | MB/s | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 134816) io write MB/s | MB/s | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 134816) rss_mb | MB | 47 | 25.652 | 25.652 | 25.652 | 25.652 | n/a | n/a |
| docker (PID 134816) vms_mb | MB | 47 | 1659.961 | 1659.961 | 1659.961 | 1659.961 | n/a | n/a |
| docker (PID 134832) rss_mb | MB | 1 | 20.020 | 20.020 | 20.020 | 20.020 | n/a | n/a |
| docker (PID 134832) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 134868) rss_mb | MB | 1 | 25.992 | 25.992 | 25.992 | 25.992 | n/a | n/a |
| docker (PID 134868) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 134878) rss_mb | MB | 1 | 8.844 | 8.844 | 8.844 | 8.844 | n/a | n/a |
| docker (PID 134878) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 134887) rss_mb | MB | 1 | 26.984 | 26.984 | 26.984 | 26.984 | n/a | n/a |
| docker (PID 134887) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 134926) CPU | percent | 3 | 9.714 | 0.000 | 29.143 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 134926) rss_mb | MB | 4 | 3.241 | 0.633 | 11.066 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 134926) vms_mb | MB | 4 | 393.215 | 1.055 | 1569.695 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 134939) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 134939) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [base_0000] (PID 134939) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 134949) rss_mb | MB | 1 | 20.762 | 20.762 | 20.762 | 20.762 | n/a | n/a |
| docker (PID 134949) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 134976) rss_mb | MB | 1 | 27.023 | 27.023 | 27.023 | 27.023 | n/a | n/a |
| docker (PID 134976) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 134996) rss_mb | MB | 1 | 11.949 | 11.949 | 11.949 | 11.949 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 134996) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 135012) rss_mb | MB | 1 | 26.980 | 26.980 | 26.980 | 26.980 | n/a | n/a |
| docker (PID 135012) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| sh [base_0000] (PID 135032) rss_mb | MB | 1 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| sh [base_0000] (PID 135032) vms_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| docker (PID 135052) rss_mb | MB | 1 | 26.922 | 26.922 | 26.922 | 26.922 | n/a | n/a |
| docker (PID 135052) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 135112) rss_mb | MB | 1 | 25.633 | 25.633 | 25.633 | 25.633 | n/a | n/a |
| docker (PID 135112) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [beam_0000] (PID 135152) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beam_0000] (PID 135152) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [beam_0000] (PID 135152) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 135163) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 135163) rss_mb | MB | 3 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [beam_0000] (PID 135163) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 135165) rss_mb | MB | 1 | 23.621 | 23.621 | 23.621 | 23.621 | n/a | n/a |
| docker (PID 135165) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 135200) rss_mb | MB | 1 | 26.945 | 26.945 | 26.945 | 26.945 | n/a | n/a |
| docker (PID 135200) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 135237) rss_mb | MB | 1 | 27.254 | 27.254 | 27.254 | 27.254 | n/a | n/a |
| docker (PID 135237) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 135258) rss_mb | MB | 1 | 11.781 | 11.781 | 11.781 | 11.781 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 135258) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 135277) rss_mb | MB | 1 | 26.180 | 26.180 | 26.180 | 26.180 | n/a | n/a |
| docker (PID 135277) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 135334) CPU | percent | 1 | 9.849 | 9.849 | 9.849 | 9.849 | 0.010000 CPU seconds | n/a |
| docker (PID 135334) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 135334) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 135334) rss_mb | MB | 2 | 15.770 | 4.938 | 26.602 | 26.602 | n/a | n/a |
| docker (PID 135334) vms_mb | MB | 2 | 846.768 | 32.762 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 135373) CPU | percent | 10 | 0.981 | 0.000 | 9.805 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 135373) rss_mb | MB | 11 | 1.714 | 0.633 | 12.523 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 135373) vms_mb | MB | 11 | 143.752 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 135388) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 135388) rss_mb | MB | 10 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [base_0000] (PID 135388) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 135398) rss_mb | MB | 1 | 27.363 | 27.363 | 27.363 | 27.363 | n/a | n/a |
| docker (PID 135398) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 135417) rss_mb | MB | 1 | 10.918 | 10.918 | 10.918 | 10.918 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 135417) vms_mb | MB | 1 | 1641.707 | 1641.707 | 1641.707 | 1641.707 | n/a | n/a |
| docker (PID 135425) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 135425) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 135425) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 135425) rss_mb | MB | 8 | 27.684 | 27.684 | 27.684 | 27.684 | n/a | n/a |
| docker (PID 135425) vms_mb | MB | 8 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| bash [base_0000] (PID 135445) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [base_0000] (PID 135445) rss_mb | MB | 8 | 3.387 | 3.387 | 3.387 | 3.387 | n/a | n/a |
| bash [base_0000] (PID 135445) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [base_0000] (PID 135454) CPU | percent | 7 | 99.337 | 97.166 | 107.909 | 98.121 | 0.710000 CPU seconds | n/a |
| python [base_0000] (PID 135454) rss_mb | MB | 8 | 30.225 | 7.801 | 41.605 | 41.605 | n/a | n/a |
| python [base_0000] (PID 135454) vms_mb | MB | 8 | 37.340 | 12.070 | 51.027 | 51.027 | n/a | n/a |
| docker (PID 135456) rss_mb | MB | 1 | 3.219 | 3.219 | 3.219 | 3.219 | n/a | n/a |
| docker (PID 135456) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 135464) rss_mb | MB | 1 | 27.293 | 27.293 | 27.293 | 27.293 | n/a | n/a |
| docker (PID 135464) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 135523) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 135523) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 135523) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 135523) rss_mb | MB | 2 | 26.941 | 26.941 | 26.941 | 26.941 | n/a | n/a |
| docker (PID 135523) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [beam_0000] (PID 135564) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beam_0000] (PID 135564) rss_mb | MB | 10 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [beam_0000] (PID 135564) vms_mb | MB | 10 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 135576) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 135576) rss_mb | MB | 10 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [beam_0000] (PID 135576) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 135611) CPU | percent | 8 | 1.219 | 0.000 | 9.751 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 135611) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 135611) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 135611) rss_mb | MB | 9 | 26.311 | 16.578 | 27.527 | 27.527 | n/a | n/a |
| docker (PID 135611) vms_mb | MB | 9 | 1644.682 | 1515.949 | 1660.773 | 1660.773 | n/a | n/a |
| bash [beam_0000] (PID 135631) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [beam_0000] (PID 135631) rss_mb | MB | 8 | 3.320 | 3.320 | 3.320 | 3.320 | n/a | n/a |
| bash [beam_0000] (PID 135631) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [beam_0000] (PID 135640) CPU | percent | 7 | 99.417 | 97.442 | 107.995 | 98.164 | 0.710000 CPU seconds | n/a |
| python [beam_0000] (PID 135640) rss_mb | MB | 8 | 31.719 | 12.578 | 41.977 | 41.977 | n/a | n/a |
| python [beam_0000] (PID 135640) vms_mb | MB | 8 | 38.858 | 16.277 | 52.238 | 52.238 | n/a | n/a |
| docker (PID 135650) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 135650) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 135650) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 135650) rss_mb | MB | 2 | 25.918 | 25.918 | 25.918 | 25.918 | n/a | n/a |
| docker (PID 135650) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 135710) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 135710) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 135710) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 135710) rss_mb | MB | 2 | 25.664 | 25.664 | 25.664 | 25.664 | n/a | n/a |
| docker (PID 135710) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 135750) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [beam_0000] (PID 135750) rss_mb | MB | 3 | 4.737 | 0.633 | 12.945 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 135750) vms_mb | MB | 3 | 524.195 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 135763) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 135763) rss_mb | MB | 2 | 1.773 | 1.773 | 1.773 | 1.773 | n/a | n/a |
| tail [beam_0000] (PID 135763) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 135839) rss_mb | MB | 1 | 25.598 | 25.598 | 25.598 | 25.598 | n/a | n/a |
| docker (PID 135839) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 135877) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 135877) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 135877) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 135877) rss_mb | MB | 2 | 27.211 | 27.211 | 27.211 | 27.211 | n/a | n/a |
| docker (PID 135877) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 135928) rss_mb | MB | 1 | 25.203 | 25.203 | 25.203 | 25.203 | n/a | n/a |
| docker (PID 135928) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 135961) CPU | percent | 39 | 0.253 | 0.000 | 9.864 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 135961) io read MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 135961) io write MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 135961) rss_mb | MB | 40 | 25.030 | 13.699 | 25.320 | 25.320 | n/a | n/a |
| docker (PID 135961) vms_mb | MB | 40 | 1656.604 | 1515.949 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 135985) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 135985) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 135985) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 135985) rss_mb | MB | 2 | 26.875 | 26.875 | 26.875 | 26.875 | n/a | n/a |
| docker (PID 135985) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 136027) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 136027) rss_mb | MB | 5 | 3.139 | 0.633 | 13.164 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 136027) vms_mb | MB | 5 | 329.440 | 1.055 | 1642.980 | 1.055 | n/a | n/a |
| docker (PID 136042) rss_mb | MB | 1 | 27.004 | 27.004 | 27.004 | 27.004 | n/a | n/a |
| docker (PID 136042) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| tail [base_0000] (PID 136056) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 136056) rss_mb | MB | 4 | 1.699 | 1.699 | 1.699 | 1.699 | n/a | n/a |
| tail [base_0000] (PID 136056) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 136064) rss_mb | MB | 1 | 25.785 | 25.785 | 25.785 | 25.785 | n/a | n/a |
| docker (PID 136064) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 136072) rss_mb | MB | 1 | 27.242 | 27.242 | 27.242 | 27.242 | n/a | n/a |
| docker (PID 136072) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 136108) rss_mb | MB | 1 | 27.316 | 27.316 | 27.316 | 27.316 | n/a | n/a |
| docker (PID 136108) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| python3 (PID 136127) CPU | percent | 4 | 86.327 | 64.900 | 98.194 | 98.194 | 0.360000 CPU seconds | n/a |
| python3 (PID 136127) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 136127) io write MB/s | MB/s | 4 | 0.623 | 0.000 | 2.493 | 2.493 | 0.253906 MB | n/a |
| python3 (PID 136127) rss_mb | MB | 5 | 26.868 | 17.688 | 34.535 | 34.535 | n/a | n/a |
| python3 (PID 136127) vms_mb | MB | 5 | 50.529 | 42.449 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 136145) rss_mb | MB | 1 | 26.051 | 26.051 | 26.051 | 26.051 | n/a | n/a |
| docker (PID 136145) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 136176) rss_mb | MB | 1 | 15.598 | 15.598 | 15.598 | 15.598 | n/a | n/a |
| docker (PID 136176) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 136184) rss_mb | MB | 1 | 27.035 | 27.035 | 27.035 | 27.035 | n/a | n/a |
| docker (PID 136184) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 136225) rss_mb | MB | 1 | 26.621 | 26.621 | 26.621 | 26.621 | n/a | n/a |
| docker (PID 136225) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 136257) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 136257) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 136257) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 136257) rss_mb | MB | 2 | 26.555 | 26.242 | 26.867 | 26.867 | n/a | n/a |
| docker (PID 136257) vms_mb | MB | 2 | 1660.523 | 1660.273 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 136271) rss_mb | MB | 1 | 1.797 | 1.797 | 1.797 | 1.797 | n/a | n/a |
| docker (PID 136271) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 136308) rss_mb | MB | 1 | 27.062 | 27.062 | 27.062 | 27.062 | n/a | n/a |
| docker (PID 136308) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 136317) CPU | percent | 7 | 4.175 | 0.000 | 29.223 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 136317) rss_mb | MB | 8 | 1.975 | 0.633 | 11.371 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 136317) vms_mb | MB | 8 | 197.166 | 1.055 | 1569.945 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 136330) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 136330) rss_mb | MB | 7 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [base_0000] (PID 136330) vms_mb | MB | 7 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 136332) rss_mb | MB | 1 | 25.719 | 25.719 | 25.719 | 25.719 | n/a | n/a |
| docker (PID 136332) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 136367) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 136367) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 136367) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 136367) rss_mb | MB | 5 | 27.484 | 27.484 | 27.484 | 27.484 | n/a | n/a |
| docker (PID 136367) vms_mb | MB | 5 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| bash [base_0000] (PID 136390) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [base_0000] (PID 136390) rss_mb | MB | 4 | 3.355 | 3.355 | 3.355 | 3.355 | n/a | n/a |
| bash [base_0000] (PID 136390) vms_mb | MB | 4 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [base_0000] (PID 136399) CPU | percent | 3 | 97.362 | 97.249 | 97.430 | 97.408 | 0.300000 CPU seconds | n/a |
| python [base_0000] (PID 136399) rss_mb | MB | 4 | 25.762 | 14.562 | 35.133 | 35.133 | n/a | n/a |
| python [base_0000] (PID 136399) vms_mb | MB | 4 | 33.103 | 18.430 | 45.023 | 45.023 | n/a | n/a |
| docker (PID 136409) CPU | percent | 1 | 9.630 | 9.630 | 9.630 | 9.630 | 0.010000 CPU seconds | n/a |
| docker (PID 136409) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 136409) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 136409) rss_mb | MB | 2 | 21.230 | 15.445 | 27.016 | 27.016 | n/a | n/a |
| docker (PID 136409) vms_mb | MB | 2 | 1588.236 | 1515.699 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 136462) rss_mb | MB | 1 | 26.504 | 26.504 | 26.504 | 26.504 | n/a | n/a |
| docker (PID 136462) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 136477) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 136477) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 136477) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 136477) rss_mb | MB | 2 | 27.281 | 27.281 | 27.281 | 27.281 | n/a | n/a |
| docker (PID 136477) vms_mb | MB | 2 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 136486) rss_mb | MB | 1 | 8.598 | 8.598 | 8.598 | 8.598 | n/a | n/a |
| docker (PID 136486) vms_mb | MB | 1 | 1226.309 | 1226.309 | 1226.309 | 1226.309 | n/a | n/a |
| docker (PID 136520) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 136520) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 136520) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 136520) rss_mb | MB | 2 | 25.832 | 25.832 | 25.832 | 25.832 | n/a | n/a |
| docker (PID 136520) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bear_0000] (PID 136534) CPU | percent | 5 | 3.793 | 0.000 | 18.966 | 0.000 | 0.020000 CPU seconds | n/a |
| docker-init [bear_0000] (PID 136534) rss_mb | MB | 6 | 2.544 | 0.633 | 12.098 | 0.633 | n/a | n/a |
| docker-init [bear_0000] (PID 136534) vms_mb | MB | 6 | 262.583 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| docker-init [base_0000] (PID 136576) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [base_0000] (PID 136576) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [base_0000] (PID 136576) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 136588) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 136588) rss_mb | MB | 5 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [bear_0000] (PID 136588) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 136590) rss_mb | MB | 1 | 27.293 | 27.293 | 27.293 | 27.293 | n/a | n/a |
| docker (PID 136590) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] (PID 136615) rss_mb | MB | 1 | 11.039 | 11.039 | 11.039 | 11.039 | n/a | n/a |
| runc:[2:INIT] (PID 136615) vms_mb | MB | 1 | 1570.211 | 1570.211 | 1570.211 | 1570.211 | n/a | n/a |
| tail [base_0000] (PID 136616) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 136616) rss_mb | MB | 4 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [base_0000] (PID 136616) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 136638) rss_mb | MB | 1 | 27.336 | 27.336 | 27.336 | 27.336 | n/a | n/a |
| docker (PID 136638) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 136648) rss_mb | MB | 1 | 26.625 | 26.625 | 26.625 | 26.625 | n/a | n/a |
| docker (PID 136648) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 136665) rss_mb | MB | 1 | 11.898 | 11.898 | 11.898 | 11.898 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 136665) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 136692) rss_mb | MB | 1 | 27.523 | 27.523 | 27.523 | 27.523 | n/a | n/a |
| docker (PID 136692) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 136700) rss_mb | MB | 1 | 27.234 | 27.234 | 27.234 | 27.234 | n/a | n/a |
| docker (PID 136700) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 136718) rss_mb | MB | 1 | 11.547 | 11.547 | 11.547 | 11.547 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 136718) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 136754) rss_mb | MB | 1 | 27.324 | 27.324 | 27.324 | 27.324 | n/a | n/a |
| docker (PID 136754) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 136784) rss_mb | MB | 1 | 8.719 | 8.719 | 8.719 | 8.719 | n/a | n/a |
| docker (PID 136784) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 136785) rss_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 136785) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 136827) rss_mb | MB | 1 | 27.000 | 27.000 | 27.000 | 27.000 | n/a | n/a |
| docker (PID 136827) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 136850) CPU | percent | 1 | 17.006 | 17.006 | 17.006 | 17.006 | 0.020000 CPU seconds | n/a |
| docker (PID 136850) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 136850) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 136850) rss_mb | MB | 2 | 22.713 | 18.406 | 27.020 | 27.020 | n/a | n/a |
| docker (PID 136850) vms_mb | MB | 2 | 1588.236 | 1515.699 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 136904) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 136904) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 136944) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 136944) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 136944) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 136944) rss_mb | MB | 2 | 26.570 | 26.570 | 26.570 | 26.570 | n/a | n/a |
| docker (PID 136944) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 136982) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 136982) rss_mb | MB | 4 | 3.646 | 0.633 | 12.684 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 136982) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 136994) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 136994) rss_mb | MB | 3 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [bear_0000] (PID 136994) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 137005) rss_mb | MB | 1 | 27.473 | 27.473 | 27.473 | 27.473 | n/a | n/a |
| docker (PID 137005) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 137070) rss_mb | MB | 1 | 22.398 | 22.398 | 22.398 | 22.398 | n/a | n/a |
| docker (PID 137070) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 137107) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 137107) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 137107) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 137107) rss_mb | MB | 2 | 26.094 | 26.094 | 26.094 | 26.094 | n/a | n/a |
| docker (PID 137107) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 137169) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 137169) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 137169) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 137169) rss_mb | MB | 2 | 27.148 | 27.148 | 27.148 | 27.148 | n/a | n/a |
| docker (PID 137169) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 137208) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 137208) rss_mb | MB | 3 | 4.810 | 0.633 | 13.164 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 137208) vms_mb | MB | 3 | 548.197 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 137224) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 137224) rss_mb | MB | 2 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [bear_0000] (PID 137224) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 137234) rss_mb | MB | 1 | 27.336 | 27.336 | 27.336 | 27.336 | n/a | n/a |
| docker (PID 137234) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 137255) rss_mb | MB | 1 | 11.801 | 11.801 | 11.801 | 11.801 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 137255) vms_mb | MB | 1 | 1498.223 | 1498.223 | 1498.223 | 1498.223 | n/a | n/a |
| docker (PID 137299) rss_mb | MB | 1 | 26.488 | 26.488 | 26.488 | 26.488 | n/a | n/a |
| docker (PID 137299) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 137307) rss_mb | MB | 1 | 25.820 | 25.820 | 25.820 | 25.820 | n/a | n/a |
| docker (PID 137307) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 137369) rss_mb | MB | 1 | 25.762 | 25.762 | 25.762 | 25.762 | n/a | n/a |
| docker (PID 137369) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bear_0000] (PID 137410) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bear_0000] (PID 137410) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bear_0000] (PID 137410) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 137422) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 137422) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [bear_0000] (PID 137422) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 137424) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 137424) vms_mb | MB | 1 | 30.523 | 30.523 | 30.523 | 30.523 | n/a | n/a |
| docker (PID 137457) rss_mb | MB | 1 | 19.523 | 19.523 | 19.523 | 19.523 | n/a | n/a |
| docker (PID 137457) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 137499) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 137499) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 137499) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 137499) rss_mb | MB | 2 | 26.088 | 24.988 | 27.188 | 27.188 | n/a | n/a |
| docker (PID 137499) vms_mb | MB | 2 | 1660.492 | 1660.211 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 137557) CPU | percent | 1 | 9.738 | 9.738 | 9.738 | 9.738 | 0.010000 CPU seconds | n/a |
| docker (PID 137557) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 137557) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 137557) rss_mb | MB | 2 | 17.561 | 8.121 | 27.000 | 27.000 | n/a | n/a |
| docker (PID 137557) vms_mb | MB | 2 | 846.820 | 32.867 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 137607) CPU | percent | 5 | 5.731 | 0.000 | 28.656 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 137607) rss_mb | MB | 6 | 2.419 | 0.633 | 11.348 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 137607) vms_mb | MB | 6 | 250.475 | 1.055 | 1497.578 | 1.055 | n/a | n/a |
| docker (PID 137630) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 137630) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| tail [bear_0000] (PID 137643) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 137643) rss_mb | MB | 5 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [bear_0000] (PID 137643) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 137645) rss_mb | MB | 1 | 25.426 | 25.426 | 25.426 | 25.426 | n/a | n/a |
| docker (PID 137645) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 137653) CPU | percent | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 137653) io read MB/s | MB/s | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 137653) io write MB/s | MB/s | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 137653) rss_mb | MB | 42 | 26.859 | 26.859 | 26.859 | 26.859 | n/a | n/a |
| docker (PID 137653) vms_mb | MB | 42 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 137658) rss_mb | MB | 1 | 26.914 | 26.914 | 26.914 | 26.914 | n/a | n/a |
| docker (PID 137658) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 137679) rss_mb | MB | 1 | 11.707 | 11.707 | 11.707 | 11.707 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 137679) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 137686) rss_mb | MB | 1 | 27.000 | 27.000 | 27.000 | 27.000 | n/a | n/a |
| docker (PID 137686) vms_mb | MB | 1 | 1733.027 | 1733.027 | 1733.027 | 1733.027 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 137706) rss_mb | MB | 1 | 11.828 | 11.828 | 11.828 | 11.828 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 137706) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 137722) rss_mb | MB | 1 | 27.121 | 27.121 | 27.121 | 27.121 | n/a | n/a |
| docker (PID 137722) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 137757) CPU | percent | 2 | 24.435 | 0.000 | 48.869 | 0.000 | 0.050000 CPU seconds | n/a |
| docker (PID 137757) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 137757) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 137757) rss_mb | MB | 3 | 25.771 | 23.461 | 26.926 | 26.926 | n/a | n/a |
| docker (PID 137757) vms_mb | MB | 3 | 1636.583 | 1588.203 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 137833) rss_mb | MB | 1 | 27.234 | 27.234 | 27.234 | 27.234 | n/a | n/a |
| docker (PID 137833) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 137849) CPU | percent | 3 | 98.693 | 89.033 | 108.757 | 89.033 | 0.300000 CPU seconds | n/a |
| python3 (PID 137849) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 137849) io write MB/s | MB/s | 3 | 0.786 | 0.000 | 2.357 | 2.357 | 0.238281 MB | n/a |
| python3 (PID 137849) rss_mb | MB | 4 | 26.604 | 14.688 | 34.648 | 34.648 | n/a | n/a |
| python3 (PID 137849) vms_mb | MB | 4 | 50.421 | 39.770 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 137867) rss_mb | MB | 1 | 27.145 | 27.145 | 27.145 | 27.145 | n/a | n/a |
| docker (PID 137867) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 137887) rss_mb | MB | 1 | 26.938 | 26.938 | 26.938 | 26.938 | n/a | n/a |
| docker (PID 137887) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 137901) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 137901) io read MB/s | MB/s | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 137901) io write MB/s | MB/s | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 137901) rss_mb | MB | 6 | 27.046 | 26.590 | 27.273 | 27.273 | n/a | n/a |
| docker (PID 137901) vms_mb | MB | 6 | 1756.779 | 1660.773 | 1804.781 | 1804.781 | n/a | n/a |
| runc:[0:PARENT] (PID 137944) rss_mb | MB | 1 | 1.949 | 1.949 | 1.949 | 1.949 | n/a | n/a |
| runc:[0:PARENT] (PID 137944) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[0:PARENT] (PID 137945) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[0:PARENT] (PID 137945) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| docker-init [beef_0000] (PID 137946) CPU | percent | 6 | 4.844 | 0.000 | 29.062 | 0.000 | 0.030000 CPU seconds | n/a |
| docker-init [beef_0000] (PID 137946) rss_mb | MB | 7 | 3.999 | 0.633 | 13.164 | 0.633 | n/a | n/a |
| docker-init [beef_0000] (PID 137946) vms_mb | MB | 7 | 449.385 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 137960) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 137960) rss_mb | MB | 5 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [beef_0000] (PID 137960) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 137962) rss_mb | MB | 1 | 27.055 | 27.055 | 27.055 | 27.055 | n/a | n/a |
| docker (PID 137962) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] (PID 137982) rss_mb | MB | 1 | 11.207 | 11.207 | 11.207 | 11.207 | n/a | n/a |
| runc:[2:INIT] (PID 137982) vms_mb | MB | 1 | 1641.965 | 1641.965 | 1641.965 | 1641.965 | n/a | n/a |
| docker (PID 138000) rss_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| docker (PID 138000) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 138029) rss_mb | MB | 1 | 26.820 | 26.820 | 26.820 | 26.820 | n/a | n/a |
| docker (PID 138029) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 138049) rss_mb | MB | 1 | 9.457 | 9.457 | 9.457 | 9.457 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 138049) vms_mb | MB | 1 | 1496.941 | 1496.941 | 1496.941 | 1496.941 | n/a | n/a |
| docker (PID 138063) rss_mb | MB | 1 | 27.195 | 27.195 | 27.195 | 27.195 | n/a | n/a |
| docker (PID 138063) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 138100) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 138100) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138100) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138100) rss_mb | MB | 2 | 26.176 | 26.176 | 26.176 | 26.176 | n/a | n/a |
| docker (PID 138100) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 138160) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 138160) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138160) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138160) rss_mb | MB | 2 | 26.555 | 26.555 | 26.555 | 26.555 | n/a | n/a |
| docker (PID 138160) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 138199) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [beef_0000] (PID 138199) rss_mb | MB | 4 | 3.768 | 0.633 | 13.172 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 138199) vms_mb | MB | 4 | 411.411 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 138212) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 138212) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [beef_0000] (PID 138212) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 138224) rss_mb | MB | 1 | 27.191 | 27.191 | 27.191 | 27.191 | n/a | n/a |
| docker (PID 138224) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 138243) rss_mb | MB | 1 | 11.480 | 11.480 | 11.480 | 11.480 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 138243) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 138322) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 138322) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138322) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138322) rss_mb | MB | 2 | 21.947 | 17.930 | 25.965 | 25.965 | n/a | n/a |
| docker (PID 138322) vms_mb | MB | 2 | 1587.955 | 1515.699 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 138388) rss_mb | MB | 1 | 20.539 | 20.539 | 20.539 | 20.539 | n/a | n/a |
| docker (PID 138388) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 138402) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 138402) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138402) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138402) rss_mb | MB | 38 | 27.055 | 27.055 | 27.055 | 27.055 | n/a | n/a |
| docker (PID 138402) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 138444) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 138444) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138444) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138444) rss_mb | MB | 2 | 27.090 | 27.090 | 27.090 | 27.090 | n/a | n/a |
| docker (PID 138444) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 138482) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 138482) rss_mb | MB | 4 | 3.634 | 0.633 | 12.637 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 138482) vms_mb | MB | 4 | 375.347 | 1.055 | 1498.223 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 138494) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 138494) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bear_0000] (PID 138494) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 138505) rss_mb | MB | 1 | 27.559 | 27.559 | 27.559 | 27.559 | n/a | n/a |
| docker (PID 138505) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 138525) rss_mb | MB | 1 | 11.645 | 11.645 | 11.645 | 11.645 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 138525) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 138569) rss_mb | MB | 1 | 1.117 | 1.117 | 1.117 | 1.117 | n/a | n/a |
| docker (PID 138569) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 138607) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 138607) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138607) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138607) rss_mb | MB | 2 | 23.869 | 21.879 | 25.859 | 25.859 | n/a | n/a |
| docker (PID 138607) vms_mb | MB | 2 | 1588.080 | 1515.949 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 138660) rss_mb | MB | 1 | 25.520 | 25.520 | 25.520 | 25.520 | n/a | n/a |
| docker (PID 138660) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bear_0000] (PID 138699) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bear_0000] (PID 138699) rss_mb | MB | 11 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bear_0000] (PID 138699) vms_mb | MB | 11 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 138712) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 138712) rss_mb | MB | 11 | 1.680 | 1.680 | 1.680 | 1.680 | n/a | n/a |
| tail [bear_0000] (PID 138712) vms_mb | MB | 11 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 138714) rss_mb | MB | 1 | 10.305 | 10.305 | 10.305 | 10.305 | n/a | n/a |
| docker (PID 138714) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 138749) CPU | percent | 8 | 1.228 | 0.000 | 9.821 | 9.821 | 0.010000 CPU seconds | n/a |
| docker (PID 138749) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138749) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138749) rss_mb | MB | 9 | 27.194 | 26.750 | 27.250 | 27.250 | n/a | n/a |
| docker (PID 138749) vms_mb | MB | 9 | 1660.746 | 1660.523 | 1660.773 | 1660.773 | n/a | n/a |
| bash [bear_0000] (PID 138769) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bear_0000] (PID 138769) rss_mb | MB | 8 | 3.480 | 3.480 | 3.480 | 3.480 | n/a | n/a |
| bash [bear_0000] (PID 138769) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bear_0000] (PID 138778) CPU | percent | 7 | 100.701 | 97.218 | 107.803 | 98.214 | 0.720000 CPU seconds | n/a |
| python [bear_0000] (PID 138778) rss_mb | MB | 8 | 31.477 | 13.230 | 41.004 | 41.004 | n/a | n/a |
| python [bear_0000] (PID 138778) vms_mb | MB | 8 | 38.655 | 16.477 | 50.340 | 50.340 | n/a | n/a |
| docker (PID 138788) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 138788) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138788) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138788) rss_mb | MB | 2 | 24.965 | 23.848 | 26.082 | 26.082 | n/a | n/a |
| docker (PID 138788) vms_mb | MB | 2 | 1624.207 | 1588.203 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 138887) CPU | percent | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 138887) io read MB/s | MB/s | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138887) io write MB/s | MB/s | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138887) rss_mb | MB | 44 | 27.016 | 27.016 | 27.016 | 27.016 | n/a | n/a |
| docker (PID 138887) vms_mb | MB | 44 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 138895) rss_mb | MB | 1 | 3.332 | 3.332 | 3.332 | 3.332 | n/a | n/a |
| docker (PID 138895) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 138912) rss_mb | MB | 1 | 25.445 | 25.445 | 25.445 | 25.445 | n/a | n/a |
| docker (PID 138912) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 138921) CPU | percent | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 138921) io read MB/s | MB/s | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138921) io write MB/s | MB/s | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 138921) rss_mb | MB | 45 | 26.762 | 26.762 | 26.762 | 26.762 | n/a | n/a |
| docker (PID 138921) vms_mb | MB | 45 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 138937) rss_mb | MB | 1 | 25.703 | 25.703 | 25.703 | 25.703 | n/a | n/a |
| docker (PID 138937) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 138981) rss_mb | MB | 1 | 26.883 | 26.883 | 26.883 | 26.883 | n/a | n/a |
| docker (PID 138981) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 138997) CPU | percent | 3 | 98.755 | 98.479 | 98.983 | 98.983 | 0.300000 CPU seconds | n/a |
| python3 (PID 138997) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 138997) io write MB/s | MB/s | 3 | 0.838 | 0.000 | 2.513 | 2.513 | 0.253906 MB | n/a |
| python3 (PID 138997) rss_mb | MB | 4 | 25.642 | 12.477 | 34.613 | 34.613 | n/a | n/a |
| python3 (PID 138997) vms_mb | MB | 4 | 49.703 | 38.293 | 57.434 | 57.434 | n/a | n/a |
| docker (PID 139023) rss_mb | MB | 1 | 3.324 | 3.324 | 3.324 | 3.324 | n/a | n/a |
| docker (PID 139023) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 139043) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 139043) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 139043) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 139043) rss_mb | MB | 2 | 25.828 | 25.828 | 25.828 | 25.828 | n/a | n/a |
| docker (PID 139043) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [beef_0000] (PID 139081) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beef_0000] (PID 139081) rss_mb | MB | 3 | 0.422 | 0.000 | 0.633 | 0.633 | n/a | n/a |
| docker-init [beef_0000] (PID 139081) vms_mb | MB | 3 | 1.010 | 0.922 | 1.055 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 139096) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 139096) rss_mb | MB | 2 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [beef_0000] (PID 139096) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 139135) rss_mb | MB | 1 | 5.656 | 5.656 | 5.656 | 5.656 | n/a | n/a |
| docker (PID 139135) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 139170) rss_mb | MB | 1 | 27.484 | 27.484 | 27.484 | 27.484 | n/a | n/a |
| docker (PID 139170) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 139208) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 139208) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 139208) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 139208) rss_mb | MB | 2 | 26.641 | 26.641 | 26.641 | 26.641 | n/a | n/a |
| docker (PID 139208) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 139271) rss_mb | MB | 1 | 25.797 | 25.797 | 25.797 | 25.797 | n/a | n/a |
| docker (PID 139271) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 139312) CPU | percent | 16 | 1.168 | 0.000 | 18.687 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [beef_0000] (PID 139312) rss_mb | MB | 17 | 1.320 | 0.633 | 12.309 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 139312) vms_mb | MB | 17 | 93.359 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| docker (PID 139319) rss_mb | MB | 1 | 23.852 | 23.852 | 23.852 | 23.852 | n/a | n/a |
| docker (PID 139319) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 139333) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 139333) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 139333) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 139333) rss_mb | MB | 3 | 27.479 | 27.078 | 27.680 | 27.680 | n/a | n/a |
| docker (PID 139333) vms_mb | MB | 3 | 1708.776 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| tail [beef_0000] (PID 139344) CPU | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 139344) rss_mb | MB | 16 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [beef_0000] (PID 139344) vms_mb | MB | 16 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 139356) rss_mb | MB | 1 | 4.469 | 4.469 | 4.469 | 4.469 | n/a | n/a |
| docker (PID 139356) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 139418) CPU | percent | 14 | 1.356 | 0.000 | 18.983 | 0.000 | 0.020000 CPU seconds | n/a |
| docker (PID 139418) io read MB/s | MB/s | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 139418) io write MB/s | MB/s | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 139418) rss_mb | MB | 15 | 25.570 | 4.043 | 27.215 | 27.215 | n/a | n/a |
| docker (PID 139418) vms_mb | MB | 15 | 1552.473 | 32.762 | 1661.023 | 1661.023 | n/a | n/a |
| docker-init [bell_0000] (PID 139424) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bell_0000] (PID 139424) rss_mb | MB | 5 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bell_0000] (PID 139424) vms_mb | MB | 5 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| bash [beef_0000] (PID 139446) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [beef_0000] (PID 139446) rss_mb | MB | 14 | 3.410 | 3.410 | 3.410 | 3.410 | n/a | n/a |
| bash [beef_0000] (PID 139446) vms_mb | MB | 14 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [beef_0000] (PID 139458) CPU | percent | 13 | 89.066 | 73.940 | 104.562 | 95.347 | 1.230000 CPU seconds | n/a |
| python [beef_0000] (PID 139458) rss_mb | MB | 14 | 31.075 | 7.074 | 42.648 | 42.648 | n/a | n/a |
| python [beef_0000] (PID 139458) vms_mb | MB | 14 | 38.332 | 11.809 | 52.238 | 52.238 | n/a | n/a |
| tail [bell_0000] (PID 139462) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 139462) rss_mb | MB | 5 | 1.681 | 1.453 | 1.738 | 1.738 | n/a | n/a |
| tail [bell_0000] (PID 139462) vms_mb | MB | 5 | 2.910 | 2.613 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 139492) rss_mb | MB | 1 | 6.344 | 6.344 | 6.344 | 6.344 | n/a | n/a |
| docker (PID 139492) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 139555) rss_mb | MB | 1 | 14.133 | 14.133 | 14.133 | 14.133 | n/a | n/a |
| docker (PID 139555) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 139601) rss_mb | MB | 1 | 25.891 | 25.891 | 25.891 | 25.891 | n/a | n/a |
| docker (PID 139601) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 139647) rss_mb | MB | 1 | 19.527 | 19.527 | 19.527 | 19.527 | n/a | n/a |
| docker (PID 139647) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 139655) rss_mb | MB | 1 | 27.000 | 27.000 | 27.000 | 27.000 | n/a | n/a |
| docker (PID 139655) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 139692) CPU | percent | 4 | 9.532 | 0.000 | 38.126 | 0.000 | 0.040000 CPU seconds | n/a |
| runc:[2:INIT] [bell_0000] (PID 139692) rss_mb | MB | 5 | 2.725 | 0.633 | 11.094 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 139692) vms_mb | MB | 5 | 314.683 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 139707) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 139707) rss_mb | MB | 4 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [bell_0000] (PID 139707) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 139709) rss_mb | MB | 1 | 25.527 | 25.527 | 25.527 | 25.527 | n/a | n/a |
| docker (PID 139709) vms_mb | MB | 1 | 1596.211 | 1596.211 | 1596.211 | 1596.211 | n/a | n/a |
| docker (PID 139771) rss_mb | MB | 1 | 6.219 | 6.219 | 6.219 | 6.219 | n/a | n/a |
| docker (PID 139771) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 139780) rss_mb | MB | 1 | 27.727 | 27.727 | 27.727 | 27.727 | n/a | n/a |
| docker (PID 139780) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| sh [bell_0000] (PID 139799) rss_mb | MB | 1 | 1.422 | 1.422 | 1.422 | 1.422 | n/a | n/a |
| sh [bell_0000] (PID 139799) vms_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| docker (PID 139815) rss_mb | MB | 1 | 25.984 | 25.984 | 25.984 | 25.984 | n/a | n/a |
| docker (PID 139815) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 139854) rss_mb | MB | 1 | 15.562 | 15.562 | 15.562 | 15.562 | n/a | n/a |
| docker (PID 139854) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 139873) rss_mb | MB | 1 | 26.828 | 26.828 | 26.828 | 26.828 | n/a | n/a |
| docker (PID 139873) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 139932) rss_mb | MB | 1 | 26.949 | 26.949 | 26.949 | 26.949 | n/a | n/a |
| docker (PID 139932) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [beef_0000] (PID 139973) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beef_0000] (PID 139973) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [beef_0000] (PID 139973) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 139985) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 139985) rss_mb | MB | 3 | 1.809 | 1.809 | 1.809 | 1.809 | n/a | n/a |
| tail [beef_0000] (PID 139985) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 140023) rss_mb | MB | 1 | 22.508 | 22.508 | 22.508 | 22.508 | n/a | n/a |
| docker (PID 140023) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 140059) rss_mb | MB | 1 | 27.402 | 27.402 | 27.402 | 27.402 | n/a | n/a |
| docker (PID 140059) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 140078) rss_mb | MB | 1 | 9.480 | 9.480 | 9.480 | 9.480 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 140078) vms_mb | MB | 1 | 1569.195 | 1569.195 | 1569.195 | 1569.195 | n/a | n/a |
| docker (PID 140094) rss_mb | MB | 1 | 26.043 | 26.043 | 26.043 | 26.043 | n/a | n/a |
| docker (PID 140094) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 140179) CPU | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 140179) io read MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 140179) io write MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 140179) rss_mb | MB | 40 | 26.664 | 26.664 | 26.664 | 26.664 | n/a | n/a |
| docker (PID 140179) vms_mb | MB | 40 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 140204) rss_mb | MB | 1 | 0.129 | 0.129 | 0.129 | 0.129 | n/a | n/a |
| docker (PID 140204) vms_mb | MB | 1 | 30.570 | 30.570 | 30.570 | 30.570 | n/a | n/a |
| docker (PID 140220) rss_mb | MB | 1 | 23.387 | 23.387 | 23.387 | 23.387 | n/a | n/a |
| docker (PID 140220) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| python3 (PID 140227) CPU | percent | 3 | 101.815 | 98.346 | 108.189 | 98.346 | 0.310000 CPU seconds | n/a |
| python3 (PID 140227) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 140227) io write MB/s | MB/s | 3 | 0.832 | 0.000 | 2.497 | 2.497 | 0.253906 MB | n/a |
| python3 (PID 140227) rss_mb | MB | 4 | 28.144 | 17.633 | 34.742 | 34.742 | n/a | n/a |
| python3 (PID 140227) vms_mb | MB | 4 | 51.767 | 42.434 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 140229) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 140229) vms_mb | MB | 1 | 0.129 | 0.129 | 0.129 | 0.129 | n/a | n/a |
| docker (PID 140254) rss_mb | MB | 1 | 25.469 | 25.469 | 25.469 | 25.469 | n/a | n/a |
| docker (PID 140254) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 140292) CPU | percent | 37 | 0.265 | 0.000 | 9.819 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 140292) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 140292) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 140292) rss_mb | MB | 38 | 26.373 | 4.469 | 26.965 | 26.965 | n/a | n/a |
| docker (PID 140292) vms_mb | MB | 38 | 1617.931 | 32.762 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 140308) rss_mb | MB | 1 | 26.594 | 26.594 | 26.594 | 26.594 | n/a | n/a |
| docker (PID 140308) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 140335) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 140335) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 140335) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 140335) rss_mb | MB | 2 | 25.293 | 25.293 | 25.293 | 25.293 | n/a | n/a |
| docker (PID 140335) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bell_0000] (PID 140376) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bell_0000] (PID 140376) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bell_0000] (PID 140376) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 140388) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 140388) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [bell_0000] (PID 140388) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 140428) rss_mb | MB | 1 | 16.238 | 16.238 | 16.238 | 16.238 | n/a | n/a |
| docker (PID 140428) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 140465) rss_mb | MB | 1 | 27.543 | 27.543 | 27.543 | 27.543 | n/a | n/a |
| docker (PID 140465) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 140504) rss_mb | MB | 1 | 26.043 | 26.043 | 26.043 | 26.043 | n/a | n/a |
| docker (PID 140504) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 140546) rss_mb | MB | 1 | 25.816 | 25.816 | 25.816 | 25.816 | n/a | n/a |
| docker (PID 140546) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 140563) rss_mb | MB | 1 | 25.457 | 25.457 | 25.457 | 25.457 | n/a | n/a |
| docker (PID 140563) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bell_0000] (PID 140603) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bell_0000] (PID 140603) rss_mb | MB | 10 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bell_0000] (PID 140603) vms_mb | MB | 10 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 140614) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 140614) rss_mb | MB | 10 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bell_0000] (PID 140614) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 140618) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 140618) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 140652) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 140652) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 140652) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 140652) rss_mb | MB | 9 | 27.598 | 27.598 | 27.598 | 27.598 | n/a | n/a |
| docker (PID 140652) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 140672) CPU | percent | 8 | 2.417 | 0.000 | 19.339 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bell_0000] (PID 140672) rss_mb | MB | 9 | 4.031 | 3.215 | 10.562 | 3.215 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 140672) vms_mb | MB | 9 | 178.286 | 4.391 | 1569.445 | 4.391 | n/a | n/a |
| python [bell_0000] (PID 140681) CPU | percent | 7 | 99.359 | 88.268 | 107.829 | 98.031 | 0.710000 CPU seconds | n/a |
| python [bell_0000] (PID 140681) rss_mb | MB | 8 | 33.029 | 15.988 | 42.582 | 42.582 | n/a | n/a |
| python [bell_0000] (PID 140681) vms_mb | MB | 8 | 40.125 | 19.738 | 52.238 | 52.238 | n/a | n/a |
| docker (PID 140691) rss_mb | MB | 1 | 27.074 | 27.074 | 27.074 | 27.074 | n/a | n/a |
| docker (PID 140691) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 140778) rss_mb | MB | 1 | 25.977 | 25.977 | 25.977 | 25.977 | n/a | n/a |
| docker (PID 140778) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 140787) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 140787) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 140787) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 140787) rss_mb | MB | 38 | 26.605 | 26.605 | 26.605 | 26.605 | n/a | n/a |
| docker (PID 140787) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 140804) rss_mb | MB | 1 | 6.406 | 6.406 | 6.406 | 6.406 | n/a | n/a |
| docker (PID 140804) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| run23:repair_bu (PID 140830) rss_mb | MB | 1 | 706.172 | 706.172 | 706.172 | 706.172 | n/a | n/a |
| run23:repair_bu (PID 140830) vms_mb | MB | 1 | 4032.445 | 4032.445 | 4032.445 | 4032.445 | n/a | n/a |
| python3 (PID 140837) CPU | percent | 3 | 98.679 | 98.363 | 98.912 | 98.912 | 0.300000 CPU seconds | n/a |
| python3 (PID 140837) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 140837) io write MB/s | MB/s | 3 | 0.837 | 0.000 | 2.511 | 2.511 | 0.253906 MB | n/a |
| python3 (PID 140837) rss_mb | MB | 4 | 28.044 | 17.367 | 34.598 | 34.598 | n/a | n/a |
| python3 (PID 140837) vms_mb | MB | 4 | 51.786 | 42.305 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 140839) rss_mb | MB | 1 | 16.395 | 16.395 | 16.395 | 16.395 | n/a | n/a |
| docker (PID 140839) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 140864) rss_mb | MB | 1 | 25.656 | 25.656 | 25.656 | 25.656 | n/a | n/a |
| docker (PID 140864) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| sandbox alex_0000 CPU | percent | 27 | 57.352 | 0.000 | 101.807 | 38.722 | 1.611802 CPU seconds | n/a |
| sandbox alex_0000 io read MB/s | MB/s | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox alex_0000 io write MB/s | MB/s | 30 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox alex_0000 memory | MB | 32 | 9.393 | 0.680 | 35.281 | 0.758 | n/a | n/a |
| sandbox alex_0000 net rx MB/s | MB/s | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox alex_0000 net tx MB/s | MB/s | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox andy_0000 CPU | percent | 29 | 53.935 | 4.012 | 100.154 | 46.791 | 1.629851 CPU seconds | n/a |
| sandbox andy_0000 io read MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox andy_0000 io write MB/s | MB/s | 32 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox andy_0000 memory | MB | 34 | 9.092 | 0.715 | 36.281 | 4.348 | n/a | n/a |
| sandbox andy_0000 net rx MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox andy_0000 net tx MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox arch_0000 CPU | percent | 20 | 58.737 | 2.985 | 100.295 | 39.195 | 1.207612 CPU seconds | n/a |
| sandbox arch_0000 io read MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox arch_0000 io write MB/s | MB/s | 23 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox arch_0000 memory | MB | 25 | 9.117 | 0.699 | 36.211 | 1.082 | n/a | n/a |
| sandbox arch_0000 net rx MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox arch_0000 net tx MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bake_0000 CPU | percent | 32 | 59.225 | 3.060 | 118.189 | 46.300 | 1.993606 CPU seconds | n/a |
| sandbox bake_0000 io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bake_0000 io write MB/s | MB/s | 36 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bake_0000 memory | MB | 38 | 10.190 | 0.000 | 34.648 | 1.090 | n/a | n/a |
| sandbox bake_0000 net rx MB/s | MB/s | 35 | 72.309 | 0.000 | 1943.556 | 0.000 | 7123.655673 MB | n/a |
| sandbox bake_0000 net tx MB/s | MB/s | 35 | 0.765 | 0.000 | 20.572 | 0.000 | 75.223331 MB | n/a |
| sandbox bale_0000 CPU | percent | 45 | 85.331 | 14.642 | 100.978 | 30.285 | 3.919762 CPU seconds | n/a |
| sandbox bale_0000 io read MB/s | MB/s | 49 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bale_0000 io write MB/s | MB/s | 48 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bale_0000 memory | MB | 50 | 23.667 | 0.707 | 35.156 | 0.707 | n/a | n/a |
| sandbox bale_0000 net rx MB/s | MB/s | 49 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bale_0000 net tx MB/s | MB/s | 49 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox band_0000 CPU | percent | 26 | 55.838 | 0.000 | 100.777 | 32.232 | 1.489792 CPU seconds | n/a |
| sandbox band_0000 io read MB/s | MB/s | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox band_0000 io write MB/s | MB/s | 30 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox band_0000 memory | MB | 32 | 7.746 | 0.699 | 35.586 | 0.801 | n/a | n/a |
| sandbox band_0000 net rx MB/s | MB/s | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox band_0000 net tx MB/s | MB/s | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bart_0000 CPU | percent | 21 | 61.484 | 11.079 | 100.072 | 45.103 | 1.323828 CPU seconds | n/a |
| sandbox bart_0000 io read MB/s | MB/s | 25 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bart_0000 io write MB/s | MB/s | 24 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bart_0000 memory | MB | 26 | 9.468 | 0.590 | 34.594 | 3.863 | n/a | n/a |
| sandbox bart_0000 net rx MB/s | MB/s | 25 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bart_0000 net tx MB/s | MB/s | 25 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox base_0000 CPU | percent | 33 | 57.627 | 3.202 | 100.308 | 36.044 | 1.960461 CPU seconds | n/a |
| sandbox base_0000 io read MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox base_0000 io write MB/s | MB/s | 37 | 0.002 | 0.000 | 0.038 | 0.000 | 0.007812 MB | n/a |
| sandbox base_0000 memory | MB | 40 | 8.419 | 0.695 | 35.184 | 4.234 | n/a | n/a |
| sandbox base_0000 net rx MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox base_0000 net tx MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beam_0000 CPU | percent | 18 | 62.600 | 28.377 | 100.153 | 28.377 | 1.153394 CPU seconds | n/a |
| sandbox beam_0000 io read MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beam_0000 io write MB/s | MB/s | 21 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox beam_0000 memory | MB | 23 | 10.179 | 0.668 | 35.461 | 0.871 | n/a | n/a |
| sandbox beam_0000 net rx MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beam_0000 net tx MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bear_0000 CPU | percent | 28 | 51.834 | 11.874 | 99.994 | 61.764 | 1.498776 CPU seconds | n/a |
| sandbox bear_0000 io read MB/s | MB/s | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bear_0000 io write MB/s | MB/s | 34 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bear_0000 memory | MB | 35 | 7.289 | 0.605 | 34.289 | 3.957 | n/a | n/a |
| sandbox bear_0000 net rx MB/s | MB/s | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bear_0000 net tx MB/s | MB/s | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beef_0000 CPU | percent | 26 | 61.920 | 17.269 | 98.906 | 34.803 | 1.697515 CPU seconds | n/a |
| sandbox beef_0000 io read MB/s | MB/s | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beef_0000 io write MB/s | MB/s | 29 | 0.597 | 0.000 | 12.067 | 0.000 | 1.843750 MB | n/a |
| sandbox beef_0000 memory | MB | 31 | 12.394 | 0.613 | 36.289 | 2.902 | n/a | n/a |
| sandbox beef_0000 net rx MB/s | MB/s | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beef_0000 net tx MB/s | MB/s | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bell_0000 CPU | percent | 17 | 64.694 | 29.545 | 100.028 | 99.990 | 1.132982 CPU seconds | n/a |
| sandbox bell_0000 io read MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bell_0000 io write MB/s | MB/s | 20 | 0.002 | 0.000 | 0.038 | 0.038 | 0.003906 MB | n/a |
| sandbox bell_0000 memory | MB | 21 | 11.145 | 0.699 | 36.215 | 36.215 | n/a | n/a |
| sandbox bell_0000 net rx MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bell_0000 net tx MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| workload total CPU | percent | 4074 | 26.332 | 0.582 | 199.784 | 70.748 | 109.799030 CPU seconds | n/a |
| workload total io read MB/s | MB/s | 418 | 0.100 | 0.000 | 28.952 | 0.000 | 4.386719 MB | n/a |
| workload total io write MB/s | MB/s | 409 | 0.057 | 0.000 | 14.674 | 0.000 | 2.500000 MB | n/a |
| workload total memory | MB | 4075 | 495.179 | 395.422 | 551.711 | 502.031 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
