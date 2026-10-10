# T005 — Verification evidence

Candidate: local working tree, HAKU-261010-erp-ui-ux-alignment

## Passed

- `python3 scripts/validate.py`
  - `PASS: 5 skills, 35 required files, templates and links valid`
- `python3 scripts/secret_scan.py`
  - `PASS: no configured secret patterns found in tracked/source files`
- `git diff --check`
  - exit code 0
- Hermes default-profile discovery:
  - `frontend-design` — URL/community/enabled
  - `shadcn` — URL/community/enabled
  - `web-design-guidelines` — URL/community/enabled
  - `haku-coagent-erp-ui-ux` — local/local/enabled
- Custom ERP skill source parity:
  - default Hermes skill and harness copy SHA-256: `48fad24a69c36bd62e3f3b05c585528f89aca84288566dbd68f7413c1d566151`

## Explicit limitation

The first native installer invocation inherited the shell's existing `HERMES_HOME=/home/arkhi25/.hermes/profiles/dev1`, so the three URL skills were installed into `dev1` before HAKU re-ran the installation with the default profile path explicitly pinned. Both profile-local copies are on disk; the default-profile discovery result above is the requested proof. Removal of the bounded `dev1` copies is not performed without a separate destructive-operation approval.

Installed/on-disk and discovery are proven; an already-running conversation may require `/reload-skills` or a fresh session for prompt activation.
