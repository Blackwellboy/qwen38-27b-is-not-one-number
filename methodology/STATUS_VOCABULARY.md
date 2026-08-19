# Status vocabulary

| Status | Meaning |
|---|---|
| `PENDING` | not started |
| `READY` | prerequisites prepared; execution not complete |
| `RUNNING` | active work; no score implied |
| `PASS` | explicit criteria met |
| `SEALED` | completed bounded result preserved with durable evidence |
| `HOLD` | blocked, protocol-mismatched or unavailable; scope-specific and not necessarily a model failure |
| `FAIL` | requested criteria failed with evidence |
| `INTERRUPTED_NON_SCOREABLE` | execution stopped and partial data cannot be validly scored or stitched |
