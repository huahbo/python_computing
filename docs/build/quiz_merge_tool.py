# -*- coding: utf-8 -*-
"""M1.1: inventory questions in old (archived) vs new chapter quizzes."""
import json, os, re, io

OLD = {
    "01": "../chapter_1_quiz/numpy_assignment_final.ipynb",
    "02&03": "../chapter_2_3_quiz/SymPy_SciPy_test_questions.ipynb",
    "04&05": "../chapter_4_5_quiz/pandas_matplotlib_quiz.ipynb",
    "06&07&08": "../chapter_6_7_8_quiz/chapter6_7_8_quiz_30_questions.ipynb",
}
NEW = {
    "01": "chapters/01-numpy/exercises/quiz.ipynb",
    "02": "chapters/02-sympy/exercises/quiz.ipynb",
    "03": "chapters/03-scipy/exercises/quiz.ipynb",
    "04": "chapters/04-pandas/exercises/quiz.ipynb",
    "05": "chapters/05-matplotlib/exercises/quiz.ipynb",
    "06": "chapters/06-networkx/exercises/quiz.ipynb",
    "07": "chapters/07-statsmodels/exercises/quiz.ipynb",
    "08": "chapters/08-sklearn/exercises/quiz.ipynb",
}

def qlist(path):
    if not os.path.exists(path):
        return []
    nb = json.load(open(path, encoding="utf-8"))
    out = []
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        src = "".join(cell.get("source", []))
        first = next((ln.strip() for ln in src.splitlines() if ln.strip()), "")
        if re.match(r"^#{1,6}\s", first) or re.match(r"^(题|Q\d|第\s*\d+\s*题)", first, re.I):
            title = first[:100]
            n = len(out) + 1
            out.append((n, title))
    return out

def md_escape(t):
    return t.replace("|", "\\|").replace("\n", " ")

lines = ["# quiz 合并盘点报告（M1.1）", "",
         "> 由 build/quiz_merge_tool.py 生成。新题为新版 exercises/quiz.ipynb 的标题；旧题为仓库根归档 quiz。",
         "", "## 一、旧题库题目清单", ""]
for key, path in OLD.items():
    qs = qlist(path)
    lines.append(f"### 旧题库（{key}）：{os.path.basename(path)}（{len(qs)} 题）")
    lines.append("")
    for n, t in qs:
        lines.append(f"- {n}. {md_escape(t)}")
    lines.append("")

lines += ["", "## 二、新版各章 quiz 题目清单", ""]
for key, path in NEW.items():
    qs = qlist(path)
    lines.append(f"### 新版（{key}）：{os.path.basename(path)}（{len(qs)} 题）")
    lines.append("")
    for n, t in qs:
        lines.append(f"- {n}. {md_escape(t)}")
    lines.append("")

report = "\n".join(lines) + "\n"
with io.open("build/quiz_merge_report.md", "w", encoding="utf-8") as f:
    f.write(report)
print("report written, chars:", len(report))
print("--- counts ---")
for key, path in OLD.items():
    print("old", key, len(qlist(path)))
for key, path in NEW.items():
    print("new", key, len(qlist(path)))
