# Architecture and boundaries

## Goal

The harness is a portable policy/documentation layer around an agent runtime. It defines how work is planned, delegated, verified, and remembered without owning provider credentials or private runtime state.

## Layers

```text
User intent
   |
HAKU orchestration: intake -> plan -> route -> reconcile -> deliver
   |
Role lanes: Dev | QA | Security | Ops
   |
Repo contract: AGENTS.md + skills + .hermes/plan/run/evidence
   |
Runtime adapters: Hermes, Telegram, model providers, memory backend
```

## Source-of-truth boundaries

| Concern | Authority |
|---|---|
| Identity and role | profile `SOUL.md` / runtime profile |
| Compact profile-local durable-memory guidance | profile `MEMORY.md` |
| Repo behavior | `AGENTS.md` and scoped project instructions |
| Reusable procedure | `skills/` |
| Current task plan | `.hermes/plans/<PLAN_ID>.md` |
| Current execution state | `.hermes/runs/<PLAN_ID>/state.json` |
| Append-only events | `.hermes/runs/<PLAN_ID>/ledger.jsonl` |
| Proof | `.hermes/runs/<PLAN_ID>/evidence/<role>/` |
| Durable cross-session rules | configured memory provider |
| Private session/runtime state | local Hermes/Mnemosyne state, never Git |

## Design rule

The harness should remain useful if Hermes, Telegram, or the model provider changes. Keep platform-specific behavior in an adapter/skill and keep governance concepts platform-neutral.

## Trust boundaries

- User authorization is required for publication, deployment, destructive actions, and real-provider side effects.
- Agent-generated plans do not grant authority to mutate external systems.
- QA evidence proves behavior, not security approval.
- Security evidence proves risk review, not product acceptance.
- Runtime health proves process health, not source parity.
