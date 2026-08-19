# agprof summary

- Duration: **657.275 s**
- Runs: **24/24 completed**, 24 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.037 runs/s**
- LLM: **84 calls**, 84 succeeded, 0 failed, 0 interrupted, 0 retries, 447.784 s total wait
- Tools: **108/108 completed**, 6 failed, 0 interrupted
- Raw resource samples: **67048** at 9.873 Hz effective (10 Hz configured)
- GPU sampling: **unavailable** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 22678.258 / 42179.818 ms |
| LLM latency p50 / p95 | 3148.036 / 21846.539 ms |
| LLM TTFT p50 / p95 | 656.630 / 984.623 ms |
| LLM input / output tokens | 419355 / 22592 |
| LLM output throughput | 57.530 tokens/s |
| LLM attempts | 84 total, 84 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 408.436 / 1169.608 ms |

### Tool outcomes

| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 12/12 | 12 | 0 | 0 | 1148.709 ms | 2828.941 ms |
| edit | 12/12 | 12 | 0 | 0 | 417.067 ms | 767.236 ms |
| glob | 4/4 | 4 | 0 | 0 | 334.578 ms | 342.816 ms |
| grep | 1/1 | 1 | 0 | 0 | 335.931 ms | 335.931 ms |
| read | 37/37 | 37 | 0 | 0 | 417.610 ms | 590.697 ms |
| return_plan | 12/12 | 12 | 0 | 0 | 0.336 ms | 0.389 ms |
| return_status | 12/12 | 12 | 0 | 0 | 0.293 ms | 0.803 ms |
| return_summary | 18/18 | 12 | 6 | 0 | 0.360 ms | 0.443 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 16.048% | 114.196% | 106.378 s | 533.296 MB | 589.203 MB | 0.070312 MB | 0.046875 MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python3 | 72710 |  | 6489 | 3.627% | 129.808% | 24.350 s | 689.774 MB | 709.117 MB | 3734.129 MB | 3766.723 MB | 26.402344 MB | 34.863281 MB |
| git-remote-http | 72718 |  | 2 | 29.614% | 29.614% | 0.030 s | 18.777 MB | 18.980 MB | 107.066 MB | 107.566 MB | 0.140625 MB | 0.000000 MB |
| git | 72717 |  | 2 | 0.000% | 0.000% | 0.000 s | 3.230 MB | 3.230 MB | 11.273 MB | 11.273 MB | 0.000000 MB | 0.000000 MB |
| git | 72716 |  | 2 | 0.000% | 0.000% | 0.000 s | 4.695 MB | 4.695 MB | 12.516 MB | 12.516 MB | 0.000000 MB | 0.000000 MB |
| python3 | 72724 |  | 99 | 99.956% | 109.012% | 9.890 s | 33.718 MB | 34.090 MB | 57.037 MB | 57.375 MB | 0.000000 MB | 0.015625 MB |
| python3 | 72725 |  | 4 | 102.320% | 108.907% | 0.310 s | 28.780 MB | 34.906 MB | 52.128 MB | 57.500 MB | 0.000000 MB | 0.230469 MB |
| python3 | 72726 |  | 4 | 102.310% | 108.969% | 0.310 s | 27.200 MB | 36.488 MB | 50.938 MB | 59.516 MB | 0.000000 MB | 0.230469 MB |
| python3 | 72727 |  | 4 | 98.983% | 109.025% | 0.300 s | 29.114 MB | 34.918 MB | 52.204 MB | 57.508 MB | 0.000000 MB | 0.230469 MB |
| python3 | 72728 |  | 25 | 100.275% | 108.976% | 2.430 s | 32.980 MB | 34.941 MB | 56.360 MB | 57.512 MB | 0.000000 MB | 0.230469 MB |
| python3 | 72729 |  | 71 | 99.866% | 108.975% | 7.060 s | 41.409 MB | 47.824 MB | 64.059 MB | 69.633 MB | 0.000000 MB | 0.238281 MB |
| python3 | 72730 |  | 4 | 102.338% | 109.023% | 0.310 s | 25.850 MB | 34.816 MB | 49.733 MB | 57.508 MB | 0.000000 MB | 0.238281 MB |
| python3 | 72731 |  | 99 | 99.973% | 115.910% | 9.910 s | 34.069 MB | 34.254 MB | 57.283 MB | 57.457 MB | 0.000000 MB | 0.015625 MB |
| python3 | 72791 |  | 5 | 89.089% | 99.085% | 0.360 s | 27.260 MB | 34.922 MB | 50.789 MB | 57.492 MB | 0.910156 MB | 0.238281 MB |
| python3 | 72792 |  | 4 | 102.290% | 108.969% | 0.310 s | 26.701 MB | 34.789 MB | 50.436 MB | 57.508 MB | 0.000000 MB | 0.238281 MB |
| python3 | 72793 |  | 5 | 99.022% | 109.020% | 0.400 s | 25.652 MB | 34.805 MB | 49.815 MB | 57.457 MB | 0.000000 MB | 0.242188 MB |
| python3 | 72794 |  | 4 | 99.003% | 99.039% | 0.300 s | 25.851 MB | 34.699 MB | 49.987 MB | 57.508 MB | 0.000000 MB | 0.242188 MB |
| docker | 72798 |  | 2 | 9.896% | 9.896% | 0.010 s | 21.654 MB | 26.242 MB | 1588.361 MB | 1660.773 MB | 0.078125 MB | 0.000000 MB |
| docker-trust | 72806 |  | 1 | n/a% | n/a% | n/a s | 12.289 MB | 12.289 MB | 1212.965 MB | 1212.965 MB | n/a MB | n/a MB |
| docker | 72850 |  | 3 | 9.850% | 19.701% | 0.020 s | 27.158 MB | 27.551 MB | 1684.775 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 72891 | alex_0000 | 4 | 6.600% | 19.799% | 0.020 s | 3.486 MB | 12.047 MB | 375.347 MB | 1498.223 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 72924 |  | 1 | n/a% | n/a% | n/a s | 11.762 MB | 11.762 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| tail | 72902 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 72904 |  | 1 | n/a% | n/a% | n/a s | 27.137 MB | 27.137 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 72968 |  | 1 | n/a% | n/a% | n/a s | 2.539 MB | 2.539 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 73004 |  | 1 | n/a% | n/a% | n/a s | 27.062 MB | 27.062 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 73041 |  | 1 | n/a% | n/a% | n/a s | 26.730 MB | 26.730 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| docker | 73098 |  | 1 | n/a% | n/a% | n/a s | 25.859 MB | 25.859 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 73160 |  | 1 | n/a% | n/a% | n/a s | 2.797 MB | 2.797 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| tail | 73150 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.809 MB | 1.809 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 73136 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 73208 | alex_0000 | 1 | n/a% | n/a% | n/a s | 10.133 MB | 10.133 MB | 1569.195 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 73188 |  | 1 | n/a% | n/a% | n/a s | 27.301 MB | 27.301 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 73245 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.398 MB | 11.398 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 73224 |  | 1 | n/a% | n/a% | n/a s | 26.926 MB | 26.926 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 73261 |  | 1 | n/a% | n/a% | n/a s | 25.824 MB | 25.824 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 73320 |  | 2 | 9.909% | 9.909% | 0.010 s | 23.611 MB | 26.867 MB | 1588.486 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 73358 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 4.639 MB | 12.652 MB | 524.112 MB | 1570.227 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 73403 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.656 MB | 11.656 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 73372 | alex_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 73383 |  | 1 | n/a% | n/a% | n/a s | 27.242 MB | 27.242 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 73444 |  | 1 | n/a% | n/a% | n/a s | 19.699 MB | 19.699 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 73452 |  | 1 | n/a% | n/a% | n/a s | 26.098 MB | 26.098 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 73514 |  | 1 | n/a% | n/a% | n/a s | 26.930 MB | 26.930 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 73555 | alex_0000 | 4 | 6.540% | 19.619% | 0.020 s | 2.699 MB | 8.898 MB | 393.152 MB | 1569.445 MB | n/a MB | n/a MB |
| docker | 73578 |  | 1 | n/a% | n/a% | n/a s | 19.945 MB | 19.945 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 73568 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.664 MB | 1.664 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 73608 |  | 1 | n/a% | n/a% | n/a s | 27.238 MB | 27.238 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 73628 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.469 MB | 11.469 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 73644 |  | 1 | n/a% | n/a% | n/a s | 27.391 MB | 27.391 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 73664 | alex_0000 | 1 | n/a% | n/a% | n/a s | 12.113 MB | 12.113 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 73681 |  | 1 | n/a% | n/a% | n/a s | 26.918 MB | 26.918 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 73751 |  | 1 | n/a% | n/a% | n/a s | 25.852 MB | 25.852 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 73765 |  | 37 | 0.000% | 0.000% | 0.000 s | 25.652 MB | 25.652 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 73781 |  | 1 | n/a% | n/a% | n/a s | 1.613 MB | 1.613 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 73799 |  | 1 | n/a% | n/a% | n/a s | 9.285 MB | 9.285 MB | 1371.691 MB | 1371.691 MB | n/a MB | n/a MB |
| docker | 73808 |  | 1 | n/a% | n/a% | n/a s | 25.469 MB | 25.469 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 73847 | alex_0000 | 4 | 6.529% | 19.586% | 0.020 s | 3.312 MB | 11.352 MB | 393.154 MB | 1569.453 MB | n/a MB | n/a MB |
| docker | 73869 |  | 1 | n/a% | n/a% | n/a s | 27.062 MB | 27.062 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 73859 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 73916 | alex_0000 | 1 | n/a% | n/a% | n/a s | 12.285 MB | 12.285 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 73896 |  | 1 | n/a% | n/a% | n/a s | 27.426 MB | 27.426 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 73964 |  | 1 | n/a% | n/a% | n/a s | 1.633 MB | 1.633 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 73972 |  | 1 | n/a% | n/a% | n/a s | 25.977 MB | 25.977 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 74032 |  | 2 | 0.000% | 0.000% | 0.000 s | 24.898 MB | 25.719 MB | 1628.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 74076 | alex_0000 | 11 | 0.981% | 9.811% | 0.010 s | 1.737 MB | 12.781 MB | 143.707 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 74088 | alex_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 74118 | alex_0000 | 1 | n/a% | n/a% | n/a s | 10.781 MB | 10.781 MB | 1569.582 MB | 1569.582 MB | n/a MB | n/a MB |
| docker | 74099 |  | 1 | n/a% | n/a% | n/a s | 27.332 MB | 27.332 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| bash | 74145 | alex_0000 | 9 | 0.000% | 0.000% | 0.000 s | 3.445 MB | 3.445 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 74154 | alex_0000 | 8 | 99.445% | 107.982% | 0.710 s | 29.484 MB | 42.832 MB | 36.031 MB | 52.238 MB | n/a MB | n/a MB |
| docker | 74125 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.297 MB | 27.297 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 74165 |  | 1 | n/a% | n/a% | n/a s | 25.688 MB | 25.688 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 74223 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.484 MB | 26.484 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 74264 | alex_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.686 MB | 12.844 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 74276 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 74286 |  | 1 | n/a% | n/a% | n/a s | 27.160 MB | 27.160 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 74306 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.539 MB | 11.539 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 74351 |  | 1 | n/a% | n/a% | n/a s | 4.473 MB | 4.473 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 74388 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.816 MB | 25.816 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 74455 |  | 1 | n/a% | n/a% | n/a s | 6.090 MB | 6.090 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 74471 |  | 51 | 0.000% | 0.000% | 0.000 s | 26.328 MB | 26.328 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 74545 |  | 1 | n/a% | n/a% | n/a s | 25.223 MB | 25.223 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| python3 | 74569 |  | 4 | 102.135% | 108.733% | 0.310 s | 28.872 MB | 34.633 MB | 52.256 MB | 57.438 MB | 0.000000 MB | 0.207031 MB |
| docker | 74591 |  | 1 | n/a% | n/a% | n/a s | 26.023 MB | 26.023 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 74621 |  | 3 | 4.919% | 9.838% | 0.010 s | 27.276 MB | 27.520 MB | 1708.776 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 74660 | andy_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.747 MB | 13.090 MB | 393.473 MB | 1570.727 MB | n/a MB | n/a MB |
| tail | 74672 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 74701 |  | 1 | n/a% | n/a% | n/a s | 26.473 MB | 26.473 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 74737 |  | 1 | n/a% | n/a% | n/a s | 27.605 MB | 27.605 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 74772 |  | 1 | n/a% | n/a% | n/a s | 27.477 MB | 27.477 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 74792 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.820 MB | 11.820 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 74810 |  | 1 | n/a% | n/a% | n/a s | 27.125 MB | 27.125 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 74861 |  | 1 | n/a% | n/a% | n/a s | 26.871 MB | 26.871 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 74870 |  | 1 | n/a% | n/a% | n/a s | 25.344 MB | 25.344 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 74909 | andy_0000 | 4 | 3.285% | 9.856% | 0.010 s | 3.556 MB | 12.324 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 74932 |  | 1 | n/a% | n/a% | n/a s | 27.223 MB | 27.223 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 74922 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 74953 | andy_0000 | 1 | n/a% | n/a% | n/a s | 10.242 MB | 10.242 MB | 1641.199 MB | 1641.199 MB | n/a MB | n/a MB |
| docker | 75028 |  | 1 | n/a% | n/a% | n/a s | 19.363 MB | 19.363 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 75036 |  | 1 | n/a% | n/a% | n/a s | 26.645 MB | 26.645 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 75155 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.293 MB | 26.293 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 75195 | andy_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.678 MB | 12.812 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 75218 |  | 1 | n/a% | n/a% | n/a s | 27.301 MB | 27.301 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 75237 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.996 MB | 11.996 MB | 1498.223 MB | 1498.223 MB | n/a MB | n/a MB |
| tail | 75207 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.664 MB | 1.664 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 75280 |  | 1 | n/a% | n/a% | n/a s | 8.793 MB | 8.793 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 75317 |  | 2 | 9.778% | 9.778% | 0.010 s | 26.576 MB | 26.883 MB | 1660.648 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 75387 |  | 1 | n/a% | n/a% | n/a s | 26.871 MB | 26.871 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| docker | 75401 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.770 MB | 26.770 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 75444 |  | 1 | n/a% | n/a% | n/a s | 26.633 MB | 26.633 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 75499 |  | 1 | n/a% | n/a% | n/a s | 0.125 MB | 0.125 MB | 30.570 MB | 30.570 MB | n/a MB | n/a MB |
| docker-init | 75484 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 75497 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 75536 |  | 1 | n/a% | n/a% | n/a s | 20.125 MB | 20.125 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 75573 |  | 1 | n/a% | n/a% | n/a s | 27.242 MB | 27.242 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 75612 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.824 MB | 25.824 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 75671 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.941 MB | 26.941 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 75711 | andy_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.757 MB | 13.004 MB | 143.707 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 75723 | andy_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 75733 |  | 1 | n/a% | n/a% | n/a s | 27.188 MB | 27.188 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| python | 75791 | andy_0000 | 9 | 99.192% | 107.857% | 0.810 s | 32.240 MB | 42.902 MB | 39.469 MB | 52.238 MB | n/a MB | n/a MB |
| bash | 75781 | andy_0000 | 9 | 0.000% | 0.000% | 0.000 s | 3.449 MB | 3.449 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 75761 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.383 MB | 27.383 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 75801 |  | 1 | n/a% | n/a% | n/a s | 27.227 MB | 27.227 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 75913 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.016 MB | 27.016 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| tail | 75967 | andy_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 75953 | andy_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 76004 |  | 1 | n/a% | n/a% | n/a s | 18.961 MB | 18.961 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 76044 |  | 1 | n/a% | n/a% | n/a s | 27.227 MB | 27.227 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 76081 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.898 MB | 25.898 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 76173 |  | 39 | 0.000% | 0.000% | 0.000 s | 27.066 MB | 27.066 MB | 1661.023 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| docker | 76198 |  | 1 | n/a% | n/a% | n/a s | 21.750 MB | 21.750 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| python3 | 76223 |  | 4 | 102.194% | 108.911% | 0.310 s | 29.079 MB | 34.680 MB | 52.506 MB | 57.438 MB | 0.000000 MB | 0.226562 MB |
| docker | 76236 |  | 1 | n/a% | n/a% | n/a s | 11.164 MB | 11.164 MB | 1387.949 MB | 1387.949 MB | n/a MB | n/a MB |
| docker | 76275 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.398 MB | 27.398 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 76315 | arch_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.662 MB | 12.750 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 76359 |  | 1 | n/a% | n/a% | n/a s | 18.113 MB | 18.113 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 76327 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 76395 |  | 1 | n/a% | n/a% | n/a s | 26.992 MB | 26.992 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 76430 |  | 1 | n/a% | n/a% | n/a s | 27.246 MB | 27.246 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 76451 | arch_0000 | 1 | n/a% | n/a% | n/a s | 11.422 MB | 11.422 MB | 1570.098 MB | 1570.098 MB | n/a MB | n/a MB |
| docker | 76467 |  | 1 | n/a% | n/a% | n/a s | 26.945 MB | 26.945 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 76519 |  | 1 | n/a% | n/a% | n/a s | 15.664 MB | 15.664 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 76529 |  | 1 | n/a% | n/a% | n/a s | 26.805 MB | 26.805 MB | 1588.770 MB | 1588.770 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 76568 | arch_0000 | 4 | 9.804% | 29.412% | 0.030 s | 3.463 MB | 11.953 MB | 393.315 MB | 1570.098 MB | n/a MB | n/a MB |
| docker | 76593 |  | 1 | n/a% | n/a% | n/a s | 27.195 MB | 27.195 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 76580 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| run4:diagnose_b | 76646 |  | 1 | n/a% | n/a% | n/a s | 682.520 MB | 682.520 MB | 3752.562 MB | 3752.562 MB | n/a MB | n/a MB |
| docker | 76683 |  | 1 | n/a% | n/a% | n/a s | 11.211 MB | 11.211 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 76692 |  | 1 | n/a% | n/a% | n/a s | 25.938 MB | 25.938 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 76767 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.848 MB | 26.848 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 76783 |  | 1 | n/a% | n/a% | n/a s | 25.621 MB | 25.621 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 76809 |  | 1 | n/a% | n/a% | n/a s | 25.535 MB | 25.535 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker-init | 76849 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.566 MB | 0.566 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 76861 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 76897 |  | 1 | n/a% | n/a% | n/a s | 23.000 MB | 23.000 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 76933 |  | 1 | n/a% | n/a% | n/a s | 27.230 MB | 27.230 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 76972 |  | 1 | n/a% | n/a% | n/a s | 26.152 MB | 26.152 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 77013 |  | 1 | n/a% | n/a% | n/a s | 23.227 MB | 23.227 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 77030 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.016 MB | 27.016 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 77071 | arch_0000 | 10 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 77083 | arch_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 77119 |  | 9 | 1.216% | 9.731% | 0.010 s | 26.320 MB | 27.477 MB | 1644.682 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| bash | 77139 | arch_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.395 MB | 3.395 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 77148 | arch_0000 | 8 | 100.806% | 107.891% | 0.720 s | 31.622 MB | 41.559 MB | 38.696 MB | 51.219 MB | n/a MB | n/a MB |
| docker | 77158 |  | 1 | n/a% | n/a% | n/a s | 26.688 MB | 26.688 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 77198 |  | 1 | n/a% | n/a% | n/a s | 3.879 MB | 3.879 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 77254 | arch_0000 | 4 | 6.514% | 19.542% | 0.020 s | 3.195 MB | 10.883 MB | 393.090 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 77216 |  | 1 | n/a% | n/a% | n/a s | 27.004 MB | 27.004 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 77277 |  | 1 | n/a% | n/a% | n/a s | 24.195 MB | 24.195 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 77267 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 77325 | arch_0000 | 1 | n/a% | n/a% | n/a s | 11.852 MB | 11.852 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 77304 |  | 1 | n/a% | n/a% | n/a s | 27.320 MB | 27.320 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 77341 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 77376 |  | 1 | n/a% | n/a% | n/a s | 25.941 MB | 25.941 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 77453 |  | 1 | n/a% | n/a% | n/a s | 25.828 MB | 25.828 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 77461 |  | 39 | 0.000% | 0.000% | 0.000 s | 26.965 MB | 26.965 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 77494 |  | 1 | n/a% | n/a% | n/a s | 22.961 MB | 22.961 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| python3 | 77509 |  | 4 | 98.803% | 98.899% | 0.300 s | 25.103 MB | 34.363 MB | 49.563 MB | 57.438 MB | 0.000000 MB | 0.226562 MB |
| docker | 77540 |  | 1 | n/a% | n/a% | n/a s | 7.680 MB | 7.680 MB | 32.867 MB | 32.867 MB | n/a MB | n/a MB |
| docker | 77548 |  | 1 | n/a% | n/a% | n/a s | 26.352 MB | 26.352 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 77562 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.391 MB | 27.391 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 77601 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.749 MB | 13.098 MB | 393.473 MB | 1570.727 MB | n/a MB | n/a MB |
| tail | 77614 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 77645 |  | 1 | n/a% | n/a% | n/a s | 19.871 MB | 19.871 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 77680 |  | 1 | n/a% | n/a% | n/a s | 27.480 MB | 27.480 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 77738 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.387 MB | 11.387 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 77716 |  | 1 | n/a% | n/a% | n/a s | 26.949 MB | 26.949 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 77754 |  | 1 | n/a% | n/a% | n/a s | 26.195 MB | 26.195 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 77804 |  | 1 | n/a% | n/a% | n/a s | 21.504 MB | 21.504 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 77813 |  | 1 | n/a% | n/a% | n/a s | 25.605 MB | 25.605 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 77852 | bake_0000 | 4 | 6.482% | 19.445% | 0.020 s | 3.571 MB | 12.387 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 77875 |  | 1 | n/a% | n/a% | n/a s | 27.434 MB | 27.434 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 77865 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.695 MB | 1.695 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 77902 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 77966 |  | 1 | n/a% | n/a% | n/a s | 17.344 MB | 17.344 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 77974 |  | 1 | n/a% | n/a% | n/a s | 25.691 MB | 25.691 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 78027 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.738 MB | 26.738 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 78065 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.623 MB | 12.594 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 78080 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 78110 | bake_0000 | 1 | n/a% | n/a% | n/a s | 12.422 MB | 12.422 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 78090 |  | 1 | n/a% | n/a% | n/a s | 26.984 MB | 26.984 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 78155 |  | 1 | n/a% | n/a% | n/a s | 18.230 MB | 18.230 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 78190 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.020 MB | 27.020 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 78250 |  | 1 | n/a% | n/a% | n/a s | 14.324 MB | 14.324 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 78272 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.277 MB | 26.277 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 78288 |  | 1 | n/a% | n/a% | n/a s | 26.664 MB | 26.664 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 78315 |  | 4 | 6.565% | 19.694% | 0.020 s | 20.448 MB | 27.078 MB | 1253.771 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 78353 | bake_0000 | 10 | 4.167% | 37.500% | 0.040 s | 1.757 MB | 11.875 MB | 165.183 MB | 1642.336 MB | n/a MB | n/a MB |
| tail | 78367 | bake_0000 | 9 | 0.000% | 0.000% | 0.000 s | 1.472 MB | 1.641 MB | 2.706 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 78378 |  | 3 | 28.814% | 57.628% | 0.060 s | 18.667 MB | 26.969 MB | 1118.103 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 78397 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.891 MB | 11.891 MB | 1642.730 MB | 1642.730 MB | n/a MB | n/a MB |
| docker | 78405 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.199 MB | 27.199 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 78424 | bake_0000 | 1 | n/a% | n/a% | n/a s | 12.137 MB | 12.137 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 78441 |  | 2 | 67.171% | 67.171% | 0.070 s | 20.867 MB | 26.863 MB | 1588.361 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 78462 | bake_0000 | 1 | n/a% | n/a% | n/a s | 10.680 MB | 10.680 MB | 1569.582 MB | 1569.582 MB | n/a MB | n/a MB |
| docker | 78480 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.262 MB | 27.262 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 78530 |  | 1 | n/a% | n/a% | n/a s | 10.746 MB | 10.746 MB | 1451.949 MB | 1451.949 MB | n/a MB | n/a MB |
| docker | 78538 |  | 1 | n/a% | n/a% | n/a s | 25.750 MB | 25.750 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 78578 | bake_0000 | 11 | 2.928% | 29.280% | 0.030 s | 1.611 MB | 11.391 MB | 143.647 MB | 1569.574 MB | n/a MB | n/a MB |
| docker | 78602 |  | 1 | n/a% | n/a% | n/a s | 19.363 MB | 19.363 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| tail | 78592 | bake_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 78628 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.461 MB | 27.461 MB | 1661.023 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 78648 | bake_0000 | 8 | 2.796% | 19.574% | 0.020 s | 4.435 MB | 11.770 MB | 200.135 MB | 1570.348 MB | n/a MB | n/a MB |
| python | 78657 | bake_0000 | 7 | 99.663% | 107.825% | 0.610 s | 32.056 MB | 41.000 MB | 38.799 MB | 50.375 MB | n/a MB | n/a MB |
| docker | 78667 |  | 1 | n/a% | n/a% | n/a s | 25.828 MB | 25.828 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 78728 |  | 1 | n/a% | n/a% | n/a s | 26.887 MB | 26.887 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker-init | 78770 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 78781 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.809 MB | 1.809 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 78820 |  | 1 | n/a% | n/a% | n/a s | 24.055 MB | 24.055 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 78856 |  | 1 | n/a% | n/a% | n/a s | 27.266 MB | 27.266 MB | 1733.027 MB | 1733.027 MB | n/a MB | n/a MB |
| docker | 78893 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.992 MB | 25.992 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 78971 |  | 1 | n/a% | n/a% | n/a s | 16.297 MB | 16.297 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 78979 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.852 MB | 25.852 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 79004 |  | 1 | n/a% | n/a% | n/a s | 23.922 MB | 23.922 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| python3 | 79027 |  | 3 | 103.695% | 108.772% | 0.210 s | 27.737 MB | 33.676 MB | 51.315 MB | 56.461 MB | 0.000000 MB | 0.000000 MB |
| docker | 79056 |  | 1 | n/a% | n/a% | n/a s | 25.332 MB | 25.332 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 79064 |  | 1 | n/a% | n/a% | n/a s | 22.535 MB | 22.535 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 79078 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.953 MB | 27.953 MB | 1804.781 MB | 1804.781 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 79120 | bale_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.773 MB | 13.195 MB | 393.473 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 79165 |  | 1 | n/a% | n/a% | n/a s | 4.711 MB | 4.711 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| tail | 79132 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 79200 |  | 1 | n/a% | n/a% | n/a s | 27.297 MB | 27.297 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 79256 | bale_0000 | 1 | n/a% | n/a% | n/a s | 10.582 MB | 10.582 MB | 1569.453 MB | 1569.453 MB | n/a MB | n/a MB |
| docker | 79236 |  | 1 | n/a% | n/a% | n/a s | 27.402 MB | 27.402 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 79273 |  | 1 | n/a% | n/a% | n/a s | 27.137 MB | 27.137 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 79323 |  | 1 | n/a% | n/a% | n/a s | 10.766 MB | 10.766 MB | 1387.949 MB | 1387.949 MB | n/a MB | n/a MB |
| docker | 79331 |  | 1 | n/a% | n/a% | n/a s | 27.102 MB | 27.102 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 79371 | bale_0000 | 4 | 3.251% | 9.753% | 0.010 s | 3.440 MB | 11.863 MB | 393.283 MB | 1569.969 MB | n/a MB | n/a MB |
| docker | 79394 |  | 1 | n/a% | n/a% | n/a s | 27.207 MB | 27.207 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 79383 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 79424 |  | 1 | n/a% | n/a% | n/a s | 27.453 MB | 27.453 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 79488 |  | 1 | n/a% | n/a% | n/a s | 15.574 MB | 15.574 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 79497 |  | 1 | n/a% | n/a% | n/a s | 26.012 MB | 26.012 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 79582 |  | 37 | 0.000% | 0.000% | 0.000 s | 25.535 MB | 25.535 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 79598 |  | 1 | n/a% | n/a% | n/a s | 10.984 MB | 10.984 MB | 1451.949 MB | 1451.949 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 79663 | bale_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.502 MB | 12.109 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 79624 |  | 1 | n/a% | n/a% | n/a s | 26.742 MB | 26.742 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 79701 | bale_0000 | 1 | n/a% | n/a% | n/a s | 1.996 MB | 1.996 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| tail | 79675 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 79685 |  | 1 | n/a% | n/a% | n/a s | 27.219 MB | 27.219 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 79745 |  | 1 | n/a% | n/a% | n/a s | 0.547 MB | 0.547 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 79782 |  | 1 | n/a% | n/a% | n/a s | 23.930 MB | 23.930 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 79791 |  | 1 | n/a% | n/a% | n/a s | 25.812 MB | 25.812 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 79846 |  | 1 | n/a% | n/a% | n/a s | 27.062 MB | 27.062 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 79900 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker-init | 79886 | bale_0000 | 37 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 79898 | bale_0000 | 37 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 79938 |  | 35 | 0.000% | 0.000% | 0.000 s | 27.078 MB | 27.078 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[0:PARENT] | 79954 | bale_0000 | 1 | n/a% | n/a% | n/a s | 1.934 MB | 1.934 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| python | 79967 | bale_0000 | 34 | 100.146% | 108.039% | 3.370 s | 39.068 MB | 41.047 MB | 47.867 MB | 50.594 MB | n/a MB | n/a MB |
| bash | 79958 | bale_0000 | 34 | 0.000% | 0.000% | 0.000 s | 3.387 MB | 3.387 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 79977 |  | 1 | n/a% | n/a% | n/a s | 26.047 MB | 26.047 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 80063 |  | 1 | n/a% | n/a% | n/a s | 27.016 MB | 27.016 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 80072 |  | 47 | 0.000% | 0.000% | 0.000 s | 26.977 MB | 26.977 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 80104 |  | 1 | n/a% | n/a% | n/a s | 26.785 MB | 26.785 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| python3 | 80120 |  | 25 | 100.120% | 108.770% | 2.430 s | 32.844 MB | 34.789 MB | 56.325 MB | 57.457 MB | 0.000000 MB | 0.226562 MB |
| docker | 80149 |  | 1 | n/a% | n/a% | n/a s | 20.609 MB | 20.609 MB | 1524.203 MB | 1524.203 MB | n/a MB | n/a MB |
| docker | 80171 |  | 3 | 9.857% | 19.714% | 0.020 s | 17.776 MB | 27.480 MB | 1131.017 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| tail | 80224 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 80212 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 80262 |  | 1 | n/a% | n/a% | n/a s | 25.387 MB | 25.387 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 80288 |  | 1 | n/a% | n/a% | n/a s | 27.508 MB | 27.508 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 80307 | band_0000 | 1 | n/a% | n/a% | n/a s | 11.941 MB | 11.941 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 80363 |  | 1 | n/a% | n/a% | n/a s | 26.844 MB | 26.844 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 80420 |  | 1 | n/a% | n/a% | n/a s | 26.496 MB | 26.496 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 80460 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.525 MB | 12.203 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 80472 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.699 MB | 1.699 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 80502 | band_0000 | 1 | n/a% | n/a% | n/a s | 10.871 MB | 10.871 MB | 1569.711 MB | 1569.711 MB | n/a MB | n/a MB |
| docker | 80482 |  | 1 | n/a% | n/a% | n/a s | 27.309 MB | 27.309 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 80538 |  | 1 | n/a% | n/a% | n/a s | 23.594 MB | 23.594 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 80584 |  | 2 | 0.000% | 0.000% | 0.000 s | 16.199 MB | 25.883 MB | 846.486 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 80653 |  | 1 | n/a% | n/a% | n/a s | 26.594 MB | 26.594 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 80667 |  | 37 | 0.000% | 0.000% | 0.000 s | 27.008 MB | 27.008 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 80683 |  | 1 | n/a% | n/a% | n/a s | 0.414 MB | 0.414 MB | 30.578 MB | 30.578 MB | n/a MB | n/a MB |
| docker | 80711 |  | 1 | n/a% | n/a% | n/a s | 25.344 MB | 25.344 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 80765 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 80767 |  | 1 | n/a% | n/a% | n/a s | 23.422 MB | 23.422 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker-init | 80753 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 80802 |  | 1 | n/a% | n/a% | n/a s | 26.809 MB | 26.809 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 80860 | band_0000 | 1 | n/a% | n/a% | n/a s | 10.309 MB | 10.309 MB | 1641.449 MB | 1641.449 MB | n/a MB | n/a MB |
| docker | 80840 |  | 1 | n/a% | n/a% | n/a s | 27.129 MB | 27.129 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 80880 |  | 1 | n/a% | n/a% | n/a s | 25.824 MB | 25.824 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 80922 |  | 1 | n/a% | n/a% | n/a s | 23.555 MB | 23.555 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 80940 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.562 MB | 26.562 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 80979 | band_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.755 MB | 12.977 MB | 150.275 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 81002 |  | 1 | n/a% | n/a% | n/a s | 27.258 MB | 27.258 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 80992 | band_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 81022 | band_0000 | 1 | n/a% | n/a% | n/a s | 12.301 MB | 12.301 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 81030 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.695 MB | 27.695 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| bash | 81050 | band_0000 | 9 | 0.000% | 0.000% | 0.000 s | 3.473 MB | 3.473 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 81060 | band_0000 | 8 | 100.699% | 107.814% | 0.720 s | 30.746 MB | 41.957 MB | 37.783 MB | 51.324 MB | n/a MB | n/a MB |
| docker | 81070 |  | 1 | n/a% | n/a% | n/a s | 26.863 MB | 26.863 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 81116 |  | 1 | n/a% | n/a% | n/a s | 20.320 MB | 20.320 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 81149 |  | 40 | 0.000% | 0.000% | 0.000 s | 25.174 MB | 25.605 MB | 1619.527 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 81181 |  | 1 | n/a% | n/a% | n/a s | 2.793 MB | 2.793 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| python3 | 81197 |  | 4 | 98.838% | 98.995% | 0.300 s | 23.988 MB | 34.426 MB | 48.287 MB | 57.438 MB | 0.000000 MB | 0.222656 MB |
| docker | 81210 |  | 1 | n/a% | n/a% | n/a s | 23.754 MB | 23.754 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 81250 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.943 MB | 27.184 MB | 1696.775 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 81291 | bart_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 81304 | bart_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 81307 |  | 1 | n/a% | n/a% | n/a s | 18.414 MB | 18.414 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 81342 |  | 1 | n/a% | n/a% | n/a s | 27.254 MB | 27.254 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 81431 |  | 1 | n/a% | n/a% | n/a s | 21.090 MB | 21.090 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 81439 |  | 1 | n/a% | n/a% | n/a s | 27.188 MB | 27.188 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 81497 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.684 MB | 25.684 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 81536 | bart_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.749 MB | 13.098 MB | 393.473 MB | 1570.727 MB | n/a MB | n/a MB |
| tail | 81549 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 81580 | bart_0000 | 1 | n/a% | n/a% | n/a s | 11.781 MB | 11.781 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 81561 |  | 1 | n/a% | n/a% | n/a s | 27.312 MB | 27.312 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 81623 |  | 1 | n/a% | n/a% | n/a s | 3.484 MB | 3.484 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 81661 |  | 2 | 9.797% | 9.797% | 0.010 s | 26.145 MB | 27.094 MB | 1660.492 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 81719 |  | 2 | 0.000% | 0.000% | 0.000 s | 24.752 MB | 25.855 MB | 1624.207 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 81759 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 4.673 MB | 12.754 MB | 524.112 MB | 1570.227 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 81801 | bart_0000 | 1 | n/a% | n/a% | n/a s | 11.816 MB | 11.816 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 81771 | bart_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 81782 |  | 1 | n/a% | n/a% | n/a s | 27.324 MB | 27.324 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 81842 |  | 1 | n/a% | n/a% | n/a s | 15.203 MB | 15.203 MB | 1451.699 MB | 1451.699 MB | n/a MB | n/a MB |
| docker | 81850 |  | 1 | n/a% | n/a% | n/a s | 26.000 MB | 26.000 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 81909 |  | 1 | n/a% | n/a% | n/a s | 27.094 MB | 27.094 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 81947 | bart_0000 | 3 | 9.563% | 19.126% | 0.020 s | 3.008 MB | 7.758 MB | 523.852 MB | 1569.445 MB | n/a MB | n/a MB |
| docker | 81970 |  | 1 | n/a% | n/a% | n/a s | 17.613 MB | 17.613 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 81960 | bart_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 81998 |  | 1 | n/a% | n/a% | n/a s | 27.430 MB | 27.430 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 82018 | bart_0000 | 1 | n/a% | n/a% | n/a s | 11.453 MB | 11.453 MB | 1498.094 MB | 1498.094 MB | n/a MB | n/a MB |
| docker | 82040 |  | 1 | n/a% | n/a% | n/a s | 26.969 MB | 26.969 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 82085 |  | 1 | n/a% | n/a% | n/a s | 17.238 MB | 17.238 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 82102 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.820 MB | 25.820 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 82141 | bart_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.655 MB | 12.723 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 82183 | bart_0000 | 1 | n/a% | n/a% | n/a s | 10.906 MB | 10.906 MB | 1569.582 MB | 1569.582 MB | n/a MB | n/a MB |
| docker | 82164 |  | 1 | n/a% | n/a% | n/a s | 27.395 MB | 27.395 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 82154 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 82218 |  | 1 | n/a% | n/a% | n/a s | 19.504 MB | 19.504 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 82264 |  | 2 | 0.000% | 0.000% | 0.000 s | 17.598 MB | 25.953 MB | 1552.078 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 82331 |  | 1 | n/a% | n/a% | n/a s | 27.043 MB | 27.043 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 82345 |  | 37 | 0.000% | 0.000% | 0.000 s | 26.566 MB | 26.566 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 82363 |  | 1 | n/a% | n/a% | n/a s | 16.289 MB | 16.289 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 82391 |  | 1 | n/a% | n/a% | n/a s | 25.699 MB | 25.699 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 82445 |  | 1 | n/a% | n/a% | n/a s | 23.586 MB | 23.586 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| tail | 82443 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 82430 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 82499 | bart_0000 | 1 | n/a% | n/a% | n/a s | 5.258 MB | 5.258 MB | 1441.445 MB | 1441.445 MB | n/a MB | n/a MB |
| docker | 82480 |  | 1 | n/a% | n/a% | n/a s | 27.273 MB | 27.273 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 82515 |  | 1 | n/a% | n/a% | n/a s | 27.430 MB | 27.430 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 82534 | bart_0000 | 1 | n/a% | n/a% | n/a s | 11.410 MB | 11.410 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 82553 |  | 1 | n/a% | n/a% | n/a s | 26.840 MB | 26.840 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 82613 |  | 1 | n/a% | n/a% | n/a s | 25.820 MB | 25.820 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker-init | 82652 | bart_0000 | 10 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 82664 | bart_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 82702 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.141 MB | 27.141 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 82722 | bart_0000 | 9 | 2.431% | 19.445% | 0.020 s | 4.256 MB | 11.020 MB | 178.328 MB | 1569.824 MB | n/a MB | n/a MB |
| python | 82731 | bart_0000 | 8 | 100.810% | 107.857% | 0.720 s | 32.823 MB | 42.055 MB | 40.093 MB | 52.289 MB | n/a MB | n/a MB |
| docker | 82741 |  | 1 | n/a% | n/a% | n/a s | 26.758 MB | 26.758 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 82786 |  | 1 | n/a% | n/a% | n/a s | 17.211 MB | 17.211 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 82795 |  | 1 | n/a% | n/a% | n/a s | 17.949 MB | 17.949 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 82804 |  | 1 | n/a% | n/a% | n/a s | 27.031 MB | 27.031 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 82844 | bart_0000 | 4 | 6.533% | 19.599% | 0.020 s | 3.598 MB | 12.492 MB | 411.474 MB | 1642.730 MB | n/a MB | n/a MB |
| tail | 82857 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 82867 |  | 1 | n/a% | n/a% | n/a s | 27.562 MB | 27.562 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 82896 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 82958 |  | 1 | n/a% | n/a% | n/a s | 25.656 MB | 25.656 MB | 1587.957 MB | 1587.957 MB | n/a MB | n/a MB |
| docker | 82966 |  | 1 | n/a% | n/a% | n/a s | 27.125 MB | 27.125 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 83029 |  | 1 | n/a% | n/a% | n/a s | 16.590 MB | 16.590 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 83048 |  | 1 | n/a% | n/a% | n/a s | 5.668 MB | 5.668 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 83064 |  | 40 | 0.000% | 0.000% | 0.000 s | 25.730 MB | 25.730 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 83100 |  | 1 | n/a% | n/a% | n/a s | 25.465 MB | 25.465 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| python3 | 83115 |  | 4 | 98.795% | 108.846% | 0.300 s | 25.901 MB | 34.402 MB | 50.062 MB | 57.457 MB | 0.000000 MB | 0.222656 MB |
| docker | 83168 |  | 2 | 19.772% | 19.772% | 0.020 s | 27.037 MB | 27.430 MB | 1696.775 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| tail | 83222 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.707 MB | 1.707 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 83225 |  | 1 | n/a% | n/a% | n/a s | 15.582 MB | 15.582 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker-init | 83210 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 83261 |  | 1 | n/a% | n/a% | n/a s | 27.316 MB | 27.316 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 83288 |  | 1 | n/a% | n/a% | n/a s | 27.355 MB | 27.355 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| sh | 83307 | base_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.516 MB | 0.516 MB | n/a MB | n/a MB |
| docker | 83352 |  | 1 | n/a% | n/a% | n/a s | 15.301 MB | 15.301 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 83360 |  | 1 | n/a% | n/a% | n/a s | 25.738 MB | 25.738 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 83418 |  | 2 | 9.848% | 9.848% | 0.010 s | 24.646 MB | 26.605 MB | 1624.488 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 83458 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.729 MB | 13.016 MB | 411.411 MB | 1642.480 MB | n/a MB | n/a MB |
| tail | 83471 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 83484 |  | 1 | n/a% | n/a% | n/a s | 27.418 MB | 27.418 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 83504 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.395 MB | 11.395 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 83537 |  | 1 | n/a% | n/a% | n/a s | 24.266 MB | 24.266 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 83582 |  | 2 | 0.000% | 0.000% | 0.000 s | 23.469 MB | 25.961 MB | 1624.207 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 83652 |  | 1 | n/a% | n/a% | n/a s | 8.957 MB | 8.957 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 83666 |  | 38 | 0.000% | 0.000% | 0.000 s | 25.746 MB | 25.746 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 83682 |  | 1 | n/a% | n/a% | n/a s | 25.746 MB | 25.746 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 83709 |  | 2 | 9.844% | 9.844% | 0.010 s | 23.572 MB | 26.879 MB | 1624.488 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 83748 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.745 MB | 13.082 MB | 393.473 MB | 1570.727 MB | n/a MB | n/a MB |
| tail | 83760 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 83770 |  | 1 | n/a% | n/a% | n/a s | 27.207 MB | 27.207 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 83790 | base_0000 | 1 | n/a% | n/a% | n/a s | 10.918 MB | 10.918 MB | 1569.703 MB | 1569.703 MB | n/a MB | n/a MB |
| docker | 83830 |  | 1 | n/a% | n/a% | n/a s | 5.531 MB | 5.531 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 83870 |  | 1 | n/a% | n/a% | n/a s | 15.680 MB | 15.680 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 83878 |  | 1 | n/a% | n/a% | n/a s | 25.734 MB | 25.734 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 83936 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.641 MB | 26.641 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 83977 | base_0000 | 19 | 0.000% | 0.000% | 0.000 s | 1.281 MB | 12.953 MB | 83.656 MB | 1570.477 MB | n/a MB | n/a MB |
| run15:repair_bu | 84027 |  | 17 | 1.222% | 19.547% | 0.020 s | 66.564 MB | 695.520 MB | 1784.357 MB | 3757.691 MB | 0.000000 MB | 0.000000 MB |
| tail | 83990 | base_0000 | 18 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| bash | 84046 | base_0000 | 16 | 0.000% | 0.000% | 0.000 s | 3.332 MB | 3.332 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 84055 | base_0000 | 16 | 99.687% | 107.862% | 1.540 s | 35.749 MB | 41.695 MB | 44.238 MB | 51.027 MB | n/a MB | n/a MB |
| docker | 84065 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.938 MB | 25.938 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 84116 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 30.570 MB | 30.570 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 84165 | base_0000 | 4 | 9.637% | 28.912% | 0.030 s | 3.272 MB | 11.191 MB | 393.152 MB | 1569.445 MB | n/a MB | n/a MB |
| docker | 84124 |  | 1 | n/a% | n/a% | n/a s | 25.465 MB | 25.465 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 84188 |  | 1 | n/a% | n/a% | n/a s | 25.375 MB | 25.375 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 84177 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 84234 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.773 MB | 11.773 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 84214 |  | 1 | n/a% | n/a% | n/a s | 27.367 MB | 27.367 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 84287 |  | 1 | n/a% | n/a% | n/a s | 25.961 MB | 25.961 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 84380 |  | 40 | 0.000% | 0.000% | 0.000 s | 25.083 MB | 25.324 MB | 1656.598 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 84414 |  | 1 | n/a% | n/a% | n/a s | 26.703 MB | 26.703 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 84429 |  | 4 | 102.047% | 108.701% | 0.310 s | 26.223 MB | 34.523 MB | 50.372 MB | 57.441 MB | 0.000000 MB | 0.207031 MB |
| docker | 84450 |  | 1 | n/a% | n/a% | n/a s | 6.574 MB | 6.574 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 84466 |  | 1 | n/a% | n/a% | n/a s | 25.719 MB | 25.719 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 84480 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.023 MB | 27.023 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 84521 | beam_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.657 MB | 12.730 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 84563 |  | 1 | n/a% | n/a% | n/a s | 26.000 MB | 26.000 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| tail | 84533 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 84596 |  | 1 | n/a% | n/a% | n/a s | 27.301 MB | 27.301 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 84649 | beam_0000 | 1 | n/a% | n/a% | n/a s | 11.867 MB | 11.867 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 84629 |  | 1 | n/a% | n/a% | n/a s | 27.387 MB | 27.387 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 84666 |  | 1 | n/a% | n/a% | n/a s | 26.789 MB | 26.789 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 84716 |  | 1 | n/a% | n/a% | n/a s | 26.102 MB | 26.102 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 84762 | beam_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.557 MB | 12.328 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 84724 |  | 1 | n/a% | n/a% | n/a s | 25.512 MB | 25.512 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 84787 |  | 1 | n/a% | n/a% | n/a s | 27.430 MB | 27.430 MB | 1733.027 MB | 1733.027 MB | n/a MB | n/a MB |
| tail | 84776 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 84881 |  | 1 | n/a% | n/a% | n/a s | 19.836 MB | 19.836 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 84890 |  | 1 | n/a% | n/a% | n/a s | 26.289 MB | 26.289 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 84959 |  | 1 | n/a% | n/a% | n/a s | 1.070 MB | 1.070 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 84975 |  | 37 | 0.000% | 0.000% | 0.000 s | 26.543 MB | 26.543 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 84991 |  | 1 | n/a% | n/a% | n/a s | 26.824 MB | 26.824 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 85017 |  | 2 | 0.000% | 0.000% | 0.000 s | 12.857 MB | 25.301 MB | 809.393 MB | 1588.207 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 85055 | beam_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.583 MB | 12.434 MB | 393.473 MB | 1570.727 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 85099 | beam_0000 | 1 | n/a% | n/a% | n/a s | 10.953 MB | 10.953 MB | 1641.578 MB | 1641.578 MB | n/a MB | n/a MB |
| tail | 85067 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 85079 |  | 1 | n/a% | n/a% | n/a s | 27.641 MB | 27.641 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 85137 |  | 1 | n/a% | n/a% | n/a s | 9.242 MB | 9.242 MB | 1243.691 MB | 1243.691 MB | n/a MB | n/a MB |
| docker | 85177 |  | 1 | n/a% | n/a% | n/a s | 25.629 MB | 25.629 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 85186 |  | 1 | n/a% | n/a% | n/a s | 26.082 MB | 26.082 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 85245 |  | 1 | n/a% | n/a% | n/a s | 25.438 MB | 25.438 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 85285 | beam_0000 | 11 | 1.951% | 19.514% | 0.020 s | 1.574 MB | 10.984 MB | 143.636 MB | 1569.445 MB | n/a MB | n/a MB |
| docker | 85308 |  | 1 | n/a% | n/a% | n/a s | 24.969 MB | 24.969 MB | 1659.961 MB | 1659.961 MB | n/a MB | n/a MB |
| tail | 85297 | beam_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.801 MB | 1.801 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 85334 |  | 9 | 0.000% | 0.000% | 0.000 s | 24.139 MB | 27.156 MB | 1476.243 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 85354 | beam_0000 | 8 | 1.398% | 9.783% | 0.010 s | 4.540 MB | 11.957 MB | 209.214 MB | 1642.980 MB | n/a MB | n/a MB |
| python | 85364 | beam_0000 | 7 | 101.318% | 108.024% | 0.620 s | 32.141 MB | 42.578 MB | 39.160 MB | 52.238 MB | n/a MB | n/a MB |
| docker | 85374 |  | 1 | n/a% | n/a% | n/a s | 25.910 MB | 25.910 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 85432 |  | 1 | n/a% | n/a% | n/a s | 26.992 MB | 26.992 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 85483 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 85471 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 85538 | beam_0000 | 1 | n/a% | n/a% | n/a s | 1.969 MB | 1.969 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 85539 | beam_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 85521 |  | 1 | n/a% | n/a% | n/a s | 27.438 MB | 27.438 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 85555 |  | 1 | n/a% | n/a% | n/a s | 27.348 MB | 27.348 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 85575 | beam_0000 | 1 | n/a% | n/a% | n/a s | 11.770 MB | 11.770 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 85592 |  | 1 | n/a% | n/a% | n/a s | 25.906 MB | 25.906 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 85661 |  | 1 | n/a% | n/a% | n/a s | 25.773 MB | 25.773 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 85677 |  | 39 | 0.000% | 0.000% | 0.000 s | 26.812 MB | 26.812 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 85701 |  | 1 | n/a% | n/a% | n/a s | 26.859 MB | 26.859 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 85724 |  | 3 | 98.741% | 98.922% | 0.200 s | 28.033 MB | 33.914 MB | 51.760 MB | 57.461 MB | 0.000000 MB | 0.000000 MB |
| docker | 85737 |  | 1 | n/a% | n/a% | n/a s | 26.188 MB | 26.188 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 85753 |  | 1 | n/a% | n/a% | n/a s | 26.941 MB | 26.941 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 85776 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.241 MB | 27.738 MB | 1708.609 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 85818 | bear_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.653 MB | 12.715 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 85862 |  | 1 | n/a% | n/a% | n/a s | 8.676 MB | 8.676 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| tail | 85830 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 85897 |  | 1 | n/a% | n/a% | n/a s | 27.426 MB | 27.426 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 85950 | bear_0000 | 1 | n/a% | n/a% | n/a s | 10.914 MB | 10.914 MB | 1641.707 MB | 1641.707 MB | n/a MB | n/a MB |
| docker | 85932 |  | 1 | n/a% | n/a% | n/a s | 27.559 MB | 27.559 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 85967 |  | 1 | n/a% | n/a% | n/a s | 27.133 MB | 27.133 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 86017 |  | 1 | n/a% | n/a% | n/a s | 13.012 MB | 13.012 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 86025 |  | 1 | n/a% | n/a% | n/a s | 25.371 MB | 25.371 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 86068 | bear_0000 | 4 | 6.501% | 19.503% | 0.020 s | 3.521 MB | 12.387 MB | 393.408 MB | 1570.469 MB | n/a MB | n/a MB |
| docker | 86090 |  | 1 | n/a% | n/a% | n/a s | 27.246 MB | 27.246 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 86080 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 86139 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.703 MB | 11.703 MB | 1498.223 MB | 1498.223 MB | n/a MB | n/a MB |
| docker | 86119 |  | 1 | n/a% | n/a% | n/a s | 27.422 MB | 27.422 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 86153 |  | 1 | n/a% | n/a% | n/a s | 27.195 MB | 27.195 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| sh | 86173 | bear_0000 | 1 | n/a% | n/a% | n/a s | 1.676 MB | 1.676 MB | 2.617 MB | 2.617 MB | n/a MB | n/a MB |
| docker | 86190 |  | 1 | n/a% | n/a% | n/a s | 26.215 MB | 26.215 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 86249 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.473 MB | 25.473 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 86288 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 4.790 MB | 13.105 MB | 548.197 MB | 1642.480 MB | n/a MB | n/a MB |
| tail | 86303 | bear_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 86313 |  | 1 | n/a% | n/a% | n/a s | 27.246 MB | 27.246 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 86376 |  | 1 | n/a% | n/a% | n/a s | 19.770 MB | 19.770 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 86384 |  | 1 | n/a% | n/a% | n/a s | 25.875 MB | 25.875 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 86433 |  | 1 | n/a% | n/a% | n/a s | 1.637 MB | 1.637 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 86441 |  | 1 | n/a% | n/a% | n/a s | 26.859 MB | 26.859 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 86481 | bear_0000 | 3 | 9.755% | 19.510% | 0.020 s | 2.993 MB | 7.715 MB | 523.768 MB | 1569.195 MB | n/a MB | n/a MB |
| tail | 86494 | bear_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.574 MB | 1.574 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 86505 |  | 1 | n/a% | n/a% | n/a s | 1.938 MB | 1.938 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 86551 | bear_0000 | 1 | n/a% | n/a% | n/a s | 10.781 MB | 10.781 MB | 1569.711 MB | 1569.711 MB | n/a MB | n/a MB |
| docker | 86532 |  | 1 | n/a% | n/a% | n/a s | 27.340 MB | 27.340 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 86574 |  | 1 | n/a% | n/a% | n/a s | 26.918 MB | 26.918 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 86616 |  | 1 | n/a% | n/a% | n/a s | 26.469 MB | 26.469 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 86633 |  | 1 | n/a% | n/a% | n/a s | 26.695 MB | 26.695 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 86696 |  | 1 | n/a% | n/a% | n/a s | 1.051 MB | 1.051 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| tail | 86685 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.730 MB | 1.730 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 86672 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 86743 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.059 MB | 11.059 MB | 1641.836 MB | 1641.836 MB | n/a MB | n/a MB |
| docker | 86724 |  | 1 | n/a% | n/a% | n/a s | 27.168 MB | 27.168 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 86759 |  | 1 | n/a% | n/a% | n/a s | 27.301 MB | 27.301 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 86777 | bear_0000 | 1 | n/a% | n/a% | n/a s | 12.176 MB | 12.176 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 86793 |  | 1 | n/a% | n/a% | n/a s | 26.766 MB | 26.766 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 86843 |  | 1 | n/a% | n/a% | n/a s | 23.023 MB | 23.023 MB | 1524.203 MB | 1524.203 MB | n/a MB | n/a MB |
| docker | 86873 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.922 MB | 26.922 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 86889 |  | 1 | n/a% | n/a% | n/a s | 25.852 MB | 25.852 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 86956 | bear_0000 | 4 | 3.257% | 9.770% | 0.010 s | 3.496 MB | 12.086 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 86917 |  | 1 | n/a% | n/a% | n/a s | 27.000 MB | 27.000 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 86968 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 86994 | bear_0000 | 1 | n/a% | n/a% | n/a s | 1.996 MB | 1.996 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 86978 |  | 1 | n/a% | n/a% | n/a s | 27.184 MB | 27.184 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 87072 |  | 1 | n/a% | n/a% | n/a s | 21.703 MB | 21.703 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 87080 |  | 1 | n/a% | n/a% | n/a s | 25.977 MB | 25.977 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 87138 |  | 1 | n/a% | n/a% | n/a s | 25.535 MB | 25.535 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 87192 | bear_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 87179 | bear_0000 | 10 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 87194 |  | 1 | n/a% | n/a% | n/a s | 18.629 MB | 18.629 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 87231 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.336 MB | 27.336 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 87260 | bear_0000 | 7 | 102.836% | 117.623% | 0.630 s | 31.502 MB | 41.043 MB | 38.301 MB | 51.340 MB | n/a MB | n/a MB |
| bash | 87251 | bear_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.422 MB | 3.422 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 87270 |  | 1 | n/a% | n/a% | n/a s | 26.160 MB | 26.160 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 87329 |  | 1 | n/a% | n/a% | n/a s | 11.285 MB | 11.285 MB | 1451.699 MB | 1451.699 MB | n/a MB | n/a MB |
| docker | 87338 |  | 1 | n/a% | n/a% | n/a s | 20.195 MB | 20.195 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 87362 |  | 40 | 0.000% | 0.000% | 0.000 s | 26.668 MB | 26.668 MB | 1588.770 MB | 1588.770 MB | 0.000000 MB | 0.000000 MB |
| docker | 87386 |  | 1 | n/a% | n/a% | n/a s | 21.551 MB | 21.551 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| python3 | 87409 |  | 11 | 100.308% | 108.035% | 1.030 s | 27.554 MB | 34.531 MB | 51.275 MB | 57.434 MB | 0.000000 MB | 0.222656 MB |
| docker | 87430 |  | 1 | n/a% | n/a% | n/a s | 26.004 MB | 26.004 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 87446 |  | 1 | n/a% | n/a% | n/a s | 16.395 MB | 16.395 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 87461 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.357 MB | 27.602 MB | 1696.775 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 87501 | beef_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.128 MB | 13.109 MB | 314.989 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 87519 |  | 1 | n/a% | n/a% | n/a s | 27.137 MB | 27.137 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 87516 | beef_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 87538 |  | 1 | n/a% | n/a% | n/a s | 11.645 MB | 11.645 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 87616 |  | 1 | n/a% | n/a% | n/a s | 26.254 MB | 26.254 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 87651 |  | 1 | n/a% | n/a% | n/a s | 26.934 MB | 26.934 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 87693 |  | 1 | n/a% | n/a% | n/a s | 18.234 MB | 18.234 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 87749 | beef_0000 | 4 | 9.623% | 28.868% | 0.030 s | 0.641 MB | 0.664 MB | 4.318 MB | 14.109 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 87744 | beef_0000 | 1 | n/a% | n/a% | n/a s | 1.961 MB | 1.961 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 87709 |  | 1 | n/a% | n/a% | n/a s | 26.945 MB | 26.945 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 87761 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 87772 |  | 1 | n/a% | n/a% | n/a s | 16.512 MB | 16.512 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 87801 |  | 1 | n/a% | n/a% | n/a s | 27.414 MB | 27.414 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 87820 | beef_0000 | 1 | n/a% | n/a% | n/a s | 11.824 MB | 11.824 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 87836 |  | 1 | n/a% | n/a% | n/a s | 27.430 MB | 27.430 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 87856 | beef_0000 | 1 | n/a% | n/a% | n/a s | 11.738 MB | 11.738 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 87873 |  | 1 | n/a% | n/a% | n/a s | 26.926 MB | 26.926 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 87934 |  | 1 | n/a% | n/a% | n/a s | 16.270 MB | 16.270 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 87957 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.746 MB | 26.746 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 88041 | beef_0000 | 4 | 9.720% | 29.160% | 0.030 s | 3.309 MB | 11.336 MB | 393.215 MB | 1569.695 MB | n/a MB | n/a MB |
| docker | 88000 |  | 1 | n/a% | n/a% | n/a s | 25.516 MB | 25.516 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 88055 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 88066 |  | 1 | n/a% | n/a% | n/a s | 25.520 MB | 25.520 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 88115 | beef_0000 | 1 | n/a% | n/a% | n/a s | 11.664 MB | 11.664 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 88096 |  | 1 | n/a% | n/a% | n/a s | 27.336 MB | 27.336 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| sh | 88153 | beef_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 88131 |  | 1 | n/a% | n/a% | n/a s | 27.176 MB | 27.176 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 88171 |  | 1 | n/a% | n/a% | n/a s | 26.805 MB | 26.805 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 88230 |  | 2 | 0.000% | 0.000% | 0.000 s | 23.307 MB | 26.918 MB | 1588.486 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 88268 | beef_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.741 MB | 12.820 MB | 143.707 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 88281 | beef_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 88310 | beef_0000 | 1 | n/a% | n/a% | n/a s | 11.664 MB | 11.664 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 88291 |  | 1 | n/a% | n/a% | n/a s | 27.289 MB | 27.289 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| python | 88346 | beef_0000 | 8 | 100.631% | 107.905% | 0.720 s | 30.545 MB | 41.719 MB | 37.918 MB | 51.238 MB | n/a MB | n/a MB |
| docker | 88318 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.258 MB | 27.258 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| bash | 88337 | beef_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.410 MB | 3.410 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 88358 |  | 2 | 9.684% | 9.684% | 0.010 s | 23.395 MB | 26.930 MB | 1588.361 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 88419 |  | 1 | n/a% | n/a% | n/a s | 26.801 MB | 26.801 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| 6 | 88453 | beef_0000 | 1 | n/a% | n/a% | n/a s | 1.785 MB | 1.785 MB | 13.980 MB | 13.980 MB | n/a MB | n/a MB |
| tail | 88471 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 88473 |  | 1 | n/a% | n/a% | n/a s | 23.168 MB | 23.168 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker-init | 88458 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 88508 |  | 1 | n/a% | n/a% | n/a s | 26.945 MB | 26.945 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 88564 | beef_0000 | 1 | n/a% | n/a% | n/a s | 11.762 MB | 11.762 MB | 1570.348 MB | 1570.348 MB | n/a MB | n/a MB |
| docker | 88544 |  | 1 | n/a% | n/a% | n/a s | 26.953 MB | 26.953 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 88580 |  | 1 | n/a% | n/a% | n/a s | 26.605 MB | 26.605 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 88624 |  | 1 | n/a% | n/a% | n/a s | 25.637 MB | 25.637 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 88657 |  | 1 | n/a% | n/a% | n/a s | 25.719 MB | 25.719 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 88665 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.504 MB | 25.504 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 88698 |  | 1 | n/a% | n/a% | n/a s | 25.520 MB | 25.520 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| python3 | 88713 |  | 4 | 102.128% | 108.811% | 0.310 s | 26.693 MB | 34.438 MB | 50.429 MB | 57.438 MB | 0.000000 MB | 0.222656 MB |
| docker | 88743 |  | 1 | n/a% | n/a% | n/a s | 13.797 MB | 13.797 MB | 1451.699 MB | 1451.699 MB | n/a MB | n/a MB |
| docker | 88765 |  | 3 | 9.867% | 19.733% | 0.020 s | 27.286 MB | 27.406 MB | 1708.776 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| tail | 88817 | bell_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 88804 | bell_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 88858 |  | 1 | n/a% | n/a% | n/a s | 3.488 MB | 3.488 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 88886 |  | 1 | n/a% | n/a% | n/a s | 27.242 MB | 27.242 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 88907 | bell_0000 | 1 | n/a% | n/a% | n/a s | 4.371 MB | 4.371 MB | 1224.934 MB | 1224.934 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 88943 | bell_0000 | 1 | n/a% | n/a% | n/a s | 11.410 MB | 11.410 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 88922 |  | 1 | n/a% | n/a% | n/a s | 27.387 MB | 27.387 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 88959 |  | 1 | n/a% | n/a% | n/a s | 26.035 MB | 26.035 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 89057 | bell_0000 | 4 | 6.429% | 19.286% | 0.020 s | 3.178 MB | 10.812 MB | 393.090 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 89019 |  | 1 | n/a% | n/a% | n/a s | 25.246 MB | 25.246 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 89083 |  | 1 | n/a% | n/a% | n/a s | 25.699 MB | 25.699 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 89073 | bell_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 89131 | bell_0000 | 1 | n/a% | n/a% | n/a s | 11.336 MB | 11.336 MB | 1570.098 MB | 1570.098 MB | n/a MB | n/a MB |
| docker | 89111 |  | 1 | n/a% | n/a% | n/a s | 27.293 MB | 27.293 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 89147 |  | 1 | n/a% | n/a% | n/a s | 27.457 MB | 27.457 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| sh | 89166 | bell_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.516 MB | 0.516 MB | n/a MB | n/a MB |
| docker | 89182 |  | 1 | n/a% | n/a% | n/a s | 26.031 MB | 26.031 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 89262 |  | 37 | 0.000% | 0.000% | 0.000 s | 26.855 MB | 26.855 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 89278 |  | 1 | n/a% | n/a% | n/a s | 17.395 MB | 17.395 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 89298 |  | 1 | n/a% | n/a% | n/a s | 26.727 MB | 26.727 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 89345 | bell_0000 | 4 | 3.259% | 9.778% | 0.010 s | 3.558 MB | 12.332 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 89306 |  | 1 | n/a% | n/a% | n/a s | 25.742 MB | 25.742 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 89370 |  | 1 | n/a% | n/a% | n/a s | 27.500 MB | 27.500 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 89360 | bell_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 89463 |  | 1 | n/a% | n/a% | n/a s | 15.883 MB | 15.883 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 89471 |  | 1 | n/a% | n/a% | n/a s | 25.652 MB | 25.652 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 89533 |  | 1 | n/a% | n/a% | n/a s | 25.715 MB | 25.715 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 89586 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| tail | 89584 | bell_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.809 MB | 1.809 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 89571 | bell_0000 | 11 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 89620 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.477 MB | 27.477 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 89640 | bell_0000 | 9 | 2.408% | 19.263% | 0.020 s | 4.126 MB | 10.039 MB | 170.257 MB | 1497.191 MB | n/a MB | n/a MB |
| python | 89648 | bell_0000 | 8 | 99.286% | 107.899% | 0.710 s | 32.335 MB | 41.750 MB | 39.348 MB | 51.238 MB | n/a MB | n/a MB |
| docker | 89660 |  | 2 | 9.613% | 9.613% | 0.010 s | 23.520 MB | 26.750 MB | 1624.488 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 89747 |  | 1 | n/a% | n/a% | n/a s | 26.918 MB | 26.918 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 89755 |  | 39 | 0.000% | 0.000% | 0.000 s | 26.695 MB | 26.695 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 89789 |  | 1 | n/a% | n/a% | n/a s | 26.574 MB | 26.574 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 89804 |  | 4 | 102.029% | 108.711% | 0.310 s | 25.315 MB | 34.527 MB | 49.604 MB | 57.438 MB | 0.000000 MB | 0.222656 MB |
| docker | 89823 |  | 1 | n/a% | n/a% | n/a s | 27.051 MB | 27.051 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |

