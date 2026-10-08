# Haku Co-Agent Harness

## Active plans

- `plans/HAKU-261008-harness-bootstrap.md` — initial sanitized harness bootstrap (in progress).

## Rules

- The plan is the source of truth for scope, tasks, acceptance criteria, and DoD.
- `runs/<PLAN_ID>/ledger.jsonl` is append-only execution history.
- `runs/<PLAN_ID>/evidence/<role>/` contains role-specific proof.
- Only HAKU/master marks top-level tasks complete after verifying evidence.
- Keep private memory, credentials, session state, and temporary logs outside the repository.
