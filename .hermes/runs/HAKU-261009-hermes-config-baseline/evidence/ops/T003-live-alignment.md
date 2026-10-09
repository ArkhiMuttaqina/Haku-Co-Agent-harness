# T003 — live dev1 alignment

Target: `/home/arkhi25/.hermes/profiles/dev1/`

Changed on disk:

- Added `agent.reasoning_effort: high`.
- Enabled the same operational plugin set as HAKU where the plugins are
  available: `disk-cleanup`, `security-guidance`, `platforms/telegram`,
  `hermes-lcm`, `hermes-progress-tail`, `mnemosyne`, and
  `hermes-error-transparency`.
- Progress-tail config was already behaviorally aligned; Shiro's label and
  worker admission gate were preserved.

Backup:

- `/home/arkhi25/.hermes/profiles/dev1/backups/config-before-haku-baseline-20261009T132810Z.yaml`
- Pre-change config and backup SHA-256 matched:
  `81533ce5c8779f4acdccec4083697161f69ae0c449f97b9f320c906d49a818a4`

No gateway restart was run. Plugin CLI explicitly reports activation on the
next session, so runtime activation remains pending.
