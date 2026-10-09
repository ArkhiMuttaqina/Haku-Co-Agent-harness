#!/usr/bin/env python3
"""Validate the sanitized Haku Co-Agent Harness package."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "AGENTS.md", "CONTRIBUTING.md", "SECURITY.md", "LICENSE",
    ".hermes/README.md", ".env.example",
    "docs/architecture.md", "docs/operating-model.md", "docs/memory-policy.md",
    "docs/telegram-behavior.md",
    "profiles/haku/SOUL.md", "profiles/haku/MEMORY.md",
    "profiles/dev/SOUL.md", "profiles/dev/MEMORY.md",
    "profiles/qa/SOUL.md", "profiles/qa/MEMORY.md",
    "profiles/security/SOUL.md", "profiles/security/MEMORY.md",
    "profiles/ops/SOUL.md", "profiles/ops/MEMORY.md",
    "templates/plan.md", "templates/state.json", "templates/ledger.jsonl",
    "templates/memory.seed.yaml", "templates/evidence/README.md",
    "templates/evidence/ROLE-evidence.md",
    "templates/hermes/config.common.yaml", "templates/hermes/config.haku.yaml",
    "templates/hermes/config.dev1.yaml", "templates/hermes/memory.mnemosyne.yaml",
    "scripts/validate.py", "scripts/secret_scan.py", "scripts/install-skills.sh",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> int:
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            fail(f"missing required file: {rel}")

    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skill_files:
        fail("no curated skills found")

    for path in skill_files:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            fail(f"skill frontmatter must start at byte 0: {path.relative_to(ROOT)}")
        marker = "\n---\n"
        end = text.find(marker, 4)
        if end < 0:
            fail(f"skill frontmatter is not closed: {path.relative_to(ROOT)}")
        frontmatter = text[4:end]
        body = text[end + len(marker):].strip()
        if not body:
            fail(f"skill body is empty: {path.relative_to(ROOT)}")
        fields = dict(re.findall(r"^(name|description|version|author|license):\s*(.+)$", frontmatter, re.MULTILINE))
        for key in ("name", "description"):
            if key not in fields:
                fail(f"skill missing {key}: {path.relative_to(ROOT)}")
        if len(fields["description"]) > 1024:
            fail(f"skill description too long: {path.relative_to(ROOT)}")
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", fields["name"]):
            fail(f"invalid skill name {fields['name']!r}: {path.relative_to(ROOT)}")

    state = json.loads((ROOT / "templates/state.json").read_text(encoding="utf-8"))
    for key in ("plan_id", "status", "phase", "execution_approved", "next_action"):
        if key not in state:
            fail(f"template state missing {key}")
    for line_no, line in enumerate((ROOT / "templates/ledger.jsonl").read_text().splitlines(), 1):
        try:
            json.loads(line)
        except json.JSONDecodeError as exc:
            fail(f"invalid ledger JSON at line {line_no}: {exc}")

    plan = (ROOT / ".hermes/plans/HAKU-261008-harness-bootstrap.md").read_text(encoding="utf-8")
    if "HAKU-261008-harness-bootstrap" not in plan:
        fail("active bootstrap plan is missing its plan ID")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for target in re.findall(r"\]\((?!https?://|#)([^)]+)\)", readme):
        target = target.split("#", 1)[0]
        if target and not (ROOT / target).exists():
            fail(f"README link target missing: {target}")

    print(f"PASS: {len(skill_files)} skills, {len(REQUIRED)} required files, templates and links valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
