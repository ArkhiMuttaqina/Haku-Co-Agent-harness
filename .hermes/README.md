# Haku Co-Agent Harness

## Active plans

- `plans/HAKU-261008-harness-bootstrap.md` — initial sanitized harness bootstrap (in progress).
- `plans/HAKU-261010-erp-ui-ux-alignment.md` — ERP/UI/UX skill and Hermes tooling alignment (local).

## Rules

- The plan is the source of truth for scope, tasks, acceptance criteria, and DoD.
- `runs/<PLAN_ID>/ledger.jsonl` is append-only execution history.
- `runs/<PLAN_ID>/evidence/<role>/` contains role-specific proof.
- Only HAKU/master marks top-level tasks complete after verifying evidence.
- Keep private memory, credentials, session state, and temporary logs outside the repository.
- `skills/haku-coagent-erp-ui-ux/SKILL.md` governs ERP/UI/UX work; companion third-party skills remain separately sourced and verified in the target Hermes profile.
