# Claims and limitations

This release is a first-party deployment study, not a universal model leaderboard. The model can only be compared across cells whose protocol is actually matched.

Strong claims supported here include: the pinned open template's unset effort behaves as XHIGH; `preserve_thinking` can dramatically inflate subsequent prompts; LOW beat XHIGH on the bounded 50-task hard pack under a fixed completion budget; BF16/FP8/NVFP4 were close and mixed on the matched GSM8K/IFEval board; one 262K-configured deployment exposed only 42,624 realized KV tokens; and the same RTX 5090 moved from about 71.8 to 81.74 to 151.27 true decode tok/s across different serving stacks.

Claims **not** supported include: LOW is universally smarter than XHIGH; MEDIUM is fake; NVFP4 is universally equivalent or superior to BF16; every RTX 5090 deployment can use 262K context; llama.cpp was proven at 261K; DSPARK produced 206 tok/s here; Mia reproduced 160 tok/s; or a partial benchmark can be treated as nearly complete.

ProgramBench Q11A is explicitly one-task, non-leaderboard evidence. The AEON matched base-BF16 leg was incomplete at this release checkpoint. Full matched BF16/FP8 coding and BigCodeBench were also not complete at the export checkpoint.
