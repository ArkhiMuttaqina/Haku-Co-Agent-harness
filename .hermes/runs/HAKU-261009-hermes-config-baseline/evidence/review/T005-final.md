# T005 — final review

Status: local implementation and verification complete; runtime activation
pending.

- Shared config and progress-tail parity is present in sanitized templates.
- Live dev1 has the recommended reasoning setting and available HAKU baseline
  plugins enabled on disk.
- `hermes-progress-tail` is now byte-identical on disk for default and dev1 at
  version `0.2.12`; the previous default `0.2.11` copy was preserved at
  `/home/arkhi25/.hermes/backups/hermes-progress-tail-before-parity-20261009T143525Z/`.
- Role boundaries remain intact: HAKU free-response, Shiro mention-gated;
  labels remain `Hermes` and `Shiro`.
- Config rollback backup exists at
  `/home/arkhi25/.hermes/profiles/dev1/backups/config-before-haku-baseline-20261009T132810Z.yaml`.
- Both gateway services are `active`, but their main processes predate these
  changes (`hermes-gateway` PID 505105 since 2026-10-03; `hermes-gateway-dev1`
  PID 6693 since 2026-09-21). No gateway restart was performed, so runtime
  activation and Telegram behavior are not claimed as refreshed.
- Git publication was not requested and was not performed.
