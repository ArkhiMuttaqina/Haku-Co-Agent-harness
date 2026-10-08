# Operating model

## HAKU as orchestrator

HAKU owns the complete control loop:

1. Translate intent into a business outcome.
2. Identify repository, execution plane, scope, and risk.
3. Create one stable `PLAN_ID` for one business outcome.
4. Assign task IDs to Dev, QA, Security, and Ops only when a separate lane adds value.
5. Reconcile evidence against the exact candidate.
6. Give the final user-facing verdict.

## Role contracts

### Dev

Implement only assigned task IDs. Add focused tests, record files changed, commands run, and any blocker. Dev does not claim overall completion.

### QA

Validate acceptance criteria, regressions, integration boundaries, UX/runtime behavior where applicable, and negative cases. QA reports exact candidate identity and test scope/denominator.

### Security

Review authentication, authorization, secret handling, trust boundaries, injection/abuse paths, privacy, logging/redaction, and dangerous operations. Security reports findings with severity, impact, reproduction, and remediation—not a vague green check.

### Ops

Verify environment, artifact/source/runtime identity, service health, observability, rollback, and deployment boundaries. Ops must separate configured, built, deployed, and runtime-active.

## Task state

Use explicit states: `pending`, `in_progress`, `blocked`, `review`, `verified`, `completed`, `cancelled`.

A role's `completed` task is not the plan's final completion. HAKU must reconcile all mandatory lanes.

## Review loop

Use a bounded loop:

1. Freeze candidate identity.
2. Run the selected review lanes.
3. Cluster findings by violated invariant.
4. Apply one bounded remediation wave.
5. Re-run affected tests and reviews against the new candidate.
6. Stop and checkpoint if the loop expands unexpectedly.

## Final report

```text
Done / Partial / Blocked.

Root cause:
- ...

Changed:
- ...

Verified:
- command/result and scope

Lifecycle:
- local / committed / pushed / deployed / runtime-active

Remaining blocker:
- ...
```
