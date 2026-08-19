# Benchmark harness failures are part of the result

The final three-arm GSM8K + IFEval table required three attempts. The first two are deliberately not converted into scores.

| Attempt | What happened | Operational counters | Disposition |
|---|---|---|---|
| 1 | Main control-plane OOM; remote Spark servers survived | BF16 392/1860, FP8 976/1860, NVFP4 1329/1860 | `INTERRUPTED_NON_SCOREABLE` |
| 2 | lm-eval SQLite response cache became read-only | partial progress only | `INTERRUPTED_NON_SCOREABLE` |
| 3 | Hardened recovery run | 1860/1860 on each arm, 0 errors | `PASS / SEALED` |

No partial rows were stitched between runs. After the failures, the controller path was hardened with lm-eval 0.4.12, deterministic response-cache resume, append-only fsynced journaling, terminal-independent managed controllers with `Restart=no`, exact/fail-closed completion gates, and immutable run identities.

The scientific point is simple: a model endpoint can remain healthy while a benchmark becomes invalid. The harness/controller belongs in the benchmark provenance.
