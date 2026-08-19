# Hard-reasoning effort pack

Same model/deployment/prompts, `max_tokens=4096`; only reasoning mode changed.

| Mode | Score | Truncations |
|---|---:|---:|
| OFF | 68% | 1 |
| LOW | **94%** | **0** |
| XHIGH | 88% | 5 |

Among the 45 XHIGH tasks that actually finished, 44 were correct (97.8%). Paired comparison: XHIGH-only wins 0, LOW-only wins 3; McNemar `p=0.25`. Five XHIGH misses were retried with a 7,000-token ceiling: two recovered after consuming 5,150 and 5,958 reasoning tokens, two stayed wrong, and one still truncated.

**Interpretation:** LOW was the better operating point under this fixed budget. This is not evidence that LOW is inherently more intelligent. XHIGH was frequently colliding with the output ceiling.

Evidence seal: `e5fd10282bd758e0d65b836a8c1b4b39a609b463`.
