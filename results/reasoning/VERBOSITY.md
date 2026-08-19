# Easy-task overthinking and latency

A 466-request bounded study found that simple tasks can become dramatically more expensive when thinking is enabled. On the tested stack, DEFAULT/unset behaved as XHIGH (36/36 primary outputs identical).

| Mode | p50 latency | Approx. reasoning/final token ratio |
|---|---:|---:|
| OFF | **0.93 s** | 0× |
| LOW | 8.35 s | ~33× |
| DEFAULT/unset | 8.51 s | ~33× |
| XHIGH | 8.49 s | ~33× |

Thinking-off showed no reasoning leakage in the tested cells. `preserve_thinking` defaulted on; explicitly disabling it substantially reduced multi-turn prompt replay. Lowering `max_tokens` alone was not a good verbosity fix because it increased mid-reasoning truncation.

Evidence seal: `5c158ebeef7577605589934f3e8b1243f35e8dbb`.
