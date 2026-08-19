# Supplemental: ProgramBench Q11A reasoning-mode A/B

**This result sealed after the main article draft.** It is a single preregistered ProgramBench task, not a multi-task score and not leaderboard-comparable. Only the reasoning-mode setting changed under a frozen Mia #40914 agent setup.

| Mode | Tests | Pass % | Model calls | Wall | Reasoning chars | Terminal state |
|---|---:|---:|---:|---:|---:|---|
| OFF original | 251/502 | 50.0% | 18 | 78 s | 0 | submitted early / unresolved |
| OFF repeat | 241/502 | 48.01% | 30 | 302 s | 0 | limits exceeded |
| LOW | 253/502 | 50.4% | 30 | 303 s | 22,540 | submitted / unresolved |
| XHIGH | 0/502 | 0.0% | 15 | 343 s | 9,978 | repeated format error / compile failure |
| MEDIUM | **308/502** | **61.35%** | 30 | 594 s | 38,085 | limits exceeded |

![ProgramBench Q11A reasoning A/B](../figures/fig-programbench-q11a.png)

No arm hit `finish_reason=length` under `max_tokens=8192`, so the XHIGH failure here was **not the same output-budget-starvation mechanism** seen in the 2K shader study. XHIGH failed the agent loop before a compiling solution. MEDIUM produced the highest test coverage but also the longest wall time.

This result complicates, rather than overturns, the article's MEDIUM discussion: MEDIUM still has no dedicated MEDIUM instruction branch on the pinned template, yet on this one task the resulting “thinking on without LOW/XHIGH instruction text” behavior produced the best coverage. That is interesting one-task evidence, not a universal default recommendation.

Evidence seal: `9161bdd5ba2b70d452a010c1cb5547efdcbcf2f6`.
