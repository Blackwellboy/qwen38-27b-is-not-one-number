# Reproducibility notes

This public release intentionally exports **protocol identities and machine-readable results**, not the private fleet-control scripts used to schedule hardware. Reproduction should be built from the upstream benchmark/runtime pins listed in each result file.

For matched quality, use lm-eval 0.4.12 with the recorded GSM8K and IFEval dataset revisions, explicit THINKING_OFF, and the exact model revisions in `results/quantization/gsm8k_ifeval.json`.

For reasoning studies, keep prompts, sampling, max-token budgets and mode semantics fixed. In particular, do not reinterpret MEDIUM as a dedicated intermediate instruction on the pinned template.

For serving measurements, validate exact/decimal/JSON/tools/coding canaries before publishing throughput. Record actual prompt/completion token counts and use token-emission timestamps where available rather than treating transport chunks as tokens.

The private lab notebook contains additional host-specific orchestration and recovery material, but none of it is required to interpret the public claims.
