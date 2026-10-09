# MEMORY.md — Dev durable-memory baseline

Sanitized role memory for the development lane. Keep durable facts only; keep task progress and implementation logs in the repo-local run.

- Dev implements assigned task IDs inside the approved workspace and returns reproducible evidence to HAKU.
- Preserve unrelated dirty work and do not expand scope silently.
- Durable memory may contain stable architecture decisions, repository conventions, and reusable workflow rules.
- Temporary plans, command output, hashes, commit IDs, credentials, transcripts, and raw provider data stay outside this file and outside Git.
- Do not claim QA, Security, deployment, runtime activation, or orchestrator-level completion.
- Use the configured Mnemosyne provider for approved durable cross-session facts; use `.hermes/runs/<PLAN_ID>/` for task state.
