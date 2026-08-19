# Output-budget starvation — shader/code study

At `max_tokens=2048` across 240 generations:

| Recipe | Mode | Pass | Truncated | Mean reasoning tokens | Mean code tokens |
|---|---|---:|---:|---:|---:|
| HF | LOW | 70.0% | 21.7% | 646 | 90 |
| HF | XHIGH | 48.3% | 50.0% | 1,274 | 38 |
| Control | LOW | 73.3% | 20.0% | 661 | 98 |
| Control | XHIGH | 50.0% | 43.3% | 1,233 | 46 |

The failure mechanism is important: in many XHIGH cases, extra reasoning consumed the shared completion budget before enough final code could be emitted. At a deliberately tiny 64-token ceiling, LOW and XHIGH each truncated about 77.8% of the time.

This supports **budget-starvation** as a deployment explanation; it does not support the universal claim that more reasoning is intrinsically worse.
