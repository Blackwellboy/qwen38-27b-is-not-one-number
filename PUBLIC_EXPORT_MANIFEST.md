# Public export boundary

The export is intentionally allowlist-based. Public content consists of the article, original figures, sealed/sanitized result summaries, machine-readable tables, protocol manifests, methodology, supplemental public-safe findings and release validation tooling.

Excluded by design: private operational queues, session handoffs, fleet-control state, TODOs/changelogs, agent orchestration prompts, machine-local paths and network details, private benchmark payloads, access tokens/credentials, internal scratch logs, and raw disallowed AEON outputs.

A failure is **not** excluded merely because it is ugly. Scientifically relevant interrupted runs, protocol mismatches and correctness HOLDs remain in the release.
