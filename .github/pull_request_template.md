## Summary

<!-- What behavior or documentation changed? -->

## Scope

- [ ] Generic and sanitized
- [ ] No private memory, credentials, or session data added
- [ ] Role boundaries remain explicit

## Verification

```text
python3 scripts/validate.py
python3 scripts/secret_scan.py
git diff --check
```

## Lifecycle state

- [ ] Changed locally
- [ ] Verified
- [ ] Committed
- [ ] Pushed
- [ ] Deployed/runtime-active (only if applicable)

## Review lanes

- Dev:
- QA:
- Security:
