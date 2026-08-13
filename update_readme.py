#!/usr/bin/env python3
"""
Generate an elaborate, beautifully formatted README.md for LeetCode solutions 
with up-to-date metrics, topic breakdowns, latest progress, and interactive index sections.
"""

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
    ("1 - 99", 1, 99),
    ("100 - 199", 100, 199),
    ("200 - 299", 200, 299),
    ("300 - 399", 300, 399),
    ("400 - 499", 400, 499),
    ("500 - 999", 500, 999),
    ("1000 - 1999", 1000, 1999),
    ("2000 - 2999", 2000, 2999),
    ("3000 - 3999", 3000, 3999),
    ("Other / Named", None, None),
]

range_counts = {label: 0 for label, _, _ in RANGE_LABELS}


def problem_range_label(file_name: str):
    number = extract_problem_number(file_name)
    if number is None:
        return "Other / Named"
    if 1 <= number <= 99:
        return "1 - 99"
    if 100 <= number <= 199:
        return "100 - 199"
    if 200 <= number <= 299:
        return "200 - 299"
    if 300 <= number <= 399:
        return "300 - 399"
    if 400 <= number <= 499:
        return "400 - 499"
    if 500 <= number <= 999:
        return "500 - 999"
    if 1000 <= number <= 1999:
        return "1000 - 1999"
    if 2000 <= number <= 2999:
        return "2000 - 2999"
    if 3000 <= number <= 3999:
        return "3000 - 3999"
    return "Other / Named"


for file_path in PY_FILES + JAVA_FILES:
    range_counts[problem_range_label(file_path.name)] += 1

max_range_count = max(range_counts.values()) if range_counts else 1


def make_progress_bar(count, max_val, width=12):
    if max_val == 0:
        return "`░`" * width
    filled = int((count / max_val) * width)
    return f"`{'█' * filled}{'░' * (width - filled)}`"


def get_lang_badge(path: Path):
    ext = path.suffix.lower()
    if ext == ".py":
        return "🐍 Python"
    elif ext == ".java":
        return "☕ Java"
    elif ext == ".sql":
        return "🛢️ SQL"
    elif ext == ".txt":
        return "📄 Text"
    return "📁 Other"


