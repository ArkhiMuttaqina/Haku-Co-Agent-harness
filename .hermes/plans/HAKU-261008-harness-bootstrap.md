# HAKU-261008-harness-bootstrap

## Problem and business intent

Create a sanitized, reusable Haku Co-Agent Harness repository for Hermes/HAKU-style multi-agent work. Preserve the workflow that makes HAKU effective without publishing private profile state, raw memory, credentials, or project-specific confidential material.

## Scope

### In scope

- Repository README and contributor/security guidance.
- Repo-readable AGENTS.md contract.
- Generic HAKU, Dev, QA, and Security profile templates.
- Architecture, operating model, memory policy, and Telegram behavior docs.
- Curated reusable skills for core orchestration, Telegram war-room behavior, QA, and Security.
- Plan/run/evidence templates.
- Dependency-light validation, secret-safety scan, and isolated skill installer.

### Out of scope

- Raw Hermes/Mnemosyne databases, sessions, logs, credentials, or personal memory.
- Real Telegram bot configuration, gateway restart, deployment, or provider calls.
- Project-specific HashMicro/Apollo incidents or private infrastructure details.
- GitHub release automation beyond the initial repository push.

## Assumptions and boundaries

- Target checkout: `/home/arkhi25/repo/Haku-Co-Agent-harness`.
- Target remote: `https://github.com/ArkhiMuttaqina/Haku-Co-Agent-harness.git`.
- Sibling boundary: do not write inside `/home/arkhi25/repo/sshpick`.
- Initial repository is private/owner-controlled; publication state is reported separately from local verification.

## Architecture/runtime flow

User intent -> HAKU orchestration -> role lanes (Dev/QA/Security/Ops) -> repo plan/run/evidence -> runtime adapter (optional Hermes/Telegram/provider).

## Risks and rollback

- Risk: accidentally exporting private profile/runtime state. Mitigation: curated files only, `.gitignore`, secret scan, manual diff review.
- Risk: scripts overwrite a user's Hermes home. Mitigation: explicit target, canonicalization, refuse protected roots, refuse existing skill destination.
- Rollback: remove the initial local commit or revert the commit; no external runtime mutation is performed.

## Tasks

| ID | Owner | Depends on | Acceptance criteria | Verification | Evidence |
|---|---|---|---|---|---|
| T001 | HAKU | - | Empty GitHub repo cloned to exact sibling path; sshpick untouched | `git remote -v`, path/status checks | `evidence/dev/T001-bootstrap.md` |
| T002 | HAKU | T001 | Sanitized README, AGENTS, docs, profiles, skills, templates, and scripts exist | file inventory + validator | `evidence/dev/T002-package.md` |
| T003 | HAKU | T002 | Secret scan, shell syntax, diff check, and isolated install pass | real command outputs | `evidence/qa/T003-validation.md` |
| T004 | HAKU | T003 | Security boundary and publication readiness reviewed; no raw private state included | tracked-file scan + diff review | `evidence/security/T004-security.md` |
| T005 | HAKU | T003,T004 | Local commit and remote push verified against exact commit | `git show`, `git ls-remote` | `evidence/review/T005-final.md` |

## Definition of Done

- [x] All in-scope sanitized artifacts exist.
- [x] Validator, secret scan, shell syntax, diff check, and isolated install pass.
- [x] sshpick remains outside the target tree and unchanged.
- [x] Plan, state, ledger, and role evidence reconcile.
- [x] Local commit and remote branch parity are verified if publication is authorized.
- [x] No claim is made for runtime activation because no Hermes gateway was modified.
