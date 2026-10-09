# HAKU-261009-hermes-config-baseline

## Problem and business intent

The portable harness documented Telegram behavior but did not ship the recommended
Hermes configuration surface or the complete progress-tail baseline. Add a
sanitized, profile-aware baseline so HAKU and Shiro can share the operational
settings without publishing private provider catalogs, credentials, chat IDs,
or runtime state.

## Scope

### In scope

- Add a sanitized shared Hermes YAML baseline under `templates/hermes/`.
- Add HAKU and Shiro/dev1 role overlays for progress-tail identity and Telegram
  admission semantics.
- Document what is shared versus intentionally role-specific.
- Extend the dependency-light validator to require the new template files.
- Align the live dev1 profile's recommended operational settings and plugin
  enablement, with a rollback backup and no gateway restart.
- Include sanitized profile `SOUL.md` and `MEMORY.md` baselines plus the
  recommended Mnemosyne memory configuration; never copy private profile
  memory or raw databases.

### Out of scope

- Copying or publishing live `config.yaml`, provider/model catalogs, tokens,
  chat IDs, `.env`, memory databases, sessions, or logs.
- Changing dev1's selected model/provider, auxiliary routing, SOUL, memory
  records, Telegram allowlists, or worker mention gate.
- Copying private `SOUL.md`, `MEMORY.md`, canonical user records, raw Mnemosyne
  databases, session history, or profile-private identity state into the repo.
- Restarting gateways, performing Telegram behavioral smoke, or publishing a
  new GitHub commit in this task.

## Assumptions and boundaries

- Canonical repository: `/home/arkhi25/repo/Haku-Co-Agent-harness`.
- Live HAKU profile: `/home/arkhi25/.hermes/`.
- Live Shiro/dev1 profile: `/home/arkhi25/.hermes/profiles/dev1/`.
- Existing dev1 profile is the target for operational alignment; HAKU remains
  the reference baseline.
- The live config edit is reversible from the timestamped backup and remains
  restart-pending because gateways are not restarted here.

## Architecture/runtime flow

Portable common YAML -> role overlay -> profile-owned provider/model and
credential configuration -> Hermes config loader -> plugin discovery -> fresh
session/gateway behavior. Static templates prove the intended contract only;
plugin installation, config readback, and runtime rendering are separate gates.

## Risks and rollback

- Risk: a full profile copy could overwrite role identity or private provider
  settings. Mitigation: templates contain only shared operational keys and
  explicit overlays; live edits touch only `agent.reasoning_effort` and plugin
  enablement.
- Risk: enabling a plugin changes the next session. Mitigation: no restart;
  preserve the pre-change config backup and report activation as pending.
- Rollback: restore `/home/arkhi25/.hermes/profiles/dev1/backups/config-before-haku-baseline-20261009T132810Z.yaml`
  and disable only the newly enabled plugin entries if Arkhi requests rollback.

## Tasks

| ID | Owner | Depends on | Acceptance criteria | Verification | Evidence |
|---|---|---|---|---|---|
| T001 | HAKU | - | Live HAKU/dev1 configs and harness boundaries inspected; private fields excluded | redacted config diff and path inventory | `evidence/dev/T001-discovery.md` |
| T002 | HAKU | T001 | Common baseline and HAKU/dev1 overlays exist and are documented | YAML parse, README/docs readback | `evidence/dev/T002-templates.md` |
| T003 | HAKU | T002 | dev1 recommended settings/plugins aligned with rollback available; no restart performed | config readback, plugin list, backup hash | `evidence/ops/T003-live-alignment.md` |
| T004 | HAKU | T002,T003 | validator and secret scan pass; no private runtime artifact enters repo | real validation commands and tracked-tree scan | `evidence/qa/T004-validation.md` |
| T005 | HAKU | T004 | HAKU reconciles plan/state/ledger/evidence and reports runtime activation boundary | final diff and status readback | `evidence/review/T005-final.md` |
| T006 | HAKU | T005 | Progress-tail duplicate discovery is removed without deleting recovery material; default/dev1 active copies are identical | plugin discovery and byte-level parity readback | `evidence/ops/T006-progress-tail-parity.md` |
| T007 | HAKU | T005 | Sanitized SOUL/MEMORY role baselines and Mnemosyne config are included and validated; private runtime state remains excluded | required-file validation, YAML parse, secret scan, content review | `evidence/dev/T007-memory-soul-baseline.md` |

## Definition of Done

- [x] Shared sanitized Hermes baseline and two role overlays exist.
- [x] README and Telegram behavior docs explain parity and role exceptions.
- [x] Live dev1 recommended settings/plugins are aligned with backup retained.
- [x] Validator, YAML parse, secret scan, shell syntax, and diff checks pass.
- [x] No gateway restart, Git push, or private runtime artifact occurs.
- [x] Runtime activation is reported as restart-pending, not claimed active.
- [x] Sanitized role SOUL/MEMORY baselines and Mnemosyne config are included;
  private memory records and raw databases remain excluded.
