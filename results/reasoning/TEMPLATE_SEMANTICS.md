# Open-template reasoning semantics

Scope: the pinned open Qwen3.8-27B template at official model revision `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`. Provider-hosted APIs may map labels differently.

- Unset reasoning effort rendered equivalently to explicit **XHIGH** on the pin.
- LOW and XHIGH have dedicated instruction branches.
- MEDIUM is accepted and keeps thinking enabled, but has **no dedicated MEDIUM effort instruction**. It is therefore more precise to call it “thinking on without the LOW restraint or XHIGH nudge” than to call it fake.
- Invalid `high` fails loudly on this template.
- `preserve_thinking` defaults on.
- `enable_thinking=false` was clean in the tested cells: no reasoning leakage.

Replay-cost examples:

| Prior reasoning | Preserve on | `preserve_thinking=false` |
|---|---:|---:|
| ~4k characters | 1,973 next-prompt tokens | 55 |
| ~50k characters | 23,654 | 55 |

Evidence seals: `a801ae61bfa2a9006af5eeba488c6ddeb4aacf8c`, official re-audit `0f13cac639bbadc2be617551f3ad78b3a801722f`.
