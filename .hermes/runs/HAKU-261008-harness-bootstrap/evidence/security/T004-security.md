# T004 — security evidence

Review boundary:

- No raw Mnemosyne/state/session database was copied.
- No bot token, provider credential, private key, cookie, or chat transcript was added.
- `.gitignore` excludes runtime databases, sessions, logs, and credential patterns.
- `secret_scan.py` passed against current source files.
- Installer canonicalizes its target, refuses `/`, `/home`, and the current home, refuses existing destination skills, and does not touch runtime state.
- README and docs label behavioral controls as workflow defense in depth rather than a kernel sandbox.

Verdict: PASS for the sanitized bootstrap scope; live runtime security remains out of scope.
