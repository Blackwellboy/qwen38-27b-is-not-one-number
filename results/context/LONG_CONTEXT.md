# Long context: configured is not realized

The model's advertised/configured context and a deployment's usable context are different claims.

One official SGLang NONE RTX 5090 profile was configured for 262,144 tokens but reported only **42,624 realized KV tokens**. Native ~261K on that profile is therefore `HOLD_REALIZED_KV_CAPACITY`, not a pass. A bounded ~12.7K three-needle retrieval test passed.

A separate long-context SGLang deployment, using FP8 KV and no speculative decoder, produced 3/3 needle retrieval through near-native context:

| Actual input length | Decode tok/s |
|---:|---:|
| 32,780 | 76.85 |
| 131,084 | 66.86 |
| 240,012 | 59.16 |
| 256,012 | 57.57 |
| 261,212 | 57.52 |

At ~261K, TTFT was about **121.4 s**.

The llama.cpp Q4_K_M path is a separate claim: it was functionally sealed at 64K and 128K in this campaign, **not at 261K**.
