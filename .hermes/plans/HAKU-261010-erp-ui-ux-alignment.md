# HAKU-261010-erp-ui-ux-alignment

## Problem and business intent

Make the reusable Haku Co-Agent harness aware of the supplied ERP/UI/UX workflow and align the active default Hermes profile with practical UI tooling. Arkhi explicitly wants shadcn/ui installed; other popular UI/UX skills are nice-to-have only when the live installer and target semantics are understood.

## Ownership and source boundaries

- Owner: HAKU-direct; no Shiro task is required.
- Canonical workspace: `/home/arkhi25/repo/Haku-Co-Agent-harness`
- Neighboring repositories are out of scope.
- User-supplied source: `/home/arkhi25/.hermes/cache/documents/doc_4c2b580e2cf0_agentic-erp-ui-ux-skills.md` and previously installed local skill `/home/arkhi25/.hermes/skills/haku-coagent-erp-ui-ux/SKILL.md`.
- Official upstream references must be inspected before installing third-party skills.

## Scope

1. Audit live `npx skills`/Hermes skill installation behavior and target directories.
2. Install the official shadcn/ui skill for the default Hermes profile when supported.
3. Optionally install only high-value, broadly applicable UI/UX skills from the supplied references; do not install React-specific guidance unless the target/project scope justifies it.
4. Add the ERP/UI/UX skill to the Haku Co-Agent harness, preserve source attribution/reference URLs, and update the harness index/validation requirements.
5. Verify installed discovery, source parity, repository validators, secret scan, and diff hygiene.

## Out of scope

- No deployment, publication, Git push, release tag, or remote mutation.
- No live application dependency installation inside an application repository.
- No blind `curl | bash`, broad skill ecosystem installation, or profile rollout beyond the default Hermes profile.
- No edits to unrelated repositories or private profile state beyond the requested default skill installation.

## Assumptions and decisions

- The sent ZIP and prior local skill are the canonical custom ERP skill content.
- `shadcn/ui` is required by Arkhi's explicit instruction.
- Vercel web-design guidelines and Playwright are candidates only if the live installer exposes safe, Hermes-discoverable targets. React best practices is deferred unless a React/Next.js project is the target.
- Local harness changes are sufficient for “update repo”; publication remains separately gated.

## Architecture/runtime flow

`agentic-erp-ui-ux-skills.md` references → custom `haku-coagent-erp-ui-ux` skill → Hermes default profile skill discovery; the Haku harness carries a sanitized, versioned copy plus references and validation coverage. Third-party skills remain separately sourced and are not copied into the harness unless their licensing/source boundary is clear.

## Risks and rollback

- Installer may target `.agents/skills` or another CLI-specific directory instead of Hermes. Mitigate by inspecting installer output and Hermes discovery.
- Existing skill name collisions may cause overwrite. Preflight and preserve existing files; do not overwrite without explicit scope.
- Upstream skill content may change. Record source URL/version/commit where available and verify installed path.
- Rollback: remove only newly created bounded skill directories or restore a repo-local file from Git; no broad cleanup.

## Sprint/tasks

### S1 — Discovery and install audit

- T001 [HAKU] Inspect repository, live Hermes version, skills CLI help, install targets, and existing skill state.
- T002 [HAKU] Install shadcn/ui and selected safe UI/UX skills only after source/target audit.

### S2 — Harness alignment

- T003 [HAKU] Add the ERP/UI/UX skill and source references to the Haku harness.
- T004 [HAKU] Update validator/README/index coverage without copying private runtime state.

### S3 — Verification

- T005 [HAKU] Run skill discovery/parity checks, harness validator, secret scan, and diff checks.
- T006 [HAKU] Reconcile plan/run/evidence and final local-only verdict.

## Acceptance criteria

- `shadcn/ui` is installed in a Hermes-supported/default-profile discoverable location, or a precise installer blocker is recorded.
- Any optional skill is installed only with verified source/target semantics and is separately named.
- Harness contains `skills/haku-coagent-erp-ui-ux/SKILL.md` with valid frontmatter and references the supplied workflow without private state.
- README and validator describe the new skill and pass.
- No unrelated repository files are changed; no credentials or runtime databases enter Git.
- Final report distinguishes installed/on-disk, discovered, runtime-active, changed, committed, and pushed states.

## Verification commands

- `hermes --version`
- `hermes skills list` / `hermes skills inspect` as supported
- `npx skills --help`, `npx skills list`, and installer dry-run/inspect options as supported
- `python3 scripts/validate.py`
- `python3 scripts/secret_scan.py`
- `git diff --check` plus untracked-file checks where applicable
- exact file/hash/parity checks for the custom skill

## Definition of Done

HAKU has directly verified the live install/discovery result, repository source and documentation alignment, validators, secret scan, and final Git status. No remote publication is claimed.

## Execution approval

Approved by Arkhi in the current Telegram turn for local installation/alignment only. Publication/push remains unapproved.
