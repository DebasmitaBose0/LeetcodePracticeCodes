#!/usr/bin/env python3
"""Update README.md progress, latest code summary, and problem index for LeetCode solutions."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"

PY_FILES = sorted([p.name for p in ROOT.glob("*.py") if p.name != Path(__file__).name])
SQL_FILES = sorted([p.name for p in ROOT.glob("*.sql")])
TXT_FILES = sorted([p.name for p in ROOT.glob("*.txt")])

TOTAL_PY = len(PY_FILES)
TOTAL_SQL = len(SQL_FILES)
TOTAL_TXT = len(TXT_FILES)

LATEST_PY = sorted(PY_FILES, key=lambda name: (ROOT / name).stat().st_mtime, reverse=True)[:10]
LATEST_SQL = sorted(SQL_FILES, key=lambda name: (ROOT / name).stat().st_mtime, reverse=True)[:5]

text = README.read_text(encoding="utf-8")
pre_latest, sep_latest, post_latest = text.partition("# Latest Codes")
if sep_latest:
    _, sep_repo, post_repo = post_latest.partition("# Repository Layout")
    repo_section = sep_repo + post_repo
else:
    pre_latest, sep_repo, post_repo = text.partition("# Repository Layout")
    repo_section = sep_repo + post_repo

# update snapshot counts in the header
lines = pre_latest.splitlines()
updated_head = []
for line in lines:
    if line.startswith("- Python solution files in this repo:"):
        updated_head.append(f"- Python solution files in this repo: **{TOTAL_PY}**")
    elif line.startswith("- SQL practice files in this repo:"):
        updated_head.append(f"- SQL practice files in this repo: **{TOTAL_SQL}**")
    elif line.startswith("- Text problem files in this repo:"):
        updated_head.append(f"- Text problem files in this repo: **{TOTAL_TXT}**")
    else:
        updated_head.append(line)

latest_section = [
    "# Latest Codes",
    "",
    "Most recent solved problems include:",
    "",
] + [f"- `{name}`" for name in LATEST_SQL + LATEST_PY] + [""]

index_lines = [
    "# Problem Index",
    "",
    "Below is a comprehensive index of all Python solution files in this repository, sorted alphabetically:",
    "",
] + [f" - `{name}`" for name in PY_FILES] + [""]

new_text = "\n".join(updated_head).rstrip() + "\n\n" + "\n".join(latest_section) + "\n" + repo_section.split("# Problem Index", 1)[0].rstrip() + "\n\n" + "\n".join(index_lines)

README.write_text(new_text, encoding="utf-8")
print(f"Updated README.md: {TOTAL_PY} Python solutions indexed, {TOTAL_SQL} SQL files, {TOTAL_TXT} text files.")
