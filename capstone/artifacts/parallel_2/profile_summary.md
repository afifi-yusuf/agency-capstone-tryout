# agprof summary

- Duration: **309.571 s**
- Runs: **12/12 completed**, 12 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.039 runs/s**
- LLM: **41 calls**, 41 succeeded, 0 failed, 0 interrupted, 0 retries, 227.009 s total wait
- Tools: **53/53 completed**, 2 failed, 0 interrupted
- Raw resource samples: **38000** at 9.85 Hz effective (10 Hz configured)
- GPU sampling: **unavailable** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 24173.717 / 39294.430 ms |
| LLM latency p50 / p95 | 3408.518 / 22632.857 ms |
| LLM TTFT p50 / p95 | 702.628 / 1566.891 ms |
| LLM input / output tokens | 211694 / 9208 |
| LLM output throughput | 46.941 tokens/s |
| LLM attempts | 41 total, 41 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 457.131 / 1344.050 ms |

### Tool outcomes

| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 6/6 | 6 | 0 | 0 | 1380.072 ms | 3341.242 ms |
| edit | 6/6 | 6 | 0 | 0 | 566.793 ms | 708.875 ms |
| glob | 1/1 | 1 | 0 | 0 | 385.538 ms | 385.538 ms |
| read | 20/20 | 20 | 0 | 0 | 649.191 ms | 947.632 ms |
| return_plan | 6/6 | 6 | 0 | 0 | 0.371 ms | 0.404 ms |
| return_status | 6/6 | 6 | 0 | 0 | 0.310 ms | 0.586 ms |
| return_summary | 8/8 | 6 | 2 | 0 | 0.353 ms | 0.505 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 55.271% | 194.371% | 171.293 s | 460.374 MB | 523.324 MB | 1.734375 MB | 2.066406 MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python3 | 40348 |  | 3049 | 3.529% | 133.079% | 11.350 s | 670.115 MB | 694.426 MB | 3739.516 MB | 3973.430 MB | 29.285156 MB | 15.503906 MB |
| git | 40354 |  | 5 | 0.000% | 0.000% | 0.000 s | 4.707 MB | 4.707 MB | 12.516 MB | 12.516 MB | 0.000000 MB | 0.000000 MB |
| git | 40355 |  | 5 | 0.000% | 0.000% | 0.000 s | 3.512 MB | 3.512 MB | 11.273 MB | 11.273 MB | 0.000000 MB | 0.000000 MB |
| git-remote-http | 40356 |  | 5 | 14.768% | 39.383% | 0.060 s | 15.460 MB | 19.332 MB | 85.941 MB | 107.566 MB | 0.871094 MB | 0.000000 MB |
| git | 40360 |  | 1 | n/a% | n/a% | n/a s | 4.383 MB | 4.383 MB | 11.273 MB | 11.273 MB | n/a MB | n/a MB |
| python3 | 40362 |  | 1189 | 99.993% | 109.057% | 119.980 s | 34.074 MB | 34.094 MB | 56.359 MB | 56.375 MB | 0.000000 MB | 0.015625 MB |
| python3 | 40363 |  | 4 | 99.009% | 108.828% | 0.300 s | 25.030 MB | 34.695 MB | 49.276 MB | 57.500 MB | 0.000000 MB | 0.210938 MB |
| python3 | 40364 |  | 4 | 99.007% | 108.848% | 0.300 s | 29.270 MB | 36.043 MB | 52.499 MB | 58.508 MB | 0.000000 MB | 0.210938 MB |
| python3 | 40365 |  | 4 | 98.984% | 99.091% | 0.300 s | 22.988 MB | 34.094 MB | 47.879 MB | 57.504 MB | 0.000000 MB | 0.015625 MB |
| python3 | 40366 |  | 24 | 99.914% | 108.994% | 2.320 s | 33.306 MB | 34.336 MB | 55.790 MB | 57.504 MB | 0.000000 MB | 0.015625 MB |
| python3 | 40367 |  | 69 | 99.896% | 108.958% | 6.860 s | 41.615 MB | 47.414 MB | 64.629 MB | 70.637 MB | 0.000000 MB | 0.214844 MB |
| docker | 40371 |  | 1 | n/a% | n/a% | n/a s | 26.199 MB | 26.199 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 40409 |  | 1 | n/a% | n/a% | n/a s | 25.988 MB | 25.988 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 40417 |  | 1 | n/a% | n/a% | n/a s | 1.703 MB | 1.703 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 40428 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.345 MB | 27.508 MB | 1708.776 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 40449 |  | 4 | 0.000% | 0.000% | 0.000 s | 27.483 MB | 27.637 MB | 1714.776 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 40520 | alex_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.582 MB | 12.328 MB | 250.583 MB | 1498.223 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 40526 | andy_0000 | 7 | 1.611% | 9.665% | 0.010 s | 4.091 MB | 13.016 MB | 449.532 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 40565 |  | 2 | 14.645% | 14.645% | 0.020 s | 14.395 MB | 27.289 MB | 846.768 MB | 1660.773 MB | 0.035156 MB | 0.000000 MB |
| tail | 40555 | alex_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| tail | 40573 | andy_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 40584 |  | 1 | n/a% | n/a% | n/a s | 27.531 MB | 27.531 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 40602 |  | 1 | n/a% | n/a% | n/a s | 12.453 MB | 12.453 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 40647 |  | 1 | n/a% | n/a% | n/a s | 27.406 MB | 27.406 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 40649 |  | 1 | n/a% | n/a% | n/a s | 27.438 MB | 27.438 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 40693 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.992 MB | 11.992 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 40692 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.473 MB | 11.473 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 40705 |  | 1 | n/a% | n/a% | n/a s | 27.453 MB | 27.453 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 40746 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.418 MB | 11.418 MB | 1498.223 MB | 1498.223 MB | n/a MB | n/a MB |
| docker | 40707 |  | 1 | n/a% | n/a% | n/a s | 27.285 MB | 27.285 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 40744 | andy_0000 | 1 | n/a% | n/a% | n/a s | 12.004 MB | 12.004 MB | 1642.730 MB | 1642.730 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 40804 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.543 MB | 11.543 MB | 1570.098 MB | 1570.098 MB | n/a MB | n/a MB |
| docker | 40776 |  | 1 | n/a% | n/a% | n/a s | 27.266 MB | 27.266 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 40781 |  | 1 | n/a% | n/a% | n/a s | 27.527 MB | 27.527 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 40839 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.152 MB | 27.152 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 40862 |  | 3 | 9.576% | 19.152% | 0.020 s | 24.257 MB | 27.215 MB | 1612.499 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 40986 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.453 MB | 25.453 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 40995 |  | 3 | 4.887% | 9.774% | 0.010 s | 24.210 MB | 27.039 MB | 1612.499 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 41073 | alex_0000 | 6 | 3.834% | 19.168% | 0.020 s | 4.512 MB | 13.016 MB | 524.066 MB | 1570.477 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 41056 | andy_0000 | 6 | 1.917% | 9.584% | 0.010 s | 2.544 MB | 12.098 MB | 262.583 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 41097 | andy_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 41106 |  | 1 | n/a% | n/a% | n/a s | 9.574 MB | 9.574 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 41123 | alex_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 41121 |  | 1 | n/a% | n/a% | n/a s | 26.836 MB | 26.836 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 41159 |  | 1 | n/a% | n/a% | n/a s | 15.613 MB | 15.613 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 41150 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.676 MB | 11.676 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 41181 |  | 1 | n/a% | n/a% | n/a s | 27.199 MB | 27.199 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 41207 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.941 MB | 11.941 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 41214 |  | 1 | n/a% | n/a% | n/a s | 25.086 MB | 25.086 MB | 1659.961 MB | 1659.961 MB | n/a MB | n/a MB |
| docker | 41259 |  | 1 | n/a% | n/a% | n/a s | 24.047 MB | 24.047 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 41251 |  | 1 | n/a% | n/a% | n/a s | 26.688 MB | 26.688 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 41278 | andy_0000 | 1 | n/a% | n/a% | n/a s | 10.715 MB | 10.715 MB | 1569.695 MB | 1569.695 MB | n/a MB | n/a MB |
| docker | 41323 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.902 MB | 25.902 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 41353 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.078 MB | 26.078 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 41468 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.914 MB | 25.914 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 41508 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 4.734 MB | 12.938 MB | 524.112 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 41543 |  | 1 | n/a% | n/a% | n/a s | 26.801 MB | 26.801 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 41561 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.480 MB | 11.480 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 41530 | alex_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 41588 | alex_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| docker | 41568 |  | 1 | n/a% | n/a% | n/a s | 27.152 MB | 27.152 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 41611 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.977 MB | 25.977 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 41685 |  | 2 | 9.866% | 9.866% | 0.010 s | 18.102 MB | 27.102 MB | 1484.232 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 41723 | alex_0000 | 4 | 6.532% | 19.597% | 0.020 s | 3.634 MB | 12.637 MB | 393.473 MB | 1570.727 MB | n/a MB | n/a MB |
| tail | 41749 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 41751 |  | 1 | n/a% | n/a% | n/a s | 27.023 MB | 27.023 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[1:CHILD] | 41803 | alex_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 41801 | alex_0000 | 1 | n/a% | n/a% | n/a s | 1.996 MB | 1.996 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 41785 |  | 1 | n/a% | n/a% | n/a s | 27.449 MB | 27.449 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 41821 |  | 1 | n/a% | n/a% | n/a s | 27.316 MB | 27.316 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 41843 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.898 MB | 11.898 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 41859 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.320 MB | 26.320 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 41923 |  | 1 | n/a% | n/a% | n/a s | 14.875 MB | 14.875 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 41970 | andy_0000 | 4 | 9.795% | 29.384% | 0.030 s | 3.370 MB | 11.582 MB | 393.249 MB | 1569.832 MB | n/a MB | n/a MB |
| docker | 41931 |  | 1 | n/a% | n/a% | n/a s | 25.566 MB | 25.566 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 41994 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 42034 |  | 1 | n/a% | n/a% | n/a s | 25.562 MB | 25.562 MB | 1587.957 MB | 1587.957 MB | n/a MB | n/a MB |
| docker | 42070 |  | 1 | n/a% | n/a% | n/a s | 27.430 MB | 27.430 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 42086 | andy_0000 | 1 | n/a% | n/a% | n/a s | 1.969 MB | 1.969 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 42107 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.852 MB | 26.852 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 42205 |  | 38 | 0.000% | 0.000% | 0.000 s | 25.682 MB | 25.730 MB | 1658.316 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 42221 |  | 1 | n/a% | n/a% | n/a s | 19.055 MB | 19.055 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 42240 |  | 1 | n/a% | n/a% | n/a s | 23.008 MB | 23.008 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 42288 | andy_0000 | 4 | 6.535% | 19.604% | 0.020 s | 3.394 MB | 11.676 MB | 393.281 MB | 1569.961 MB | n/a MB | n/a MB |
| docker | 42248 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.621 MB | 25.621 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| tail | 42314 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 42353 |  | 1 | n/a% | n/a% | n/a s | 16.309 MB | 16.309 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 42389 |  | 1 | n/a% | n/a% | n/a s | 27.520 MB | 27.520 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 42428 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.109 MB | 27.109 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 42503 |  | 2 | 0.000% | 0.000% | 0.000 s | 24.393 MB | 26.738 MB | 1588.486 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 42543 | andy_0000 | 11 | 0.861% | 8.605% | 0.010 s | 1.737 MB | 12.777 MB | 143.707 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 42578 |  | 1 | n/a% | n/a% | n/a s | 26.715 MB | 26.715 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 42566 | andy_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 42626 | andy_0000 | 9 | 2.447% | 19.577% | 0.020 s | 4.283 MB | 11.672 MB | 178.414 MB | 1570.598 MB | n/a MB | n/a MB |
| docker | 42606 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.178 MB | 27.289 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 42635 | andy_0000 | 8 | 100.775% | 107.858% | 0.720 s | 32.959 MB | 42.469 MB | 40.277 MB | 52.238 MB | n/a MB | n/a MB |
| docker | 42645 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.129 MB | 27.129 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 42718 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.336 MB | 27.336 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 42758 | andy_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.681 MB | 12.824 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 42792 |  | 1 | n/a% | n/a% | n/a s | 27.488 MB | 27.488 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 42782 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.809 MB | 1.809 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 42823 |  | 1 | n/a% | n/a% | n/a s | 26.961 MB | 26.961 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 42886 |  | 1 | n/a% | n/a% | n/a s | 20.148 MB | 20.148 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 42894 |  | 1 | n/a% | n/a% | n/a s | 26.055 MB | 26.055 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 42952 |  | 1 | n/a% | n/a% | n/a s | 17.109 MB | 17.109 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 42992 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.352 MB | 25.352 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 43005 |  | 1 | n/a% | n/a% | n/a s | 25.711 MB | 25.711 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 43035 |  | 1 | n/a% | n/a% | n/a s | 26.715 MB | 26.715 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 43060 |  | 1 | n/a% | n/a% | n/a s | 11.168 MB | 11.168 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 43045 |  | 43 | 0.000% | 0.000% | 0.000 s | 26.938 MB | 26.938 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 43079 |  | 3 | 0.000% | 0.000% | 0.000 s | 25.387 MB | 25.387 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 43117 | alex_0000 | 6 | 7.843% | 39.215% | 0.040 s | 4.498 MB | 13.016 MB | 524.045 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 43161 |  | 1 | n/a% | n/a% | n/a s | 27.316 MB | 27.316 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 43149 | alex_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 43187 |  | 1 | n/a% | n/a% | n/a s | 27.094 MB | 27.094 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 43221 |  | 1 | n/a% | n/a% | n/a s | 18.078 MB | 18.078 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 43251 |  | 1 | n/a% | n/a% | n/a s | 18.859 MB | 18.859 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 43260 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.004 MB | 26.004 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 43336 |  | 1 | n/a% | n/a% | n/a s | 8.730 MB | 8.730 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| run2:repair_bug | 43361 |  | 1 | n/a% | n/a% | n/a s | 679.926 MB | 679.926 MB | 3968.688 MB | 3968.688 MB | n/a MB | n/a MB |
| python3 | 43369 |  | 4 | 98.843% | 98.946% | 0.300 s | 28.187 MB | 34.512 MB | 51.832 MB | 57.438 MB | 0.062500 MB | 0.199219 MB |
| docker | 43379 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.004 MB | 27.004 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| 6 | 43416 | alex_0000 | 1 | n/a% | n/a% | n/a s | 1.789 MB | 1.789 MB | 13.980 MB | 13.980 MB | n/a MB | n/a MB |
| docker-init | 43420 | alex_0000 | 11 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 43481 |  | 9 | 2.438% | 9.804% | 0.020 s | 24.349 MB | 27.348 MB | 1479.883 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| tail | 43444 | alex_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| python | 43510 | alex_0000 | 8 | 100.864% | 107.845% | 0.720 s | 30.730 MB | 41.852 MB | 37.888 MB | 51.238 MB | n/a MB | n/a MB |
| bash | 43501 | alex_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.395 MB | 3.395 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 43520 |  | 2 | 9.808% | 9.808% | 0.010 s | 13.986 MB | 26.316 MB | 846.486 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 43577 |  | 1 | n/a% | n/a% | n/a s | 22.441 MB | 22.441 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 43594 |  | 5 | 0.000% | 0.000% | 0.000 s | 26.531 MB | 26.531 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 43636 | alex_0000 | 7 | 17.286% | 86.434% | 0.110 s | 5.694 MB | 12.922 MB | 673.554 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 43658 | alex_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 43670 |  | 1 | n/a% | n/a% | n/a s | 4.586 MB | 4.586 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 43696 |  | 1 | n/a% | n/a% | n/a s | 25.336 MB | 25.336 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 43732 |  | 1 | n/a% | n/a% | n/a s | 26.648 MB | 26.648 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 43771 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.883 MB | 26.883 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 43844 |  | 1 | n/a% | n/a% | n/a s | 25.902 MB | 25.902 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 43868 |  | 39 | 0.000% | 0.000% | 0.000 s | 26.559 MB | 26.559 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 43893 |  | 1 | n/a% | n/a% | n/a s | 9.242 MB | 9.242 MB | 1243.691 MB | 1243.691 MB | n/a MB | n/a MB |
| python3 | 43916 |  | 4 | 98.802% | 108.750% | 0.300 s | 24.135 MB | 34.277 MB | 48.325 MB | 57.453 MB | 0.000000 MB | 0.183594 MB |
| docker | 43926 |  | 1 | n/a% | n/a% | n/a s | 24.172 MB | 24.172 MB | 1596.211 MB | 1596.211 MB | n/a MB | n/a MB |
| docker | 43969 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 44003 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.456 MB | 27.680 MB | 1756.779 MB | 1804.781 MB | 0.000000 MB | 0.000000 MB |
| docker | 44043 |  | 1 | n/a% | n/a% | n/a s | 23.906 MB | 23.906 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 44050 | arch_0000 | 7 | 6.339% | 38.035% | 0.040 s | 3.680 MB | 13.086 MB | 449.278 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 44066 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.146 MB | 27.375 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| tail | 44090 | arch_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 44119 |  | 1 | n/a% | n/a% | n/a s | 11.574 MB | 11.574 MB | 1570.219 MB | 1570.219 MB | n/a MB | n/a MB |
| docker | 44095 |  | 1 | n/a% | n/a% | n/a s | 27.559 MB | 27.559 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 44157 | bake_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.384 MB | 12.895 MB | 235.544 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 44171 |  | 1 | n/a% | n/a% | n/a s | 27.379 MB | 27.379 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 44222 |  | 1 | n/a% | n/a% | n/a s | 3.324 MB | 3.324 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| tail | 44212 | bake_0000 | 6 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 44216 |  | 1 | n/a% | n/a% | n/a s | 20.234 MB | 20.234 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 44277 |  | 1 | n/a% | n/a% | n/a s | 4.469 MB | 4.469 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 44269 |  | 1 | n/a% | n/a% | n/a s | 19.223 MB | 19.223 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 44331 | arch_0000 | 1 | n/a% | n/a% | n/a s | 12.336 MB | 12.336 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 44314 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.977 MB | 11.977 MB | 1498.223 MB | 1498.223 MB | n/a MB | n/a MB |
| docker | 44286 |  | 1 | n/a% | n/a% | n/a s | 26.965 MB | 26.965 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 44288 |  | 1 | n/a% | n/a% | n/a s | 27.215 MB | 27.215 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 44363 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.047 MB | 26.047 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 44410 |  | 1 | n/a% | n/a% | n/a s | 27.699 MB | 27.699 MB | 1733.027 MB | 1733.027 MB | n/a MB | n/a MB |
| docker | 44488 |  | 1 | n/a% | n/a% | n/a s | 0.559 MB | 0.559 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 44481 |  | 4 | 3.168% | 9.504% | 0.010 s | 23.729 MB | 25.473 MB | 1624.146 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 44499 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.773 MB | 26.773 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 44558 | arch_0000 | 6 | 1.912% | 9.559% | 0.010 s | 2.643 MB | 12.695 MB | 250.583 MB | 1498.223 MB | n/a MB | n/a MB |
| docker | 44599 |  | 1 | n/a% | n/a% | n/a s | 26.465 MB | 26.465 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| tail | 44617 | arch_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 44668 | arch_0000 | 1 | n/a% | n/a% | n/a s | 12.043 MB | 12.043 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 44642 |  | 1 | n/a% | n/a% | n/a s | 27.492 MB | 27.492 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 44640 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.113 MB | 27.113 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 44706 | bake_0000 | 5 | 2.430% | 9.721% | 0.010 s | 3.084 MB | 12.887 MB | 314.939 MB | 1570.477 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 44733 | arch_0000 | 1 | n/a% | n/a% | n/a s | 10.723 MB | 10.723 MB | 1641.699 MB | 1641.699 MB | n/a MB | n/a MB |
| docker | 44713 |  | 1 | n/a% | n/a% | n/a s | 27.117 MB | 27.117 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 44776 |  | 1 | n/a% | n/a% | n/a s | 9.277 MB | 9.277 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| tail | 44755 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 44774 |  | 1 | n/a% | n/a% | n/a s | 18.086 MB | 18.086 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 44834 |  | 1 | n/a% | n/a% | n/a s | 10.547 MB | 10.547 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 44828 |  | 1 | n/a% | n/a% | n/a s | 19.684 MB | 19.684 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 44845 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.074 MB | 27.074 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 44883 |  | 1 | n/a% | n/a% | n/a s | 20.238 MB | 20.238 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 44911 |  | 1 | n/a% | n/a% | n/a s | 27.527 MB | 27.527 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 44945 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.523 MB | 11.523 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 44972 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.859 MB | 26.859 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 45050 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.844 MB | 26.844 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 45090 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.712 MB | 12.949 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 45118 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.785 MB | 1.785 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 45128 |  | 1 | n/a% | n/a% | n/a s | 27.367 MB | 27.367 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 45145 | bake_0000 | 1 | n/a% | n/a% | n/a s | 10.762 MB | 10.762 MB | 1569.711 MB | 1569.711 MB | n/a MB | n/a MB |
| docker | 45179 |  | 1 | n/a% | n/a% | n/a s | 5.402 MB | 5.402 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 45217 |  | 1 | n/a% | n/a% | n/a s | 26.469 MB | 26.469 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 45225 |  | 1 | n/a% | n/a% | n/a s | 25.965 MB | 25.965 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 45308 |  | 1 | n/a% | n/a% | n/a s | 27.000 MB | 27.000 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 45322 |  | 44 | 0.000% | 0.000% | 0.000 s | 25.828 MB | 25.828 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 45338 |  | 1 | n/a% | n/a% | n/a s | 19.223 MB | 19.223 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 45361 |  | 44 | 0.000% | 0.000% | 0.000 s | 26.941 MB | 26.941 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 45377 |  | 1 | n/a% | n/a% | n/a s | 25.965 MB | 25.965 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 45403 |  | 1 | n/a% | n/a% | n/a s | 26.965 MB | 26.965 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 45429 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.535 MB | 26.535 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 45468 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.711 MB | 12.945 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 45508 |  | 1 | n/a% | n/a% | n/a s | 27.586 MB | 27.586 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 45494 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 45534 |  | 1 | n/a% | n/a% | n/a s | 26.941 MB | 26.941 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| sh | 45554 | bake_0000 | 1 | n/a% | n/a% | n/a s | 1.641 MB | 1.641 MB | 2.617 MB | 2.617 MB | n/a MB | n/a MB |
| docker | 45601 |  | 1 | n/a% | n/a% | n/a s | 6.516 MB | 6.516 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 45609 |  | 1 | n/a% | n/a% | n/a s | 25.879 MB | 25.879 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 45675 |  | 1 | n/a% | n/a% | n/a s | 17.707 MB | 17.707 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 45684 |  | 1 | n/a% | n/a% | n/a s | 25.680 MB | 25.680 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 45730 |  | 1 | n/a% | n/a% | n/a s | 4.473 MB | 4.473 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 45723 | bake_0000 | 14 | 1.915% | 24.895% | 0.030 s | 1.366 MB | 10.891 MB | 113.065 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 45738 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.383 MB | 25.383 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| tail | 45764 | bake_0000 | 13 | 0.000% | 0.000% | 0.000 s | 1.695 MB | 1.695 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 45815 | arch_0000 | 5 | 2.290% | 9.162% | 0.010 s | 3.109 MB | 13.016 MB | 329.340 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 45802 |  | 1 | n/a% | n/a% | n/a s | 27.246 MB | 27.246 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 45834 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.699 MB | 11.699 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 45861 | arch_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 45850 |  | 11 | 0.000% | 0.000% | 0.000 s | 27.355 MB | 27.355 MB | 1661.023 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| docker | 45891 |  | 1 | n/a% | n/a% | n/a s | 27.469 MB | 27.469 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| bash | 45882 | bake_0000 | 10 | 0.000% | 0.000% | 0.000 s | 3.406 MB | 3.406 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 45914 | arch_0000 | 1 | n/a% | n/a% | n/a s | 11.781 MB | 11.781 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| python | 45901 | bake_0000 | 10 | 92.726% | 110.354% | 0.890 s | 29.916 MB | 41.805 MB | 36.659 MB | 51.375 MB | n/a MB | n/a MB |
| sh | 45943 | arch_0000 | 1 | n/a% | n/a% | n/a s | 1.641 MB | 1.641 MB | 2.617 MB | 2.617 MB | n/a MB | n/a MB |
| docker | 45921 |  | 1 | n/a% | n/a% | n/a s | 27.289 MB | 27.289 MB | 1733.027 MB | 1733.027 MB | n/a MB | n/a MB |
| docker | 45959 |  | 1 | n/a% | n/a% | n/a s | 27.656 MB | 27.656 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| sh | 45980 | arch_0000 | 1 | n/a% | n/a% | n/a s | 1.656 MB | 1.656 MB | 2.617 MB | 2.617 MB | n/a MB | n/a MB |
| docker | 45998 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.098 MB | 27.098 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 46076 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.098 MB | 26.098 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 46150 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.000 MB | 27.000 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 46189 | arch_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.470 MB | 13.188 MB | 110.500 MB | 1642.730 MB | n/a MB | n/a MB |
| docker | 46224 |  | 1 | n/a% | n/a% | n/a s | 27.078 MB | 27.078 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 46212 | arch_0000 | 14 | 0.000% | 0.000% | 0.000 s | 1.777 MB | 1.777 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| python | 46279 | arch_0000 | 12 | 87.837% | 104.473% | 1.030 s | 31.286 MB | 42.527 MB | 38.944 MB | 52.219 MB | n/a MB | n/a MB |
| docker | 46250 |  | 12 | 0.000% | 0.000% | 0.000 s | 27.382 MB | 27.496 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| bash | 46270 | arch_0000 | 12 | 0.000% | 0.000% | 0.000 s | 3.418 MB | 3.418 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 46290 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.379 MB | 25.379 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 46328 | bake_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.072 MB | 12.828 MB | 314.889 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 46361 |  | 1 | n/a% | n/a% | n/a s | 3.844 MB | 3.844 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| tail | 46350 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 46388 |  | 1 | n/a% | n/a% | n/a s | 16.062 MB | 16.062 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 46422 |  | 1 | n/a% | n/a% | n/a s | 15.566 MB | 15.566 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 46459 |  | 1 | n/a% | n/a% | n/a s | 25.984 MB | 25.984 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 46515 |  | 1 | n/a% | n/a% | n/a s | 13.508 MB | 13.508 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 46533 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.047 MB | 26.047 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 46599 |  | 1 | n/a% | n/a% | n/a s | 4.219 MB | 4.219 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 46649 | arch_0000 | 4 | 9.858% | 29.573% | 0.030 s | 3.313 MB | 11.355 MB | 393.215 MB | 1569.695 MB | n/a MB | n/a MB |
| docker | 46609 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.930 MB | 26.930 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| tail | 46674 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.586 MB | 1.586 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 46712 |  | 1 | n/a% | n/a% | n/a s | 10.297 MB | 10.297 MB | 1323.949 MB | 1323.949 MB | n/a MB | n/a MB |
| docker | 46747 |  | 1 | n/a% | n/a% | n/a s | 27.328 MB | 27.328 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 46783 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.102 MB | 27.102 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 46858 |  | 1 | n/a% | n/a% | n/a s | 23.695 MB | 23.695 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 46884 |  | 1 | n/a% | n/a% | n/a s | 0.410 MB | 0.410 MB | 30.570 MB | 30.570 MB | n/a MB | n/a MB |
| docker | 46900 |  | 56 | 0.000% | 0.000% | 0.000 s | 27.195 MB | 27.195 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 46908 |  | 1 | n/a% | n/a% | n/a s | 8.148 MB | 8.148 MB | 32.867 MB | 32.867 MB | n/a MB | n/a MB |
| docker | 46924 |  | 1 | n/a% | n/a% | n/a s | 25.961 MB | 25.961 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 46932 |  | 55 | 0.000% | 0.000% | 0.000 s | 26.680 MB | 26.680 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 46948 |  | 1 | n/a% | n/a% | n/a s | 14.332 MB | 14.332 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 46972 |  | 1 | n/a% | n/a% | n/a s | 25.387 MB | 25.387 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| python3 | 46993 |  | 9 | 68.549% | 107.840% | 0.560 s | 24.304 MB | 34.141 MB | 48.717 MB | 57.438 MB | 4.296875 MB | 0.199219 MB |
| docker | 46998 |  | 1 | n/a% | n/a% | n/a s | 26.754 MB | 26.754 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 47021 |  | 7 | 71.826% | 98.036% | 0.440 s | 27.768 MB | 34.082 MB | 51.605 MB | 57.453 MB | 1.753906 MB | 0.199219 MB |
| docker | 47039 |  | 1 | n/a% | n/a% | n/a s | 14.504 MB | 14.504 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 47083 |  | 1 | n/a% | n/a% | n/a s | 15.305 MB | 15.305 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 47109 |  | 4 | 3.260% | 9.779% | 0.010 s | 27.171 MB | 27.324 MB | 1714.776 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 47150 | band_0000 | 6 | 7.724% | 38.621% | 0.040 s | 4.464 MB | 13.059 MB | 524.023 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 47178 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.555 MB | 1.555 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 47199 |  | 1 | n/a% | n/a% | n/a s | 12.617 MB | 12.617 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 47180 |  | 1 | n/a% | n/a% | n/a s | 26.957 MB | 26.957 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 47243 |  | 1 | n/a% | n/a% | n/a s | 1.188 MB | 1.188 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 47280 |  | 1 | n/a% | n/a% | n/a s | 26.289 MB | 26.289 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 47315 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.922 MB | 26.922 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 47378 |  | 1 | n/a% | n/a% | n/a s | 26.250 MB | 26.250 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 47386 |  | 1 | n/a% | n/a% | n/a s | 25.699 MB | 25.699 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 47427 | band_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.564 MB | 12.219 MB | 262.583 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 47450 | band_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.688 MB | 1.688 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 47452 |  | 1 | n/a% | n/a% | n/a s | 26.664 MB | 26.664 MB | 1596.523 MB | 1596.523 MB | n/a MB | n/a MB |
| docker | 47504 |  | 4 | 6.370% | 19.111% | 0.020 s | 21.871 MB | 27.211 MB | 1289.772 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 47505 |  | 1 | n/a% | n/a% | n/a s | 8.844 MB | 8.844 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 47602 | band_0000 | 1 | n/a% | n/a% | n/a s | 11.688 MB | 11.688 MB | 1642.223 MB | 1642.223 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 47585 | bale_0000 | 6 | 5.753% | 28.765% | 0.030 s | 4.507 MB | 13.109 MB | 524.023 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 47557 |  | 1 | n/a% | n/a% | n/a s | 27.379 MB | 27.379 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 47617 |  | 1 | n/a% | n/a% | n/a s | 26.527 MB | 26.527 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 47631 |  | 1 | n/a% | n/a% | n/a s | 26.871 MB | 26.871 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 47643 | bale_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.801 MB | 1.801 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 47652 |  | 1 | n/a% | n/a% | n/a s | 27.426 MB | 27.426 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 47725 |  | 1 | n/a% | n/a% | n/a s | 3.523 MB | 3.523 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 47713 |  | 1 | n/a% | n/a% | n/a s | 25.668 MB | 25.668 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 47762 |  | 1 | n/a% | n/a% | n/a s | 25.648 MB | 25.648 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 47797 |  | 1 | n/a% | n/a% | n/a s | 26.961 MB | 26.961 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 47833 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.031 MB | 26.031 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 47912 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.844 MB | 26.844 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 47951 | bale_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.670 MB | 12.781 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 47986 |  | 1 | n/a% | n/a% | n/a s | 27.148 MB | 27.148 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 47974 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.633 MB | 1.633 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 48076 |  | 1 | n/a% | n/a% | n/a s | 26.613 MB | 26.613 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 48084 |  | 1 | n/a% | n/a% | n/a s | 25.875 MB | 25.875 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 48182 |  | 39 | 0.000% | 0.000% | 0.000 s | 27.000 MB | 27.000 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 48232 |  | 1 | n/a% | n/a% | n/a s | 24.027 MB | 24.027 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 48246 |  | 41 | 0.000% | 0.000% | 0.000 s | 26.699 MB | 26.699 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 48254 |  | 1 | n/a% | n/a% | n/a s | 23.145 MB | 23.145 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 48262 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.715 MB | 26.715 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 48301 | bale_0000 | 6 | 1.946% | 9.732% | 0.010 s | 2.689 MB | 12.973 MB | 262.625 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 48333 |  | 1 | n/a% | n/a% | n/a s | 16.445 MB | 16.445 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| tail | 48326 | bale_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 48341 |  | 1 | n/a% | n/a% | n/a s | 27.121 MB | 27.121 MB | 1733.027 MB | 1733.027 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 48390 | bale_0000 | 1 | n/a% | n/a% | n/a s | 11.855 MB | 11.855 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 48371 |  | 1 | n/a% | n/a% | n/a s | 25.883 MB | 25.883 MB | 1659.961 MB | 1659.961 MB | n/a MB | n/a MB |
| docker | 48407 |  | 1 | n/a% | n/a% | n/a s | 27.219 MB | 27.219 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 48426 | bale_0000 | 1 | n/a% | n/a% | n/a s | 10.645 MB | 10.645 MB | 1497.320 MB | 1497.320 MB | n/a MB | n/a MB |
| docker | 48444 |  | 2 | 16.588% | 16.588% | 0.020 s | 18.037 MB | 27.184 MB | 1444.104 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 48497 |  | 1 | n/a% | n/a% | n/a s | 25.609 MB | 25.609 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 48520 |  | 1 | n/a% | n/a% | n/a s | 25.328 MB | 25.328 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 48546 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.000 MB | 27.000 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 48585 | bale_0000 | 38 | 0.000% | 0.000% | 0.000 s | 0.948 MB | 12.598 MB | 42.349 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 48620 |  | 1 | n/a% | n/a% | n/a s | 27.398 MB | 27.398 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 48610 | bale_0000 | 37 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| bash | 48667 | bale_0000 | 35 | 0.000% | 0.000% | 0.000 s | 3.257 MB | 3.262 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 48648 |  | 35 | 0.576% | 19.572% | 0.020 s | 27.105 MB | 27.105 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 48677 | bale_0000 | 34 | 99.803% | 107.976% | 3.360 s | 39.996 MB | 41.891 MB | 48.885 MB | 51.324 MB | n/a MB | n/a MB |
| docker | 48687 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.840 MB | 25.840 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 48762 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.375 MB | 25.375 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 48803 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.739 MB | 13.059 MB | 393.473 MB | 1570.727 MB | n/a MB | n/a MB |
| tail | 48826 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.668 MB | 1.668 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 48838 |  | 1 | n/a% | n/a% | n/a s | 27.285 MB | 27.285 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 48857 | band_0000 | 1 | n/a% | n/a% | n/a s | 10.707 MB | 10.707 MB | 1569.582 MB | 1569.582 MB | n/a MB | n/a MB |
| docker | 48891 |  | 1 | n/a% | n/a% | n/a s | 22.207 MB | 22.207 MB | 1523.953 MB | 1523.953 MB | n/a MB | n/a MB |
| docker | 48936 |  | 1 | n/a% | n/a% | n/a s | 18.387 MB | 18.387 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 49000 | bale_0000 | 5 | 4.639% | 18.555% | 0.020 s | 5.120 MB | 12.656 MB | 628.517 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 48953 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.789 MB | 25.789 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 48944 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.422 MB | 25.422 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 49074 |  | 1 | n/a% | n/a% | n/a s | 18.098 MB | 18.098 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 49070 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 49108 |  | 1 | n/a% | n/a% | n/a s | 27.469 MB | 27.469 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 49143 |  | 1 | n/a% | n/a% | n/a s | 26.988 MB | 26.988 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 49164 | bale_0000 | 1 | n/a% | n/a% | n/a s | 11.375 MB | 11.375 MB | 1569.969 MB | 1569.969 MB | n/a MB | n/a MB |
| docker | 49180 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.965 MB | 25.965 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 49254 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.801 MB | 25.801 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 49292 | band_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.737 MB | 12.781 MB | 143.707 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 49320 | band_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 49352 | band_0000 | 1 | n/a% | n/a% | n/a s | 11.770 MB | 11.770 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 49331 |  | 1 | n/a% | n/a% | n/a s | 26.980 MB | 26.980 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| bash | 49379 | band_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.270 MB | 3.270 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 49359 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.316 MB | 27.316 MB | 1661.023 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| python | 49388 | band_0000 | 8 | 100.633% | 107.930% | 0.720 s | 30.378 MB | 41.031 MB | 37.663 MB | 51.324 MB | n/a MB | n/a MB |
| docker | 49390 |  | 1 | n/a% | n/a% | n/a s | 19.934 MB | 19.934 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 49398 |  | 1 | n/a% | n/a% | n/a s | 26.953 MB | 26.953 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 49452 |  | 1 | n/a% | n/a% | n/a s | 0.559 MB | 0.559 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 49461 |  | 1 | n/a% | n/a% | n/a s | 18.184 MB | 18.184 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 49485 |  | 1 | n/a% | n/a% | n/a s | 25.152 MB | 25.152 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 49493 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.301 MB | 25.301 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 49526 |  | 1 | n/a% | n/a% | n/a s | 25.484 MB | 25.484 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| python3 | 49541 |  | 32 | 99.630% | 108.794% | 3.140 s | 33.197 MB | 34.457 MB | 56.686 MB | 57.438 MB | 0.000000 MB | 0.199219 MB |
| docker | 49543 |  | 1 | n/a% | n/a% | n/a s | 25.824 MB | 25.824 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 49569 |  | 1 | n/a% | n/a% | n/a s | 0.559 MB | 0.559 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 49585 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.668 MB | 25.668 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 49601 |  | 1 | n/a% | n/a% | n/a s | 25.488 MB | 25.488 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 49625 |  | 1 | n/a% | n/a% | n/a s | 23.070 MB | 23.070 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| python3 | 49632 |  | 3 | 103.737% | 108.821% | 0.210 s | 27.849 MB | 33.883 MB | 51.331 MB | 56.379 MB | 0.000000 MB | 0.000000 MB |
| docker | 49659 |  | 1 | n/a% | n/a% | n/a s | 25.621 MB | 25.621 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 49692 |  | 1 | n/a% | n/a% | n/a s | 9.582 MB | 9.582 MB | 1451.949 MB | 1451.949 MB | n/a MB | n/a MB |

