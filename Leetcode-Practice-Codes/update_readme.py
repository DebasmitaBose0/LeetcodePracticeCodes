#!/usr/bin/env python3
"""Generate a detailed README.md for LeetCode solutions with latest progress and repository metrics."""

from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"

BANNER = r"""
```
 _                          _    ____                  _       ____            _      
| |    ___  _ __ ___   ___ | |_ / ___| ___ _ __   __ _| | __  / ___| ___  _ __| | ___ 
| |   / _ \| '_ ` _ \ / _ \| __| |  _ / _ \ '_ \ / _` | |/ / | |  _ / _ \| '__| |/ _ \
| |__| (_) | | | | | | (_) | |_| |_| |  __/ | | | (_| |   <  | |_| | (_) | |  | |  __/
|_____|___/|_| |_| |_\___/ \__|\____|\___|_| |_|\__,_|_|\_\  \____|\___/|_|  |_|\___|
```
"""
EXCLUDE = {Path(__file__).name}

def extract_problem_number(file_name: str):
    number = ""
    for ch in file_name:
        if ch.isdigit():
            number += ch
        else:
            break
    return int(number) if number else None


def sort_key(p):
    num = extract_problem_number(p.name)
    return (num is None, num or 0, p.name.lower())

PY_FILES = sorted([p for p in ROOT.glob("*.py") if p.name not in EXCLUDE], key=sort_key)
SQL_FILES = sorted(ROOT.glob("*.sql"), key=sort_key)
TXT_FILES = sorted(ROOT.glob("*.txt"), key=sort_key)

TOTAL_PY = len(PY_FILES)
TOTAL_SQL = len(SQL_FILES)
TOTAL_TXT = len(TXT_FILES)
TOTAL_FILES = TOTAL_PY + TOTAL_SQL + TOTAL_TXT

ALL_FILES = PY_FILES + SQL_FILES + TXT_FILES
LATEST_FILES = sorted(ALL_FILES, key=lambda p: p.stat().st_mtime, reverse=True)[:20]

RANGE_LABELS = [
    "1-99",
    "100-199",
    "200-299",
    "300-399",
    "400-499",
    "500-999",
    "1000-1999",
    "2000-2999",
    "3000-3999",
    "Other",
]

range_counts = {label: 0 for label in RANGE_LABELS}


def problem_range_label(file_name: str):
    number = extract_problem_number(file_name)
    if number is None:
        return "Other"
    if 1 <= number <= 99:
        return "1-99"
    if 100 <= number <= 199:
        return "100-199"
    if 200 <= number <= 299:
        return "200-299"
    if 300 <= number <= 399:
        return "300-399"
    if 400 <= number <= 499:
        return "400-499"
    if 500 <= number <= 999:
        return "500-999"
    if 1000 <= number <= 1999:
        return "1000-1999"
    if 2000 <= number <= 2999:
        return "2000-2999"
    if 3000 <= number <= 3999:
        return "3000-3999"
    return "Other"

for file_path in PY_FILES:
    range_counts[problem_range_label(file_path.name)] += 1

range_summary = [
    f"- **{label}**: {range_counts[label]} solutions"
    for label in RANGE_LABELS
    if range_counts[label] > 0
]

latest_lines = []
for file_path in LATEST_FILES:
    modified = datetime.fromtimestamp(file_path.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
    latest_lines.append(f"- `{file_path.name}` — {modified}")

readme_lines = [
    "# LeetCode Practice Codes",
    "",
] + BANNER.strip("\n").splitlines() + [
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
    "## 📊 Coverage Breakdown",
    "",
] + range_summary + [
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
    "- Full Python index is sequentially numbered below to keep the page clean.",
    "- License: Proprietary (All Rights Reserved)",
    "",
    "## 🛠️ Regenerate README",
    "",
    "Run `python update_readme.py` from the repository root to refresh counts and the latest work section.",
    "",
    "## 📜 License",
    "",
    "This repository is proprietary. All rights reserved. See [`LICENSE`](LICENSE) for details.",
    "",
    "<details>",
    f"<summary>🗂 Full Python Problem Index ({TOTAL_PY} files)</summary>",
    "",
] + [f"{index}. 🧩 `{file_path.name}` — Python solution" for index, file_path in enumerate(PY_FILES, start=1)] + [
    "",
    "</details>",
    "",
    "---",
    "",
    "*Generated automatically by update_readme.py.*",
]

README.write_text("\n".join(readme_lines).strip() + "\n", encoding="utf-8")
print(f"Updated README.md with {TOTAL_PY} Python solutions, {TOTAL_SQL} SQL files, and {TOTAL_TXT} text files.")
