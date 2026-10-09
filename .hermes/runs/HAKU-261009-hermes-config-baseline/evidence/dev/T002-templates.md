# T002 — templates

Added:

- `templates/hermes/config.common.yaml`
- `templates/hermes/config.haku.yaml`
- `templates/hermes/config.dev1.yaml`

The common file carries the shared recommended operational baseline, including
queue mode, max turns, reasoning effort, compression/LCM, memory, delegation,
Telegram tool progress/streaming, and the complete progress-tail sections.
Overlays keep HAKU free-response and Shiro mention-gated, with distinct labels.

Validation of all three YAML files passed with Python/PyYAML.