## GPU metrics

_No GPU samples were collected._

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| alex_0000 | 47.580% | 100.099% | 1.667 s | 6.714 MB | 35.340 MB | 0.000000 MB | 0.003906 MB | 3531.773222 MB | 21.366227 MB |
| andy_0000 | 48.204% | 100.707% | 1.344 s | 8.314 MB | 36.395 MB | 0.105469 MB | 0.003906 MB | 0.001476 MB | 0.000240 MB |
| arch_0000 | 51.931% | 101.514% | 1.592 s | 10.597 MB | 36.211 MB | 0.000000 MB | 1.625000 MB | 0.001286 MB | 0.000160 MB |
| bake_0000 | 48.035% | 106.365% | 1.536 s | 8.060 MB | 35.484 MB | 0.000000 MB | 0.425781 MB | 0.001429 MB | 0.000200 MB |
| bale_0000 | 77.905% | 101.106% | 3.987 s | 21.584 MB | 35.703 MB | 0.125000 MB | 0.003906 MB | 0.001570 MB | 0.000200 MB |
| band_0000 | 57.293% | 100.113% | 1.175 s | 9.878 MB | 34.836 MB | 0.023438 MB | 0.003906 MB | 0.000866 MB | 0.000080 MB |

## Incomplete spans

_No spans were still open when profiling stopped._

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sync:result_wait | 12/12 | 0 | 0 | 318.767 | 0.002 | 318.762 | 26563.958 | 24173.812 | 39294.041 |
| turn | 41/41 | 0 | 0 | 263.683 | 1.277 | 262.126 | 6431.292 | 4429.521 | 22654.328 |
| llm:attempt | 41/41 | 0 | 0 | 227.009 | 1.018 | 225.833 | 5536.804 | 3408.518 | 22632.857 |
| run:diagnose_bug | 6/6 | 0 | 0 | 184.651 | 0.691 | 183.787 | 30775.236 | 30347.322 | 41236.241 |
| agsync:join | 3/3 | 0 | 0 | 172.987 | 0.001 | 172.986 | 57662.283 | 52857.440 | 71393.886 |
| llm:diagnose_bug | 16/16 | 0 | 0 | 143.567 | 0.530 | 142.956 | 8972.915 | 5852.072 | 26480.627 |
| run:repair_bug | 6/6 | 0 | 0 | 134.120 | 0.661 | 133.337 | 22353.388 | 22068.916 | 28902.636 |
| capstone:prepare:bitcount | 1/1 | 0 | 0 | 120.133 | 0.031 | 120.102 | 120132.883 | 120132.883 | 120132.883 |
| llm:repair_bug | 25/25 | 0 | 0 | 83.456 | 0.501 | 82.877 | 3338.233 | 2909.771 | 6608.714 |
| teardown:commit | 12/12 | 0 | 0 | 54.842 | 0.031 | 54.802 | 4570.174 | 4287.728 | 5937.265 |
| sandbox:commit | 12/12 | 0 | 0 | 54.542 | 0.024 | 54.511 | 4545.159 | 4267.779 | 5908.795 |
| capstone:plan:mergesort | 1/1 | 0 | 0 | 42.854 | 0.001 | 42.854 | 42854.482 | 42854.482 | 42854.482 |
| capstone:plan:levenshtein | 1/1 | 0 | 0 | 36.382 | 0.001 | 36.381 | 36382.120 | 36382.120 | 36382.120 |
| capstone:plan:bitcount | 1/1 | 0 | 0 | 35.473 | 0.001 | 35.471 | 35472.619 | 35472.619 | 35472.619 |
| capstone:build:mergesort | 1/1 | 0 | 0 | 30.203 | 0.001 | 30.203 | 30203.334 | 30203.334 | 30203.334 |
| capstone:plan:gcd | 1/1 | 0 | 0 | 25.226 | 0.001 | 25.223 | 25225.861 | 25225.861 | 25225.861 |
| capstone:build:levenshtein | 1/1 | 0 | 0 | 25.001 | 0.001 | 25.000 | 25000.568 | 25000.568 | 25000.568 |
| capstone:build:is_valid_parenthesization | 1/1 | 0 | 0 | 23.348 | 0.000 | 23.347 | 23348.025 | 23348.025 | 23348.025 |
| capstone:plan:is_valid_parenthesization | 1/1 | 0 | 0 | 22.563 | 0.001 | 22.562 | 22563.010 | 22563.010 | 22563.010 |
| capstone:plan:flatten | 1/1 | 0 | 0 | 22.160 | 0.001 | 22.158 | 22160.132 | 22160.132 | 22160.132 |
| tool_dispatch:repair_bug | 25/25 | 0 | 0 | 21.607 | 0.110 | 21.460 | 864.261 | 737.211 | 1792.248 |
| capstone:build:gcd | 1/1 | 0 | 0 | 20.791 | 0.000 | 20.790 | 20790.544 | 20790.544 | 20790.544 |
| capstone:build:flatten | 1/1 | 0 | 0 | 17.624 | 0.001 | 17.623 | 17623.687 | 17623.687 | 17623.687 |
| capstone:build:bitcount | 1/1 | 0 | 0 | 17.156 | 0.000 | 17.155 | 17155.610 | 17155.610 | 17155.610 |
| tool_dispatch:diagnose_bug | 16/16 | 0 | 0 | 15.021 | 0.106 | 14.832 | 938.791 | 686.159 | 2182.270 |
| tool:read | 20/20 | 0 | 0 | 13.400 | 0.092 | 13.232 | 669.977 | 649.191 | 947.632 |
| sandbox:start | 33/33 | 0 | 0 | 12.804 | 0.055 | 12.718 | 387.999 | 353.604 | 641.789 |
| sandbox:exec | 7/7 | 0 | 0 | 11.026 | 0.016 | 11.009 | 1575.112 | 1199.384 | 3223.424 |
| tool:bash | 6/6 | 0 | 0 | 10.645 | 0.017 | 10.627 | 1774.206 | 1380.072 | 3341.242 |
| sandbox:stop | 65/65 | 0 | 0 | 9.019 | 0.054 | 8.940 | 138.750 | 204.545 | 295.086 |
| capstone:prepare:mergesort | 1/1 | 0 | 0 | 7.058 | 0.043 | 7.014 | 7057.709 | 7057.709 | 7057.709 |
| sandbox:read_file | 26/26 | 0 | 0 | 5.092 | 0.039 | 5.000 | 195.854 | 130.701 | 552.927 |
| tool:edit | 6/6 | 0 | 0 | 3.446 | 0.026 | 3.401 | 574.344 | 566.793 | 708.875 |
| capstone:verify:levenshtein | 1/1 | 0 | 0 | 3.327 | 0.003 | 3.323 | 3326.741 | 3326.741 | 3326.741 |
| capstone:prepare:levenshtein | 1/1 | 0 | 0 | 2.520 | 0.031 | 2.489 | 2519.712 | 2519.712 | 2519.712 |
| agent:create | 6/6 | 0 | 0 | 1.827 | 0.494 | 1.330 | 304.521 | 135.984 | 891.840 |
| capstone:verify:gcd | 1/1 | 0 | 0 | 0.921 | 0.001 | 0.918 | 921.070 | 921.070 | 921.070 |
| capstone:verify:is_valid_parenthesization | 1/1 | 0 | 0 | 0.764 | 0.001 | 0.762 | 763.588 | 763.588 | 763.588 |
| sandbox:destroy | 6/6 | 0 | 0 | 0.715 | 0.010 | 0.705 | 119.237 | 117.341 | 128.457 |
| sandbox:write_file | 6/6 | 0 | 0 | 0.680 | 0.007 | 0.667 | 113.285 | 114.168 | 134.533 |
| capstone:prepare:gcd | 1/1 | 0 | 0 | 0.482 | 0.034 | 0.448 | 482.185 | 482.185 | 482.185 |
| capstone:prepare:flatten | 1/1 | 0 | 0 | 0.443 | 0.030 | 0.412 | 442.833 | 442.833 | 442.833 |
| capstone:prepare:is_valid_parenthesization | 1/1 | 0 | 0 | 0.435 | 0.033 | 0.401 | 434.706 | 434.706 | 434.706 |
| capstone:verify:flatten | 1/1 | 0 | 0 | 0.396 | 0.001 | 0.394 | 395.524 | 395.524 | 395.524 |
| capstone:verify:mergesort | 1/1 | 0 | 0 | 0.394 | 0.001 | 0.392 | 394.250 | 394.250 | 394.250 |
| tool:glob | 1/1 | 0 | 0 | 0.386 | 0.003 | 0.383 | 385.538 | 385.538 | 385.538 |
| capstone:verify:bitcount | 1/1 | 0 | 0 | 0.381 | 0.001 | 0.380 | 381.379 | 381.379 | 381.379 |
| sandbox:provision | 6/6 | 0 | 0 | 0.170 | 0.006 | 0.162 | 28.284 | 0.706 | 124.795 |
| sandbox:create | 6/6 | 0 | 0 | 0.168 | 0.005 | 0.162 | 28.068 | 0.525 | 124.519 |
| run:detect | 1/1 | 0 | 0 | 0.110 | 0.001 | 0.108 | 109.684 | 109.684 | 109.684 |
| sync:container | 438/438 | 0 | 0 | 0.061 | 0.055 | 0.002 | 0.138 | 0.136 | 0.258 |
| prune | 12/12 | 0 | 0 | 0.004 | 0.002 | 0.001 | 0.301 | 0.260 | 0.631 |
| agprof:clock_sync | 1/1 | 0 | 0 | 0.003 | 0.003 | 0.000 | 3.219 | 3.219 | 3.219 |
| tool:return_summary | 8/8 | 2 | 0 | 0.003 | 0.003 | 0.000 | 0.377 | 0.353 | 0.505 |
| llm:sync | 41/41 | 0 | 0 | 0.003 | 0.002 | 0.000 | 0.061 | 0.048 | 0.128 |
| tool:return_plan | 6/6 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.365 | 0.371 | 0.404 |
| tool:return_status | 6/6 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.364 | 0.310 | 0.586 |
| proc_wait | 12/12 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.120 | 0.068 | 0.350 |
| input:prepare | 12/12 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.115 | 0.095 | 0.201 |
| resolve | 12/12 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.086 | 0.077 | 0.157 |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1678 | 43.343 | 0.000 | 229.273 | 18.017 | 74.226881 CPU seconds | n/a |
| python3 (PID 40348) CPU | percent | 3048 | 3.529 | 0.000 | 133.079 | 0.000 | 11.350000 CPU seconds | n/a |
| python3 (PID 40348) io read MB/s | MB/s | 3048 | 0.092 | 0.000 | 69.564 | 0.000 | 29.285156 MB | n/a |
| python3 (PID 40348) io write MB/s | MB/s | 3048 | 0.050 | 0.000 | 22.249 | 0.000 | 15.503906 MB | n/a |
| python3 (PID 40348) rss_mb | MB | 3049 | 670.115 | 610.820 | 694.426 | 694.426 | n/a | n/a |
| python3 (PID 40348) vms_mb | MB | 3049 | 3739.516 | 3405.512 | 3973.430 | 3949.371 | n/a | n/a |
| git (PID 40354) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| git (PID 40354) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 40354) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 40354) rss_mb | MB | 5 | 4.707 | 4.707 | 4.707 | 4.707 | n/a | n/a |
| git (PID 40354) vms_mb | MB | 5 | 12.516 | 12.516 | 12.516 | 12.516 | n/a | n/a |
| git (PID 40355) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| git (PID 40355) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 40355) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 40355) rss_mb | MB | 5 | 3.512 | 3.512 | 3.512 | 3.512 | n/a | n/a |
| git (PID 40355) vms_mb | MB | 5 | 11.273 | 11.273 | 11.273 | 11.273 | n/a | n/a |
| git-remote-http (PID 40356) CPU | percent | 4 | 14.768 | 0.000 | 39.383 | 0.000 | 0.060000 CPU seconds | n/a |
| git-remote-http (PID 40356) io read MB/s | MB/s | 4 | 2.144 | 0.000 | 6.846 | 0.000 | 0.871094 MB | n/a |
| git-remote-http (PID 40356) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git-remote-http (PID 40356) rss_mb | MB | 5 | 15.460 | 0.258 | 19.332 | 19.332 | n/a | n/a |
| git-remote-http (PID 40356) vms_mb | MB | 5 | 85.941 | 1.438 | 107.566 | 107.566 | n/a | n/a |
| git (PID 40360) rss_mb | MB | 1 | 4.383 | 4.383 | 4.383 | 4.383 | n/a | n/a |
| git (PID 40360) vms_mb | MB | 1 | 11.273 | 11.273 | 11.273 | 11.273 | n/a | n/a |
| python3 (PID 40362) CPU | percent | 1188 | 99.993 | 95.082 | 109.057 | 99.028 | 119.980000 CPU seconds | n/a |
| python3 (PID 40362) io read MB/s | MB/s | 1188 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 40362) io write MB/s | MB/s | 1188 | 0.000 | 0.000 | 0.116 | 0.000 | 0.015625 MB | n/a |
| python3 (PID 40362) rss_mb | MB | 1189 | 34.074 | 17.773 | 34.094 | 34.094 | n/a | n/a |
| python3 (PID 40362) vms_mb | MB | 1189 | 56.359 | 42.430 | 56.375 | 56.375 | n/a | n/a |
| python3 (PID 40363) CPU | percent | 3 | 99.009 | 89.124 | 108.828 | 99.074 | 0.300000 CPU seconds | n/a |
| python3 (PID 40363) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 40363) io write MB/s | MB/s | 3 | 0.697 | 0.000 | 2.090 | 2.090 | 0.210938 MB | n/a |
| python3 (PID 40363) rss_mb | MB | 4 | 25.030 | 11.703 | 34.695 | 34.695 | n/a | n/a |
| python3 (PID 40363) vms_mb | MB | 4 | 49.276 | 38.035 | 57.500 | 57.500 | n/a | n/a |
| python3 (PID 40364) CPU | percent | 3 | 99.007 | 89.177 | 108.848 | 89.177 | 0.300000 CPU seconds | n/a |
| python3 (PID 40364) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 40364) io write MB/s | MB/s | 3 | 0.697 | 0.000 | 2.051 | 2.051 | 0.210938 MB | n/a |
| python3 (PID 40364) rss_mb | MB | 4 | 29.270 | 19.934 | 36.043 | 36.043 | n/a | n/a |
| python3 (PID 40364) vms_mb | MB | 4 | 52.499 | 44.238 | 58.508 | 58.508 | n/a | n/a |
| python3 (PID 40365) CPU | percent | 3 | 98.984 | 98.883 | 99.091 | 99.091 | 0.300000 CPU seconds | n/a |
| python3 (PID 40365) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 40365) io write MB/s | MB/s | 3 | 0.052 | 0.000 | 0.155 | 0.155 | 0.015625 MB | n/a |
| python3 (PID 40365) rss_mb | MB | 4 | 22.988 | 6.766 | 34.094 | 34.094 | n/a | n/a |
| python3 (PID 40365) vms_mb | MB | 4 | 47.879 | 35.051 | 57.504 | 57.504 | n/a | n/a |
| python3 (PID 40366) CPU | percent | 23 | 99.914 | 89.124 | 108.994 | 99.032 | 2.320000 CPU seconds | n/a |
| python3 (PID 40366) io read MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 40366) io write MB/s | MB/s | 23 | 0.007 | 0.000 | 0.116 | 0.000 | 0.015625 MB | n/a |
| python3 (PID 40366) rss_mb | MB | 24 | 33.306 | 19.492 | 34.336 | 34.336 | n/a | n/a |
| python3 (PID 40366) vms_mb | MB | 24 | 55.790 | 44.055 | 57.504 | 57.504 | n/a | n/a |
| python3 (PID 40367) CPU | percent | 68 | 99.896 | 89.078 | 108.958 | 99.065 | 6.860000 CPU seconds | n/a |
| python3 (PID 40367) io read MB/s | MB/s | 68 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 40367) io write MB/s | MB/s | 68 | 0.031 | 0.000 | 1.974 | 0.000 | 0.214844 MB | n/a |
| python3 (PID 40367) rss_mb | MB | 69 | 41.615 | 19.828 | 47.414 | 47.414 | n/a | n/a |
| python3 (PID 40367) vms_mb | MB | 69 | 64.629 | 44.055 | 70.637 | 70.637 | n/a | n/a |
| docker (PID 40371) rss_mb | MB | 1 | 26.199 | 26.199 | 26.199 | 26.199 | n/a | n/a |
| docker (PID 40371) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 40409) rss_mb | MB | 1 | 25.988 | 25.988 | 25.988 | 25.988 | n/a | n/a |
| docker (PID 40409) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 40417) rss_mb | MB | 1 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| docker (PID 40417) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 40428) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 40428) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 40428) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 40428) rss_mb | MB | 3 | 27.345 | 27.020 | 27.508 | 27.508 | n/a | n/a |
| docker (PID 40428) vms_mb | MB | 3 | 1708.776 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 40449) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 40449) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 40449) io write MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 40449) rss_mb | MB | 4 | 27.483 | 27.023 | 27.637 | 27.637 | n/a | n/a |
| docker (PID 40449) vms_mb | MB | 4 | 1714.776 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [alex_0000] (PID 40520) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [alex_0000] (PID 40520) rss_mb | MB | 6 | 2.582 | 0.633 | 12.328 | 0.633 | n/a | n/a |
| docker-init [alex_0000] (PID 40520) vms_mb | MB | 6 | 250.583 | 1.055 | 1498.223 | 1.055 | n/a | n/a |
| docker-init [andy_0000] (PID 40526) CPU | percent | 6 | 1.611 | 0.000 | 9.665 | 0.000 | 0.010000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 40526) rss_mb | MB | 7 | 4.091 | 0.633 | 13.016 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 40526) vms_mb | MB | 7 | 449.532 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 40555) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 40555) rss_mb | MB | 5 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [alex_0000] (PID 40555) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 40565) CPU | percent | 1 | 14.645 | 14.645 | 14.645 | 14.645 | 0.020000 CPU seconds | n/a |
| docker (PID 40565) io read MB/s | MB/s | 1 | 0.257 | 0.257 | 0.257 | 0.257 | 0.035156 MB | n/a |
| docker (PID 40565) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 40565) rss_mb | MB | 2 | 14.395 | 1.500 | 27.289 | 27.289 | n/a | n/a |
| docker (PID 40565) vms_mb | MB | 2 | 846.768 | 32.762 | 1660.773 | 1660.773 | n/a | n/a |
| tail [andy_0000] (PID 40573) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 40573) rss_mb | MB | 5 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [andy_0000] (PID 40573) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 40584) rss_mb | MB | 1 | 27.531 | 27.531 | 27.531 | 27.531 | n/a | n/a |
| docker (PID 40584) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] (PID 40602) rss_mb | MB | 1 | 12.453 | 12.453 | 12.453 | 12.453 | n/a | n/a |
| runc:[2:INIT] (PID 40602) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 40647) rss_mb | MB | 1 | 27.406 | 27.406 | 27.406 | 27.406 | n/a | n/a |
| docker (PID 40647) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 40649) rss_mb | MB | 1 | 27.438 | 27.438 | 27.438 | 27.438 | n/a | n/a |
| docker (PID 40649) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 40692) rss_mb | MB | 1 | 11.473 | 11.473 | 11.473 | 11.473 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 40692) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 40693) rss_mb | MB | 1 | 11.992 | 11.992 | 11.992 | 11.992 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 40693) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 40705) rss_mb | MB | 1 | 27.453 | 27.453 | 27.453 | 27.453 | n/a | n/a |
| docker (PID 40705) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 40707) rss_mb | MB | 1 | 27.285 | 27.285 | 27.285 | 27.285 | n/a | n/a |
| docker (PID 40707) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 40744) rss_mb | MB | 1 | 12.004 | 12.004 | 12.004 | 12.004 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 40744) vms_mb | MB | 1 | 1642.730 | 1642.730 | 1642.730 | 1642.730 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 40746) rss_mb | MB | 1 | 11.418 | 11.418 | 11.418 | 11.418 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 40746) vms_mb | MB | 1 | 1498.223 | 1498.223 | 1498.223 | 1498.223 | n/a | n/a |
| docker (PID 40776) rss_mb | MB | 1 | 27.266 | 27.266 | 27.266 | 27.266 | n/a | n/a |
| docker (PID 40776) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 40781) rss_mb | MB | 1 | 27.527 | 27.527 | 27.527 | 27.527 | n/a | n/a |
| docker (PID 40781) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 40804) rss_mb | MB | 1 | 11.543 | 11.543 | 11.543 | 11.543 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 40804) vms_mb | MB | 1 | 1570.098 | 1570.098 | 1570.098 | 1570.098 | n/a | n/a |
| docker (PID 40839) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 40839) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 40839) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 40839) rss_mb | MB | 3 | 27.152 | 27.152 | 27.152 | 27.152 | n/a | n/a |
| docker (PID 40839) vms_mb | MB | 3 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 40862) CPU | percent | 2 | 9.576 | 0.000 | 19.152 | 0.000 | 0.020000 CPU seconds | n/a |
| docker (PID 40862) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 40862) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 40862) rss_mb | MB | 3 | 24.257 | 18.340 | 27.215 | 27.215 | n/a | n/a |
| docker (PID 40862) vms_mb | MB | 3 | 1612.499 | 1515.949 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 40986) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 40986) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 40986) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 40986) rss_mb | MB | 2 | 25.453 | 25.453 | 25.453 | 25.453 | n/a | n/a |
| docker (PID 40986) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 40995) CPU | percent | 2 | 4.887 | 0.000 | 9.774 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 40995) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 40995) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 40995) rss_mb | MB | 3 | 24.210 | 18.551 | 27.039 | 27.039 | n/a | n/a |
| docker (PID 40995) vms_mb | MB | 3 | 1612.499 | 1515.949 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 41056) CPU | percent | 5 | 1.917 | 0.000 | 9.584 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 41056) rss_mb | MB | 6 | 2.544 | 0.633 | 12.098 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 41056) vms_mb | MB | 6 | 262.583 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 41073) CPU | percent | 5 | 3.834 | 0.000 | 19.168 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 41073) rss_mb | MB | 6 | 4.512 | 0.633 | 13.016 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 41073) vms_mb | MB | 6 | 524.066 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 41097) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 41097) rss_mb | MB | 5 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [andy_0000] (PID 41097) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 41106) rss_mb | MB | 1 | 9.574 | 9.574 | 9.574 | 9.574 | n/a | n/a |
| docker (PID 41106) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 41121) rss_mb | MB | 1 | 26.836 | 26.836 | 26.836 | 26.836 | n/a | n/a |
| docker (PID 41121) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| tail [alex_0000] (PID 41123) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 41123) rss_mb | MB | 4 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [alex_0000] (PID 41123) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 41150) rss_mb | MB | 1 | 11.676 | 11.676 | 11.676 | 11.676 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 41150) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 41159) rss_mb | MB | 1 | 15.613 | 15.613 | 15.613 | 15.613 | n/a | n/a |
| docker (PID 41159) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 41181) rss_mb | MB | 1 | 27.199 | 27.199 | 27.199 | 27.199 | n/a | n/a |
| docker (PID 41181) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 41207) rss_mb | MB | 1 | 11.941 | 11.941 | 11.941 | 11.941 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 41207) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 41214) rss_mb | MB | 1 | 25.086 | 25.086 | 25.086 | 25.086 | n/a | n/a |
| docker (PID 41214) vms_mb | MB | 1 | 1659.961 | 1659.961 | 1659.961 | 1659.961 | n/a | n/a |
| docker (PID 41251) rss_mb | MB | 1 | 26.688 | 26.688 | 26.688 | 26.688 | n/a | n/a |
| docker (PID 41251) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 41259) rss_mb | MB | 1 | 24.047 | 24.047 | 24.047 | 24.047 | n/a | n/a |
| docker (PID 41259) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 41278) rss_mb | MB | 1 | 10.715 | 10.715 | 10.715 | 10.715 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 41278) vms_mb | MB | 1 | 1569.695 | 1569.695 | 1569.695 | 1569.695 | n/a | n/a |
| docker (PID 41323) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 41323) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 41323) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 41323) rss_mb | MB | 2 | 25.902 | 25.902 | 25.902 | 25.902 | n/a | n/a |
| docker (PID 41323) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 41353) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 41353) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 41353) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 41353) rss_mb | MB | 2 | 26.078 | 26.078 | 26.078 | 26.078 | n/a | n/a |
| docker (PID 41353) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 41468) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 41468) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 41468) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 41468) rss_mb | MB | 2 | 25.914 | 25.914 | 25.914 | 25.914 | n/a | n/a |
| docker (PID 41468) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 41508) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 41508) rss_mb | MB | 3 | 4.734 | 0.633 | 12.938 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 41508) vms_mb | MB | 3 | 524.112 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 41530) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 41530) rss_mb | MB | 2 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [alex_0000] (PID 41530) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 41543) rss_mb | MB | 1 | 26.801 | 26.801 | 26.801 | 26.801 | n/a | n/a |
| docker (PID 41543) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 41561) rss_mb | MB | 1 | 11.480 | 11.480 | 11.480 | 11.480 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 41561) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 41568) rss_mb | MB | 1 | 27.152 | 27.152 | 27.152 | 27.152 | n/a | n/a |
| docker (PID 41568) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 41588) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 41588) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| docker (PID 41611) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 41611) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 41611) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 41611) rss_mb | MB | 2 | 25.977 | 25.977 | 25.977 | 25.977 | n/a | n/a |
| docker (PID 41611) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 41685) CPU | percent | 1 | 9.866 | 9.866 | 9.866 | 9.866 | 0.010000 CPU seconds | n/a |
| docker (PID 41685) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 41685) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 41685) rss_mb | MB | 2 | 18.102 | 9.102 | 27.102 | 27.102 | n/a | n/a |
| docker (PID 41685) vms_mb | MB | 2 | 1484.232 | 1307.691 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 41723) CPU | percent | 3 | 6.532 | 0.000 | 19.597 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 41723) rss_mb | MB | 4 | 3.634 | 0.633 | 12.637 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 41723) vms_mb | MB | 4 | 393.473 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 41749) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 41749) rss_mb | MB | 3 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [alex_0000] (PID 41749) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 41751) rss_mb | MB | 1 | 27.023 | 27.023 | 27.023 | 27.023 | n/a | n/a |
| docker (PID 41751) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 41785) rss_mb | MB | 1 | 27.449 | 27.449 | 27.449 | 27.449 | n/a | n/a |
| docker (PID 41785) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[0:PARENT] [alex_0000] (PID 41801) rss_mb | MB | 1 | 1.996 | 1.996 | 1.996 | 1.996 | n/a | n/a |
| runc:[0:PARENT] [alex_0000] (PID 41801) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[1:CHILD] [alex_0000] (PID 41803) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[1:CHILD] [alex_0000] (PID 41803) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 41821) rss_mb | MB | 1 | 27.316 | 27.316 | 27.316 | 27.316 | n/a | n/a |
| docker (PID 41821) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 41843) rss_mb | MB | 1 | 11.898 | 11.898 | 11.898 | 11.898 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 41843) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 41859) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 41859) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 41859) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 41859) rss_mb | MB | 2 | 26.320 | 26.320 | 26.320 | 26.320 | n/a | n/a |
| docker (PID 41859) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 41923) rss_mb | MB | 1 | 14.875 | 14.875 | 14.875 | 14.875 | n/a | n/a |
| docker (PID 41923) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 41931) rss_mb | MB | 1 | 25.566 | 25.566 | 25.566 | 25.566 | n/a | n/a |
| docker (PID 41931) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 41970) CPU | percent | 3 | 9.795 | 0.000 | 29.384 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 41970) rss_mb | MB | 4 | 3.370 | 0.633 | 11.582 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 41970) vms_mb | MB | 4 | 393.249 | 1.055 | 1569.832 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 41994) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 41994) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [andy_0000] (PID 41994) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 42034) rss_mb | MB | 1 | 25.562 | 25.562 | 25.562 | 25.562 | n/a | n/a |
| docker (PID 42034) vms_mb | MB | 1 | 1587.957 | 1587.957 | 1587.957 | 1587.957 | n/a | n/a |
| docker (PID 42070) rss_mb | MB | 1 | 27.430 | 27.430 | 27.430 | 27.430 | n/a | n/a |
| docker (PID 42070) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[0:PARENT] [andy_0000] (PID 42086) rss_mb | MB | 1 | 1.969 | 1.969 | 1.969 | 1.969 | n/a | n/a |
| runc:[0:PARENT] [andy_0000] (PID 42086) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| docker (PID 42107) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 42107) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 42107) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 42107) rss_mb | MB | 2 | 26.852 | 26.852 | 26.852 | 26.852 | n/a | n/a |
| docker (PID 42107) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 42205) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 42205) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 42205) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 42205) rss_mb | MB | 38 | 25.682 | 23.879 | 25.730 | 25.730 | n/a | n/a |
| docker (PID 42205) vms_mb | MB | 38 | 1658.316 | 1588.203 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 42221) rss_mb | MB | 1 | 19.055 | 19.055 | 19.055 | 19.055 | n/a | n/a |
| docker (PID 42221) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 42240) rss_mb | MB | 1 | 23.008 | 23.008 | 23.008 | 23.008 | n/a | n/a |
| docker (PID 42240) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 42248) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 42248) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 42248) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 42248) rss_mb | MB | 2 | 25.621 | 25.621 | 25.621 | 25.621 | n/a | n/a |
| docker (PID 42248) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 42288) CPU | percent | 3 | 6.535 | 0.000 | 19.604 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 42288) rss_mb | MB | 4 | 3.394 | 0.633 | 11.676 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 42288) vms_mb | MB | 4 | 393.281 | 1.055 | 1569.961 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 42314) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 42314) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [andy_0000] (PID 42314) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 42353) rss_mb | MB | 1 | 16.309 | 16.309 | 16.309 | 16.309 | n/a | n/a |
| docker (PID 42353) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 42389) rss_mb | MB | 1 | 27.520 | 27.520 | 27.520 | 27.520 | n/a | n/a |
| docker (PID 42389) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 42428) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 42428) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 42428) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 42428) rss_mb | MB | 2 | 27.109 | 27.109 | 27.109 | 27.109 | n/a | n/a |
| docker (PID 42428) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 42503) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 42503) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 42503) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 42503) rss_mb | MB | 2 | 24.393 | 22.047 | 26.738 | 26.738 | n/a | n/a |
| docker (PID 42503) vms_mb | MB | 2 | 1588.486 | 1516.199 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 42543) CPU | percent | 10 | 0.861 | 0.000 | 8.605 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 42543) rss_mb | MB | 11 | 1.737 | 0.633 | 12.777 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 42543) vms_mb | MB | 11 | 143.707 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 42566) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 42566) rss_mb | MB | 10 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [andy_0000] (PID 42566) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 42578) rss_mb | MB | 1 | 26.715 | 26.715 | 26.715 | 26.715 | n/a | n/a |
| docker (PID 42578) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 42606) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 42606) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 42606) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 42606) rss_mb | MB | 9 | 27.178 | 27.164 | 27.289 | 27.289 | n/a | n/a |
| docker (PID 42606) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 42626) CPU | percent | 8 | 2.447 | 0.000 | 19.577 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 42626) rss_mb | MB | 9 | 4.283 | 3.359 | 11.672 | 3.359 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 42626) vms_mb | MB | 9 | 178.414 | 4.391 | 1570.598 | 4.391 | n/a | n/a |
| python [andy_0000] (PID 42635) CPU | percent | 7 | 100.775 | 88.173 | 107.858 | 107.846 | 0.720000 CPU seconds | n/a |
| python [andy_0000] (PID 42635) rss_mb | MB | 8 | 32.959 | 16.379 | 42.469 | 42.469 | n/a | n/a |
| python [andy_0000] (PID 42635) vms_mb | MB | 8 | 40.277 | 20.949 | 52.238 | 52.238 | n/a | n/a |
| docker (PID 42645) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 42645) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 42645) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 42645) rss_mb | MB | 2 | 27.129 | 27.129 | 27.129 | 27.129 | n/a | n/a |
| docker (PID 42645) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 42718) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 42718) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 42718) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 42718) rss_mb | MB | 2 | 27.336 | 27.336 | 27.336 | 27.336 | n/a | n/a |
| docker (PID 42718) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 42758) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 42758) rss_mb | MB | 4 | 3.681 | 0.633 | 12.824 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 42758) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 42782) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 42782) rss_mb | MB | 3 | 1.809 | 1.809 | 1.809 | 1.809 | n/a | n/a |
| tail [andy_0000] (PID 42782) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 42792) rss_mb | MB | 1 | 27.488 | 27.488 | 27.488 | 27.488 | n/a | n/a |
| docker (PID 42792) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 42823) rss_mb | MB | 1 | 26.961 | 26.961 | 26.961 | 26.961 | n/a | n/a |
| docker (PID 42823) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 42886) rss_mb | MB | 1 | 20.148 | 20.148 | 20.148 | 20.148 | n/a | n/a |
| docker (PID 42886) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 42894) rss_mb | MB | 1 | 26.055 | 26.055 | 26.055 | 26.055 | n/a | n/a |
| docker (PID 42894) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 42952) rss_mb | MB | 1 | 17.109 | 17.109 | 17.109 | 17.109 | n/a | n/a |
| docker (PID 42952) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 42992) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 42992) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 42992) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 42992) rss_mb | MB | 39 | 25.352 | 25.352 | 25.352 | 25.352 | n/a | n/a |
| docker (PID 42992) vms_mb | MB | 39 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 43005) rss_mb | MB | 1 | 25.711 | 25.711 | 25.711 | 25.711 | n/a | n/a |
| docker (PID 43005) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 43035) rss_mb | MB | 1 | 26.715 | 26.715 | 26.715 | 26.715 | n/a | n/a |
| docker (PID 43035) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 43045) CPU | percent | 42 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 43045) io read MB/s | MB/s | 42 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 43045) io write MB/s | MB/s | 42 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 43045) rss_mb | MB | 43 | 26.938 | 26.938 | 26.938 | 26.938 | n/a | n/a |
| docker (PID 43045) vms_mb | MB | 43 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 43060) rss_mb | MB | 1 | 11.168 | 11.168 | 11.168 | 11.168 | n/a | n/a |
| docker (PID 43060) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 43079) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 43079) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 43079) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 43079) rss_mb | MB | 3 | 25.387 | 25.387 | 25.387 | 25.387 | n/a | n/a |
| docker (PID 43079) vms_mb | MB | 3 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 43117) CPU | percent | 5 | 7.843 | 0.000 | 39.215 | 0.000 | 0.040000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 43117) rss_mb | MB | 6 | 4.498 | 0.633 | 13.016 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 43117) vms_mb | MB | 6 | 524.045 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 43149) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 43149) rss_mb | MB | 4 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [alex_0000] (PID 43149) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 43161) rss_mb | MB | 1 | 27.316 | 27.316 | 27.316 | 27.316 | n/a | n/a |
| docker (PID 43161) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 43187) rss_mb | MB | 1 | 27.094 | 27.094 | 27.094 | 27.094 | n/a | n/a |
| docker (PID 43187) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 43221) rss_mb | MB | 1 | 18.078 | 18.078 | 18.078 | 18.078 | n/a | n/a |
| docker (PID 43221) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 43251) rss_mb | MB | 1 | 18.859 | 18.859 | 18.859 | 18.859 | n/a | n/a |
| docker (PID 43251) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 43260) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 43260) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 43260) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 43260) rss_mb | MB | 2 | 26.004 | 26.004 | 26.004 | 26.004 | n/a | n/a |
| docker (PID 43260) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 43336) rss_mb | MB | 1 | 8.730 | 8.730 | 8.730 | 8.730 | n/a | n/a |
| docker (PID 43336) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| run2:repair_bug (PID 43361) rss_mb | MB | 1 | 679.926 | 679.926 | 679.926 | 679.926 | n/a | n/a |
| run2:repair_bug (PID 43361) vms_mb | MB | 1 | 3968.688 | 3968.688 | 3968.688 | 3968.688 | n/a | n/a |
| python3 (PID 43369) CPU | percent | 3 | 98.843 | 98.687 | 98.946 | 98.946 | 0.300000 CPU seconds | n/a |
| python3 (PID 43369) io read MB/s | MB/s | 3 | 0.206 | 0.000 | 0.618 | 0.000 | 0.062500 MB | n/a |
| python3 (PID 43369) io write MB/s | MB/s | 3 | 0.657 | 0.000 | 1.971 | 1.971 | 0.199219 MB | n/a |
| python3 (PID 43369) rss_mb | MB | 4 | 28.187 | 17.980 | 34.512 | 34.512 | n/a | n/a |
| python3 (PID 43369) vms_mb | MB | 4 | 51.832 | 42.570 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 43379) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 43379) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 43379) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 43379) rss_mb | MB | 2 | 27.004 | 27.004 | 27.004 | 27.004 | n/a | n/a |
| docker (PID 43379) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| 6 [alex_0000] (PID 43416) rss_mb | MB | 1 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| 6 [alex_0000] (PID 43416) vms_mb | MB | 1 | 13.980 | 13.980 | 13.980 | 13.980 | n/a | n/a |
| docker-init [alex_0000] (PID 43420) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [alex_0000] (PID 43420) rss_mb | MB | 11 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [alex_0000] (PID 43420) vms_mb | MB | 11 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 43444) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 43444) rss_mb | MB | 10 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [alex_0000] (PID 43444) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 43481) CPU | percent | 8 | 2.438 | 0.000 | 9.804 | 9.804 | 0.020000 CPU seconds | n/a |
| docker (PID 43481) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 43481) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 43481) rss_mb | MB | 9 | 24.349 | 1.234 | 27.348 | 27.348 | n/a | n/a |
| docker (PID 43481) vms_mb | MB | 9 | 1479.883 | 32.762 | 1660.773 | 1660.773 | n/a | n/a |
| bash [alex_0000] (PID 43501) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [alex_0000] (PID 43501) rss_mb | MB | 8 | 3.395 | 3.395 | 3.395 | 3.395 | n/a | n/a |
| bash [alex_0000] (PID 43501) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [alex_0000] (PID 43510) CPU | percent | 7 | 100.864 | 97.846 | 107.845 | 107.845 | 0.720000 CPU seconds | n/a |
| python [alex_0000] (PID 43510) rss_mb | MB | 8 | 30.730 | 11.562 | 41.852 | 41.852 | n/a | n/a |
| python [alex_0000] (PID 43510) vms_mb | MB | 8 | 37.888 | 15.047 | 51.238 | 51.238 | n/a | n/a |
| docker (PID 43520) CPU | percent | 1 | 9.808 | 9.808 | 9.808 | 9.808 | 0.010000 CPU seconds | n/a |
| docker (PID 43520) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 43520) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 43520) rss_mb | MB | 2 | 13.986 | 1.656 | 26.316 | 26.316 | n/a | n/a |
| docker (PID 43520) vms_mb | MB | 2 | 846.486 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 43577) rss_mb | MB | 1 | 22.441 | 22.441 | 22.441 | 22.441 | n/a | n/a |
| docker (PID 43577) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 43594) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 43594) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 43594) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 43594) rss_mb | MB | 5 | 26.531 | 26.531 | 26.531 | 26.531 | n/a | n/a |
| docker (PID 43594) vms_mb | MB | 5 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 43636) CPU | percent | 6 | 17.286 | 0.000 | 86.434 | 0.000 | 0.110000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 43636) rss_mb | MB | 7 | 5.694 | 0.633 | 12.922 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 43636) vms_mb | MB | 7 | 673.554 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 43658) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 43658) rss_mb | MB | 4 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [alex_0000] (PID 43658) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 43670) rss_mb | MB | 1 | 4.586 | 4.586 | 4.586 | 4.586 | n/a | n/a |
| docker (PID 43670) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 43696) rss_mb | MB | 1 | 25.336 | 25.336 | 25.336 | 25.336 | n/a | n/a |
| docker (PID 43696) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 43732) rss_mb | MB | 1 | 26.648 | 26.648 | 26.648 | 26.648 | n/a | n/a |
| docker (PID 43732) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 43771) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 43771) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 43771) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 43771) rss_mb | MB | 2 | 26.883 | 26.883 | 26.883 | 26.883 | n/a | n/a |
| docker (PID 43771) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 43844) rss_mb | MB | 1 | 25.902 | 25.902 | 25.902 | 25.902 | n/a | n/a |
| docker (PID 43844) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 43868) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 43868) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 43868) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 43868) rss_mb | MB | 39 | 26.559 | 26.559 | 26.559 | 26.559 | n/a | n/a |
| docker (PID 43868) vms_mb | MB | 39 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 43893) rss_mb | MB | 1 | 9.242 | 9.242 | 9.242 | 9.242 | n/a | n/a |
| docker (PID 43893) vms_mb | MB | 1 | 1243.691 | 1243.691 | 1243.691 | 1243.691 | n/a | n/a |
| python3 (PID 43916) CPU | percent | 3 | 98.802 | 88.994 | 108.750 | 88.994 | 0.300000 CPU seconds | n/a |
| python3 (PID 43916) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 43916) io write MB/s | MB/s | 3 | 0.605 | 0.000 | 1.815 | 1.815 | 0.183594 MB | n/a |
| python3 (PID 43916) rss_mb | MB | 4 | 24.135 | 9.703 | 34.277 | 34.277 | n/a | n/a |
| python3 (PID 43916) vms_mb | MB | 4 | 48.325 | 35.465 | 57.453 | 57.453 | n/a | n/a |
| docker (PID 43926) rss_mb | MB | 1 | 24.172 | 24.172 | 24.172 | 24.172 | n/a | n/a |
| docker (PID 43926) vms_mb | MB | 1 | 1596.211 | 1596.211 | 1596.211 | 1596.211 | n/a | n/a |
| docker (PID 43969) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 43969) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 44003) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 44003) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 44003) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 44003) rss_mb | MB | 3 | 27.456 | 27.008 | 27.680 | 27.680 | n/a | n/a |
| docker (PID 44003) vms_mb | MB | 3 | 1756.779 | 1660.773 | 1804.781 | 1804.781 | n/a | n/a |
| docker (PID 44043) rss_mb | MB | 1 | 23.906 | 23.906 | 23.906 | 23.906 | n/a | n/a |
| docker (PID 44043) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [arch_0000] (PID 44050) CPU | percent | 6 | 6.339 | 0.000 | 38.035 | 0.000 | 0.040000 CPU seconds | n/a |
| docker-init [arch_0000] (PID 44050) rss_mb | MB | 7 | 3.680 | 0.633 | 13.086 | 0.633 | n/a | n/a |
| docker-init [arch_0000] (PID 44050) vms_mb | MB | 7 | 449.278 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| docker (PID 44066) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 44066) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 44066) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 44066) rss_mb | MB | 3 | 27.146 | 26.688 | 27.375 | 27.375 | n/a | n/a |
| docker (PID 44066) vms_mb | MB | 3 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| tail [arch_0000] (PID 44090) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 44090) rss_mb | MB | 5 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [arch_0000] (PID 44090) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 44095) rss_mb | MB | 1 | 27.559 | 27.559 | 27.559 | 27.559 | n/a | n/a |
| docker (PID 44095) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] (PID 44119) rss_mb | MB | 1 | 11.574 | 11.574 | 11.574 | 11.574 | n/a | n/a |
| runc:[2:INIT] (PID 44119) vms_mb | MB | 1 | 1570.219 | 1570.219 | 1570.219 | 1570.219 | n/a | n/a |
| docker-init [bake_0000] (PID 44157) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bake_0000] (PID 44157) rss_mb | MB | 7 | 2.384 | 0.633 | 12.895 | 0.633 | n/a | n/a |
| docker-init [bake_0000] (PID 44157) vms_mb | MB | 7 | 235.544 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| docker (PID 44171) rss_mb | MB | 1 | 27.379 | 27.379 | 27.379 | 27.379 | n/a | n/a |
| docker (PID 44171) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| tail [bake_0000] (PID 44212) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 44212) rss_mb | MB | 6 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [bake_0000] (PID 44212) vms_mb | MB | 6 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 44216) rss_mb | MB | 1 | 20.234 | 20.234 | 20.234 | 20.234 | n/a | n/a |
| docker (PID 44216) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 44222) rss_mb | MB | 1 | 3.324 | 3.324 | 3.324 | 3.324 | n/a | n/a |
| docker (PID 44222) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 44269) rss_mb | MB | 1 | 19.223 | 19.223 | 19.223 | 19.223 | n/a | n/a |
| docker (PID 44269) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 44277) rss_mb | MB | 1 | 4.469 | 4.469 | 4.469 | 4.469 | n/a | n/a |
| docker (PID 44277) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 44286) rss_mb | MB | 1 | 26.965 | 26.965 | 26.965 | 26.965 | n/a | n/a |
| docker (PID 44286) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 44288) rss_mb | MB | 1 | 27.215 | 27.215 | 27.215 | 27.215 | n/a | n/a |
| docker (PID 44288) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 44314) rss_mb | MB | 1 | 11.977 | 11.977 | 11.977 | 11.977 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 44314) vms_mb | MB | 1 | 1498.223 | 1498.223 | 1498.223 | 1498.223 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 44331) rss_mb | MB | 1 | 12.336 | 12.336 | 12.336 | 12.336 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 44331) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 44363) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 44363) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 44363) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 44363) rss_mb | MB | 2 | 26.047 | 26.047 | 26.047 | 26.047 | n/a | n/a |
| docker (PID 44363) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 44410) rss_mb | MB | 1 | 27.699 | 27.699 | 27.699 | 27.699 | n/a | n/a |
| docker (PID 44410) vms_mb | MB | 1 | 1733.027 | 1733.027 | 1733.027 | 1733.027 | n/a | n/a |
| docker (PID 44481) CPU | percent | 3 | 3.168 | 0.000 | 9.504 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 44481) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 44481) io write MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 44481) rss_mb | MB | 4 | 23.729 | 18.496 | 25.473 | 25.473 | n/a | n/a |
| docker (PID 44481) vms_mb | MB | 4 | 1624.146 | 1515.949 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 44488) rss_mb | MB | 1 | 0.559 | 0.559 | 0.559 | 0.559 | n/a | n/a |
| docker (PID 44488) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 44499) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 44499) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 44499) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 44499) rss_mb | MB | 2 | 26.773 | 26.773 | 26.773 | 26.773 | n/a | n/a |
| docker (PID 44499) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 44558) CPU | percent | 5 | 1.912 | 0.000 | 9.559 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 44558) rss_mb | MB | 6 | 2.643 | 0.633 | 12.695 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 44558) vms_mb | MB | 6 | 250.583 | 1.055 | 1498.223 | 1.055 | n/a | n/a |
| docker (PID 44599) rss_mb | MB | 1 | 26.465 | 26.465 | 26.465 | 26.465 | n/a | n/a |
| docker (PID 44599) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| tail [arch_0000] (PID 44617) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 44617) rss_mb | MB | 5 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [arch_0000] (PID 44617) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 44640) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 44640) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 44640) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 44640) rss_mb | MB | 2 | 27.113 | 27.113 | 27.113 | 27.113 | n/a | n/a |
| docker (PID 44640) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 44642) rss_mb | MB | 1 | 27.492 | 27.492 | 27.492 | 27.492 | n/a | n/a |
| docker (PID 44642) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 44668) rss_mb | MB | 1 | 12.043 | 12.043 | 12.043 | 12.043 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 44668) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 44706) CPU | percent | 4 | 2.430 | 0.000 | 9.721 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 44706) rss_mb | MB | 5 | 3.084 | 0.633 | 12.887 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 44706) vms_mb | MB | 5 | 314.939 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| docker (PID 44713) rss_mb | MB | 1 | 27.117 | 27.117 | 27.117 | 27.117 | n/a | n/a |
| docker (PID 44713) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 44733) rss_mb | MB | 1 | 10.723 | 10.723 | 10.723 | 10.723 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 44733) vms_mb | MB | 1 | 1641.699 | 1641.699 | 1641.699 | 1641.699 | n/a | n/a |
| tail [bake_0000] (PID 44755) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 44755) rss_mb | MB | 4 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [bake_0000] (PID 44755) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 44774) rss_mb | MB | 1 | 18.086 | 18.086 | 18.086 | 18.086 | n/a | n/a |
| docker (PID 44774) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 44776) rss_mb | MB | 1 | 9.277 | 9.277 | 9.277 | 9.277 | n/a | n/a |
| docker (PID 44776) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 44828) rss_mb | MB | 1 | 19.684 | 19.684 | 19.684 | 19.684 | n/a | n/a |
| docker (PID 44828) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 44834) rss_mb | MB | 1 | 10.547 | 10.547 | 10.547 | 10.547 | n/a | n/a |
| docker (PID 44834) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 44845) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 44845) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 44845) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 44845) rss_mb | MB | 2 | 27.074 | 27.074 | 27.074 | 27.074 | n/a | n/a |
| docker (PID 44845) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 44883) rss_mb | MB | 1 | 20.238 | 20.238 | 20.238 | 20.238 | n/a | n/a |
| docker (PID 44883) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 44911) rss_mb | MB | 1 | 27.527 | 27.527 | 27.527 | 27.527 | n/a | n/a |
| docker (PID 44911) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 44945) rss_mb | MB | 1 | 11.523 | 11.523 | 11.523 | 11.523 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 44945) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 44972) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 44972) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 44972) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 44972) rss_mb | MB | 2 | 26.859 | 26.859 | 26.859 | 26.859 | n/a | n/a |
| docker (PID 44972) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 45050) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 45050) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 45050) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 45050) rss_mb | MB | 2 | 26.844 | 26.844 | 26.844 | 26.844 | n/a | n/a |
| docker (PID 45050) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 45090) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 45090) rss_mb | MB | 4 | 3.712 | 0.633 | 12.949 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 45090) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 45118) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 45118) rss_mb | MB | 3 | 1.785 | 1.785 | 1.785 | 1.785 | n/a | n/a |
| tail [bake_0000] (PID 45118) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 45128) rss_mb | MB | 1 | 27.367 | 27.367 | 27.367 | 27.367 | n/a | n/a |
| docker (PID 45128) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 45145) rss_mb | MB | 1 | 10.762 | 10.762 | 10.762 | 10.762 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 45145) vms_mb | MB | 1 | 1569.711 | 1569.711 | 1569.711 | 1569.711 | n/a | n/a |
| docker (PID 45179) rss_mb | MB | 1 | 5.402 | 5.402 | 5.402 | 5.402 | n/a | n/a |
| docker (PID 45179) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 45217) rss_mb | MB | 1 | 26.469 | 26.469 | 26.469 | 26.469 | n/a | n/a |
| docker (PID 45217) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 45225) rss_mb | MB | 1 | 25.965 | 25.965 | 25.965 | 25.965 | n/a | n/a |
| docker (PID 45225) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 45308) rss_mb | MB | 1 | 27.000 | 27.000 | 27.000 | 27.000 | n/a | n/a |
| docker (PID 45308) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 45322) CPU | percent | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 45322) io read MB/s | MB/s | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 45322) io write MB/s | MB/s | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 45322) rss_mb | MB | 44 | 25.828 | 25.828 | 25.828 | 25.828 | n/a | n/a |
| docker (PID 45322) vms_mb | MB | 44 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 45338) rss_mb | MB | 1 | 19.223 | 19.223 | 19.223 | 19.223 | n/a | n/a |
| docker (PID 45338) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 45361) CPU | percent | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 45361) io read MB/s | MB/s | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 45361) io write MB/s | MB/s | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 45361) rss_mb | MB | 44 | 26.941 | 26.941 | 26.941 | 26.941 | n/a | n/a |
| docker (PID 45361) vms_mb | MB | 44 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 45377) rss_mb | MB | 1 | 25.965 | 25.965 | 25.965 | 25.965 | n/a | n/a |
| docker (PID 45377) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 45403) rss_mb | MB | 1 | 26.965 | 26.965 | 26.965 | 26.965 | n/a | n/a |
| docker (PID 45403) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 45429) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 45429) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 45429) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 45429) rss_mb | MB | 2 | 26.535 | 26.535 | 26.535 | 26.535 | n/a | n/a |
| docker (PID 45429) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 45468) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 45468) rss_mb | MB | 4 | 3.711 | 0.633 | 12.945 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 45468) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 45494) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 45494) rss_mb | MB | 3 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [bake_0000] (PID 45494) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 45508) rss_mb | MB | 1 | 27.586 | 27.586 | 27.586 | 27.586 | n/a | n/a |
| docker (PID 45508) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 45534) rss_mb | MB | 1 | 26.941 | 26.941 | 26.941 | 26.941 | n/a | n/a |
| docker (PID 45534) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| sh [bake_0000] (PID 45554) rss_mb | MB | 1 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| sh [bake_0000] (PID 45554) vms_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| docker (PID 45601) rss_mb | MB | 1 | 6.516 | 6.516 | 6.516 | 6.516 | n/a | n/a |
| docker (PID 45601) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 45609) rss_mb | MB | 1 | 25.879 | 25.879 | 25.879 | 25.879 | n/a | n/a |
| docker (PID 45609) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 45675) rss_mb | MB | 1 | 17.707 | 17.707 | 17.707 | 17.707 | n/a | n/a |
| docker (PID 45675) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 45684) rss_mb | MB | 1 | 25.680 | 25.680 | 25.680 | 25.680 | n/a | n/a |
| docker (PID 45684) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 45723) CPU | percent | 13 | 1.915 | 0.000 | 24.895 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 45723) rss_mb | MB | 14 | 1.366 | 0.633 | 10.891 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 45723) vms_mb | MB | 14 | 113.065 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| docker (PID 45730) rss_mb | MB | 1 | 4.473 | 4.473 | 4.473 | 4.473 | n/a | n/a |
| docker (PID 45730) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 45738) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 45738) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 45738) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 45738) rss_mb | MB | 2 | 25.383 | 25.383 | 25.383 | 25.383 | n/a | n/a |
| docker (PID 45738) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| tail [bake_0000] (PID 45764) CPU | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 45764) rss_mb | MB | 13 | 1.695 | 1.695 | 1.695 | 1.695 | n/a | n/a |
| tail [bake_0000] (PID 45764) vms_mb | MB | 13 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 45802) rss_mb | MB | 1 | 27.246 | 27.246 | 27.246 | 27.246 | n/a | n/a |
| docker (PID 45802) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 45815) CPU | percent | 4 | 2.290 | 0.000 | 9.162 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 45815) rss_mb | MB | 5 | 3.109 | 0.633 | 13.016 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 45815) vms_mb | MB | 5 | 329.340 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 45834) rss_mb | MB | 1 | 11.699 | 11.699 | 11.699 | 11.699 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 45834) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 45850) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 45850) io read MB/s | MB/s | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 45850) io write MB/s | MB/s | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 45850) rss_mb | MB | 11 | 27.355 | 27.355 | 27.355 | 27.355 | n/a | n/a |
| docker (PID 45850) vms_mb | MB | 11 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| tail [arch_0000] (PID 45861) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 45861) rss_mb | MB | 4 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [arch_0000] (PID 45861) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| bash [bake_0000] (PID 45882) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bake_0000] (PID 45882) rss_mb | MB | 10 | 3.406 | 3.406 | 3.406 | 3.406 | n/a | n/a |
| bash [bake_0000] (PID 45882) vms_mb | MB | 10 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| docker (PID 45891) rss_mb | MB | 1 | 27.469 | 27.469 | 27.469 | 27.469 | n/a | n/a |
| docker (PID 45891) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python [bake_0000] (PID 45901) CPU | percent | 9 | 92.726 | 71.667 | 110.354 | 88.257 | 0.890000 CPU seconds | n/a |
| python [bake_0000] (PID 45901) rss_mb | MB | 10 | 29.916 | 10.301 | 41.805 | 41.805 | n/a | n/a |
| python [bake_0000] (PID 45901) vms_mb | MB | 10 | 36.659 | 14.660 | 51.375 | 51.375 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 45914) rss_mb | MB | 1 | 11.781 | 11.781 | 11.781 | 11.781 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 45914) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 45921) rss_mb | MB | 1 | 27.289 | 27.289 | 27.289 | 27.289 | n/a | n/a |
| docker (PID 45921) vms_mb | MB | 1 | 1733.027 | 1733.027 | 1733.027 | 1733.027 | n/a | n/a |
| sh [arch_0000] (PID 45943) rss_mb | MB | 1 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| sh [arch_0000] (PID 45943) vms_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| docker (PID 45959) rss_mb | MB | 1 | 27.656 | 27.656 | 27.656 | 27.656 | n/a | n/a |
| docker (PID 45959) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| sh [arch_0000] (PID 45980) rss_mb | MB | 1 | 1.656 | 1.656 | 1.656 | 1.656 | n/a | n/a |
| sh [arch_0000] (PID 45980) vms_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| docker (PID 45998) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 45998) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 45998) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 45998) rss_mb | MB | 2 | 27.098 | 27.098 | 27.098 | 27.098 | n/a | n/a |
| docker (PID 45998) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 46076) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 46076) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 46076) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 46076) rss_mb | MB | 2 | 26.098 | 26.098 | 26.098 | 26.098 | n/a | n/a |
| docker (PID 46076) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 46150) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 46150) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 46150) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 46150) rss_mb | MB | 2 | 27.000 | 27.000 | 27.000 | 27.000 | n/a | n/a |
| docker (PID 46150) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 46189) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 46189) rss_mb | MB | 15 | 1.470 | 0.633 | 13.188 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 46189) vms_mb | MB | 15 | 110.500 | 1.055 | 1642.730 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 46212) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 46212) rss_mb | MB | 14 | 1.777 | 1.777 | 1.777 | 1.777 | n/a | n/a |
| tail [arch_0000] (PID 46212) vms_mb | MB | 14 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 46224) rss_mb | MB | 1 | 27.078 | 27.078 | 27.078 | 27.078 | n/a | n/a |
| docker (PID 46224) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 46250) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 46250) io read MB/s | MB/s | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 46250) io write MB/s | MB/s | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 46250) rss_mb | MB | 12 | 27.382 | 27.371 | 27.496 | 27.496 | n/a | n/a |
| docker (PID 46250) vms_mb | MB | 12 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [arch_0000] (PID 46270) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [arch_0000] (PID 46270) rss_mb | MB | 12 | 3.418 | 3.418 | 3.418 | 3.418 | n/a | n/a |
| bash [arch_0000] (PID 46270) vms_mb | MB | 12 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [arch_0000] (PID 46279) CPU | percent | 11 | 87.837 | 48.894 | 104.473 | 103.106 | 1.030000 CPU seconds | n/a |
| python [arch_0000] (PID 46279) rss_mb | MB | 12 | 31.286 | 0.688 | 42.527 | 42.527 | n/a | n/a |
| python [arch_0000] (PID 46279) vms_mb | MB | 12 | 38.944 | 9.645 | 52.219 | 52.219 | n/a | n/a |
| docker (PID 46290) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 46290) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 46290) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 46290) rss_mb | MB | 2 | 25.379 | 25.379 | 25.379 | 25.379 | n/a | n/a |
| docker (PID 46290) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 46328) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 46328) rss_mb | MB | 5 | 3.072 | 0.633 | 12.828 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 46328) vms_mb | MB | 5 | 314.889 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 46350) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 46350) rss_mb | MB | 4 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [bake_0000] (PID 46350) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 46361) rss_mb | MB | 1 | 3.844 | 3.844 | 3.844 | 3.844 | n/a | n/a |
| docker (PID 46361) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 46388) rss_mb | MB | 1 | 16.062 | 16.062 | 16.062 | 16.062 | n/a | n/a |
| docker (PID 46388) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 46422) rss_mb | MB | 1 | 15.566 | 15.566 | 15.566 | 15.566 | n/a | n/a |
| docker (PID 46422) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 46459) rss_mb | MB | 1 | 25.984 | 25.984 | 25.984 | 25.984 | n/a | n/a |
| docker (PID 46459) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 46515) rss_mb | MB | 1 | 13.508 | 13.508 | 13.508 | 13.508 | n/a | n/a |
| docker (PID 46515) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 46533) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 46533) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 46533) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 46533) rss_mb | MB | 2 | 26.047 | 26.047 | 26.047 | 26.047 | n/a | n/a |
| docker (PID 46533) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 46599) rss_mb | MB | 1 | 4.219 | 4.219 | 4.219 | 4.219 | n/a | n/a |
| docker (PID 46599) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 46609) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 46609) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 46609) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 46609) rss_mb | MB | 2 | 26.930 | 26.930 | 26.930 | 26.930 | n/a | n/a |
| docker (PID 46609) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 46649) CPU | percent | 3 | 9.858 | 0.000 | 29.573 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 46649) rss_mb | MB | 4 | 3.313 | 0.633 | 11.355 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 46649) vms_mb | MB | 4 | 393.215 | 1.055 | 1569.695 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 46674) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 46674) rss_mb | MB | 3 | 1.586 | 1.586 | 1.586 | 1.586 | n/a | n/a |
| tail [arch_0000] (PID 46674) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 46712) rss_mb | MB | 1 | 10.297 | 10.297 | 10.297 | 10.297 | n/a | n/a |
| docker (PID 46712) vms_mb | MB | 1 | 1323.949 | 1323.949 | 1323.949 | 1323.949 | n/a | n/a |
| docker (PID 46747) rss_mb | MB | 1 | 27.328 | 27.328 | 27.328 | 27.328 | n/a | n/a |
| docker (PID 46747) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 46783) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 46783) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 46783) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 46783) rss_mb | MB | 2 | 27.102 | 27.102 | 27.102 | 27.102 | n/a | n/a |
| docker (PID 46783) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 46858) rss_mb | MB | 1 | 23.695 | 23.695 | 23.695 | 23.695 | n/a | n/a |
| docker (PID 46858) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 46884) rss_mb | MB | 1 | 0.410 | 0.410 | 0.410 | 0.410 | n/a | n/a |
| docker (PID 46884) vms_mb | MB | 1 | 30.570 | 30.570 | 30.570 | 30.570 | n/a | n/a |
| docker (PID 46900) CPU | percent | 55 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 46900) io read MB/s | MB/s | 55 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 46900) io write MB/s | MB/s | 55 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 46900) rss_mb | MB | 56 | 27.195 | 27.195 | 27.195 | 27.195 | n/a | n/a |
| docker (PID 46900) vms_mb | MB | 56 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 46908) rss_mb | MB | 1 | 8.148 | 8.148 | 8.148 | 8.148 | n/a | n/a |
| docker (PID 46908) vms_mb | MB | 1 | 32.867 | 32.867 | 32.867 | 32.867 | n/a | n/a |
| docker (PID 46924) rss_mb | MB | 1 | 25.961 | 25.961 | 25.961 | 25.961 | n/a | n/a |
| docker (PID 46924) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 46932) CPU | percent | 54 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 46932) io read MB/s | MB/s | 54 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 46932) io write MB/s | MB/s | 54 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 46932) rss_mb | MB | 55 | 26.680 | 26.680 | 26.680 | 26.680 | n/a | n/a |
| docker (PID 46932) vms_mb | MB | 55 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 46948) rss_mb | MB | 1 | 14.332 | 14.332 | 14.332 | 14.332 | n/a | n/a |
| docker (PID 46948) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 46972) rss_mb | MB | 1 | 25.387 | 25.387 | 25.387 | 25.387 | n/a | n/a |
| docker (PID 46972) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| python3 (PID 46993) CPU | percent | 8 | 68.549 | 29.573 | 107.840 | 107.840 | 0.560000 CPU seconds | n/a |
| python3 (PID 46993) io read MB/s | MB/s | 8 | 5.258 | 0.153 | 13.209 | 0.153 | 4.296875 MB | n/a |
| python3 (PID 46993) io write MB/s | MB/s | 8 | 0.244 | 0.000 | 1.953 | 1.953 | 0.199219 MB | n/a |
| python3 (PID 46993) rss_mb | MB | 9 | 24.304 | 10.191 | 34.141 | 34.141 | n/a | n/a |
| python3 (PID 46993) vms_mb | MB | 9 | 48.717 | 36.465 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 46998) rss_mb | MB | 1 | 26.754 | 26.754 | 26.754 | 26.754 | n/a | n/a |
| docker (PID 46998) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 47021) CPU | percent | 6 | 71.826 | 29.573 | 98.036 | 98.036 | 0.440000 CPU seconds | n/a |
| python3 (PID 47021) io read MB/s | MB/s | 6 | 2.861 | 0.153 | 4.537 | 0.153 | 1.753906 MB | n/a |
| python3 (PID 47021) io write MB/s | MB/s | 6 | 0.326 | 0.000 | 1.953 | 1.953 | 0.199219 MB | n/a |
| python3 (PID 47021) rss_mb | MB | 7 | 27.768 | 18.383 | 34.082 | 34.082 | n/a | n/a |
| python3 (PID 47021) vms_mb | MB | 7 | 51.605 | 42.703 | 57.453 | 57.453 | n/a | n/a |
| docker (PID 47039) rss_mb | MB | 1 | 14.504 | 14.504 | 14.504 | 14.504 | n/a | n/a |
| docker (PID 47039) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 47083) rss_mb | MB | 1 | 15.305 | 15.305 | 15.305 | 15.305 | n/a | n/a |
| docker (PID 47083) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 47109) CPU | percent | 3 | 3.260 | 0.000 | 9.779 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 47109) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 47109) io write MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 47109) rss_mb | MB | 4 | 27.171 | 26.711 | 27.324 | 27.324 | n/a | n/a |
| docker (PID 47109) vms_mb | MB | 4 | 1714.776 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [band_0000] (PID 47150) CPU | percent | 5 | 7.724 | 0.000 | 38.621 | 0.000 | 0.040000 CPU seconds | n/a |
| docker-init [band_0000] (PID 47150) rss_mb | MB | 6 | 4.464 | 0.633 | 13.059 | 0.633 | n/a | n/a |
| docker-init [band_0000] (PID 47150) vms_mb | MB | 6 | 524.023 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 47178) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 47178) rss_mb | MB | 4 | 1.555 | 1.555 | 1.555 | 1.555 | n/a | n/a |
| tail [band_0000] (PID 47178) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 47180) rss_mb | MB | 1 | 26.957 | 26.957 | 26.957 | 26.957 | n/a | n/a |
| docker (PID 47180) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] (PID 47199) rss_mb | MB | 1 | 12.617 | 12.617 | 12.617 | 12.617 | n/a | n/a |
| runc:[2:INIT] (PID 47199) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 47243) rss_mb | MB | 1 | 1.188 | 1.188 | 1.188 | 1.188 | n/a | n/a |
| docker (PID 47243) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 47280) rss_mb | MB | 1 | 26.289 | 26.289 | 26.289 | 26.289 | n/a | n/a |
| docker (PID 47280) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 47315) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 47315) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 47315) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 47315) rss_mb | MB | 2 | 26.922 | 26.922 | 26.922 | 26.922 | n/a | n/a |
| docker (PID 47315) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 47378) rss_mb | MB | 1 | 26.250 | 26.250 | 26.250 | 26.250 | n/a | n/a |
| docker (PID 47378) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 47386) rss_mb | MB | 1 | 25.699 | 25.699 | 25.699 | 25.699 | n/a | n/a |
| docker (PID 47386) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 47427) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 47427) rss_mb | MB | 6 | 2.564 | 0.633 | 12.219 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 47427) vms_mb | MB | 6 | 262.583 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 47450) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 47450) rss_mb | MB | 5 | 1.688 | 1.688 | 1.688 | 1.688 | n/a | n/a |
| tail [band_0000] (PID 47450) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 47452) rss_mb | MB | 1 | 26.664 | 26.664 | 26.664 | 26.664 | n/a | n/a |
| docker (PID 47452) vms_mb | MB | 1 | 1596.523 | 1596.523 | 1596.523 | 1596.523 | n/a | n/a |
| docker (PID 47504) CPU | percent | 3 | 6.370 | 0.000 | 19.111 | 0.000 | 0.020000 CPU seconds | n/a |
| docker (PID 47504) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 47504) io write MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 47504) rss_mb | MB | 4 | 21.871 | 6.281 | 27.211 | 27.211 | n/a | n/a |
| docker (PID 47504) vms_mb | MB | 4 | 1289.772 | 32.762 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 47505) rss_mb | MB | 1 | 8.844 | 8.844 | 8.844 | 8.844 | n/a | n/a |
| docker (PID 47505) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 47557) rss_mb | MB | 1 | 27.379 | 27.379 | 27.379 | 27.379 | n/a | n/a |
| docker (PID 47557) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker-init [bale_0000] (PID 47585) CPU | percent | 5 | 5.753 | 0.000 | 28.765 | 0.000 | 0.030000 CPU seconds | n/a |
| docker-init [bale_0000] (PID 47585) rss_mb | MB | 6 | 4.507 | 0.633 | 13.109 | 0.633 | n/a | n/a |
| docker-init [bale_0000] (PID 47585) vms_mb | MB | 6 | 524.023 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 47602) rss_mb | MB | 1 | 11.688 | 11.688 | 11.688 | 11.688 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 47602) vms_mb | MB | 1 | 1642.223 | 1642.223 | 1642.223 | 1642.223 | n/a | n/a |
| docker (PID 47617) rss_mb | MB | 1 | 26.527 | 26.527 | 26.527 | 26.527 | n/a | n/a |
| docker (PID 47617) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 47631) rss_mb | MB | 1 | 26.871 | 26.871 | 26.871 | 26.871 | n/a | n/a |
| docker (PID 47631) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| tail [bale_0000] (PID 47643) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 47643) rss_mb | MB | 4 | 1.801 | 1.801 | 1.801 | 1.801 | n/a | n/a |
| tail [bale_0000] (PID 47643) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 47652) rss_mb | MB | 1 | 27.426 | 27.426 | 27.426 | 27.426 | n/a | n/a |
| docker (PID 47652) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 47713) rss_mb | MB | 1 | 25.668 | 25.668 | 25.668 | 25.668 | n/a | n/a |
| docker (PID 47713) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 47725) rss_mb | MB | 1 | 3.523 | 3.523 | 3.523 | 3.523 | n/a | n/a |
| docker (PID 47725) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 47762) rss_mb | MB | 1 | 25.648 | 25.648 | 25.648 | 25.648 | n/a | n/a |
| docker (PID 47762) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 47797) rss_mb | MB | 1 | 26.961 | 26.961 | 26.961 | 26.961 | n/a | n/a |
| docker (PID 47797) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 47833) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 47833) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 47833) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 47833) rss_mb | MB | 2 | 26.031 | 26.031 | 26.031 | 26.031 | n/a | n/a |
| docker (PID 47833) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 47912) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 47912) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 47912) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 47912) rss_mb | MB | 2 | 26.844 | 26.844 | 26.844 | 26.844 | n/a | n/a |
| docker (PID 47912) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 47951) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 47951) rss_mb | MB | 4 | 3.670 | 0.633 | 12.781 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 47951) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 47974) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 47974) rss_mb | MB | 3 | 1.633 | 1.633 | 1.633 | 1.633 | n/a | n/a |
| tail [bale_0000] (PID 47974) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 47986) rss_mb | MB | 1 | 27.148 | 27.148 | 27.148 | 27.148 | n/a | n/a |
| docker (PID 47986) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 48076) rss_mb | MB | 1 | 26.613 | 26.613 | 26.613 | 26.613 | n/a | n/a |
| docker (PID 48076) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 48084) rss_mb | MB | 1 | 25.875 | 25.875 | 25.875 | 25.875 | n/a | n/a |
| docker (PID 48084) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 48182) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 48182) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48182) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48182) rss_mb | MB | 39 | 27.000 | 27.000 | 27.000 | 27.000 | n/a | n/a |
| docker (PID 48182) vms_mb | MB | 39 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 48232) rss_mb | MB | 1 | 24.027 | 24.027 | 24.027 | 24.027 | n/a | n/a |
| docker (PID 48232) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 48246) CPU | percent | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 48246) io read MB/s | MB/s | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48246) io write MB/s | MB/s | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48246) rss_mb | MB | 41 | 26.699 | 26.699 | 26.699 | 26.699 | n/a | n/a |
| docker (PID 48246) vms_mb | MB | 41 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 48254) rss_mb | MB | 1 | 23.145 | 23.145 | 23.145 | 23.145 | n/a | n/a |
| docker (PID 48254) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 48262) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 48262) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48262) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48262) rss_mb | MB | 2 | 26.715 | 26.715 | 26.715 | 26.715 | n/a | n/a |
| docker (PID 48262) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 48301) CPU | percent | 5 | 1.946 | 0.000 | 9.732 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 48301) rss_mb | MB | 6 | 2.689 | 0.633 | 12.973 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 48301) vms_mb | MB | 6 | 262.625 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 48326) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 48326) rss_mb | MB | 5 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [bale_0000] (PID 48326) vms_mb | MB | 5 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 48333) rss_mb | MB | 1 | 16.445 | 16.445 | 16.445 | 16.445 | n/a | n/a |
| docker (PID 48333) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 48341) rss_mb | MB | 1 | 27.121 | 27.121 | 27.121 | 27.121 | n/a | n/a |
| docker (PID 48341) vms_mb | MB | 1 | 1733.027 | 1733.027 | 1733.027 | 1733.027 | n/a | n/a |
| docker (PID 48371) rss_mb | MB | 1 | 25.883 | 25.883 | 25.883 | 25.883 | n/a | n/a |
| docker (PID 48371) vms_mb | MB | 1 | 1659.961 | 1659.961 | 1659.961 | 1659.961 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 48390) rss_mb | MB | 1 | 11.855 | 11.855 | 11.855 | 11.855 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 48390) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 48407) rss_mb | MB | 1 | 27.219 | 27.219 | 27.219 | 27.219 | n/a | n/a |
| docker (PID 48407) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 48426) rss_mb | MB | 1 | 10.645 | 10.645 | 10.645 | 10.645 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 48426) vms_mb | MB | 1 | 1497.320 | 1497.320 | 1497.320 | 1497.320 | n/a | n/a |
| docker (PID 48444) CPU | percent | 1 | 16.588 | 16.588 | 16.588 | 16.588 | 0.020000 CPU seconds | n/a |
| docker (PID 48444) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48444) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48444) rss_mb | MB | 2 | 18.037 | 8.891 | 27.184 | 27.184 | n/a | n/a |
| docker (PID 48444) vms_mb | MB | 2 | 1444.104 | 1227.434 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 48497) rss_mb | MB | 1 | 25.609 | 25.609 | 25.609 | 25.609 | n/a | n/a |
| docker (PID 48497) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 48520) rss_mb | MB | 1 | 25.328 | 25.328 | 25.328 | 25.328 | n/a | n/a |
| docker (PID 48520) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 48546) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 48546) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48546) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48546) rss_mb | MB | 2 | 27.000 | 27.000 | 27.000 | 27.000 | n/a | n/a |
| docker (PID 48546) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 48585) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 48585) rss_mb | MB | 38 | 0.948 | 0.633 | 12.598 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 48585) vms_mb | MB | 38 | 42.349 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 48610) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 48610) rss_mb | MB | 37 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [bale_0000] (PID 48610) vms_mb | MB | 37 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 48620) rss_mb | MB | 1 | 27.398 | 27.398 | 27.398 | 27.398 | n/a | n/a |
| docker (PID 48620) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 48648) CPU | percent | 34 | 0.576 | 0.000 | 19.572 | 0.000 | 0.020000 CPU seconds | n/a |
| docker (PID 48648) io read MB/s | MB/s | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48648) io write MB/s | MB/s | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48648) rss_mb | MB | 35 | 27.105 | 27.105 | 27.105 | 27.105 | n/a | n/a |
| docker (PID 48648) vms_mb | MB | 35 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [bale_0000] (PID 48667) CPU | percent | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bale_0000] (PID 48667) rss_mb | MB | 35 | 3.257 | 3.105 | 3.262 | 3.262 | n/a | n/a |
| bash [bale_0000] (PID 48667) vms_mb | MB | 35 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bale_0000] (PID 48677) CPU | percent | 33 | 99.803 | 97.628 | 107.976 | 97.986 | 3.360000 CPU seconds | n/a |
| python [bale_0000] (PID 48677) rss_mb | MB | 34 | 39.996 | 18.871 | 41.891 | 41.891 | n/a | n/a |
| python [bale_0000] (PID 48677) vms_mb | MB | 34 | 48.885 | 23.258 | 51.324 | 51.324 | n/a | n/a |
| docker (PID 48687) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 48687) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48687) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48687) rss_mb | MB | 2 | 25.840 | 25.840 | 25.840 | 25.840 | n/a | n/a |
| docker (PID 48687) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 48762) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 48762) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48762) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48762) rss_mb | MB | 2 | 25.375 | 25.375 | 25.375 | 25.375 | n/a | n/a |
| docker (PID 48762) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 48803) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 48803) rss_mb | MB | 4 | 3.739 | 0.633 | 13.059 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 48803) vms_mb | MB | 4 | 393.473 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 48826) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 48826) rss_mb | MB | 3 | 1.668 | 1.668 | 1.668 | 1.668 | n/a | n/a |
| tail [band_0000] (PID 48826) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 48838) rss_mb | MB | 1 | 27.285 | 27.285 | 27.285 | 27.285 | n/a | n/a |
| docker (PID 48838) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 48857) rss_mb | MB | 1 | 10.707 | 10.707 | 10.707 | 10.707 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 48857) vms_mb | MB | 1 | 1569.582 | 1569.582 | 1569.582 | 1569.582 | n/a | n/a |
| docker (PID 48891) rss_mb | MB | 1 | 22.207 | 22.207 | 22.207 | 22.207 | n/a | n/a |
| docker (PID 48891) vms_mb | MB | 1 | 1523.953 | 1523.953 | 1523.953 | 1523.953 | n/a | n/a |
| docker (PID 48936) rss_mb | MB | 1 | 18.387 | 18.387 | 18.387 | 18.387 | n/a | n/a |
| docker (PID 48936) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 48944) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 48944) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48944) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48944) rss_mb | MB | 2 | 25.422 | 25.422 | 25.422 | 25.422 | n/a | n/a |
| docker (PID 48944) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 48953) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 48953) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48953) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 48953) rss_mb | MB | 2 | 25.789 | 25.789 | 25.789 | 25.789 | n/a | n/a |
| docker (PID 48953) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 49000) CPU | percent | 4 | 4.639 | 0.000 | 18.555 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 49000) rss_mb | MB | 5 | 5.120 | 0.633 | 12.656 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 49000) vms_mb | MB | 5 | 628.517 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 49070) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 49070) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bale_0000] (PID 49070) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 49074) rss_mb | MB | 1 | 18.098 | 18.098 | 18.098 | 18.098 | n/a | n/a |
| docker (PID 49074) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 49108) rss_mb | MB | 1 | 27.469 | 27.469 | 27.469 | 27.469 | n/a | n/a |
| docker (PID 49108) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 49143) rss_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| docker (PID 49143) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 49164) rss_mb | MB | 1 | 11.375 | 11.375 | 11.375 | 11.375 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 49164) vms_mb | MB | 1 | 1569.969 | 1569.969 | 1569.969 | 1569.969 | n/a | n/a |
| docker (PID 49180) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 49180) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 49180) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 49180) rss_mb | MB | 2 | 25.965 | 25.965 | 25.965 | 25.965 | n/a | n/a |
| docker (PID 49180) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 49254) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 49254) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 49254) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 49254) rss_mb | MB | 2 | 25.801 | 25.801 | 25.801 | 25.801 | n/a | n/a |
| docker (PID 49254) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 49292) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 49292) rss_mb | MB | 11 | 1.737 | 0.633 | 12.781 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 49292) vms_mb | MB | 11 | 143.707 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 49320) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 49320) rss_mb | MB | 10 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [band_0000] (PID 49320) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 49331) rss_mb | MB | 1 | 26.980 | 26.980 | 26.980 | 26.980 | n/a | n/a |
| docker (PID 49331) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 49352) rss_mb | MB | 1 | 11.770 | 11.770 | 11.770 | 11.770 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 49352) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 49359) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 49359) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 49359) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 49359) rss_mb | MB | 8 | 27.316 | 27.316 | 27.316 | 27.316 | n/a | n/a |
| docker (PID 49359) vms_mb | MB | 8 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| bash [band_0000] (PID 49379) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [band_0000] (PID 49379) rss_mb | MB | 8 | 3.270 | 3.270 | 3.270 | 3.270 | n/a | n/a |
| bash [band_0000] (PID 49379) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [band_0000] (PID 49388) CPU | percent | 7 | 100.633 | 97.234 | 107.930 | 107.930 | 0.720000 CPU seconds | n/a |
| python [band_0000] (PID 49388) rss_mb | MB | 8 | 30.378 | 9.527 | 41.031 | 41.031 | n/a | n/a |
| python [band_0000] (PID 49388) vms_mb | MB | 8 | 37.663 | 13.531 | 51.324 | 51.324 | n/a | n/a |
| docker (PID 49390) rss_mb | MB | 1 | 19.934 | 19.934 | 19.934 | 19.934 | n/a | n/a |
| docker (PID 49390) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 49398) rss_mb | MB | 1 | 26.953 | 26.953 | 26.953 | 26.953 | n/a | n/a |
| docker (PID 49398) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 49452) rss_mb | MB | 1 | 0.559 | 0.559 | 0.559 | 0.559 | n/a | n/a |
| docker (PID 49452) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 49461) rss_mb | MB | 1 | 18.184 | 18.184 | 18.184 | 18.184 | n/a | n/a |
| docker (PID 49461) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 49485) rss_mb | MB | 1 | 25.152 | 25.152 | 25.152 | 25.152 | n/a | n/a |
| docker (PID 49485) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 49493) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 49493) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 49493) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 49493) rss_mb | MB | 39 | 25.301 | 25.301 | 25.301 | 25.301 | n/a | n/a |
| docker (PID 49493) vms_mb | MB | 39 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 49526) rss_mb | MB | 1 | 25.484 | 25.484 | 25.484 | 25.484 | n/a | n/a |
| docker (PID 49526) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| python3 (PID 49541) CPU | percent | 31 | 99.630 | 89.017 | 108.794 | 97.929 | 3.140000 CPU seconds | n/a |
| python3 (PID 49541) io read MB/s | MB/s | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 49541) io write MB/s | MB/s | 31 | 0.063 | 0.000 | 1.951 | 1.951 | 0.199219 MB | n/a |
| python3 (PID 49541) rss_mb | MB | 32 | 33.197 | 18.172 | 34.457 | 34.457 | n/a | n/a |
| python3 (PID 49541) vms_mb | MB | 32 | 56.686 | 42.570 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 49543) rss_mb | MB | 1 | 25.824 | 25.824 | 25.824 | 25.824 | n/a | n/a |
| docker (PID 49543) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 49569) rss_mb | MB | 1 | 0.559 | 0.559 | 0.559 | 0.559 | n/a | n/a |
| docker (PID 49569) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 49585) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 49585) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 49585) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 49585) rss_mb | MB | 39 | 25.668 | 25.668 | 25.668 | 25.668 | n/a | n/a |
| docker (PID 49585) vms_mb | MB | 39 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 49601) rss_mb | MB | 1 | 25.488 | 25.488 | 25.488 | 25.488 | n/a | n/a |
| docker (PID 49601) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 49625) rss_mb | MB | 1 | 23.070 | 23.070 | 23.070 | 23.070 | n/a | n/a |
| docker (PID 49625) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| python3 (PID 49632) CPU | percent | 2 | 103.737 | 98.654 | 108.821 | 108.821 | 0.210000 CPU seconds | n/a |
| python3 (PID 49632) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 49632) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 49632) rss_mb | MB | 3 | 27.849 | 21.215 | 33.883 | 33.883 | n/a | n/a |
| python3 (PID 49632) vms_mb | MB | 3 | 51.331 | 45.445 | 56.379 | 56.379 | n/a | n/a |
| docker (PID 49659) rss_mb | MB | 1 | 25.621 | 25.621 | 25.621 | 25.621 | n/a | n/a |
| docker (PID 49659) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 49692) rss_mb | MB | 1 | 9.582 | 9.582 | 9.582 | 9.582 | n/a | n/a |
| docker (PID 49692) vms_mb | MB | 1 | 1451.949 | 1451.949 | 1451.949 | 1451.949 | n/a | n/a |
| sandbox alex_0000 CPU | percent | 34 | 47.580 | 0.000 | 100.099 | 32.007 | 1.667218 CPU seconds | n/a |
| sandbox alex_0000 io read MB/s | MB/s | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox alex_0000 io write MB/s | MB/s | 39 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox alex_0000 memory | MB | 41 | 6.714 | 0.000 | 35.340 | 0.723 | n/a | n/a |
| sandbox alex_0000 net rx MB/s | MB/s | 34 | 51.314 | 0.000 | 1744.657 | 0.001 | 3531.773222 MB | n/a |
| sandbox alex_0000 net tx MB/s | MB/s | 35 | 0.302 | 0.000 | 10.555 | 0.000 | 21.366227 MB | n/a |
| sandbox andy_0000 CPU | percent | 27 | 48.204 | 2.911 | 100.707 | 30.948 | 1.343580 CPU seconds | n/a |
| sandbox andy_0000 io read MB/s | MB/s | 31 | 0.030 | 0.000 | 0.934 | 0.000 | 0.105469 MB | n/a |
| sandbox andy_0000 io write MB/s | MB/s | 31 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox andy_0000 memory | MB | 33 | 8.314 | 0.578 | 36.395 | 0.895 | n/a | n/a |
| sandbox andy_0000 net rx MB/s | MB/s | 27 | 0.001 | 0.000 | 0.002 | 0.000 | 0.001476 MB | n/a |
| sandbox andy_0000 net tx MB/s | MB/s | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000240 MB | n/a |
| sandbox arch_0000 CPU | percent | 29 | 51.931 | 3.297 | 101.514 | 30.216 | 1.592359 CPU seconds | n/a |
| sandbox arch_0000 io read MB/s | MB/s | 32 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox arch_0000 io write MB/s | MB/s | 32 | 0.497 | 0.000 | 15.853 | 0.000 | 1.625000 MB | n/a |
| sandbox arch_0000 memory | MB | 34 | 10.597 | 0.613 | 36.211 | 0.621 | n/a | n/a |
| sandbox arch_0000 net rx MB/s | MB/s | 29 | 0.000 | 0.000 | 0.003 | 0.000 | 0.001286 MB | n/a |
| sandbox arch_0000 net tx MB/s | MB/s | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000160 MB | n/a |
| sandbox bake_0000 CPU | percent | 30 | 48.035 | 0.000 | 106.365 | 34.232 | 1.536365 CPU seconds | n/a |
| sandbox bake_0000 io read MB/s | MB/s | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bake_0000 io write MB/s | MB/s | 34 | 0.112 | 0.000 | 3.779 | 0.000 | 0.425781 MB | n/a |
| sandbox bake_0000 memory | MB | 36 | 8.060 | 0.574 | 35.484 | 0.789 | n/a | n/a |
| sandbox bake_0000 net rx MB/s | MB/s | 31 | 0.000 | 0.000 | 0.002 | 0.000 | 0.001429 MB | n/a |
| sandbox bake_0000 net tx MB/s | MB/s | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000200 MB | n/a |
| sandbox bale_0000 CPU | percent | 50 | 77.905 | 3.202 | 101.106 | 42.912 | 3.986830 CPU seconds | n/a |
| sandbox bale_0000 io read MB/s | MB/s | 52 | 0.009 | 0.000 | 0.246 | 0.000 | 0.125000 MB | n/a |
| sandbox bale_0000 io write MB/s | MB/s | 53 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bale_0000 memory | MB | 55 | 21.584 | 0.578 | 35.703 | 3.859 | n/a | n/a |
| sandbox bale_0000 net rx MB/s | MB/s | 50 | 0.000 | 0.000 | 0.003 | 0.000 | 0.001570 MB | n/a |
| sandbox bale_0000 net tx MB/s | MB/s | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000200 MB | n/a |
| sandbox band_0000 CPU | percent | 20 | 57.293 | 9.223 | 100.113 | 84.182 | 1.175484 CPU seconds | n/a |
| sandbox band_0000 io read MB/s | MB/s | 21 | 0.011 | 0.000 | 0.192 | 0.000 | 0.023438 MB | n/a |
| sandbox band_0000 io write MB/s | MB/s | 23 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox band_0000 memory | MB | 24 | 9.878 | 0.621 | 34.836 | 3.816 | n/a | n/a |
| sandbox band_0000 net rx MB/s | MB/s | 20 | 0.000 | 0.000 | 0.002 | 0.000 | 0.000866 MB | n/a |
| sandbox band_0000 net tx MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 3048 | 55.271 | 0.579 | 194.371 | 68.540 | 171.293094 CPU seconds | n/a |
| workload total io read MB/s | MB/s | 216 | 0.075 | 0.000 | 10.667 | 0.000 | 1.734375 MB | n/a |
| workload total io write MB/s | MB/s | 218 | 0.091 | 0.000 | 15.853 | 0.000 | 2.066406 MB | n/a |
| workload total memory | MB | 3049 | 460.374 | 382.004 | 523.324 | 452.500 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
