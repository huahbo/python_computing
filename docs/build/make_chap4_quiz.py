# -*- coding: utf-8 -*-
"""Build exercises/quiz.ipynb & answers.ipynb for chapter 04 (Pandas).

Reuse the existing combined pandas+matplotlib quiz from ../chapter_4_5_quiz,
keep only the pandas questions (drop the 5 Matplotlib ones), and renumber.
"""
import json, os

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "chapter_4_5_quiz")
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "chapters", "04-pandas", "exercises")
os.makedirs(OUT, exist_ok=True)
NL = chr(10)

def load(name):
    with open(os.path.join(BASE, name), encoding="utf-8") as f:
        return json.load(f)

def src(c):
    return "".join(c.get("source", []))

quiz = load("pandas_matplotlib_quiz.ipynb")
ans = load("pandas_matplotlib_quiz_answers.ipynb")

remove = set()
for i, c in enumerate(quiz["cells"]):
    if c["cell_type"] == "markdown" and src(c).strip().startswith("### 题"):
        if "matplotlib" in src(c).lower():
            remove.add(i)
            if i + 1 < len(quiz["cells"]):
                remove.add(i + 1)

def renumber(nb):
    new_cells = [c for j, c in enumerate(nb["cells"]) if j not in remove]
    n = 0
    for c in new_cells:
        if c["cell_type"] != "markdown":
            continue
        s = src(c).strip()
        if not s.startswith("### 题 "):
            continue
        # replace the leading question number
        start = len("### 题 ")
        j = start
        while j < len(s) and s[j].isdigit():
            j += 1
        old = s[start:j]
        new = s[:start] + str(n + 1) + s[j:]
        c["source"] = [new + NL]
        n += 1
    return new_cells, n

def patch_title(nb, title, subtitle, total):
    for c in nb["cells"]:
        if c["cell_type"] == "markdown" and src(c).strip().startswith("# "):
            c["source"] = [title + NL, NL, subtitle]
            break
    return nb

quiz_cells, nq = renumber(quiz)
ans_cells, na = renumber(ans)
quiz2 = patch_title({"cells": quiz_cells}, "# Pandas 深度练习（试题）",
    "**说明**：" + NL
    + "- 共有 " + str(nq) + " 道题，覆盖 简单/中等/困难 三个等级；" + NL
    + "- 每题包含：题目描述、隐藏提示（点击展开）、以及供学生填写的代码单元。" + NL
    + "- Python 版本：3.10+；pandas ≥ 2.0。" + NL
    + "- Matplotlib 相关题目已移至第 5 章。" + NL
    + "- 请在每个代码单元处填写代码并运行。" + NL, nq)
ans2 = patch_title({"cells": ans_cells}, "# Pandas 深度练习（参考答案）",
    "本文件包含上述 " + str(na) + " 道题的完整、已测试答案代码。每题前都有简短说明与输出。" + NL + NL
    + "环境：Python 3.10+, pandas, numpy。" + NL, na)

json.dump(quiz2, open(os.path.join(OUT, "quiz.ipynb"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(ans2, open(os.path.join(OUT, "answers.ipynb"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("quiz cells:", len(quiz2["cells"]), "answers cells:", len(ans2["cells"]))
for nb, name in [(quiz2, "quiz"), (ans2, "ans")]:
    mpl = [i for i, c in enumerate(nb["cells"])
           if c["cell_type"] == "markdown" and "matplotlib" in src(c).lower()]
    print(name, "remaining matplotlib markdown cells:", mpl)
