# -*- coding: utf-8 -*-
"""Dump question bodies for old 2&3 combined quiz and new ch2/ch3 quizzes."""
import json, io, re, os

def dump(path, label):
    nb = json.load(open(path, encoding="utf-8"))
    cur = None
    out = []
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        src = "".join(cell.get("source", []))
        m = re.search(r"(^#{1,6}\s*题\s*\d+|题\s*\d+[：:.])", src, re.I | re.M)
        if m:
            if cur:
                out.append(cur)
            cur = [m.group(0)[:40], src.strip()[:420]]
        elif cur and src.strip():
            cur[1] += " || " + src.strip()[:200]
    if cur:
        out.append(cur)
    lines = [f"### {label}（{path}，{len(out)} 题）", ""]
    for i, (head, body) in enumerate(out, 1):
        lines.append(f"{i}. **{head}** :: {body.replace(chr(10),' ')[:380]}")
    return lines

res = []
res += dump("../chapter_2_3_quiz/SymPy_SciPy_test_questions.ipynb", "旧题库 2&3 合订")
res += ["", "---", ""]
res += dump("chapters/02-sympy/exercises/quiz.ipynb", "新版 02 SymPy")
res += ["", "---", ""]
res += dump("chapters/03-scipy/exercises/quiz.ipynb", "新版 03 SciPy")
res += ["", ""]
report = "\n".join(res)
with io.open("build/quiz_body_report_23.md", "w", encoding="utf-8") as f:
    f.write(report)
print("written", len(report))
