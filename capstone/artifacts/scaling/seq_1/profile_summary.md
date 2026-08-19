# agprof summary

- Duration: **706.663 s**
- Runs: **24/24 completed**, 24 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.034 runs/s**
- LLM: **85 calls**, 85 succeeded, 0 failed, 0 interrupted, 0 retries, 493.570 s total wait
- Tools: **109/109 completed**, 3 failed, 0 interrupted
- Raw resource samples: **71531** at 9.88 Hz effective (10 Hz configured)
- GPU sampling: **unavailable** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 23382.102 / 40555.061 ms |
| LLM latency p50 / p95 | 3033.195 / 18232.006 ms |
| LLM TTFT p50 / p95 | 640.883 / 1250.339 ms |
| LLM input / output tokens | 444884 / 24405 |
| LLM output throughput | 56.103 tokens/s |
| LLM attempts | 85 total, 85 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 409.453 / 1158.298 ms |

### Tool outcomes

| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 13/13 | 13 | 0 | 0 | 1139.813 ms | 2270.296 ms |
| edit | 13/13 | 13 | 0 | 0 | 416.399 ms | 459.453 ms |
| glob | 4/4 | 4 | 0 | 0 | 335.505 ms | 337.422 ms |
| grep | 2/2 | 2 | 0 | 0 | 330.086 ms | 334.789 ms |
| read | 38/38 | 38 | 0 | 0 | 419.947 ms | 654.707 ms |
| return_plan | 12/12 | 12 | 0 | 0 | 0.336 ms | 0.380 ms |
| return_status | 12/12 | 12 | 0 | 0 | 0.284 ms | 0.533 ms |
| return_summary | 15/15 | 12 | 3 | 0 | 0.349 ms | 0.407 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 15.522% | 110.100% | 110.459 s | 472.177 MB | 530.016 MB | 0.390625 MB | 0.050781 MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python3 | 55012 |  | 6982 | 3.648% | 134.078% | 26.120 s | 688.491 MB | 704.691 MB | 3740.764 MB | 3767.047 MB | 25.164062 MB | 34.722656 MB |
| git | 55018 |  | 5 | 0.000% | 0.000% | 0.000 s | 4.812 MB | 4.812 MB | 12.516 MB | 12.516 MB | 0.000000 MB | 0.000000 MB |
| git | 55019 |  | 5 | 0.000% | 0.000% | 0.000 s | 3.359 MB | 3.359 MB | 11.273 MB | 11.273 MB | 0.000000 MB | 0.000000 MB |
| git-remote-http | 55020 |  | 5 | 4.940% | 19.759% | 0.020 s | 19.163 MB | 19.191 MB | 106.966 MB | 107.566 MB | 0.265625 MB | 0.000000 MB |
| python3 | 55026 |  | 99 | 99.965% | 109.043% | 9.890 s | 33.887 MB | 34.133 MB | 56.178 MB | 56.375 MB | 0.000000 MB | 0.015625 MB |
| python3 | 55027 |  | 4 | 102.325% | 108.876% | 0.310 s | 24.344 MB | 34.281 MB | 48.595 MB | 57.504 MB | 0.000000 MB | 0.015625 MB |
| python3 | 55028 |  | 4 | 99.007% | 108.909% | 0.300 s | 29.860 MB | 36.566 MB | 53.073 MB | 58.516 MB | 0.000000 MB | 0.218750 MB |
| python3 | 55029 |  | 4 | 99.004% | 99.072% | 0.300 s | 26.514 MB | 34.715 MB | 50.386 MB | 57.508 MB | 0.000000 MB | 0.222656 MB |
| python3 | 55030 |  | 25 | 99.886% | 108.957% | 2.420 s | 32.635 MB | 34.762 MB | 56.138 MB | 57.512 MB | 0.000000 MB | 0.222656 MB |
| python3 | 55031 |  | 80 | 99.948% | 108.983% | 8.000 s | 41.489 MB | 47.855 MB | 64.046 MB | 69.637 MB | 0.000000 MB | 0.226562 MB |
| python3 | 55032 |  | 4 | 102.322% | 108.979% | 0.310 s | 26.462 MB | 34.734 MB | 50.420 MB | 57.508 MB | 0.000000 MB | 0.226562 MB |
| python3 | 55033 |  | 99 | 99.873% | 109.053% | 9.880 s | 34.175 MB | 34.363 MB | 56.352 MB | 56.508 MB | 0.000000 MB | 0.015625 MB |
| python3 | 55034 |  | 4 | 102.223% | 108.978% | 0.310 s | 26.435 MB | 34.590 MB | 50.416 MB | 57.492 MB | 0.000000 MB | 0.230469 MB |
| python3 | 55035 |  | 4 | 98.998% | 108.872% | 0.300 s | 29.669 MB | 34.953 MB | 53.134 MB | 57.504 MB | 0.000000 MB | 0.230469 MB |
| python3 | 55036 |  | 4 | 102.317% | 108.952% | 0.310 s | 27.646 MB | 34.793 MB | 51.431 MB | 57.508 MB | 0.000000 MB | 0.230469 MB |
| python3 | 55037 |  | 4 | 102.308% | 108.865% | 0.310 s | 24.476 MB | 34.301 MB | 48.637 MB | 57.504 MB | 0.000000 MB | 0.015625 MB |
| docker | 55092 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.115 MB | 27.633 MB | 1708.776 MB | 1804.781 MB | 0.000000 MB | 0.000000 MB |
| docker | 55147 |  | 1 | n/a% | n/a% | n/a s | 23.523 MB | 23.523 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker-init | 55133 | alex_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 55145 | alex_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 55182 |  | 1 | n/a% | n/a% | n/a s | 27.332 MB | 27.332 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 55273 |  | 1 | n/a% | n/a% | n/a s | 23.250 MB | 23.250 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 55282 |  | 1 | n/a% | n/a% | n/a s | 26.262 MB | 26.262 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 55340 |  | 2 | 9.813% | 9.813% | 0.010 s | 20.086 MB | 25.617 MB | 1552.078 MB | 1588.207 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 55378 | alex_0000 | 4 | 6.553% | 19.658% | 0.020 s | 3.603 MB | 12.512 MB | 411.474 MB | 1642.730 MB | n/a MB | n/a MB |
| docker | 55405 |  | 1 | n/a% | n/a% | n/a s | 27.281 MB | 27.281 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 55425 | alex_0000 | 1 | n/a% | n/a% | n/a s | 4.523 MB | 4.523 MB | 1505.445 MB | 1505.445 MB | n/a MB | n/a MB |
| tail | 55392 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.840 MB | 1.840 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 55452 | alex_0000 | 1 | n/a% | n/a% | n/a s | 12.027 MB | 12.027 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 55432 |  | 1 | n/a% | n/a% | n/a s | 27.191 MB | 27.191 MB | 1733.027 MB | 1733.027 MB | n/a MB | n/a MB |
| docker | 55467 |  | 1 | n/a% | n/a% | n/a s | 27.105 MB | 27.105 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 55486 | alex_0000 | 1 | n/a% | n/a% | n/a s | 11.730 MB | 11.730 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 55503 |  | 1 | n/a% | n/a% | n/a s | 26.879 MB | 26.879 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 55564 |  | 1 | n/a% | n/a% | n/a s | 26.508 MB | 26.508 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| docker | 55618 |  | 1 | n/a% | n/a% | n/a s | 10.340 MB | 10.340 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 55616 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.707 MB | 1.707 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 55603 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 55652 |  | 1 | n/a% | n/a% | n/a s | 27.422 MB | 27.422 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 55693 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.672 MB | 25.672 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 55754 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.691 MB | 26.691 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 55792 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 4.728 MB | 12.918 MB | 524.195 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 55806 | alex_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 55886 |  | 2 | 9.810% | 9.810% | 0.010 s | 17.889 MB | 26.785 MB | 1480.105 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 55946 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.984 MB | 26.984 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| tail | 55998 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 55986 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 56036 |  | 1 | n/a% | n/a% | n/a s | 22.383 MB | 22.383 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 56090 | alex_0000 | 1 | n/a% | n/a% | n/a s | 4.371 MB | 4.371 MB | 1288.934 MB | 1288.934 MB | n/a MB | n/a MB |
| docker | 56071 |  | 1 | n/a% | n/a% | n/a s | 27.250 MB | 27.250 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 56106 |  | 1 | n/a% | n/a% | n/a s | 27.188 MB | 27.188 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 56146 |  | 1 | n/a% | n/a% | n/a s | 25.707 MB | 25.707 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 56185 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.863 MB | 26.863 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 56201 |  | 1 | n/a% | n/a% | n/a s | 25.625 MB | 25.625 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 56227 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.910 MB | 26.910 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 56267 | alex_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.645 MB | 12.680 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 56280 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 56356 |  | 1 | n/a% | n/a% | n/a s | 25.297 MB | 25.297 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 56396 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.910 MB | 26.910 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 56449 |  | 1 | n/a% | n/a% | n/a s | 17.238 MB | 17.238 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 56457 |  | 1 | n/a% | n/a% | n/a s | 26.797 MB | 26.797 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 56496 | alex_0000 | 11 | 1.967% | 19.673% | 0.020 s | 1.549 MB | 10.715 MB | 137.067 MB | 1497.191 MB | n/a MB | n/a MB |
| tail | 56508 | alex_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 56518 |  | 1 | n/a% | n/a% | n/a s | 23.844 MB | 23.844 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 56546 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.309 MB | 27.309 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 56566 | alex_0000 | 9 | 3.672% | 29.373% | 0.030 s | 4.263 MB | 11.082 MB | 186.329 MB | 1641.836 MB | n/a MB | n/a MB |
| python | 56576 | alex_0000 | 8 | 99.402% | 107.876% | 0.710 s | 33.282 MB | 42.535 MB | 40.540 MB | 52.238 MB | n/a MB | n/a MB |
| docker | 56586 |  | 1 | n/a% | n/a% | n/a s | 27.004 MB | 27.004 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 56630 |  | 1 | n/a% | n/a% | n/a s | 18.039 MB | 18.039 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 56648 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.883 MB | 26.883 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 56689 | alex_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.641 MB | 12.664 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 56701 | alex_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 56732 | alex_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| docker | 56712 |  | 1 | n/a% | n/a% | n/a s | 26.844 MB | 26.844 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 56774 |  | 1 | n/a% | n/a% | n/a s | 22.164 MB | 22.164 MB | 1523.953 MB | 1523.953 MB | n/a MB | n/a MB |
| docker | 56811 |  | 1 | n/a% | n/a% | n/a s | 26.035 MB | 26.035 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 56852 |  | 1 | n/a% | n/a% | n/a s | 1.508 MB | 1.508 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 56862 |  | 1 | n/a% | n/a% | n/a s | 9.402 MB | 9.402 MB | 1315.695 MB | 1315.695 MB | n/a MB | n/a MB |
| docker | 56886 |  | 1 | n/a% | n/a% | n/a s | 25.898 MB | 25.898 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 56894 |  | 46 | 0.000% | 0.000% | 0.000 s | 26.652 MB | 26.652 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 56926 |  | 1 | n/a% | n/a% | n/a s | 27.035 MB | 27.035 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 56942 |  | 7 | 67.580% | 88.972% | 0.410 s | 25.224 MB | 34.645 MB | 49.179 MB | 57.438 MB | 5.042969 MB | 0.195312 MB |
| docker | 56971 |  | 1 | n/a% | n/a% | n/a s | 3.227 MB | 3.227 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 56993 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.250 MB | 27.422 MB | 1732.777 MB | 1804.781 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 57035 | andy_0000 | 5 | 4.912% | 19.647% | 0.020 s | 2.978 MB | 12.359 MB | 314.889 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 57050 |  | 1 | n/a% | n/a% | n/a s | 26.988 MB | 26.988 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 57069 |  | 1 | n/a% | n/a% | n/a s | 11.613 MB | 11.613 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 57048 | andy_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 57144 |  | 1 | n/a% | n/a% | n/a s | 20.168 MB | 20.168 MB | 1524.203 MB | 1524.203 MB | n/a MB | n/a MB |
| docker | 57182 |  | 1 | n/a% | n/a% | n/a s | 25.707 MB | 25.707 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 57224 |  | 1 | n/a% | n/a% | n/a s | 4.160 MB | 4.160 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 57241 |  | 1 | n/a% | n/a% | n/a s | 25.234 MB | 25.234 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker-init | 57282 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 57294 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 57296 |  | 1 | n/a% | n/a% | n/a s | 27.012 MB | 27.012 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 57331 |  | 1 | n/a% | n/a% | n/a s | 27.438 MB | 27.438 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 57347 | andy_0000 | 1 | n/a% | n/a% | n/a s | 1.953 MB | 1.953 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| runc:[1:CHILD] | 57350 | andy_0000 | 1 | n/a% | n/a% | n/a s | 0.840 MB | 0.840 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 57387 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.590 MB | 11.590 MB | 1642.352 MB | 1642.352 MB | n/a MB | n/a MB |
| docker | 57367 |  | 1 | n/a% | n/a% | n/a s | 27.398 MB | 27.398 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 57405 |  | 1 | n/a% | n/a% | n/a s | 25.707 MB | 25.707 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 57490 |  | 38 | 0.267% | 9.867% | 0.010 s | 25.879 MB | 26.332 MB | 1649.580 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 57506 |  | 1 | n/a% | n/a% | n/a s | 25.465 MB | 25.465 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 57532 |  | 1 | n/a% | n/a% | n/a s | 27.164 MB | 27.164 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 57586 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 57571 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 57588 |  | 1 | n/a% | n/a% | n/a s | 17.285 MB | 17.285 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 57626 |  | 1 | n/a% | n/a% | n/a s | 27.168 MB | 27.168 MB | 1733.027 MB | 1733.027 MB | n/a MB | n/a MB |
| docker | 57663 |  | 1 | n/a% | n/a% | n/a s | 27.289 MB | 27.289 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 57683 | andy_0000 | 1 | n/a% | n/a% | n/a s | 11.605 MB | 11.605 MB | 1642.352 MB | 1642.352 MB | n/a MB | n/a MB |
| docker | 57702 |  | 1 | n/a% | n/a% | n/a s | 26.977 MB | 26.977 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 57759 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.887 MB | 25.887 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 57799 | andy_0000 | 11 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 57812 | andy_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 57850 |  | 9 | 1.222% | 9.772% | 0.010 s | 24.719 MB | 27.016 MB | 1479.883 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| bash | 57869 | andy_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.418 MB | 3.418 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 57878 | andy_0000 | 8 | 99.433% | 107.889% | 0.710 s | 31.862 MB | 42.754 MB | 38.816 MB | 52.238 MB | n/a MB | n/a MB |
| docker | 57888 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.012 MB | 27.012 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 57948 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.770 MB | 25.770 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 57988 | andy_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.733 MB | 13.035 MB | 411.411 MB | 1642.480 MB | n/a MB | n/a MB |
| tail | 58001 | andy_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 58074 |  | 1 | n/a% | n/a% | n/a s | 25.801 MB | 25.801 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 58111 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.062 MB | 27.062 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 58190 |  | 1 | n/a% | n/a% | n/a s | 26.363 MB | 26.363 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 58198 |  | 39 | 0.000% | 0.000% | 0.000 s | 26.754 MB | 26.754 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 58232 |  | 1 | n/a% | n/a% | n/a s | 26.848 MB | 26.848 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 58249 |  | 4 | 102.076% | 108.507% | 0.310 s | 26.159 MB | 34.504 MB | 50.094 MB | 57.438 MB | 0.000000 MB | 0.214844 MB |
| docker | 58280 |  | 1 | n/a% | n/a% | n/a s | 1.828 MB | 1.828 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 58302 |  | 2 | 9.899% | 9.899% | 0.010 s | 27.035 MB | 27.441 MB | 1732.777 MB | 1804.781 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 58342 | arch_0000 | 5 | 4.918% | 19.672% | 0.020 s | 2.696 MB | 10.949 MB | 314.683 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 58358 |  | 1 | n/a% | n/a% | n/a s | 27.383 MB | 27.383 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 58378 |  | 1 | n/a% | n/a% | n/a s | 10.707 MB | 10.707 MB | 1641.449 MB | 1641.449 MB | n/a MB | n/a MB |
| tail | 58356 | arch_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 58394 |  | 1 | n/a% | n/a% | n/a s | 27.086 MB | 27.086 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 58413 | arch_0000 | 1 | n/a% | n/a% | n/a s | 11.938 MB | 11.938 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 58455 |  | 1 | n/a% | n/a% | n/a s | 0.129 MB | 0.129 MB | 30.570 MB | 30.570 MB | n/a MB | n/a MB |
| docker | 58491 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.090 MB | 27.152 MB | 1660.648 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 58552 |  | 1 | n/a% | n/a% | n/a s | 26.977 MB | 26.977 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker-init | 58590 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.566 MB | 0.566 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 58606 |  | 1 | n/a% | n/a% | n/a s | 20.051 MB | 20.051 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 58603 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 58642 |  | 1 | n/a% | n/a% | n/a s | 27.043 MB | 27.043 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 58677 |  | 1 | n/a% | n/a% | n/a s | 27.352 MB | 27.352 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 58696 | arch_0000 | 1 | n/a% | n/a% | n/a s | 10.344 MB | 10.344 MB | 1641.449 MB | 1641.449 MB | n/a MB | n/a MB |
| docker | 58715 |  | 1 | n/a% | n/a% | n/a s | 26.789 MB | 26.789 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 58755 |  | 1 | n/a% | n/a% | n/a s | 14.605 MB | 14.605 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 58764 |  | 1 | n/a% | n/a% | n/a s | 26.648 MB | 26.648 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 58796 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.781 MB | 26.781 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 58812 |  | 1 | n/a% | n/a% | n/a s | 27.008 MB | 27.008 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 58838 |  | 1 | n/a% | n/a% | n/a s | 25.344 MB | 25.344 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 58892 |  | 1 | n/a% | n/a% | n/a s | 23.727 MB | 23.727 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker-init | 58877 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 58890 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 58944 | arch_0000 | 1 | n/a% | n/a% | n/a s | 1.953 MB | 1.953 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 58928 |  | 1 | n/a% | n/a% | n/a s | 27.168 MB | 27.168 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 58985 | arch_0000 | 1 | n/a% | n/a% | n/a s | 11.324 MB | 11.324 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 58965 |  | 1 | n/a% | n/a% | n/a s | 27.332 MB | 27.332 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 59004 |  | 1 | n/a% | n/a% | n/a s | 26.012 MB | 26.012 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 59045 |  | 1 | n/a% | n/a% | n/a s | 20.133 MB | 20.133 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 59054 |  | 1 | n/a% | n/a% | n/a s | 26.496 MB | 26.496 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 59062 |  | 1 | n/a% | n/a% | n/a s | 27.148 MB | 27.148 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 59102 | arch_0000 | 12 | 1.787% | 19.658% | 0.020 s | 1.633 MB | 12.637 MB | 131.861 MB | 1570.727 MB | n/a MB | n/a MB |
| tail | 59115 | arch_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 59125 |  | 1 | n/a% | n/a% | n/a s | 27.223 MB | 27.223 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 59179 | arch_0000 | 9 | 0.000% | 0.000% | 0.000 s | 4.424 MB | 12.473 MB | 186.401 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 59158 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.031 MB | 27.031 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 59189 | arch_0000 | 8 | 99.290% | 107.747% | 0.710 s | 32.457 MB | 41.938 MB | 39.794 MB | 52.219 MB | n/a MB | n/a MB |
| docker | 59199 |  | 2 | 9.775% | 9.775% | 0.010 s | 14.150 MB | 27.070 MB | 846.768 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 59251 |  | 1 | n/a% | n/a% | n/a s | 24.496 MB | 24.496 MB | 1588.270 MB | 1588.270 MB | n/a MB | n/a MB |
| docker | 59259 |  | 1 | n/a% | n/a% | n/a s | 26.727 MB | 26.727 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 59298 | arch_0000 | 4 | 3.258% | 9.775% | 0.010 s | 3.553 MB | 12.312 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 59320 |  | 1 | n/a% | n/a% | n/a s | 27.309 MB | 27.309 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 59310 | arch_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 59347 |  | 1 | n/a% | n/a% | n/a s | 27.445 MB | 27.445 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 59410 |  | 1 | n/a% | n/a% | n/a s | 23.785 MB | 23.785 MB | 1660.207 MB | 1660.207 MB | n/a MB | n/a MB |
| docker | 59418 |  | 1 | n/a% | n/a% | n/a s | 25.730 MB | 25.730 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 59470 |  | 1 | n/a% | n/a% | n/a s | 5.539 MB | 5.539 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 59503 |  | 38 | 0.000% | 0.000% | 0.000 s | 27.059 MB | 27.059 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 59519 |  | 1 | n/a% | n/a% | n/a s | 13.621 MB | 13.621 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 59544 |  | 1 | n/a% | n/a% | n/a s | 2.027 MB | 2.027 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| python3 | 59551 |  | 4 | 98.852% | 108.834% | 0.300 s | 28.244 MB | 34.633 MB | 51.801 MB | 57.438 MB | 0.000000 MB | 0.214844 MB |
| docker | 59572 |  | 1 | n/a% | n/a% | n/a s | 26.859 MB | 26.859 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 59589 |  | 1 | n/a% | n/a% | n/a s | 26.430 MB | 26.430 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 59603 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.422 MB | 27.422 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 59645 | bake_0000 | 4 | 3.273% | 9.820% | 0.010 s | 3.746 MB | 13.086 MB | 429.475 MB | 1714.734 MB | n/a MB | n/a MB |
| tail | 59659 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 59750 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.168 MB | 11.168 MB | 1641.965 MB | 1641.965 MB | n/a MB | n/a MB |
| docker | 59731 |  | 1 | n/a% | n/a% | n/a s | 27.070 MB | 27.070 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 59766 |  | 1 | n/a% | n/a% | n/a s | 27.363 MB | 27.363 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 59786 | bake_0000 | 1 | n/a% | n/a% | n/a s | 12.477 MB | 12.477 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 59804 |  | 1 | n/a% | n/a% | n/a s | 26.973 MB | 26.973 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 59855 |  | 1 | n/a% | n/a% | n/a s | 21.719 MB | 21.719 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 59906 | bake_0000 | 4 | 6.549% | 19.646% | 0.020 s | 3.477 MB | 12.008 MB | 375.347 MB | 1498.223 MB | n/a MB | n/a MB |
| docker | 59864 |  | 1 | n/a% | n/a% | n/a s | 25.512 MB | 25.512 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 59917 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 59927 |  | 1 | n/a% | n/a% | n/a s | 27.121 MB | 27.121 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 59947 | bake_0000 | 1 | n/a% | n/a% | n/a s | 4.340 MB | 4.340 MB | 1369.191 MB | 1369.191 MB | n/a MB | n/a MB |
| docker | 59981 |  | 1 | n/a% | n/a% | n/a s | 6.398 MB | 6.398 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 60016 |  | 1 | n/a% | n/a% | n/a s | 24.598 MB | 24.598 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 60024 |  | 1 | n/a% | n/a% | n/a s | 25.879 MB | 25.879 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 60084 |  | 2 | 9.818% | 9.818% | 0.010 s | 22.545 MB | 26.547 MB | 1588.236 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 60123 | bake_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.688 MB | 12.855 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 60166 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.777 MB | 11.777 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 60147 |  | 1 | n/a% | n/a% | n/a s | 27.426 MB | 27.426 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| tail | 60136 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.809 MB | 1.809 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 60200 |  | 1 | n/a% | n/a% | n/a s | 27.016 MB | 27.016 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 60246 |  | 2 | 9.707% | 9.707% | 0.010 s | 25.492 MB | 26.895 MB | 1624.490 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 60330 |  | 38 | 0.000% | 0.000% | 0.000 s | 25.215 MB | 25.215 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 60346 |  | 1 | n/a% | n/a% | n/a s | 25.520 MB | 25.520 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 60412 | bake_0000 | 4 | 6.507% | 19.521% | 0.020 s | 3.000 MB | 10.102 MB | 411.153 MB | 1641.449 MB | n/a MB | n/a MB |
| docker | 60372 |  | 1 | n/a% | n/a% | n/a s | 26.410 MB | 26.410 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 60435 |  | 1 | n/a% | n/a% | n/a s | 19.504 MB | 19.504 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| tail | 60425 | bake_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 60463 |  | 1 | n/a% | n/a% | n/a s | 27.188 MB | 27.188 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 60482 | bake_0000 | 1 | n/a% | n/a% | n/a s | 11.820 MB | 11.820 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 60499 |  | 1 | n/a% | n/a% | n/a s | 27.293 MB | 27.293 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| sh | 60524 | bake_0000 | 1 | n/a% | n/a% | n/a s | 1.746 MB | 1.746 MB | 2.617 MB | 2.617 MB | n/a MB | n/a MB |
| sh | 60516 | bake_0000 | 1 | n/a% | n/a% | n/a s | 1.746 MB | 1.746 MB | 2.617 MB | 2.617 MB | n/a MB | n/a MB |
| docker | 60534 |  | 1 | n/a% | n/a% | n/a s | 25.941 MB | 25.941 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 60593 |  | 1 | n/a% | n/a% | n/a s | 26.918 MB | 26.918 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 60649 |  | 1 | n/a% | n/a% | n/a s | 5.719 MB | 5.719 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| tail | 60647 | bake_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 60633 | bake_0000 | 11 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 60684 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.243 MB | 27.312 MB | 1732.722 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| python | 60713 | bake_0000 | 8 | 99.346% | 107.790% | 0.710 s | 32.367 MB | 42.152 MB | 39.237 MB | 51.375 MB | n/a MB | n/a MB |
| bash | 60704 | bake_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.203 MB | 3.203 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 60723 |  | 2 | 9.784% | 9.784% | 0.010 s | 21.465 MB | 27.102 MB | 1588.361 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 60783 |  | 3 | 0.000% | 0.000% | 0.000 s | 25.629 MB | 25.629 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 60821 | bake_0000 | 12 | 5.221% | 57.432% | 0.060 s | 2.613 MB | 12.918 MB | 262.604 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 60834 | bake_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 60845 |  | 3 | 18.273% | 36.545% | 0.040 s | 22.000 MB | 27.430 MB | 1636.500 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[1:CHILD] | 60864 | bake_0000 | 1 | n/a% | n/a% | n/a s | 0.125 MB | 0.125 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 60860 | bake_0000 | 1 | n/a% | n/a% | n/a s | 1.961 MB | 1.961 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| docker | 60871 |  | 3 | 28.485% | 56.969% | 0.070 s | 18.072 MB | 27.043 MB | 1117.372 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 60891 | bake_0000 | 1 | n/a% | n/a% | n/a s | 12.527 MB | 12.527 MB | 1570.727 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 60906 |  | 2 | 58.680% | 58.680% | 0.060 s | 22.008 MB | 26.980 MB | 1588.361 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 60926 | bake_0000 | 1 | n/a% | n/a% | n/a s | 4.055 MB | 4.055 MB | 1216.680 MB | 1216.680 MB | n/a MB | n/a MB |
| docker | 60941 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.152 MB | 27.152 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 61017 |  | 1 | n/a% | n/a% | n/a s | 18.961 MB | 18.961 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 61025 |  | 39 | 0.000% | 0.000% | 0.000 s | 26.664 MB | 26.664 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| docker | 61059 |  | 1 | n/a% | n/a% | n/a s | 25.387 MB | 25.387 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| python3 | 61074 |  | 4 | 98.778% | 98.881% | 0.300 s | 25.631 MB | 34.488 MB | 49.737 MB | 57.434 MB | 0.000000 MB | 0.214844 MB |
| docker | 61111 |  | 1 | n/a% | n/a% | n/a s | 21.762 MB | 21.762 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 61126 |  | 2 | 9.867% | 9.867% | 0.010 s | 27.023 MB | 27.238 MB | 1696.775 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 61167 | bale_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.719 MB | 12.977 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 61179 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 61181 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 61243 |  | 1 | n/a% | n/a% | n/a s | 18.105 MB | 18.105 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 61279 |  | 1 | n/a% | n/a% | n/a s | 27.379 MB | 27.379 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 61317 |  | 1 | n/a% | n/a% | n/a s | 26.910 MB | 26.910 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 61367 |  | 1 | n/a% | n/a% | n/a s | 2.074 MB | 2.074 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 61376 |  | 1 | n/a% | n/a% | n/a s | 25.543 MB | 25.543 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 61417 | bale_0000 | 4 | 9.726% | 29.178% | 0.030 s | 3.439 MB | 11.859 MB | 393.281 MB | 1569.961 MB | n/a MB | n/a MB |
| docker | 61439 |  | 1 | n/a% | n/a% | n/a s | 27.363 MB | 27.363 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 61429 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 61494 |  | 1 | n/a% | n/a% | n/a s | 2.688 MB | 2.688 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 61502 |  | 1 | n/a% | n/a% | n/a s | 27.254 MB | 27.254 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| sh | 61521 | bale_0000 | 1 | n/a% | n/a% | n/a s | 1.656 MB | 1.656 MB | 2.617 MB | 2.617 MB | n/a MB | n/a MB |
| base64 | 61528 | bale_0000 | 1 | n/a% | n/a% | n/a s | 1.422 MB | 1.422 MB | 2.586 MB | 2.586 MB | n/a MB | n/a MB |
| docker | 61538 |  | 1 | n/a% | n/a% | n/a s | 25.902 MB | 25.902 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 61590 |  | 1 | n/a% | n/a% | n/a s | 6.574 MB | 6.574 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 61620 |  | 38 | 0.000% | 0.000% | 0.000 s | 25.660 MB | 25.660 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 61636 |  | 1 | n/a% | n/a% | n/a s | 24.328 MB | 24.328 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 61654 |  | 1 | n/a% | n/a% | n/a s | 13.809 MB | 13.809 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 61701 | bale_0000 | 4 | 6.456% | 19.369% | 0.020 s | 3.237 MB | 11.051 MB | 393.215 MB | 1569.695 MB | n/a MB | n/a MB |
| docker | 61662 |  | 1 | n/a% | n/a% | n/a s | 27.137 MB | 27.137 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 61713 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 61723 |  | 1 | n/a% | n/a% | n/a s | 26.711 MB | 26.711 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 61749 |  | 1 | n/a% | n/a% | n/a s | 27.164 MB | 27.164 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 61769 | bale_0000 | 1 | n/a% | n/a% | n/a s | 12.426 MB | 12.426 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 61816 |  | 1 | n/a% | n/a% | n/a s | 1.781 MB | 1.781 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 61824 |  | 1 | n/a% | n/a% | n/a s | 26.926 MB | 26.926 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 61886 |  | 1 | n/a% | n/a% | n/a s | 25.586 MB | 25.586 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker-init | 61923 | bale_0000 | 37 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 61937 | bale_0000 | 37 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 61941 |  | 1 | n/a% | n/a% | n/a s | 20.902 MB | 20.902 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 61977 |  | 35 | 0.000% | 0.000% | 0.000 s | 27.512 MB | 27.512 MB | 1661.023 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| bash | 61996 | bale_0000 | 34 | 0.000% | 0.000% | 0.000 s | 3.348 MB | 3.348 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 62005 | bale_0000 | 34 | 99.875% | 107.998% | 3.360 s | 39.027 MB | 41.773 MB | 47.798 MB | 51.289 MB | n/a MB | n/a MB |
| docker | 62015 |  | 1 | n/a% | n/a% | n/a s | 26.090 MB | 26.090 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 62074 |  | 2 | 9.858% | 9.858% | 0.010 s | 25.391 MB | 26.773 MB | 1624.490 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 62114 | bale_0000 | 4 | 3.261% | 9.783% | 0.010 s | 3.631 MB | 12.625 MB | 375.347 MB | 1498.223 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 62153 | bale_0000 | 1 | n/a% | n/a% | n/a s | 10.301 MB | 10.301 MB | 1569.695 MB | 1569.695 MB | n/a MB | n/a MB |
| tail | 62125 | bale_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.695 MB | 1.695 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 62135 |  | 1 | n/a% | n/a% | n/a s | 27.426 MB | 27.426 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 62188 |  | 1 | n/a% | n/a% | n/a s | 9.680 MB | 9.680 MB | 1387.949 MB | 1387.949 MB | n/a MB | n/a MB |
| docker | 62222 |  | 1 | n/a% | n/a% | n/a s | 26.848 MB | 26.848 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 62231 |  | 1 | n/a% | n/a% | n/a s | 25.945 MB | 25.945 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 62293 |  | 1 | n/a% | n/a% | n/a s | 7.219 MB | 7.219 MB | 32.867 MB | 32.867 MB | n/a MB | n/a MB |
| docker | 62317 |  | 39 | 0.260% | 9.867% | 0.010 s | 26.958 MB | 26.988 MB | 1660.761 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 62341 |  | 1 | n/a% | n/a% | n/a s | 26.949 MB | 26.949 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 62364 |  | 34 | 99.601% | 108.863% | 3.340 s | 32.531 MB | 34.617 MB | 55.402 MB | 57.438 MB | 0.000000 MB | 0.214844 MB |
| docker | 62394 |  | 1 | n/a% | n/a% | n/a s | 0.270 MB | 0.270 MB | 32.750 MB | 32.750 MB | n/a MB | n/a MB |
| docker | 62416 |  | 2 | 9.857% | 9.857% | 0.010 s | 27.340 MB | 27.707 MB | 1733.027 MB | 1805.031 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 62456 | band_0000 | 5 | 4.900% | 19.602% | 0.020 s | 2.752 MB | 11.230 MB | 314.733 MB | 1569.445 MB | n/a MB | n/a MB |
| tail | 62470 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 62492 |  | 1 | n/a% | n/a% | n/a s | 11.133 MB | 11.133 MB | 1641.707 MB | 1641.707 MB | n/a MB | n/a MB |
| docker | 62472 |  | 1 | n/a% | n/a% | n/a s | 27.305 MB | 27.305 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 62509 |  | 1 | n/a% | n/a% | n/a s | 27.535 MB | 27.535 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 62531 | band_0000 | 1 | n/a% | n/a% | n/a s | 11.691 MB | 11.691 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 62572 |  | 1 | n/a% | n/a% | n/a s | 17.266 MB | 17.266 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 62611 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.824 MB | 26.824 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 62668 |  | 1 | n/a% | n/a% | n/a s | 25.387 MB | 25.387 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 62721 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 62723 |  | 1 | n/a% | n/a% | n/a s | 23.730 MB | 23.730 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker-init | 62708 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 62759 |  | 1 | n/a% | n/a% | n/a s | 27.297 MB | 27.297 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 62793 |  | 1 | n/a% | n/a% | n/a s | 27.309 MB | 27.309 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 62813 | band_0000 | 1 | n/a% | n/a% | n/a s | 10.641 MB | 10.641 MB | 1569.445 MB | 1569.445 MB | n/a MB | n/a MB |
| docker | 62830 |  | 1 | n/a% | n/a% | n/a s | 26.824 MB | 26.824 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 62897 |  | 1 | n/a% | n/a% | n/a s | 26.766 MB | 26.766 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 62911 |  | 37 | 0.000% | 0.000% | 0.000 s | 26.645 MB | 26.645 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 62927 |  | 1 | n/a% | n/a% | n/a s | 26.746 MB | 26.746 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| docker | 62945 |  | 1 | n/a% | n/a% | n/a s | 25.625 MB | 25.625 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 62993 | band_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.475 MB | 12.000 MB | 375.284 MB | 1497.973 MB | n/a MB | n/a MB |
| docker | 62953 |  | 1 | n/a% | n/a% | n/a s | 26.918 MB | 26.918 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 63004 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 63015 |  | 1 | n/a% | n/a% | n/a s | 27.371 MB | 27.371 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 63034 | band_0000 | 1 | n/a% | n/a% | n/a s | 10.301 MB | 10.301 MB | 1569.445 MB | 1569.445 MB | n/a MB | n/a MB |
| docker | 63068 |  | 1 | n/a% | n/a% | n/a s | 15.523 MB | 15.523 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 63116 |  | 1 | n/a% | n/a% | n/a s | 25.762 MB | 25.762 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 63168 |  | 1 | n/a% | n/a% | n/a s | 23.070 MB | 23.070 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 63176 |  | 1 | n/a% | n/a% | n/a s | 26.973 MB | 26.973 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 63216 | band_0000 | 11 | 1.961% | 19.607% | 0.020 s | 1.693 MB | 12.297 MB | 150.252 MB | 1642.230 MB | n/a MB | n/a MB |
| tail | 63229 | band_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 63239 |  | 1 | n/a% | n/a% | n/a s | 26.973 MB | 26.973 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| bash | 63289 | band_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.301 MB | 3.301 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 63269 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.160 MB | 27.160 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 63299 | band_0000 | 7 | 99.548% | 107.427% | 0.610 s | 32.273 MB | 41.957 MB | 39.022 MB | 51.324 MB | n/a MB | n/a MB |
| docker | 63301 |  | 1 | n/a% | n/a% | n/a s | 0.129 MB | 0.129 MB | 30.570 MB | 30.570 MB | n/a MB | n/a MB |
| docker | 63309 |  | 1 | n/a% | n/a% | n/a s | 27.141 MB | 27.141 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 63367 |  | 1 | n/a% | n/a% | n/a s | 25.340 MB | 25.340 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker-init | 63406 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 63419 | band_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.711 MB | 1.711 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 63421 |  | 1 | n/a% | n/a% | n/a s | 21.418 MB | 21.418 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 63459 |  | 1 | n/a% | n/a% | n/a s | 27.305 MB | 27.305 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 63516 | band_0000 | 1 | n/a% | n/a% | n/a s | 11.469 MB | 11.469 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 63495 |  | 1 | n/a% | n/a% | n/a s | 27.453 MB | 27.453 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 63532 |  | 1 | n/a% | n/a% | n/a s | 26.879 MB | 26.879 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 63618 |  | 1 | n/a% | n/a% | n/a s | 25.621 MB | 25.621 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 63626 |  | 46 | 0.000% | 0.000% | 0.000 s | 26.855 MB | 26.855 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 63658 |  | 1 | n/a% | n/a% | n/a s | 0.410 MB | 0.410 MB | 30.602 MB | 30.602 MB | n/a MB | n/a MB |
| python3 | 63673 |  | 4 | 98.787% | 98.948% | 0.300 s | 24.244 MB | 34.422 MB | 48.571 MB | 57.438 MB | 0.000000 MB | 0.210938 MB |
| docker | 63695 |  | 1 | n/a% | n/a% | n/a s | 8.965 MB | 8.965 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 63711 |  | 1 | n/a% | n/a% | n/a s | 26.945 MB | 26.945 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 63725 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.277 MB | 27.277 MB | 1733.027 MB | 1733.027 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 63766 | bart_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 63778 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.723 MB | 1.723 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 63816 |  | 1 | n/a% | n/a% | n/a s | 5.129 MB | 5.129 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 63844 |  | 1 | n/a% | n/a% | n/a s | 27.434 MB | 27.434 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 63880 |  | 1 | n/a% | n/a% | n/a s | 27.117 MB | 27.117 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 63900 | bart_0000 | 1 | n/a% | n/a% | n/a s | 11.070 MB | 11.070 MB | 1569.840 MB | 1569.840 MB | n/a MB | n/a MB |
| docker | 63916 |  | 1 | n/a% | n/a% | n/a s | 26.293 MB | 26.293 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 63966 |  | 1 | n/a% | n/a% | n/a s | 19.117 MB | 19.117 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 64016 | bart_0000 | 4 | 6.520% | 19.561% | 0.020 s | 3.577 MB | 12.410 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 63974 |  | 1 | n/a% | n/a% | n/a s | 26.574 MB | 26.574 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 64037 |  | 1 | n/a% | n/a% | n/a s | 27.410 MB | 27.410 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 64027 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 64067 |  | 1 | n/a% | n/a% | n/a s | 27.551 MB | 27.551 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 64130 |  | 1 | n/a% | n/a% | n/a s | 6.281 MB | 6.281 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 64138 |  | 1 | n/a% | n/a% | n/a s | 26.707 MB | 26.707 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 64198 |  | 2 | 9.841% | 9.841% | 0.010 s | 20.109 MB | 26.805 MB | 1588.236 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 64238 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 4.734 MB | 12.938 MB | 524.112 MB | 1570.227 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 64283 | bart_0000 | 1 | n/a% | n/a% | n/a s | 11.664 MB | 11.664 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 64251 | bart_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 64264 |  | 1 | n/a% | n/a% | n/a s | 27.078 MB | 27.078 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 64323 |  | 1 | n/a% | n/a% | n/a s | 17.656 MB | 17.656 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 64332 |  | 1 | n/a% | n/a% | n/a s | 27.109 MB | 27.109 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 64392 |  | 1 | n/a% | n/a% | n/a s | 25.223 MB | 25.223 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 64445 |  | 1 | n/a% | n/a% | n/a s | 22.016 MB | 22.016 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| tail | 64443 | bart_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 64430 | bart_0000 | 2 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 64480 |  | 1 | n/a% | n/a% | n/a s | 27.238 MB | 27.238 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 64521 |  | 1 | n/a% | n/a% | n/a s | 26.863 MB | 26.863 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 64557 |  | 1 | n/a% | n/a% | n/a s | 22.883 MB | 22.883 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 64574 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.887 MB | 26.887 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 64613 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 4.704 MB | 12.848 MB | 524.195 MB | 1570.477 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 64657 | bart_0000 | 1 | n/a% | n/a% | n/a s | 11.984 MB | 11.984 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 64627 | bart_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 64637 |  | 1 | n/a% | n/a% | n/a s | 27.176 MB | 27.176 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 64699 |  | 1 | n/a% | n/a% | n/a s | 23.000 MB | 23.000 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 64736 |  | 1 | n/a% | n/a% | n/a s | 26.027 MB | 26.027 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 64777 |  | 1 | n/a% | n/a% | n/a s | 16.914 MB | 16.914 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 64794 |  | 1 | n/a% | n/a% | n/a s | 19.883 MB | 19.883 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 64816 |  | 38 | 0.000% | 0.000% | 0.000 s | 25.609 MB | 25.609 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 64859 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.859 MB | 25.859 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 64899 | bart_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.705 MB | 12.922 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 64911 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 64940 | bart_0000 | 1 | n/a% | n/a% | n/a s | 12.250 MB | 12.250 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 64921 |  | 1 | n/a% | n/a% | n/a s | 26.879 MB | 26.879 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 64983 |  | 1 | n/a% | n/a% | n/a s | 10.039 MB | 10.039 MB | 1459.953 MB | 1459.953 MB | n/a MB | n/a MB |
| docker | 65021 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.809 MB | 25.809 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 65082 |  | 2 | 0.000% | 0.000% | 0.000 s | 24.977 MB | 26.992 MB | 1660.490 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 65122 | bart_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.744 MB | 12.859 MB | 143.729 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 65145 |  | 1 | n/a% | n/a% | n/a s | 27.270 MB | 27.270 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 65165 | bart_0000 | 1 | n/a% | n/a% | n/a s | 12.078 MB | 12.078 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 65135 | bart_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| python | 65203 | bart_0000 | 8 | 100.786% | 107.906% | 0.720 s | 30.654 MB | 40.742 MB | 37.943 MB | 50.324 MB | n/a MB | n/a MB |
| bash | 65193 | bart_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.410 MB | 3.410 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 65173 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.531 MB | 27.531 MB | 1661.023 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| docker | 65214 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.914 MB | 26.914 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 65264 |  | 1 | n/a% | n/a% | n/a s | 1.625 MB | 1.625 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 65312 | bart_0000 | 4 | 6.515% | 19.546% | 0.020 s | 3.400 MB | 11.703 MB | 411.280 MB | 1641.957 MB | n/a MB | n/a MB |
| docker | 65272 |  | 1 | n/a% | n/a% | n/a s | 25.488 MB | 25.488 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 65336 |  | 1 | n/a% | n/a% | n/a s | 27.645 MB | 27.645 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 65326 | bart_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 65363 |  | 1 | n/a% | n/a% | n/a s | 27.281 MB | 27.281 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 65382 | bart_0000 | 1 | n/a% | n/a% | n/a s | 12.105 MB | 12.105 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 65427 |  | 1 | n/a% | n/a% | n/a s | 16.211 MB | 16.211 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 65436 |  | 1 | n/a% | n/a% | n/a s | 26.168 MB | 26.168 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 65503 |  | 1 | n/a% | n/a% | n/a s | 15.250 MB | 15.250 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 65519 |  | 40 | 0.000% | 0.000% | 0.000 s | 25.762 MB | 25.762 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 65536 |  | 1 | n/a% | n/a% | n/a s | 23.129 MB | 23.129 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 65561 |  | 1 | n/a% | n/a% | n/a s | 20.820 MB | 20.820 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| python3 | 65568 |  | 4 | 102.067% | 108.458% | 0.310 s | 27.472 MB | 34.449 MB | 51.167 MB | 57.438 MB | 0.003906 MB | 0.210938 MB |
| docker | 65582 |  | 1 | n/a% | n/a% | n/a s | 2.801 MB | 2.801 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 65623 |  | 3 | 9.712% | 19.425% | 0.020 s | 18.742 MB | 27.617 MB | 1214.275 MB | 1805.031 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 65665 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.664 MB | 12.758 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 65677 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 65709 |  | 1 | n/a% | n/a% | n/a s | 18.121 MB | 18.121 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 65744 |  | 1 | n/a% | n/a% | n/a s | 27.441 MB | 27.441 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 65797 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.770 MB | 11.770 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 65778 |  | 1 | n/a% | n/a% | n/a s | 27.191 MB | 27.191 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 65814 |  | 1 | n/a% | n/a% | n/a s | 25.836 MB | 25.836 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 65873 |  | 1 | n/a% | n/a% | n/a s | 27.332 MB | 27.332 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 65913 | base_0000 | 7 | 3.244% | 19.464% | 0.020 s | 2.058 MB | 10.844 MB | 225.075 MB | 1569.195 MB | n/a MB | n/a MB |
| tail | 65927 | base_0000 | 6 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 65938 |  | 1 | n/a% | n/a% | n/a s | 27.141 MB | 27.141 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 65957 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.473 MB | 11.473 MB | 1642.230 MB | 1642.230 MB | n/a MB | n/a MB |
| docker | 65965 |  | 2 | 48.833% | 48.833% | 0.050 s | 18.020 MB | 27.320 MB | 1444.104 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 65985 | base_0000 | 1 | n/a% | n/a% | n/a s | 10.312 MB | 10.312 MB | 1569.195 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 66000 |  | 1 | n/a% | n/a% | n/a s | 27.137 MB | 27.137 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 66036 |  | 3 | 9.717% | 19.433% | 0.020 s | 23.216 MB | 27.059 MB | 1612.415 MB | 1660.773 MB | 0.109375 MB | 0.000000 MB |
| docker | 66120 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.856 MB | 26.941 MB | 1658.864 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 66144 |  | 1 | n/a% | n/a% | n/a s | 12.742 MB | 12.742 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| docker | 66163 |  | 1 | n/a% | n/a% | n/a s | 25.469 MB | 25.469 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker-init | 66202 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 66218 |  | 1 | n/a% | n/a% | n/a s | 2.633 MB | 2.633 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| tail | 66216 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 66254 |  | 1 | n/a% | n/a% | n/a s | 27.105 MB | 27.105 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 66313 | base_0000 | 1 | n/a% | n/a% | n/a s | 10.398 MB | 10.398 MB | 1569.445 MB | 1569.445 MB | n/a MB | n/a MB |
| docker | 66292 |  | 1 | n/a% | n/a% | n/a s | 27.445 MB | 27.445 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 66331 |  | 1 | n/a% | n/a% | n/a s | 26.004 MB | 26.004 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 66372 |  | 1 | n/a% | n/a% | n/a s | 22.387 MB | 22.387 MB | 1524.203 MB | 1524.203 MB | n/a MB | n/a MB |
| docker | 66389 |  | 1 | n/a% | n/a% | n/a s | 26.633 MB | 26.633 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 66427 | base_0000 | 11 | 0.941% | 9.411% | 0.010 s | 1.713 MB | 12.512 MB | 150.275 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 66452 |  | 1 | n/a% | n/a% | n/a s | 26.988 MB | 26.988 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 66440 | base_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.711 MB | 1.711 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 66473 | base_0000 | 1 | n/a% | n/a% | n/a s | 8.934 MB | 8.934 MB | 1569.195 MB | 1569.195 MB | n/a MB | n/a MB |
| bash | 66500 | base_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.480 MB | 3.480 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 66509 | base_0000 | 8 | 99.305% | 107.845% | 0.710 s | 29.877 MB | 41.652 MB | 37.432 MB | 51.027 MB | n/a MB | n/a MB |
| docker | 66481 |  | 9 | 0.000% | 0.000% | 0.000 s | 27.125 MB | 27.223 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 66519 |  | 1 | n/a% | n/a% | n/a s | 26.914 MB | 26.914 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 66578 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.730 MB | 25.730 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 66621 | base_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.718 MB | 12.973 MB | 393.473 MB | 1570.727 MB | n/a MB | n/a MB |
| tail | 66634 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.824 MB | 1.824 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 66644 |  | 1 | n/a% | n/a% | n/a s | 27.086 MB | 27.086 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 66692 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.766 MB | 11.766 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 66671 |  | 1 | n/a% | n/a% | n/a s | 27.328 MB | 27.328 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 66731 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.605 MB | 11.605 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 66711 |  | 1 | n/a% | n/a% | n/a s | 27.141 MB | 27.141 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 66749 |  | 1 | n/a% | n/a% | n/a s | 27.059 MB | 27.059 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 66790 |  | 1 | n/a% | n/a% | n/a s | 20.734 MB | 20.734 MB | 1524.203 MB | 1524.203 MB | n/a MB | n/a MB |
| docker | 66808 |  | 3 | 9.858% | 19.716% | 0.020 s | 20.931 MB | 25.961 MB | 1590.790 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 66848 | base_0000 | 10 | 2.167% | 19.501% | 0.020 s | 1.801 MB | 12.316 MB | 157.972 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 66871 |  | 1 | n/a% | n/a% | n/a s | 11.594 MB | 11.594 MB | 1515.699 MB | 1515.699 MB | n/a MB | n/a MB |
| tail | 66860 | base_0000 | 9 | 0.000% | 0.000% | 0.000 s | 1.688 MB | 1.688 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 66897 |  | 7 | 0.000% | 0.000% | 0.000 s | 27.184 MB | 27.184 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| bash | 66918 | base_0000 | 6 | 0.000% | 0.000% | 0.000 s | 3.328 MB | 3.328 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 66927 | base_0000 | 6 | 99.520% | 107.701% | 0.510 s | 26.216 MB | 34.762 MB | 33.558 MB | 45.023 MB | n/a MB | n/a MB |
| docker | 66937 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.902 MB | 25.902 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 66988 |  | 1 | n/a% | n/a% | n/a s | 26.211 MB | 26.211 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 67036 | base_0000 | 4 | 9.643% | 28.928% | 0.030 s | 3.392 MB | 11.668 MB | 411.250 MB | 1641.836 MB | n/a MB | n/a MB |
| docker | 66996 |  | 1 | n/a% | n/a% | n/a s | 25.465 MB | 25.465 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 67050 | base_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 67062 |  | 1 | n/a% | n/a% | n/a s | 16.430 MB | 16.430 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 67111 | base_0000 | 1 | n/a% | n/a% | n/a s | 10.203 MB | 10.203 MB | 1569.195 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 67090 |  | 1 | n/a% | n/a% | n/a s | 26.988 MB | 26.988 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 67127 |  | 1 | n/a% | n/a% | n/a s | 27.410 MB | 27.410 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 67147 | base_0000 | 1 | n/a% | n/a% | n/a s | 11.859 MB | 11.859 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 67165 |  | 1 | n/a% | n/a% | n/a s | 26.172 MB | 26.172 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 67240 |  | 1 | n/a% | n/a% | n/a s | 25.859 MB | 25.859 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 67248 |  | 39 | 0.000% | 0.000% | 0.000 s | 26.793 MB | 26.793 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 67280 |  | 1 | n/a% | n/a% | n/a s | 26.965 MB | 26.965 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 67295 |  | 4 | 102.052% | 108.796% | 0.310 s | 26.506 MB | 34.602 MB | 50.372 MB | 57.441 MB | 0.000000 MB | 0.199219 MB |
| docker | 67300 |  | 1 | n/a% | n/a% | n/a s | 25.320 MB | 25.320 MB | 1588.207 MB | 1588.207 MB | n/a MB | n/a MB |
| docker | 67347 |  | 3 | 0.000% | 0.000% | 0.000 s | 27.225 MB | 27.484 MB | 1756.779 MB | 1804.781 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 67388 | beam_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.719 MB | 12.977 MB | 393.410 MB | 1570.477 MB | n/a MB | n/a MB |
| tail | 67400 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 67464 |  | 1 | n/a% | n/a% | n/a s | 27.043 MB | 27.043 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 67485 | beam_0000 | 1 | n/a% | n/a% | n/a s | 8.508 MB | 8.508 MB | 1569.195 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 67500 |  | 1 | n/a% | n/a% | n/a s | 27.477 MB | 27.477 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 67520 | beam_0000 | 1 | n/a% | n/a% | n/a s | 11.480 MB | 11.480 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 67537 |  | 1 | n/a% | n/a% | n/a s | 26.070 MB | 26.070 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 67594 |  | 2 | 9.848% | 9.848% | 0.010 s | 15.043 MB | 27.055 MB | 846.643 MB | 1660.523 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 67634 | beam_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.484 MB | 12.039 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 67658 |  | 1 | n/a% | n/a% | n/a s | 26.922 MB | 26.922 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 67647 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 67678 | beam_0000 | 1 | n/a% | n/a% | n/a s | 10.801 MB | 10.801 MB | 1641.578 MB | 1641.578 MB | n/a MB | n/a MB |
| docker | 67713 |  | 1 | n/a% | n/a% | n/a s | 12.039 MB | 12.039 MB | 1451.699 MB | 1451.699 MB | n/a MB | n/a MB |
| docker | 67758 |  | 2 | 9.774% | 9.774% | 0.010 s | 15.012 MB | 26.715 MB | 846.768 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 67838 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.941 MB | 26.941 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 67872 |  | 1 | n/a% | n/a% | n/a s | 5.094 MB | 5.094 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 67921 | beam_0000 | 4 | 9.768% | 29.305% | 0.030 s | 3.213 MB | 10.953 MB | 393.090 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 67880 |  | 1 | n/a% | n/a% | n/a s | 27.094 MB | 27.094 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 67943 |  | 1 | n/a% | n/a% | n/a s | 26.934 MB | 26.934 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 67933 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.637 MB | 1.637 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 67971 |  | 1 | n/a% | n/a% | n/a s | 27.230 MB | 27.230 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 67992 | beam_0000 | 1 | n/a% | n/a% | n/a s | 12.145 MB | 12.145 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 68038 |  | 1 | n/a% | n/a% | n/a s | 0.844 MB | 0.844 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 68046 |  | 1 | n/a% | n/a% | n/a s | 25.879 MB | 25.879 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 68098 |  | 1 | n/a% | n/a% | n/a s | 23.508 MB | 23.508 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 68145 | beam_0000 | 11 | 0.971% | 9.715% | 0.010 s | 1.645 MB | 11.762 MB | 143.683 MB | 1569.969 MB | n/a MB | n/a MB |
| docker | 68106 |  | 1 | n/a% | n/a% | n/a s | 26.781 MB | 26.781 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 68159 | beam_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.727 MB | 1.727 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 68169 |  | 1 | n/a% | n/a% | n/a s | 27.258 MB | 27.258 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| bash | 68215 | beam_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.410 MB | 3.410 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 68196 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.062 MB | 27.062 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 68224 | beam_0000 | 7 | 99.665% | 107.951% | 0.610 s | 32.780 MB | 42.730 MB | 40.680 MB | 52.238 MB | n/a MB | n/a MB |
| docker | 68226 |  | 1 | n/a% | n/a% | n/a s | 25.688 MB | 25.688 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 68234 |  | 1 | n/a% | n/a% | n/a s | 26.027 MB | 26.027 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 68334 | beam_0000 | 4 | 6.467% | 19.402% | 0.020 s | 3.079 MB | 10.418 MB | 393.215 MB | 1569.695 MB | n/a MB | n/a MB |
| docker | 68293 |  | 1 | n/a% | n/a% | n/a s | 25.676 MB | 25.676 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 68357 |  | 1 | n/a% | n/a% | n/a s | 13.031 MB | 13.031 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| tail | 68346 | beam_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 68404 | beam_0000 | 1 | n/a% | n/a% | n/a s | 11.344 MB | 11.344 MB | 1570.098 MB | 1570.098 MB | n/a MB | n/a MB |
| docker | 68384 |  | 1 | n/a% | n/a% | n/a s | 27.086 MB | 27.086 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 68419 |  | 1 | n/a% | n/a% | n/a s | 27.570 MB | 27.570 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| sh | 68439 | beam_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.516 MB | 0.516 MB | n/a MB | n/a MB |
| docker | 68455 |  | 1 | n/a% | n/a% | n/a s | 26.070 MB | 26.070 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 68533 |  | 1 | n/a% | n/a% | n/a s | 9.402 MB | 9.402 MB | 1235.438 MB | 1235.438 MB | n/a MB | n/a MB |
| docker | 68541 |  | 39 | 0.000% | 0.000% | 0.000 s | 25.844 MB | 25.844 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 68557 |  | 1 | n/a% | n/a% | n/a s | 25.520 MB | 25.520 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 68581 |  | 1 | n/a% | n/a% | n/a s | 25.215 MB | 25.215 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| python3 | 68589 |  | 3 | 98.693% | 98.860% | 0.200 s | 26.586 MB | 33.609 MB | 49.964 MB | 56.379 MB | 0.000000 MB | 0.000000 MB |
| docker | 68594 |  | 1 | n/a% | n/a% | n/a s | 25.246 MB | 25.246 MB | 1587.957 MB | 1587.957 MB | n/a MB | n/a MB |
| docker | 68618 |  | 1 | n/a% | n/a% | n/a s | 17.910 MB | 17.910 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 68640 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.230 MB | 27.469 MB | 1732.777 MB | 1732.777 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 68681 | bear_0000 | 5 | 4.798% | 19.190% | 0.020 s | 1.380 MB | 4.367 MB | 300.282 MB | 1497.191 MB | n/a MB | n/a MB |
| runc:[0:PARENT] | 68678 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 68696 |  | 1 | n/a% | n/a% | n/a s | 26.902 MB | 26.902 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 68694 | bear_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 68734 |  | 1 | n/a% | n/a% | n/a s | 27.430 MB | 27.430 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 68755 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.133 MB | 11.133 MB | 1641.836 MB | 1641.836 MB | n/a MB | n/a MB |
| docker | 68791 |  | 1 | n/a% | n/a% | n/a s | 20.199 MB | 20.199 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 68837 |  | 2 | 0.000% | 0.000% | 0.000 s | 20.869 MB | 25.746 MB | 1588.080 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 68896 |  | 1 | n/a% | n/a% | n/a s | 25.613 MB | 25.613 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker-init | 68937 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 68950 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.805 MB | 1.805 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 68952 |  | 1 | n/a% | n/a% | n/a s | 5.594 MB | 5.594 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 68988 |  | 1 | n/a% | n/a% | n/a s | 26.637 MB | 26.637 MB | 1660.523 MB | 1660.523 MB | n/a MB | n/a MB |
| docker | 69024 |  | 1 | n/a% | n/a% | n/a s | 26.961 MB | 26.961 MB | 1732.777 MB | 1732.777 MB | n/a MB | n/a MB |
| docker | 69061 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.879 MB | 26.879 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 69120 |  | 1 | n/a% | n/a% | n/a s | 25.746 MB | 25.746 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 69159 | bear_0000 | 3 | 9.805% | 19.610% | 0.020 s | 2.681 MB | 6.777 MB | 523.852 MB | 1569.445 MB | n/a MB | n/a MB |
| docker | 69183 |  | 1 | n/a% | n/a% | n/a s | 20.109 MB | 20.109 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| tail | 69173 | bear_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.773 MB | 1.773 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 69230 | bear_0000 | 1 | n/a% | n/a% | n/a s | 10.555 MB | 10.555 MB | 1569.453 MB | 1569.453 MB | n/a MB | n/a MB |
| docker | 69210 |  | 1 | n/a% | n/a% | n/a s | 27.285 MB | 27.285 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 69253 |  | 1 | n/a% | n/a% | n/a s | 25.785 MB | 25.785 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 69293 |  | 1 | n/a% | n/a% | n/a s | 23.070 MB | 23.070 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 69310 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.793 MB | 25.793 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 69352 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.422 MB | 0.633 MB | 1.010 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 69365 | bear_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 69446 |  | 2 | 0.000% | 0.000% | 0.000 s | 17.719 MB | 26.723 MB | 1444.104 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 69505 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.336 MB | 27.336 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 69544 | bear_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.659 MB | 12.738 MB | 393.348 MB | 1570.227 MB | n/a MB | n/a MB |
| tail | 69556 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.836 MB | 1.836 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 69587 | bear_0000 | 1 | n/a% | n/a% | n/a s | 11.809 MB | 11.809 MB | 1570.477 MB | 1570.477 MB | n/a MB | n/a MB |
| docker | 69568 |  | 1 | n/a% | n/a% | n/a s | 27.555 MB | 27.555 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 69629 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 30.535 MB | 30.535 MB | n/a MB | n/a MB |
| docker | 69666 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.820 MB | 25.820 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 69748 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.660 MB | 26.660 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 69792 |  | 1 | n/a% | n/a% | n/a s | 26.633 MB | 26.633 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker-init | 69833 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 69848 |  | 1 | n/a% | n/a% | n/a s | 4.473 MB | 4.473 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| tail | 69845 | bear_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.734 MB | 1.734 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 69883 |  | 1 | n/a% | n/a% | n/a s | 26.680 MB | 26.680 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 69921 |  | 1 | n/a% | n/a% | n/a s | 27.402 MB | 27.402 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 69940 | bear_0000 | 1 | n/a% | n/a% | n/a s | 2.590 MB | 2.590 MB | 1111.484 MB | 1111.484 MB | n/a MB | n/a MB |
| docker | 69958 |  | 1 | n/a% | n/a% | n/a s | 26.008 MB | 26.008 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 70001 |  | 1 | n/a% | n/a% | n/a s | 23.438 MB | 23.438 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 70010 |  | 1 | n/a% | n/a% | n/a s | 23.070 MB | 23.070 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 70019 |  | 1 | n/a% | n/a% | n/a s | 26.746 MB | 26.746 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 70058 | bear_0000 | 11 | 1.950% | 19.496% | 0.020 s | 1.678 MB | 12.125 MB | 143.706 MB | 1570.219 MB | n/a MB | n/a MB |
| docker | 70081 |  | 1 | n/a% | n/a% | n/a s | 27.254 MB | 27.254 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 70071 | bear_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| bash | 70127 | bear_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.391 MB | 3.391 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| python | 70135 | bear_0000 | 8 | 99.325% | 107.872% | 0.710 s | 29.737 MB | 41.742 MB | 37.483 MB | 51.340 MB | n/a MB | n/a MB |
| docker | 70108 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.461 MB | 27.461 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 70137 |  | 1 | n/a% | n/a% | n/a s | 20.375 MB | 20.375 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 70146 |  | 1 | n/a% | n/a% | n/a s | 25.914 MB | 25.914 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 70197 |  | 1 | n/a% | n/a% | n/a s | 9.242 MB | 9.242 MB | 1443.695 MB | 1443.695 MB | n/a MB | n/a MB |
| docker | 70222 |  | 1 | n/a% | n/a% | n/a s | 25.336 MB | 25.336 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 70232 |  | 38 | 0.000% | 0.000% | 0.000 s | 26.539 MB | 26.539 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 70248 |  | 1 | n/a% | n/a% | n/a s | 20.500 MB | 20.500 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 70272 |  | 1 | n/a% | n/a% | n/a s | 1.824 MB | 1.824 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| python3 | 70280 |  | 4 | 98.754% | 98.914% | 0.300 s | 28.187 MB | 34.625 MB | 51.798 MB | 57.438 MB | 0.000000 MB | 0.214844 MB |
| docker | 70294 |  | 1 | n/a% | n/a% | n/a s | 16.570 MB | 16.570 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 70332 |  | 2 | 9.844% | 9.844% | 0.010 s | 27.057 MB | 27.254 MB | 1768.779 MB | 1804.781 MB | 0.000000 MB | 0.000000 MB |
| runc:[0:PARENT] | 70372 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| tail | 70389 | beef_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 70391 |  | 1 | n/a% | n/a% | n/a s | 27.230 MB | 27.230 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker-init | 70375 | beef_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 70427 |  | 1 | n/a% | n/a% | n/a s | 27.328 MB | 27.328 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 70445 | beef_0000 | 1 | n/a% | n/a% | n/a s | 12.004 MB | 12.004 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 70481 |  | 1 | n/a% | n/a% | n/a s | 25.770 MB | 25.770 MB | 1660.273 MB | 1660.273 MB | n/a MB | n/a MB |
| docker | 70525 |  | 2 | 9.770% | 9.770% | 0.010 s | 25.000 MB | 27.004 MB | 1624.488 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 70585 |  | 1 | n/a% | n/a% | n/a s | 25.688 MB | 25.688 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| tail | 70636 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 70638 |  | 1 | n/a% | n/a% | n/a s | 1.633 MB | 1.633 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker-init | 70623 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 70673 |  | 1 | n/a% | n/a% | n/a s | 26.676 MB | 26.676 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 70710 |  | 1 | n/a% | n/a% | n/a s | 27.133 MB | 27.133 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 70745 |  | 1 | n/a% | n/a% | n/a s | 25.738 MB | 25.738 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 70787 |  | 1 | n/a% | n/a% | n/a s | 17.184 MB | 17.184 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 70813 |  | 1 | n/a% | n/a% | n/a s | 18.109 MB | 18.109 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 70828 |  | 38 | 0.000% | 0.000% | 0.000 s | 25.219 MB | 25.219 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 70870 |  | 1 | n/a% | n/a% | n/a s | 26.785 MB | 26.785 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 70924 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 70926 |  | 1 | n/a% | n/a% | n/a s | 13.098 MB | 13.098 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker-init | 70909 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 70963 |  | 1 | n/a% | n/a% | n/a s | 27.082 MB | 27.082 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 71000 |  | 1 | n/a% | n/a% | n/a s | 26.973 MB | 26.973 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 71021 | beef_0000 | 1 | n/a% | n/a% | n/a s | 10.898 MB | 10.898 MB | 1569.703 MB | 1569.703 MB | n/a MB | n/a MB |
| docker | 71039 |  | 1 | n/a% | n/a% | n/a s | 27.055 MB | 27.055 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 71081 |  | 1 | n/a% | n/a% | n/a s | 9.766 MB | 9.766 MB | 1387.949 MB | 1387.949 MB | n/a MB | n/a MB |
| docker | 71098 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.723 MB | 26.723 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| runc:[2:INIT] | 71138 | beef_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.820 MB | 13.105 MB | 158.022 MB | 1570.727 MB | n/a MB | n/a MB |
| docker | 71159 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| tail | 71149 | beef_0000 | 9 | 0.000% | 0.000% | 0.000 s | 1.789 MB | 1.789 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| python | 71219 | beef_0000 | 8 | 100.653% | 107.873% | 0.720 s | 31.119 MB | 42.578 MB | 38.135 MB | 52.238 MB | n/a MB | n/a MB |
| bash | 71209 | beef_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.395 MB | 3.395 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 71189 |  | 8 | 0.000% | 0.000% | 0.000 s | 27.398 MB | 27.398 MB | 1661.023 MB | 1661.023 MB | 0.000000 MB | 0.000000 MB |
| docker | 71229 |  | 1 | n/a% | n/a% | n/a s | 26.047 MB | 26.047 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 71288 |  | 1 | n/a% | n/a% | n/a s | 26.652 MB | 26.652 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 71337 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.793 MB | 1.793 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 71326 | beef_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 71348 |  | 1 | n/a% | n/a% | n/a s | 3.641 MB | 3.641 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 71395 | beef_0000 | 1 | n/a% | n/a% | n/a s | 10.141 MB | 10.141 MB | 1569.195 MB | 1569.195 MB | n/a MB | n/a MB |
| docker | 71375 |  | 1 | n/a% | n/a% | n/a s | 27.117 MB | 27.117 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 71410 |  | 1 | n/a% | n/a% | n/a s | 27.477 MB | 27.477 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 71429 | beef_0000 | 1 | n/a% | n/a% | n/a s | 11.859 MB | 11.859 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 71446 |  | 1 | n/a% | n/a% | n/a s | 26.082 MB | 26.082 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker | 71542 |  | 39 | 0.000% | 0.000% | 0.000 s | 26.652 MB | 26.652 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 71574 |  | 1 | n/a% | n/a% | n/a s | 22.621 MB | 22.621 MB | 1660.207 MB | 1660.207 MB | n/a MB | n/a MB |
| python3 | 71591 |  | 4 | 98.748% | 108.777% | 0.300 s | 24.560 MB | 34.410 MB | 48.618 MB | 57.457 MB | 0.000000 MB | 0.214844 MB |
| docker | 71596 |  | 1 | n/a% | n/a% | n/a s | 19.641 MB | 19.641 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 71620 |  | 1 | n/a% | n/a% | n/a s | 26.984 MB | 26.984 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 71642 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.352 MB | 27.688 MB | 1697.025 MB | 1733.027 MB | 0.000000 MB | 0.000000 MB |
| runc:[0:PARENT] | 71679 |  | 1 | n/a% | n/a% | n/a s | 1.996 MB | 1.996 MB | 14.109 MB | 14.109 MB | n/a MB | n/a MB |
| runc:[1:CHILD] | 71681 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker-init | 71682 | bell_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 71698 |  | 1 | n/a% | n/a% | n/a s | 27.551 MB | 27.551 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| tail | 71696 | bell_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.703 MB | 1.703 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 71733 |  | 1 | n/a% | n/a% | n/a s | 27.203 MB | 27.203 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 71753 | bell_0000 | 1 | n/a% | n/a% | n/a s | 11.961 MB | 11.961 MB | 1642.480 MB | 1642.480 MB | n/a MB | n/a MB |
| docker | 71788 |  | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| docker | 71831 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.797 MB | 25.797 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 71891 |  | 1 | n/a% | n/a% | n/a s | 25.699 MB | 25.699 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker-init | 71931 | bell_0000 | 3 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 71943 | bell_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.641 MB | 1.641 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 72000 | bell_0000 | 1 | n/a% | n/a% | n/a s | 10.547 MB | 10.547 MB | 1569.453 MB | 1569.453 MB | n/a MB | n/a MB |
| docker | 71979 |  | 1 | n/a% | n/a% | n/a s | 26.992 MB | 26.992 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| runc:[2:INIT] | 72034 | bell_0000 | 1 | n/a% | n/a% | n/a s | 11.387 MB | 11.387 MB | 1570.227 MB | 1570.227 MB | n/a MB | n/a MB |
| docker | 72015 |  | 1 | n/a% | n/a% | n/a s | 27.133 MB | 27.133 MB | 1661.023 MB | 1661.023 MB | n/a MB | n/a MB |
| docker | 72050 |  | 1 | n/a% | n/a% | n/a s | 26.883 MB | 26.883 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 72116 |  | 1 | n/a% | n/a% | n/a s | 19.715 MB | 19.715 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 72130 |  | 48 | 0.000% | 0.000% | 0.000 s | 26.746 MB | 26.746 MB | 1660.523 MB | 1660.523 MB | 0.000000 MB | 0.000000 MB |
| docker | 72146 |  | 1 | n/a% | n/a% | n/a s | 27.020 MB | 27.020 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| docker | 72174 |  | 2 | 0.000% | 0.000% | 0.000 s | 26.707 MB | 26.707 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| tail | 72226 | bell_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.306 MB | 1.641 MB | 2.849 MB | 2.984 MB | n/a MB | n/a MB |
| docker-init | 72213 | bell_0000 | 4 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| docker | 72265 |  | 1 | n/a% | n/a% | n/a s | 4.094 MB | 4.094 MB | 32.762 MB | 32.762 MB | n/a MB | n/a MB |
| docker | 72300 |  | 1 | n/a% | n/a% | n/a s | 19.961 MB | 19.961 MB | 1516.199 MB | 1516.199 MB | n/a MB | n/a MB |
| docker | 72337 |  | 2 | 0.000% | 0.000% | 0.000 s | 27.070 MB | 27.070 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 72396 |  | 1 | n/a% | n/a% | n/a s | 25.676 MB | 25.676 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |
| docker-init | 72435 | bell_0000 | 11 | 0.000% | 0.000% | 0.000 s | 0.633 MB | 0.633 MB | 1.055 MB | 1.055 MB | n/a MB | n/a MB |
| tail | 72449 | bell_0000 | 11 | 0.000% | 0.000% | 0.000 s | 1.738 MB | 1.738 MB | 2.984 MB | 2.984 MB | n/a MB | n/a MB |
| docker | 72451 |  | 1 | n/a% | n/a% | n/a s | 23.266 MB | 23.266 MB | 1587.953 MB | 1587.953 MB | n/a MB | n/a MB |
| docker | 72487 |  | 9 | 1.225% | 9.799% | 0.010 s | 26.809 MB | 26.809 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| python | 72517 | bell_0000 | 8 | 100.697% | 107.805% | 0.720 s | 31.858 MB | 42.348 MB | 39.046 MB | 52.238 MB | n/a MB | n/a MB |
| bash | 72507 | bell_0000 | 8 | 0.000% | 0.000% | 0.000 s | 3.402 MB | 3.402 MB | 4.391 MB | 4.391 MB | n/a MB | n/a MB |
| docker | 72527 |  | 2 | 0.000% | 0.000% | 0.000 s | 25.961 MB | 25.961 MB | 1660.211 MB | 1660.211 MB | 0.000000 MB | 0.000000 MB |
| docker | 72597 |  | 1 | n/a% | n/a% | n/a s | 20.172 MB | 20.172 MB | 1588.203 MB | 1588.203 MB | n/a MB | n/a MB |
| docker | 72621 |  | 40 | 0.000% | 0.000% | 0.000 s | 26.230 MB | 26.230 MB | 1660.773 MB | 1660.773 MB | 0.000000 MB | 0.000000 MB |
| docker | 72645 |  | 1 | n/a% | n/a% | n/a s | 14.238 MB | 14.238 MB | 1515.949 MB | 1515.949 MB | n/a MB | n/a MB |
| docker | 72662 |  | 1 | n/a% | n/a% | n/a s | 26.766 MB | 26.766 MB | 1660.773 MB | 1660.773 MB | n/a MB | n/a MB |
| python3 | 72670 |  | 4 | 98.759% | 108.843% | 0.300 s | 28.585 MB | 34.691 MB | 52.115 MB | 57.438 MB | 0.000000 MB | 0.214844 MB |
| docker | 72672 |  | 1 | n/a% | n/a% | n/a s | 8.832 MB | 8.832 MB | 1227.434 MB | 1227.434 MB | n/a MB | n/a MB |
| docker | 72696 |  | 1 | n/a% | n/a% | n/a s | 25.297 MB | 25.297 MB | 1660.211 MB | 1660.211 MB | n/a MB | n/a MB |

