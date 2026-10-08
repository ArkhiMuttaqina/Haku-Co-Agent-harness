#!/usr/bin/env python3
"""Conservative secret-safety scan for tracked/source files.

This is a review aid, not a replacement for a dedicated secret scanner.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = [
    ("private-key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
    ("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_\-]{20,}\b")),
    ("aws-access-key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("bearer-token", re.compile(r"\bBearer\s+[A-Za-z0-9._~+/=-]{24,}\b", re.I)),
    ("generic-secret-assignment", re.compile(r"(?i)\b(?:api[_-]?key|secret|password|token)\s*[:=]\s*[\"'](?!CHANGE_ME|YOUR_|REPLACE_|<|\$\{)[^\"']{16,}[\"']")),
]
ALLOW = {".git", ".venv", "venv", "__pycache__"}


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "--cached", "--others", "--exclude-standard"],
        check=True, text=True, capture_output=True,
    )
    return [ROOT / line for line in result.stdout.splitlines() if line]


def main() -> int:
    findings: list[str] = []
    for path in tracked_files():
        if any(part in ALLOW for part in path.parts) or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for name, pattern in PATTERNS:
            if pattern.search(text):
                findings.append(f"{name}: {path.relative_to(ROOT)}")
    if findings:
        print("FAIL: possible secret material detected:")
        print("\n".join(f"- {item}" for item in findings))
        return 1
    print("PASS: no configured secret patterns found in tracked/source files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
