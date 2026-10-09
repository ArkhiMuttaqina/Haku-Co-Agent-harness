# T004 — security review

- Templates contain no Telegram tokens, API keys, provider secrets, chat IDs,
  session data, memory databases, or private profile state.
- Provider/model routing stays profile-owned; the common baseline does not
  overwrite credentials or catalogs.
- `plugins.enabled` is documented as an expectation, not proof of runtime
  activation; the live plugin list was separately read back.
- The live backup is outside the repository and was not copied into Git.
