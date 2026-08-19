# RTX 5090 — llama.cpp Q4_K_M

Model source: `unsloth/Qwen3.8-27B-GGUF` revision `430473d9d0e975450ce1f445642b6527cb4faea1`; runtime llama.cpp rev 9402 (`19e92c33e`), full GPU offload. Load time was about 4.3 s. Exact `BLACKWELL38_READY` and decimal `9.9` canaries passed.

| Workload | Decode tok/s |
|---|---:|
| short | 79.45 |
| ~1K | 73.66 |
| ~8K | 71.76 |
| ~32K | 64.09 |

Stability: 2-hour mixed soak **6,992/6,992**; 8-hour soak **27,404 requests, zero failed**. Functional context was separately sealed at 64K and 128K; no 261K llama.cpp claim is made.

Initial qualification seal: `2755a446ee4c184b8138031aaff622e50dd22e02`.