## GPU metrics

_No GPU samples were collected._

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| alex_0000 | 58.256% | 100.193% | 1.427 s | 8.172 MB | 36.145 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| andy_0000 | 59.211% | 100.108% | 1.333 s | 9.676 MB | 36.375 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| arch_0000 | 63.329% | 100.019% | 1.166 s | 10.113 MB | 35.305 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bake_0000 | 52.078% | 100.082% | 1.504 s | 7.135 MB | 34.535 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bale_0000 | 87.896% | 101.144% | 3.857 s | 24.215 MB | 34.582 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| band_0000 | 68.190% | 100.969% | 1.186 s | 11.975 MB | 35.500 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bart_0000 | 55.838% | 100.116% | 1.489 s | 7.954 MB | 35.258 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| base_0000 | 71.422% | 101.962% | 2.132 s | 15.081 MB | 35.223 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| beam_0000 | 63.294% | 100.250% | 1.230 s | 9.418 MB | 36.434 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bear_0000 | 59.902% | 112.720% | 1.366 s | 8.923 MB | 34.652 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| beef_0000 | 60.200% | 100.043% | 1.294 s | 9.186 MB | 35.570 MB | 0.000000 MB | 0.003906 MB | 3546.975211 MB | 30.661978 MB |
| bell_0000 | 66.762% | 101.022% | 1.233 s | 10.977 MB | 35.375 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |

