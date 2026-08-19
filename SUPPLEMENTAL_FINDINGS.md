# Supplemental findings after the article draft

The main article is a timestamped narrative of the sealed campaign state when it was written. Results that landed later are added here instead of silently rewriting the original argument.

## ProgramBench reasoning-mode A/B

A single preregistered ProgramBench task was rerun under OFF/LOW/XHIGH/MEDIUM on frozen Mia #40914. MEDIUM produced the highest coverage (308/502 = 61.35%); LOW was 253/502; OFF_REPEAT 241/502; XHIGH failed the agent loop and scored 0/502. This was not output-budget starvation and is not leaderboard-comparable.

See [`supplemental/PROGRAMBENCH_Q11A.md`](supplemental/PROGRAMBENCH_Q11A.md).

## AEON uncensored BF16

The campaign also performed a public-safe first pass on AEON's Qwen3.8 uncensored BF16 checkpoint. Exact canaries passed on the compatible runtime and refusal behavior changed, but the matched base-BF16 comparison was still incomplete at this release checkpoint.

See [`supplemental/AEON_PUBLIC_SAFE.md`](supplemental/AEON_PUBLIC_SAFE.md).
