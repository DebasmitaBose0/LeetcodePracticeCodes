#!/usr/bin/env python3
"""Update README.md progress and problem index for LeetCode solutions."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"

PY_FILES = sorted([p.name for p in ROOT.glob("*.py") if p.name != Path(__file__).name])
TOTAL = len(PY_FILES)

intro = README.read_text(encoding="utf-8")
start = intro.split("# Problem Index")[0]

# update progress count only in first block
lines = start.splitlines()
new_lines = []
for line in lines:
    if line.startswith("- Currently contains solutions for"):
        new_lines.append(f"- Currently contains solutions for {TOTAL} LeetCode problems in Python.")
    else:
        new_lines.append(line)

index_lines = [
    "# Problem Index",
    "",
    "Below is a comprehensive index of all Python solution files in this repository, sorted alphabetically:",
    "",
] + [f" - `{name}`" for name in PY_FILES] + [""]

README.write_text("\n".join(new_lines + ["\n".join(index_lines)]), encoding="utf-8")
print(f"Updated README.md: {TOTAL} Python solutions indexed.")
