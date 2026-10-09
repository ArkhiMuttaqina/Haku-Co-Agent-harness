# Memory policy

## Principle

Memory is a continuity aid, not an authority bypass and not a replacement for repository evidence.

## Three storage classes

### Durable memory

Store stable user preferences, role mappings, architecture decisions, environment conventions, and reusable workflow rules. Keep entries compact, declarative, and sanitized.

Examples:

- `[workflow] HAKU owns orchestration and final judgment.`
- `[pref] User prefers concise Indonesian, root-cause-first reporting.`
- `[arch] Dev, QA, and Security are separate evidence lanes.`

### Task state

Store full plans, task progress, logs, command output, hashes, and evidence under the repo-local `.hermes/` run. Do not put these in durable memory.

### Private runtime state

Session transcripts, raw Mnemosyne databases, credentials, provider tokens, cookies, personal chat history, and private profile state remain local and are never committed.

## Memory write rules

- Check for an existing or superseded fact before writing.
- Prefer one canonical fact over duplicates.
- Mark uncertain facts as inferred or unknown.
- Never store secrets or raw personal data.
- Do not store temporary progress, commit IDs, issue IDs, PR numbers, or incident logs as durable facts.
- When a durable rule changes, supersede the old rule rather than leaving contradictions.

## Example seeds and profile baselines

- [`../templates/memory.seed.yaml`](../templates/memory.seed.yaml) contains a
  provider-neutral durable-memory seed.
- [`../templates/hermes/memory.mnemosyne.yaml`](../templates/hermes/memory.mnemosyne.yaml)
  contains the sanitized recommended Mnemosyne profile configuration.
- `profiles/*/MEMORY.md` contains role-local durable-memory guidance. These are
  sanitized baselines, not private memory exports.
- `profiles/*/SOUL.md` contains role identity and operating-boundary templates.

All actual databases, canonical user facts, profile identity details, and
private records remain in the configured local runtime/provider.

## Sharing across agents

Use one configured shared memory provider when HAKU, Dev, QA, and Security need the same durable context. Share policy and schema in this repository; share actual memory records only through an authenticated runtime provider.
