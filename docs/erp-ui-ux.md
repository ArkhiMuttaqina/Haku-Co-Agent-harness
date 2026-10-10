# ERP/UI/UX skill lane

This repository carries the reusable HAKU workflow in
[`skills/haku-coagent-erp-ui-ux/SKILL.md`](../skills/haku-coagent-erp-ui-ux/SKILL.md).
The skill is adapted from the supplied `agentic-erp-ui-ux-skills.md` guidance
and the HAKU custom skill package. It is intentionally workflow-focused rather
than a copy of private Hermes profile state.

## Curated companion skills

| Skill | Source | Scope | Default profile status |
|---|---|---|---|
| `shadcn` | [shadcn/ui official skill](https://raw.githubusercontent.com/shadcn-ui/ui/main/skills/shadcn/SKILL.md) | Component discovery, composition, and shadcn project APIs | Installed and enabled |
| `web-design-guidelines` | [Vercel Agent Skills](https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md) | Accessibility and Web Interface Guidelines review | Installed and enabled |
| `frontend-design` | [Anthropic Frontend Design](https://raw.githubusercontent.com/anthropics/claude-code/main/plugins/frontend-design/skills/frontend-design/SKILL.md) | Deliberate visual direction and non-generic design | Installed and enabled |
| Playwright CLI skill | [Playwright docs](https://playwright.dev/agent-cli/skills) | Browser-level interaction and visual verification | Not installed by this alignment |

`react-best-practices` remains opt-in for a React/Next.js application task; it
is not bundled into this harness because the harness itself is not an
application repository. The custom ERP skill remains the HAKU source of truth
for business workflow, domain assumptions, accessibility expectations, and
honest rendered-product verification.

## Installation boundary

Third-party skills are installed through Hermes' native skill installer into
the target Hermes profile. The harness stores the custom ERP skill and stable
upstream references, not third-party caches, credentials, session state, or
profile databases. Presence on disk means installed/on-disk; Hermes discovery
means discoverable; a running session may still need `/reload-skills` or a new
session before it loads newly installed skill content.

## Verification contract

For UI work, report these separately:

- source/repository inspection,
- component and workflow implementation,
- lint/typecheck/build/tests,
- browser interaction and screenshot/visual checks,
- accessibility checks,
- installed/discovered/runtime-active skill state.

Never claim a UI is fully accessible, pixel-perfect, or production-ready from
static source inspection alone.