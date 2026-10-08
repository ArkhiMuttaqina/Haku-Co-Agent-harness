---
name: qa-review
description: Use for independent QA of agent-produced changes, including acceptance criteria, regressions, integration boundaries, UX/runtime behavior, and evidence quality.
version: 1.0.0
author: Haku Co-Agent Harness
license: MIT
metadata:
  hermes:
    tags: [qa, testing, regression, evidence]
    related_skills: [haku-coagent-core, security-review]
---

# QA Review

## Review contract

Bind the review to the exact candidate: branch/commit or a deterministic dirty-worktree fingerprint. State test scope, denominator, skipped cases, environment, and limitations.

## Checklist

- Map each acceptance criterion to a reproducible check.
- Exercise happy path, negative path, boundary values, retries/cancellation, and relevant integration seams.
- Verify user-visible behavior in the actual runtime surface when UI/Telegram behavior is in scope.
- Separate tests run by QA from results merely cited from prior evidence.
- Do not modify product code during an independent verification pass.

## Verdicts

Use `PASS`, `PASS_WITH_LIMITATIONS`, or `BLOCKED`, with exact failing command and root cause. QA does not grant Security approval or deployment/runtime parity.
