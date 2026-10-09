# MEMORY.md — HAKU durable-memory baseline

This file is a sanitized starter memory for a HAKU profile. It is a policy and seed surface, not a copy of a user's private memory database.

## Durable facts to keep

- HAKU owns orchestration, routing, prioritization, evidence reconciliation, and final user-facing judgment.
- Dev, QA, Security, and Ops are separate evidence lanes with explicit boundaries.
- One stable `PLAN_ID` maps to one repo-local plan, run state, append-only ledger, and evidence tree.
- Source, local verification, commit, push, deployment, and runtime-active status are separate claims.
- Durable memory stores compact, sanitized preferences, stable environment conventions, role mappings, architecture decisions, and reusable workflow rules.
- Task progress, logs, hashes, commit IDs, incident details, transcripts, and raw provider output belong in task/session artifacts instead.
- Secrets, tokens, private keys, cookies, raw chat history, and raw Mnemosyne databases never belong in Git or this file.

## Memory write contract

- Check for an existing or superseded fact before writing.
- Prefer one canonical declarative fact over duplicate entries.
- Mark uncertain information as inferred or unknown.
- Keep entries compact and bounded; do not paste full conversations or logs.
- Supersede stale facts instead of leaving contradictory open entries.
- Use the configured Mnemosyne provider for durable cross-session records; use the repo-local `.hermes/runs/` tree for ephemeral task state.

## Shared-agent boundary

HAKU, Dev, QA, and Security may share durable workflow context only through the authenticated configured memory provider. The repository ships schema, policy, and placeholders—not private memory records.

## Local customization

Replace or extend this file only with sanitized, durable facts appropriate for the target profile. Keep user-specific identity, provider settings, chat IDs, credentials, and personal preferences in the local Hermes profile or memory provider rather than in the public harness repository.
