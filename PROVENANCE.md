# Provenance

This public repository is an allowlisted export from a separate private campaign lab notebook. The private repository is not required to read or reproduce the published results.

Evidence seal identifiers are preserved in public result files to make the research trail auditable against the original campaign. The most important seals include:

| Study | Seal |
|---|---|
| Template re-audit | `0f13cac639bbadc2be617551f3ad78b3a801722f` |
| Hard reasoning 50-task pack | `e5fd10282bd758e0d65b836a8c1b4b39a609b463` |
| Temperature | `0bb7426c280a911dc5422a2a4dda8c70f9763c20` |
| Verbosity | `5c158ebeef7577605589934f3e8b1243f35e8dbb` |
| BF16 quality | `aa28cf974870dede92b5c15f6dd565b8716b36c6` |
| FP8 quality | `417704f6636bf14f544ad34f89e752cb160dd4ff` |
| NVFP4 quality | `040dd1d02e52829e58fa53481cb1236c00911617` |
| DSPARK RTX5090 | `ca5dc168a9faaa1d364b28b85726090159c3994f` |
| Mia patched #40914 | `5e9aa4ebcf149bd4b9a303fbdc02c48386cc8320` |
| ProgramBench Q11A reasoning A/B | `9161bdd5ba2b70d452a010c1cb5547efdcbcf2f6` |

The repository's validation workflow checks the required public evidence surface, parses every JSON result, scans public text for credential/local-path patterns, checks relative links, and verifies the three headline claim traces.