## GPU metrics

_No GPU samples were collected._

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| alex_0000 | 54.077% | 101.244% | 1.492 s | 7.778 MB | 36.281 MB | 0.007812 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| andy_0000 | 61.563% | 100.138% | 1.194 s | 9.818 MB | 36.270 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| arch_0000 | 62.930% | 100.693% | 1.289 s | 10.022 MB | 35.664 MB | 0.054688 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bake_0000 | 51.661% | 100.085% | 1.647 s | 7.391 MB | 35.676 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bale_0000 | 83.815% | 100.172% | 3.935 s | 22.370 MB | 35.254 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| band_0000 | 62.693% | 100.438% | 1.220 s | 9.182 MB | 35.312 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bart_0000 | 53.847% | 100.166% | 1.434 s | 7.764 MB | 34.484 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| base_0000 | 60.333% | 101.044% | 2.103 s | 9.290 MB | 35.328 MB | 0.000000 MB | 0.007812 MB | 0.000000 MB | 0.000000 MB |
| beam_0000 | 61.950% | 100.148% | 1.274 s | 9.229 MB | 36.219 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bear_0000 | 56.973% | 100.130% | 1.342 s | 7.760 MB | 35.344 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| beef_0000 | 64.413% | 100.067% | 1.123 s | 10.536 MB | 36.324 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |
| bell_0000 | 65.098% | 100.065% | 1.199 s | 10.635 MB | 36.465 MB | 0.000000 MB | 0.003906 MB | 0.000000 MB | 0.000000 MB |

