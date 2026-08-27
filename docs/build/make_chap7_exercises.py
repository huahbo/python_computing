# -*- coding: utf-8 -*-
"""Build exercises/quiz.ipynb and exercises/answers.ipynb for chapter 07.

Extracts the 10 Statsmodels questions (original quiz题 11-20) from
../chapter_6_7_8_quiz and renumbers them to 题 1-10.
"""
import json, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(BASE, "..", "..", "chapter_6_7_8_quiz"))
QD = os.path.join(SRC, "chapter6_7_8_quiz_30_questions.ipynb")
SD = os.path.join(SRC, "chapter6_7_8_quiz_30_solutions.ipynb")
DST = os.path.normpath(os.path.join(BASE, "..", "chapters", "07-statsmodels", "exercises"))

def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)

def renumber(src, base):
    def repl(m):
        k = int(m.group(1)) - base
        suffix = m.group(2) or ""
        return "## 题 %d%s（" % (k, suffix)
    return re.sub(r"## 题 (\d+)( 解答)?（", repl, src)

def cell(type_, source, outputs=None):
    return {"cell_type": type_, "metadata": {}, "source": source,
            "execution_count": None, "outputs": outputs or []}

def make_nb(out, title, blocks):
    cells = [cell("markdown", "# " + title + "\n")]
    for typ, src in blocks:
        cells.append(cell(typ, src))
    nb = {"cells": cells,
          "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                        "language_info": {"name": "python", "version": "3.13"}},
          "nbformat": 4, "nbformat_minor": 5}
    with open(out, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    return len(cells)

qn = load(QD)
sn = load(SD)

# question cells for 题 11-20: title md, question md, hint md, code cell
q_blocks = []
for i in range(41, 81, 4):
    title = renumber("".join(qn["cells"][i]["source"]), 10)
    q_md = "".join(qn["cells"][i+1]["source"])
    q_md = q_md.replace("第11题", "第1题").replace("第14题", "第4题")
    hint = "".join(qn["cells"][i+2]["source"])
    code_src = "".join(qn["cells"][i+3]["source"])
    q_blocks.append(("markdown", title))
    q_blocks.append(("markdown", q_md))
    q_blocks.append(("markdown", hint))
    q_blocks.append(("code", code_src))

# solution cells for 题 11-20: title md, idea md, code cell
s_blocks = []
for i in range(31, 61, 3):
    title = renumber("".join(sn["cells"][i]["source"]), 10)
    idea = "".join(sn["cells"][i+1]["source"])
    code_src = "".join(sn["cells"][i+2]["source"])
    s_blocks.append(("markdown", title))
    s_blocks.append(("markdown", idea))
    s_blocks.append(("code", code_src))

os.makedirs(DST, exist_ok=True)
nq = make_nb(os.path.join(DST, "quiz.ipynb"),
             "Statsmodels 自测题（第 7 章 exercises / quiz）", q_blocks)
na = make_nb(os.path.join(DST, "answers.ipynb"),
             "Statsmodels 参考答案与解析（第 7 章 exercises / answers）", s_blocks)
print("quiz cells:", nq, "answers cells:", na)
