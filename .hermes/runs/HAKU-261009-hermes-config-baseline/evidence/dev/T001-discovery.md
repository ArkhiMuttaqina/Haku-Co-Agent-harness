# T001 — discovery

- Canonical repo: `/home/arkhi25/repo/Haku-Co-Agent-harness`.
- Live profiles inspected: HAKU/default and Shiro/dev1.
- Shared operational sections already mostly matched: display, context compression,
  sessions, delegation, memory, terminal, approvals, and progress-tail values.
- Gaps found: dev1 lacked `agent.reasoning_effort: high`; plugin enablement was
  narrower than HAKU; the repository did not ship the actual sanitized baseline.
- Intentional differences preserved: selected model/provider, auxiliary routing,
  provider/model catalogs, `telegram.require_mention`, and progress label.
- No credential value or private runtime database was copied into the repository.
