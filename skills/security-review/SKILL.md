---
name: security-review
description: Use for security review of agent workflows and repository changes covering auth, permissions, secrets, privacy, abuse paths, logging, and destructive operations.
version: 1.0.0
author: Haku Co-Agent Harness
license: MIT
metadata:
  hermes:
    tags: [security, auth, secrets, privacy, abuse]
    related_skills: [haku-coagent-core, qa-review]
---

# Security Review

## Review contract

Review the exact candidate and trust boundary. Classify findings by severity, impact, exploitability, evidence, and remediation. Do not expose secret values or personal data.

## Checklist

- Trace authentication and authorization from ingress to mutation/runtime use.
- Check secret storage, logging, redaction, error paths, and artifact handling.
- Exercise unauthorized, cross-tenant, malformed, replay, injection, and privilege-boundary cases where relevant.
- Inspect dangerous terminal/file/database/container/publication paths for scope validation, ambiguity handling, rollback, and confirmation fencing.
- Check that memory/session data cannot be accidentally committed or disclosed.

## Verdicts

Use `PASS`, `BLOCKED`, or `FINDINGS`. A narrow test pass is not a repo-wide security claim. Security approval does not imply product acceptance, deployment, or runtime health.