## Incomplete spans

_No spans were still open when profiling stopped._

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sync:result_wait | 24/24 | 0 | 0 | 602.837 | 0.006 | 602.830 | 25118.198 | 22677.896 | 42179.907 |
| turn | 84/84 | 0 | 0 | 502.815 | 2.544 | 500.231 | 5985.893 | 3949.524 | 21869.163 |
| llm:attempt | 84/84 | 0 | 0 | 447.784 | 2.071 | 445.690 | 5330.764 | 3148.036 | 21846.539 |
| run:diagnose_bug | 12/12 | 0 | 0 | 364.915 | 1.466 | 363.420 | 30409.551 | 28282.017 | 43421.009 |
| llm:diagnose_bug | 34/34 | 0 | 0 | 295.195 | 1.178 | 294.000 | 8682.198 | 3167.404 | 25221.841 |
| run:repair_bug | 12/12 | 0 | 0 | 237.933 | 1.207 | 236.713 | 19827.772 | 19368.502 | 23582.049 |
| llm:repair_bug | 50/50 | 0 | 0 | 152.611 | 0.914 | 151.691 | 3052.217 | 3148.275 | 5124.635 |
| teardown:commit | 24/24 | 0 | 0 | 99.752 | 0.061 | 99.690 | 4156.313 | 4088.979 | 4876.526 |
| sandbox:commit | 24/24 | 0 | 0 | 99.233 | 0.046 | 99.186 | 4134.727 | 4064.129 | 4852.313 |
| capstone:plan:bucketsort | 1/1 | 0 | 0 | 43.978 | 0.002 | 43.977 | 43978.408 | 43978.408 | 43978.408 |
| capstone:plan:find_first_in_sorted | 1/1 | 0 | 0 | 42.966 | 0.001 | 42.965 | 42965.640 | 42965.640 | 42965.640 |
| capstone:plan:next_palindrome | 1/1 | 0 | 0 | 37.739 | 0.001 | 37.738 | 37738.810 | 37738.810 | 37738.810 |
| capstone:plan:mergesort | 1/1 | 0 | 0 | 33.964 | 0.001 | 33.964 | 33964.229 | 33964.229 | 33964.229 |
| tool_dispatch:repair_bug | 50/50 | 0 | 0 | 33.107 | 0.203 | 32.897 | 662.147 | 590.199 | 1392.297 |
| capstone:plan:bitcount | 1/1 | 0 | 0 | 33.032 | 0.001 | 33.031 | 33031.551 | 33031.551 | 33031.551 |
| capstone:plan:powerset | 1/1 | 0 | 0 | 29.340 | 0.001 | 29.339 | 29339.869 | 29339.869 | 29339.869 |
| capstone:plan:flatten | 1/1 | 0 | 0 | 27.224 | 0.001 | 27.224 | 27224.488 | 27224.488 | 27224.488 |
| capstone:plan:gcd | 1/1 | 0 | 0 | 25.789 | 0.001 | 25.788 | 25788.596 | 25788.596 | 25788.596 |
| capstone:plan:hanoi | 1/1 | 0 | 0 | 24.936 | 0.001 | 24.935 | 24935.621 | 24935.621 | 24935.621 |
| capstone:build:bucketsort | 1/1 | 0 | 0 | 24.441 | 0.001 | 24.440 | 24440.817 | 24440.817 | 24440.817 |
| capstone:plan:levenshtein | 1/1 | 0 | 0 | 23.377 | 0.001 | 23.377 | 23377.413 | 23377.413 | 23377.413 |
| capstone:build:find_first_in_sorted | 1/1 | 0 | 0 | 22.880 | 0.001 | 22.879 | 22879.622 | 22879.622 | 22879.622 |
| capstone:build:levenshtein | 1/1 | 0 | 0 | 22.477 | 0.000 | 22.476 | 22477.103 | 22477.103 | 22477.103 |
| tool_dispatch:diagnose_bug | 34/34 | 0 | 0 | 21.853 | 0.200 | 21.643 | 642.728 | 546.763 | 1362.143 |
| capstone:plan:rpn_eval | 1/1 | 0 | 0 | 21.667 | 0.001 | 21.666 | 21666.818 | 21666.818 | 21666.818 |
| capstone:build:next_palindrome | 1/1 | 0 | 0 | 21.381 | 0.000 | 21.381 | 21381.062 | 21381.062 | 21381.062 |
| capstone:plan:is_valid_parenthesization | 1/1 | 0 | 0 | 20.913 | 0.001 | 20.912 | 20912.559 | 20912.559 | 20912.559 |
| capstone:build:flatten | 1/1 | 0 | 0 | 20.137 | 0.001 | 20.137 | 20137.212 | 20137.212 | 20137.212 |
| capstone:build:mergesort | 1/1 | 0 | 0 | 20.027 | 0.001 | 20.026 | 20026.717 | 20026.717 | 20026.717 |
| sandbox:exec | 17/17 | 0 | 0 | 18.994 | 0.039 | 18.953 | 1117.268 | 1128.780 | 2359.876 |
| capstone:build:rpn_eval | 1/1 | 0 | 0 | 18.711 | 0.001 | 18.710 | 18710.509 | 18710.509 | 18710.509 |
| capstone:build:bitcount | 1/1 | 0 | 0 | 18.538 | 0.000 | 18.537 | 18537.833 | 18537.833 | 18537.833 |
| capstone:build:powerset | 1/1 | 0 | 0 | 18.375 | 0.001 | 18.375 | 18375.449 | 18375.449 | 18375.449 |
| sandbox:start | 66/66 | 0 | 0 | 18.007 | 0.104 | 17.897 | 272.832 | 238.980 | 402.285 |
| tool:bash | 12/12 | 0 | 0 | 17.329 | 0.034 | 17.293 | 1444.056 | 1148.709 | 2828.941 |
| capstone:build:gcd | 1/1 | 0 | 0 | 17.321 | 0.001 | 17.320 | 17320.620 | 17320.620 | 17320.620 |
| tool:read | 37/37 | 0 | 0 | 17.258 | 0.151 | 17.097 | 466.424 | 417.610 | 590.697 |
| capstone:build:hanoi | 1/1 | 0 | 0 | 16.826 | 0.001 | 16.826 | 16826.129 | 16826.129 | 16826.129 |
| capstone:build:is_valid_parenthesization | 1/1 | 0 | 0 | 16.822 | 0.001 | 16.821 | 16821.616 | 16821.616 | 16821.616 |
| sandbox:stop | 132/132 | 0 | 0 | 13.363 | 0.104 | 13.255 | 101.235 | 110.241 | 189.637 |
| capstone:prepare:bitcount | 1/1 | 0 | 0 | 10.043 | 0.031 | 10.012 | 10042.677 | 10042.677 | 10042.677 |
| capstone:prepare:find_first_in_sorted | 1/1 | 0 | 0 | 10.042 | 0.030 | 10.011 | 10042.389 | 10042.389 | 10042.389 |
| sandbox:read_file | 49/49 | 0 | 0 | 7.822 | 0.074 | 7.742 | 159.632 | 89.557 | 334.979 |
| capstone:prepare:mergesort | 1/1 | 0 | 0 | 7.176 | 0.040 | 7.136 | 7176.287 | 7176.287 | 7176.287 |
| tool:edit | 12/12 | 0 | 0 | 5.796 | 0.055 | 5.738 | 482.972 | 417.067 | 767.236 |
| capstone:scheduler:tick | 618/618 | 0 | 0 | 2.758 | 0.796 | 1.957 | 4.463 | 0.191 | 0.344 |
| agent:create | 12/12 | 0 | 0 | 2.597 | 0.656 | 1.938 | 216.393 | 138.654 | 559.049 |
| capstone:prepare:levenshtein | 1/1 | 0 | 0 | 2.532 | 0.032 | 2.500 | 2531.901 | 2531.901 | 2531.901 |
| capstone:verify:levenshtein | 1/1 | 0 | 0 | 2.497 | 0.001 | 2.496 | 2497.487 | 2497.487 | 2497.487 |
| sandbox:destroy | 12/12 | 0 | 0 | 1.551 | 0.024 | 1.527 | 129.220 | 121.853 | 163.957 |
| tool:glob | 4/4 | 0 | 0 | 1.339 | 0.012 | 1.327 | 334.663 | 334.578 | 342.816 |
| sandbox:write_file | 12/12 | 0 | 0 | 1.242 | 0.013 | 1.229 | 103.474 | 90.935 | 159.696 |
| capstone:verify:next_palindrome | 1/1 | 0 | 0 | 1.088 | 0.002 | 1.085 | 1087.638 | 1087.638 | 1087.638 |
| capstone:prepare:hanoi | 1/1 | 0 | 0 | 0.732 | 0.057 | 0.675 | 731.822 | 731.822 | 731.822 |
| capstone:prepare:powerset | 1/1 | 0 | 0 | 0.469 | 0.033 | 0.436 | 468.503 | 468.503 | 468.503 |
| capstone:prepare:gcd | 1/1 | 0 | 0 | 0.463 | 0.030 | 0.433 | 462.722 | 462.722 | 462.722 |
| capstone:prepare:rpn_eval | 1/1 | 0 | 0 | 0.452 | 0.036 | 0.416 | 452.095 | 452.095 | 452.095 |
| capstone:prepare:is_valid_parenthesization | 1/1 | 0 | 0 | 0.445 | 0.032 | 0.413 | 444.728 | 444.728 | 444.728 |
| capstone:prepare:bucketsort | 1/1 | 0 | 0 | 0.438 | 0.030 | 0.409 | 438.315 | 438.315 | 438.315 |
| capstone:prepare:next_palindrome | 1/1 | 0 | 0 | 0.438 | 0.030 | 0.408 | 437.878 | 437.878 | 437.878 |
| capstone:prepare:flatten | 1/1 | 0 | 0 | 0.437 | 0.032 | 0.406 | 437.367 | 437.367 | 437.367 |
| capstone:verify:bitcount | 1/1 | 0 | 0 | 0.416 | 0.001 | 0.415 | 415.975 | 415.975 | 415.975 |
| capstone:verify:flatten | 1/1 | 0 | 0 | 0.412 | 0.001 | 0.411 | 411.757 | 411.757 | 411.757 |
| capstone:verify:find_first_in_sorted | 1/1 | 0 | 0 | 0.395 | 0.001 | 0.394 | 395.243 | 395.243 | 395.243 |
| capstone:verify:bucketsort | 1/1 | 0 | 0 | 0.391 | 0.001 | 0.390 | 391.390 | 391.390 | 391.390 |
| capstone:verify:hanoi | 1/1 | 0 | 0 | 0.389 | 0.001 | 0.388 | 389.475 | 389.475 | 389.475 |
| capstone:verify:mergesort | 1/1 | 0 | 0 | 0.389 | 0.001 | 0.387 | 388.538 | 388.538 | 388.538 |
| capstone:verify:is_valid_parenthesization | 1/1 | 0 | 0 | 0.387 | 0.001 | 0.386 | 386.822 | 386.822 | 386.822 |
| capstone:verify:gcd | 1/1 | 0 | 0 | 0.380 | 0.001 | 0.379 | 380.297 | 380.297 | 380.297 |
| capstone:verify:rpn_eval | 1/1 | 0 | 0 | 0.378 | 0.001 | 0.376 | 378.213 | 378.213 | 378.213 |
| capstone:verify:powerset | 1/1 | 0 | 0 | 0.374 | 0.001 | 0.373 | 373.662 | 373.662 | 373.662 |
| tool:grep | 1/1 | 0 | 0 | 0.336 | 0.003 | 0.333 | 335.931 | 335.931 | 335.931 |
| sandbox:provision | 12/12 | 0 | 0 | 0.196 | 0.008 | 0.188 | 16.311 | 0.448 | 86.068 |
| sandbox:create | 12/12 | 0 | 0 | 0.194 | 0.006 | 0.188 | 16.170 | 0.309 | 85.932 |
| run:detect | 1/1 | 0 | 0 | 0.141 | 0.001 | 0.140 | 140.513 | 140.513 | 140.513 |
| sync:container | 872/872 | 0 | 0 | 0.100 | 0.098 | 0.002 | 0.114 | 0.129 | 0.210 |
| prune | 24/24 | 0 | 0 | 0.008 | 0.004 | 0.004 | 0.320 | 0.261 | 0.651 |
| tool:return_summary | 18/18 | 6 | 0 | 0.006 | 0.006 | 0.000 | 0.354 | 0.360 | 0.443 |
| agsync:join | 12/12 | 0 | 0 | 0.006 | 0.006 | 0.000 | 0.471 | 0.233 | 1.547 |
| tool:return_status | 12/12 | 0 | 0 | 0.005 | 0.005 | 0.000 | 0.393 | 0.293 | 0.803 |
| tool:return_plan | 12/12 | 0 | 0 | 0.004 | 0.004 | 0.000 | 0.337 | 0.336 | 0.389 |
| llm:sync | 84/84 | 0 | 0 | 0.003 | 0.003 | 0.000 | 0.040 | 0.037 | 0.071 |
| input:prepare | 24/24 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.097 | 0.090 | 0.125 |
| agprof:clock_sync | 1/1 | 0 | 0 | 0.002 | 0.001 | 0.001 | 1.920 | 1.920 | 1.920 |
| proc_wait | 24/24 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.073 | 0.066 | 0.095 |
| resolve | 24/24 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.067 | 0.066 | 0.087 |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 6100 | 24.137 | 0.000 | 156.445 | 10.829 | 149.446008 CPU seconds | n/a |
| python3 (PID 72710) CPU | percent | 6488 | 3.627 | 0.000 | 129.808 | 19.512 | 24.350000 CPU seconds | n/a |
| python3 (PID 72710) io read MB/s | MB/s | 6488 | 0.039 | 0.000 | 91.833 | 0.000 | 26.402344 MB | n/a |
| python3 (PID 72710) io write MB/s | MB/s | 6488 | 0.053 | 0.000 | 22.547 | 8.575 | 34.863281 MB | n/a |
| python3 (PID 72710) rss_mb | MB | 6489 | 689.774 | 612.617 | 709.117 | 709.117 | n/a | n/a |
| python3 (PID 72710) vms_mb | MB | 6489 | 3734.129 | 3406.559 | 3766.723 | 3766.676 | n/a | n/a |
| git (PID 72716) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| git (PID 72716) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 72716) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 72716) rss_mb | MB | 2 | 4.695 | 4.695 | 4.695 | 4.695 | n/a | n/a |
| git (PID 72716) vms_mb | MB | 2 | 12.516 | 12.516 | 12.516 | 12.516 | n/a | n/a |
| git (PID 72717) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| git (PID 72717) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 72717) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 72717) rss_mb | MB | 2 | 3.230 | 3.230 | 3.230 | 3.230 | n/a | n/a |
| git (PID 72717) vms_mb | MB | 2 | 11.273 | 11.273 | 11.273 | 11.273 | n/a | n/a |
| git-remote-http (PID 72718) CPU | percent | 1 | 29.614 | 29.614 | 29.614 | 29.614 | 0.030000 CPU seconds | n/a |
| git-remote-http (PID 72718) io read MB/s | MB/s | 1 | 1.388 | 1.388 | 1.388 | 1.388 | 0.140625 MB | n/a |
| git-remote-http (PID 72718) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git-remote-http (PID 72718) rss_mb | MB | 2 | 18.777 | 18.574 | 18.980 | 18.980 | n/a | n/a |
| git-remote-http (PID 72718) vms_mb | MB | 2 | 107.066 | 106.566 | 107.566 | 107.566 | n/a | n/a |
| python3 (PID 72724) CPU | percent | 98 | 99.956 | 98.722 | 109.012 | 99.062 | 9.890000 CPU seconds | n/a |
| python3 (PID 72724) io read MB/s | MB/s | 98 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 72724) io write MB/s | MB/s | 98 | 0.002 | 0.000 | 0.155 | 0.000 | 0.015625 MB | n/a |
| python3 (PID 72724) rss_mb | MB | 99 | 33.718 | 11.242 | 34.090 | 34.090 | n/a | n/a |
| python3 (PID 72724) vms_mb | MB | 99 | 57.037 | 36.938 | 57.375 | 57.375 | n/a | n/a |
| python3 (PID 72725) CPU | percent | 3 | 102.320 | 98.963 | 108.907 | 108.907 | 0.310000 CPU seconds | n/a |
| python3 (PID 72725) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 72725) io write MB/s | MB/s | 3 | 0.761 | 0.000 | 2.243 | 2.243 | 0.230469 MB | n/a |
| python3 (PID 72725) rss_mb | MB | 4 | 28.780 | 18.766 | 34.906 | 34.906 | n/a | n/a |
| python3 (PID 72725) vms_mb | MB | 4 | 52.128 | 43.699 | 57.500 | 57.500 | n/a | n/a |
| python3 (PID 72726) CPU | percent | 3 | 102.310 | 98.934 | 108.969 | 108.969 | 0.310000 CPU seconds | n/a |
| python3 (PID 72726) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 72726) io write MB/s | MB/s | 3 | 0.761 | 0.000 | 2.283 | 2.283 | 0.230469 MB | n/a |
| python3 (PID 72726) rss_mb | MB | 4 | 27.200 | 14.824 | 36.488 | 36.488 | n/a | n/a |
| python3 (PID 72726) vms_mb | MB | 4 | 50.938 | 39.766 | 59.516 | 59.516 | n/a | n/a |
| python3 (PID 72727) CPU | percent | 3 | 98.983 | 89.119 | 109.025 | 89.119 | 0.300000 CPU seconds | n/a |
| python3 (PID 72727) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 72727) io write MB/s | MB/s | 3 | 0.761 | 0.000 | 2.243 | 2.243 | 0.230469 MB | n/a |
| python3 (PID 72727) rss_mb | MB | 4 | 29.114 | 19.918 | 34.918 | 34.918 | n/a | n/a |
| python3 (PID 72727) vms_mb | MB | 4 | 52.204 | 44.055 | 57.508 | 57.508 | n/a | n/a |
| python3 (PID 72728) CPU | percent | 24 | 100.275 | 98.866 | 108.976 | 99.115 | 2.430000 CPU seconds | n/a |
| python3 (PID 72728) io read MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 72728) io write MB/s | MB/s | 24 | 0.095 | 0.000 | 2.129 | 2.129 | 0.230469 MB | n/a |
| python3 (PID 72728) rss_mb | MB | 25 | 32.980 | 14.172 | 34.941 | 34.941 | n/a | n/a |
| python3 (PID 72728) vms_mb | MB | 25 | 56.360 | 39.566 | 57.512 | 57.512 | n/a | n/a |
| python3 (PID 72729) CPU | percent | 70 | 99.866 | 89.014 | 108.975 | 99.050 | 7.060000 CPU seconds | n/a |
| python3 (PID 72729) io read MB/s | MB/s | 70 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 72729) io write MB/s | MB/s | 70 | 0.034 | 0.000 | 2.206 | 0.000 | 0.238281 MB | n/a |
| python3 (PID 72729) rss_mb | MB | 71 | 41.409 | 13.570 | 47.824 | 47.824 | n/a | n/a |
| python3 (PID 72729) vms_mb | MB | 71 | 64.059 | 39.566 | 69.633 | 69.633 | n/a | n/a |
| python3 (PID 72730) CPU | percent | 3 | 102.338 | 98.965 | 109.023 | 109.023 | 0.310000 CPU seconds | n/a |
| python3 (PID 72730) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 72730) io write MB/s | MB/s | 3 | 0.787 | 0.000 | 2.362 | 2.362 | 0.238281 MB | n/a |
| python3 (PID 72730) rss_mb | MB | 4 | 25.850 | 12.766 | 34.816 | 34.816 | n/a | n/a |
| python3 (PID 72730) vms_mb | MB | 4 | 49.733 | 38.293 | 57.508 | 57.508 | n/a | n/a |
| python3 (PID 72731) CPU | percent | 98 | 99.973 | 89.107 | 115.910 | 99.017 | 9.910000 CPU seconds | n/a |
| python3 (PID 72731) io read MB/s | MB/s | 98 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 72731) io write MB/s | MB/s | 98 | 0.002 | 0.000 | 0.155 | 0.000 | 0.015625 MB | n/a |
| python3 (PID 72731) rss_mb | MB | 99 | 34.069 | 21.711 | 34.254 | 34.254 | n/a | n/a |
| python3 (PID 72731) vms_mb | MB | 99 | 57.283 | 45.531 | 57.457 | 57.457 | n/a | n/a |
| python3 (PID 72791) CPU | percent | 4 | 89.089 | 79.090 | 99.085 | 99.046 | 0.360000 CPU seconds | n/a |
| python3 (PID 72791) io read MB/s | MB/s | 4 | 2.251 | 0.000 | 5.796 | 0.000 | 0.910156 MB | n/a |
| python3 (PID 72791) io write MB/s | MB/s | 4 | 0.590 | 0.000 | 2.321 | 2.321 | 0.238281 MB | n/a |
| python3 (PID 72791) rss_mb | MB | 5 | 27.260 | 15.859 | 34.922 | 34.922 | n/a | n/a |
| python3 (PID 72791) vms_mb | MB | 5 | 50.789 | 41.035 | 57.492 | 57.492 | n/a | n/a |
| python3 (PID 72792) CPU | percent | 3 | 102.290 | 98.849 | 108.969 | 108.969 | 0.310000 CPU seconds | n/a |
| python3 (PID 72792) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 72792) io write MB/s | MB/s | 3 | 0.787 | 0.000 | 2.360 | 2.360 | 0.238281 MB | n/a |
| python3 (PID 72792) rss_mb | MB | 4 | 26.701 | 14.691 | 34.789 | 34.789 | n/a | n/a |
| python3 (PID 72792) vms_mb | MB | 4 | 50.436 | 39.766 | 57.508 | 57.508 | n/a | n/a |
| python3 (PID 72793) CPU | percent | 4 | 99.022 | 89.137 | 109.020 | 99.017 | 0.400000 CPU seconds | n/a |
| python3 (PID 72793) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 72793) io write MB/s | MB/s | 4 | 0.600 | 0.000 | 2.243 | 2.243 | 0.242188 MB | n/a |
| python3 (PID 72793) rss_mb | MB | 5 | 25.652 | 8.641 | 34.805 | 34.805 | n/a | n/a |
| python3 (PID 72793) vms_mb | MB | 5 | 49.815 | 35.199 | 57.457 | 57.457 | n/a | n/a |
| python3 (PID 72794) CPU | percent | 3 | 99.003 | 98.962 | 99.039 | 99.039 | 0.300000 CPU seconds | n/a |
| python3 (PID 72794) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 72794) io write MB/s | MB/s | 3 | 0.800 | 0.000 | 2.399 | 2.399 | 0.242188 MB | n/a |
| python3 (PID 72794) rss_mb | MB | 4 | 25.851 | 13.449 | 34.699 | 34.699 | n/a | n/a |
| python3 (PID 72794) vms_mb | MB | 4 | 49.987 | 39.566 | 57.508 | 57.508 | n/a | n/a |
| docker (PID 72798) CPU | percent | 1 | 9.896 | 9.896 | 9.896 | 9.896 | 0.010000 CPU seconds | n/a |
| docker (PID 72798) io read MB/s | MB/s | 1 | 0.773 | 0.773 | 0.773 | 0.773 | 0.078125 MB | n/a |
| docker (PID 72798) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 72798) rss_mb | MB | 2 | 21.654 | 17.066 | 26.242 | 26.242 | n/a | n/a |
| docker (PID 72798) vms_mb | MB | 2 | 1588.361 | 1515.949 | 1660.773 | 1660.773 | n/a | n/a |
| docker-trust (PID 72806) rss_mb | MB | 1 | 12.289 | 12.289 | 12.289 | 12.289 | n/a | n/a |
| docker-trust (PID 72806) vms_mb | MB | 1 | 1212.965 | 1212.965 | 1212.965 | 1212.965 | n/a | n/a |
| docker (PID 72850) CPU | percent | 2 | 9.850 | 0.000 | 19.701 | 19.701 | 0.020000 CPU seconds | n/a |
| docker (PID 72850) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 72850) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 72850) rss_mb | MB | 3 | 27.158 | 26.961 | 27.551 | 27.551 | n/a | n/a |
| docker (PID 72850) vms_mb | MB | 3 | 1684.775 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [alex_0000] (PID 72891) CPU | percent | 3 | 6.600 | 0.000 | 19.799 | 0.000 | 0.020000 CPU seconds | n/a |
| docker-init [alex_0000] (PID 72891) rss_mb | MB | 4 | 3.486 | 0.633 | 12.047 | 0.633 | n/a | n/a |
| docker-init [alex_0000] (PID 72891) vms_mb | MB | 4 | 375.347 | 1.055 | 1498.223 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 72902) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 72902) rss_mb | MB | 3 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [alex_0000] (PID 72902) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 72904) rss_mb | MB | 1 | 27.137 | 27.137 | 27.137 | 27.137 | n/a | n/a |
| docker (PID 72904) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] (PID 72924) rss_mb | MB | 1 | 11.762 | 11.762 | 11.762 | 11.762 | n/a | n/a |
| runc:[2:INIT] (PID 72924) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 72968) rss_mb | MB | 1 | 2.539 | 2.539 | 2.539 | 2.539 | n/a | n/a |
| docker (PID 72968) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 73004) rss_mb | MB | 1 | 27.062 | 27.062 | 27.062 | 27.062 | n/a | n/a |
| docker (PID 73004) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 73041) rss_mb | MB | 1 | 26.730 | 26.730 | 26.730 | 26.730 | n/a | n/a |
| docker (PID 73041) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 73098) rss_mb | MB | 1 | 25.859 | 25.859 | 25.859 | 25.859 | n/a | n/a |
| docker (PID 73098) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [alex_0000] (PID 73136) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [alex_0000] (PID 73136) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [alex_0000] (PID 73136) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 73150) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 73150) rss_mb | MB | 3 | 1.809 | 1.809 | 1.809 | 1.809 | n/a | n/a |
| tail [alex_0000] (PID 73150) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 73160) rss_mb | MB | 1 | 2.797 | 2.797 | 2.797 | 2.797 | n/a | n/a |
| docker (PID 73160) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 73188) rss_mb | MB | 1 | 27.301 | 27.301 | 27.301 | 27.301 | n/a | n/a |
| docker (PID 73188) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 73208) rss_mb | MB | 1 | 10.133 | 10.133 | 10.133 | 10.133 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 73208) vms_mb | MB | 1 | 1569.195 | 1569.195 | 1569.195 | 1569.195 | n/a | n/a |
| docker (PID 73224) rss_mb | MB | 1 | 26.926 | 26.926 | 26.926 | 26.926 | n/a | n/a |
| docker (PID 73224) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 73245) rss_mb | MB | 1 | 11.398 | 11.398 | 11.398 | 11.398 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 73245) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 73261) rss_mb | MB | 1 | 25.824 | 25.824 | 25.824 | 25.824 | n/a | n/a |
| docker (PID 73261) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 73320) CPU | percent | 1 | 9.909 | 9.909 | 9.909 | 9.909 | 0.010000 CPU seconds | n/a |
| docker (PID 73320) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 73320) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 73320) rss_mb | MB | 2 | 23.611 | 20.355 | 26.867 | 26.867 | n/a | n/a |
| docker (PID 73320) vms_mb | MB | 2 | 1588.486 | 1516.199 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 73358) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 73358) rss_mb | MB | 3 | 4.639 | 0.633 | 12.652 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 73358) vms_mb | MB | 3 | 524.112 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 73372) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 73372) rss_mb | MB | 2 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [alex_0000] (PID 73372) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 73383) rss_mb | MB | 1 | 27.242 | 27.242 | 27.242 | 27.242 | n/a | n/a |
| docker (PID 73383) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 73403) rss_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 73403) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 73444) rss_mb | MB | 1 | 19.699 | 19.699 | 19.699 | 19.699 | n/a | n/a |
| docker (PID 73444) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 73452) rss_mb | MB | 1 | 26.098 | 26.098 | 26.098 | 26.098 | n/a | n/a |
| docker (PID 73452) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 73514) rss_mb | MB | 1 | 26.930 | 26.930 | 26.930 | 26.930 | n/a | n/a |
| docker (PID 73514) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 73555) CPU | percent | 3 | 6.540 | 0.000 | 19.619 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 73555) rss_mb | MB | 4 | 2.699 | 0.633 | 8.898 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 73555) vms_mb | MB | 4 | 393.152 | 1.055 | 1569.445 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 73568) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 73568) rss_mb | MB | 3 | 1.664 | 1.664 | 1.664 | 1.664 | n/a | n/a |
| tail [alex_0000] (PID 73568) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 73578) rss_mb | MB | 1 | 19.945 | 19.945 | 19.945 | 19.945 | n/a | n/a |
| docker (PID 73578) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 73608) rss_mb | MB | 1 | 27.238 | 27.238 | 27.238 | 27.238 | n/a | n/a |
| docker (PID 73608) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 73628) rss_mb | MB | 1 | 11.469 | 11.469 | 11.469 | 11.469 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 73628) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 73644) rss_mb | MB | 1 | 27.391 | 27.391 | 27.391 | 27.391 | n/a | n/a |
| docker (PID 73644) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 73664) rss_mb | MB | 1 | 12.113 | 12.113 | 12.113 | 12.113 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 73664) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 73681) rss_mb | MB | 1 | 26.918 | 26.918 | 26.918 | 26.918 | n/a | n/a |
| docker (PID 73681) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 73751) rss_mb | MB | 1 | 25.852 | 25.852 | 25.852 | 25.852 | n/a | n/a |
| docker (PID 73751) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 73765) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 73765) io read MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 73765) io write MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 73765) rss_mb | MB | 37 | 25.652 | 25.652 | 25.652 | 25.652 | n/a | n/a |
| docker (PID 73765) vms_mb | MB | 37 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 73781) rss_mb | MB | 1 | 1.613 | 1.613 | 1.613 | 1.613 | n/a | n/a |
| docker (PID 73781) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 73799) rss_mb | MB | 1 | 9.285 | 9.285 | 9.285 | 9.285 | n/a | n/a |
| docker (PID 73799) vms_mb | MB | 1 | 1371.691 | 1371.691 | 1371.691 | 1371.691 | n/a | n/a |
| docker (PID 73808) rss_mb | MB | 1 | 25.469 | 25.469 | 25.469 | 25.469 | n/a | n/a |
| docker (PID 73808) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 73847) CPU | percent | 3 | 6.529 | 0.000 | 19.586 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 73847) rss_mb | MB | 4 | 3.312 | 0.633 | 11.352 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 73847) vms_mb | MB | 4 | 393.154 | 1.055 | 1569.453 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 73859) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 73859) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [alex_0000] (PID 73859) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 73869) rss_mb | MB | 1 | 27.062 | 27.062 | 27.062 | 27.062 | n/a | n/a |
| docker (PID 73869) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 73896) rss_mb | MB | 1 | 27.426 | 27.426 | 27.426 | 27.426 | n/a | n/a |
| docker (PID 73896) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 73916) rss_mb | MB | 1 | 12.285 | 12.285 | 12.285 | 12.285 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 73916) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 73964) rss_mb | MB | 1 | 1.633 | 1.633 | 1.633 | 1.633 | n/a | n/a |
| docker (PID 73964) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 73972) rss_mb | MB | 1 | 25.977 | 25.977 | 25.977 | 25.977 | n/a | n/a |
| docker (PID 73972) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 74032) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 74032) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 74032) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 74032) rss_mb | MB | 2 | 24.898 | 24.078 | 25.719 | 25.719 | n/a | n/a |
| docker (PID 74032) vms_mb | MB | 2 | 1628.211 | 1596.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 74076) CPU | percent | 10 | 0.981 | 0.000 | 9.811 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 74076) rss_mb | MB | 11 | 1.737 | 0.633 | 12.781 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 74076) vms_mb | MB | 11 | 143.707 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 74088) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 74088) rss_mb | MB | 10 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [alex_0000] (PID 74088) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 74099) rss_mb | MB | 1 | 27.332 | 27.332 | 27.332 | 27.332 | n/a | n/a |
| docker (PID 74099) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 74118) rss_mb | MB | 1 | 10.781 | 10.781 | 10.781 | 10.781 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 74118) vms_mb | MB | 1 | 1569.582 | 1569.582 | 1569.582 | 1569.582 | n/a | n/a |
| docker (PID 74125) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 74125) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 74125) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 74125) rss_mb | MB | 9 | 27.297 | 27.297 | 27.297 | 27.297 | n/a | n/a |
| docker (PID 74125) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [alex_0000] (PID 74145) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [alex_0000] (PID 74145) rss_mb | MB | 9 | 3.445 | 3.445 | 3.445 | 3.445 | n/a | n/a |
| bash [alex_0000] (PID 74145) vms_mb | MB | 9 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [alex_0000] (PID 74154) CPU | percent | 7 | 99.445 | 88.287 | 107.982 | 88.287 | 0.710000 CPU seconds | n/a |
| python [alex_0000] (PID 74154) rss_mb | MB | 8 | 29.484 | 7.973 | 42.832 | 42.832 | n/a | n/a |
| python [alex_0000] (PID 74154) vms_mb | MB | 8 | 36.031 | 13.070 | 52.238 | 52.238 | n/a | n/a |
| docker (PID 74165) rss_mb | MB | 1 | 25.688 | 25.688 | 25.688 | 25.688 | n/a | n/a |
| docker (PID 74165) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 74223) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 74223) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 74223) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 74223) rss_mb | MB | 2 | 26.484 | 26.484 | 26.484 | 26.484 | n/a | n/a |
| docker (PID 74223) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 74264) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 74264) rss_mb | MB | 4 | 3.686 | 0.633 | 12.844 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 74264) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 74276) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 74276) rss_mb | MB | 3 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [alex_0000] (PID 74276) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 74286) rss_mb | MB | 1 | 27.160 | 27.160 | 27.160 | 27.160 | n/a | n/a |
| docker (PID 74286) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 74306) rss_mb | MB | 1 | 11.539 | 11.539 | 11.539 | 11.539 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 74306) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 74351) rss_mb | MB | 1 | 4.473 | 4.473 | 4.473 | 4.473 | n/a | n/a |
| docker (PID 74351) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 74388) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 74388) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 74388) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 74388) rss_mb | MB | 2 | 25.816 | 25.816 | 25.816 | 25.816 | n/a | n/a |
| docker (PID 74388) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 74455) rss_mb | MB | 1 | 6.090 | 6.090 | 6.090 | 6.090 | n/a | n/a |
| docker (PID 74455) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 74471) CPU | percent | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 74471) io read MB/s | MB/s | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 74471) io write MB/s | MB/s | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 74471) rss_mb | MB | 51 | 26.328 | 26.328 | 26.328 | 26.328 | n/a | n/a |
| docker (PID 74471) vms_mb | MB | 51 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 74545) rss_mb | MB | 1 | 25.223 | 25.223 | 25.223 | 25.223 | n/a | n/a |
| docker (PID 74545) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| python3 (PID 74569) CPU | percent | 3 | 102.135 | 98.813 | 108.733 | 108.733 | 0.310000 CPU seconds | n/a |
| python3 (PID 74569) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 74569) io write MB/s | MB/s | 3 | 0.682 | 0.000 | 2.046 | 2.046 | 0.207031 MB | n/a |
| python3 (PID 74569) rss_mb | MB | 4 | 28.872 | 19.855 | 34.633 | 34.633 | n/a | n/a |
| python3 (PID 74569) vms_mb | MB | 4 | 52.256 | 44.188 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 74591) rss_mb | MB | 1 | 26.023 | 26.023 | 26.023 | 26.023 | n/a | n/a |
| docker (PID 74591) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 74621) CPU | percent | 2 | 4.919 | 0.000 | 9.838 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 74621) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 74621) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 74621) rss_mb | MB | 3 | 27.276 | 26.789 | 27.520 | 27.520 | n/a | n/a |
| docker (PID 74621) vms_mb | MB | 3 | 1708.776 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [andy_0000] (PID 74660) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 74660) rss_mb | MB | 4 | 3.747 | 0.633 | 13.090 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 74660) vms_mb | MB | 4 | 393.473 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 74672) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 74672) rss_mb | MB | 3 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [andy_0000] (PID 74672) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 74701) rss_mb | MB | 1 | 26.473 | 26.473 | 26.473 | 26.473 | n/a | n/a |
| docker (PID 74701) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 74737) rss_mb | MB | 1 | 27.605 | 27.605 | 27.605 | 27.605 | n/a | n/a |
| docker (PID 74737) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 74772) rss_mb | MB | 1 | 27.477 | 27.477 | 27.477 | 27.477 | n/a | n/a |
| docker (PID 74772) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 74792) rss_mb | MB | 1 | 11.820 | 11.820 | 11.820 | 11.820 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 74792) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 74810) rss_mb | MB | 1 | 27.125 | 27.125 | 27.125 | 27.125 | n/a | n/a |
| docker (PID 74810) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 74861) rss_mb | MB | 1 | 26.871 | 26.871 | 26.871 | 26.871 | n/a | n/a |
| docker (PID 74861) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 74870) rss_mb | MB | 1 | 25.344 | 25.344 | 25.344 | 25.344 | n/a | n/a |
| docker (PID 74870) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 74909) CPU | percent | 3 | 3.285 | 0.000 | 9.856 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 74909) rss_mb | MB | 4 | 3.556 | 0.633 | 12.324 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 74909) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 74922) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 74922) rss_mb | MB | 3 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [andy_0000] (PID 74922) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 74932) rss_mb | MB | 1 | 27.223 | 27.223 | 27.223 | 27.223 | n/a | n/a |
| docker (PID 74932) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 74953) rss_mb | MB | 1 | 10.242 | 10.242 | 10.242 | 10.242 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 74953) vms_mb | MB | 1 | 1641.199 | 1641.199 | 1641.199 | 1641.199 | n/a | n/a |
| docker (PID 75028) rss_mb | MB | 1 | 19.363 | 19.363 | 19.363 | 19.363 | n/a | n/a |
| docker (PID 75028) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 75036) rss_mb | MB | 1 | 26.645 | 26.645 | 26.645 | 26.645 | n/a | n/a |
| docker (PID 75036) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 75155) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 75155) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 75155) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 75155) rss_mb | MB | 2 | 26.293 | 26.293 | 26.293 | 26.293 | n/a | n/a |
| docker (PID 75155) vms_mb | MB | 2 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 75195) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 75195) rss_mb | MB | 4 | 3.678 | 0.633 | 12.812 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 75195) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 75207) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 75207) rss_mb | MB | 3 | 1.664 | 1.664 | 1.664 | 1.664 | n/a | n/a |
| tail [andy_0000] (PID 75207) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 75218) rss_mb | MB | 1 | 27.301 | 27.301 | 27.301 | 27.301 | n/a | n/a |
| docker (PID 75218) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 75237) rss_mb | MB | 1 | 11.996 | 11.996 | 11.996 | 11.996 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 75237) vms_mb | MB | 1 | 1498.223 | 1498.223 | 1498.223 | 1498.223 | n/a | n/a |
| docker (PID 75280) rss_mb | MB | 1 | 8.793 | 8.793 | 8.793 | 8.793 | n/a | n/a |
| docker (PID 75280) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 75317) CPU | percent | 1 | 9.778 | 9.778 | 9.778 | 9.778 | 0.010000 CPU seconds | n/a |
| docker (PID 75317) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 75317) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 75317) rss_mb | MB | 2 | 26.576 | 26.270 | 26.883 | 26.883 | n/a | n/a |
| docker (PID 75317) vms_mb | MB | 2 | 1660.648 | 1660.523 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 75387) rss_mb | MB | 1 | 26.871 | 26.871 | 26.871 | 26.871 | n/a | n/a |
| docker (PID 75387) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 75401) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 75401) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 75401) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 75401) rss_mb | MB | 38 | 26.770 | 26.770 | 26.770 | 26.770 | n/a | n/a |
| docker (PID 75401) vms_mb | MB | 38 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 75444) rss_mb | MB | 1 | 26.633 | 26.633 | 26.633 | 26.633 | n/a | n/a |
| docker (PID 75444) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [andy_0000] (PID 75484) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 75484) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 75484) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 75497) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 75497) rss_mb | MB | 3 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [andy_0000] (PID 75497) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 75499) rss_mb | MB | 1 | 0.125 | 0.125 | 0.125 | 0.125 | n/a | n/a |
| docker (PID 75499) vms_mb | MB | 1 | 30.570 | 30.570 | 30.570 | 30.570 | n/a | n/a |
| docker (PID 75536) rss_mb | MB | 1 | 20.125 | 20.125 | 20.125 | 20.125 | n/a | n/a |
| docker (PID 75536) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 75573) rss_mb | MB | 1 | 27.242 | 27.242 | 27.242 | 27.242 | n/a | n/a |
| docker (PID 75573) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 75612) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 75612) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 75612) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 75612) rss_mb | MB | 2 | 25.824 | 25.824 | 25.824 | 25.824 | n/a | n/a |
| docker (PID 75612) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 75671) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 75671) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 75671) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 75671) rss_mb | MB | 2 | 26.941 | 26.941 | 26.941 | 26.941 | n/a | n/a |
| docker (PID 75671) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 75711) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 75711) rss_mb | MB | 11 | 1.757 | 0.633 | 13.004 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 75711) vms_mb | MB | 11 | 143.707 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 75723) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 75723) rss_mb | MB | 10 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [andy_0000] (PID 75723) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 75733) rss_mb | MB | 1 | 27.188 | 27.188 | 27.188 | 27.188 | n/a | n/a |
| docker (PID 75733) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 75761) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 75761) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 75761) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 75761) rss_mb | MB | 9 | 27.383 | 27.383 | 27.383 | 27.383 | n/a | n/a |
| docker (PID 75761) vms_mb | MB | 9 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| bash [andy_0000] (PID 75781) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [andy_0000] (PID 75781) rss_mb | MB | 9 | 3.449 | 3.449 | 3.449 | 3.449 | n/a | n/a |
| bash [andy_0000] (PID 75781) vms_mb | MB | 9 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [andy_0000] (PID 75791) CPU | percent | 8 | 99.192 | 87.825 | 107.857 | 107.786 | 0.810000 CPU seconds | n/a |
| python [andy_0000] (PID 75791) rss_mb | MB | 9 | 32.240 | 11.125 | 42.902 | 42.902 | n/a | n/a |
| python [andy_0000] (PID 75791) vms_mb | MB | 9 | 39.469 | 14.898 | 52.238 | 52.238 | n/a | n/a |
| docker (PID 75801) rss_mb | MB | 1 | 27.227 | 27.227 | 27.227 | 27.227 | n/a | n/a |
| docker (PID 75801) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 75913) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 75913) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 75913) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 75913) rss_mb | MB | 2 | 27.016 | 27.016 | 27.016 | 27.016 | n/a | n/a |
| docker (PID 75913) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [andy_0000] (PID 75953) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 75953) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 75953) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 75967) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 75967) rss_mb | MB | 4 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [andy_0000] (PID 75967) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 76004) rss_mb | MB | 1 | 18.961 | 18.961 | 18.961 | 18.961 | n/a | n/a |
| docker (PID 76004) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 76044) rss_mb | MB | 1 | 27.227 | 27.227 | 27.227 | 27.227 | n/a | n/a |
| docker (PID 76044) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 76081) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 76081) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 76081) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 76081) rss_mb | MB | 2 | 25.898 | 25.898 | 25.898 | 25.898 | n/a | n/a |
| docker (PID 76081) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 76173) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 76173) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 76173) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 76173) rss_mb | MB | 39 | 27.066 | 27.066 | 27.066 | 27.066 | n/a | n/a |
| docker (PID 76173) vms_mb | MB | 39 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 76198) rss_mb | MB | 1 | 21.750 | 21.750 | 21.750 | 21.750 | n/a | n/a |
| docker (PID 76198) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| python3 (PID 76223) CPU | percent | 3 | 102.194 | 98.763 | 108.911 | 98.909 | 0.310000 CPU seconds | n/a |
| python3 (PID 76223) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 76223) io write MB/s | MB/s | 3 | 0.747 | 0.000 | 2.241 | 2.241 | 0.226562 MB | n/a |
| python3 (PID 76223) rss_mb | MB | 4 | 29.079 | 20.406 | 34.680 | 34.680 | n/a | n/a |
| python3 (PID 76223) vms_mb | MB | 4 | 52.506 | 45.188 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 76236) rss_mb | MB | 1 | 11.164 | 11.164 | 11.164 | 11.164 | n/a | n/a |
| docker (PID 76236) vms_mb | MB | 1 | 1387.949 | 1387.949 | 1387.949 | 1387.949 | n/a | n/a |
| docker (PID 76275) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 76275) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 76275) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 76275) rss_mb | MB | 2 | 27.398 | 27.398 | 27.398 | 27.398 | n/a | n/a |
| docker (PID 76275) vms_mb | MB | 2 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [arch_0000] (PID 76315) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [arch_0000] (PID 76315) rss_mb | MB | 4 | 3.662 | 0.633 | 12.750 | 0.633 | n/a | n/a |
| docker-init [arch_0000] (PID 76315) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 76327) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 76327) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [arch_0000] (PID 76327) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 76359) rss_mb | MB | 1 | 18.113 | 18.113 | 18.113 | 18.113 | n/a | n/a |
| docker (PID 76359) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 76395) rss_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| docker (PID 76395) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 76430) rss_mb | MB | 1 | 27.246 | 27.246 | 27.246 | 27.246 | n/a | n/a |
| docker (PID 76430) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 76451) rss_mb | MB | 1 | 11.422 | 11.422 | 11.422 | 11.422 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 76451) vms_mb | MB | 1 | 1570.098 | 1570.098 | 1570.098 | 1570.098 | n/a | n/a |
| docker (PID 76467) rss_mb | MB | 1 | 26.945 | 26.945 | 26.945 | 26.945 | n/a | n/a |
| docker (PID 76467) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 76519) rss_mb | MB | 1 | 15.664 | 15.664 | 15.664 | 15.664 | n/a | n/a |
| docker (PID 76519) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 76529) rss_mb | MB | 1 | 26.805 | 26.805 | 26.805 | 26.805 | n/a | n/a |
| docker (PID 76529) vms_mb | MB | 1 | 1588.770 | 1588.770 | 1588.770 | 1588.770 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 76568) CPU | percent | 3 | 9.804 | 0.000 | 29.412 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 76568) rss_mb | MB | 4 | 3.463 | 0.633 | 11.953 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 76568) vms_mb | MB | 4 | 393.315 | 1.055 | 1570.098 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 76580) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 76580) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [arch_0000] (PID 76580) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 76593) rss_mb | MB | 1 | 27.195 | 27.195 | 27.195 | 27.195 | n/a | n/a |
| docker (PID 76593) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| run4:diagnose_b (PID 76646) rss_mb | MB | 1 | 682.520 | 682.520 | 682.520 | 682.520 | n/a | n/a |
| run4:diagnose_b (PID 76646) vms_mb | MB | 1 | 3752.562 | 3752.562 | 3752.562 | 3752.562 | n/a | n/a |
| docker (PID 76683) rss_mb | MB | 1 | 11.211 | 11.211 | 11.211 | 11.211 | n/a | n/a |
| docker (PID 76683) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 76692) rss_mb | MB | 1 | 25.938 | 25.938 | 25.938 | 25.938 | n/a | n/a |
| docker (PID 76692) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 76767) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 76767) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 76767) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 76767) rss_mb | MB | 38 | 26.848 | 26.848 | 26.848 | 26.848 | n/a | n/a |
| docker (PID 76767) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 76783) rss_mb | MB | 1 | 25.621 | 25.621 | 25.621 | 25.621 | n/a | n/a |
| docker (PID 76783) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 76809) rss_mb | MB | 1 | 25.535 | 25.535 | 25.535 | 25.535 | n/a | n/a |
| docker (PID 76809) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [arch_0000] (PID 76849) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [arch_0000] (PID 76849) rss_mb | MB | 3 | 0.566 | 0.566 | 0.566 | 0.566 | n/a | n/a |
| docker-init [arch_0000] (PID 76849) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 76861) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 76861) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [arch_0000] (PID 76861) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 76897) rss_mb | MB | 1 | 23.000 | 23.000 | 23.000 | 23.000 | n/a | n/a |
| docker (PID 76897) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 76933) rss_mb | MB | 1 | 27.230 | 27.230 | 27.230 | 27.230 | n/a | n/a |
| docker (PID 76933) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 76972) rss_mb | MB | 1 | 26.152 | 26.152 | 26.152 | 26.152 | n/a | n/a |
| docker (PID 76972) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 77013) rss_mb | MB | 1 | 23.227 | 23.227 | 23.227 | 23.227 | n/a | n/a |
| docker (PID 77013) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 77030) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 77030) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 77030) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 77030) rss_mb | MB | 2 | 27.016 | 27.016 | 27.016 | 27.016 | n/a | n/a |
| docker (PID 77030) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [arch_0000] (PID 77071) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [arch_0000] (PID 77071) rss_mb | MB | 10 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [arch_0000] (PID 77071) vms_mb | MB | 10 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 77083) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 77083) rss_mb | MB | 10 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [arch_0000] (PID 77083) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 77119) CPU | percent | 8 | 1.216 | 0.000 | 9.731 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 77119) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 77119) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 77119) rss_mb | MB | 9 | 26.320 | 17.066 | 27.477 | 27.477 | n/a | n/a |
| docker (PID 77119) vms_mb | MB | 9 | 1644.682 | 1515.949 | 1660.773 | 1660.773 | n/a | n/a |
| bash [arch_0000] (PID 77139) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [arch_0000] (PID 77139) rss_mb | MB | 8 | 3.395 | 3.395 | 3.395 | 3.395 | n/a | n/a |
| bash [arch_0000] (PID 77139) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [arch_0000] (PID 77148) CPU | percent | 7 | 100.806 | 88.232 | 107.891 | 107.891 | 0.720000 CPU seconds | n/a |
| python [arch_0000] (PID 77148) rss_mb | MB | 8 | 31.622 | 12.855 | 41.559 | 41.559 | n/a | n/a |
| python [arch_0000] (PID 77148) vms_mb | MB | 8 | 38.696 | 16.414 | 51.219 | 51.219 | n/a | n/a |
| docker (PID 77158) rss_mb | MB | 1 | 26.688 | 26.688 | 26.688 | 26.688 | n/a | n/a |
| docker (PID 77158) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 77198) rss_mb | MB | 1 | 3.879 | 3.879 | 3.879 | 3.879 | n/a | n/a |
| docker (PID 77198) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 77216) rss_mb | MB | 1 | 27.004 | 27.004 | 27.004 | 27.004 | n/a | n/a |
| docker (PID 77216) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 77254) CPU | percent | 3 | 6.514 | 0.000 | 19.542 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 77254) rss_mb | MB | 4 | 3.195 | 0.633 | 10.883 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 77254) vms_mb | MB | 4 | 393.090 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 77267) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 77267) rss_mb | MB | 3 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [arch_0000] (PID 77267) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 77277) rss_mb | MB | 1 | 24.195 | 24.195 | 24.195 | 24.195 | n/a | n/a |
| docker (PID 77277) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 77304) rss_mb | MB | 1 | 27.320 | 27.320 | 27.320 | 27.320 | n/a | n/a |
| docker (PID 77304) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 77325) rss_mb | MB | 1 | 11.852 | 11.852 | 11.852 | 11.852 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 77325) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 77341) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 77341) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 77376) rss_mb | MB | 1 | 25.941 | 25.941 | 25.941 | 25.941 | n/a | n/a |
| docker (PID 77376) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 77453) rss_mb | MB | 1 | 25.828 | 25.828 | 25.828 | 25.828 | n/a | n/a |
| docker (PID 77453) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 77461) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 77461) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 77461) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 77461) rss_mb | MB | 39 | 26.965 | 26.965 | 26.965 | 26.965 | n/a | n/a |
| docker (PID 77461) vms_mb | MB | 39 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 77494) rss_mb | MB | 1 | 22.961 | 22.961 | 22.961 | 22.961 | n/a | n/a |
| docker (PID 77494) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| python3 (PID 77509) CPU | percent | 3 | 98.803 | 98.617 | 98.899 | 98.899 | 0.300000 CPU seconds | n/a |
| python3 (PID 77509) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 77509) io write MB/s | MB/s | 3 | 0.747 | 0.000 | 2.241 | 2.241 | 0.226562 MB | n/a |
| python3 (PID 77509) rss_mb | MB | 4 | 25.103 | 11.652 | 34.363 | 34.363 | n/a | n/a |
| python3 (PID 77509) vms_mb | MB | 4 | 49.563 | 37.938 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 77540) rss_mb | MB | 1 | 7.680 | 7.680 | 7.680 | 7.680 | n/a | n/a |
| docker (PID 77540) vms_mb | MB | 1 | 32.867 | 32.867 | 32.867 | 32.867 | n/a | n/a |
| docker (PID 77548) rss_mb | MB | 1 | 26.352 | 26.352 | 26.352 | 26.352 | n/a | n/a |
| docker (PID 77548) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 77562) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 77562) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 77562) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 77562) rss_mb | MB | 2 | 27.391 | 27.391 | 27.391 | 27.391 | n/a | n/a |
| docker (PID 77562) vms_mb | MB | 2 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [bake_0000] (PID 77601) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bake_0000] (PID 77601) rss_mb | MB | 4 | 3.749 | 0.633 | 13.098 | 0.633 | n/a | n/a |
| docker-init [bake_0000] (PID 77601) vms_mb | MB | 4 | 393.473 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 77614) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 77614) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bake_0000] (PID 77614) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 77645) rss_mb | MB | 1 | 19.871 | 19.871 | 19.871 | 19.871 | n/a | n/a |
| docker (PID 77645) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 77680) rss_mb | MB | 1 | 27.480 | 27.480 | 27.480 | 27.480 | n/a | n/a |
| docker (PID 77680) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 77716) rss_mb | MB | 1 | 26.949 | 26.949 | 26.949 | 26.949 | n/a | n/a |
| docker (PID 77716) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 77738) rss_mb | MB | 1 | 11.387 | 11.387 | 11.387 | 11.387 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 77738) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 77754) rss_mb | MB | 1 | 26.195 | 26.195 | 26.195 | 26.195 | n/a | n/a |
| docker (PID 77754) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 77804) rss_mb | MB | 1 | 21.504 | 21.504 | 21.504 | 21.504 | n/a | n/a |
| docker (PID 77804) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 77813) rss_mb | MB | 1 | 25.605 | 25.605 | 25.605 | 25.605 | n/a | n/a |
| docker (PID 77813) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 77852) CPU | percent | 3 | 6.482 | 0.000 | 19.445 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 77852) rss_mb | MB | 4 | 3.571 | 0.633 | 12.387 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 77852) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 77865) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 77865) rss_mb | MB | 3 | 1.695 | 1.695 | 1.695 | 1.695 | n/a | n/a |
| tail [bake_0000] (PID 77865) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 77875) rss_mb | MB | 1 | 27.434 | 27.434 | 27.434 | 27.434 | n/a | n/a |
| docker (PID 77875) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 77902) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 77902) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 77966) rss_mb | MB | 1 | 17.344 | 17.344 | 17.344 | 17.344 | n/a | n/a |
| docker (PID 77966) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 77974) rss_mb | MB | 1 | 25.691 | 25.691 | 25.691 | 25.691 | n/a | n/a |
| docker (PID 77974) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 78027) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 78027) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78027) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78027) rss_mb | MB | 2 | 26.738 | 26.738 | 26.738 | 26.738 | n/a | n/a |
| docker (PID 78027) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 78065) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 78065) rss_mb | MB | 4 | 3.623 | 0.633 | 12.594 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 78065) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 78080) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 78080) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [bake_0000] (PID 78080) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 78090) rss_mb | MB | 1 | 26.984 | 26.984 | 26.984 | 26.984 | n/a | n/a |
| docker (PID 78090) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 78110) rss_mb | MB | 1 | 12.422 | 12.422 | 12.422 | 12.422 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 78110) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 78155) rss_mb | MB | 1 | 18.230 | 18.230 | 18.230 | 18.230 | n/a | n/a |
| docker (PID 78155) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 78190) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 78190) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78190) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78190) rss_mb | MB | 2 | 27.020 | 27.020 | 27.020 | 27.020 | n/a | n/a |
| docker (PID 78190) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 78250) rss_mb | MB | 1 | 14.324 | 14.324 | 14.324 | 14.324 | n/a | n/a |
| docker (PID 78250) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 78272) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 78272) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78272) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78272) rss_mb | MB | 38 | 26.277 | 26.277 | 26.277 | 26.277 | n/a | n/a |
| docker (PID 78272) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 78288) rss_mb | MB | 1 | 26.664 | 26.664 | 26.664 | 26.664 | n/a | n/a |
| docker (PID 78288) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 78315) CPU | percent | 3 | 6.565 | 0.000 | 19.694 | 0.000 | 0.020000 CPU seconds | n/a |
| docker (PID 78315) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78315) io write MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78315) rss_mb | MB | 4 | 20.448 | 0.559 | 27.078 | 27.078 | n/a | n/a |
| docker (PID 78315) vms_mb | MB | 4 | 1253.771 | 32.762 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 78353) CPU | percent | 9 | 4.167 | 0.000 | 37.500 | 0.000 | 0.040000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 78353) rss_mb | MB | 10 | 1.757 | 0.633 | 11.875 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 78353) vms_mb | MB | 10 | 165.183 | 1.055 | 1642.336 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 78367) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 78367) rss_mb | MB | 9 | 1.472 | 0.125 | 1.641 | 1.641 | n/a | n/a |
| tail [bake_0000] (PID 78367) vms_mb | MB | 9 | 2.706 | 0.477 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 78378) CPU | percent | 2 | 28.814 | 0.000 | 57.628 | 0.000 | 0.060000 CPU seconds | n/a |
| docker (PID 78378) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78378) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78378) rss_mb | MB | 3 | 18.667 | 2.062 | 26.969 | 26.969 | n/a | n/a |
| docker (PID 78378) vms_mb | MB | 3 | 1118.103 | 32.762 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 78397) rss_mb | MB | 1 | 11.891 | 11.891 | 11.891 | 11.891 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 78397) vms_mb | MB | 1 | 1642.730 | 1642.730 | 1642.730 | 1642.730 | n/a | n/a |
| docker (PID 78405) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 78405) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78405) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78405) rss_mb | MB | 2 | 27.199 | 27.199 | 27.199 | 27.199 | n/a | n/a |
| docker (PID 78405) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 78424) rss_mb | MB | 1 | 12.137 | 12.137 | 12.137 | 12.137 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 78424) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 78441) CPU | percent | 1 | 67.171 | 67.171 | 67.171 | 67.171 | 0.070000 CPU seconds | n/a |
| docker (PID 78441) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78441) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78441) rss_mb | MB | 2 | 20.867 | 14.871 | 26.863 | 26.863 | n/a | n/a |
| docker (PID 78441) vms_mb | MB | 2 | 1588.361 | 1515.949 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 78462) rss_mb | MB | 1 | 10.680 | 10.680 | 10.680 | 10.680 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 78462) vms_mb | MB | 1 | 1569.582 | 1569.582 | 1569.582 | 1569.582 | n/a | n/a |
| docker (PID 78480) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 78480) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78480) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78480) rss_mb | MB | 2 | 27.262 | 27.262 | 27.262 | 27.262 | n/a | n/a |
| docker (PID 78480) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 78530) rss_mb | MB | 1 | 10.746 | 10.746 | 10.746 | 10.746 | n/a | n/a |
| docker (PID 78530) vms_mb | MB | 1 | 1451.949 | 1451.949 | 1451.949 | 1451.949 | n/a | n/a |
| docker (PID 78538) rss_mb | MB | 1 | 25.750 | 25.750 | 25.750 | 25.750 | n/a | n/a |
| docker (PID 78538) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 78578) CPU | percent | 10 | 2.928 | 0.000 | 29.280 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 78578) rss_mb | MB | 11 | 1.611 | 0.633 | 11.391 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 78578) vms_mb | MB | 11 | 143.647 | 1.055 | 1569.574 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 78592) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 78592) rss_mb | MB | 10 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [bake_0000] (PID 78592) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 78602) rss_mb | MB | 1 | 19.363 | 19.363 | 19.363 | 19.363 | n/a | n/a |
| docker (PID 78602) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 78628) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 78628) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78628) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78628) rss_mb | MB | 8 | 27.461 | 27.461 | 27.461 | 27.461 | n/a | n/a |
| docker (PID 78628) vms_mb | MB | 8 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 78648) CPU | percent | 7 | 2.796 | 0.000 | 19.574 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 78648) rss_mb | MB | 8 | 4.435 | 3.387 | 11.770 | 3.387 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 78648) vms_mb | MB | 8 | 200.135 | 4.391 | 1570.348 | 4.391 | n/a | n/a |
| python [bake_0000] (PID 78657) CPU | percent | 6 | 99.663 | 97.891 | 107.825 | 98.088 | 0.610000 CPU seconds | n/a |
| python [bake_0000] (PID 78657) rss_mb | MB | 7 | 32.056 | 18.305 | 41.000 | 41.000 | n/a | n/a |
| python [bake_0000] (PID 78657) vms_mb | MB | 7 | 38.799 | 23.074 | 50.375 | 50.375 | n/a | n/a |
| docker (PID 78667) rss_mb | MB | 1 | 25.828 | 25.828 | 25.828 | 25.828 | n/a | n/a |
| docker (PID 78667) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 78728) rss_mb | MB | 1 | 26.887 | 26.887 | 26.887 | 26.887 | n/a | n/a |
| docker (PID 78728) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [bake_0000] (PID 78770) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bake_0000] (PID 78770) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bake_0000] (PID 78770) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 78781) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 78781) rss_mb | MB | 3 | 1.809 | 1.809 | 1.809 | 1.809 | n/a | n/a |
| tail [bake_0000] (PID 78781) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 78820) rss_mb | MB | 1 | 24.055 | 24.055 | 24.055 | 24.055 | n/a | n/a |
| docker (PID 78820) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 78856) rss_mb | MB | 1 | 27.266 | 27.266 | 27.266 | 27.266 | n/a | n/a |
| docker (PID 78856) vms_mb | MB | 1 | 1733.027 | 1733.027 | 1733.027 | 1733.027 | n/a | n/a |
| docker (PID 78893) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 78893) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78893) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78893) rss_mb | MB | 2 | 25.992 | 25.992 | 25.992 | 25.992 | n/a | n/a |
| docker (PID 78893) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 78971) rss_mb | MB | 1 | 16.297 | 16.297 | 16.297 | 16.297 | n/a | n/a |
| docker (PID 78971) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 78979) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 78979) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78979) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 78979) rss_mb | MB | 39 | 25.852 | 25.852 | 25.852 | 25.852 | n/a | n/a |
| docker (PID 78979) vms_mb | MB | 39 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 79004) rss_mb | MB | 1 | 23.922 | 23.922 | 23.922 | 23.922 | n/a | n/a |
| docker (PID 79004) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| python3 (PID 79027) CPU | percent | 2 | 103.695 | 98.619 | 108.772 | 108.772 | 0.210000 CPU seconds | n/a |
| python3 (PID 79027) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 79027) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 79027) rss_mb | MB | 3 | 27.737 | 20.953 | 33.676 | 33.676 | n/a | n/a |
| python3 (PID 79027) vms_mb | MB | 3 | 51.315 | 45.316 | 56.461 | 56.461 | n/a | n/a |
| docker (PID 79056) rss_mb | MB | 1 | 25.332 | 25.332 | 25.332 | 25.332 | n/a | n/a |
| docker (PID 79056) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 79064) rss_mb | MB | 1 | 22.535 | 22.535 | 22.535 | 22.535 | n/a | n/a |
| docker (PID 79064) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 79078) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 79078) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 79078) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 79078) rss_mb | MB | 2 | 27.953 | 27.953 | 27.953 | 27.953 | n/a | n/a |
| docker (PID 79078) vms_mb | MB | 2 | 1804.781 | 1804.781 | 1804.781 | 1804.781 | n/a | n/a |
| docker-init [bale_0000] (PID 79120) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bale_0000] (PID 79120) rss_mb | MB | 4 | 3.773 | 0.633 | 13.195 | 0.633 | n/a | n/a |
| docker-init [bale_0000] (PID 79120) vms_mb | MB | 4 | 393.473 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 79132) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 79132) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bale_0000] (PID 79132) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 79165) rss_mb | MB | 1 | 4.711 | 4.711 | 4.711 | 4.711 | n/a | n/a |
| docker (PID 79165) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 79200) rss_mb | MB | 1 | 27.297 | 27.297 | 27.297 | 27.297 | n/a | n/a |
| docker (PID 79200) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 79236) rss_mb | MB | 1 | 27.402 | 27.402 | 27.402 | 27.402 | n/a | n/a |
| docker (PID 79236) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 79256) rss_mb | MB | 1 | 10.582 | 10.582 | 10.582 | 10.582 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 79256) vms_mb | MB | 1 | 1569.453 | 1569.453 | 1569.453 | 1569.453 | n/a | n/a |
| docker (PID 79273) rss_mb | MB | 1 | 27.137 | 27.137 | 27.137 | 27.137 | n/a | n/a |
| docker (PID 79273) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 79323) rss_mb | MB | 1 | 10.766 | 10.766 | 10.766 | 10.766 | n/a | n/a |
| docker (PID 79323) vms_mb | MB | 1 | 1387.949 | 1387.949 | 1387.949 | 1387.949 | n/a | n/a |
| docker (PID 79331) rss_mb | MB | 1 | 27.102 | 27.102 | 27.102 | 27.102 | n/a | n/a |
| docker (PID 79331) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 79371) CPU | percent | 3 | 3.251 | 0.000 | 9.753 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 79371) rss_mb | MB | 4 | 3.440 | 0.633 | 11.863 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 79371) vms_mb | MB | 4 | 393.283 | 1.055 | 1569.969 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 79383) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 79383) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bale_0000] (PID 79383) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 79394) rss_mb | MB | 1 | 27.207 | 27.207 | 27.207 | 27.207 | n/a | n/a |
| docker (PID 79394) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 79424) rss_mb | MB | 1 | 27.453 | 27.453 | 27.453 | 27.453 | n/a | n/a |
| docker (PID 79424) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 79488) rss_mb | MB | 1 | 15.574 | 15.574 | 15.574 | 15.574 | n/a | n/a |
| docker (PID 79488) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 79497) rss_mb | MB | 1 | 26.012 | 26.012 | 26.012 | 26.012 | n/a | n/a |
| docker (PID 79497) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 79582) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 79582) io read MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 79582) io write MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 79582) rss_mb | MB | 37 | 25.535 | 25.535 | 25.535 | 25.535 | n/a | n/a |
| docker (PID 79582) vms_mb | MB | 37 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 79598) rss_mb | MB | 1 | 10.984 | 10.984 | 10.984 | 10.984 | n/a | n/a |
| docker (PID 79598) vms_mb | MB | 1 | 1451.949 | 1451.949 | 1451.949 | 1451.949 | n/a | n/a |
| docker (PID 79624) rss_mb | MB | 1 | 26.742 | 26.742 | 26.742 | 26.742 | n/a | n/a |
| docker (PID 79624) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 79663) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 79663) rss_mb | MB | 4 | 3.502 | 0.633 | 12.109 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 79663) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 79675) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 79675) rss_mb | MB | 3 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [bale_0000] (PID 79675) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 79685) rss_mb | MB | 1 | 27.219 | 27.219 | 27.219 | 27.219 | n/a | n/a |
| docker (PID 79685) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[0:PARENT] [bale_0000] (PID 79701) rss_mb | MB | 1 | 1.996 | 1.996 | 1.996 | 1.996 | n/a | n/a |
| runc:[0:PARENT] [bale_0000] (PID 79701) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| docker (PID 79745) rss_mb | MB | 1 | 0.547 | 0.547 | 0.547 | 0.547 | n/a | n/a |
| docker (PID 79745) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 79782) rss_mb | MB | 1 | 23.930 | 23.930 | 23.930 | 23.930 | n/a | n/a |
| docker (PID 79782) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 79791) rss_mb | MB | 1 | 25.812 | 25.812 | 25.812 | 25.812 | n/a | n/a |
| docker (PID 79791) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 79846) rss_mb | MB | 1 | 27.062 | 27.062 | 27.062 | 27.062 | n/a | n/a |
| docker (PID 79846) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [bale_0000] (PID 79886) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bale_0000] (PID 79886) rss_mb | MB | 37 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bale_0000] (PID 79886) vms_mb | MB | 37 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 79898) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 79898) rss_mb | MB | 37 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [bale_0000] (PID 79898) vms_mb | MB | 37 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 79900) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 79900) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 79938) CPU | percent | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 79938) io read MB/s | MB/s | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 79938) io write MB/s | MB/s | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 79938) rss_mb | MB | 35 | 27.078 | 27.078 | 27.078 | 27.078 | n/a | n/a |
| docker (PID 79938) vms_mb | MB | 35 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[0:PARENT] [bale_0000] (PID 79954) rss_mb | MB | 1 | 1.934 | 1.934 | 1.934 | 1.934 | n/a | n/a |
| runc:[0:PARENT] [bale_0000] (PID 79954) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| bash [bale_0000] (PID 79958) CPU | percent | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bale_0000] (PID 79958) rss_mb | MB | 34 | 3.387 | 3.387 | 3.387 | 3.387 | n/a | n/a |
| bash [bale_0000] (PID 79958) vms_mb | MB | 34 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bale_0000] (PID 79967) CPU | percent | 33 | 100.146 | 97.586 | 108.039 | 107.851 | 3.370000 CPU seconds | n/a |
| python [bale_0000] (PID 79967) rss_mb | MB | 34 | 39.068 | 15.422 | 41.047 | 40.992 | n/a | n/a |
| python [bale_0000] (PID 79967) vms_mb | MB | 34 | 47.867 | 19.508 | 50.594 | 50.324 | n/a | n/a |
| docker (PID 79977) rss_mb | MB | 1 | 26.047 | 26.047 | 26.047 | 26.047 | n/a | n/a |
| docker (PID 79977) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 80063) rss_mb | MB | 1 | 27.016 | 27.016 | 27.016 | 27.016 | n/a | n/a |
| docker (PID 80063) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 80072) CPU | percent | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 80072) io read MB/s | MB/s | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 80072) io write MB/s | MB/s | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 80072) rss_mb | MB | 47 | 26.977 | 26.977 | 26.977 | 26.977 | n/a | n/a |
| docker (PID 80072) vms_mb | MB | 47 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 80104) rss_mb | MB | 1 | 26.785 | 26.785 | 26.785 | 26.785 | n/a | n/a |
| docker (PID 80104) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| python3 (PID 80120) CPU | percent | 24 | 100.120 | 98.596 | 108.770 | 98.891 | 2.430000 CPU seconds | n/a |
| python3 (PID 80120) io read MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 80120) io write MB/s | MB/s | 24 | 0.093 | 0.000 | 2.240 | 2.240 | 0.226562 MB | n/a |
| python3 (PID 80120) rss_mb | MB | 25 | 32.844 | 14.332 | 34.789 | 34.789 | n/a | n/a |
| python3 (PID 80120) vms_mb | MB | 25 | 56.325 | 39.570 | 57.457 | 57.438 | n/a | n/a |
| docker (PID 80149) rss_mb | MB | 1 | 20.609 | 20.609 | 20.609 | 20.609 | n/a | n/a |
| docker (PID 80149) vms_mb | MB | 1 | 1524.203 | 1524.203 | 1524.203 | 1524.203 | n/a | n/a |
| docker (PID 80171) CPU | percent | 2 | 9.857 | 0.000 | 19.714 | 0.000 | 0.020000 CPU seconds | n/a |
| docker (PID 80171) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 80171) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 80171) rss_mb | MB | 3 | 17.776 | 0.000 | 27.480 | 0.000 | n/a | n/a |
| docker (PID 80171) vms_mb | MB | 3 | 1131.017 | 0.000 | 1732.777 | 0.000 | n/a | n/a |
| docker-init [band_0000] (PID 80212) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [band_0000] (PID 80212) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [band_0000] (PID 80212) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 80224) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 80224) rss_mb | MB | 4 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [band_0000] (PID 80224) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 80262) rss_mb | MB | 1 | 25.387 | 25.387 | 25.387 | 25.387 | n/a | n/a |
| docker (PID 80262) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 80288) rss_mb | MB | 1 | 27.508 | 27.508 | 27.508 | 27.508 | n/a | n/a |
| docker (PID 80288) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 80307) rss_mb | MB | 1 | 11.941 | 11.941 | 11.941 | 11.941 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 80307) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 80363) rss_mb | MB | 1 | 26.844 | 26.844 | 26.844 | 26.844 | n/a | n/a |
| docker (PID 80363) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 80420) rss_mb | MB | 1 | 26.496 | 26.496 | 26.496 | 26.496 | n/a | n/a |
| docker (PID 80420) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 80460) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 80460) rss_mb | MB | 4 | 3.525 | 0.633 | 12.203 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 80460) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 80472) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 80472) rss_mb | MB | 3 | 1.699 | 1.699 | 1.699 | 1.699 | n/a | n/a |
| tail [band_0000] (PID 80472) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 80482) rss_mb | MB | 1 | 27.309 | 27.309 | 27.309 | 27.309 | n/a | n/a |
| docker (PID 80482) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 80502) rss_mb | MB | 1 | 10.871 | 10.871 | 10.871 | 10.871 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 80502) vms_mb | MB | 1 | 1569.711 | 1569.711 | 1569.711 | 1569.711 | n/a | n/a |
| docker (PID 80538) rss_mb | MB | 1 | 23.594 | 23.594 | 23.594 | 23.594 | n/a | n/a |
| docker (PID 80538) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 80584) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 80584) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 80584) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 80584) rss_mb | MB | 2 | 16.199 | 6.516 | 25.883 | 25.883 | n/a | n/a |
| docker (PID 80584) vms_mb | MB | 2 | 846.486 | 32.762 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 80653) rss_mb | MB | 1 | 26.594 | 26.594 | 26.594 | 26.594 | n/a | n/a |
| docker (PID 80653) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 80667) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 80667) io read MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 80667) io write MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 80667) rss_mb | MB | 37 | 27.008 | 27.008 | 27.008 | 27.008 | n/a | n/a |
| docker (PID 80667) vms_mb | MB | 37 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 80683) rss_mb | MB | 1 | 0.414 | 0.414 | 0.414 | 0.414 | n/a | n/a |
| docker (PID 80683) vms_mb | MB | 1 | 30.578 | 30.578 | 30.578 | 30.578 | n/a | n/a |
| docker (PID 80711) rss_mb | MB | 1 | 25.344 | 25.344 | 25.344 | 25.344 | n/a | n/a |
| docker (PID 80711) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [band_0000] (PID 80753) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [band_0000] (PID 80753) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [band_0000] (PID 80753) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 80765) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 80765) rss_mb | MB | 3 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [band_0000] (PID 80765) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 80767) rss_mb | MB | 1 | 23.422 | 23.422 | 23.422 | 23.422 | n/a | n/a |
| docker (PID 80767) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 80802) rss_mb | MB | 1 | 26.809 | 26.809 | 26.809 | 26.809 | n/a | n/a |
| docker (PID 80802) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 80840) rss_mb | MB | 1 | 27.129 | 27.129 | 27.129 | 27.129 | n/a | n/a |
| docker (PID 80840) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 80860) rss_mb | MB | 1 | 10.309 | 10.309 | 10.309 | 10.309 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 80860) vms_mb | MB | 1 | 1641.449 | 1641.449 | 1641.449 | 1641.449 | n/a | n/a |
| docker (PID 80880) rss_mb | MB | 1 | 25.824 | 25.824 | 25.824 | 25.824 | n/a | n/a |
| docker (PID 80880) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 80922) rss_mb | MB | 1 | 23.555 | 23.555 | 23.555 | 23.555 | n/a | n/a |
| docker (PID 80922) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 80940) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 80940) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 80940) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 80940) rss_mb | MB | 2 | 26.562 | 26.562 | 26.562 | 26.562 | n/a | n/a |
| docker (PID 80940) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 80979) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 80979) rss_mb | MB | 11 | 1.755 | 0.633 | 12.977 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 80979) vms_mb | MB | 11 | 150.275 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 80992) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 80992) rss_mb | MB | 10 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [band_0000] (PID 80992) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 81002) rss_mb | MB | 1 | 27.258 | 27.258 | 27.258 | 27.258 | n/a | n/a |
| docker (PID 81002) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 81022) rss_mb | MB | 1 | 12.301 | 12.301 | 12.301 | 12.301 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 81022) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 81030) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 81030) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 81030) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 81030) rss_mb | MB | 9 | 27.695 | 27.695 | 27.695 | 27.695 | n/a | n/a |
| docker (PID 81030) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [band_0000] (PID 81050) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [band_0000] (PID 81050) rss_mb | MB | 9 | 3.473 | 3.473 | 3.473 | 3.473 | n/a | n/a |
| bash [band_0000] (PID 81050) vms_mb | MB | 9 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [band_0000] (PID 81060) CPU | percent | 7 | 100.699 | 88.132 | 107.814 | 107.744 | 0.720000 CPU seconds | n/a |
| python [band_0000] (PID 81060) rss_mb | MB | 8 | 30.746 | 10.809 | 41.957 | 41.957 | n/a | n/a |
| python [band_0000] (PID 81060) vms_mb | MB | 8 | 37.783 | 14.766 | 51.324 | 51.324 | n/a | n/a |
| docker (PID 81070) rss_mb | MB | 1 | 26.863 | 26.863 | 26.863 | 26.863 | n/a | n/a |
| docker (PID 81070) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 81116) rss_mb | MB | 1 | 20.320 | 20.320 | 20.320 | 20.320 | n/a | n/a |
| docker (PID 81116) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 81149) CPU | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 81149) io read MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 81149) io write MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 81149) rss_mb | MB | 40 | 25.174 | 8.363 | 25.605 | 25.605 | n/a | n/a |
| docker (PID 81149) vms_mb | MB | 40 | 1619.527 | 32.867 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 81181) rss_mb | MB | 1 | 2.793 | 2.793 | 2.793 | 2.793 | n/a | n/a |
| docker (PID 81181) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| python3 (PID 81197) CPU | percent | 3 | 98.838 | 98.588 | 98.995 | 98.931 | 0.300000 CPU seconds | n/a |
| python3 (PID 81197) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 81197) io write MB/s | MB/s | 3 | 0.734 | 0.000 | 2.203 | 2.203 | 0.222656 MB | n/a |
| python3 (PID 81197) rss_mb | MB | 4 | 23.988 | 9.109 | 34.426 | 34.426 | n/a | n/a |
| python3 (PID 81197) vms_mb | MB | 4 | 48.287 | 35.328 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 81210) rss_mb | MB | 1 | 23.754 | 23.754 | 23.754 | 23.754 | n/a | n/a |
| docker (PID 81210) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 81250) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 81250) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 81250) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 81250) rss_mb | MB | 2 | 26.943 | 26.703 | 27.184 | 27.184 | n/a | n/a |
| docker (PID 81250) vms_mb | MB | 2 | 1696.775 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [bart_0000] (PID 81291) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bart_0000] (PID 81291) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bart_0000] (PID 81291) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 81304) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 81304) rss_mb | MB | 4 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bart_0000] (PID 81304) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 81307) rss_mb | MB | 1 | 18.414 | 18.414 | 18.414 | 18.414 | n/a | n/a |
| docker (PID 81307) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 81342) rss_mb | MB | 1 | 27.254 | 27.254 | 27.254 | 27.254 | n/a | n/a |
| docker (PID 81342) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 81431) rss_mb | MB | 1 | 21.090 | 21.090 | 21.090 | 21.090 | n/a | n/a |
| docker (PID 81431) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 81439) rss_mb | MB | 1 | 27.188 | 27.188 | 27.188 | 27.188 | n/a | n/a |
| docker (PID 81439) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 81497) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 81497) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 81497) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 81497) rss_mb | MB | 2 | 25.684 | 25.684 | 25.684 | 25.684 | n/a | n/a |
| docker (PID 81497) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 81536) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 81536) rss_mb | MB | 4 | 3.749 | 0.633 | 13.098 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 81536) vms_mb | MB | 4 | 393.473 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 81549) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 81549) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bart_0000] (PID 81549) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 81561) rss_mb | MB | 1 | 27.312 | 27.312 | 27.312 | 27.312 | n/a | n/a |
| docker (PID 81561) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 81580) rss_mb | MB | 1 | 11.781 | 11.781 | 11.781 | 11.781 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 81580) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 81623) rss_mb | MB | 1 | 3.484 | 3.484 | 3.484 | 3.484 | n/a | n/a |
| docker (PID 81623) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 81661) CPU | percent | 1 | 9.797 | 9.797 | 9.797 | 9.797 | 0.010000 CPU seconds | n/a |
| docker (PID 81661) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 81661) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 81661) rss_mb | MB | 2 | 26.145 | 25.195 | 27.094 | 27.094 | n/a | n/a |
| docker (PID 81661) vms_mb | MB | 2 | 1660.492 | 1660.211 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 81719) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 81719) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 81719) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 81719) rss_mb | MB | 2 | 24.752 | 23.648 | 25.855 | 25.855 | n/a | n/a |
| docker (PID 81719) vms_mb | MB | 2 | 1624.207 | 1588.203 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 81759) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 81759) rss_mb | MB | 3 | 4.673 | 0.633 | 12.754 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 81759) vms_mb | MB | 3 | 524.112 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 81771) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 81771) rss_mb | MB | 2 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [bart_0000] (PID 81771) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 81782) rss_mb | MB | 1 | 27.324 | 27.324 | 27.324 | 27.324 | n/a | n/a |
| docker (PID 81782) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 81801) rss_mb | MB | 1 | 11.816 | 11.816 | 11.816 | 11.816 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 81801) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 81842) rss_mb | MB | 1 | 15.203 | 15.203 | 15.203 | 15.203 | n/a | n/a |
| docker (PID 81842) vms_mb | MB | 1 | 1451.699 | 1451.699 | 1451.699 | 1451.699 | n/a | n/a |
| docker (PID 81850) rss_mb | MB | 1 | 26.000 | 26.000 | 26.000 | 26.000 | n/a | n/a |
| docker (PID 81850) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 81909) rss_mb | MB | 1 | 27.094 | 27.094 | 27.094 | 27.094 | n/a | n/a |
| docker (PID 81909) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 81947) CPU | percent | 2 | 9.563 | 0.000 | 19.126 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 81947) rss_mb | MB | 3 | 3.008 | 0.633 | 7.758 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 81947) vms_mb | MB | 3 | 523.852 | 1.055 | 1569.445 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 81960) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 81960) rss_mb | MB | 2 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bart_0000] (PID 81960) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 81970) rss_mb | MB | 1 | 17.613 | 17.613 | 17.613 | 17.613 | n/a | n/a |
| docker (PID 81970) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 81998) rss_mb | MB | 1 | 27.430 | 27.430 | 27.430 | 27.430 | n/a | n/a |
| docker (PID 81998) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 82018) rss_mb | MB | 1 | 11.453 | 11.453 | 11.453 | 11.453 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 82018) vms_mb | MB | 1 | 1498.094 | 1498.094 | 1498.094 | 1498.094 | n/a | n/a |
| docker (PID 82040) rss_mb | MB | 1 | 26.969 | 26.969 | 26.969 | 26.969 | n/a | n/a |
| docker (PID 82040) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 82085) rss_mb | MB | 1 | 17.238 | 17.238 | 17.238 | 17.238 | n/a | n/a |
| docker (PID 82085) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 82102) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 82102) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 82102) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 82102) rss_mb | MB | 2 | 25.820 | 25.820 | 25.820 | 25.820 | n/a | n/a |
| docker (PID 82102) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 82141) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 82141) rss_mb | MB | 4 | 3.655 | 0.633 | 12.723 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 82141) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 82154) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 82154) rss_mb | MB | 3 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [bart_0000] (PID 82154) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 82164) rss_mb | MB | 1 | 27.395 | 27.395 | 27.395 | 27.395 | n/a | n/a |
| docker (PID 82164) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 82183) rss_mb | MB | 1 | 10.906 | 10.906 | 10.906 | 10.906 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 82183) vms_mb | MB | 1 | 1569.582 | 1569.582 | 1569.582 | 1569.582 | n/a | n/a |
| docker (PID 82218) rss_mb | MB | 1 | 19.504 | 19.504 | 19.504 | 19.504 | n/a | n/a |
| docker (PID 82218) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 82264) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 82264) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 82264) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 82264) rss_mb | MB | 2 | 17.598 | 9.242 | 25.953 | 25.953 | n/a | n/a |
| docker (PID 82264) vms_mb | MB | 2 | 1552.078 | 1443.945 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 82331) rss_mb | MB | 1 | 27.043 | 27.043 | 27.043 | 27.043 | n/a | n/a |
| docker (PID 82331) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 82345) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 82345) io read MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 82345) io write MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 82345) rss_mb | MB | 37 | 26.566 | 26.566 | 26.566 | 26.566 | n/a | n/a |
| docker (PID 82345) vms_mb | MB | 37 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 82363) rss_mb | MB | 1 | 16.289 | 16.289 | 16.289 | 16.289 | n/a | n/a |
| docker (PID 82363) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 82391) rss_mb | MB | 1 | 25.699 | 25.699 | 25.699 | 25.699 | n/a | n/a |
| docker (PID 82391) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bart_0000] (PID 82430) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bart_0000] (PID 82430) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bart_0000] (PID 82430) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 82443) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 82443) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bart_0000] (PID 82443) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 82445) rss_mb | MB | 1 | 23.586 | 23.586 | 23.586 | 23.586 | n/a | n/a |
| docker (PID 82445) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 82480) rss_mb | MB | 1 | 27.273 | 27.273 | 27.273 | 27.273 | n/a | n/a |
| docker (PID 82480) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 82499) rss_mb | MB | 1 | 5.258 | 5.258 | 5.258 | 5.258 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 82499) vms_mb | MB | 1 | 1441.445 | 1441.445 | 1441.445 | 1441.445 | n/a | n/a |
| docker (PID 82515) rss_mb | MB | 1 | 27.430 | 27.430 | 27.430 | 27.430 | n/a | n/a |
| docker (PID 82515) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 82534) rss_mb | MB | 1 | 11.410 | 11.410 | 11.410 | 11.410 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 82534) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 82553) rss_mb | MB | 1 | 26.840 | 26.840 | 26.840 | 26.840 | n/a | n/a |
| docker (PID 82553) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 82613) rss_mb | MB | 1 | 25.820 | 25.820 | 25.820 | 25.820 | n/a | n/a |
| docker (PID 82613) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bart_0000] (PID 82652) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bart_0000] (PID 82652) rss_mb | MB | 10 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bart_0000] (PID 82652) vms_mb | MB | 10 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 82664) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 82664) rss_mb | MB | 10 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [bart_0000] (PID 82664) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 82702) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 82702) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 82702) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 82702) rss_mb | MB | 9 | 27.141 | 27.141 | 27.141 | 27.141 | n/a | n/a |
| docker (PID 82702) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 82722) CPU | percent | 8 | 2.431 | 0.000 | 19.445 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 82722) rss_mb | MB | 9 | 4.256 | 3.410 | 11.020 | 3.410 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 82722) vms_mb | MB | 9 | 178.328 | 4.391 | 1569.824 | 4.391 | n/a | n/a |
| python [bart_0000] (PID 82731) CPU | percent | 7 | 100.810 | 88.211 | 107.857 | 107.857 | 0.720000 CPU seconds | n/a |
| python [bart_0000] (PID 82731) rss_mb | MB | 8 | 32.823 | 15.562 | 42.055 | 41.262 | n/a | n/a |
| python [bart_0000] (PID 82731) vms_mb | MB | 8 | 40.093 | 19.637 | 52.289 | 51.324 | n/a | n/a |
| docker (PID 82741) rss_mb | MB | 1 | 26.758 | 26.758 | 26.758 | 26.758 | n/a | n/a |
| docker (PID 82741) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 82786) rss_mb | MB | 1 | 17.211 | 17.211 | 17.211 | 17.211 | n/a | n/a |
| docker (PID 82786) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 82795) rss_mb | MB | 1 | 17.949 | 17.949 | 17.949 | 17.949 | n/a | n/a |
| docker (PID 82795) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 82804) rss_mb | MB | 1 | 27.031 | 27.031 | 27.031 | 27.031 | n/a | n/a |
| docker (PID 82804) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 82844) CPU | percent | 3 | 6.533 | 0.000 | 19.599 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 82844) rss_mb | MB | 4 | 3.598 | 0.633 | 12.492 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 82844) vms_mb | MB | 4 | 411.474 | 1.055 | 1642.730 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 82857) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 82857) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bart_0000] (PID 82857) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 82867) rss_mb | MB | 1 | 27.562 | 27.562 | 27.562 | 27.562 | n/a | n/a |
| docker (PID 82867) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 82896) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 82896) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 82958) rss_mb | MB | 1 | 25.656 | 25.656 | 25.656 | 25.656 | n/a | n/a |
| docker (PID 82958) vms_mb | MB | 1 | 1587.957 | 1587.957 | 1587.957 | 1587.957 | n/a | n/a |
| docker (PID 82966) rss_mb | MB | 1 | 27.125 | 27.125 | 27.125 | 27.125 | n/a | n/a |
| docker (PID 82966) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 83029) rss_mb | MB | 1 | 16.590 | 16.590 | 16.590 | 16.590 | n/a | n/a |
| docker (PID 83029) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 83048) rss_mb | MB | 1 | 5.668 | 5.668 | 5.668 | 5.668 | n/a | n/a |
| docker (PID 83048) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 83064) CPU | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 83064) io read MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 83064) io write MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 83064) rss_mb | MB | 40 | 25.730 | 25.730 | 25.730 | 25.730 | n/a | n/a |
| docker (PID 83064) vms_mb | MB | 40 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 83100) rss_mb | MB | 1 | 25.465 | 25.465 | 25.465 | 25.465 | n/a | n/a |
| docker (PID 83100) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| python3 (PID 83115) CPU | percent | 3 | 98.795 | 88.945 | 108.846 | 108.846 | 0.300000 CPU seconds | n/a |
| python3 (PID 83115) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 83115) io write MB/s | MB/s | 3 | 0.734 | 0.000 | 2.203 | 2.203 | 0.222656 MB | n/a |
| python3 (PID 83115) rss_mb | MB | 4 | 25.901 | 13.027 | 34.402 | 34.402 | n/a | n/a |
| python3 (PID 83115) vms_mb | MB | 4 | 50.062 | 38.430 | 57.457 | 57.457 | n/a | n/a |
| docker (PID 83168) CPU | percent | 1 | 19.772 | 19.772 | 19.772 | 19.772 | 0.020000 CPU seconds | n/a |
| docker (PID 83168) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 83168) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 83168) rss_mb | MB | 2 | 27.037 | 26.645 | 27.430 | 27.430 | n/a | n/a |
| docker (PID 83168) vms_mb | MB | 2 | 1696.775 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [base_0000] (PID 83210) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [base_0000] (PID 83210) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [base_0000] (PID 83210) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 83222) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 83222) rss_mb | MB | 4 | 1.707 | 1.707 | 1.707 | 1.707 | n/a | n/a |
| tail [base_0000] (PID 83222) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 83225) rss_mb | MB | 1 | 15.582 | 15.582 | 15.582 | 15.582 | n/a | n/a |
| docker (PID 83225) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 83261) rss_mb | MB | 1 | 27.316 | 27.316 | 27.316 | 27.316 | n/a | n/a |
| docker (PID 83261) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 83288) rss_mb | MB | 1 | 27.355 | 27.355 | 27.355 | 27.355 | n/a | n/a |
| docker (PID 83288) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| sh [base_0000] (PID 83307) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sh [base_0000] (PID 83307) vms_mb | MB | 1 | 0.516 | 0.516 | 0.516 | 0.516 | n/a | n/a |
| docker (PID 83352) rss_mb | MB | 1 | 15.301 | 15.301 | 15.301 | 15.301 | n/a | n/a |
| docker (PID 83352) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 83360) rss_mb | MB | 1 | 25.738 | 25.738 | 25.738 | 25.738 | n/a | n/a |
| docker (PID 83360) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 83418) CPU | percent | 1 | 9.848 | 9.848 | 9.848 | 9.848 | 0.010000 CPU seconds | n/a |
| docker (PID 83418) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 83418) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 83418) rss_mb | MB | 2 | 24.646 | 22.688 | 26.605 | 26.605 | n/a | n/a |
| docker (PID 83418) vms_mb | MB | 2 | 1624.488 | 1588.203 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 83458) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 83458) rss_mb | MB | 4 | 3.729 | 0.633 | 13.016 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 83458) vms_mb | MB | 4 | 411.411 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 83471) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 83471) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [base_0000] (PID 83471) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 83484) rss_mb | MB | 1 | 27.418 | 27.418 | 27.418 | 27.418 | n/a | n/a |
| docker (PID 83484) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 83504) rss_mb | MB | 1 | 11.395 | 11.395 | 11.395 | 11.395 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 83504) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 83537) rss_mb | MB | 1 | 24.266 | 24.266 | 24.266 | 24.266 | n/a | n/a |
| docker (PID 83537) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 83582) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 83582) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 83582) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 83582) rss_mb | MB | 2 | 23.469 | 20.977 | 25.961 | 25.961 | n/a | n/a |
| docker (PID 83582) vms_mb | MB | 2 | 1624.207 | 1588.203 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 83652) rss_mb | MB | 1 | 8.957 | 8.957 | 8.957 | 8.957 | n/a | n/a |
| docker (PID 83652) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 83666) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 83666) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 83666) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 83666) rss_mb | MB | 38 | 25.746 | 25.746 | 25.746 | 25.746 | n/a | n/a |
| docker (PID 83666) vms_mb | MB | 38 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 83682) rss_mb | MB | 1 | 25.746 | 25.746 | 25.746 | 25.746 | n/a | n/a |
| docker (PID 83682) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 83709) CPU | percent | 1 | 9.844 | 9.844 | 9.844 | 9.844 | 0.010000 CPU seconds | n/a |
| docker (PID 83709) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 83709) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 83709) rss_mb | MB | 2 | 23.572 | 20.266 | 26.879 | 26.879 | n/a | n/a |
| docker (PID 83709) vms_mb | MB | 2 | 1624.488 | 1588.203 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 83748) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 83748) rss_mb | MB | 4 | 3.745 | 0.633 | 13.082 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 83748) vms_mb | MB | 4 | 393.473 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 83760) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 83760) rss_mb | MB | 3 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [base_0000] (PID 83760) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 83770) rss_mb | MB | 1 | 27.207 | 27.207 | 27.207 | 27.207 | n/a | n/a |
| docker (PID 83770) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 83790) rss_mb | MB | 1 | 10.918 | 10.918 | 10.918 | 10.918 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 83790) vms_mb | MB | 1 | 1569.703 | 1569.703 | 1569.703 | 1569.703 | n/a | n/a |
| docker (PID 83830) rss_mb | MB | 1 | 5.531 | 5.531 | 5.531 | 5.531 | n/a | n/a |
| docker (PID 83830) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 83870) rss_mb | MB | 1 | 15.680 | 15.680 | 15.680 | 15.680 | n/a | n/a |
| docker (PID 83870) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 83878) rss_mb | MB | 1 | 25.734 | 25.734 | 25.734 | 25.734 | n/a | n/a |
| docker (PID 83878) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 83936) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 83936) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 83936) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 83936) rss_mb | MB | 2 | 26.641 | 26.641 | 26.641 | 26.641 | n/a | n/a |
| docker (PID 83936) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 83977) CPU | percent | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 83977) rss_mb | MB | 19 | 1.281 | 0.633 | 12.953 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 83977) vms_mb | MB | 19 | 83.656 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 83990) CPU | percent | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 83990) rss_mb | MB | 18 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [base_0000] (PID 83990) vms_mb | MB | 18 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| run15:repair_bu (PID 84027) CPU | percent | 16 | 1.222 | 0.000 | 19.547 | 0.000 | 0.020000 CPU seconds | n/a |
| run15:repair_bu (PID 84027) io read MB/s | MB/s | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| run15:repair_bu (PID 84027) io write MB/s | MB/s | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| run15:repair_bu (PID 84027) rss_mb | MB | 17 | 66.564 | 27.254 | 695.520 | 27.254 | n/a | n/a |
| run15:repair_bu (PID 84027) vms_mb | MB | 17 | 1784.357 | 1661.023 | 3757.691 | 1661.023 | n/a | n/a |
| bash [base_0000] (PID 84046) CPU | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [base_0000] (PID 84046) rss_mb | MB | 16 | 3.332 | 3.332 | 3.332 | 3.332 | n/a | n/a |
| bash [base_0000] (PID 84046) vms_mb | MB | 16 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [base_0000] (PID 84055) CPU | percent | 15 | 99.687 | 88.017 | 107.862 | 97.511 | 1.540000 CPU seconds | n/a |
| python [base_0000] (PID 84055) rss_mb | MB | 16 | 35.749 | 11.820 | 41.695 | 41.695 | n/a | n/a |
| python [base_0000] (PID 84055) vms_mb | MB | 16 | 44.238 | 16.047 | 51.027 | 51.027 | n/a | n/a |
| docker (PID 84065) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 84065) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 84065) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 84065) rss_mb | MB | 2 | 25.938 | 25.938 | 25.938 | 25.938 | n/a | n/a |
| docker (PID 84065) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 84116) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 84116) vms_mb | MB | 1 | 30.570 | 30.570 | 30.570 | 30.570 | n/a | n/a |
| docker (PID 84124) rss_mb | MB | 1 | 25.465 | 25.465 | 25.465 | 25.465 | n/a | n/a |
| docker (PID 84124) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 84165) CPU | percent | 3 | 9.637 | 0.000 | 28.912 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 84165) rss_mb | MB | 4 | 3.272 | 0.633 | 11.191 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 84165) vms_mb | MB | 4 | 393.152 | 1.055 | 1569.445 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 84177) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 84177) rss_mb | MB | 3 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [base_0000] (PID 84177) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 84188) rss_mb | MB | 1 | 25.375 | 25.375 | 25.375 | 25.375 | n/a | n/a |
| docker (PID 84188) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 84214) rss_mb | MB | 1 | 27.367 | 27.367 | 27.367 | 27.367 | n/a | n/a |
| docker (PID 84214) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 84234) rss_mb | MB | 1 | 11.773 | 11.773 | 11.773 | 11.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 84234) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 84287) rss_mb | MB | 1 | 25.961 | 25.961 | 25.961 | 25.961 | n/a | n/a |
| docker (PID 84287) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 84380) CPU | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 84380) io read MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 84380) io write MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 84380) rss_mb | MB | 40 | 25.083 | 15.656 | 25.324 | 25.324 | n/a | n/a |
| docker (PID 84380) vms_mb | MB | 40 | 1656.598 | 1515.699 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 84414) rss_mb | MB | 1 | 26.703 | 26.703 | 26.703 | 26.703 | n/a | n/a |
| docker (PID 84414) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 84429) CPU | percent | 3 | 102.047 | 89.006 | 108.701 | 108.701 | 0.310000 CPU seconds | n/a |
| python3 (PID 84429) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 84429) io write MB/s | MB/s | 3 | 0.682 | 0.000 | 2.046 | 2.046 | 0.207031 MB | n/a |
| python3 (PID 84429) rss_mb | MB | 4 | 26.223 | 13.520 | 34.523 | 34.523 | n/a | n/a |
| python3 (PID 84429) vms_mb | MB | 4 | 50.372 | 39.570 | 57.441 | 57.441 | n/a | n/a |
| docker (PID 84450) rss_mb | MB | 1 | 6.574 | 6.574 | 6.574 | 6.574 | n/a | n/a |
| docker (PID 84450) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 84466) rss_mb | MB | 1 | 25.719 | 25.719 | 25.719 | 25.719 | n/a | n/a |
| docker (PID 84466) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 84480) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 84480) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 84480) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 84480) rss_mb | MB | 2 | 27.023 | 27.023 | 27.023 | 27.023 | n/a | n/a |
| docker (PID 84480) vms_mb | MB | 2 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [beam_0000] (PID 84521) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beam_0000] (PID 84521) rss_mb | MB | 4 | 3.657 | 0.633 | 12.730 | 0.633 | n/a | n/a |
| docker-init [beam_0000] (PID 84521) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 84533) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 84533) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [beam_0000] (PID 84533) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 84563) rss_mb | MB | 1 | 26.000 | 26.000 | 26.000 | 26.000 | n/a | n/a |
| docker (PID 84563) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 84596) rss_mb | MB | 1 | 27.301 | 27.301 | 27.301 | 27.301 | n/a | n/a |
| docker (PID 84596) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 84629) rss_mb | MB | 1 | 27.387 | 27.387 | 27.387 | 27.387 | n/a | n/a |
| docker (PID 84629) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 84649) rss_mb | MB | 1 | 11.867 | 11.867 | 11.867 | 11.867 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 84649) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 84666) rss_mb | MB | 1 | 26.789 | 26.789 | 26.789 | 26.789 | n/a | n/a |
| docker (PID 84666) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 84716) rss_mb | MB | 1 | 26.102 | 26.102 | 26.102 | 26.102 | n/a | n/a |
| docker (PID 84716) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 84724) rss_mb | MB | 1 | 25.512 | 25.512 | 25.512 | 25.512 | n/a | n/a |
| docker (PID 84724) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 84762) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [beam_0000] (PID 84762) rss_mb | MB | 4 | 3.557 | 0.633 | 12.328 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 84762) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 84776) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 84776) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [beam_0000] (PID 84776) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 84787) rss_mb | MB | 1 | 27.430 | 27.430 | 27.430 | 27.430 | n/a | n/a |
| docker (PID 84787) vms_mb | MB | 1 | 1733.027 | 1733.027 | 1733.027 | 1733.027 | n/a | n/a |
| docker (PID 84881) rss_mb | MB | 1 | 19.836 | 19.836 | 19.836 | 19.836 | n/a | n/a |
| docker (PID 84881) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 84890) rss_mb | MB | 1 | 26.289 | 26.289 | 26.289 | 26.289 | n/a | n/a |
| docker (PID 84890) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 84959) rss_mb | MB | 1 | 1.070 | 1.070 | 1.070 | 1.070 | n/a | n/a |
| docker (PID 84959) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 84975) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 84975) io read MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 84975) io write MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 84975) rss_mb | MB | 37 | 26.543 | 26.543 | 26.543 | 26.543 | n/a | n/a |
| docker (PID 84975) vms_mb | MB | 37 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 84991) rss_mb | MB | 1 | 26.824 | 26.824 | 26.824 | 26.824 | n/a | n/a |
| docker (PID 84991) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 85017) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 85017) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 85017) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 85017) rss_mb | MB | 2 | 12.857 | 0.414 | 25.301 | 25.301 | n/a | n/a |
| docker (PID 85017) vms_mb | MB | 2 | 809.393 | 30.578 | 1588.207 | 1588.207 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 85055) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [beam_0000] (PID 85055) rss_mb | MB | 4 | 3.583 | 0.633 | 12.434 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 85055) vms_mb | MB | 4 | 393.473 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 85067) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 85067) rss_mb | MB | 3 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [beam_0000] (PID 85067) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 85079) rss_mb | MB | 1 | 27.641 | 27.641 | 27.641 | 27.641 | n/a | n/a |
| docker (PID 85079) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 85099) rss_mb | MB | 1 | 10.953 | 10.953 | 10.953 | 10.953 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 85099) vms_mb | MB | 1 | 1641.578 | 1641.578 | 1641.578 | 1641.578 | n/a | n/a |
| docker (PID 85137) rss_mb | MB | 1 | 9.242 | 9.242 | 9.242 | 9.242 | n/a | n/a |
| docker (PID 85137) vms_mb | MB | 1 | 1243.691 | 1243.691 | 1243.691 | 1243.691 | n/a | n/a |
| docker (PID 85177) rss_mb | MB | 1 | 25.629 | 25.629 | 25.629 | 25.629 | n/a | n/a |
| docker (PID 85177) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 85186) rss_mb | MB | 1 | 26.082 | 26.082 | 26.082 | 26.082 | n/a | n/a |
| docker (PID 85186) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 85245) rss_mb | MB | 1 | 25.438 | 25.438 | 25.438 | 25.438 | n/a | n/a |
| docker (PID 85245) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 85285) CPU | percent | 10 | 1.951 | 0.000 | 19.514 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [beam_0000] (PID 85285) rss_mb | MB | 11 | 1.574 | 0.633 | 10.984 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 85285) vms_mb | MB | 11 | 143.636 | 1.055 | 1569.445 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 85297) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 85297) rss_mb | MB | 10 | 1.801 | 1.801 | 1.801 | 1.801 | n/a | n/a |
| tail [beam_0000] (PID 85297) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 85308) rss_mb | MB | 1 | 24.969 | 24.969 | 24.969 | 24.969 | n/a | n/a |
| docker (PID 85308) vms_mb | MB | 1 | 1659.961 | 1659.961 | 1659.961 | 1659.961 | n/a | n/a |
| docker (PID 85334) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 85334) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 85334) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 85334) rss_mb | MB | 9 | 24.139 | 0.000 | 27.156 | 0.000 | n/a | n/a |
| docker (PID 85334) vms_mb | MB | 9 | 1476.243 | 0.000 | 1660.773 | 0.000 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 85354) CPU | percent | 7 | 1.398 | 0.000 | 9.783 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [beam_0000] (PID 85354) rss_mb | MB | 8 | 4.540 | 3.480 | 11.957 | 3.480 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 85354) vms_mb | MB | 8 | 209.214 | 4.391 | 1642.980 | 4.391 | n/a | n/a |
| python [beam_0000] (PID 85364) CPU | percent | 6 | 101.318 | 98.071 | 108.024 | 98.090 | 0.620000 CPU seconds | n/a |
| python [beam_0000] (PID 85364) rss_mb | MB | 7 | 32.141 | 18.207 | 42.578 | 42.578 | n/a | n/a |
| python [beam_0000] (PID 85364) vms_mb | MB | 7 | 39.160 | 23.074 | 52.238 | 52.238 | n/a | n/a |
| docker (PID 85374) rss_mb | MB | 1 | 25.910 | 25.910 | 25.910 | 25.910 | n/a | n/a |
| docker (PID 85374) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 85432) rss_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| docker (PID 85432) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [beam_0000] (PID 85471) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beam_0000] (PID 85471) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [beam_0000] (PID 85471) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 85483) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 85483) rss_mb | MB | 3 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [beam_0000] (PID 85483) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 85521) rss_mb | MB | 1 | 27.438 | 27.438 | 27.438 | 27.438 | n/a | n/a |
| docker (PID 85521) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[0:PARENT] [beam_0000] (PID 85538) rss_mb | MB | 1 | 1.969 | 1.969 | 1.969 | 1.969 | n/a | n/a |
| runc:[0:PARENT] [beam_0000] (PID 85538) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[0:PARENT] [beam_0000] (PID 85539) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[0:PARENT] [beam_0000] (PID 85539) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| docker (PID 85555) rss_mb | MB | 1 | 27.348 | 27.348 | 27.348 | 27.348 | n/a | n/a |
| docker (PID 85555) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 85575) rss_mb | MB | 1 | 11.770 | 11.770 | 11.770 | 11.770 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 85575) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 85592) rss_mb | MB | 1 | 25.906 | 25.906 | 25.906 | 25.906 | n/a | n/a |
| docker (PID 85592) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 85661) rss_mb | MB | 1 | 25.773 | 25.773 | 25.773 | 25.773 | n/a | n/a |
| docker (PID 85661) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 85677) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 85677) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 85677) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 85677) rss_mb | MB | 39 | 26.812 | 26.812 | 26.812 | 26.812 | n/a | n/a |
| docker (PID 85677) vms_mb | MB | 39 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 85701) rss_mb | MB | 1 | 26.859 | 26.859 | 26.859 | 26.859 | n/a | n/a |
| docker (PID 85701) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 85724) CPU | percent | 2 | 98.741 | 98.560 | 98.922 | 98.922 | 0.200000 CPU seconds | n/a |
| python3 (PID 85724) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 85724) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 85724) rss_mb | MB | 3 | 28.033 | 21.664 | 33.914 | 33.914 | n/a | n/a |
| python3 (PID 85724) vms_mb | MB | 3 | 51.760 | 45.652 | 57.461 | 57.461 | n/a | n/a |
| docker (PID 85737) rss_mb | MB | 1 | 26.188 | 26.188 | 26.188 | 26.188 | n/a | n/a |
| docker (PID 85737) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 85753) rss_mb | MB | 1 | 26.941 | 26.941 | 26.941 | 26.941 | n/a | n/a |
| docker (PID 85753) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 85776) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 85776) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 85776) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 85776) rss_mb | MB | 3 | 27.241 | 26.246 | 27.738 | 27.738 | n/a | n/a |
| docker (PID 85776) vms_mb | MB | 3 | 1708.609 | 1660.273 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [bear_0000] (PID 85818) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bear_0000] (PID 85818) rss_mb | MB | 4 | 3.653 | 0.633 | 12.715 | 0.633 | n/a | n/a |
| docker-init [bear_0000] (PID 85818) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 85830) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 85830) rss_mb | MB | 3 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [bear_0000] (PID 85830) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 85862) rss_mb | MB | 1 | 8.676 | 8.676 | 8.676 | 8.676 | n/a | n/a |
| docker (PID 85862) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 85897) rss_mb | MB | 1 | 27.426 | 27.426 | 27.426 | 27.426 | n/a | n/a |
| docker (PID 85897) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 85932) rss_mb | MB | 1 | 27.559 | 27.559 | 27.559 | 27.559 | n/a | n/a |
| docker (PID 85932) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 85950) rss_mb | MB | 1 | 10.914 | 10.914 | 10.914 | 10.914 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 85950) vms_mb | MB | 1 | 1641.707 | 1641.707 | 1641.707 | 1641.707 | n/a | n/a |
| docker (PID 85967) rss_mb | MB | 1 | 27.133 | 27.133 | 27.133 | 27.133 | n/a | n/a |
| docker (PID 85967) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 86017) rss_mb | MB | 1 | 13.012 | 13.012 | 13.012 | 13.012 | n/a | n/a |
| docker (PID 86017) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 86025) rss_mb | MB | 1 | 25.371 | 25.371 | 25.371 | 25.371 | n/a | n/a |
| docker (PID 86025) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 86068) CPU | percent | 3 | 6.501 | 0.000 | 19.503 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 86068) rss_mb | MB | 4 | 3.521 | 0.566 | 12.387 | 0.566 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 86068) vms_mb | MB | 4 | 393.408 | 1.055 | 1570.469 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 86080) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 86080) rss_mb | MB | 3 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [bear_0000] (PID 86080) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 86090) rss_mb | MB | 1 | 27.246 | 27.246 | 27.246 | 27.246 | n/a | n/a |
| docker (PID 86090) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 86119) rss_mb | MB | 1 | 27.422 | 27.422 | 27.422 | 27.422 | n/a | n/a |
| docker (PID 86119) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 86139) rss_mb | MB | 1 | 11.703 | 11.703 | 11.703 | 11.703 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 86139) vms_mb | MB | 1 | 1498.223 | 1498.223 | 1498.223 | 1498.223 | n/a | n/a |
| docker (PID 86153) rss_mb | MB | 1 | 27.195 | 27.195 | 27.195 | 27.195 | n/a | n/a |
| docker (PID 86153) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| sh [bear_0000] (PID 86173) rss_mb | MB | 1 | 1.676 | 1.676 | 1.676 | 1.676 | n/a | n/a |
| sh [bear_0000] (PID 86173) vms_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| docker (PID 86190) rss_mb | MB | 1 | 26.215 | 26.215 | 26.215 | 26.215 | n/a | n/a |
| docker (PID 86190) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 86249) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 86249) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 86249) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 86249) rss_mb | MB | 2 | 25.473 | 25.473 | 25.473 | 25.473 | n/a | n/a |
| docker (PID 86249) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 86288) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 86288) rss_mb | MB | 3 | 4.790 | 0.633 | 13.105 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 86288) vms_mb | MB | 3 | 548.197 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 86303) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 86303) rss_mb | MB | 2 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bear_0000] (PID 86303) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 86313) rss_mb | MB | 1 | 27.246 | 27.246 | 27.246 | 27.246 | n/a | n/a |
| docker (PID 86313) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 86376) rss_mb | MB | 1 | 19.770 | 19.770 | 19.770 | 19.770 | n/a | n/a |
| docker (PID 86376) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 86384) rss_mb | MB | 1 | 25.875 | 25.875 | 25.875 | 25.875 | n/a | n/a |
| docker (PID 86384) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 86433) rss_mb | MB | 1 | 1.637 | 1.637 | 1.637 | 1.637 | n/a | n/a |
| docker (PID 86433) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 86441) rss_mb | MB | 1 | 26.859 | 26.859 | 26.859 | 26.859 | n/a | n/a |
| docker (PID 86441) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 86481) CPU | percent | 2 | 9.755 | 0.000 | 19.510 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 86481) rss_mb | MB | 3 | 2.993 | 0.633 | 7.715 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 86481) vms_mb | MB | 3 | 523.768 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 86494) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 86494) rss_mb | MB | 2 | 1.574 | 1.574 | 1.574 | 1.574 | n/a | n/a |
| tail [bear_0000] (PID 86494) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 86505) rss_mb | MB | 1 | 1.938 | 1.938 | 1.938 | 1.938 | n/a | n/a |
| docker (PID 86505) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 86532) rss_mb | MB | 1 | 27.340 | 27.340 | 27.340 | 27.340 | n/a | n/a |
| docker (PID 86532) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 86551) rss_mb | MB | 1 | 10.781 | 10.781 | 10.781 | 10.781 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 86551) vms_mb | MB | 1 | 1569.711 | 1569.711 | 1569.711 | 1569.711 | n/a | n/a |
| docker (PID 86574) rss_mb | MB | 1 | 26.918 | 26.918 | 26.918 | 26.918 | n/a | n/a |
| docker (PID 86574) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 86616) rss_mb | MB | 1 | 26.469 | 26.469 | 26.469 | 26.469 | n/a | n/a |
| docker (PID 86616) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 86633) rss_mb | MB | 1 | 26.695 | 26.695 | 26.695 | 26.695 | n/a | n/a |
| docker (PID 86633) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [bear_0000] (PID 86672) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bear_0000] (PID 86672) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bear_0000] (PID 86672) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 86685) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 86685) rss_mb | MB | 3 | 1.730 | 1.730 | 1.730 | 1.730 | n/a | n/a |
| tail [bear_0000] (PID 86685) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 86696) rss_mb | MB | 1 | 1.051 | 1.051 | 1.051 | 1.051 | n/a | n/a |
| docker (PID 86696) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 86724) rss_mb | MB | 1 | 27.168 | 27.168 | 27.168 | 27.168 | n/a | n/a |
| docker (PID 86724) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 86743) rss_mb | MB | 1 | 11.059 | 11.059 | 11.059 | 11.059 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 86743) vms_mb | MB | 1 | 1641.836 | 1641.836 | 1641.836 | 1641.836 | n/a | n/a |
| docker (PID 86759) rss_mb | MB | 1 | 27.301 | 27.301 | 27.301 | 27.301 | n/a | n/a |
| docker (PID 86759) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 86777) rss_mb | MB | 1 | 12.176 | 12.176 | 12.176 | 12.176 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 86777) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 86793) rss_mb | MB | 1 | 26.766 | 26.766 | 26.766 | 26.766 | n/a | n/a |
| docker (PID 86793) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 86843) rss_mb | MB | 1 | 23.023 | 23.023 | 23.023 | 23.023 | n/a | n/a |
| docker (PID 86843) vms_mb | MB | 1 | 1524.203 | 1524.203 | 1524.203 | 1524.203 | n/a | n/a |
| docker (PID 86873) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 86873) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 86873) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 86873) rss_mb | MB | 38 | 26.922 | 26.922 | 26.922 | 26.922 | n/a | n/a |
| docker (PID 86873) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 86889) rss_mb | MB | 1 | 25.852 | 25.852 | 25.852 | 25.852 | n/a | n/a |
| docker (PID 86889) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 86917) rss_mb | MB | 1 | 27.000 | 27.000 | 27.000 | 27.000 | n/a | n/a |
| docker (PID 86917) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 86956) CPU | percent | 3 | 3.257 | 0.000 | 9.770 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 86956) rss_mb | MB | 4 | 3.496 | 0.633 | 12.086 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 86956) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 86968) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 86968) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [bear_0000] (PID 86968) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 86978) rss_mb | MB | 1 | 27.184 | 27.184 | 27.184 | 27.184 | n/a | n/a |
| docker (PID 86978) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[0:PARENT] [bear_0000] (PID 86994) rss_mb | MB | 1 | 1.996 | 1.996 | 1.996 | 1.996 | n/a | n/a |
| runc:[0:PARENT] [bear_0000] (PID 86994) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| docker (PID 87072) rss_mb | MB | 1 | 21.703 | 21.703 | 21.703 | 21.703 | n/a | n/a |
| docker (PID 87072) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 87080) rss_mb | MB | 1 | 25.977 | 25.977 | 25.977 | 25.977 | n/a | n/a |
| docker (PID 87080) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 87138) rss_mb | MB | 1 | 25.535 | 25.535 | 25.535 | 25.535 | n/a | n/a |
| docker (PID 87138) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bear_0000] (PID 87179) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bear_0000] (PID 87179) rss_mb | MB | 10 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bear_0000] (PID 87179) vms_mb | MB | 10 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 87192) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 87192) rss_mb | MB | 10 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [bear_0000] (PID 87192) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 87194) rss_mb | MB | 1 | 18.629 | 18.629 | 18.629 | 18.629 | n/a | n/a |
| docker (PID 87194) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 87231) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 87231) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 87231) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 87231) rss_mb | MB | 9 | 27.336 | 27.336 | 27.336 | 27.336 | n/a | n/a |
| docker (PID 87231) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [bear_0000] (PID 87251) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bear_0000] (PID 87251) rss_mb | MB | 8 | 3.422 | 3.422 | 3.422 | 3.422 | n/a | n/a |
| bash [bear_0000] (PID 87251) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bear_0000] (PID 87260) CPU | percent | 6 | 102.836 | 97.302 | 117.623 | 117.623 | 0.630000 CPU seconds | n/a |
| python [bear_0000] (PID 87260) rss_mb | MB | 7 | 31.502 | 14.738 | 41.043 | 41.043 | n/a | n/a |
| python [bear_0000] (PID 87260) vms_mb | MB | 7 | 38.301 | 18.395 | 51.340 | 51.340 | n/a | n/a |
| docker (PID 87270) rss_mb | MB | 1 | 26.160 | 26.160 | 26.160 | 26.160 | n/a | n/a |
| docker (PID 87270) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 87329) rss_mb | MB | 1 | 11.285 | 11.285 | 11.285 | 11.285 | n/a | n/a |
| docker (PID 87329) vms_mb | MB | 1 | 1451.699 | 1451.699 | 1451.699 | 1451.699 | n/a | n/a |
| docker (PID 87338) rss_mb | MB | 1 | 20.195 | 20.195 | 20.195 | 20.195 | n/a | n/a |
| docker (PID 87338) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 87362) CPU | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 87362) io read MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 87362) io write MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 87362) rss_mb | MB | 40 | 26.668 | 26.668 | 26.668 | 26.668 | n/a | n/a |
| docker (PID 87362) vms_mb | MB | 40 | 1588.770 | 1588.770 | 1588.770 | 1588.770 | n/a | n/a |
| docker (PID 87386) rss_mb | MB | 1 | 21.551 | 21.551 | 21.551 | 21.551 | n/a | n/a |
| docker (PID 87386) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| python3 (PID 87409) CPU | percent | 10 | 100.308 | 87.728 | 108.035 | 98.681 | 1.030000 CPU seconds | n/a |
| python3 (PID 87409) io read MB/s | MB/s | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 87409) io write MB/s | MB/s | 10 | 0.219 | 0.000 | 2.186 | 0.000 | 0.222656 MB | n/a |
| python3 (PID 87409) rss_mb | MB | 11 | 27.554 | 10.605 | 34.531 | 34.531 | n/a | n/a |
| python3 (PID 87409) vms_mb | MB | 11 | 51.275 | 36.633 | 57.434 | 57.434 | n/a | n/a |
| docker (PID 87430) rss_mb | MB | 1 | 26.004 | 26.004 | 26.004 | 26.004 | n/a | n/a |
| docker (PID 87430) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 87446) rss_mb | MB | 1 | 16.395 | 16.395 | 16.395 | 16.395 | n/a | n/a |
| docker (PID 87446) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 87461) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 87461) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 87461) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 87461) rss_mb | MB | 2 | 27.357 | 27.113 | 27.602 | 27.602 | n/a | n/a |
| docker (PID 87461) vms_mb | MB | 2 | 1696.775 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [beef_0000] (PID 87501) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beef_0000] (PID 87501) rss_mb | MB | 5 | 3.128 | 0.633 | 13.109 | 0.633 | n/a | n/a |
| docker-init [beef_0000] (PID 87501) vms_mb | MB | 5 | 314.989 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 87516) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 87516) rss_mb | MB | 4 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [beef_0000] (PID 87516) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 87519) rss_mb | MB | 1 | 27.137 | 27.137 | 27.137 | 27.137 | n/a | n/a |
| docker (PID 87519) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] (PID 87538) rss_mb | MB | 1 | 11.645 | 11.645 | 11.645 | 11.645 | n/a | n/a |
| runc:[2:INIT] (PID 87538) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 87616) rss_mb | MB | 1 | 26.254 | 26.254 | 26.254 | 26.254 | n/a | n/a |
| docker (PID 87616) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 87651) rss_mb | MB | 1 | 26.934 | 26.934 | 26.934 | 26.934 | n/a | n/a |
| docker (PID 87651) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 87693) rss_mb | MB | 1 | 18.234 | 18.234 | 18.234 | 18.234 | n/a | n/a |
| docker (PID 87693) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 87709) rss_mb | MB | 1 | 26.945 | 26.945 | 26.945 | 26.945 | n/a | n/a |
| docker (PID 87709) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[0:PARENT] [beef_0000] (PID 87744) rss_mb | MB | 1 | 1.961 | 1.961 | 1.961 | 1.961 | n/a | n/a |
| runc:[0:PARENT] [beef_0000] (PID 87744) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 87749) CPU | percent | 3 | 9.623 | 0.000 | 28.868 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [beef_0000] (PID 87749) rss_mb | MB | 4 | 0.641 | 0.633 | 0.664 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 87749) vms_mb | MB | 4 | 4.318 | 1.055 | 14.109 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 87761) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 87761) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [beef_0000] (PID 87761) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 87772) rss_mb | MB | 1 | 16.512 | 16.512 | 16.512 | 16.512 | n/a | n/a |
| docker (PID 87772) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 87801) rss_mb | MB | 1 | 27.414 | 27.414 | 27.414 | 27.414 | n/a | n/a |
| docker (PID 87801) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 87820) rss_mb | MB | 1 | 11.824 | 11.824 | 11.824 | 11.824 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 87820) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 87836) rss_mb | MB | 1 | 27.430 | 27.430 | 27.430 | 27.430 | n/a | n/a |
| docker (PID 87836) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 87856) rss_mb | MB | 1 | 11.738 | 11.738 | 11.738 | 11.738 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 87856) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 87873) rss_mb | MB | 1 | 26.926 | 26.926 | 26.926 | 26.926 | n/a | n/a |
| docker (PID 87873) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 87934) rss_mb | MB | 1 | 16.270 | 16.270 | 16.270 | 16.270 | n/a | n/a |
| docker (PID 87934) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 87957) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 87957) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 87957) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 87957) rss_mb | MB | 38 | 26.746 | 26.746 | 26.746 | 26.746 | n/a | n/a |
| docker (PID 87957) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 88000) rss_mb | MB | 1 | 25.516 | 25.516 | 25.516 | 25.516 | n/a | n/a |
| docker (PID 88000) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 88041) CPU | percent | 3 | 9.720 | 0.000 | 29.160 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [beef_0000] (PID 88041) rss_mb | MB | 4 | 3.309 | 0.633 | 11.336 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 88041) vms_mb | MB | 4 | 393.215 | 1.055 | 1569.695 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 88055) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 88055) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [beef_0000] (PID 88055) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 88066) rss_mb | MB | 1 | 25.520 | 25.520 | 25.520 | 25.520 | n/a | n/a |
| docker (PID 88066) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 88096) rss_mb | MB | 1 | 27.336 | 27.336 | 27.336 | 27.336 | n/a | n/a |
| docker (PID 88096) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 88115) rss_mb | MB | 1 | 11.664 | 11.664 | 11.664 | 11.664 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 88115) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 88131) rss_mb | MB | 1 | 27.176 | 27.176 | 27.176 | 27.176 | n/a | n/a |
| docker (PID 88131) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| sh [beef_0000] (PID 88153) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sh [beef_0000] (PID 88153) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 88171) rss_mb | MB | 1 | 26.805 | 26.805 | 26.805 | 26.805 | n/a | n/a |
| docker (PID 88171) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 88230) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 88230) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 88230) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 88230) rss_mb | MB | 2 | 23.307 | 19.695 | 26.918 | 26.918 | n/a | n/a |
| docker (PID 88230) vms_mb | MB | 2 | 1588.486 | 1516.199 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 88268) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [beef_0000] (PID 88268) rss_mb | MB | 11 | 1.741 | 0.633 | 12.820 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 88268) vms_mb | MB | 11 | 143.707 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 88281) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 88281) rss_mb | MB | 10 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [beef_0000] (PID 88281) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 88291) rss_mb | MB | 1 | 27.289 | 27.289 | 27.289 | 27.289 | n/a | n/a |
| docker (PID 88291) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 88310) rss_mb | MB | 1 | 11.664 | 11.664 | 11.664 | 11.664 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 88310) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 88318) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 88318) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 88318) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 88318) rss_mb | MB | 8 | 27.258 | 27.258 | 27.258 | 27.258 | n/a | n/a |
| docker (PID 88318) vms_mb | MB | 8 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [beef_0000] (PID 88337) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [beef_0000] (PID 88337) rss_mb | MB | 8 | 3.410 | 3.410 | 3.410 | 3.410 | n/a | n/a |
| bash [beef_0000] (PID 88337) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [beef_0000] (PID 88346) CPU | percent | 7 | 100.631 | 88.092 | 107.905 | 107.887 | 0.720000 CPU seconds | n/a |
| python [beef_0000] (PID 88346) rss_mb | MB | 8 | 30.545 | 9.992 | 41.719 | 41.719 | n/a | n/a |
| python [beef_0000] (PID 88346) vms_mb | MB | 8 | 37.918 | 14.531 | 51.238 | 51.238 | n/a | n/a |
| docker (PID 88358) CPU | percent | 1 | 9.684 | 9.684 | 9.684 | 9.684 | 0.010000 CPU seconds | n/a |
| docker (PID 88358) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 88358) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 88358) rss_mb | MB | 2 | 23.395 | 19.859 | 26.930 | 26.930 | n/a | n/a |
| docker (PID 88358) vms_mb | MB | 2 | 1588.361 | 1515.949 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 88419) rss_mb | MB | 1 | 26.801 | 26.801 | 26.801 | 26.801 | n/a | n/a |
| docker (PID 88419) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| 6 [beef_0000] (PID 88453) rss_mb | MB | 1 | 1.785 | 1.785 | 1.785 | 1.785 | n/a | n/a |
| 6 [beef_0000] (PID 88453) vms_mb | MB | 1 | 13.980 | 13.980 | 13.980 | 13.980 | n/a | n/a |
| docker-init [beef_0000] (PID 88458) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beef_0000] (PID 88458) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [beef_0000] (PID 88458) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 88471) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 88471) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [beef_0000] (PID 88471) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 88473) rss_mb | MB | 1 | 23.168 | 23.168 | 23.168 | 23.168 | n/a | n/a |
| docker (PID 88473) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 88508) rss_mb | MB | 1 | 26.945 | 26.945 | 26.945 | 26.945 | n/a | n/a |
| docker (PID 88508) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 88544) rss_mb | MB | 1 | 26.953 | 26.953 | 26.953 | 26.953 | n/a | n/a |
| docker (PID 88544) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 88564) rss_mb | MB | 1 | 11.762 | 11.762 | 11.762 | 11.762 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 88564) vms_mb | MB | 1 | 1570.348 | 1570.348 | 1570.348 | 1570.348 | n/a | n/a |
| docker (PID 88580) rss_mb | MB | 1 | 26.605 | 26.605 | 26.605 | 26.605 | n/a | n/a |
| docker (PID 88580) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 88624) rss_mb | MB | 1 | 25.637 | 25.637 | 25.637 | 25.637 | n/a | n/a |
| docker (PID 88624) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 88657) rss_mb | MB | 1 | 25.719 | 25.719 | 25.719 | 25.719 | n/a | n/a |
| docker (PID 88657) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 88665) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 88665) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 88665) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 88665) rss_mb | MB | 39 | 25.504 | 25.504 | 25.504 | 25.504 | n/a | n/a |
| docker (PID 88665) vms_mb | MB | 39 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 88698) rss_mb | MB | 1 | 25.520 | 25.520 | 25.520 | 25.520 | n/a | n/a |
| docker (PID 88698) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| python3 (PID 88713) CPU | percent | 3 | 102.128 | 98.537 | 108.811 | 99.036 | 0.310000 CPU seconds | n/a |
| python3 (PID 88713) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 88713) io write MB/s | MB/s | 3 | 0.735 | 0.000 | 2.205 | 2.205 | 0.222656 MB | n/a |
| python3 (PID 88713) rss_mb | MB | 4 | 26.693 | 14.871 | 34.438 | 34.438 | n/a | n/a |
| python3 (PID 88713) vms_mb | MB | 4 | 50.429 | 39.770 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 88743) rss_mb | MB | 1 | 13.797 | 13.797 | 13.797 | 13.797 | n/a | n/a |
| docker (PID 88743) vms_mb | MB | 1 | 1451.699 | 1451.699 | 1451.699 | 1451.699 | n/a | n/a |
| docker (PID 88765) CPU | percent | 2 | 9.867 | 0.000 | 19.733 | 0.000 | 0.020000 CPU seconds | n/a |
| docker (PID 88765) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 88765) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 88765) rss_mb | MB | 3 | 27.286 | 27.047 | 27.406 | 27.406 | n/a | n/a |
| docker (PID 88765) vms_mb | MB | 3 | 1708.776 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [bell_0000] (PID 88804) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bell_0000] (PID 88804) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bell_0000] (PID 88804) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 88817) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 88817) rss_mb | MB | 4 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bell_0000] (PID 88817) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 88858) rss_mb | MB | 1 | 3.488 | 3.488 | 3.488 | 3.488 | n/a | n/a |
| docker (PID 88858) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 88886) rss_mb | MB | 1 | 27.242 | 27.242 | 27.242 | 27.242 | n/a | n/a |
| docker (PID 88886) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 88907) rss_mb | MB | 1 | 4.371 | 4.371 | 4.371 | 4.371 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 88907) vms_mb | MB | 1 | 1224.934 | 1224.934 | 1224.934 | 1224.934 | n/a | n/a |
| docker (PID 88922) rss_mb | MB | 1 | 27.387 | 27.387 | 27.387 | 27.387 | n/a | n/a |
| docker (PID 88922) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 88943) rss_mb | MB | 1 | 11.410 | 11.410 | 11.410 | 11.410 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 88943) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 88959) rss_mb | MB | 1 | 26.035 | 26.035 | 26.035 | 26.035 | n/a | n/a |
| docker (PID 88959) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 89019) rss_mb | MB | 1 | 25.246 | 25.246 | 25.246 | 25.246 | n/a | n/a |
| docker (PID 89019) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 89057) CPU | percent | 3 | 6.429 | 0.000 | 19.286 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bell_0000] (PID 89057) rss_mb | MB | 4 | 3.178 | 0.633 | 10.812 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 89057) vms_mb | MB | 4 | 393.090 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 89073) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 89073) rss_mb | MB | 3 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [bell_0000] (PID 89073) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 89083) rss_mb | MB | 1 | 25.699 | 25.699 | 25.699 | 25.699 | n/a | n/a |
| docker (PID 89083) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 89111) rss_mb | MB | 1 | 27.293 | 27.293 | 27.293 | 27.293 | n/a | n/a |
| docker (PID 89111) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 89131) rss_mb | MB | 1 | 11.336 | 11.336 | 11.336 | 11.336 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 89131) vms_mb | MB | 1 | 1570.098 | 1570.098 | 1570.098 | 1570.098 | n/a | n/a |
| docker (PID 89147) rss_mb | MB | 1 | 27.457 | 27.457 | 27.457 | 27.457 | n/a | n/a |
| docker (PID 89147) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| sh [bell_0000] (PID 89166) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sh [bell_0000] (PID 89166) vms_mb | MB | 1 | 0.516 | 0.516 | 0.516 | 0.516 | n/a | n/a |
| docker (PID 89182) rss_mb | MB | 1 | 26.031 | 26.031 | 26.031 | 26.031 | n/a | n/a |
| docker (PID 89182) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 89262) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 89262) io read MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 89262) io write MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 89262) rss_mb | MB | 37 | 26.855 | 26.855 | 26.855 | 26.855 | n/a | n/a |
| docker (PID 89262) vms_mb | MB | 37 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 89278) rss_mb | MB | 1 | 17.395 | 17.395 | 17.395 | 17.395 | n/a | n/a |
| docker (PID 89278) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 89298) rss_mb | MB | 1 | 26.727 | 26.727 | 26.727 | 26.727 | n/a | n/a |
| docker (PID 89298) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 89306) rss_mb | MB | 1 | 25.742 | 25.742 | 25.742 | 25.742 | n/a | n/a |
| docker (PID 89306) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 89345) CPU | percent | 3 | 3.259 | 0.000 | 9.778 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bell_0000] (PID 89345) rss_mb | MB | 4 | 3.558 | 0.633 | 12.332 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 89345) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 89360) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 89360) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [bell_0000] (PID 89360) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 89370) rss_mb | MB | 1 | 27.500 | 27.500 | 27.500 | 27.500 | n/a | n/a |
| docker (PID 89370) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 89463) rss_mb | MB | 1 | 15.883 | 15.883 | 15.883 | 15.883 | n/a | n/a |
| docker (PID 89463) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 89471) rss_mb | MB | 1 | 25.652 | 25.652 | 25.652 | 25.652 | n/a | n/a |
| docker (PID 89471) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 89533) rss_mb | MB | 1 | 25.715 | 25.715 | 25.715 | 25.715 | n/a | n/a |
| docker (PID 89533) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bell_0000] (PID 89571) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bell_0000] (PID 89571) rss_mb | MB | 11 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bell_0000] (PID 89571) vms_mb | MB | 11 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 89584) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 89584) rss_mb | MB | 11 | 1.809 | 1.809 | 1.809 | 1.809 | n/a | n/a |
| tail [bell_0000] (PID 89584) vms_mb | MB | 11 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 89586) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 89586) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 89620) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 89620) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 89620) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 89620) rss_mb | MB | 9 | 27.477 | 27.477 | 27.477 | 27.477 | n/a | n/a |
| docker (PID 89620) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 89640) CPU | percent | 8 | 2.408 | 0.000 | 19.263 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bell_0000] (PID 89640) rss_mb | MB | 9 | 4.126 | 3.387 | 10.039 | 3.387 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 89640) vms_mb | MB | 9 | 170.257 | 4.391 | 1497.191 | 4.391 | n/a | n/a |
| python [bell_0000] (PID 89648) CPU | percent | 7 | 99.286 | 87.796 | 107.899 | 97.708 | 0.710000 CPU seconds | n/a |
| python [bell_0000] (PID 89648) rss_mb | MB | 8 | 32.335 | 16.047 | 41.750 | 41.750 | n/a | n/a |
| python [bell_0000] (PID 89648) vms_mb | MB | 8 | 39.348 | 19.738 | 51.238 | 51.238 | n/a | n/a |
| docker (PID 89660) CPU | percent | 1 | 9.613 | 9.613 | 9.613 | 9.613 | 0.010000 CPU seconds | n/a |
| docker (PID 89660) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 89660) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 89660) rss_mb | MB | 2 | 23.520 | 20.289 | 26.750 | 26.750 | n/a | n/a |
| docker (PID 89660) vms_mb | MB | 2 | 1624.488 | 1588.203 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 89747) rss_mb | MB | 1 | 26.918 | 26.918 | 26.918 | 26.918 | n/a | n/a |
| docker (PID 89747) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 89755) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 89755) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 89755) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 89755) rss_mb | MB | 39 | 26.695 | 26.695 | 26.695 | 26.695 | n/a | n/a |
| docker (PID 89755) vms_mb | MB | 39 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 89789) rss_mb | MB | 1 | 26.574 | 26.574 | 26.574 | 26.574 | n/a | n/a |
| docker (PID 89789) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 89804) CPU | percent | 3 | 102.029 | 98.456 | 108.711 | 108.711 | 0.310000 CPU seconds | n/a |
| python3 (PID 89804) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 89804) io write MB/s | MB/s | 3 | 0.733 | 0.000 | 2.200 | 2.200 | 0.222656 MB | n/a |
| python3 (PID 89804) rss_mb | MB | 4 | 25.315 | 11.758 | 34.527 | 34.527 | n/a | n/a |
| python3 (PID 89804) vms_mb | MB | 4 | 49.604 | 38.035 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 89823) rss_mb | MB | 1 | 27.051 | 27.051 | 27.051 | 27.051 | n/a | n/a |
| docker (PID 89823) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| sandbox alex_0000 CPU | percent | 24 | 58.256 | 14.131 | 100.193 | 30.900 | 1.426991 CPU seconds | n/a |
| sandbox alex_0000 io read MB/s | MB/s | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox alex_0000 io write MB/s | MB/s | 29 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox alex_0000 memory | MB | 31 | 8.172 | 0.688 | 36.145 | 1.020 | n/a | n/a |
| sandbox alex_0000 net rx MB/s | MB/s | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox alex_0000 net tx MB/s | MB/s | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox andy_0000 CPU | percent | 22 | 59.211 | 17.140 | 100.108 | 30.850 | 1.332701 CPU seconds | n/a |
| sandbox andy_0000 io read MB/s | MB/s | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox andy_0000 io write MB/s | MB/s | 26 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox andy_0000 memory | MB | 28 | 9.676 | 0.621 | 36.375 | 0.797 | n/a | n/a |
| sandbox andy_0000 net rx MB/s | MB/s | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox andy_0000 net tx MB/s | MB/s | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox arch_0000 CPU | percent | 18 | 63.329 | 17.156 | 100.019 | 45.428 | 1.165861 CPU seconds | n/a |
| sandbox arch_0000 io read MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox arch_0000 io write MB/s | MB/s | 21 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox arch_0000 memory | MB | 23 | 10.113 | 0.668 | 35.305 | 0.926 | n/a | n/a |
| sandbox arch_0000 net rx MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox arch_0000 net tx MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bake_0000 CPU | percent | 28 | 52.078 | 0.000 | 100.082 | 33.936 | 1.503757 CPU seconds | n/a |
| sandbox bake_0000 io read MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bake_0000 io write MB/s | MB/s | 32 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bake_0000 memory | MB | 34 | 7.135 | 0.586 | 34.535 | 1.941 | n/a | n/a |
| sandbox bake_0000 net rx MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bake_0000 net tx MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bale_0000 CPU | percent | 43 | 87.896 | 12.038 | 101.144 | 94.242 | 3.856908 CPU seconds | n/a |
| sandbox bale_0000 io read MB/s | MB/s | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bale_0000 io write MB/s | MB/s | 46 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bale_0000 memory | MB | 47 | 24.215 | 0.668 | 34.582 | 3.941 | n/a | n/a |
| sandbox bale_0000 net rx MB/s | MB/s | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bale_0000 net tx MB/s | MB/s | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox band_0000 CPU | percent | 17 | 68.190 | 18.903 | 100.969 | 99.673 | 1.185632 CPU seconds | n/a |
| sandbox band_0000 io read MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox band_0000 io write MB/s | MB/s | 20 | 0.002 | 0.000 | 0.038 | 0.038 | 0.003906 MB | n/a |
| sandbox band_0000 memory | MB | 21 | 11.975 | 0.633 | 35.500 | 23.672 | n/a | n/a |
| sandbox band_0000 net rx MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox band_0000 net tx MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bart_0000 CPU | percent | 26 | 55.838 | 14.058 | 100.116 | 30.367 | 1.488581 CPU seconds | n/a |
| sandbox bart_0000 io read MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bart_0000 io write MB/s | MB/s | 32 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bart_0000 memory | MB | 34 | 7.954 | 0.664 | 35.258 | 0.965 | n/a | n/a |
| sandbox bart_0000 net rx MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bart_0000 net tx MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox base_0000 CPU | percent | 29 | 71.422 | 13.726 | 101.962 | 39.516 | 2.131791 CPU seconds | n/a |
| sandbox base_0000 io read MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox base_0000 io write MB/s | MB/s | 32 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox base_0000 memory | MB | 34 | 15.081 | 0.652 | 35.223 | 0.863 | n/a | n/a |
| sandbox base_0000 net rx MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox base_0000 net tx MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beam_0000 CPU | percent | 19 | 63.294 | 11.279 | 100.250 | 45.399 | 1.229844 CPU seconds | n/a |
| sandbox beam_0000 io read MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beam_0000 io write MB/s | MB/s | 22 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox beam_0000 memory | MB | 24 | 9.418 | 0.660 | 36.434 | 4.328 | n/a | n/a |
| sandbox beam_0000 net rx MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beam_0000 net tx MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bear_0000 CPU | percent | 22 | 59.902 | 12.808 | 112.720 | 88.096 | 1.366272 CPU seconds | n/a |
| sandbox bear_0000 io read MB/s | MB/s | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bear_0000 io write MB/s | MB/s | 28 | 0.001 | 0.000 | 0.034 | 0.034 | 0.003906 MB | n/a |
| sandbox bear_0000 memory | MB | 29 | 8.923 | 0.637 | 34.652 | 33.508 | n/a | n/a |
| sandbox bear_0000 net rx MB/s | MB/s | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bear_0000 net tx MB/s | MB/s | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beef_0000 CPU | percent | 21 | 60.200 | 23.050 | 100.043 | 45.431 | 1.293896 CPU seconds | n/a |
| sandbox beef_0000 io read MB/s | MB/s | 25 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beef_0000 io write MB/s | MB/s | 24 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox beef_0000 memory | MB | 26 | 9.186 | 0.000 | 35.570 | 4.152 | n/a | n/a |
| sandbox beef_0000 net rx MB/s | MB/s | 24 | 77.018 | 0.000 | 1848.431 | 0.000 | 3546.975211 MB | n/a |
| sandbox beef_0000 net tx MB/s | MB/s | 24 | 0.666 | 0.000 | 15.979 | 0.000 | 30.661978 MB | n/a |
| sandbox bell_0000 CPU | percent | 18 | 66.762 | 13.927 | 101.022 | 61.084 | 1.233022 CPU seconds | n/a |
| sandbox bell_0000 io read MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bell_0000 io write MB/s | MB/s | 21 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bell_0000 memory | MB | 22 | 10.977 | 0.777 | 35.375 | 3.910 | n/a | n/a |
| sandbox bell_0000 net rx MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bell_0000 net tx MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| workload total CPU | percent | 6488 | 16.048 | 0.541 | 114.196 | 87.947 | 106.378466 CPU seconds | n/a |
| workload total io read MB/s | MB/s | 405 | 0.002 | 0.000 | 0.688 | 0.000 | 0.070312 MB | n/a |
| workload total io write MB/s | MB/s | 395 | 0.001 | 0.000 | 0.038 | 0.000 | 0.046875 MB | n/a |
| workload total memory | MB | 6489 | 533.296 | 422.586 | 589.203 | 552.305 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
