# Contributing

Thanks for improving the Haku Co-Agent Harness.

## Before changing files

- Read `AGENTS.md` and the relevant skill under `skills/`.
- Keep the change generic and sanitized; do not add user-specific secrets, chat history, private profile state, or project credentials.
- For multi-step work, create/update one `.hermes/plans/<PLAN_ID>.md` and matching run state.

## Change workflow

1. State the problem and intended behavior.
2. Make the smallest complete change.
3. Add or update validation/tests.
4. Run:

   ```bash
   python3 scripts/validate.py
   python3 scripts/secret_scan.py
   git diff --check
   ```

5. Re-read the complete diff, including untracked files.
6. Summarize changed, verified, and unverified lifecycle states.

## Review lanes

Cross-cutting workflow changes should receive:

- Dev review for correctness and maintainability
- QA review for behavior and regression risk
- Security review for secrets, trust boundaries, permissions, and abuse cases

A single green lane does not replace the others.

## Commits

Use focused, imperative commit messages. Do not bundle unrelated application changes into this repository. Pushes and releases require explicit authorization from the repository owner.
