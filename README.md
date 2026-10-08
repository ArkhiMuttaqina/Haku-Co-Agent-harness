# Haku Co-Agent Harness

A governed operating harness for multi-agent software development, QA, security, memory, and delivery.

> HAKU is the orchestrator. Agents do not merely generate code; they work inside an explicit plan, role boundary, evidence contract, and verification gate.

## What this is

Haku Co-Agent Harness packages the reusable parts of an effective Hermes/HAKU workflow:

- role separation for HAKU, Dev, QA, Security, and Ops
- plan/run/evidence continuity across long tasks and context compression
- repo-readable `AGENTS.md` guidance
- safe memory policy without shipping private memory contents
- Telegram war-room behavior and liveness conventions
- QA and security review contracts
- validation and secret-safety checks

## What this is not

This repository intentionally does **not** contain:

- Telegram bot tokens, API keys, OAuth credentials, or private keys
- raw Hermes `state.db`, Mnemosyne databases, session history, or chat transcripts
- personal user memory or private profile state
- production deployment credentials or environment files
- unrelated project-specific incident reports

## Repository layout

```text
AGENTS.md                    # repository-wide agent contract
README.md                    # this overview
CONTRIBUTING.md              # contribution and review workflow
SECURITY.md                  # reporting and secret-safety policy

docs/
  architecture.md            # system boundaries and data ownership
  operating-model.md         # HAKU/Dev/QA/Security/Ops workflow
  memory-policy.md           # durable memory versus private runtime state
  telegram-behavior.md       # reactions, topics, routing, queue semantics

profiles/
├── haku/SOUL.md               # orchestrator identity template
├── dev/SOUL.md                # implementation worker template
├── qa/SOUL.md                 # verification worker template
├── security/SOUL.md           # security reviewer template
└── ops/SOUL.md                # runtime/deployment evidence template

skills/
  haku-coagent-core/          # core execution and evidence contract
  telegram-war-room/          # Telegram behavior contract
  qa-review/                  # QA lane contract
  security-review/            # security lane contract

templates/
  plan.md                     # decision-complete plan template
  state.json                  # compact resume-state template
  ledger.jsonl                # append-only ledger example
  evidence/                   # role evidence directory template

scripts/
  validate.py                 # structure/frontmatter/reference validation
  secret_scan.py              # conservative tracked-file secret scan
  install-skills.sh           # copy curated skills into a target Hermes home

.hermes/
  plans/                      # repo-local plans for this repository
  runs/                       # execution state and evidence for this repository
```

## Quick start

```bash
# Clone
mkdir -p ~/repo
cd ~/repo
git clone https://github.com/ArkhiMuttaqina/Haku-Co-Agent-harness.git
cd Haku-Co-Agent-harness

# Validate the package
python3 scripts/validate.py
python3 scripts/secret_scan.py
```

Both checks are dependency-light and should run with Python 3.10+.

## How a governed task works

1. **Intake:** HAKU clarifies the business outcome, target repo, execution plane, and risk.
2. **Plan:** create one stable `PLAN_ID` under `.hermes/plans/` with scope, owners, acceptance criteria, rollback, and DoD.
3. **Run:** create `.hermes/runs/<PLAN_ID>/state.json`, `ledger.jsonl`, and role evidence folders.
4. **Execute:** Dev implements; QA and Security review their assigned lanes; Ops verifies runtime only when requested.
5. **Reconcile:** HAKU checks exact source identity, test output, evidence, and lifecycle state.
6. **Deliver:** report what changed, what was verified, what remains blocked, and whether anything was committed/pushed/deployed.

## Role model

| Role | Owns | Does not claim |
|---|---|---|
| HAKU | plan, routing, reconciliation, final verdict | deployment without proof |
| Dev | implementation and focused tests | overall completion |
| QA | functional/regression/runtime proof | security approval |
| Security | threat/auth/secrets review | product acceptance alone |
| Ops | environment/deployment evidence | source correctness alone |

## Memory model

The harness ships a **memory policy and examples**, not private memory. Durable facts may be stored in a configured shared memory provider; transient task state belongs in the repo-local plan/run; credentials and session transcripts stay outside Git.

See [`docs/memory-policy.md`](docs/memory-policy.md).

## Telegram model

The optional Telegram surface uses HAKU as the unrestricted orchestrator and workers as mention/reply-gated participants. Reactions are a low-noise liveness surface:

- `👀` observed/targeted
- `🤔` listening but not targeted
- `⚡` processing
- `✅` completed

See [`docs/telegram-behavior.md`](docs/telegram-behavior.md).

## Security posture

Treat this repository as workflow code. Review changes to role boundaries, approval behavior, memory routing, secret handling, and publication scripts with extra care. Never add real credentials to examples or tests.

See [`SECURITY.md`](SECURITY.md).

## Status semantics

Use precise lifecycle labels:

- `planned`: scope exists; no implementation claim
- `changed`: files were modified locally
- `verified`: relevant checks passed against the exact candidate
- `committed`: Git commit exists locally
- `pushed`: remote ref was verified
- `deployed`: artifact was intentionally installed/released
- `runtime-active`: the running process loaded and exercised the candidate

## License

MIT. See [`LICENSE`](LICENSE).