# Format Latest Solved
latest_rows = []
for file_path in LATEST_FILES:
    modified = datetime.fromtimestamp(file_path.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
    lang = get_lang_badge(file_path)
    latest_rows.append(f"| `{file_path.name}` | {lang} | `{modified}` |")

# Format Range Breakdown Rows
range_rows = []
for label, _, _ in RANGE_LABELS:
    cnt = range_counts[label]
    bar = make_progress_bar(cnt, max_range_count)
    range_rows.append(f"| **{label}** | `{cnt}` | {bar} |")

# Build README content
now_str = datetime.now().strftime("%Y-%m-%d")

readme_content = f"""<div align="center">

# ⚡ LEETCODE PRACTICE CODES ⚡

### <sub><i>🚀 A Curated, Production-Grade Repository of Competitive Programming & DSA Solutions</i></sub>

[![LeetCode Profile](https://img.shields.io/badge/LeetCode-Debasmita__Bose-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/Debasmita_Bose/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)](https://www.oracle.com/java/)
[![SQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge)](LICENSE)
[![CI Status](https://img.shields.io/badge/CI-Passing-brightgreen?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/DebasmitaBose0/LeetcodePracticeCodes/actions)

---

</div>

## 🌟 Overview

Welcome to **LeetCode Practice Codes**! This repository serves as a personal archive of solved algorithm problems, optimized data structure implementations, and SQL query practice. It is continuously updated with clean, well-annotated Python, Java, and SQL solutions designed for interview readiness and competitive programming.

---

## 📊 Repository Snapshot & Metrics

| Metric 📌 | Value 🔢 | Status ⚡ |
| :--- | :---: | :---: |
| 🐍 **Python Solutions** | `{TOTAL_PY}` | Active 🟢 |
| ☕ **Java Solutions** | `{TOTAL_JAVA}` | Active 🟢 |
| 🛢️ **SQL Database Queries** | `{TOTAL_SQL}` | Active 🟢 |
| 📄 **Text Notes & Misc** | `{TOTAL_TXT}` | Active 🟢 |
| 📦 **Total Practice Files** | `{TOTAL_FILES}` | Maintained 🚀 |
| 📅 **Last Updated** | `{now_str}` | Sync Complete 🔄 |
| 📜 **License** | Proprietary | All Rights Reserved 🔒 |

---

## 📈 Solution Breakdown by ID Range

| Problem Range 🔢 | Solutions Solved 🧮 | Distribution Visual 📊 |
| :--- | :---: | :--- |
""" + "\n".join(range_rows) + f"""

---

## 🔥 Recently Solved / Updated Work (Top 20)

| Solution File 📄 | Language 💻 | Last Modified ⏱️ |
| :--- | :---: | :--- |
""" + "\n".join(latest_rows) + f"""

---

## 🧠 Algorithmic Domains & Key Techniques

<details open>
<summary><b>💡 Click to view core algorithmic patterns mastered in this repository</b></summary>

<br>

- 🎯 **Arrays & Strings:** Sliding Window, Two Pointers, Monotonic Stack/Queue, Kadane's Algorithm, Prefix Sums.
- 🌲 **Trees & Graphs:** DFS, BFS, Lowest Common Ancestor (LCA), Binary Search Trees (BST), Union-Find (DSU), Dijkstra's & Shortest Path.
- 🧩 **Dynamic Programming (DP):** 1D / 2D DP, Subsequence/Subset Problems, Interval DP, Bitmask DP, Tree DP, Space Optimization.
- ⚡ **Advanced Data Structures:** Segment Trees, Binary Indexed Trees (BIT / Fenwick), Trie, LRU / LFU Caches, Priority Queues.
- 🛢️ **Database & SQL:** Window Functions (`ROW_NUMBER`, `DENSE_RANK`), Multi-Table `JOIN`s, Group Aggregations, Recursive CTEs.

</details>

---

## 🗂️ Interactive Solutions Index

<details>
<summary><b>🐍 Python Solutions ({TOTAL_PY} Files)</b></summary>

<br>

""" + "\n".join([f"- `{p.name}`" for p in PY_FILES]) + f"""

</details>

<details>
<summary><b>☕ Java Solutions ({TOTAL_JAVA} Files)</b></summary>

<br>

""" + "\n".join([f"- `{p.name}`" for p in JAVA_FILES]) + f"""

</details>

<details>
<summary><b>🛢️ SQL Solutions ({TOTAL_SQL} Files)</b></summary>

<br>

""" + "\n".join([f"- `{p.name}`" for p in SQL_FILES]) + f"""

</details>

<details>
<summary><b>📄 Text & Miscellaneous ({TOTAL_TXT} Files)</b></summary>

<br>

""" + "\n".join([f"- `{p.name}`" for p in TXT_FILES]) + f"""

</details>

---

## 🛠️ Automated Maintenance

This repository utilizes an automated script `update_readme.py` to keep problem counts, statistics, and recent activity up to date.

To refresh the README automatically after adding new solutions, run:

```bash
python update_readme.py
```

---

## 📜 License & Citation

This repository is **Proprietary**. All rights reserved. Please refer to [`LICENSE`](LICENSE) for details.

<div align="center">

<sub><i>Crafted with ❤️ by <a href="https://github.com/DebasmitaBose0">Debasmita Bose</a> • Built for continuous learning & interview mastery 🚀</i></sub>

</div>
"""

README.write_text(readme_content.strip() + "\n", encoding="utf-8")
print(
    f"Successfully generated elaborate README.md with {TOTAL_PY} Python solutions, {TOTAL_JAVA} Java solutions, {TOTAL_SQL} SQL files, and {TOTAL_TXT} text files."
)
