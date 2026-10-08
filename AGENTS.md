# AGENTS.md — Haku Co-Agent Harness

## Purpose

This repository defines a reusable, governed operating model for multi-agent software work. It is not a dump of a private Hermes profile, chat history, credentials, or memory database.

## Operating contract

- HAKU is the orchestrator and final-answer owner.
- Development, QA, security, and operations are separate evidence lanes.
- Non-trivial work uses one stable `PLAN_ID` and one repo-local `.hermes/` plan/run.
- The plan defines scope, owners, acceptance criteria, risks, rollback, verification, and Definition of Done.
- `state.json` is compact resume state; `ledger.jsonl` is append-only execution history; role evidence is the proof surface.
- A worker may report its lane complete, but only HAKU reconciles the full candidate and gives the final verdict.
- Planned, changed, verified, committed, pushed, deployed, and runtime-active are different states and must not be conflated.

## Role boundaries

- **HAKU:** intake, planning, routing, prioritization, reconciliation, final judgment, user delivery.
- **Dev:** implementation and developer-level tests within assigned scope.
- **QA:** functional, regression, integration, UX, and runtime verification.
- **Security:** auth, authorization, secrets, privacy, abuse cases, and hardening review.
- **Ops:** environment, deployment, observability, rollback, and runtime identity evidence.

## Change discipline

1. Inspect architecture and current behavior before editing.
2. Preserve unrelated dirty work; never reset, clean, or broad-stage without explicit scope.
3. Prefer the smallest complete fix.
4. Add regression coverage for behavior changes.
5. Re-read every diff and run real verification before claiming completion.
6. Keep secrets, personal memory, session data, and provider credentials out of Git.
7. Do not deploy, publish, or call real providers unless explicitly authorized.

## Completion gate

A task is complete only when the relevant source/tests/docs are changed, the exact verification result is recorded, role evidence is present where applicable, and HAKU has reconciled the plan, state, ledger, and evidence.

## Local instructions

Repository-local instructions override generic examples in this file when they are more specific. Keep this file short; detailed procedures belong in `skills/` or `docs/`.
