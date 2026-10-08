# Security Policy

## Scope

This repository contains workflow guidance, templates, and validation scripts. It must never contain production credentials, private keys, raw memory databases, session transcripts, or personal chat exports.

## Reporting a vulnerability

Do not open a public issue containing secrets or exploitable details. Contact the repository owner through a private GitHub security advisory or another private channel.

Include:

- affected file or component
- reproducible impact
- sanitized reproduction steps
- suggested containment or fix

## Secret handling rules

- Use environment variables or a secret manager for credentials.
- Commit only placeholders such as `CHANGE_ME` or `${ENV_VAR}`.
- Redact tokens, cookies, authorization headers, phone numbers, prompts, memory content, and customer identifiers from evidence.
- Run `python3 scripts/secret_scan.py` before committing.
- If a secret is committed, revoke/rotate it first, then remove it from the current tree and history through an approved repository maintenance procedure.

## Workflow safety

Behavioral instructions are defense in depth, not a kernel sandbox. High-impact actions still require bounded scope, explicit authorization, rollback, and independent verification.
