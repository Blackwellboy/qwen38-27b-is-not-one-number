# Qwen 3.8 27B is not one number

**First-party deployment research across one RTX 5090 and three DGX Sparks.**

This is the public, sanitized research release behind the article **“Qwen 3.8 27B is not one number.”** It contains the technical results, protocol identities, figures, negative results and reproducibility notes needed to interpret the claims — without the private lab notebook's fleet-control chatter, TODOs, session handoffs or sensitive raw material.

![RTX 5090 stack comparison](figures/fig-5090-stacks.png)

## Start here

- **[Read the article](ARTICLE.md)**
- **[Browse the results index](results/INDEX.md)**
- **[Read post-draft supplemental findings](SUPPLEMENTAL_FINDINGS.md)**
- **[Methodology](methodology/METHODOLOGY.md)** and **[claims / limitations](methodology/CLAIMS_AND_LIMITATIONS.md)**
- **[Machine-readable master table](data/master_results.csv)**

## Headline findings

| Finding | Result |
|---|---|
| Hard reasoning, fixed 4K completion budget | OFF 68% · **LOW 94%** · XHIGH 88%; XHIGH truncated 5/50 |
| Easy-task latency | OFF p50 **0.93 s** vs LOW 8.35 s / unset 8.51 s / XHIGH 8.49 s |
| Open-template default | unset reasoning effort behaved as **XHIGH** on the pinned template |
| Quant quality | BF16 / FP8 / NVFP4 stayed close and metric-dependent on matched GSM8K + IFEval |
| Context trap | one “262K” SGLang deployment exposed only **42,624 realized KV tokens** |
| RTX 5090 serving | ~71.8 tok/s SGLang NONE → 81.74 DSPARK → **151.27 patched Mia** |
| Mia stock accelerated path | TQ4 KV + MTP3 active, but correctness failed → **HOLD_CORRECTNESS** |
| Patched Mia #40914 | correctness PASS, 1,056 ISL / 1,024 OSL, **151.27 tok/s**, 99.52% MTP acceptance |
| Harness integrity | two long quality attempts discarded; only the third clean 1,860/1,860-per-arm run was scored |

## A note on MEDIUM

The pinned open template accepts `reasoning_effort=medium`, but there is no dedicated MEDIUM effort instruction branch. That does **not** mean the mode has no observable behavior. A post-draft, single-task ProgramBench A/B actually produced the highest coverage under MEDIUM (308/502 = 61.35%), while XHIGH failed the agent loop. That supplemental result is intentionally labeled **one-task, non-leaderboard evidence** rather than turned into a universal MEDIUM recommendation.

## What is intentionally not here

The private campaign repository remains the lab notebook. This public export excludes machine-specific orchestration, working queues, TODOs, change logs, agent prompts, network/port details, local filesystem paths, private benchmark payloads, secret-bearing material, and raw harmful-content outputs. Scientific negative results are kept when they affect interpretation.

## Evidence policy

A green HTTP response, process exit, progress counter or pretty throughput number is not a benchmark PASS. This release requires explicit correctness and completion gates, keeps requested vs realized token counts separate, labels protocol mismatches as HOLDs, and never stitches interrupted benchmark rows into a later score. See [methodology](methodology/METHODOLOGY.md).

## Release checkpoint

This snapshot incorporates sealed evidence through **2026-08-19 11:30 UTC**, including the post-draft ProgramBench Q11A reasoning-mode A/B. The matched BF16/FP8 HumanEval+ arms and full MBPP+/BigCodeBench comparison were not terminal at this export checkpoint, so partial progress is not published as a score.

## License

Original scripts in this repository are MIT-licensed. Original BlackwellBoy prose, figures and result tables are CC BY 4.0. No third-party benchmark datasets, model weights or restricted raw outputs are redistributed; upstream materials retain their own licenses. See [LICENSE.md](LICENSE.md).
