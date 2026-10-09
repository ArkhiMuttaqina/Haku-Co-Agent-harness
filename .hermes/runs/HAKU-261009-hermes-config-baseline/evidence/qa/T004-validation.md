# T004 — validation

Repository checks:

- `python3 scripts/validate.py` — PASS: 4 skills, 28 required files,
  templates and links valid.
- `python3 scripts/secret_scan.py` — PASS: no configured secret patterns in
  tracked/source files.
- `bash -n scripts/install-skills.sh` — PASS.
- `git diff --check` — PASS.
- Python/PyYAML parse of all three `templates/hermes/*.yaml` — PASS.
- Run `state.json` and every `ledger.jsonl` line parse — PASS.

Live dev1 checks:

- `hermes config check` — exit 0; required Telegram variables present; the
  installed Hermes reports the normal `Config version: 2 -> 33` migration
  notice, which was not applied in this scoped parity change.
- Enabled plugin readback — `hermes-error-transparency`, `hermes-lcm`,
  `hermes-progress-tail`, and `mnemosyne` enabled; bundled Telegram,
  security-guidance, and disk-cleanup are enabled on disk as well.
- `hermes-progress-tail` on-disk parity readback — default and dev1 both
  report version `0.2.12`; 228 non-cache files each; SHA-256 comparison found
  zero file-set or content differences.
- Full installed-plugin pytest run was attempted from the copied profile
  directory: 14 failures / 1806 passed. The failures are not treated as a
  product regression because the profile copy is not a Git checkout (tests
  call `git ls-files`) and several namespace-isolation cases require package
  import semantics absent from this installed layout. One lifecycle/background
  case also exposed host-process/module-state sensitivity. The scoped config,
  YAML, validator, and parity checks remain passing.
- No provider secret values were printed.
