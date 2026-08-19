# Methodology

## Core rule

A result is publishable only when the requested protocol, model/runtime identity, correctness gates and completion criteria are all satisfied. HTTP 200, process exit, elapsed time, a progress counter or an attractive tokens-per-second value is not enough.

## Measurement rules

- Preserve model revision, quantization, runtime/build, context settings, reasoning mode and benchmark/harness revision.
- Record requested and realized input/output token counts separately.
- Keep cold, warm and post-idle measurements distinct.
- Do not assume an SSE chunk is a token.
- Speculative decoding claims require proof that speculation is active; acceptance is reported only when exposed and measured.
- A backend flag is not proof of an effective backend.
- Partial benchmark outputs are never manually stitched into a new run.
- Protocol mismatch becomes `HOLD`, not a substituted benchmark.
- Correctness canaries run before throughput claims on accelerated stacks.

## Result classes

See [`STATUS_VOCABULARY.md`](STATUS_VOCABULARY.md).
