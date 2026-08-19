# RTX 5090 serving stacks

A tokens-per-second number is only meaningful with the serving stack attached to it. These cells are not averaged together.

| Stack | Realized ISL | Realized OSL | True decode tok/s | TTFT | Correctness |
|---|---:|---:|---:|---:|---|
| SGLang NONE | ~1,049 | 1,024 | ~71.8 | — | PASS |
| DSPARK | ~1,038 | 1,024 | 81.74 | 0.124 s | PASS |
| Mia stock TQ4 KV + MTP3 | — | — | **not published** | — | **HOLD_CORRECTNESS** |
| Mia patched #40914, TQ4 KV + MTP3 | 1,056 | 1,024 | **151.27** | 0.920 s | **PASS** |

For the patched Mia C1 cell: E2E 7.69 s, 28,918 MiB GPU memory, ~351.5 W, 50°C, MTP accepted **830/834 = 99.52%**. The ~160 tok/s target was **not** reproduced; the public number is 151.27.

The stock accelerated stack is retained as an important negative result: TQ4 KV and MTP3 were active and decimal `9.9` happened to pass, but exact output, JSON, tools, coding and multi-turn canaries were garbled. Performance was therefore not chased. Patch #40914 lifted the frozen canaries and produced the valid 151.27 tok/s cell.

DSPARK seal: `ca5dc168a9faaa1d364b28b85726090159c3994f`; patched Mia seal: `5e9aa4ebcf149bd4b9a303fbdc02c48386cc8320`.
