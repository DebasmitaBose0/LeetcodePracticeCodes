#!/usr/bin/env python3
"""Generate a detailed README.md for LeetCode solutions with latest progress and repository metrics."""

from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"
EXCLUDE = {Path(__file__).name}


def extract_problem_number(file_name: str):
    number = ""
    for ch in file_name:
        if ch.isdigit():
            number += ch
        else:
            break
    return int(number) if number else None


def sort_key(path: Path):
    num = extract_problem_number(path.name)
    return (num is None, num or 0, path.name.lower())


PY_FILES = sorted([p for p in ROOT.glob("*.[pP][yY]") if p.name not in EXCLUDE], key=sort_key)
JAVA_FILES = sorted(ROOT.glob("*.java"), key=sort_key)
SQL_FILES = sorted(ROOT.glob("*.sql"), key=sort_key)
TXT_FILES = sorted(ROOT.glob("*.txt"), key=sort_key)

TOTAL_PY = len(PY_FILES)
TOTAL_JAVA = len(JAVA_FILES)
TOTAL_SQL = len(SQL_FILES)
TOTAL_TXT = len(TXT_FILES)
TOTAL_FILES = TOTAL_PY + TOTAL_JAVA + TOTAL_SQL + TOTAL_TXT

ALL_FILES = PY_FILES + JAVA_FILES + SQL_FILES + TXT_FILES
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


for file_path in PY_FILES + JAVA_FILES:
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

snapshot_lines = [
    f"- **Last updated:** {datetime.now().strftime('%Y-%m-%d')}",
    f"- **Python solutions:** {TOTAL_PY}",
]
if TOTAL_JAVA > 0:
    snapshot_lines.append(f"- **Java solutions:** {TOTAL_JAVA}")
snapshot_lines.extend([
    f"- **SQL practice files:** {TOTAL_SQL}",
    f"- **Text problem files:** {TOTAL_TXT}",
    f"- **Total files:** {TOTAL_FILES}",
    "- **Status:** actively updated",
    "- **License:** Proprietary (All Rights Reserved)",
])

readme_lines = [
    "# LeetCode Practice Codes",
    "",
    "[![LeetCode Profile](https://img.shields.io/badge/LeetCode-Debasmita_Bose-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/u/Debasmita_Bose/)",
    "[![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)](https://www.python.org/)",
    "[![License](https://img.shields.io/badge/license-Proprietary-lightgrey)](LICENSE)",
    "[![CI](https://github.com/DebasmitaBose0/LeetcodePracticeCodes/actions/workflows/ci.yml/badge.svg)](https://github.com/DebasmitaBose0/LeetcodePracticeCodes/actions)",
    "",
    "A compact and readable archive of LeetCode solutions, focused on algorithms, data structures, and interview-style practice.",
    "",
    "## 🚀 Snapshot",
    "",
] + snapshot_lines + [
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
    "- File format: `<problem_number>. <title>.py` / `.java`",
    "- SQL solutions: `.sql`",
    "- Extra practice: `.txt`",
    "- Full Python index is tucked below to keep the page clean.",
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
] + [f"- `{file_path.name}`" for file_path in PY_FILES] + [
    "",
    "</details>",
    "",
    "---",
    "",
    "*Generated automatically by update_readme.py.*",
]

README.write_text("\n".join(readme_lines).strip() + "\n", encoding="utf-8")
print(
    f"Updated README.md with {TOTAL_PY} Python solutions, {TOTAL_JAVA} Java solutions, {TOTAL_SQL} SQL files, and {TOTAL_TXT} text files."
)
