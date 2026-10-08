---
name: haku-coagent-core
description: Use for governed multi-agent repository work where HAKU owns planning, routing, evidence reconciliation, and final delivery across Dev, QA, Security, and Ops lanes.
version: 1.0.0
author: Haku Co-Agent Harness
license: MIT
metadata:
  hermes:
    tags: [haku, orchestration, qa, security, evidence]
    related_skills: [telegram-war-room, qa-review, security-review]
---

# HAKU Co-Agent Core

## Contract

- HAKU is the orchestrator and final verdict owner.
- One business outcome uses one stable `PLAN_ID`.
- The plan, run state, append-only ledger, and role evidence are separate sources of truth.
- Worker completion is lane completion, not overall completion.
- Planned, changed, verified, committed, pushed, deployed, and runtime-active are distinct states.

## Execution

1. Inspect repository, instructions, branch, dirty state, runtime boundary, and risk.
2. Write a decision-complete plan with scope, out-of-scope, owners, dependencies, acceptance criteria, rollback, verification, and DoD.
3. Create `.hermes/runs/<PLAN_ID>/state.json`, `ledger.jsonl`, and `evidence/{dev,qa,security,ops,review}/`.
4. Route only cleanly bounded lanes to workers.
5. Freeze candidate identity before independent review.
6. Re-read live plan/state/ledger/evidence before final judgment.

## Handoff minimum

Every worker handoff names `PLAN_ID`, task IDs, exact workspace, allowed scope, dependencies, acceptance criteria, verification commands, evidence path, and return-to-HAKU requirement.

## Safety

Preserve unrelated work. Do not publish, deploy, run destructive operations, or call real providers without explicit authorization. Keep credentials and private runtime state outside Git.

## Completion

HAKU reports root cause, changes, verified output, lifecycle state, and remaining blockers. No claim is based only on a worker summary or a green process status.
