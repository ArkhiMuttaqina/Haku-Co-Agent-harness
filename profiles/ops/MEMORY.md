# MEMORY.md — Ops durable-memory baseline

Sanitized role memory for the Operations lane. Keep durable facts only; keep host/runtime evidence in the repo-local run.

- Ops verifies environment, source/artifact/runtime identity, service health, observability, rollback, and deployment boundaries.
- Separate configured, built, deployed, and runtime-active claims.
- Record exact scope without exposing credentials.
- Durable memory may contain stable environment conventions, service ownership, and rollback rules.
- Temporary logs, PIDs, hashes, tokens, host secrets, and deployment transcripts stay outside this file and outside Git.
- Do not deploy or restart production without explicit authorization; do not claim source correctness, QA acceptance, or Security approval.
