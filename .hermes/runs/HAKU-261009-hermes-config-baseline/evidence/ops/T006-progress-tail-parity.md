# T006 — progress-tail parity and discovery cleanup

- Default and dev1 active plugin copies report `0.2.12`.
- Byte-level comparison covered 228 non-cache files per profile and found zero
  file-set or content differences.
- The former default `0.2.11` recovery copy was preserved outside plugin
  discovery at:
  `/home/arkhi25/.hermes/backups/hermes-progress-tail-before-parity-20261009T143525Z/`.
- `hermes plugins list --plain --enabled --no-bundled` now emits one enabled
  `hermes-progress-tail 0.2.12` row for each profile.
- Gateway restart was not performed; runtime activation remains separately
  restart-pending.
