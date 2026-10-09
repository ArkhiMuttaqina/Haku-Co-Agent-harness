# T007 — sanitized SOUL/MEMORY and Mnemosyne baseline

Added public-safe role profile baselines:

- `profiles/*/SOUL.md` — role identity, operating boundaries, and completion semantics.
- `profiles/*/MEMORY.md` — durable-memory guidance for each role.
- `templates/hermes/memory.mnemosyne.yaml` — recommended Mnemosyne settings:
  global scope, profile isolation disabled, auto-sleep threshold, sync role, and
  bounded reflection settings.

The HAKU SOUL baseline includes the co-agent plan/run/evidence contract and
hard destructive-operation boundaries without user-specific bot handles,
credentials, chat IDs, private paths, or raw memory.

The MEMORY files intentionally contain policy and durable workflow facts only.
They do not contain canonical user records, session history, logs, tokens,
private profile exports, or Mnemosyne databases.