## Incomplete spans

_No spans were still open when profiling stopped._

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sync:result_wait | 24/24 | 0 | 0 | 651.236 | 0.005 | 651.230 | 27134.815 | 23381.395 | 40554.903 |
| turn | 85/85 | 0 | 0 | 551.071 | 2.792 | 548.234 | 6483.189 | 3928.453 | 18253.983 |
| llm:attempt | 85/85 | 0 | 0 | 493.570 | 2.263 | 491.289 | 5806.706 | 3033.195 | 18232.006 |
| run:diagnose_bug | 12/12 | 0 | 0 | 394.215 | 1.614 | 392.572 | 32851.279 | 27751.036 | 62590.149 |
| llm:diagnose_bug | 34/34 | 0 | 0 | 323.423 | 1.313 | 322.095 | 9512.447 | 3165.528 | 20618.525 |
| run:repair_bug | 12/12 | 0 | 0 | 257.031 | 1.312 | 255.703 | 21419.265 | 18490.104 | 35529.247 |
| llm:repair_bug | 51/51 | 0 | 0 | 170.169 | 0.971 | 169.194 | 3336.644 | 3006.232 | 6008.700 |
| teardown:commit | 24/24 | 0 | 0 | 100.005 | 0.059 | 99.946 | 4166.876 | 4120.426 | 4887.722 |
| sandbox:commit | 24/24 | 0 | 0 | 99.514 | 0.046 | 99.467 | 4146.397 | 4100.583 | 4868.041 |
| capstone:plan:find_first_in_sorted | 1/1 | 0 | 0 | 99.311 | 0.001 | 99.310 | 99310.952 | 99310.952 | 99310.952 |
| capstone:build:find_first_in_sorted | 1/1 | 0 | 0 | 41.969 | 0.001 | 41.968 | 41968.787 | 41968.787 | 41968.787 |
| tool_dispatch:repair_bug | 51/51 | 0 | 0 | 35.320 | 0.240 | 35.069 | 692.551 | 588.274 | 1384.225 |
| capstone:plan:bucketsort | 1/1 | 0 | 0 | 32.547 | 0.001 | 32.545 | 32546.577 | 32546.577 | 32546.577 |
| capstone:plan:mergesort | 1/1 | 0 | 0 | 31.992 | 0.002 | 31.990 | 31992.367 | 31992.367 | 31992.367 |
| capstone:plan:next_palindrome | 1/1 | 0 | 0 | 30.739 | 0.001 | 30.738 | 30738.965 | 30738.965 | 30738.965 |
| capstone:build:mergesort | 1/1 | 0 | 0 | 30.261 | 0.000 | 30.260 | 30260.796 | 30260.796 | 30260.796 |
| capstone:plan:rpn_eval | 1/1 | 0 | 0 | 29.157 | 0.001 | 29.156 | 29157.274 | 29157.274 | 29157.274 |
| capstone:plan:bitcount | 1/1 | 0 | 0 | 28.225 | 0.001 | 28.224 | 28225.094 | 28225.094 | 28225.094 |
| capstone:plan:flatten | 1/1 | 0 | 0 | 27.278 | 0.001 | 27.277 | 27277.558 | 27277.558 | 27277.558 |
| capstone:plan:levenshtein | 1/1 | 0 | 0 | 24.402 | 0.001 | 24.402 | 24402.467 | 24402.467 | 24402.467 |
| capstone:plan:hanoi | 1/1 | 0 | 0 | 23.620 | 0.001 | 23.619 | 23619.676 | 23619.676 | 23619.676 |
| capstone:plan:powerset | 1/1 | 0 | 0 | 23.413 | 0.001 | 23.413 | 23413.486 | 23413.486 | 23413.486 |
| capstone:plan:gcd | 1/1 | 0 | 0 | 23.351 | 0.001 | 23.350 | 23350.635 | 23350.635 | 23350.635 |
| tool_dispatch:diagnose_bug | 34/34 | 0 | 0 | 22.095 | 0.204 | 21.876 | 649.861 | 513.888 | 1393.863 |
| capstone:build:powerset | 1/1 | 0 | 0 | 21.307 | 0.001 | 21.307 | 21307.353 | 21307.353 | 21307.353 |
| capstone:build:levenshtein | 1/1 | 0 | 0 | 21.282 | 0.001 | 21.281 | 21281.677 | 21281.677 | 21281.677 |
| capstone:build:rpn_eval | 1/1 | 0 | 0 | 20.593 | 0.001 | 20.593 | 20593.136 | 20593.136 | 20593.136 |
| capstone:plan:is_valid_parenthesization | 1/1 | 0 | 0 | 20.184 | 0.001 | 20.184 | 20184.213 | 20184.213 | 20184.213 |
| sandbox:exec | 19/19 | 0 | 0 | 19.586 | 0.045 | 19.539 | 1030.834 | 1124.963 | 1482.899 |
| sandbox:start | 70/70 | 0 | 0 | 19.205 | 0.114 | 19.084 | 274.363 | 239.081 | 393.533 |
| capstone:build:is_valid_parenthesization | 1/1 | 0 | 0 | 18.838 | 0.001 | 18.838 | 18838.451 | 18838.451 | 18838.451 |
| tool:read | 38/38 | 0 | 0 | 18.777 | 0.180 | 18.579 | 494.143 | 419.947 | 654.707 |
| capstone:build:bucketsort | 1/1 | 0 | 0 | 18.142 | 0.000 | 18.141 | 18141.874 | 18141.874 | 18141.874 |
| capstone:build:bitcount | 1/1 | 0 | 0 | 18.016 | 0.001 | 18.016 | 18016.037 | 18016.037 | 18016.037 |
| tool:bash | 13/13 | 0 | 0 | 17.601 | 0.039 | 17.561 | 1353.937 | 1139.813 | 2270.296 |
| capstone:build:flatten | 1/1 | 0 | 0 | 16.989 | 0.000 | 16.989 | 16989.433 | 16989.433 | 16989.433 |
| capstone:build:gcd | 1/1 | 0 | 0 | 16.781 | 0.000 | 16.781 | 16781.342 | 16781.342 | 16781.342 |
| capstone:build:hanoi | 1/1 | 0 | 0 | 16.625 | 0.001 | 16.624 | 16625.052 | 16625.052 | 16625.052 |
| capstone:build:next_palindrome | 1/1 | 0 | 0 | 16.229 | 0.001 | 16.228 | 16228.891 | 16228.891 | 16228.891 |
| sandbox:stop | 133/133 | 0 | 0 | 13.988 | 0.109 | 13.877 | 105.174 | 162.052 | 191.863 |
| capstone:prepare:bitcount | 1/1 | 0 | 0 | 10.324 | 0.070 | 10.254 | 10324.140 | 10324.140 | 10324.140 |
| capstone:prepare:find_first_in_sorted | 1/1 | 0 | 0 | 10.043 | 0.031 | 10.012 | 10043.057 | 10043.057 | 10043.057 |
| capstone:prepare:mergesort | 1/1 | 0 | 0 | 8.097 | 0.041 | 8.056 | 8097.249 | 8097.249 | 8097.249 |
| sandbox:read_file | 51/51 | 0 | 0 | 7.918 | 0.074 | 7.837 | 155.249 | 89.670 | 331.279 |
| tool:edit | 13/13 | 0 | 0 | 5.482 | 0.051 | 5.430 | 421.714 | 416.399 | 459.453 |
| capstone:verify:levenshtein | 1/1 | 0 | 0 | 3.403 | 0.001 | 3.401 | 3402.625 | 3402.625 | 3402.625 |
| capstone:scheduler:tick | 665/665 | 0 | 0 | 2.936 | 0.710 | 2.225 | 4.414 | 0.188 | 0.426 |
| agent:create | 12/12 | 0 | 0 | 2.770 | 0.563 | 2.207 | 230.821 | 140.347 | 496.182 |
| capstone:prepare:levenshtein | 1/1 | 0 | 0 | 2.509 | 0.031 | 2.478 | 2509.338 | 2509.338 | 2509.338 |
| sandbox:destroy | 12/12 | 0 | 0 | 1.467 | 0.020 | 1.446 | 122.225 | 119.049 | 137.634 |
| tool:glob | 4/4 | 0 | 0 | 1.336 | 0.012 | 1.323 | 334.123 | 335.505 | 337.422 |
| sandbox:write_file | 13/13 | 0 | 0 | 1.189 | 0.013 | 1.176 | 91.454 | 89.285 | 98.630 |
| tool:grep | 2/2 | 0 | 0 | 0.660 | 0.006 | 0.654 | 330.086 | 330.086 | 334.789 |
| capstone:verify:bitcount | 1/1 | 0 | 0 | 0.656 | 0.001 | 0.655 | 655.836 | 655.836 | 655.836 |
| capstone:prepare:hanoi | 1/1 | 0 | 0 | 0.455 | 0.034 | 0.422 | 455.130 | 455.130 | 455.130 |
| capstone:prepare:bucketsort | 1/1 | 0 | 0 | 0.452 | 0.032 | 0.420 | 452.268 | 452.268 | 452.268 |
| capstone:prepare:gcd | 1/1 | 0 | 0 | 0.452 | 0.031 | 0.420 | 451.719 | 451.719 | 451.719 |
| capstone:prepare:rpn_eval | 1/1 | 0 | 0 | 0.448 | 0.031 | 0.418 | 448.335 | 448.335 | 448.335 |
| capstone:prepare:powerset | 1/1 | 0 | 0 | 0.447 | 0.031 | 0.416 | 446.667 | 446.667 | 446.667 |
| capstone:prepare:next_palindrome | 1/1 | 0 | 0 | 0.443 | 0.031 | 0.412 | 443.030 | 443.030 | 443.030 |
| capstone:prepare:flatten | 1/1 | 0 | 0 | 0.431 | 0.031 | 0.400 | 430.666 | 430.666 | 430.666 |
| capstone:prepare:is_valid_parenthesization | 1/1 | 0 | 0 | 0.425 | 0.031 | 0.393 | 424.622 | 424.622 | 424.622 |
| capstone:verify:mergesort | 1/1 | 0 | 0 | 0.419 | 0.001 | 0.417 | 418.613 | 418.613 | 418.613 |
| capstone:verify:bucketsort | 1/1 | 0 | 0 | 0.407 | 0.001 | 0.406 | 407.149 | 407.149 | 407.149 |
| capstone:verify:rpn_eval | 1/1 | 0 | 0 | 0.394 | 0.001 | 0.393 | 394.314 | 394.314 | 394.314 |
| capstone:verify:find_first_in_sorted | 1/1 | 0 | 0 | 0.386 | 0.001 | 0.385 | 386.470 | 386.470 | 386.470 |
| capstone:verify:powerset | 1/1 | 0 | 0 | 0.386 | 0.001 | 0.385 | 385.741 | 385.741 | 385.741 |
| capstone:verify:flatten | 1/1 | 0 | 0 | 0.385 | 0.001 | 0.384 | 385.054 | 385.054 | 385.054 |
| capstone:verify:next_palindrome | 1/1 | 0 | 0 | 0.380 | 0.001 | 0.379 | 380.190 | 380.190 | 380.190 |
| capstone:verify:is_valid_parenthesization | 1/1 | 0 | 0 | 0.378 | 0.001 | 0.377 | 378.217 | 378.217 | 378.217 |
| capstone:verify:hanoi | 1/1 | 0 | 0 | 0.372 | 0.001 | 0.371 | 372.309 | 372.309 | 372.309 |
| capstone:verify:gcd | 1/1 | 0 | 0 | 0.369 | 0.001 | 0.368 | 369.484 | 369.484 | 369.484 |
| sync:container | 905/905 | 0 | 0 | 0.118 | 0.112 | 0.003 | 0.131 | 0.129 | 0.198 |
| sandbox:provision | 12/12 | 0 | 0 | 0.093 | 0.014 | 0.079 | 7.741 | 0.434 | 40.619 |
| sandbox:create | 12/12 | 0 | 0 | 0.091 | 0.013 | 0.079 | 7.606 | 0.308 | 40.455 |
| run:detect | 1/1 | 0 | 0 | 0.034 | 0.001 | 0.033 | 34.192 | 34.192 | 34.192 |
| agsync:join | 12/12 | 0 | 0 | 0.007 | 0.007 | 0.000 | 0.576 | 0.231 | 2.117 |
| prune | 24/24 | 0 | 0 | 0.007 | 0.004 | 0.002 | 0.272 | 0.267 | 0.360 |
| tool:return_summary | 15/15 | 3 | 0 | 0.005 | 0.005 | 0.000 | 0.357 | 0.349 | 0.407 |
| tool:return_plan | 12/12 | 0 | 0 | 0.004 | 0.004 | 0.000 | 0.336 | 0.336 | 0.380 |
| tool:return_status | 12/12 | 0 | 0 | 0.004 | 0.004 | 0.000 | 0.333 | 0.284 | 0.533 |
| llm:sync | 85/85 | 0 | 0 | 0.003 | 0.003 | 0.000 | 0.040 | 0.037 | 0.063 |
| input:prepare | 24/24 | 0 | 0 | 0.003 | 0.003 | 0.000 | 0.105 | 0.094 | 0.175 |
| proc_wait | 24/24 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.078 | 0.068 | 0.098 |
| resolve | 24/24 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.068 | 0.059 | 0.117 |
| agprof:clock_sync | 1/1 | 0 | 0 | 0.001 | 0.001 | 0.000 | 1.021 | 1.021 | 1.021 |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 6578 | 22.622 | 0.000 | 158.758 | 20.891 | 151.029108 CPU seconds | n/a |
| python3 (PID 55012) CPU | percent | 6981 | 3.648 | 0.000 | 134.078 | 9.833 | 26.120000 CPU seconds | n/a |
| python3 (PID 55012) io read MB/s | MB/s | 6981 | 0.035 | 0.000 | 55.871 | 0.000 | 25.164062 MB | n/a |
| python3 (PID 55012) io write MB/s | MB/s | 6981 | 0.049 | 0.000 | 22.451 | 0.000 | 34.722656 MB | n/a |
| python3 (PID 55012) rss_mb | MB | 6982 | 688.491 | 612.414 | 704.691 | 704.691 | n/a | n/a |
| python3 (PID 55012) vms_mb | MB | 6982 | 3740.764 | 3406.684 | 3767.047 | 3767.016 | n/a | n/a |
| git (PID 55018) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| git (PID 55018) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 55018) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 55018) rss_mb | MB | 5 | 4.812 | 4.812 | 4.812 | 4.812 | n/a | n/a |
| git (PID 55018) vms_mb | MB | 5 | 12.516 | 12.516 | 12.516 | 12.516 | n/a | n/a |
| git (PID 55019) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| git (PID 55019) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 55019) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git (PID 55019) rss_mb | MB | 5 | 3.359 | 3.359 | 3.359 | 3.359 | n/a | n/a |
| git (PID 55019) vms_mb | MB | 5 | 11.273 | 11.273 | 11.273 | 11.273 | n/a | n/a |
| git-remote-http (PID 55020) CPU | percent | 4 | 4.940 | 0.000 | 19.759 | 0.000 | 0.020000 CPU seconds | n/a |
| git-remote-http (PID 55020) io read MB/s | MB/s | 4 | 0.656 | 0.000 | 2.624 | 0.000 | 0.265625 MB | n/a |
| git-remote-http (PID 55020) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| git-remote-http (PID 55020) rss_mb | MB | 5 | 19.163 | 19.051 | 19.191 | 19.191 | n/a | n/a |
| git-remote-http (PID 55020) vms_mb | MB | 5 | 106.966 | 106.566 | 107.566 | 107.566 | n/a | n/a |
| python3 (PID 55026) CPU | percent | 98 | 99.965 | 89.095 | 109.043 | 99.074 | 9.890000 CPU seconds | n/a |
| python3 (PID 55026) io read MB/s | MB/s | 98 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 55026) io write MB/s | MB/s | 98 | 0.002 | 0.000 | 0.116 | 0.000 | 0.015625 MB | n/a |
| python3 (PID 55026) rss_mb | MB | 99 | 33.887 | 17.422 | 34.133 | 34.133 | n/a | n/a |
| python3 (PID 55026) vms_mb | MB | 99 | 56.178 | 42.301 | 56.375 | 56.375 | n/a | n/a |
| python3 (PID 55027) CPU | percent | 3 | 102.325 | 99.017 | 108.876 | 99.081 | 0.310000 CPU seconds | n/a |
| python3 (PID 55027) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 55027) io write MB/s | MB/s | 3 | 0.052 | 0.000 | 0.155 | 0.155 | 0.015625 MB | n/a |
| python3 (PID 55027) rss_mb | MB | 4 | 24.344 | 10.133 | 34.281 | 34.281 | n/a | n/a |
| python3 (PID 55027) vms_mb | MB | 4 | 48.595 | 36.465 | 57.504 | 57.504 | n/a | n/a |
| python3 (PID 55028) CPU | percent | 3 | 99.007 | 89.050 | 108.909 | 99.061 | 0.300000 CPU seconds | n/a |
| python3 (PID 55028) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 55028) io write MB/s | MB/s | 3 | 0.722 | 0.000 | 2.012 | 2.012 | 0.218750 MB | n/a |
| python3 (PID 55028) rss_mb | MB | 4 | 29.860 | 20.531 | 36.566 | 36.566 | n/a | n/a |
| python3 (PID 55028) vms_mb | MB | 4 | 53.073 | 45.238 | 58.516 | 58.516 | n/a | n/a |
| python3 (PID 55029) CPU | percent | 3 | 99.004 | 98.968 | 99.072 | 99.072 | 0.300000 CPU seconds | n/a |
| python3 (PID 55029) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 55029) io write MB/s | MB/s | 3 | 0.735 | 0.000 | 2.206 | 2.206 | 0.222656 MB | n/a |
| python3 (PID 55029) rss_mb | MB | 4 | 26.514 | 14.125 | 34.715 | 34.715 | n/a | n/a |
| python3 (PID 55029) vms_mb | MB | 4 | 50.386 | 39.566 | 57.508 | 57.508 | n/a | n/a |
| python3 (PID 55030) CPU | percent | 24 | 99.886 | 98.952 | 108.957 | 99.073 | 2.420000 CPU seconds | n/a |
| python3 (PID 55030) io read MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 55030) io write MB/s | MB/s | 24 | 0.092 | 0.000 | 2.051 | 2.051 | 0.222656 MB | n/a |
| python3 (PID 55030) rss_mb | MB | 25 | 32.635 | 10.836 | 34.762 | 34.762 | n/a | n/a |
| python3 (PID 55030) vms_mb | MB | 25 | 56.138 | 36.777 | 57.512 | 57.512 | n/a | n/a |
| python3 (PID 55031) CPU | percent | 79 | 99.948 | 89.025 | 108.983 | 98.949 | 8.000000 CPU seconds | n/a |
| python3 (PID 55031) io read MB/s | MB/s | 79 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 55031) io write MB/s | MB/s | 79 | 0.028 | 0.000 | 2.090 | 0.000 | 0.226562 MB | n/a |
| python3 (PID 55031) rss_mb | MB | 80 | 41.489 | 13.172 | 47.855 | 47.855 | n/a | n/a |
| python3 (PID 55031) vms_mb | MB | 80 | 64.046 | 38.422 | 69.637 | 69.637 | n/a | n/a |
| python3 (PID 55032) CPU | percent | 3 | 102.322 | 98.941 | 108.979 | 108.979 | 0.310000 CPU seconds | n/a |
| python3 (PID 55032) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 55032) io write MB/s | MB/s | 3 | 0.748 | 0.000 | 2.245 | 2.245 | 0.226562 MB | n/a |
| python3 (PID 55032) rss_mb | MB | 4 | 26.462 | 14.285 | 34.734 | 34.734 | n/a | n/a |
| python3 (PID 55032) vms_mb | MB | 4 | 50.420 | 39.703 | 57.508 | 57.508 | n/a | n/a |
| python3 (PID 55033) CPU | percent | 98 | 99.873 | 98.960 | 109.053 | 99.006 | 9.880000 CPU seconds | n/a |
| python3 (PID 55033) io read MB/s | MB/s | 98 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 55033) io write MB/s | MB/s | 98 | 0.002 | 0.000 | 0.155 | 0.000 | 0.015625 MB | n/a |
| python3 (PID 55033) rss_mb | MB | 99 | 34.175 | 21.699 | 34.363 | 34.363 | n/a | n/a |
| python3 (PID 55033) vms_mb | MB | 99 | 56.352 | 45.531 | 56.508 | 56.508 | n/a | n/a |
| python3 (PID 55034) CPU | percent | 3 | 102.223 | 98.669 | 108.978 | 108.978 | 0.310000 CPU seconds | n/a |
| python3 (PID 55034) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 55034) io write MB/s | MB/s | 3 | 0.761 | 0.000 | 2.283 | 2.283 | 0.230469 MB | n/a |
| python3 (PID 55034) rss_mb | MB | 4 | 26.435 | 14.316 | 34.590 | 34.590 | n/a | n/a |
| python3 (PID 55034) vms_mb | MB | 4 | 50.416 | 39.703 | 57.492 | 57.492 | n/a | n/a |
| python3 (PID 55035) CPU | percent | 3 | 98.998 | 89.196 | 108.872 | 108.872 | 0.300000 CPU seconds | n/a |
| python3 (PID 55035) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 55035) io write MB/s | MB/s | 3 | 0.760 | 0.000 | 2.126 | 2.126 | 0.230469 MB | n/a |
| python3 (PID 55035) rss_mb | MB | 4 | 29.669 | 21.074 | 34.953 | 34.953 | n/a | n/a |
| python3 (PID 55035) vms_mb | MB | 4 | 53.134 | 45.371 | 57.504 | 57.496 | n/a | n/a |
| python3 (PID 55036) CPU | percent | 3 | 102.317 | 89.128 | 108.952 | 108.952 | 0.310000 CPU seconds | n/a |
| python3 (PID 55036) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 55036) io write MB/s | MB/s | 3 | 0.761 | 0.000 | 2.283 | 2.283 | 0.230469 MB | n/a |
| python3 (PID 55036) rss_mb | MB | 4 | 27.646 | 17.000 | 34.793 | 34.793 | n/a | n/a |
| python3 (PID 55036) vms_mb | MB | 4 | 51.431 | 41.164 | 57.508 | 57.508 | n/a | n/a |
| python3 (PID 55037) CPU | percent | 3 | 102.308 | 99.018 | 108.865 | 99.040 | 0.310000 CPU seconds | n/a |
| python3 (PID 55037) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 55037) io write MB/s | MB/s | 3 | 0.052 | 0.000 | 0.155 | 0.155 | 0.015625 MB | n/a |
| python3 (PID 55037) rss_mb | MB | 4 | 24.476 | 10.508 | 34.301 | 34.301 | n/a | n/a |
| python3 (PID 55037) vms_mb | MB | 4 | 48.637 | 36.633 | 57.504 | 57.504 | n/a | n/a |
| docker (PID 55092) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 55092) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 55092) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 55092) rss_mb | MB | 3 | 27.115 | 26.855 | 27.633 | 27.633 | n/a | n/a |
| docker (PID 55092) vms_mb | MB | 3 | 1708.776 | 1660.773 | 1804.781 | 1804.781 | n/a | n/a |
| docker-init [alex_0000] (PID 55133) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [alex_0000] (PID 55133) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [alex_0000] (PID 55133) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 55145) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 55145) rss_mb | MB | 4 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [alex_0000] (PID 55145) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 55147) rss_mb | MB | 1 | 23.523 | 23.523 | 23.523 | 23.523 | n/a | n/a |
| docker (PID 55147) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 55182) rss_mb | MB | 1 | 27.332 | 27.332 | 27.332 | 27.332 | n/a | n/a |
| docker (PID 55182) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 55273) rss_mb | MB | 1 | 23.250 | 23.250 | 23.250 | 23.250 | n/a | n/a |
| docker (PID 55273) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 55282) rss_mb | MB | 1 | 26.262 | 26.262 | 26.262 | 26.262 | n/a | n/a |
| docker (PID 55282) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 55340) CPU | percent | 1 | 9.813 | 9.813 | 9.813 | 9.813 | 0.010000 CPU seconds | n/a |
| docker (PID 55340) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 55340) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 55340) rss_mb | MB | 2 | 20.086 | 14.555 | 25.617 | 25.617 | n/a | n/a |
| docker (PID 55340) vms_mb | MB | 2 | 1552.078 | 1515.949 | 1588.207 | 1588.207 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 55378) CPU | percent | 3 | 6.553 | 0.000 | 19.658 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 55378) rss_mb | MB | 4 | 3.603 | 0.633 | 12.512 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 55378) vms_mb | MB | 4 | 411.474 | 1.055 | 1642.730 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 55392) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 55392) rss_mb | MB | 3 | 1.840 | 1.840 | 1.840 | 1.840 | n/a | n/a |
| tail [alex_0000] (PID 55392) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 55405) rss_mb | MB | 1 | 27.281 | 27.281 | 27.281 | 27.281 | n/a | n/a |
| docker (PID 55405) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 55425) rss_mb | MB | 1 | 4.523 | 4.523 | 4.523 | 4.523 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 55425) vms_mb | MB | 1 | 1505.445 | 1505.445 | 1505.445 | 1505.445 | n/a | n/a |
| docker (PID 55432) rss_mb | MB | 1 | 27.191 | 27.191 | 27.191 | 27.191 | n/a | n/a |
| docker (PID 55432) vms_mb | MB | 1 | 1733.027 | 1733.027 | 1733.027 | 1733.027 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 55452) rss_mb | MB | 1 | 12.027 | 12.027 | 12.027 | 12.027 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 55452) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 55467) rss_mb | MB | 1 | 27.105 | 27.105 | 27.105 | 27.105 | n/a | n/a |
| docker (PID 55467) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 55486) rss_mb | MB | 1 | 11.730 | 11.730 | 11.730 | 11.730 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 55486) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 55503) rss_mb | MB | 1 | 26.879 | 26.879 | 26.879 | 26.879 | n/a | n/a |
| docker (PID 55503) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 55564) rss_mb | MB | 1 | 26.508 | 26.508 | 26.508 | 26.508 | n/a | n/a |
| docker (PID 55564) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker-init [alex_0000] (PID 55603) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [alex_0000] (PID 55603) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [alex_0000] (PID 55603) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 55616) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 55616) rss_mb | MB | 3 | 1.707 | 1.707 | 1.707 | 1.707 | n/a | n/a |
| tail [alex_0000] (PID 55616) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 55618) rss_mb | MB | 1 | 10.340 | 10.340 | 10.340 | 10.340 | n/a | n/a |
| docker (PID 55618) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 55652) rss_mb | MB | 1 | 27.422 | 27.422 | 27.422 | 27.422 | n/a | n/a |
| docker (PID 55652) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 55693) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 55693) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 55693) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 55693) rss_mb | MB | 2 | 25.672 | 25.672 | 25.672 | 25.672 | n/a | n/a |
| docker (PID 55693) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 55754) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 55754) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 55754) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 55754) rss_mb | MB | 2 | 26.691 | 26.691 | 26.691 | 26.691 | n/a | n/a |
| docker (PID 55754) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 55792) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 55792) rss_mb | MB | 3 | 4.728 | 0.633 | 12.918 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 55792) vms_mb | MB | 3 | 524.195 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 55806) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 55806) rss_mb | MB | 2 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [alex_0000] (PID 55806) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 55886) CPU | percent | 1 | 9.810 | 9.810 | 9.810 | 9.810 | 0.010000 CPU seconds | n/a |
| docker (PID 55886) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 55886) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 55886) rss_mb | MB | 2 | 17.889 | 8.992 | 26.785 | 26.785 | n/a | n/a |
| docker (PID 55886) vms_mb | MB | 2 | 1480.105 | 1227.434 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 55946) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 55946) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 55946) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 55946) rss_mb | MB | 2 | 26.984 | 26.984 | 26.984 | 26.984 | n/a | n/a |
| docker (PID 55946) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [alex_0000] (PID 55986) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [alex_0000] (PID 55986) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [alex_0000] (PID 55986) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 55998) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 55998) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [alex_0000] (PID 55998) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 56036) rss_mb | MB | 1 | 22.383 | 22.383 | 22.383 | 22.383 | n/a | n/a |
| docker (PID 56036) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 56071) rss_mb | MB | 1 | 27.250 | 27.250 | 27.250 | 27.250 | n/a | n/a |
| docker (PID 56071) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 56090) rss_mb | MB | 1 | 4.371 | 4.371 | 4.371 | 4.371 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 56090) vms_mb | MB | 1 | 1288.934 | 1288.934 | 1288.934 | 1288.934 | n/a | n/a |
| docker (PID 56106) rss_mb | MB | 1 | 27.188 | 27.188 | 27.188 | 27.188 | n/a | n/a |
| docker (PID 56106) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 56146) rss_mb | MB | 1 | 25.707 | 25.707 | 25.707 | 25.707 | n/a | n/a |
| docker (PID 56146) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 56185) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 56185) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 56185) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 56185) rss_mb | MB | 38 | 26.863 | 26.863 | 26.863 | 26.863 | n/a | n/a |
| docker (PID 56185) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 56201) rss_mb | MB | 1 | 25.625 | 25.625 | 25.625 | 25.625 | n/a | n/a |
| docker (PID 56201) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 56227) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 56227) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 56227) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 56227) rss_mb | MB | 2 | 26.910 | 26.910 | 26.910 | 26.910 | n/a | n/a |
| docker (PID 56227) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 56267) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 56267) rss_mb | MB | 4 | 3.645 | 0.633 | 12.680 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 56267) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 56280) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 56280) rss_mb | MB | 3 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [alex_0000] (PID 56280) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 56356) rss_mb | MB | 1 | 25.297 | 25.297 | 25.297 | 25.297 | n/a | n/a |
| docker (PID 56356) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 56396) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 56396) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 56396) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 56396) rss_mb | MB | 2 | 26.910 | 26.910 | 26.910 | 26.910 | n/a | n/a |
| docker (PID 56396) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 56449) rss_mb | MB | 1 | 17.238 | 17.238 | 17.238 | 17.238 | n/a | n/a |
| docker (PID 56449) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 56457) rss_mb | MB | 1 | 26.797 | 26.797 | 26.797 | 26.797 | n/a | n/a |
| docker (PID 56457) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 56496) CPU | percent | 10 | 1.967 | 0.000 | 19.673 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 56496) rss_mb | MB | 11 | 1.549 | 0.633 | 10.715 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 56496) vms_mb | MB | 11 | 137.067 | 1.055 | 1497.191 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 56508) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 56508) rss_mb | MB | 10 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [alex_0000] (PID 56508) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 56518) rss_mb | MB | 1 | 23.844 | 23.844 | 23.844 | 23.844 | n/a | n/a |
| docker (PID 56518) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 56546) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 56546) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 56546) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 56546) rss_mb | MB | 9 | 27.309 | 27.309 | 27.309 | 27.309 | n/a | n/a |
| docker (PID 56546) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 56566) CPU | percent | 8 | 3.672 | 0.000 | 29.373 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 56566) rss_mb | MB | 9 | 4.263 | 3.410 | 11.082 | 3.410 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 56566) vms_mb | MB | 9 | 186.329 | 4.391 | 1641.836 | 4.391 | n/a | n/a |
| python [alex_0000] (PID 56576) CPU | percent | 7 | 99.402 | 88.146 | 107.876 | 107.832 | 0.710000 CPU seconds | n/a |
| python [alex_0000] (PID 56576) rss_mb | MB | 8 | 33.282 | 18.000 | 42.535 | 42.535 | n/a | n/a |
| python [alex_0000] (PID 56576) vms_mb | MB | 8 | 40.540 | 23.254 | 52.238 | 52.238 | n/a | n/a |
| docker (PID 56586) rss_mb | MB | 1 | 27.004 | 27.004 | 27.004 | 27.004 | n/a | n/a |
| docker (PID 56586) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 56630) rss_mb | MB | 1 | 18.039 | 18.039 | 18.039 | 18.039 | n/a | n/a |
| docker (PID 56630) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 56648) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 56648) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 56648) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 56648) rss_mb | MB | 2 | 26.883 | 26.883 | 26.883 | 26.883 | n/a | n/a |
| docker (PID 56648) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 56689) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [alex_0000] (PID 56689) rss_mb | MB | 4 | 3.641 | 0.633 | 12.664 | 0.633 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 56689) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [alex_0000] (PID 56701) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [alex_0000] (PID 56701) rss_mb | MB | 3 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [alex_0000] (PID 56701) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 56712) rss_mb | MB | 1 | 26.844 | 26.844 | 26.844 | 26.844 | n/a | n/a |
| docker (PID 56712) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 56732) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[2:INIT] [alex_0000] (PID 56732) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| docker (PID 56774) rss_mb | MB | 1 | 22.164 | 22.164 | 22.164 | 22.164 | n/a | n/a |
| docker (PID 56774) vms_mb | MB | 1 | 1523.953 | 1523.953 | 1523.953 | 1523.953 | n/a | n/a |
| docker (PID 56811) rss_mb | MB | 1 | 26.035 | 26.035 | 26.035 | 26.035 | n/a | n/a |
| docker (PID 56811) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 56852) rss_mb | MB | 1 | 1.508 | 1.508 | 1.508 | 1.508 | n/a | n/a |
| docker (PID 56852) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 56862) rss_mb | MB | 1 | 9.402 | 9.402 | 9.402 | 9.402 | n/a | n/a |
| docker (PID 56862) vms_mb | MB | 1 | 1315.695 | 1315.695 | 1315.695 | 1315.695 | n/a | n/a |
| docker (PID 56886) rss_mb | MB | 1 | 25.898 | 25.898 | 25.898 | 25.898 | n/a | n/a |
| docker (PID 56886) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 56894) CPU | percent | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 56894) io read MB/s | MB/s | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 56894) io write MB/s | MB/s | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 56894) rss_mb | MB | 46 | 26.652 | 26.652 | 26.652 | 26.652 | n/a | n/a |
| docker (PID 56894) vms_mb | MB | 46 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 56926) rss_mb | MB | 1 | 27.035 | 27.035 | 27.035 | 27.035 | n/a | n/a |
| docker (PID 56926) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 56942) CPU | percent | 6 | 67.580 | 49.473 | 88.972 | 88.972 | 0.410000 CPU seconds | n/a |
| python3 (PID 56942) io read MB/s | MB/s | 6 | 8.314 | 0.000 | 16.117 | 0.000 | 5.042969 MB | n/a |
| python3 (PID 56942) io write MB/s | MB/s | 6 | 0.322 | 0.000 | 1.931 | 1.931 | 0.195312 MB | n/a |
| python3 (PID 56942) rss_mb | MB | 7 | 25.224 | 11.523 | 34.645 | 34.645 | n/a | n/a |
| python3 (PID 56942) vms_mb | MB | 7 | 49.179 | 36.938 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 56971) rss_mb | MB | 1 | 3.227 | 3.227 | 3.227 | 3.227 | n/a | n/a |
| docker (PID 56971) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 56993) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 56993) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 56993) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 56993) rss_mb | MB | 2 | 27.250 | 27.078 | 27.422 | 27.422 | n/a | n/a |
| docker (PID 56993) vms_mb | MB | 2 | 1732.777 | 1660.773 | 1804.781 | 1804.781 | n/a | n/a |
| docker-init [andy_0000] (PID 57035) CPU | percent | 4 | 4.912 | 0.000 | 19.647 | 0.000 | 0.020000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 57035) rss_mb | MB | 5 | 2.978 | 0.633 | 12.359 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 57035) vms_mb | MB | 5 | 314.889 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 57048) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 57048) rss_mb | MB | 4 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [andy_0000] (PID 57048) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 57050) rss_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| docker (PID 57050) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] (PID 57069) rss_mb | MB | 1 | 11.613 | 11.613 | 11.613 | 11.613 | n/a | n/a |
| runc:[2:INIT] (PID 57069) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 57144) rss_mb | MB | 1 | 20.168 | 20.168 | 20.168 | 20.168 | n/a | n/a |
| docker (PID 57144) vms_mb | MB | 1 | 1524.203 | 1524.203 | 1524.203 | 1524.203 | n/a | n/a |
| docker (PID 57182) rss_mb | MB | 1 | 25.707 | 25.707 | 25.707 | 25.707 | n/a | n/a |
| docker (PID 57182) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 57224) rss_mb | MB | 1 | 4.160 | 4.160 | 4.160 | 4.160 | n/a | n/a |
| docker (PID 57224) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 57241) rss_mb | MB | 1 | 25.234 | 25.234 | 25.234 | 25.234 | n/a | n/a |
| docker (PID 57241) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [andy_0000] (PID 57282) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 57282) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 57282) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 57294) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 57294) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [andy_0000] (PID 57294) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 57296) rss_mb | MB | 1 | 27.012 | 27.012 | 27.012 | 27.012 | n/a | n/a |
| docker (PID 57296) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 57331) rss_mb | MB | 1 | 27.438 | 27.438 | 27.438 | 27.438 | n/a | n/a |
| docker (PID 57331) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[0:PARENT] [andy_0000] (PID 57347) rss_mb | MB | 1 | 1.953 | 1.953 | 1.953 | 1.953 | n/a | n/a |
| runc:[0:PARENT] [andy_0000] (PID 57347) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[1:CHILD] [andy_0000] (PID 57350) rss_mb | MB | 1 | 0.840 | 0.840 | 0.840 | 0.840 | n/a | n/a |
| runc:[1:CHILD] [andy_0000] (PID 57350) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| docker (PID 57367) rss_mb | MB | 1 | 27.398 | 27.398 | 27.398 | 27.398 | n/a | n/a |
| docker (PID 57367) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 57387) rss_mb | MB | 1 | 11.590 | 11.590 | 11.590 | 11.590 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 57387) vms_mb | MB | 1 | 1642.352 | 1642.352 | 1642.352 | 1642.352 | n/a | n/a |
| docker (PID 57405) rss_mb | MB | 1 | 25.707 | 25.707 | 25.707 | 25.707 | n/a | n/a |
| docker (PID 57405) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 57490) CPU | percent | 37 | 0.267 | 0.000 | 9.867 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 57490) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 57490) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 57490) rss_mb | MB | 38 | 25.879 | 9.117 | 26.332 | 26.332 | n/a | n/a |
| docker (PID 57490) vms_mb | MB | 38 | 1649.580 | 1235.438 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 57506) rss_mb | MB | 1 | 25.465 | 25.465 | 25.465 | 25.465 | n/a | n/a |
| docker (PID 57506) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 57532) rss_mb | MB | 1 | 27.164 | 27.164 | 27.164 | 27.164 | n/a | n/a |
| docker (PID 57532) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [andy_0000] (PID 57571) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 57571) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 57571) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 57586) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 57586) rss_mb | MB | 3 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [andy_0000] (PID 57586) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 57588) rss_mb | MB | 1 | 17.285 | 17.285 | 17.285 | 17.285 | n/a | n/a |
| docker (PID 57588) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 57626) rss_mb | MB | 1 | 27.168 | 27.168 | 27.168 | 27.168 | n/a | n/a |
| docker (PID 57626) vms_mb | MB | 1 | 1733.027 | 1733.027 | 1733.027 | 1733.027 | n/a | n/a |
| docker (PID 57663) rss_mb | MB | 1 | 27.289 | 27.289 | 27.289 | 27.289 | n/a | n/a |
| docker (PID 57663) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 57683) rss_mb | MB | 1 | 11.605 | 11.605 | 11.605 | 11.605 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 57683) vms_mb | MB | 1 | 1642.352 | 1642.352 | 1642.352 | 1642.352 | n/a | n/a |
| docker (PID 57702) rss_mb | MB | 1 | 26.977 | 26.977 | 26.977 | 26.977 | n/a | n/a |
| docker (PID 57702) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 57759) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 57759) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 57759) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 57759) rss_mb | MB | 2 | 25.887 | 25.887 | 25.887 | 25.887 | n/a | n/a |
| docker (PID 57759) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [andy_0000] (PID 57799) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [andy_0000] (PID 57799) rss_mb | MB | 11 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [andy_0000] (PID 57799) vms_mb | MB | 11 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 57812) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 57812) rss_mb | MB | 11 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [andy_0000] (PID 57812) vms_mb | MB | 11 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 57850) CPU | percent | 8 | 1.222 | 0.000 | 9.772 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 57850) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 57850) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 57850) rss_mb | MB | 9 | 24.719 | 6.344 | 27.016 | 27.016 | n/a | n/a |
| docker (PID 57850) vms_mb | MB | 9 | 1479.883 | 32.762 | 1660.773 | 1660.773 | n/a | n/a |
| bash [andy_0000] (PID 57869) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [andy_0000] (PID 57869) rss_mb | MB | 8 | 3.418 | 3.418 | 3.418 | 3.418 | n/a | n/a |
| bash [andy_0000] (PID 57869) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [andy_0000] (PID 57878) CPU | percent | 7 | 99.433 | 88.224 | 107.889 | 107.870 | 0.710000 CPU seconds | n/a |
| python [andy_0000] (PID 57878) rss_mb | MB | 8 | 31.862 | 12.586 | 42.754 | 42.754 | n/a | n/a |
| python [andy_0000] (PID 57878) vms_mb | MB | 8 | 38.816 | 16.277 | 52.238 | 52.238 | n/a | n/a |
| docker (PID 57888) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 57888) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 57888) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 57888) rss_mb | MB | 2 | 27.012 | 27.012 | 27.012 | 27.012 | n/a | n/a |
| docker (PID 57888) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 57948) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 57948) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 57948) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 57948) rss_mb | MB | 2 | 25.770 | 25.770 | 25.770 | 25.770 | n/a | n/a |
| docker (PID 57948) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 57988) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [andy_0000] (PID 57988) rss_mb | MB | 4 | 3.733 | 0.633 | 13.035 | 0.633 | n/a | n/a |
| runc:[2:INIT] [andy_0000] (PID 57988) vms_mb | MB | 4 | 411.411 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [andy_0000] (PID 58001) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [andy_0000] (PID 58001) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [andy_0000] (PID 58001) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 58074) rss_mb | MB | 1 | 25.801 | 25.801 | 25.801 | 25.801 | n/a | n/a |
| docker (PID 58074) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 58111) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 58111) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 58111) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 58111) rss_mb | MB | 2 | 27.062 | 27.062 | 27.062 | 27.062 | n/a | n/a |
| docker (PID 58111) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 58190) rss_mb | MB | 1 | 26.363 | 26.363 | 26.363 | 26.363 | n/a | n/a |
| docker (PID 58190) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 58198) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 58198) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 58198) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 58198) rss_mb | MB | 39 | 26.754 | 26.754 | 26.754 | 26.754 | n/a | n/a |
| docker (PID 58198) vms_mb | MB | 39 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 58232) rss_mb | MB | 1 | 26.848 | 26.848 | 26.848 | 26.848 | n/a | n/a |
| docker (PID 58232) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 58249) CPU | percent | 3 | 102.076 | 98.846 | 108.507 | 98.876 | 0.310000 CPU seconds | n/a |
| python3 (PID 58249) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 58249) io write MB/s | MB/s | 3 | 0.708 | 0.000 | 2.124 | 2.124 | 0.214844 MB | n/a |
| python3 (PID 58249) rss_mb | MB | 4 | 26.159 | 13.168 | 34.504 | 34.504 | n/a | n/a |
| python3 (PID 58249) vms_mb | MB | 4 | 50.094 | 38.430 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 58280) rss_mb | MB | 1 | 1.828 | 1.828 | 1.828 | 1.828 | n/a | n/a |
| docker (PID 58280) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 58302) CPU | percent | 1 | 9.899 | 9.899 | 9.899 | 9.899 | 0.010000 CPU seconds | n/a |
| docker (PID 58302) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 58302) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 58302) rss_mb | MB | 2 | 27.035 | 26.629 | 27.441 | 27.441 | n/a | n/a |
| docker (PID 58302) vms_mb | MB | 2 | 1732.777 | 1660.773 | 1804.781 | 1804.781 | n/a | n/a |
| docker-init [arch_0000] (PID 58342) CPU | percent | 4 | 4.918 | 0.000 | 19.672 | 0.000 | 0.020000 CPU seconds | n/a |
| docker-init [arch_0000] (PID 58342) rss_mb | MB | 5 | 2.696 | 0.633 | 10.949 | 0.633 | n/a | n/a |
| docker-init [arch_0000] (PID 58342) vms_mb | MB | 5 | 314.683 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 58356) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 58356) rss_mb | MB | 4 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [arch_0000] (PID 58356) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 58358) rss_mb | MB | 1 | 27.383 | 27.383 | 27.383 | 27.383 | n/a | n/a |
| docker (PID 58358) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] (PID 58378) rss_mb | MB | 1 | 10.707 | 10.707 | 10.707 | 10.707 | n/a | n/a |
| runc:[2:INIT] (PID 58378) vms_mb | MB | 1 | 1641.449 | 1641.449 | 1641.449 | 1641.449 | n/a | n/a |
| docker (PID 58394) rss_mb | MB | 1 | 27.086 | 27.086 | 27.086 | 27.086 | n/a | n/a |
| docker (PID 58394) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 58413) rss_mb | MB | 1 | 11.938 | 11.938 | 11.938 | 11.938 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 58413) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 58455) rss_mb | MB | 1 | 0.129 | 0.129 | 0.129 | 0.129 | n/a | n/a |
| docker (PID 58455) vms_mb | MB | 1 | 30.570 | 30.570 | 30.570 | 30.570 | n/a | n/a |
| docker (PID 58491) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 58491) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 58491) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 58491) rss_mb | MB | 2 | 27.090 | 27.027 | 27.152 | 27.152 | n/a | n/a |
| docker (PID 58491) vms_mb | MB | 2 | 1660.648 | 1660.523 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 58552) rss_mb | MB | 1 | 26.977 | 26.977 | 26.977 | 26.977 | n/a | n/a |
| docker (PID 58552) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [arch_0000] (PID 58590) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [arch_0000] (PID 58590) rss_mb | MB | 3 | 0.566 | 0.566 | 0.566 | 0.566 | n/a | n/a |
| docker-init [arch_0000] (PID 58590) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 58603) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 58603) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [arch_0000] (PID 58603) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 58606) rss_mb | MB | 1 | 20.051 | 20.051 | 20.051 | 20.051 | n/a | n/a |
| docker (PID 58606) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 58642) rss_mb | MB | 1 | 27.043 | 27.043 | 27.043 | 27.043 | n/a | n/a |
| docker (PID 58642) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 58677) rss_mb | MB | 1 | 27.352 | 27.352 | 27.352 | 27.352 | n/a | n/a |
| docker (PID 58677) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 58696) rss_mb | MB | 1 | 10.344 | 10.344 | 10.344 | 10.344 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 58696) vms_mb | MB | 1 | 1641.449 | 1641.449 | 1641.449 | 1641.449 | n/a | n/a |
| docker (PID 58715) rss_mb | MB | 1 | 26.789 | 26.789 | 26.789 | 26.789 | n/a | n/a |
| docker (PID 58715) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 58755) rss_mb | MB | 1 | 14.605 | 14.605 | 14.605 | 14.605 | n/a | n/a |
| docker (PID 58755) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 58764) rss_mb | MB | 1 | 26.648 | 26.648 | 26.648 | 26.648 | n/a | n/a |
| docker (PID 58764) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 58796) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 58796) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 58796) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 58796) rss_mb | MB | 38 | 26.781 | 26.781 | 26.781 | 26.781 | n/a | n/a |
| docker (PID 58796) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 58812) rss_mb | MB | 1 | 27.008 | 27.008 | 27.008 | 27.008 | n/a | n/a |
| docker (PID 58812) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 58838) rss_mb | MB | 1 | 25.344 | 25.344 | 25.344 | 25.344 | n/a | n/a |
| docker (PID 58838) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [arch_0000] (PID 58877) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [arch_0000] (PID 58877) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [arch_0000] (PID 58877) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 58890) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 58890) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [arch_0000] (PID 58890) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 58892) rss_mb | MB | 1 | 23.727 | 23.727 | 23.727 | 23.727 | n/a | n/a |
| docker (PID 58892) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 58928) rss_mb | MB | 1 | 27.168 | 27.168 | 27.168 | 27.168 | n/a | n/a |
| docker (PID 58928) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[0:PARENT] [arch_0000] (PID 58944) rss_mb | MB | 1 | 1.953 | 1.953 | 1.953 | 1.953 | n/a | n/a |
| runc:[0:PARENT] [arch_0000] (PID 58944) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| docker (PID 58965) rss_mb | MB | 1 | 27.332 | 27.332 | 27.332 | 27.332 | n/a | n/a |
| docker (PID 58965) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 58985) rss_mb | MB | 1 | 11.324 | 11.324 | 11.324 | 11.324 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 58985) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 59004) rss_mb | MB | 1 | 26.012 | 26.012 | 26.012 | 26.012 | n/a | n/a |
| docker (PID 59004) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 59045) rss_mb | MB | 1 | 20.133 | 20.133 | 20.133 | 20.133 | n/a | n/a |
| docker (PID 59045) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 59054) rss_mb | MB | 1 | 26.496 | 26.496 | 26.496 | 26.496 | n/a | n/a |
| docker (PID 59054) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 59062) rss_mb | MB | 1 | 27.148 | 27.148 | 27.148 | 27.148 | n/a | n/a |
| docker (PID 59062) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 59102) CPU | percent | 11 | 1.787 | 0.000 | 19.658 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 59102) rss_mb | MB | 12 | 1.633 | 0.633 | 12.637 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 59102) vms_mb | MB | 12 | 131.861 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 59115) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 59115) rss_mb | MB | 11 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [arch_0000] (PID 59115) vms_mb | MB | 11 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 59125) rss_mb | MB | 1 | 27.223 | 27.223 | 27.223 | 27.223 | n/a | n/a |
| docker (PID 59125) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 59158) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 59158) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 59158) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 59158) rss_mb | MB | 9 | 27.031 | 27.031 | 27.031 | 27.031 | n/a | n/a |
| docker (PID 59158) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 59179) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 59179) rss_mb | MB | 9 | 4.424 | 3.418 | 12.473 | 3.418 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 59179) vms_mb | MB | 9 | 186.401 | 4.391 | 1642.480 | 4.391 | n/a | n/a |
| python [arch_0000] (PID 59189) CPU | percent | 7 | 99.290 | 88.238 | 107.747 | 107.747 | 0.710000 CPU seconds | n/a |
| python [arch_0000] (PID 59189) rss_mb | MB | 8 | 32.457 | 18.516 | 41.938 | 41.938 | n/a | n/a |
| python [arch_0000] (PID 59189) vms_mb | MB | 8 | 39.794 | 23.172 | 52.219 | 52.219 | n/a | n/a |
| docker (PID 59199) CPU | percent | 1 | 9.775 | 9.775 | 9.775 | 9.775 | 0.010000 CPU seconds | n/a |
| docker (PID 59199) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 59199) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 59199) rss_mb | MB | 2 | 14.150 | 1.230 | 27.070 | 27.070 | n/a | n/a |
| docker (PID 59199) vms_mb | MB | 2 | 846.768 | 32.762 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 59251) rss_mb | MB | 1 | 24.496 | 24.496 | 24.496 | 24.496 | n/a | n/a |
| docker (PID 59251) vms_mb | MB | 1 | 1588.270 | 1588.270 | 1588.270 | 1588.270 | n/a | n/a |
| docker (PID 59259) rss_mb | MB | 1 | 26.727 | 26.727 | 26.727 | 26.727 | n/a | n/a |
| docker (PID 59259) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 59298) CPU | percent | 3 | 3.258 | 0.000 | 9.775 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [arch_0000] (PID 59298) rss_mb | MB | 4 | 3.553 | 0.633 | 12.312 | 0.633 | n/a | n/a |
| runc:[2:INIT] [arch_0000] (PID 59298) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [arch_0000] (PID 59310) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [arch_0000] (PID 59310) rss_mb | MB | 3 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [arch_0000] (PID 59310) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 59320) rss_mb | MB | 1 | 27.309 | 27.309 | 27.309 | 27.309 | n/a | n/a |
| docker (PID 59320) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 59347) rss_mb | MB | 1 | 27.445 | 27.445 | 27.445 | 27.445 | n/a | n/a |
| docker (PID 59347) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 59410) rss_mb | MB | 1 | 23.785 | 23.785 | 23.785 | 23.785 | n/a | n/a |
| docker (PID 59410) vms_mb | MB | 1 | 1660.207 | 1660.207 | 1660.207 | 1660.207 | n/a | n/a |
| docker (PID 59418) rss_mb | MB | 1 | 25.730 | 25.730 | 25.730 | 25.730 | n/a | n/a |
| docker (PID 59418) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 59470) rss_mb | MB | 1 | 5.539 | 5.539 | 5.539 | 5.539 | n/a | n/a |
| docker (PID 59470) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 59503) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 59503) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 59503) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 59503) rss_mb | MB | 38 | 27.059 | 27.059 | 27.059 | 27.059 | n/a | n/a |
| docker (PID 59503) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 59519) rss_mb | MB | 1 | 13.621 | 13.621 | 13.621 | 13.621 | n/a | n/a |
| docker (PID 59519) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 59544) rss_mb | MB | 1 | 2.027 | 2.027 | 2.027 | 2.027 | n/a | n/a |
| docker (PID 59544) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| python3 (PID 59551) CPU | percent | 3 | 98.852 | 89.015 | 108.834 | 89.015 | 0.300000 CPU seconds | n/a |
| python3 (PID 59551) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 59551) io write MB/s | MB/s | 3 | 0.708 | 0.000 | 2.125 | 2.125 | 0.214844 MB | n/a |
| python3 (PID 59551) rss_mb | MB | 4 | 28.244 | 17.641 | 34.633 | 34.633 | n/a | n/a |
| python3 (PID 59551) vms_mb | MB | 4 | 51.801 | 42.449 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 59572) rss_mb | MB | 1 | 26.859 | 26.859 | 26.859 | 26.859 | n/a | n/a |
| docker (PID 59572) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 59589) rss_mb | MB | 1 | 26.430 | 26.430 | 26.430 | 26.430 | n/a | n/a |
| docker (PID 59589) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 59603) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 59603) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 59603) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 59603) rss_mb | MB | 2 | 27.422 | 27.422 | 27.422 | 27.422 | n/a | n/a |
| docker (PID 59603) vms_mb | MB | 2 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [bake_0000] (PID 59645) CPU | percent | 3 | 3.273 | 0.000 | 9.820 | 0.000 | 0.010000 CPU seconds | n/a |
| docker-init [bake_0000] (PID 59645) rss_mb | MB | 4 | 3.746 | 0.633 | 13.086 | 0.633 | n/a | n/a |
| docker-init [bake_0000] (PID 59645) vms_mb | MB | 4 | 429.475 | 1.055 | 1714.734 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 59659) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 59659) rss_mb | MB | 3 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| tail [bake_0000] (PID 59659) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 59731) rss_mb | MB | 1 | 27.070 | 27.070 | 27.070 | 27.070 | n/a | n/a |
| docker (PID 59731) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 59750) rss_mb | MB | 1 | 11.168 | 11.168 | 11.168 | 11.168 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 59750) vms_mb | MB | 1 | 1641.965 | 1641.965 | 1641.965 | 1641.965 | n/a | n/a |
| docker (PID 59766) rss_mb | MB | 1 | 27.363 | 27.363 | 27.363 | 27.363 | n/a | n/a |
| docker (PID 59766) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 59786) rss_mb | MB | 1 | 12.477 | 12.477 | 12.477 | 12.477 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 59786) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 59804) rss_mb | MB | 1 | 26.973 | 26.973 | 26.973 | 26.973 | n/a | n/a |
| docker (PID 59804) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 59855) rss_mb | MB | 1 | 21.719 | 21.719 | 21.719 | 21.719 | n/a | n/a |
| docker (PID 59855) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 59864) rss_mb | MB | 1 | 25.512 | 25.512 | 25.512 | 25.512 | n/a | n/a |
| docker (PID 59864) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 59906) CPU | percent | 3 | 6.549 | 0.000 | 19.646 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 59906) rss_mb | MB | 4 | 3.477 | 0.633 | 12.008 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 59906) vms_mb | MB | 4 | 375.347 | 1.055 | 1498.223 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 59917) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 59917) rss_mb | MB | 3 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [bake_0000] (PID 59917) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 59927) rss_mb | MB | 1 | 27.121 | 27.121 | 27.121 | 27.121 | n/a | n/a |
| docker (PID 59927) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 59947) rss_mb | MB | 1 | 4.340 | 4.340 | 4.340 | 4.340 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 59947) vms_mb | MB | 1 | 1369.191 | 1369.191 | 1369.191 | 1369.191 | n/a | n/a |
| docker (PID 59981) rss_mb | MB | 1 | 6.398 | 6.398 | 6.398 | 6.398 | n/a | n/a |
| docker (PID 59981) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 60016) rss_mb | MB | 1 | 24.598 | 24.598 | 24.598 | 24.598 | n/a | n/a |
| docker (PID 60016) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 60024) rss_mb | MB | 1 | 25.879 | 25.879 | 25.879 | 25.879 | n/a | n/a |
| docker (PID 60024) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 60084) CPU | percent | 1 | 9.818 | 9.818 | 9.818 | 9.818 | 0.010000 CPU seconds | n/a |
| docker (PID 60084) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60084) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60084) rss_mb | MB | 2 | 22.545 | 18.543 | 26.547 | 26.547 | n/a | n/a |
| docker (PID 60084) vms_mb | MB | 2 | 1588.236 | 1515.699 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 60123) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 60123) rss_mb | MB | 4 | 3.688 | 0.633 | 12.855 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 60123) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 60136) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 60136) rss_mb | MB | 3 | 1.809 | 1.809 | 1.809 | 1.809 | n/a | n/a |
| tail [bake_0000] (PID 60136) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 60147) rss_mb | MB | 1 | 27.426 | 27.426 | 27.426 | 27.426 | n/a | n/a |
| docker (PID 60147) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 60166) rss_mb | MB | 1 | 11.777 | 11.777 | 11.777 | 11.777 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 60166) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 60200) rss_mb | MB | 1 | 27.016 | 27.016 | 27.016 | 27.016 | n/a | n/a |
| docker (PID 60200) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 60246) CPU | percent | 1 | 9.707 | 9.707 | 9.707 | 9.707 | 0.010000 CPU seconds | n/a |
| docker (PID 60246) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60246) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60246) rss_mb | MB | 2 | 25.492 | 24.090 | 26.895 | 26.895 | n/a | n/a |
| docker (PID 60246) vms_mb | MB | 2 | 1624.490 | 1588.207 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 60330) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 60330) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60330) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60330) rss_mb | MB | 38 | 25.215 | 25.215 | 25.215 | 25.215 | n/a | n/a |
| docker (PID 60330) vms_mb | MB | 38 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 60346) rss_mb | MB | 1 | 25.520 | 25.520 | 25.520 | 25.520 | n/a | n/a |
| docker (PID 60346) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 60372) rss_mb | MB | 1 | 26.410 | 26.410 | 26.410 | 26.410 | n/a | n/a |
| docker (PID 60372) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 60412) CPU | percent | 3 | 6.507 | 0.000 | 19.521 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 60412) rss_mb | MB | 4 | 3.000 | 0.633 | 10.102 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 60412) vms_mb | MB | 4 | 411.153 | 1.055 | 1641.449 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 60425) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 60425) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [bake_0000] (PID 60425) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 60435) rss_mb | MB | 1 | 19.504 | 19.504 | 19.504 | 19.504 | n/a | n/a |
| docker (PID 60435) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 60463) rss_mb | MB | 1 | 27.188 | 27.188 | 27.188 | 27.188 | n/a | n/a |
| docker (PID 60463) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 60482) rss_mb | MB | 1 | 11.820 | 11.820 | 11.820 | 11.820 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 60482) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 60499) rss_mb | MB | 1 | 27.293 | 27.293 | 27.293 | 27.293 | n/a | n/a |
| docker (PID 60499) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| sh [bake_0000] (PID 60516) rss_mb | MB | 1 | 1.746 | 1.746 | 1.746 | 1.746 | n/a | n/a |
| sh [bake_0000] (PID 60516) vms_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| sh [bake_0000] (PID 60524) rss_mb | MB | 1 | 1.746 | 1.746 | 1.746 | 1.746 | n/a | n/a |
| sh [bake_0000] (PID 60524) vms_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| docker (PID 60534) rss_mb | MB | 1 | 25.941 | 25.941 | 25.941 | 25.941 | n/a | n/a |
| docker (PID 60534) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 60593) rss_mb | MB | 1 | 26.918 | 26.918 | 26.918 | 26.918 | n/a | n/a |
| docker (PID 60593) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [bake_0000] (PID 60633) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bake_0000] (PID 60633) rss_mb | MB | 11 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bake_0000] (PID 60633) vms_mb | MB | 11 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 60647) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 60647) rss_mb | MB | 11 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [bake_0000] (PID 60647) vms_mb | MB | 11 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 60649) rss_mb | MB | 1 | 5.719 | 5.719 | 5.719 | 5.719 | n/a | n/a |
| docker (PID 60649) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 60684) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 60684) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60684) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60684) rss_mb | MB | 9 | 27.243 | 26.688 | 27.312 | 27.312 | n/a | n/a |
| docker (PID 60684) vms_mb | MB | 9 | 1732.722 | 1732.277 | 1732.777 | 1732.777 | n/a | n/a |
| bash [bake_0000] (PID 60704) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bake_0000] (PID 60704) rss_mb | MB | 8 | 3.203 | 3.203 | 3.203 | 3.203 | n/a | n/a |
| bash [bake_0000] (PID 60704) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bake_0000] (PID 60713) CPU | percent | 7 | 99.346 | 87.709 | 107.790 | 97.991 | 0.710000 CPU seconds | n/a |
| python [bake_0000] (PID 60713) rss_mb | MB | 8 | 32.367 | 13.910 | 42.152 | 42.152 | n/a | n/a |
| python [bake_0000] (PID 60713) vms_mb | MB | 8 | 39.237 | 17.926 | 51.375 | 51.375 | n/a | n/a |
| docker (PID 60723) CPU | percent | 1 | 9.784 | 9.784 | 9.784 | 9.784 | 0.010000 CPU seconds | n/a |
| docker (PID 60723) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60723) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60723) rss_mb | MB | 2 | 21.465 | 15.828 | 27.102 | 27.102 | n/a | n/a |
| docker (PID 60723) vms_mb | MB | 2 | 1588.361 | 1515.949 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 60783) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 60783) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60783) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60783) rss_mb | MB | 3 | 25.629 | 25.629 | 25.629 | 25.629 | n/a | n/a |
| docker (PID 60783) vms_mb | MB | 3 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 60821) CPU | percent | 11 | 5.221 | 0.000 | 57.432 | 0.000 | 0.060000 CPU seconds | n/a |
| runc:[2:INIT] [bake_0000] (PID 60821) rss_mb | MB | 12 | 2.613 | 0.633 | 12.918 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 60821) vms_mb | MB | 12 | 262.604 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bake_0000] (PID 60834) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bake_0000] (PID 60834) rss_mb | MB | 10 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bake_0000] (PID 60834) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 60845) CPU | percent | 2 | 18.273 | 0.000 | 36.545 | 0.000 | 0.040000 CPU seconds | n/a |
| docker (PID 60845) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60845) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60845) rss_mb | MB | 3 | 22.000 | 11.141 | 27.430 | 27.430 | n/a | n/a |
| docker (PID 60845) vms_mb | MB | 3 | 1636.500 | 1587.953 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[0:PARENT] [bake_0000] (PID 60860) rss_mb | MB | 1 | 1.961 | 1.961 | 1.961 | 1.961 | n/a | n/a |
| runc:[0:PARENT] [bake_0000] (PID 60860) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[1:CHILD] [bake_0000] (PID 60864) rss_mb | MB | 1 | 0.125 | 0.125 | 0.125 | 0.125 | n/a | n/a |
| runc:[1:CHILD] [bake_0000] (PID 60864) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| docker (PID 60871) CPU | percent | 2 | 28.485 | 0.000 | 56.969 | 0.000 | 0.070000 CPU seconds | n/a |
| docker (PID 60871) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60871) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60871) rss_mb | MB | 3 | 18.072 | 0.129 | 27.043 | 27.043 | n/a | n/a |
| docker (PID 60871) vms_mb | MB | 3 | 1117.372 | 30.570 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 60891) rss_mb | MB | 1 | 12.527 | 12.527 | 12.527 | 12.527 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 60891) vms_mb | MB | 1 | 1570.727 | 1570.727 | 1570.727 | 1570.727 | n/a | n/a |
| docker (PID 60906) CPU | percent | 1 | 58.680 | 58.680 | 58.680 | 58.680 | 0.060000 CPU seconds | n/a |
| docker (PID 60906) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60906) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60906) rss_mb | MB | 2 | 22.008 | 17.035 | 26.980 | 26.980 | n/a | n/a |
| docker (PID 60906) vms_mb | MB | 2 | 1588.361 | 1515.949 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 60926) rss_mb | MB | 1 | 4.055 | 4.055 | 4.055 | 4.055 | n/a | n/a |
| runc:[2:INIT] [bake_0000] (PID 60926) vms_mb | MB | 1 | 1216.680 | 1216.680 | 1216.680 | 1216.680 | n/a | n/a |
| docker (PID 60941) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 60941) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60941) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 60941) rss_mb | MB | 2 | 27.152 | 27.152 | 27.152 | 27.152 | n/a | n/a |
| docker (PID 60941) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 61017) rss_mb | MB | 1 | 18.961 | 18.961 | 18.961 | 18.961 | n/a | n/a |
| docker (PID 61017) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 61025) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 61025) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 61025) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 61025) rss_mb | MB | 39 | 26.664 | 26.664 | 26.664 | 26.664 | n/a | n/a |
| docker (PID 61025) vms_mb | MB | 39 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 61059) rss_mb | MB | 1 | 25.387 | 25.387 | 25.387 | 25.387 | n/a | n/a |
| docker (PID 61059) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| python3 (PID 61074) CPU | percent | 3 | 98.778 | 98.583 | 98.881 | 98.881 | 0.300000 CPU seconds | n/a |
| python3 (PID 61074) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 61074) io write MB/s | MB/s | 3 | 0.708 | 0.000 | 2.124 | 2.124 | 0.214844 MB | n/a |
| python3 (PID 61074) rss_mb | MB | 4 | 25.631 | 12.609 | 34.488 | 34.488 | n/a | n/a |
| python3 (PID 61074) vms_mb | MB | 4 | 49.737 | 38.426 | 57.434 | 57.434 | n/a | n/a |
| docker (PID 61111) rss_mb | MB | 1 | 21.762 | 21.762 | 21.762 | 21.762 | n/a | n/a |
| docker (PID 61111) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 61126) CPU | percent | 1 | 9.867 | 9.867 | 9.867 | 9.867 | 0.010000 CPU seconds | n/a |
| docker (PID 61126) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 61126) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 61126) rss_mb | MB | 2 | 27.023 | 26.809 | 27.238 | 27.238 | n/a | n/a |
| docker (PID 61126) vms_mb | MB | 2 | 1696.775 | 1660.773 | 1732.777 | 1732.777 | n/a | n/a |
| docker-init [bale_0000] (PID 61167) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bale_0000] (PID 61167) rss_mb | MB | 4 | 3.719 | 0.633 | 12.977 | 0.633 | n/a | n/a |
| docker-init [bale_0000] (PID 61167) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 61179) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 61179) rss_mb | MB | 3 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [bale_0000] (PID 61179) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 61181) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 61181) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 61243) rss_mb | MB | 1 | 18.105 | 18.105 | 18.105 | 18.105 | n/a | n/a |
| docker (PID 61243) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 61279) rss_mb | MB | 1 | 27.379 | 27.379 | 27.379 | 27.379 | n/a | n/a |
| docker (PID 61279) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 61317) rss_mb | MB | 1 | 26.910 | 26.910 | 26.910 | 26.910 | n/a | n/a |
| docker (PID 61317) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 61367) rss_mb | MB | 1 | 2.074 | 2.074 | 2.074 | 2.074 | n/a | n/a |
| docker (PID 61367) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 61376) rss_mb | MB | 1 | 25.543 | 25.543 | 25.543 | 25.543 | n/a | n/a |
| docker (PID 61376) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 61417) CPU | percent | 3 | 9.726 | 0.000 | 29.178 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 61417) rss_mb | MB | 4 | 3.439 | 0.633 | 11.859 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 61417) vms_mb | MB | 4 | 393.281 | 1.055 | 1569.961 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 61429) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 61429) rss_mb | MB | 3 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [bale_0000] (PID 61429) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 61439) rss_mb | MB | 1 | 27.363 | 27.363 | 27.363 | 27.363 | n/a | n/a |
| docker (PID 61439) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 61494) rss_mb | MB | 1 | 2.688 | 2.688 | 2.688 | 2.688 | n/a | n/a |
| docker (PID 61494) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 61502) rss_mb | MB | 1 | 27.254 | 27.254 | 27.254 | 27.254 | n/a | n/a |
| docker (PID 61502) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| sh [bale_0000] (PID 61521) rss_mb | MB | 1 | 1.656 | 1.656 | 1.656 | 1.656 | n/a | n/a |
| sh [bale_0000] (PID 61521) vms_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| base64 [bale_0000] (PID 61528) rss_mb | MB | 1 | 1.422 | 1.422 | 1.422 | 1.422 | n/a | n/a |
| base64 [bale_0000] (PID 61528) vms_mb | MB | 1 | 2.586 | 2.586 | 2.586 | 2.586 | n/a | n/a |
| docker (PID 61538) rss_mb | MB | 1 | 25.902 | 25.902 | 25.902 | 25.902 | n/a | n/a |
| docker (PID 61538) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 61590) rss_mb | MB | 1 | 6.574 | 6.574 | 6.574 | 6.574 | n/a | n/a |
| docker (PID 61590) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 61620) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 61620) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 61620) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 61620) rss_mb | MB | 38 | 25.660 | 25.660 | 25.660 | 25.660 | n/a | n/a |
| docker (PID 61620) vms_mb | MB | 38 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 61636) rss_mb | MB | 1 | 24.328 | 24.328 | 24.328 | 24.328 | n/a | n/a |
| docker (PID 61636) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 61654) rss_mb | MB | 1 | 13.809 | 13.809 | 13.809 | 13.809 | n/a | n/a |
| docker (PID 61654) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 61662) rss_mb | MB | 1 | 27.137 | 27.137 | 27.137 | 27.137 | n/a | n/a |
| docker (PID 61662) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 61701) CPU | percent | 3 | 6.456 | 0.000 | 19.369 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 61701) rss_mb | MB | 4 | 3.237 | 0.633 | 11.051 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 61701) vms_mb | MB | 4 | 393.215 | 1.055 | 1569.695 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 61713) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 61713) rss_mb | MB | 3 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [bale_0000] (PID 61713) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 61723) rss_mb | MB | 1 | 26.711 | 26.711 | 26.711 | 26.711 | n/a | n/a |
| docker (PID 61723) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 61749) rss_mb | MB | 1 | 27.164 | 27.164 | 27.164 | 27.164 | n/a | n/a |
| docker (PID 61749) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 61769) rss_mb | MB | 1 | 12.426 | 12.426 | 12.426 | 12.426 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 61769) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 61816) rss_mb | MB | 1 | 1.781 | 1.781 | 1.781 | 1.781 | n/a | n/a |
| docker (PID 61816) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 61824) rss_mb | MB | 1 | 26.926 | 26.926 | 26.926 | 26.926 | n/a | n/a |
| docker (PID 61824) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 61886) rss_mb | MB | 1 | 25.586 | 25.586 | 25.586 | 25.586 | n/a | n/a |
| docker (PID 61886) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bale_0000] (PID 61923) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bale_0000] (PID 61923) rss_mb | MB | 37 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bale_0000] (PID 61923) vms_mb | MB | 37 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 61937) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 61937) rss_mb | MB | 37 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [bale_0000] (PID 61937) vms_mb | MB | 37 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 61941) rss_mb | MB | 1 | 20.902 | 20.902 | 20.902 | 20.902 | n/a | n/a |
| docker (PID 61941) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 61977) CPU | percent | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 61977) io read MB/s | MB/s | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 61977) io write MB/s | MB/s | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 61977) rss_mb | MB | 35 | 27.512 | 27.512 | 27.512 | 27.512 | n/a | n/a |
| docker (PID 61977) vms_mb | MB | 35 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| bash [bale_0000] (PID 61996) CPU | percent | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bale_0000] (PID 61996) rss_mb | MB | 34 | 3.348 | 3.348 | 3.348 | 3.348 | n/a | n/a |
| bash [bale_0000] (PID 61996) vms_mb | MB | 34 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bale_0000] (PID 62005) CPU | percent | 33 | 99.875 | 97.559 | 107.998 | 98.173 | 3.360000 CPU seconds | n/a |
| python [bale_0000] (PID 62005) rss_mb | MB | 34 | 39.027 | 15.047 | 41.773 | 40.969 | n/a | n/a |
| python [bale_0000] (PID 62005) vms_mb | MB | 34 | 47.798 | 18.508 | 51.289 | 50.324 | n/a | n/a |
| docker (PID 62015) rss_mb | MB | 1 | 26.090 | 26.090 | 26.090 | 26.090 | n/a | n/a |
| docker (PID 62015) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 62074) CPU | percent | 1 | 9.858 | 9.858 | 9.858 | 9.858 | 0.010000 CPU seconds | n/a |
| docker (PID 62074) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 62074) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 62074) rss_mb | MB | 2 | 25.391 | 24.008 | 26.773 | 26.773 | n/a | n/a |
| docker (PID 62074) vms_mb | MB | 2 | 1624.490 | 1588.207 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 62114) CPU | percent | 3 | 3.261 | 0.000 | 9.783 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [bale_0000] (PID 62114) rss_mb | MB | 4 | 3.631 | 0.633 | 12.625 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 62114) vms_mb | MB | 4 | 375.347 | 1.055 | 1498.223 | 1.055 | n/a | n/a |
| tail [bale_0000] (PID 62125) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bale_0000] (PID 62125) rss_mb | MB | 3 | 1.695 | 1.695 | 1.695 | 1.695 | n/a | n/a |
| tail [bale_0000] (PID 62125) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 62135) rss_mb | MB | 1 | 27.426 | 27.426 | 27.426 | 27.426 | n/a | n/a |
| docker (PID 62135) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 62153) rss_mb | MB | 1 | 10.301 | 10.301 | 10.301 | 10.301 | n/a | n/a |
| runc:[2:INIT] [bale_0000] (PID 62153) vms_mb | MB | 1 | 1569.695 | 1569.695 | 1569.695 | 1569.695 | n/a | n/a |
| docker (PID 62188) rss_mb | MB | 1 | 9.680 | 9.680 | 9.680 | 9.680 | n/a | n/a |
| docker (PID 62188) vms_mb | MB | 1 | 1387.949 | 1387.949 | 1387.949 | 1387.949 | n/a | n/a |
| docker (PID 62222) rss_mb | MB | 1 | 26.848 | 26.848 | 26.848 | 26.848 | n/a | n/a |
| docker (PID 62222) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 62231) rss_mb | MB | 1 | 25.945 | 25.945 | 25.945 | 25.945 | n/a | n/a |
| docker (PID 62231) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 62293) rss_mb | MB | 1 | 7.219 | 7.219 | 7.219 | 7.219 | n/a | n/a |
| docker (PID 62293) vms_mb | MB | 1 | 32.867 | 32.867 | 32.867 | 32.867 | n/a | n/a |
| docker (PID 62317) CPU | percent | 38 | 0.260 | 0.000 | 9.867 | 0.000 | 0.010000 CPU seconds | n/a |
| docker (PID 62317) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 62317) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 62317) rss_mb | MB | 39 | 26.958 | 25.805 | 26.988 | 26.988 | n/a | n/a |
| docker (PID 62317) vms_mb | MB | 39 | 1660.761 | 1660.273 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 62341) rss_mb | MB | 1 | 26.949 | 26.949 | 26.949 | 26.949 | n/a | n/a |
| docker (PID 62341) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 62364) CPU | percent | 33 | 99.601 | 88.920 | 108.863 | 98.221 | 3.340000 CPU seconds | n/a |
| python3 (PID 62364) io read MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 62364) io write MB/s | MB/s | 33 | 0.064 | 0.000 | 2.103 | 0.000 | 0.214844 MB | n/a |
| python3 (PID 62364) rss_mb | MB | 34 | 32.531 | 3.008 | 34.617 | 34.617 | n/a | n/a |
| python3 (PID 62364) vms_mb | MB | 34 | 55.402 | 33.539 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 62394) rss_mb | MB | 1 | 0.270 | 0.270 | 0.270 | 0.270 | n/a | n/a |
| docker (PID 62394) vms_mb | MB | 1 | 32.750 | 32.750 | 32.750 | 32.750 | n/a | n/a |
| docker (PID 62416) CPU | percent | 1 | 9.857 | 9.857 | 9.857 | 9.857 | 0.010000 CPU seconds | n/a |
| docker (PID 62416) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 62416) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 62416) rss_mb | MB | 2 | 27.340 | 26.973 | 27.707 | 27.707 | n/a | n/a |
| docker (PID 62416) vms_mb | MB | 2 | 1733.027 | 1661.023 | 1805.031 | 1805.031 | n/a | n/a |
| docker-init [band_0000] (PID 62456) CPU | percent | 4 | 4.900 | 0.000 | 19.602 | 0.000 | 0.020000 CPU seconds | n/a |
| docker-init [band_0000] (PID 62456) rss_mb | MB | 5 | 2.752 | 0.633 | 11.230 | 0.633 | n/a | n/a |
| docker-init [band_0000] (PID 62456) vms_mb | MB | 5 | 314.733 | 1.055 | 1569.445 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 62470) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 62470) rss_mb | MB | 4 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [band_0000] (PID 62470) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 62472) rss_mb | MB | 1 | 27.305 | 27.305 | 27.305 | 27.305 | n/a | n/a |
| docker (PID 62472) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] (PID 62492) rss_mb | MB | 1 | 11.133 | 11.133 | 11.133 | 11.133 | n/a | n/a |
| runc:[2:INIT] (PID 62492) vms_mb | MB | 1 | 1641.707 | 1641.707 | 1641.707 | 1641.707 | n/a | n/a |
| docker (PID 62509) rss_mb | MB | 1 | 27.535 | 27.535 | 27.535 | 27.535 | n/a | n/a |
| docker (PID 62509) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 62531) rss_mb | MB | 1 | 11.691 | 11.691 | 11.691 | 11.691 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 62531) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 62572) rss_mb | MB | 1 | 17.266 | 17.266 | 17.266 | 17.266 | n/a | n/a |
| docker (PID 62572) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 62611) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 62611) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 62611) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 62611) rss_mb | MB | 2 | 26.824 | 26.824 | 26.824 | 26.824 | n/a | n/a |
| docker (PID 62611) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 62668) rss_mb | MB | 1 | 25.387 | 25.387 | 25.387 | 25.387 | n/a | n/a |
| docker (PID 62668) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [band_0000] (PID 62708) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [band_0000] (PID 62708) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [band_0000] (PID 62708) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 62721) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 62721) rss_mb | MB | 3 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [band_0000] (PID 62721) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 62723) rss_mb | MB | 1 | 23.730 | 23.730 | 23.730 | 23.730 | n/a | n/a |
| docker (PID 62723) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 62759) rss_mb | MB | 1 | 27.297 | 27.297 | 27.297 | 27.297 | n/a | n/a |
| docker (PID 62759) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 62793) rss_mb | MB | 1 | 27.309 | 27.309 | 27.309 | 27.309 | n/a | n/a |
| docker (PID 62793) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 62813) rss_mb | MB | 1 | 10.641 | 10.641 | 10.641 | 10.641 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 62813) vms_mb | MB | 1 | 1569.445 | 1569.445 | 1569.445 | 1569.445 | n/a | n/a |
| docker (PID 62830) rss_mb | MB | 1 | 26.824 | 26.824 | 26.824 | 26.824 | n/a | n/a |
| docker (PID 62830) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 62897) rss_mb | MB | 1 | 26.766 | 26.766 | 26.766 | 26.766 | n/a | n/a |
| docker (PID 62897) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 62911) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 62911) io read MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 62911) io write MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 62911) rss_mb | MB | 37 | 26.645 | 26.645 | 26.645 | 26.645 | n/a | n/a |
| docker (PID 62911) vms_mb | MB | 37 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 62927) rss_mb | MB | 1 | 26.746 | 26.746 | 26.746 | 26.746 | n/a | n/a |
| docker (PID 62927) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 62945) rss_mb | MB | 1 | 25.625 | 25.625 | 25.625 | 25.625 | n/a | n/a |
| docker (PID 62945) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 62953) rss_mb | MB | 1 | 26.918 | 26.918 | 26.918 | 26.918 | n/a | n/a |
| docker (PID 62953) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 62993) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 62993) rss_mb | MB | 4 | 3.475 | 0.633 | 12.000 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 62993) vms_mb | MB | 4 | 375.284 | 1.055 | 1497.973 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 63004) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 63004) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [band_0000] (PID 63004) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 63015) rss_mb | MB | 1 | 27.371 | 27.371 | 27.371 | 27.371 | n/a | n/a |
| docker (PID 63015) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 63034) rss_mb | MB | 1 | 10.301 | 10.301 | 10.301 | 10.301 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 63034) vms_mb | MB | 1 | 1569.445 | 1569.445 | 1569.445 | 1569.445 | n/a | n/a |
| docker (PID 63068) rss_mb | MB | 1 | 15.523 | 15.523 | 15.523 | 15.523 | n/a | n/a |
| docker (PID 63068) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 63116) rss_mb | MB | 1 | 25.762 | 25.762 | 25.762 | 25.762 | n/a | n/a |
| docker (PID 63116) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 63168) rss_mb | MB | 1 | 23.070 | 23.070 | 23.070 | 23.070 | n/a | n/a |
| docker (PID 63168) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 63176) rss_mb | MB | 1 | 26.973 | 26.973 | 26.973 | 26.973 | n/a | n/a |
| docker (PID 63176) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 63216) CPU | percent | 10 | 1.961 | 0.000 | 19.607 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [band_0000] (PID 63216) rss_mb | MB | 11 | 1.693 | 0.633 | 12.297 | 0.633 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 63216) vms_mb | MB | 11 | 150.252 | 1.055 | 1642.230 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 63229) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 63229) rss_mb | MB | 10 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [band_0000] (PID 63229) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 63239) rss_mb | MB | 1 | 26.973 | 26.973 | 26.973 | 26.973 | n/a | n/a |
| docker (PID 63239) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 63269) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 63269) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 63269) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 63269) rss_mb | MB | 8 | 27.160 | 27.160 | 27.160 | 27.160 | n/a | n/a |
| docker (PID 63269) vms_mb | MB | 8 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [band_0000] (PID 63289) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [band_0000] (PID 63289) rss_mb | MB | 8 | 3.301 | 3.301 | 3.301 | 3.301 | n/a | n/a |
| bash [band_0000] (PID 63289) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [band_0000] (PID 63299) CPU | percent | 6 | 99.548 | 97.558 | 107.427 | 98.098 | 0.610000 CPU seconds | n/a |
| python [band_0000] (PID 63299) rss_mb | MB | 7 | 32.273 | 18.641 | 41.957 | 41.957 | n/a | n/a |
| python [band_0000] (PID 63299) vms_mb | MB | 7 | 39.022 | 23.258 | 51.324 | 51.324 | n/a | n/a |
| docker (PID 63301) rss_mb | MB | 1 | 0.129 | 0.129 | 0.129 | 0.129 | n/a | n/a |
| docker (PID 63301) vms_mb | MB | 1 | 30.570 | 30.570 | 30.570 | 30.570 | n/a | n/a |
| docker (PID 63309) rss_mb | MB | 1 | 27.141 | 27.141 | 27.141 | 27.141 | n/a | n/a |
| docker (PID 63309) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 63367) rss_mb | MB | 1 | 25.340 | 25.340 | 25.340 | 25.340 | n/a | n/a |
| docker (PID 63367) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [band_0000] (PID 63406) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [band_0000] (PID 63406) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [band_0000] (PID 63406) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [band_0000] (PID 63419) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [band_0000] (PID 63419) rss_mb | MB | 3 | 1.711 | 1.711 | 1.711 | 1.711 | n/a | n/a |
| tail [band_0000] (PID 63419) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 63421) rss_mb | MB | 1 | 21.418 | 21.418 | 21.418 | 21.418 | n/a | n/a |
| docker (PID 63421) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 63459) rss_mb | MB | 1 | 27.305 | 27.305 | 27.305 | 27.305 | n/a | n/a |
| docker (PID 63459) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 63495) rss_mb | MB | 1 | 27.453 | 27.453 | 27.453 | 27.453 | n/a | n/a |
| docker (PID 63495) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 63516) rss_mb | MB | 1 | 11.469 | 11.469 | 11.469 | 11.469 | n/a | n/a |
| runc:[2:INIT] [band_0000] (PID 63516) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 63532) rss_mb | MB | 1 | 26.879 | 26.879 | 26.879 | 26.879 | n/a | n/a |
| docker (PID 63532) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 63618) rss_mb | MB | 1 | 25.621 | 25.621 | 25.621 | 25.621 | n/a | n/a |
| docker (PID 63618) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 63626) CPU | percent | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 63626) io read MB/s | MB/s | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 63626) io write MB/s | MB/s | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 63626) rss_mb | MB | 46 | 26.855 | 26.855 | 26.855 | 26.855 | n/a | n/a |
| docker (PID 63626) vms_mb | MB | 46 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 63658) rss_mb | MB | 1 | 0.410 | 0.410 | 0.410 | 0.410 | n/a | n/a |
| docker (PID 63658) vms_mb | MB | 1 | 30.602 | 30.602 | 30.602 | 30.602 | n/a | n/a |
| python3 (PID 63673) CPU | percent | 3 | 98.787 | 98.504 | 98.948 | 98.948 | 0.300000 CPU seconds | n/a |
| python3 (PID 63673) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 63673) io write MB/s | MB/s | 3 | 0.696 | 0.000 | 2.087 | 2.087 | 0.210938 MB | n/a |
| python3 (PID 63673) rss_mb | MB | 4 | 24.244 | 9.992 | 34.422 | 34.422 | n/a | n/a |
| python3 (PID 63673) vms_mb | MB | 4 | 48.571 | 36.465 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 63695) rss_mb | MB | 1 | 8.965 | 8.965 | 8.965 | 8.965 | n/a | n/a |
| docker (PID 63695) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 63711) rss_mb | MB | 1 | 26.945 | 26.945 | 26.945 | 26.945 | n/a | n/a |
| docker (PID 63711) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 63725) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 63725) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 63725) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 63725) rss_mb | MB | 2 | 27.277 | 27.277 | 27.277 | 27.277 | n/a | n/a |
| docker (PID 63725) vms_mb | MB | 2 | 1733.027 | 1733.027 | 1733.027 | 1733.027 | n/a | n/a |
| docker-init [bart_0000] (PID 63766) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bart_0000] (PID 63766) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bart_0000] (PID 63766) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 63778) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 63778) rss_mb | MB | 3 | 1.723 | 1.723 | 1.723 | 1.723 | n/a | n/a |
| tail [bart_0000] (PID 63778) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 63816) rss_mb | MB | 1 | 5.129 | 5.129 | 5.129 | 5.129 | n/a | n/a |
| docker (PID 63816) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 63844) rss_mb | MB | 1 | 27.434 | 27.434 | 27.434 | 27.434 | n/a | n/a |
| docker (PID 63844) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 63880) rss_mb | MB | 1 | 27.117 | 27.117 | 27.117 | 27.117 | n/a | n/a |
| docker (PID 63880) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 63900) rss_mb | MB | 1 | 11.070 | 11.070 | 11.070 | 11.070 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 63900) vms_mb | MB | 1 | 1569.840 | 1569.840 | 1569.840 | 1569.840 | n/a | n/a |
| docker (PID 63916) rss_mb | MB | 1 | 26.293 | 26.293 | 26.293 | 26.293 | n/a | n/a |
| docker (PID 63916) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 63966) rss_mb | MB | 1 | 19.117 | 19.117 | 19.117 | 19.117 | n/a | n/a |
| docker (PID 63966) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 63974) rss_mb | MB | 1 | 26.574 | 26.574 | 26.574 | 26.574 | n/a | n/a |
| docker (PID 63974) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 64016) CPU | percent | 3 | 6.520 | 0.000 | 19.561 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 64016) rss_mb | MB | 4 | 3.577 | 0.633 | 12.410 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 64016) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 64027) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 64027) rss_mb | MB | 3 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [bart_0000] (PID 64027) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 64037) rss_mb | MB | 1 | 27.410 | 27.410 | 27.410 | 27.410 | n/a | n/a |
| docker (PID 64037) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 64067) rss_mb | MB | 1 | 27.551 | 27.551 | 27.551 | 27.551 | n/a | n/a |
| docker (PID 64067) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 64130) rss_mb | MB | 1 | 6.281 | 6.281 | 6.281 | 6.281 | n/a | n/a |
| docker (PID 64130) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 64138) rss_mb | MB | 1 | 26.707 | 26.707 | 26.707 | 26.707 | n/a | n/a |
| docker (PID 64138) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 64198) CPU | percent | 1 | 9.841 | 9.841 | 9.841 | 9.841 | 0.010000 CPU seconds | n/a |
| docker (PID 64198) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 64198) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 64198) rss_mb | MB | 2 | 20.109 | 13.414 | 26.805 | 26.805 | n/a | n/a |
| docker (PID 64198) vms_mb | MB | 2 | 1588.236 | 1515.699 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 64238) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 64238) rss_mb | MB | 3 | 4.734 | 0.633 | 12.938 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 64238) vms_mb | MB | 3 | 524.112 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 64251) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 64251) rss_mb | MB | 2 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bart_0000] (PID 64251) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 64264) rss_mb | MB | 1 | 27.078 | 27.078 | 27.078 | 27.078 | n/a | n/a |
| docker (PID 64264) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 64283) rss_mb | MB | 1 | 11.664 | 11.664 | 11.664 | 11.664 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 64283) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 64323) rss_mb | MB | 1 | 17.656 | 17.656 | 17.656 | 17.656 | n/a | n/a |
| docker (PID 64323) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 64332) rss_mb | MB | 1 | 27.109 | 27.109 | 27.109 | 27.109 | n/a | n/a |
| docker (PID 64332) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 64392) rss_mb | MB | 1 | 25.223 | 25.223 | 25.223 | 25.223 | n/a | n/a |
| docker (PID 64392) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bart_0000] (PID 64430) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bart_0000] (PID 64430) rss_mb | MB | 2 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bart_0000] (PID 64430) vms_mb | MB | 2 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 64443) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 64443) rss_mb | MB | 2 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [bart_0000] (PID 64443) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 64445) rss_mb | MB | 1 | 22.016 | 22.016 | 22.016 | 22.016 | n/a | n/a |
| docker (PID 64445) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 64480) rss_mb | MB | 1 | 27.238 | 27.238 | 27.238 | 27.238 | n/a | n/a |
| docker (PID 64480) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 64521) rss_mb | MB | 1 | 26.863 | 26.863 | 26.863 | 26.863 | n/a | n/a |
| docker (PID 64521) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 64557) rss_mb | MB | 1 | 22.883 | 22.883 | 22.883 | 22.883 | n/a | n/a |
| docker (PID 64557) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 64574) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 64574) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 64574) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 64574) rss_mb | MB | 2 | 26.887 | 26.887 | 26.887 | 26.887 | n/a | n/a |
| docker (PID 64574) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 64613) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 64613) rss_mb | MB | 3 | 4.704 | 0.633 | 12.848 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 64613) vms_mb | MB | 3 | 524.195 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 64627) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 64627) rss_mb | MB | 2 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [bart_0000] (PID 64627) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 64637) rss_mb | MB | 1 | 27.176 | 27.176 | 27.176 | 27.176 | n/a | n/a |
| docker (PID 64637) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 64657) rss_mb | MB | 1 | 11.984 | 11.984 | 11.984 | 11.984 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 64657) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 64699) rss_mb | MB | 1 | 23.000 | 23.000 | 23.000 | 23.000 | n/a | n/a |
| docker (PID 64699) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 64736) rss_mb | MB | 1 | 26.027 | 26.027 | 26.027 | 26.027 | n/a | n/a |
| docker (PID 64736) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 64777) rss_mb | MB | 1 | 16.914 | 16.914 | 16.914 | 16.914 | n/a | n/a |
| docker (PID 64777) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 64794) rss_mb | MB | 1 | 19.883 | 19.883 | 19.883 | 19.883 | n/a | n/a |
| docker (PID 64794) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 64816) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 64816) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 64816) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 64816) rss_mb | MB | 38 | 25.609 | 25.609 | 25.609 | 25.609 | n/a | n/a |
| docker (PID 64816) vms_mb | MB | 38 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 64859) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 64859) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 64859) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 64859) rss_mb | MB | 2 | 25.859 | 25.859 | 25.859 | 25.859 | n/a | n/a |
| docker (PID 64859) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 64899) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 64899) rss_mb | MB | 4 | 3.705 | 0.633 | 12.922 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 64899) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 64911) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 64911) rss_mb | MB | 3 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [bart_0000] (PID 64911) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 64921) rss_mb | MB | 1 | 26.879 | 26.879 | 26.879 | 26.879 | n/a | n/a |
| docker (PID 64921) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 64940) rss_mb | MB | 1 | 12.250 | 12.250 | 12.250 | 12.250 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 64940) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 64983) rss_mb | MB | 1 | 10.039 | 10.039 | 10.039 | 10.039 | n/a | n/a |
| docker (PID 64983) vms_mb | MB | 1 | 1459.953 | 1459.953 | 1459.953 | 1459.953 | n/a | n/a |
| docker (PID 65021) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 65021) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 65021) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 65021) rss_mb | MB | 2 | 25.809 | 25.809 | 25.809 | 25.809 | n/a | n/a |
| docker (PID 65021) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 65082) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 65082) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 65082) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 65082) rss_mb | MB | 2 | 24.977 | 22.961 | 26.992 | 26.992 | n/a | n/a |
| docker (PID 65082) vms_mb | MB | 2 | 1660.490 | 1588.203 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 65122) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 65122) rss_mb | MB | 11 | 1.744 | 0.633 | 12.859 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 65122) vms_mb | MB | 11 | 143.729 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 65135) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 65135) rss_mb | MB | 10 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bart_0000] (PID 65135) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 65145) rss_mb | MB | 1 | 27.270 | 27.270 | 27.270 | 27.270 | n/a | n/a |
| docker (PID 65145) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 65165) rss_mb | MB | 1 | 12.078 | 12.078 | 12.078 | 12.078 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 65165) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 65173) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 65173) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 65173) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 65173) rss_mb | MB | 8 | 27.531 | 27.531 | 27.531 | 27.531 | n/a | n/a |
| docker (PID 65173) vms_mb | MB | 8 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| bash [bart_0000] (PID 65193) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bart_0000] (PID 65193) rss_mb | MB | 8 | 3.410 | 3.410 | 3.410 | 3.410 | n/a | n/a |
| bash [bart_0000] (PID 65193) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bart_0000] (PID 65203) CPU | percent | 7 | 100.786 | 88.230 | 107.906 | 107.893 | 0.720000 CPU seconds | n/a |
| python [bart_0000] (PID 65203) rss_mb | MB | 8 | 30.654 | 10.844 | 40.742 | 40.742 | n/a | n/a |
| python [bart_0000] (PID 65203) vms_mb | MB | 8 | 37.943 | 14.891 | 50.324 | 50.324 | n/a | n/a |
| docker (PID 65214) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 65214) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 65214) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 65214) rss_mb | MB | 2 | 26.914 | 26.914 | 26.914 | 26.914 | n/a | n/a |
| docker (PID 65214) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 65264) rss_mb | MB | 1 | 1.625 | 1.625 | 1.625 | 1.625 | n/a | n/a |
| docker (PID 65264) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 65272) rss_mb | MB | 1 | 25.488 | 25.488 | 25.488 | 25.488 | n/a | n/a |
| docker (PID 65272) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 65312) CPU | percent | 3 | 6.515 | 0.000 | 19.546 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bart_0000] (PID 65312) rss_mb | MB | 4 | 3.400 | 0.633 | 11.703 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 65312) vms_mb | MB | 4 | 411.280 | 1.055 | 1641.957 | 1.055 | n/a | n/a |
| tail [bart_0000] (PID 65326) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bart_0000] (PID 65326) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [bart_0000] (PID 65326) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 65336) rss_mb | MB | 1 | 27.645 | 27.645 | 27.645 | 27.645 | n/a | n/a |
| docker (PID 65336) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 65363) rss_mb | MB | 1 | 27.281 | 27.281 | 27.281 | 27.281 | n/a | n/a |
| docker (PID 65363) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 65382) rss_mb | MB | 1 | 12.105 | 12.105 | 12.105 | 12.105 | n/a | n/a |
| runc:[2:INIT] [bart_0000] (PID 65382) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 65427) rss_mb | MB | 1 | 16.211 | 16.211 | 16.211 | 16.211 | n/a | n/a |
| docker (PID 65427) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 65436) rss_mb | MB | 1 | 26.168 | 26.168 | 26.168 | 26.168 | n/a | n/a |
| docker (PID 65436) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 65503) rss_mb | MB | 1 | 15.250 | 15.250 | 15.250 | 15.250 | n/a | n/a |
| docker (PID 65503) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 65519) CPU | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 65519) io read MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 65519) io write MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 65519) rss_mb | MB | 40 | 25.762 | 25.762 | 25.762 | 25.762 | n/a | n/a |
| docker (PID 65519) vms_mb | MB | 40 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 65536) rss_mb | MB | 1 | 23.129 | 23.129 | 23.129 | 23.129 | n/a | n/a |
| docker (PID 65536) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 65561) rss_mb | MB | 1 | 20.820 | 20.820 | 20.820 | 20.820 | n/a | n/a |
| docker (PID 65561) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| python3 (PID 65568) CPU | percent | 3 | 102.067 | 98.869 | 108.458 | 98.872 | 0.310000 CPU seconds | n/a |
| python3 (PID 65568) io read MB/s | MB/s | 3 | 0.013 | 0.000 | 0.039 | 0.039 | 0.003906 MB | n/a |
| python3 (PID 65568) io write MB/s | MB/s | 3 | 0.695 | 0.000 | 2.086 | 2.086 | 0.210938 MB | n/a |
| python3 (PID 65568) rss_mb | MB | 4 | 27.472 | 16.707 | 34.449 | 34.449 | n/a | n/a |
| python3 (PID 65568) vms_mb | MB | 4 | 51.167 | 41.172 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 65582) rss_mb | MB | 1 | 2.801 | 2.801 | 2.801 | 2.801 | n/a | n/a |
| docker (PID 65582) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 65623) CPU | percent | 2 | 9.712 | 0.000 | 19.425 | 0.000 | 0.020000 CPU seconds | n/a |
| docker (PID 65623) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 65623) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 65623) rss_mb | MB | 3 | 18.742 | 0.992 | 27.617 | 27.617 | n/a | n/a |
| docker (PID 65623) vms_mb | MB | 3 | 1214.275 | 32.762 | 1805.031 | 1805.031 | n/a | n/a |
| docker-init [base_0000] (PID 65665) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [base_0000] (PID 65665) rss_mb | MB | 4 | 3.664 | 0.633 | 12.758 | 0.633 | n/a | n/a |
| docker-init [base_0000] (PID 65665) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 65677) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 65677) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [base_0000] (PID 65677) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 65709) rss_mb | MB | 1 | 18.121 | 18.121 | 18.121 | 18.121 | n/a | n/a |
| docker (PID 65709) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 65744) rss_mb | MB | 1 | 27.441 | 27.441 | 27.441 | 27.441 | n/a | n/a |
| docker (PID 65744) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 65778) rss_mb | MB | 1 | 27.191 | 27.191 | 27.191 | 27.191 | n/a | n/a |
| docker (PID 65778) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 65797) rss_mb | MB | 1 | 11.770 | 11.770 | 11.770 | 11.770 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 65797) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 65814) rss_mb | MB | 1 | 25.836 | 25.836 | 25.836 | 25.836 | n/a | n/a |
| docker (PID 65814) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 65873) rss_mb | MB | 1 | 27.332 | 27.332 | 27.332 | 27.332 | n/a | n/a |
| docker (PID 65873) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 65913) CPU | percent | 6 | 3.244 | 0.000 | 19.464 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 65913) rss_mb | MB | 7 | 2.058 | 0.594 | 10.844 | 0.594 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 65913) vms_mb | MB | 7 | 225.075 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 65927) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 65927) rss_mb | MB | 6 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [base_0000] (PID 65927) vms_mb | MB | 6 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 65938) rss_mb | MB | 1 | 27.141 | 27.141 | 27.141 | 27.141 | n/a | n/a |
| docker (PID 65938) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 65957) rss_mb | MB | 1 | 11.473 | 11.473 | 11.473 | 11.473 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 65957) vms_mb | MB | 1 | 1642.230 | 1642.230 | 1642.230 | 1642.230 | n/a | n/a |
| docker (PID 65965) CPU | percent | 1 | 48.833 | 48.833 | 48.833 | 48.833 | 0.050000 CPU seconds | n/a |
| docker (PID 65965) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 65965) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 65965) rss_mb | MB | 2 | 18.020 | 8.719 | 27.320 | 27.320 | n/a | n/a |
| docker (PID 65965) vms_mb | MB | 2 | 1444.104 | 1227.434 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 65985) rss_mb | MB | 1 | 10.312 | 10.312 | 10.312 | 10.312 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 65985) vms_mb | MB | 1 | 1569.195 | 1569.195 | 1569.195 | 1569.195 | n/a | n/a |
| docker (PID 66000) rss_mb | MB | 1 | 27.137 | 27.137 | 27.137 | 27.137 | n/a | n/a |
| docker (PID 66000) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 66036) CPU | percent | 2 | 9.717 | 0.000 | 19.433 | 0.000 | 0.020000 CPU seconds | n/a |
| docker (PID 66036) io read MB/s | MB/s | 2 | 0.531 | 0.000 | 1.063 | 0.000 | 0.109375 MB | n/a |
| docker (PID 66036) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 66036) rss_mb | MB | 3 | 23.216 | 15.531 | 27.059 | 27.059 | n/a | n/a |
| docker (PID 66036) vms_mb | MB | 3 | 1612.415 | 1515.699 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 66120) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 66120) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 66120) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 66120) rss_mb | MB | 38 | 26.856 | 23.684 | 26.941 | 26.941 | n/a | n/a |
| docker (PID 66120) vms_mb | MB | 38 | 1658.864 | 1588.203 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 66144) rss_mb | MB | 1 | 12.742 | 12.742 | 12.742 | 12.742 | n/a | n/a |
| docker (PID 66144) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 66163) rss_mb | MB | 1 | 25.469 | 25.469 | 25.469 | 25.469 | n/a | n/a |
| docker (PID 66163) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [base_0000] (PID 66202) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [base_0000] (PID 66202) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [base_0000] (PID 66202) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 66216) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 66216) rss_mb | MB | 3 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [base_0000] (PID 66216) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 66218) rss_mb | MB | 1 | 2.633 | 2.633 | 2.633 | 2.633 | n/a | n/a |
| docker (PID 66218) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 66254) rss_mb | MB | 1 | 27.105 | 27.105 | 27.105 | 27.105 | n/a | n/a |
| docker (PID 66254) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 66292) rss_mb | MB | 1 | 27.445 | 27.445 | 27.445 | 27.445 | n/a | n/a |
| docker (PID 66292) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 66313) rss_mb | MB | 1 | 10.398 | 10.398 | 10.398 | 10.398 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 66313) vms_mb | MB | 1 | 1569.445 | 1569.445 | 1569.445 | 1569.445 | n/a | n/a |
| docker (PID 66331) rss_mb | MB | 1 | 26.004 | 26.004 | 26.004 | 26.004 | n/a | n/a |
| docker (PID 66331) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 66372) rss_mb | MB | 1 | 22.387 | 22.387 | 22.387 | 22.387 | n/a | n/a |
| docker (PID 66372) vms_mb | MB | 1 | 1524.203 | 1524.203 | 1524.203 | 1524.203 | n/a | n/a |
| docker (PID 66389) rss_mb | MB | 1 | 26.633 | 26.633 | 26.633 | 26.633 | n/a | n/a |
| docker (PID 66389) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 66427) CPU | percent | 10 | 0.941 | 0.000 | 9.411 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 66427) rss_mb | MB | 11 | 1.713 | 0.633 | 12.512 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 66427) vms_mb | MB | 11 | 150.275 | 1.055 | 1642.480 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 66440) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 66440) rss_mb | MB | 10 | 1.711 | 1.711 | 1.711 | 1.711 | n/a | n/a |
| tail [base_0000] (PID 66440) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 66452) rss_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| docker (PID 66452) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 66473) rss_mb | MB | 1 | 8.934 | 8.934 | 8.934 | 8.934 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 66473) vms_mb | MB | 1 | 1569.195 | 1569.195 | 1569.195 | 1569.195 | n/a | n/a |
| docker (PID 66481) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 66481) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 66481) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 66481) rss_mb | MB | 9 | 27.125 | 27.098 | 27.223 | 27.223 | n/a | n/a |
| docker (PID 66481) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [base_0000] (PID 66500) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [base_0000] (PID 66500) rss_mb | MB | 8 | 3.480 | 3.480 | 3.480 | 3.480 | n/a | n/a |
| bash [base_0000] (PID 66500) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [base_0000] (PID 66509) CPU | percent | 7 | 99.305 | 87.407 | 107.845 | 98.014 | 0.710000 CPU seconds | n/a |
| python [base_0000] (PID 66509) rss_mb | MB | 8 | 29.877 | 6.020 | 41.652 | 41.652 | n/a | n/a |
| python [base_0000] (PID 66509) vms_mb | MB | 8 | 37.432 | 11.809 | 51.027 | 51.027 | n/a | n/a |
| docker (PID 66519) rss_mb | MB | 1 | 26.914 | 26.914 | 26.914 | 26.914 | n/a | n/a |
| docker (PID 66519) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 66578) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 66578) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 66578) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 66578) rss_mb | MB | 2 | 25.730 | 25.730 | 25.730 | 25.730 | n/a | n/a |
| docker (PID 66578) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 66621) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 66621) rss_mb | MB | 4 | 3.718 | 0.633 | 12.973 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 66621) vms_mb | MB | 4 | 393.473 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 66634) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 66634) rss_mb | MB | 3 | 1.824 | 1.824 | 1.824 | 1.824 | n/a | n/a |
| tail [base_0000] (PID 66634) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 66644) rss_mb | MB | 1 | 27.086 | 27.086 | 27.086 | 27.086 | n/a | n/a |
| docker (PID 66644) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 66671) rss_mb | MB | 1 | 27.328 | 27.328 | 27.328 | 27.328 | n/a | n/a |
| docker (PID 66671) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 66692) rss_mb | MB | 1 | 11.766 | 11.766 | 11.766 | 11.766 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 66692) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 66711) rss_mb | MB | 1 | 27.141 | 27.141 | 27.141 | 27.141 | n/a | n/a |
| docker (PID 66711) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 66731) rss_mb | MB | 1 | 11.605 | 11.605 | 11.605 | 11.605 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 66731) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 66749) rss_mb | MB | 1 | 27.059 | 27.059 | 27.059 | 27.059 | n/a | n/a |
| docker (PID 66749) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 66790) rss_mb | MB | 1 | 20.734 | 20.734 | 20.734 | 20.734 | n/a | n/a |
| docker (PID 66790) vms_mb | MB | 1 | 1524.203 | 1524.203 | 1524.203 | 1524.203 | n/a | n/a |
| docker (PID 66808) CPU | percent | 2 | 9.858 | 0.000 | 19.716 | 0.000 | 0.020000 CPU seconds | n/a |
| docker (PID 66808) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 66808) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 66808) rss_mb | MB | 3 | 20.931 | 10.871 | 25.961 | 25.961 | n/a | n/a |
| docker (PID 66808) vms_mb | MB | 3 | 1590.790 | 1451.949 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 66848) CPU | percent | 9 | 2.167 | 0.000 | 19.501 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 66848) rss_mb | MB | 10 | 1.801 | 0.633 | 12.316 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 66848) vms_mb | MB | 10 | 157.972 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 66860) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 66860) rss_mb | MB | 9 | 1.688 | 1.688 | 1.688 | 1.688 | n/a | n/a |
| tail [base_0000] (PID 66860) vms_mb | MB | 9 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 66871) rss_mb | MB | 1 | 11.594 | 11.594 | 11.594 | 11.594 | n/a | n/a |
| docker (PID 66871) vms_mb | MB | 1 | 1515.699 | 1515.699 | 1515.699 | 1515.699 | n/a | n/a |
| docker (PID 66897) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 66897) io read MB/s | MB/s | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 66897) io write MB/s | MB/s | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 66897) rss_mb | MB | 7 | 27.184 | 27.184 | 27.184 | 27.184 | n/a | n/a |
| docker (PID 66897) vms_mb | MB | 7 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| bash [base_0000] (PID 66918) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [base_0000] (PID 66918) rss_mb | MB | 6 | 3.328 | 3.328 | 3.328 | 3.328 | n/a | n/a |
| bash [base_0000] (PID 66918) vms_mb | MB | 6 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [base_0000] (PID 66927) CPU | percent | 5 | 99.520 | 88.212 | 107.701 | 96.687 | 0.510000 CPU seconds | n/a |
| python [base_0000] (PID 66927) rss_mb | MB | 6 | 26.216 | 11.484 | 34.762 | 34.762 | n/a | n/a |
| python [base_0000] (PID 66927) vms_mb | MB | 6 | 33.558 | 15.047 | 45.023 | 45.023 | n/a | n/a |
| docker (PID 66937) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 66937) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 66937) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 66937) rss_mb | MB | 2 | 25.902 | 25.902 | 25.902 | 25.902 | n/a | n/a |
| docker (PID 66937) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 66988) rss_mb | MB | 1 | 26.211 | 26.211 | 26.211 | 26.211 | n/a | n/a |
| docker (PID 66988) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 66996) rss_mb | MB | 1 | 25.465 | 25.465 | 25.465 | 25.465 | n/a | n/a |
| docker (PID 66996) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 67036) CPU | percent | 3 | 9.643 | 0.000 | 28.928 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [base_0000] (PID 67036) rss_mb | MB | 4 | 3.392 | 0.633 | 11.668 | 0.633 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 67036) vms_mb | MB | 4 | 411.250 | 1.055 | 1641.836 | 1.055 | n/a | n/a |
| tail [base_0000] (PID 67050) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [base_0000] (PID 67050) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [base_0000] (PID 67050) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 67062) rss_mb | MB | 1 | 16.430 | 16.430 | 16.430 | 16.430 | n/a | n/a |
| docker (PID 67062) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 67090) rss_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| docker (PID 67090) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 67111) rss_mb | MB | 1 | 10.203 | 10.203 | 10.203 | 10.203 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 67111) vms_mb | MB | 1 | 1569.195 | 1569.195 | 1569.195 | 1569.195 | n/a | n/a |
| docker (PID 67127) rss_mb | MB | 1 | 27.410 | 27.410 | 27.410 | 27.410 | n/a | n/a |
| docker (PID 67127) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 67147) rss_mb | MB | 1 | 11.859 | 11.859 | 11.859 | 11.859 | n/a | n/a |
| runc:[2:INIT] [base_0000] (PID 67147) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 67165) rss_mb | MB | 1 | 26.172 | 26.172 | 26.172 | 26.172 | n/a | n/a |
| docker (PID 67165) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 67240) rss_mb | MB | 1 | 25.859 | 25.859 | 25.859 | 25.859 | n/a | n/a |
| docker (PID 67240) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 67248) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 67248) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 67248) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 67248) rss_mb | MB | 39 | 26.793 | 26.793 | 26.793 | 26.793 | n/a | n/a |
| docker (PID 67248) vms_mb | MB | 39 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 67280) rss_mb | MB | 1 | 26.965 | 26.965 | 26.965 | 26.965 | n/a | n/a |
| docker (PID 67280) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 67295) CPU | percent | 3 | 102.052 | 98.472 | 108.796 | 108.796 | 0.310000 CPU seconds | n/a |
| python3 (PID 67295) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 67295) io write MB/s | MB/s | 3 | 0.657 | 0.000 | 1.970 | 1.970 | 0.199219 MB | n/a |
| python3 (PID 67295) rss_mb | MB | 4 | 26.506 | 14.324 | 34.602 | 34.602 | n/a | n/a |
| python3 (PID 67295) vms_mb | MB | 4 | 50.372 | 39.570 | 57.441 | 57.441 | n/a | n/a |
| docker (PID 67300) rss_mb | MB | 1 | 25.320 | 25.320 | 25.320 | 25.320 | n/a | n/a |
| docker (PID 67300) vms_mb | MB | 1 | 1588.207 | 1588.207 | 1588.207 | 1588.207 | n/a | n/a |
| docker (PID 67347) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 67347) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 67347) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 67347) rss_mb | MB | 3 | 27.225 | 26.707 | 27.484 | 27.484 | n/a | n/a |
| docker (PID 67347) vms_mb | MB | 3 | 1756.779 | 1660.773 | 1804.781 | 1804.781 | n/a | n/a |
| docker-init [beam_0000] (PID 67388) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beam_0000] (PID 67388) rss_mb | MB | 4 | 3.719 | 0.633 | 12.977 | 0.633 | n/a | n/a |
| docker-init [beam_0000] (PID 67388) vms_mb | MB | 4 | 393.410 | 1.055 | 1570.477 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 67400) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 67400) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [beam_0000] (PID 67400) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 67464) rss_mb | MB | 1 | 27.043 | 27.043 | 27.043 | 27.043 | n/a | n/a |
| docker (PID 67464) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 67485) rss_mb | MB | 1 | 8.508 | 8.508 | 8.508 | 8.508 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 67485) vms_mb | MB | 1 | 1569.195 | 1569.195 | 1569.195 | 1569.195 | n/a | n/a |
| docker (PID 67500) rss_mb | MB | 1 | 27.477 | 27.477 | 27.477 | 27.477 | n/a | n/a |
| docker (PID 67500) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 67520) rss_mb | MB | 1 | 11.480 | 11.480 | 11.480 | 11.480 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 67520) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 67537) rss_mb | MB | 1 | 26.070 | 26.070 | 26.070 | 26.070 | n/a | n/a |
| docker (PID 67537) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 67594) CPU | percent | 1 | 9.848 | 9.848 | 9.848 | 9.848 | 0.010000 CPU seconds | n/a |
| docker (PID 67594) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 67594) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 67594) rss_mb | MB | 2 | 15.043 | 3.031 | 27.055 | 27.055 | n/a | n/a |
| docker (PID 67594) vms_mb | MB | 2 | 846.643 | 32.762 | 1660.523 | 1660.523 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 67634) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [beam_0000] (PID 67634) rss_mb | MB | 4 | 3.484 | 0.633 | 12.039 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 67634) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 67647) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 67647) rss_mb | MB | 3 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [beam_0000] (PID 67647) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 67658) rss_mb | MB | 1 | 26.922 | 26.922 | 26.922 | 26.922 | n/a | n/a |
| docker (PID 67658) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 67678) rss_mb | MB | 1 | 10.801 | 10.801 | 10.801 | 10.801 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 67678) vms_mb | MB | 1 | 1641.578 | 1641.578 | 1641.578 | 1641.578 | n/a | n/a |
| docker (PID 67713) rss_mb | MB | 1 | 12.039 | 12.039 | 12.039 | 12.039 | n/a | n/a |
| docker (PID 67713) vms_mb | MB | 1 | 1451.699 | 1451.699 | 1451.699 | 1451.699 | n/a | n/a |
| docker (PID 67758) CPU | percent | 1 | 9.774 | 9.774 | 9.774 | 9.774 | 0.010000 CPU seconds | n/a |
| docker (PID 67758) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 67758) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 67758) rss_mb | MB | 2 | 15.012 | 3.309 | 26.715 | 26.715 | n/a | n/a |
| docker (PID 67758) vms_mb | MB | 2 | 846.768 | 32.762 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 67838) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 67838) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 67838) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 67838) rss_mb | MB | 38 | 26.941 | 26.941 | 26.941 | 26.941 | n/a | n/a |
| docker (PID 67838) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 67872) rss_mb | MB | 1 | 5.094 | 5.094 | 5.094 | 5.094 | n/a | n/a |
| docker (PID 67872) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 67880) rss_mb | MB | 1 | 27.094 | 27.094 | 27.094 | 27.094 | n/a | n/a |
| docker (PID 67880) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 67921) CPU | percent | 3 | 9.768 | 0.000 | 29.305 | 0.000 | 0.030000 CPU seconds | n/a |
| runc:[2:INIT] [beam_0000] (PID 67921) rss_mb | MB | 4 | 3.213 | 0.633 | 10.953 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 67921) vms_mb | MB | 4 | 393.090 | 1.055 | 1569.195 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 67933) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 67933) rss_mb | MB | 3 | 1.637 | 1.637 | 1.637 | 1.637 | n/a | n/a |
| tail [beam_0000] (PID 67933) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 67943) rss_mb | MB | 1 | 26.934 | 26.934 | 26.934 | 26.934 | n/a | n/a |
| docker (PID 67943) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 67971) rss_mb | MB | 1 | 27.230 | 27.230 | 27.230 | 27.230 | n/a | n/a |
| docker (PID 67971) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 67992) rss_mb | MB | 1 | 12.145 | 12.145 | 12.145 | 12.145 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 67992) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 68038) rss_mb | MB | 1 | 0.844 | 0.844 | 0.844 | 0.844 | n/a | n/a |
| docker (PID 68038) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 68046) rss_mb | MB | 1 | 25.879 | 25.879 | 25.879 | 25.879 | n/a | n/a |
| docker (PID 68046) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 68098) rss_mb | MB | 1 | 23.508 | 23.508 | 23.508 | 23.508 | n/a | n/a |
| docker (PID 68098) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 68106) rss_mb | MB | 1 | 26.781 | 26.781 | 26.781 | 26.781 | n/a | n/a |
| docker (PID 68106) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 68145) CPU | percent | 10 | 0.971 | 0.000 | 9.715 | 0.000 | 0.010000 CPU seconds | n/a |
| runc:[2:INIT] [beam_0000] (PID 68145) rss_mb | MB | 11 | 1.645 | 0.633 | 11.762 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 68145) vms_mb | MB | 11 | 143.683 | 1.055 | 1569.969 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 68159) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 68159) rss_mb | MB | 10 | 1.727 | 1.727 | 1.727 | 1.727 | n/a | n/a |
| tail [beam_0000] (PID 68159) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 68169) rss_mb | MB | 1 | 27.258 | 27.258 | 27.258 | 27.258 | n/a | n/a |
| docker (PID 68169) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 68196) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 68196) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 68196) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 68196) rss_mb | MB | 8 | 27.062 | 27.062 | 27.062 | 27.062 | n/a | n/a |
| docker (PID 68196) vms_mb | MB | 8 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [beam_0000] (PID 68215) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [beam_0000] (PID 68215) rss_mb | MB | 8 | 3.410 | 3.410 | 3.410 | 3.410 | n/a | n/a |
| bash [beam_0000] (PID 68215) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [beam_0000] (PID 68224) CPU | percent | 6 | 99.665 | 97.661 | 107.951 | 98.004 | 0.610000 CPU seconds | n/a |
| python [beam_0000] (PID 68224) rss_mb | MB | 7 | 32.780 | 18.656 | 42.730 | 42.730 | n/a | n/a |
| python [beam_0000] (PID 68224) vms_mb | MB | 7 | 40.680 | 23.266 | 52.238 | 52.238 | n/a | n/a |
| docker (PID 68226) rss_mb | MB | 1 | 25.688 | 25.688 | 25.688 | 25.688 | n/a | n/a |
| docker (PID 68226) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 68234) rss_mb | MB | 1 | 26.027 | 26.027 | 26.027 | 26.027 | n/a | n/a |
| docker (PID 68234) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 68293) rss_mb | MB | 1 | 25.676 | 25.676 | 25.676 | 25.676 | n/a | n/a |
| docker (PID 68293) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 68334) CPU | percent | 3 | 6.467 | 0.000 | 19.402 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [beam_0000] (PID 68334) rss_mb | MB | 4 | 3.079 | 0.633 | 10.418 | 0.633 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 68334) vms_mb | MB | 4 | 393.215 | 1.055 | 1569.695 | 1.055 | n/a | n/a |
| tail [beam_0000] (PID 68346) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beam_0000] (PID 68346) rss_mb | MB | 3 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [beam_0000] (PID 68346) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 68357) rss_mb | MB | 1 | 13.031 | 13.031 | 13.031 | 13.031 | n/a | n/a |
| docker (PID 68357) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 68384) rss_mb | MB | 1 | 27.086 | 27.086 | 27.086 | 27.086 | n/a | n/a |
| docker (PID 68384) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 68404) rss_mb | MB | 1 | 11.344 | 11.344 | 11.344 | 11.344 | n/a | n/a |
| runc:[2:INIT] [beam_0000] (PID 68404) vms_mb | MB | 1 | 1570.098 | 1570.098 | 1570.098 | 1570.098 | n/a | n/a |
| docker (PID 68419) rss_mb | MB | 1 | 27.570 | 27.570 | 27.570 | 27.570 | n/a | n/a |
| docker (PID 68419) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| sh [beam_0000] (PID 68439) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sh [beam_0000] (PID 68439) vms_mb | MB | 1 | 0.516 | 0.516 | 0.516 | 0.516 | n/a | n/a |
| docker (PID 68455) rss_mb | MB | 1 | 26.070 | 26.070 | 26.070 | 26.070 | n/a | n/a |
| docker (PID 68455) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 68533) rss_mb | MB | 1 | 9.402 | 9.402 | 9.402 | 9.402 | n/a | n/a |
| docker (PID 68533) vms_mb | MB | 1 | 1235.438 | 1235.438 | 1235.438 | 1235.438 | n/a | n/a |
| docker (PID 68541) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 68541) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 68541) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 68541) rss_mb | MB | 39 | 25.844 | 25.844 | 25.844 | 25.844 | n/a | n/a |
| docker (PID 68541) vms_mb | MB | 39 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 68557) rss_mb | MB | 1 | 25.520 | 25.520 | 25.520 | 25.520 | n/a | n/a |
| docker (PID 68557) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 68581) rss_mb | MB | 1 | 25.215 | 25.215 | 25.215 | 25.215 | n/a | n/a |
| docker (PID 68581) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| python3 (PID 68589) CPU | percent | 2 | 98.693 | 98.526 | 98.860 | 98.860 | 0.200000 CPU seconds | n/a |
| python3 (PID 68589) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 68589) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 68589) rss_mb | MB | 3 | 26.586 | 18.566 | 33.609 | 33.609 | n/a | n/a |
| python3 (PID 68589) vms_mb | MB | 3 | 49.964 | 42.570 | 56.379 | 56.379 | n/a | n/a |
| docker (PID 68594) rss_mb | MB | 1 | 25.246 | 25.246 | 25.246 | 25.246 | n/a | n/a |
| docker (PID 68594) vms_mb | MB | 1 | 1587.957 | 1587.957 | 1587.957 | 1587.957 | n/a | n/a |
| docker (PID 68618) rss_mb | MB | 1 | 17.910 | 17.910 | 17.910 | 17.910 | n/a | n/a |
| docker (PID 68618) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 68640) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 68640) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 68640) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 68640) rss_mb | MB | 2 | 27.230 | 26.992 | 27.469 | 27.469 | n/a | n/a |
| docker (PID 68640) vms_mb | MB | 2 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[0:PARENT] (PID 68678) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[0:PARENT] (PID 68678) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker-init [bear_0000] (PID 68681) CPU | percent | 4 | 4.798 | 0.000 | 19.190 | 0.000 | 0.020000 CPU seconds | n/a |
| docker-init [bear_0000] (PID 68681) rss_mb | MB | 5 | 1.380 | 0.633 | 4.367 | 0.633 | n/a | n/a |
| docker-init [bear_0000] (PID 68681) vms_mb | MB | 5 | 300.282 | 1.055 | 1497.191 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 68694) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 68694) rss_mb | MB | 4 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [bear_0000] (PID 68694) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 68696) rss_mb | MB | 1 | 26.902 | 26.902 | 26.902 | 26.902 | n/a | n/a |
| docker (PID 68696) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 68734) rss_mb | MB | 1 | 27.430 | 27.430 | 27.430 | 27.430 | n/a | n/a |
| docker (PID 68734) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 68755) rss_mb | MB | 1 | 11.133 | 11.133 | 11.133 | 11.133 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 68755) vms_mb | MB | 1 | 1641.836 | 1641.836 | 1641.836 | 1641.836 | n/a | n/a |
| docker (PID 68791) rss_mb | MB | 1 | 20.199 | 20.199 | 20.199 | 20.199 | n/a | n/a |
| docker (PID 68791) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 68837) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 68837) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 68837) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 68837) rss_mb | MB | 2 | 20.869 | 15.992 | 25.746 | 25.746 | n/a | n/a |
| docker (PID 68837) vms_mb | MB | 2 | 1588.080 | 1515.949 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 68896) rss_mb | MB | 1 | 25.613 | 25.613 | 25.613 | 25.613 | n/a | n/a |
| docker (PID 68896) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bear_0000] (PID 68937) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bear_0000] (PID 68937) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bear_0000] (PID 68937) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 68950) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 68950) rss_mb | MB | 3 | 1.805 | 1.805 | 1.805 | 1.805 | n/a | n/a |
| tail [bear_0000] (PID 68950) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 68952) rss_mb | MB | 1 | 5.594 | 5.594 | 5.594 | 5.594 | n/a | n/a |
| docker (PID 68952) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 68988) rss_mb | MB | 1 | 26.637 | 26.637 | 26.637 | 26.637 | n/a | n/a |
| docker (PID 68988) vms_mb | MB | 1 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 69024) rss_mb | MB | 1 | 26.961 | 26.961 | 26.961 | 26.961 | n/a | n/a |
| docker (PID 69024) vms_mb | MB | 1 | 1732.777 | 1732.777 | 1732.777 | 1732.777 | n/a | n/a |
| docker (PID 69061) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 69061) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 69061) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 69061) rss_mb | MB | 2 | 26.879 | 26.879 | 26.879 | 26.879 | n/a | n/a |
| docker (PID 69061) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 69120) rss_mb | MB | 1 | 25.746 | 25.746 | 25.746 | 25.746 | n/a | n/a |
| docker (PID 69120) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 69159) CPU | percent | 2 | 9.805 | 0.000 | 19.610 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 69159) rss_mb | MB | 3 | 2.681 | 0.633 | 6.777 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 69159) vms_mb | MB | 3 | 523.852 | 1.055 | 1569.445 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 69173) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 69173) rss_mb | MB | 2 | 1.773 | 1.773 | 1.773 | 1.773 | n/a | n/a |
| tail [bear_0000] (PID 69173) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 69183) rss_mb | MB | 1 | 20.109 | 20.109 | 20.109 | 20.109 | n/a | n/a |
| docker (PID 69183) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 69210) rss_mb | MB | 1 | 27.285 | 27.285 | 27.285 | 27.285 | n/a | n/a |
| docker (PID 69210) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 69230) rss_mb | MB | 1 | 10.555 | 10.555 | 10.555 | 10.555 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 69230) vms_mb | MB | 1 | 1569.453 | 1569.453 | 1569.453 | 1569.453 | n/a | n/a |
| docker (PID 69253) rss_mb | MB | 1 | 25.785 | 25.785 | 25.785 | 25.785 | n/a | n/a |
| docker (PID 69253) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 69293) rss_mb | MB | 1 | 23.070 | 23.070 | 23.070 | 23.070 | n/a | n/a |
| docker (PID 69293) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 69310) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 69310) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 69310) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 69310) rss_mb | MB | 2 | 25.793 | 25.793 | 25.793 | 25.793 | n/a | n/a |
| docker (PID 69310) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bear_0000] (PID 69352) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bear_0000] (PID 69352) rss_mb | MB | 3 | 0.422 | 0.000 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bear_0000] (PID 69352) vms_mb | MB | 3 | 1.010 | 0.922 | 1.055 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 69365) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 69365) rss_mb | MB | 2 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [bear_0000] (PID 69365) vms_mb | MB | 2 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 69446) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 69446) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 69446) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 69446) rss_mb | MB | 2 | 17.719 | 8.715 | 26.723 | 26.723 | n/a | n/a |
| docker (PID 69446) vms_mb | MB | 2 | 1444.104 | 1227.434 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 69505) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 69505) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 69505) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 69505) rss_mb | MB | 2 | 27.336 | 27.336 | 27.336 | 27.336 | n/a | n/a |
| docker (PID 69505) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 69544) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 69544) rss_mb | MB | 4 | 3.659 | 0.633 | 12.738 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 69544) vms_mb | MB | 4 | 393.348 | 1.055 | 1570.227 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 69556) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 69556) rss_mb | MB | 3 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| tail [bear_0000] (PID 69556) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 69568) rss_mb | MB | 1 | 27.555 | 27.555 | 27.555 | 27.555 | n/a | n/a |
| docker (PID 69568) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 69587) rss_mb | MB | 1 | 11.809 | 11.809 | 11.809 | 11.809 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 69587) vms_mb | MB | 1 | 1570.477 | 1570.477 | 1570.477 | 1570.477 | n/a | n/a |
| docker (PID 69629) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 69629) vms_mb | MB | 1 | 30.535 | 30.535 | 30.535 | 30.535 | n/a | n/a |
| docker (PID 69666) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 69666) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 69666) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 69666) rss_mb | MB | 2 | 25.820 | 25.820 | 25.820 | 25.820 | n/a | n/a |
| docker (PID 69666) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 69748) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 69748) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 69748) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 69748) rss_mb | MB | 38 | 26.660 | 26.660 | 26.660 | 26.660 | n/a | n/a |
| docker (PID 69748) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 69792) rss_mb | MB | 1 | 26.633 | 26.633 | 26.633 | 26.633 | n/a | n/a |
| docker (PID 69792) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [bear_0000] (PID 69833) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bear_0000] (PID 69833) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bear_0000] (PID 69833) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 69845) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 69845) rss_mb | MB | 3 | 1.734 | 1.734 | 1.734 | 1.734 | n/a | n/a |
| tail [bear_0000] (PID 69845) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 69848) rss_mb | MB | 1 | 4.473 | 4.473 | 4.473 | 4.473 | n/a | n/a |
| docker (PID 69848) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 69883) rss_mb | MB | 1 | 26.680 | 26.680 | 26.680 | 26.680 | n/a | n/a |
| docker (PID 69883) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 69921) rss_mb | MB | 1 | 27.402 | 27.402 | 27.402 | 27.402 | n/a | n/a |
| docker (PID 69921) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 69940) rss_mb | MB | 1 | 2.590 | 2.590 | 2.590 | 2.590 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 69940) vms_mb | MB | 1 | 1111.484 | 1111.484 | 1111.484 | 1111.484 | n/a | n/a |
| docker (PID 69958) rss_mb | MB | 1 | 26.008 | 26.008 | 26.008 | 26.008 | n/a | n/a |
| docker (PID 69958) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 70001) rss_mb | MB | 1 | 23.438 | 23.438 | 23.438 | 23.438 | n/a | n/a |
| docker (PID 70001) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 70010) rss_mb | MB | 1 | 23.070 | 23.070 | 23.070 | 23.070 | n/a | n/a |
| docker (PID 70010) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 70019) rss_mb | MB | 1 | 26.746 | 26.746 | 26.746 | 26.746 | n/a | n/a |
| docker (PID 70019) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 70058) CPU | percent | 10 | 1.950 | 0.000 | 19.496 | 0.000 | 0.020000 CPU seconds | n/a |
| runc:[2:INIT] [bear_0000] (PID 70058) rss_mb | MB | 11 | 1.678 | 0.633 | 12.125 | 0.633 | n/a | n/a |
| runc:[2:INIT] [bear_0000] (PID 70058) vms_mb | MB | 11 | 143.706 | 1.055 | 1570.219 | 1.055 | n/a | n/a |
| tail [bear_0000] (PID 70071) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bear_0000] (PID 70071) rss_mb | MB | 10 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [bear_0000] (PID 70071) vms_mb | MB | 10 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 70081) rss_mb | MB | 1 | 27.254 | 27.254 | 27.254 | 27.254 | n/a | n/a |
| docker (PID 70081) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 70108) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 70108) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 70108) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 70108) rss_mb | MB | 8 | 27.461 | 27.461 | 27.461 | 27.461 | n/a | n/a |
| docker (PID 70108) vms_mb | MB | 8 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [bear_0000] (PID 70127) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bear_0000] (PID 70127) rss_mb | MB | 8 | 3.391 | 3.391 | 3.391 | 3.391 | n/a | n/a |
| bash [bear_0000] (PID 70127) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bear_0000] (PID 70135) CPU | percent | 7 | 99.325 | 97.159 | 107.872 | 98.037 | 0.710000 CPU seconds | n/a |
| python [bear_0000] (PID 70135) rss_mb | MB | 8 | 29.737 | 5.375 | 41.742 | 41.742 | n/a | n/a |
| python [bear_0000] (PID 70135) vms_mb | MB | 8 | 37.483 | 11.664 | 51.340 | 51.340 | n/a | n/a |
| docker (PID 70137) rss_mb | MB | 1 | 20.375 | 20.375 | 20.375 | 20.375 | n/a | n/a |
| docker (PID 70137) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 70146) rss_mb | MB | 1 | 25.914 | 25.914 | 25.914 | 25.914 | n/a | n/a |
| docker (PID 70146) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 70197) rss_mb | MB | 1 | 9.242 | 9.242 | 9.242 | 9.242 | n/a | n/a |
| docker (PID 70197) vms_mb | MB | 1 | 1443.695 | 1443.695 | 1443.695 | 1443.695 | n/a | n/a |
| docker (PID 70222) rss_mb | MB | 1 | 25.336 | 25.336 | 25.336 | 25.336 | n/a | n/a |
| docker (PID 70222) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 70232) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 70232) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 70232) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 70232) rss_mb | MB | 38 | 26.539 | 26.539 | 26.539 | 26.539 | n/a | n/a |
| docker (PID 70232) vms_mb | MB | 38 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 70248) rss_mb | MB | 1 | 20.500 | 20.500 | 20.500 | 20.500 | n/a | n/a |
| docker (PID 70248) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 70272) rss_mb | MB | 1 | 1.824 | 1.824 | 1.824 | 1.824 | n/a | n/a |
| docker (PID 70272) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| python3 (PID 70280) CPU | percent | 3 | 98.754 | 98.460 | 98.914 | 98.888 | 0.300000 CPU seconds | n/a |
| python3 (PID 70280) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 70280) io write MB/s | MB/s | 3 | 0.708 | 0.000 | 2.125 | 2.125 | 0.214844 MB | n/a |
| python3 (PID 70280) rss_mb | MB | 4 | 28.187 | 17.625 | 34.625 | 34.625 | n/a | n/a |
| python3 (PID 70280) vms_mb | MB | 4 | 51.798 | 42.434 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 70294) rss_mb | MB | 1 | 16.570 | 16.570 | 16.570 | 16.570 | n/a | n/a |
| docker (PID 70294) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 70332) CPU | percent | 1 | 9.844 | 9.844 | 9.844 | 9.844 | 0.010000 CPU seconds | n/a |
| docker (PID 70332) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 70332) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 70332) rss_mb | MB | 2 | 27.057 | 26.859 | 27.254 | 27.254 | n/a | n/a |
| docker (PID 70332) vms_mb | MB | 2 | 1768.779 | 1732.777 | 1804.781 | 1804.781 | n/a | n/a |
| runc:[0:PARENT] (PID 70372) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[0:PARENT] (PID 70372) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker-init [beef_0000] (PID 70375) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beef_0000] (PID 70375) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [beef_0000] (PID 70375) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 70389) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 70389) rss_mb | MB | 4 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| tail [beef_0000] (PID 70389) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 70391) rss_mb | MB | 1 | 27.230 | 27.230 | 27.230 | 27.230 | n/a | n/a |
| docker (PID 70391) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 70427) rss_mb | MB | 1 | 27.328 | 27.328 | 27.328 | 27.328 | n/a | n/a |
| docker (PID 70427) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 70445) rss_mb | MB | 1 | 12.004 | 12.004 | 12.004 | 12.004 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 70445) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 70481) rss_mb | MB | 1 | 25.770 | 25.770 | 25.770 | 25.770 | n/a | n/a |
| docker (PID 70481) vms_mb | MB | 1 | 1660.273 | 1660.273 | 1660.273 | 1660.273 | n/a | n/a |
| docker (PID 70525) CPU | percent | 1 | 9.770 | 9.770 | 9.770 | 9.770 | 0.010000 CPU seconds | n/a |
| docker (PID 70525) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 70525) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 70525) rss_mb | MB | 2 | 25.000 | 22.996 | 27.004 | 27.004 | n/a | n/a |
| docker (PID 70525) vms_mb | MB | 2 | 1624.488 | 1588.203 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 70585) rss_mb | MB | 1 | 25.688 | 25.688 | 25.688 | 25.688 | n/a | n/a |
| docker (PID 70585) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [beef_0000] (PID 70623) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beef_0000] (PID 70623) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [beef_0000] (PID 70623) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 70636) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 70636) rss_mb | MB | 3 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [beef_0000] (PID 70636) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 70638) rss_mb | MB | 1 | 1.633 | 1.633 | 1.633 | 1.633 | n/a | n/a |
| docker (PID 70638) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 70673) rss_mb | MB | 1 | 26.676 | 26.676 | 26.676 | 26.676 | n/a | n/a |
| docker (PID 70673) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 70710) rss_mb | MB | 1 | 27.133 | 27.133 | 27.133 | 27.133 | n/a | n/a |
| docker (PID 70710) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| docker (PID 70745) rss_mb | MB | 1 | 25.738 | 25.738 | 25.738 | 25.738 | n/a | n/a |
| docker (PID 70745) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 70787) rss_mb | MB | 1 | 17.184 | 17.184 | 17.184 | 17.184 | n/a | n/a |
| docker (PID 70787) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 70813) rss_mb | MB | 1 | 18.109 | 18.109 | 18.109 | 18.109 | n/a | n/a |
| docker (PID 70813) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 70828) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 70828) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 70828) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 70828) rss_mb | MB | 38 | 25.219 | 25.219 | 25.219 | 25.219 | n/a | n/a |
| docker (PID 70828) vms_mb | MB | 38 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 70870) rss_mb | MB | 1 | 26.785 | 26.785 | 26.785 | 26.785 | n/a | n/a |
| docker (PID 70870) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [beef_0000] (PID 70909) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beef_0000] (PID 70909) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [beef_0000] (PID 70909) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 70924) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 70924) rss_mb | MB | 3 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| tail [beef_0000] (PID 70924) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 70926) rss_mb | MB | 1 | 13.098 | 13.098 | 13.098 | 13.098 | n/a | n/a |
| docker (PID 70926) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 70963) rss_mb | MB | 1 | 27.082 | 27.082 | 27.082 | 27.082 | n/a | n/a |
| docker (PID 70963) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 71000) rss_mb | MB | 1 | 26.973 | 26.973 | 26.973 | 26.973 | n/a | n/a |
| docker (PID 71000) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 71021) rss_mb | MB | 1 | 10.898 | 10.898 | 10.898 | 10.898 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 71021) vms_mb | MB | 1 | 1569.703 | 1569.703 | 1569.703 | 1569.703 | n/a | n/a |
| docker (PID 71039) rss_mb | MB | 1 | 27.055 | 27.055 | 27.055 | 27.055 | n/a | n/a |
| docker (PID 71039) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 71081) rss_mb | MB | 1 | 9.766 | 9.766 | 9.766 | 9.766 | n/a | n/a |
| docker (PID 71081) vms_mb | MB | 1 | 1387.949 | 1387.949 | 1387.949 | 1387.949 | n/a | n/a |
| docker (PID 71098) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 71098) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 71098) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 71098) rss_mb | MB | 2 | 26.723 | 26.723 | 26.723 | 26.723 | n/a | n/a |
| docker (PID 71098) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 71138) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| runc:[2:INIT] [beef_0000] (PID 71138) rss_mb | MB | 10 | 1.820 | 0.566 | 13.105 | 0.566 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 71138) vms_mb | MB | 10 | 158.022 | 1.055 | 1570.727 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 71149) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 71149) rss_mb | MB | 9 | 1.789 | 1.789 | 1.789 | 1.789 | n/a | n/a |
| tail [beef_0000] (PID 71149) vms_mb | MB | 9 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 71159) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 71159) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 71189) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 71189) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 71189) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 71189) rss_mb | MB | 8 | 27.398 | 27.398 | 27.398 | 27.398 | n/a | n/a |
| docker (PID 71189) vms_mb | MB | 8 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| bash [beef_0000] (PID 71209) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [beef_0000] (PID 71209) rss_mb | MB | 8 | 3.395 | 3.395 | 3.395 | 3.395 | n/a | n/a |
| bash [beef_0000] (PID 71209) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [beef_0000] (PID 71219) CPU | percent | 7 | 100.653 | 88.169 | 107.873 | 107.789 | 0.720000 CPU seconds | n/a |
| python [beef_0000] (PID 71219) rss_mb | MB | 8 | 31.119 | 11.430 | 42.578 | 42.578 | n/a | n/a |
| python [beef_0000] (PID 71219) vms_mb | MB | 8 | 38.135 | 15.047 | 52.238 | 52.238 | n/a | n/a |
| docker (PID 71229) rss_mb | MB | 1 | 26.047 | 26.047 | 26.047 | 26.047 | n/a | n/a |
| docker (PID 71229) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 71288) rss_mb | MB | 1 | 26.652 | 26.652 | 26.652 | 26.652 | n/a | n/a |
| docker (PID 71288) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [beef_0000] (PID 71326) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [beef_0000] (PID 71326) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [beef_0000] (PID 71326) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [beef_0000] (PID 71337) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [beef_0000] (PID 71337) rss_mb | MB | 3 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| tail [beef_0000] (PID 71337) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 71348) rss_mb | MB | 1 | 3.641 | 3.641 | 3.641 | 3.641 | n/a | n/a |
| docker (PID 71348) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 71375) rss_mb | MB | 1 | 27.117 | 27.117 | 27.117 | 27.117 | n/a | n/a |
| docker (PID 71375) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 71395) rss_mb | MB | 1 | 10.141 | 10.141 | 10.141 | 10.141 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 71395) vms_mb | MB | 1 | 1569.195 | 1569.195 | 1569.195 | 1569.195 | n/a | n/a |
| docker (PID 71410) rss_mb | MB | 1 | 27.477 | 27.477 | 27.477 | 27.477 | n/a | n/a |
| docker (PID 71410) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 71429) rss_mb | MB | 1 | 11.859 | 11.859 | 11.859 | 11.859 | n/a | n/a |
| runc:[2:INIT] [beef_0000] (PID 71429) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 71446) rss_mb | MB | 1 | 26.082 | 26.082 | 26.082 | 26.082 | n/a | n/a |
| docker (PID 71446) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 71542) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 71542) io read MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 71542) io write MB/s | MB/s | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 71542) rss_mb | MB | 39 | 26.652 | 26.652 | 26.652 | 26.652 | n/a | n/a |
| docker (PID 71542) vms_mb | MB | 39 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 71574) rss_mb | MB | 1 | 22.621 | 22.621 | 22.621 | 22.621 | n/a | n/a |
| docker (PID 71574) vms_mb | MB | 1 | 1660.207 | 1660.207 | 1660.207 | 1660.207 | n/a | n/a |
| python3 (PID 71591) CPU | percent | 3 | 98.748 | 88.607 | 108.777 | 98.861 | 0.300000 CPU seconds | n/a |
| python3 (PID 71591) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 71591) io write MB/s | MB/s | 3 | 0.708 | 0.000 | 2.124 | 2.124 | 0.214844 MB | n/a |
| python3 (PID 71591) rss_mb | MB | 4 | 24.560 | 10.602 | 34.410 | 34.410 | n/a | n/a |
| python3 (PID 71591) vms_mb | MB | 4 | 48.618 | 36.633 | 57.457 | 57.457 | n/a | n/a |
| docker (PID 71596) rss_mb | MB | 1 | 19.641 | 19.641 | 19.641 | 19.641 | n/a | n/a |
| docker (PID 71596) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 71620) rss_mb | MB | 1 | 26.984 | 26.984 | 26.984 | 26.984 | n/a | n/a |
| docker (PID 71620) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 71642) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 71642) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 71642) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 71642) rss_mb | MB | 2 | 27.352 | 27.016 | 27.688 | 27.688 | n/a | n/a |
| docker (PID 71642) vms_mb | MB | 2 | 1697.025 | 1661.023 | 1733.027 | 1733.027 | n/a | n/a |
| runc:[0:PARENT] (PID 71679) rss_mb | MB | 1 | 1.996 | 1.996 | 1.996 | 1.996 | n/a | n/a |
| runc:[0:PARENT] (PID 71679) vms_mb | MB | 1 | 14.109 | 14.109 | 14.109 | 14.109 | n/a | n/a |
| runc:[1:CHILD] (PID 71681) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| runc:[1:CHILD] (PID 71681) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker-init [bell_0000] (PID 71682) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bell_0000] (PID 71682) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bell_0000] (PID 71682) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 71696) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 71696) rss_mb | MB | 4 | 1.703 | 1.703 | 1.703 | 1.703 | n/a | n/a |
| tail [bell_0000] (PID 71696) vms_mb | MB | 4 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 71698) rss_mb | MB | 1 | 27.551 | 27.551 | 27.551 | 27.551 | n/a | n/a |
| docker (PID 71698) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 71733) rss_mb | MB | 1 | 27.203 | 27.203 | 27.203 | 27.203 | n/a | n/a |
| docker (PID 71733) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 71753) rss_mb | MB | 1 | 11.961 | 11.961 | 11.961 | 11.961 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 71753) vms_mb | MB | 1 | 1642.480 | 1642.480 | 1642.480 | 1642.480 | n/a | n/a |
| docker (PID 71788) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 71788) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| docker (PID 71831) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 71831) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 71831) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 71831) rss_mb | MB | 2 | 25.797 | 25.797 | 25.797 | 25.797 | n/a | n/a |
| docker (PID 71831) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 71891) rss_mb | MB | 1 | 25.699 | 25.699 | 25.699 | 25.699 | n/a | n/a |
| docker (PID 71891) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bell_0000] (PID 71931) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bell_0000] (PID 71931) rss_mb | MB | 3 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bell_0000] (PID 71931) vms_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 71943) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 71943) rss_mb | MB | 3 | 1.641 | 1.641 | 1.641 | 1.641 | n/a | n/a |
| tail [bell_0000] (PID 71943) vms_mb | MB | 3 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 71979) rss_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| docker (PID 71979) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 72000) rss_mb | MB | 1 | 10.547 | 10.547 | 10.547 | 10.547 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 72000) vms_mb | MB | 1 | 1569.453 | 1569.453 | 1569.453 | 1569.453 | n/a | n/a |
| docker (PID 72015) rss_mb | MB | 1 | 27.133 | 27.133 | 27.133 | 27.133 | n/a | n/a |
| docker (PID 72015) vms_mb | MB | 1 | 1661.023 | 1661.023 | 1661.023 | 1661.023 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 72034) rss_mb | MB | 1 | 11.387 | 11.387 | 11.387 | 11.387 | n/a | n/a |
| runc:[2:INIT] [bell_0000] (PID 72034) vms_mb | MB | 1 | 1570.227 | 1570.227 | 1570.227 | 1570.227 | n/a | n/a |
| docker (PID 72050) rss_mb | MB | 1 | 26.883 | 26.883 | 26.883 | 26.883 | n/a | n/a |
| docker (PID 72050) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 72116) rss_mb | MB | 1 | 19.715 | 19.715 | 19.715 | 19.715 | n/a | n/a |
| docker (PID 72116) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 72130) CPU | percent | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 72130) io read MB/s | MB/s | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 72130) io write MB/s | MB/s | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 72130) rss_mb | MB | 48 | 26.746 | 26.746 | 26.746 | 26.746 | n/a | n/a |
| docker (PID 72130) vms_mb | MB | 48 | 1660.523 | 1660.523 | 1660.523 | 1660.523 | n/a | n/a |
| docker (PID 72146) rss_mb | MB | 1 | 27.020 | 27.020 | 27.020 | 27.020 | n/a | n/a |
| docker (PID 72146) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 72174) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 72174) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 72174) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 72174) rss_mb | MB | 2 | 26.707 | 26.707 | 26.707 | 26.707 | n/a | n/a |
| docker (PID 72174) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker-init [bell_0000] (PID 72213) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bell_0000] (PID 72213) rss_mb | MB | 4 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bell_0000] (PID 72213) vms_mb | MB | 4 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 72226) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 72226) rss_mb | MB | 4 | 1.306 | 0.301 | 1.641 | 1.641 | n/a | n/a |
| tail [bell_0000] (PID 72226) vms_mb | MB | 4 | 2.849 | 2.441 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 72265) rss_mb | MB | 1 | 4.094 | 4.094 | 4.094 | 4.094 | n/a | n/a |
| docker (PID 72265) vms_mb | MB | 1 | 32.762 | 32.762 | 32.762 | 32.762 | n/a | n/a |
| docker (PID 72300) rss_mb | MB | 1 | 19.961 | 19.961 | 19.961 | 19.961 | n/a | n/a |
| docker (PID 72300) vms_mb | MB | 1 | 1516.199 | 1516.199 | 1516.199 | 1516.199 | n/a | n/a |
| docker (PID 72337) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 72337) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 72337) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 72337) rss_mb | MB | 2 | 27.070 | 27.070 | 27.070 | 27.070 | n/a | n/a |
| docker (PID 72337) vms_mb | MB | 2 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 72396) rss_mb | MB | 1 | 25.676 | 25.676 | 25.676 | 25.676 | n/a | n/a |
| docker (PID 72396) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker-init [bell_0000] (PID 72435) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker-init [bell_0000] (PID 72435) rss_mb | MB | 11 | 0.633 | 0.633 | 0.633 | 0.633 | n/a | n/a |
| docker-init [bell_0000] (PID 72435) vms_mb | MB | 11 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| tail [bell_0000] (PID 72449) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail [bell_0000] (PID 72449) rss_mb | MB | 11 | 1.738 | 1.738 | 1.738 | 1.738 | n/a | n/a |
| tail [bell_0000] (PID 72449) vms_mb | MB | 11 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| docker (PID 72451) rss_mb | MB | 1 | 23.266 | 23.266 | 23.266 | 23.266 | n/a | n/a |
| docker (PID 72451) vms_mb | MB | 1 | 1587.953 | 1587.953 | 1587.953 | 1587.953 | n/a | n/a |
| docker (PID 72487) CPU | percent | 8 | 1.225 | 0.000 | 9.799 | 9.799 | 0.010000 CPU seconds | n/a |
| docker (PID 72487) io read MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 72487) io write MB/s | MB/s | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 72487) rss_mb | MB | 9 | 26.809 | 26.809 | 26.809 | 26.809 | n/a | n/a |
| docker (PID 72487) vms_mb | MB | 9 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| bash [bell_0000] (PID 72507) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash [bell_0000] (PID 72507) rss_mb | MB | 8 | 3.402 | 3.402 | 3.402 | 3.402 | n/a | n/a |
| bash [bell_0000] (PID 72507) vms_mb | MB | 8 | 4.391 | 4.391 | 4.391 | 4.391 | n/a | n/a |
| python [bell_0000] (PID 72517) CPU | percent | 7 | 100.697 | 88.260 | 107.805 | 107.791 | 0.720000 CPU seconds | n/a |
| python [bell_0000] (PID 72517) rss_mb | MB | 8 | 31.858 | 14.621 | 42.348 | 42.348 | n/a | n/a |
| python [bell_0000] (PID 72517) vms_mb | MB | 8 | 39.046 | 18.395 | 52.238 | 52.238 | n/a | n/a |
| docker (PID 72527) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 72527) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 72527) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 72527) rss_mb | MB | 2 | 25.961 | 25.961 | 25.961 | 25.961 | n/a | n/a |
| docker (PID 72527) vms_mb | MB | 2 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| docker (PID 72597) rss_mb | MB | 1 | 20.172 | 20.172 | 20.172 | 20.172 | n/a | n/a |
| docker (PID 72597) vms_mb | MB | 1 | 1588.203 | 1588.203 | 1588.203 | 1588.203 | n/a | n/a |
| docker (PID 72621) CPU | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker (PID 72621) io read MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 72621) io write MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 72621) rss_mb | MB | 40 | 26.230 | 26.230 | 26.230 | 26.230 | n/a | n/a |
| docker (PID 72621) vms_mb | MB | 40 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| docker (PID 72645) rss_mb | MB | 1 | 14.238 | 14.238 | 14.238 | 14.238 | n/a | n/a |
| docker (PID 72645) vms_mb | MB | 1 | 1515.949 | 1515.949 | 1515.949 | 1515.949 | n/a | n/a |
| docker (PID 72662) rss_mb | MB | 1 | 26.766 | 26.766 | 26.766 | 26.766 | n/a | n/a |
| docker (PID 72662) vms_mb | MB | 1 | 1660.773 | 1660.773 | 1660.773 | 1660.773 | n/a | n/a |
| python3 (PID 72670) CPU | percent | 3 | 98.759 | 88.529 | 108.843 | 98.904 | 0.300000 CPU seconds | n/a |
| python3 (PID 72670) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| python3 (PID 72670) io write MB/s | MB/s | 3 | 0.708 | 0.000 | 2.125 | 2.125 | 0.214844 MB | n/a |
| python3 (PID 72670) rss_mb | MB | 4 | 28.585 | 18.641 | 34.691 | 34.691 | n/a | n/a |
| python3 (PID 72670) vms_mb | MB | 4 | 52.115 | 43.703 | 57.438 | 57.438 | n/a | n/a |
| docker (PID 72672) rss_mb | MB | 1 | 8.832 | 8.832 | 8.832 | 8.832 | n/a | n/a |
| docker (PID 72672) vms_mb | MB | 1 | 1227.434 | 1227.434 | 1227.434 | 1227.434 | n/a | n/a |
| docker (PID 72696) rss_mb | MB | 1 | 25.297 | 25.297 | 25.297 | 25.297 | n/a | n/a |
| docker (PID 72696) vms_mb | MB | 1 | 1660.211 | 1660.211 | 1660.211 | 1660.211 | n/a | n/a |
| sandbox alex_0000 CPU | percent | 27 | 54.077 | 11.664 | 101.244 | 31.257 | 1.491648 CPU seconds | n/a |
| sandbox alex_0000 io read MB/s | MB/s | 33 | 0.002 | 0.000 | 0.076 | 0.000 | 0.007812 MB | n/a |
| sandbox alex_0000 io write MB/s | MB/s | 33 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox alex_0000 memory | MB | 35 | 7.778 | 0.730 | 36.281 | 0.852 | n/a | n/a |
| sandbox alex_0000 net rx MB/s | MB/s | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox alex_0000 net tx MB/s | MB/s | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox andy_0000 CPU | percent | 19 | 61.563 | 29.562 | 100.138 | 32.261 | 1.194276 CPU seconds | n/a |
| sandbox andy_0000 io read MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox andy_0000 io write MB/s | MB/s | 22 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox andy_0000 memory | MB | 24 | 9.818 | 0.711 | 36.270 | 0.863 | n/a | n/a |
| sandbox andy_0000 net rx MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox andy_0000 net tx MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox arch_0000 CPU | percent | 20 | 62.930 | 12.427 | 100.693 | 29.989 | 1.288962 CPU seconds | n/a |
| sandbox arch_0000 io read MB/s | MB/s | 23 | 0.001 | 0.000 | 0.030 | 0.000 | 0.054688 MB | n/a |
| sandbox arch_0000 io write MB/s | MB/s | 23 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox arch_0000 memory | MB | 25 | 10.022 | 0.664 | 35.664 | 0.871 | n/a | n/a |
| sandbox arch_0000 net rx MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox arch_0000 net tx MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bake_0000 CPU | percent | 31 | 51.661 | 0.000 | 100.085 | 0.050 | 1.646833 CPU seconds | n/a |
| sandbox bake_0000 io read MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bake_0000 io write MB/s | MB/s | 35 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bake_0000 memory | MB | 37 | 7.391 | 0.625 | 35.676 | 0.773 | n/a | n/a |
| sandbox bake_0000 net rx MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bake_0000 net tx MB/s | MB/s | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bale_0000 CPU | percent | 46 | 83.815 | 10.191 | 100.172 | 33.132 | 3.935406 CPU seconds | n/a |
| sandbox bale_0000 io read MB/s | MB/s | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bale_0000 io write MB/s | MB/s | 49 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bale_0000 memory | MB | 51 | 22.370 | 0.691 | 35.254 | 0.809 | n/a | n/a |
| sandbox bale_0000 net rx MB/s | MB/s | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bale_0000 net tx MB/s | MB/s | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox band_0000 CPU | percent | 19 | 62.693 | 15.643 | 100.438 | 47.192 | 1.219662 CPU seconds | n/a |
| sandbox band_0000 io read MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox band_0000 io write MB/s | MB/s | 22 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox band_0000 memory | MB | 24 | 9.182 | 0.652 | 35.312 | 4.027 | n/a | n/a |
| sandbox band_0000 net rx MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox band_0000 net tx MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bart_0000 CPU | percent | 26 | 53.847 | 15.394 | 100.166 | 32.535 | 1.433906 CPU seconds | n/a |
| sandbox bart_0000 io read MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bart_0000 io write MB/s | MB/s | 32 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bart_0000 memory | MB | 34 | 7.764 | 0.633 | 34.484 | 0.977 | n/a | n/a |
| sandbox bart_0000 net rx MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bart_0000 net tx MB/s | MB/s | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox base_0000 CPU | percent | 34 | 60.333 | 3.282 | 101.044 | 46.901 | 2.103325 CPU seconds | n/a |
| sandbox base_0000 io read MB/s | MB/s | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox base_0000 io write MB/s | MB/s | 38 | 0.002 | 0.000 | 0.038 | 0.000 | 0.007812 MB | n/a |
| sandbox base_0000 memory | MB | 41 | 9.290 | 0.734 | 35.328 | 4.371 | n/a | n/a |
| sandbox base_0000 net rx MB/s | MB/s | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox base_0000 net tx MB/s | MB/s | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beam_0000 CPU | percent | 20 | 61.950 | 18.361 | 100.148 | 44.657 | 1.273688 CPU seconds | n/a |
| sandbox beam_0000 io read MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beam_0000 io write MB/s | MB/s | 23 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox beam_0000 memory | MB | 25 | 9.229 | 0.703 | 36.219 | 1.254 | n/a | n/a |
| sandbox beam_0000 net rx MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beam_0000 net tx MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bear_0000 CPU | percent | 23 | 56.973 | 18.220 | 100.130 | 83.742 | 1.342267 CPU seconds | n/a |
| sandbox bear_0000 io read MB/s | MB/s | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bear_0000 io write MB/s | MB/s | 29 | 0.001 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bear_0000 memory | MB | 30 | 7.760 | 0.676 | 35.344 | 3.789 | n/a | n/a |
| sandbox bear_0000 net rx MB/s | MB/s | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bear_0000 net tx MB/s | MB/s | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beef_0000 CPU | percent | 17 | 64.413 | 30.336 | 100.067 | 47.750 | 1.123332 CPU seconds | n/a |
| sandbox beef_0000 io read MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beef_0000 io write MB/s | MB/s | 20 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox beef_0000 memory | MB | 22 | 10.536 | 0.758 | 36.324 | 4.414 | n/a | n/a |
| sandbox beef_0000 net rx MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox beef_0000 net tx MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bell_0000 CPU | percent | 18 | 65.098 | 30.819 | 100.065 | 44.465 | 1.199199 CPU seconds | n/a |
| sandbox bell_0000 io read MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bell_0000 io write MB/s | MB/s | 21 | 0.002 | 0.000 | 0.038 | 0.000 | 0.003906 MB | n/a |
| sandbox bell_0000 memory | MB | 22 | 10.635 | 0.000 | 36.465 | 3.781 | n/a | n/a |
| sandbox bell_0000 net rx MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox bell_0000 net tx MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| workload total CPU | percent | 6981 | 15.522 | 0.566 | 110.100 | 76.941 | 110.458827 CPU seconds | n/a |
| workload total io read MB/s | MB/s | 415 | 0.008 | 0.000 | 1.385 | 0.000 | 0.390625 MB | n/a |
| workload total io write MB/s | MB/s | 409 | 0.001 | 0.000 | 0.038 | 0.000 | 0.050781 MB | n/a |
| workload total memory | MB | 6982 | 472.177 | 359.230 | 530.016 | 492.801 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
