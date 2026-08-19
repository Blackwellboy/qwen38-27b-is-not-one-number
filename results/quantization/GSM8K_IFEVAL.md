# BF16 vs FP8 vs NVFP4 — GSM8K + IFEval

Matched three-arm DGX Spark comparison using explicit **THINKING_OFF**, lm-eval 0.4.12, and identical benchmark revisions. Every arm completed **1,860/1,860 requests with zero request errors**. There is no combined score and no universal quantization winner.

| Metric | BF16 | FP8 | NVFP4 |
|---|---:|---:|---:|
| GSM8K flexible | 96.5125% | 95.9818% | 95.3753% |
| GSM8K strict | 96.0576% | 95.8302% | 95.2237% |
| IFEval prompt strict | 81.5157% | 81.3309% | 81.8854% |
| IFEval instruction strict | 86.8106% | 87.1703% | 87.4101% |
| IFEval prompt loose | 85.7671% | 85.0277% | 85.0277% |
| IFEval instruction loose | 90.2878% | 90.0480% | 89.9281% |
| Requests | 1860/1860 | 1860/1860 | 1860/1860 |

## Identity

| Arm | Model revision | Runtime | Evidence seal |
|---|---|---|---|
| BF16 | `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0` | aeon-vllm `0.25.0+aeon.sm121a.dflash` | `aa28cf974870dede92b5c15f6dd565b8716b36c6` |
| FP8 | `017b9c7af6b5689d5dd426a76e0bc077eb5ca20a` | same | `417704f6636bf14f544ad34f89e752cb160dd4ff` |
| NVFP4 | `9c73e2daee1d0fd494ffbd1d8753f2174a953796` | same | `040dd1d02e52829e58fa53481cb1236c00911617` |

The result supports a narrow claim: on this board, aggressive quantization **did not collapse quality**. GSM8K moved modestly downward as quantization increased; the strict IFEval metrics were small and mixed. It does not establish universal BF16/FP8/NVFP4 equivalence.
