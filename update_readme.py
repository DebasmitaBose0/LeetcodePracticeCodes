import os
import re
import subprocess

def main():
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f not in ['README.md', 'LICENSE', '.gitignore', 'TODO.md', 'update_readme.py']]

    def sort_key(f):
        m = re.match(r'^(\d+)\.(.*)', f)
        if m:
            return (0, int(m.group(1)), m.group(2).lower())
        return (1, 0, f.lower())

    py_files = sorted([f for f in files if f.endswith('.py') or f.endswith('.PY')], key=sort_key)
    java_files = sorted([f for f in files if f.endswith('.java')], key=sort_key)
    sql_files = sorted([f for f in files if f.endswith('.sql')], key=sort_key)
    txt_files = sorted([f for f in files if f.endswith('.txt')], key=sort_key)
    misc_files = sorted([f for f in files if not (f.endswith('.py') or f.endswith('.PY') or f.endswith('.java') or f.endswith('.sql') or f.endswith('.txt'))], key=sort_key)

    total_practice = len(py_files) + len(java_files) + len(sql_files) + len(txt_files) + len(misc_files)

    ranges = {
        '1 - 99': 0,
        '100 - 199': 0,
        '200 - 299': 0,
        '300 - 399': 0,
        '400 - 499': 0,
        '500 - 999': 0,
        '1000 - 1999': 0,
        '2000 - 2999': 0,
        '3000 - 3999': 0,
        'Other / Named': 0
    }

    for f in py_files + java_files + sql_files + txt_files + misc_files:
        m = re.match(r'^(\d+)\.', f)
        if m:
            num = int(m.group(1))
            if 1 <= num <= 99: ranges['1 - 99'] += 1
            elif 100 <= num <= 199: ranges['100 - 199'] += 1
            elif 200 <= num <= 299: ranges['200 - 299'] += 1
            elif 300 <= num <= 399: ranges['300 - 399'] += 1
            elif 400 <= num <= 499: ranges['400 - 499'] += 1
            elif 500 <= num <= 999: ranges['500 - 999'] += 1
            elif 1000 <= num <= 1999: ranges['1000 - 1999'] += 1
            elif 2000 <= num <= 2999: ranges['2000 - 2999'] += 1
            elif 3000 <= num <= 3999: ranges['3000 - 3999'] += 1
            else: ranges['Other / Named'] += 1
        else:
            ranges['Other / Named'] += 1

    def get_recent():
        cmd = ['git', 'log', '--name-status', '--format=COMMIT:%cd', '--date=format:%Y-%m-%d %H:%M', '-n', '200']
        out = subprocess.check_output(cmd, encoding='utf-8')
        items = []
        seen = set()
        current_date = ''
        for line in out.splitlines():
            if line.startswith('COMMIT:'):
                current_date = line.replace('COMMIT:', '').strip()
            elif line.startswith('A\t') or line.startswith('M\t'):
                parts = line.split('\t')
                fname = parts[1]
                if fname not in ['README.md', 'LICENSE', '.gitignore', 'TODO.md', 'update_readme.py'] and fname not in seen and os.path.exists(fname):
                    seen.add(fname)
                    lang_icon = '🐍 Python'
                    if fname.endswith('.java'): lang_icon = '☕ Java'
                    elif fname.endswith('.sql'): lang_icon = '🛢️ SQL'
                    elif fname.endswith('.txt'): lang_icon = '📄 Text'
                    items.append((fname, lang_icon, current_date))
                    if len(items) == 20:
                        break
        return items

    recent = get_recent()

    max_count = max(ranges.values())
    bars = {}
    for k, v in ranges.items():
        filled = round((v / max_count) * 12) if max_count > 0 else 0
        empty = 12 - filled
        bars[k] = '█' * filled + '░' * empty

    lines = []
    lines.append('<div align="center">')
    lines.append('')
    lines.append('# ⚡ LEETCODE PRACTICE CODES ⚡')
    lines.append('')
    lines.append('### <sub><i>🚀 A Curated, Production-Grade Repository of Competitive Programming & DSA Solutions</i></sub>')
    lines.append('')
    lines.append('[![LeetCode Profile](https://img.shields.io/badge/LeetCode-Debasmita__Bose-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/Debasmita_Bose/)')
    lines.append('[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)')
    lines.append('[![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)](https://www.oracle.com/java/)')
    lines.append('[![SQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)')
    lines.append('[![License](https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge)](LICENSE)')
    lines.append('[![CI Status](https://img.shields.io/badge/CI-Passing-brightgreen?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/DebasmitaBose0/LeetcodePracticeCodes/actions)')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('</div>')
    lines.append('')
    lines.append('## 🌟 Overview')
    lines.append('')
    lines.append('Welcome to **LeetCode Practice Codes**! This repository serves as a personal archive of solved algorithm problems, optimized data structure implementations, and SQL query practice. It is continuously updated with clean, well-annotated Python, Java, and SQL solutions designed for interview readiness and competitive programming.')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## 📊 Repository Snapshot & Metrics')
    lines.append('')
    lines.append('| Metric 📌 | Value 🔢 | Status ⚡ |')
    lines.append('| :--- | :---: | :---: |')
    lines.append(f'| 🐍 **Python Solutions** | `{len(py_files)}` | Active 🟢 |')
    lines.append(f'| ☕ **Java Solutions** | `{len(java_files)}` | Active 🟢 |')
    lines.append(f'| 🛢️ **SQL Database Queries** | `{len(sql_files)}` | Active 🟢 |')
    lines.append(f'| 📄 **Text Notes & Misc** | `{len(txt_files) + len(misc_files)}` | Active 🟢 |')
    lines.append(f'| 📦 **Total Practice Files** | `{total_practice}` | Maintained 🚀 |')
    lines.append('| 📅 **Last Updated** | `2026-09-04` | Sync Complete 🔄 |')
    lines.append('| 📜 **License** | Proprietary | All Rights Reserved 🔒 |')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## 📈 Solution Breakdown by ID Range')
    lines.append('')
    lines.append('| Problem Range 🔢 | Solutions Solved 🧮 | Distribution Visual 📊 |')
    lines.append('| :--- | :---: | :--- |')
    for r_key in ['1 - 99', '100 - 199', '200 - 299', '300 - 399', '400 - 499', '500 - 999', '1000 - 1999', '2000 - 2999', '3000 - 3999', 'Other / Named']:
        lines.append(f'| **{r_key}** | `{ranges[r_key]}` | `{bars[r_key]}` |')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## 🔥 Recently Solved / Updated Work (Top 20)')
    lines.append('')
    lines.append('| Solution File 📄 | Language 💻 | Last Modified ⏱️ |')
    lines.append('| :--- | :---: | :--- |')
    for fname, lang_icon, date in recent:
        lines.append(f'| `{fname}` | {lang_icon} | `{date}` |')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## 🧠 Algorithmic Domains & Key Techniques')
    lines.append('')
    lines.append('<details open>')
    lines.append('<summary><b>💡 Click to view core algorithmic patterns mastered in this repository</b></summary>')
    lines.append('')
    lines.append('<br>')
    lines.append('')
    lines.append("- 🎯 **Arrays & Strings:** Sliding Window, Two Pointers, Monotonic Stack/Queue, Kadane's Algorithm, Prefix Sums.")
    lines.append("- 🌲 **Trees & Graphs:** DFS, BFS, Lowest Common Ancestor (LCA), Binary Search Trees (BST), Union-Find (DSU), Dijkstra's & Shortest Path.")
    lines.append('- 🧩 **Dynamic Programming (DP):** 1D / 2D DP, Subsequence/Subset Problems, Interval DP, Bitmask DP, Tree DP, Space Optimization.')
    lines.append('- ⚡ **Advanced Data Structures:** Segment Trees, Binary Indexed Trees (BIT / Fenwick), Trie, LRU / LFU Caches, Priority Queues.')
    lines.append('- 🛢️ **Database & SQL:** Window Functions (`ROW_NUMBER`, `DENSE_RANK`), Multi-Table `JOIN`s, Group Aggregations, Recursive CTEs.')
    lines.append('')
    lines.append('</details>')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## 🗂️ Interactive Solutions Index')
    lines.append('')
    lines.append('<details>')
    lines.append(f'<summary><b>🐍 Python Solutions ({len(py_files)} Files)</b></summary>')
    lines.append('')
    lines.append('<br>')
    lines.append('')
    for f in py_files:
        lines.append(f'- `{f}`')
    lines.append('')
    lines.append('</details>')
    lines.append('')
    lines.append('<details>')
    lines.append(f'<summary><b>☕ Java Solutions ({len(java_files)} Files)</b></summary>')
    lines.append('')
    lines.append('<br>')
    lines.append('')
    for f in java_files:
        lines.append(f'- `{f}`')
    lines.append('')
    lines.append('</details>')
    lines.append('')
    lines.append('<details>')
    lines.append(f'<summary><b>🛢️ SQL Solutions ({len(sql_files)} Files)</b></summary>')
    lines.append('')
    lines.append('<br>')
    lines.append('')
    for f in sql_files:
        lines.append(f'- `{f}`')
    lines.append('')
    lines.append('</details>')
    lines.append('')
    lines.append('<details>')
    lines.append(f'<summary><b>📄 Text & Miscellaneous ({len(txt_files) + len(misc_files)} Files)</b></summary>')
    lines.append('')
    lines.append('<br>')
    lines.append('')
    for f in txt_files + misc_files:
        lines.append(f'- `{f}`')
    lines.append('')
    lines.append('</details>')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## 🛠️ Automated Maintenance')
    lines.append('')
    lines.append('This repository utilizes an automated script `update_readme.py` to keep problem counts, statistics, and recent activity up to date.')
    lines.append('')
    lines.append('To refresh the README automatically after adding new solutions, run:')
    lines.append('')
    lines.append('```bash')
    lines.append('python update_readme.py')
    lines.append('```')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## 📜 License & Citation')
    lines.append('')
    lines.append('This repository is **Proprietary**. All rights reserved. Please refer to [`LICENSE`](LICENSE) for details.')
    lines.append('')
    lines.append('<div align="center">')
    lines.append('')
    lines.append('<sub><i>Crafted with ❤️ by <a href="https://github.com/DebasmitaBose0">Debasmita Bose</a> • Built for continuous learning & interview mastery 🚀</i></sub>')
    lines.append('')
    lines.append('</div>')
    lines.append('')

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print('README.md generated successfully!')

if __name__ == '__main__':
    main()
