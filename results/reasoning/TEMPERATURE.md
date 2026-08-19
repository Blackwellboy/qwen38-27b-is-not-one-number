# Temperature / sampling

Thinking-off primary sweep, 36 generations per temperature:

| Temperature | Pass | Mean unique answers / prompt |
|---:|---:|---:|
| 0.0 | 36/36 | 1.00 |
| 0.2 | 36/36 | 1.08 |
| 0.4 | 36/36 | 1.17 |
| 0.6 | 36/36 | 1.25 |
| 0.8 | 35/36 | 1.33 |

The official instruct-style cell tested (T=0.7, top_p=0.80, presence_penalty=1.5) was also 36/36.

**Bounded conclusion:** lower temperature mainly reduced variance/lock-in on this pack. This is not evidence that temperature 0 universally makes the model smarter.

Evidence seal: `0bb7426c280a911dc5422a2a4dda8c70f9763c20`.
