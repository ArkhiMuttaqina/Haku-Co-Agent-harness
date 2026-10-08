# T003 — validation evidence

Commands and results:

```text
python3 scripts/validate.py
PASS: 4 skills, 25 required files, templates and links valid

python3 scripts/secret_scan.py
PASS: no configured secret patterns found in tracked/source files

bash -n scripts/install-skills.sh && git diff --check
PASS

git diff --no-index --check /dev/null templates/plan.md
PASS

git diff --no-index --check /dev/null templates/evidence/ROLE-evidence.md
PASS

isolated clean install into /tmp/haku-harness-install.*
PASS: four curated skills installed

isolated pre-existing destination test
PASS: preflight rejected existing skill without partial install

protected target test
PASS: /home rejected
```

No real Hermes home, gateway, Telegram bot, or model provider was touched.
