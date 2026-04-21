#!/usr/bin/env python3
"""Generate a clean README.md for LeetCode solutions with latest progress and a full index."""

from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"

EXCLUDE = {Path(__file__).name}
PY_FILES = sorted([p for p in ROOT.glob("*.py") if p.name not in EXCLUDE], key=lambda p: p.name.lower())
SQL_FILES = sorted(ROOT.glob("*.sql"), key=lambda p: p.name.lower())
TXT_FILES = sorted(ROOT.glob("*.txt"), key=lambda p: p.name.lower())

TOTAL_PY = len(PY_FILES)
TOTAL_SQL = len(SQL_FILES)
TOTAL_TXT = len(TXT_FILES)
TOTAL_FILES = TOTAL_PY + TOTAL_SQL + TOTAL_TXT

ALL_FILES = PY_FILES + SQL_FILES + TXT_FILES
LATEST_FILES = sorted(ALL_FILES, key=lambda p: p.stat().st_mtime, reverse=True)[:20]

latest_lines = []
for file_path in LATEST_FILES:
    modified = datetime.fromtimestamp(file_path.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
    latest_lines.append(f"- `{file_path.name}` — {modified}")

readme_lines = [
    "# LeetCode Practice Codes",
    "",
    "[![LeetCode Profile](https://img.shields.io/badge/LeetCode-Debasmita_Bose-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/u/Debasmita_Bose/)",
    "",
    "A compact and readable archive of LeetCode solutions, focused on algorithms, data structures, and interview-style practice.",
    "",
    "## 🚀 Snapshot",
    "",
    f"- **Last updated:** {datetime.now().strftime('%Y-%m-%d')}",
    f"- **Python solutions:** {TOTAL_PY}",
    f"- **SQL practice files:** {TOTAL_SQL}",
    f"- **Text problem files:** {TOTAL_TXT}",
    f"- **Total files:** {TOTAL_FILES}",
    "- **Status:** actively updated",
    "- **License:** Proprietary (All Rights Reserved)",
    "",
    "## ✨ Latest Work",
    "",
] + latest_lines + [
    "",
    "## 🧠 Skills & Topics",
    "",
    "- Arrays/Strings: sliding window, two pointers, greedy",
    "- Linked Lists: cycle detection, reversal, k-group, random pointer",
    "- Trees/Graphs: traversals, reconstruction, shortest paths",
    "- DP: subsequence, interval, 1D/2D, optimization",
    "- Advanced: binary search, backtracking, matrix simulation, hashing",
    "",
    "## 📁 Repository Notes",
    "",
    "- File format: `<problem_number>. <title>.py`",
    "- SQL solutions: `.sql`",
    "- Extra practice: `.txt`",
    "- Full Python index is tucked below to keep the page clean.",
    "- License: Proprietary (All Rights Reserved)",
    "",
    "## 📜 License",
    "",
    "This repository is proprietary. All rights reserved. See [`LICENSE`](LICENSE) for details.",
    "",
    "<details>",
    f"<summary>🗂 Full Python Problem Index ({TOTAL_PY} files)</summary>",
    "",
] + [f"- `{file_path.name}`" for file_path in PY_FILES] + [
    "",
    "</details>",
    "",
    "---",
    "",
    "*Generated automatically by update_readme.py.*",
]

README.write_text("\n".join(readme_lines).strip() + "\n", encoding="utf-8")
print(f"Updated README.md with {TOTAL_PY} Python solutions, {TOTAL_SQL} SQL files, and {TOTAL_TXT} text files.")
