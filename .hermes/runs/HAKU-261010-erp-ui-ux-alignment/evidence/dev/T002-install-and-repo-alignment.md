# T002/T003 — ERP UI/UX installation and harness alignment

Candidate: local working tree on `main` (publication not authorized)
Owner: HAKU-direct

## Hermes install evidence

Official source URLs were inspected before installation:

- shadcn: https://raw.githubusercontent.com/shadcn-ui/ui/main/skills/shadcn/SKILL.md
- Vercel Web Design Guidelines: https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md
- Anthropic Frontend Design: https://raw.githubusercontent.com/anthropics/claude-code/main/plugins/frontend-design/skills/frontend-design/SKILL.md

Hermes native installer security scans returned `SAFE` and `ALLOWED` for all three. The default profile was targeted explicitly with `HERMES_HOME=/home/arkhi25/.hermes`.

Installed/enabled in the default profile:

- `frontend/shadcn`
- `frontend/web-design-guidelines`
- `frontend/frontend-design`
- existing local `haku-coagent-erp-ui-ux`

Playwright CLI was documented as a reference but not installed in this alignment because no application target or browser CLI rollout was requested.

## Harness changes

- Added `skills/haku-coagent-erp-ui-ux/SKILL.md`.
- Added `docs/erp-ui-ux.md` with source boundaries and companion matrix.
- Updated README, `.hermes/README.md`, core skill related skills, and validator coverage.
- Kept third-party caches, private profile state, credentials, sessions, and databases out of the repository.

## Exact custom skill parity

`/home/arkhi25/.hermes/skills/haku-coagent-erp-ui-ux/SKILL.md` and
`skills/haku-coagent-erp-ui-ux/SKILL.md` have matching SHA-256:

`48fad24a69c36bd62e3f3b05c585528f89aca84288566dbd68f7413c1d566151`
