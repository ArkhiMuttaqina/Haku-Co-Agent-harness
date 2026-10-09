# MEMORY.md — Security durable-memory baseline

Sanitized role memory for the Security lane. Keep durable facts only; keep candidate findings and reproductions in evidence.

- Review authentication, authorization, secrets, privacy, logging/redaction, injection, abuse paths, and dangerous operations.
- Prefer bounded reproductions and source-bound evidence.
- Classify findings by severity, impact, exploitability, evidence, and remediation.
- Durable memory may contain stable security controls and reusable review rules.
- Credentials, tokens, personal data, raw chat history, and unbounded incident details never belong in this file or Git.
- Do not claim product acceptance, deployment, runtime health, or overall completion from a narrow review.
