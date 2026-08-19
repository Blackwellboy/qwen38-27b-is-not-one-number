# Explicit HOLDs and non-claims

`HOLD` means the requested protocol could not be validly completed under the tested conditions. It is not automatically a model failure.

| Item | Disposition | What it means |
|---|---|---|
| SGLang NONE native ~261K | `HOLD_REALIZED_KV_CAPACITY` | configured 262K, but that deployment exposed only 42,624 realized KV tokens |
| DFlash-2 on stock SGLang image | `HOLD_PROTOCOL_RUNTIME_DFLASH2DRAFTMODEL_UNREGISTERED` | stock runtime lacked the required draft-model registration; not a verdict that DFlash-2 itself cannot work |
| Spark native tools / BFCL | `HOLD_PROTOCOL_NATIVE_TOOLS_REQUIRED` | native OpenAI tools schema returned HTTP 400 on the three tested Spark arms; text-JSON substitution was not accepted as equivalent |
| GPQA Diamond | gated-data access HOLD | no substitute benchmark was used |
| MMLU-Pro | harness compatibility HOLD | no forced protocol equivalence |
| Marlin NVFP4 | PTX/toolchain HOLD | requested backend could not be validly exercised on the tested build/toolchain |
| Mia stock TQ4 KV + MTP3 | `HOLD_CORRECTNESS` | acceleration active, but correctness canaries failed |

This repository prefers a documented HOLD to a prettier number produced by changing the protocol.
