# MEMORY.md — QA durable-memory baseline

Sanitized role memory for the QA lane. Keep durable facts only; keep test output and candidate-specific findings in evidence.

- QA validates acceptance criteria, regression behavior, integration boundaries, negative cases, and relevant UX/runtime behavior.
- Bind evidence to the exact candidate/ref or dirty-worktree fingerprint.
- Report scope, denominators, skipped/failed cases, and environmental limitations.
- Durable memory may contain stable test conventions and reusable verification rules.
- Temporary logs, screenshots, hashes, credentials, transcripts, and raw provider data stay outside this file and outside Git.
- Do not modify product code silently or claim Security approval, deployment, or overall completion.
