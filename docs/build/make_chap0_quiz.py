# -*- coding: utf-8 -*-
"""Generate Chapter 0 quiz / answers / hidden-answers notebooks (exercises/).

Run: python build/make_chap0_quiz.py
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "chapters", "00-prep", "exercises")
os.makedirs(OUT, exist_ok=True)

def md(src):
    lines = [s + "\n" for s in src] if isinstance(src, list) else [s]
    return {"cell_type": "markdown", "metadata": {}, "source": lines}

def code(src):
    lines = [s + "\n" for s in src] if isinstance(src, list) else [s]
    return {"cell_type": "code", "execution_count": None, "metadata": {},
            "outputs": [], "source": lines}

QUESTIONS = [
    dict(num=1, pts=2,
         prompt=r"写出创建名为 scicomp、Python 3.12 的 conda 环境的命令（包含 -n、python=3.12）。",
         hint=r"提示：conda create -n 环境名 python=版本号 -y",
         ans=r'''_q1_cmd = "conda create -n scicomp python=3.12 -y"''',
         test=r'''# Q1 test (2 points)
try:
    pts = 2
    assert "conda create" in _q1_cmd
    assert "scicomp" in _q1_cmd
    assert "python=3.12" in _q1_cmd
    score = pts; note = "OK"
except Exception as e:
    score = 0; note = str(e)
_GRADES.append((1, score, pts, note))
print("Q1:", score, "/", pts, note)'''),
    dict(num=2, pts=2,
         prompt=r"写出激活该环境的命令。",
         hint=r"提示：conda activate 环境名",
         ans=r'''_q2_cmd = "conda activate scicomp"''',
         test=r'''# Q2 test (2 points)
try:
    pts = 2
    assert "conda activate" in _q2_cmd
    assert "scicomp" in _q2_cmd
    score = pts; note = "OK"
except Exception as e:
    score = 0; note = str(e)
_GRADES.append((2, score, pts, note))
print("Q2:", score, "/", pts, note)'''),
    dict(num=3, pts=2,
         prompt=r"课程提供的环境定义文件名是什么（前面 00-02 提到）？",
         hint=r"提示：.yml 结尾",
         ans=r'''_q3_file = "environment.yml"''',
         test=r'''# Q3 test (2 points)
try:
    pts = 2
    assert "environment" in _q3_file and _q3_file.endswith((".yml", ".yaml"))
    score = pts; note = "OK"
except Exception as e:
    score = 0; note = str(e)
_GRADES.append((3, score, pts, note))
print("Q3:", score, "/", pts, note)'''),
    dict(num=4, pts=2,
         prompt=r"写出“查看当前环境已安装包及版本”的一条命令。",
         hint=r"提示：pip 或 conda 都有",
         ans=r'''_q4_cmd = "pip list"''',
         test=r'''# Q4 test (2 points)
try:
    pts = 2
    assert ("pip list" in _q4_cmd) or ("conda list" in _q4_cmd)
    score = pts; note = "OK"
except Exception as e:
    score = 0; note = str(e)
_GRADES.append((4, score, pts, note))
print("Q4:", score, "/", pts, note)'''),
    dict(num=5, pts=2,
         prompt=r"VS Code 中找不到 scicomp 解释器，第一步应该执行哪个命令面板操作？",
         hint=r"提示：Ctrl+Shift+P → Python: ...",
         ans=r'''_q5_choice = "Python: Select Interpreter"''',
         test=r'''# Q5 test (2 points)
try:
    pts = 2
    assert ("Select Interpreter" in _q5_choice) or ("解释器" in _q5_choice)
    score = pts; note = "OK"
except Exception as e:
    score = 0; note = str(e)
_GRADES.append((5, score, pts, note))
print("Q5:", score, "/", pts, note)'''),
    dict(num=6, pts=2,
         prompt=r"给定 nums = [0,1,2,3,4,5,6,7,8,9]，用切片取出偶数位元素（下标 0,2,4,...）赋值给 _q6_even。",
         hint=r"提示：nums[::2]",
         ans=r'''nums = [0,1,2,3,4,5,6,7,8,9]
_q6_even = nums[::2]''',
         test=r'''# Q6 test (2 points)
try:
    pts = 2
    assert _q6_even == [0, 2, 4, 6, 8]
    score = pts; note = "OK"
except Exception as e:
    score = 0; note = str(e)
_GRADES.append((6, score, pts, note))
print("Q6:", score, "/", pts, note)'''),
    dict(num=7, pts=2,
         prompt=r"scores = [68, 91, 55, 76, 88, 73]；用列表推导式保留 60~89 分并四舍五入，结果赋给 _q7。",
         hint=r"提示：[round(s) for s in scores if 60 <= s <= 89]",
         ans=r'''scores = [68, 91, 55, 76, 88, 73]
_q7 = [round(s) for s in scores if 60 <= s <= 89]''',
         test=r'''# Q7 test (2 points)
try:
    pts = 2
    assert _q7 == [68, 76, 88, 73]
    score = pts; note = "OK"
except Exception as e:
    score = 0; note = str(e)
_GRADES.append((7, score, pts, note))
print("Q7:", score, "/", pts, note)'''),
    dict(num=8, pts=2,
         prompt=r"names=['张三','李四']，avgs=[86.3, 78.0]；用 zip 生成字典赋给 _q8，并用 get 取“王五”的默认值 0 赋给 _q8_default。",
         hint=r"提示：dict(zip(names, avgs))；d.get('王五', 0)",
         ans=r'''names = ['张三', '李四']
avgs = [86.3, 78.0]
_q8 = dict(zip(names, avgs))
_q8_default = _q8.get('王五', 0)''',
         test=r'''# Q8 test (2 points)
try:
    pts = 2
    assert _q8 == {"张三": 86.3, "李四": 78.0}
    assert _q8_default == 0
    score = pts; note = "OK"
except Exception as e:
    score = 0; note = str(e)
_GRADES.append((8, score, pts, note))
print("Q8:", score, "/", pts, note)'''),
    dict(num=9, pts=2,
         prompt=r"写一个安全版本的“默认列表”函数 _q9_f(a, l=None)，并调用两次分别赋给 _q9_a、_q9_b，证明两个调用互不共享列表。",
         hint=r"提示：l = [] if l is None else l",
         ans=r'''def _q9_f(a, l=None):
    l = [] if l is None else l
    l.append(a)
    return l

_q9_a = _q9_f(1)
_q9_b = _q9_f(2)''',
         test=r'''# Q9 test (2 points)
try:
    pts = 2
    assert _q9_a == [1]
    assert _q9_b == [2]
    assert _q9_a is not _q9_b
    score = pts; note = "OK"
except Exception as e:
    score = 0; note = str(e)
_GRADES.append((9, score, pts, note))
print("Q9:", score, "/", pts, note)'''),
    dict(num=10, pts=2,
         prompt=r"写函数 read_float(path)：用 with 打开文件，逐行转 float；无效行 print 行号并跳过；返回有效数值列表。",
         hint=r"提示：try/except ValueError；enumerate(f, 1)",
         ans=r'''def read_float(path):
    vals = []
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            try:
                vals.append(float(line.strip()))
            except ValueError:
                print("跳过第", i, "行")
    return vals''',
         test=r'''# Q10 test (2 points)
try:
    pts = 2
    import tempfile, os
    tmp = os.path.join(tempfile.gettempdir(), "_q10_scores.txt")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("1\nx\n3\n")
    assert read_float(tmp) == [1.0, 3.0]
    score = pts; note = "OK"
except Exception as e:
    score = 0; note = str(e)
_GRADES.append((10, score, pts, note))
print("Q10:", score, "/", pts, note)'''),
    dict(num=11, pts=2,
         prompt=r"names=['张三','李四','王五']，scores=[88, 91, 76]；把 (姓名, 分数) 按分数降序排列，取前 3 赋给 _q11_top3。",
         hint=r"提示：sorted(zip(...), key=..., reverse=True)[:3]",
         ans=r'''names = ['张三', '李四', '王五']
scores = [88, 91, 76]
_q11_top3 = sorted(zip(names, scores), key=lambda x: x[1], reverse=True)[:3]''',
         test=r'''# Q11 test (2 points)
try:
    pts = 2
    assert _q11_top3 == [("李四", 91), ("张三", 88), ("王五", 76)]
    score = pts; note = "OK"
except Exception as e:
    score = 0; note = str(e)
_GRADES.append((11, score, pts, note))
print("Q11:", score, "/", pts, note)'''),
    dict(num=12, pts=3,
         prompt=r"写出一个最小 LaTeX 文档字符串（含 ctexart、\begin{equation} 公式、\includegraphics 插图、注释标明 xelatex 编译），赋值给 _q12_tex。",
         hint=r"提示：\documentclass{ctexart} 开头；公式与插图见 00-05 5.5",
         ans=r'''_q12_tex = r"""
% !TeX program = xelatex
\documentclass{ctexart}
\usepackage{amsmath}
\usepackage{graphicx}
\begin{document}
\begin{equation}
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
\end{equation}
\includegraphics[width=0.6\textwidth]{example.png}
\end{document}
"""''',
         test=r'''# Q12 test (3 points)
try:
    pts = 3
    assert "ctexart" in _q12_tex
    assert "\\begin{equation}" in _q12_tex
    assert "\\includegraphics" in _q12_tex
    assert "xelatex" in _q12_tex.lower()
    score = pts; note = "OK"
except Exception as e:
    score = 0; note = str(e)
_GRADES.append((12, score, pts, note))
print("Q12:", score, "/", pts, note)'''),
    dict(num=13, pts=2,
         prompt=r"编译含中文的 LaTeX 文档必须使用哪个引擎/命令？",
         hint=r"提示：00-05 5.6 节",
         ans=r'''_q13 = "xelatex"''',
         test=r'''# Q13 test (2 points)
try:
    pts = 2
    assert "xelatex" in _q13.lower()
    assert "pdflatex" not in _q13.lower()
    score = pts; note = "OK"
except Exception as e:
    score = 0; note = str(e)
_GRADES.append((13, score, pts, note))
print("Q13:", score, "/", pts, note)'''),
    dict(num=14, pts=2,
         prompt=r"写出两个可在浏览器中使用的在线 LaTeX 编译/写作平台（分开写，放入列表 _q14）。",
         hint=r"提示：00-05 5.2 节",
         ans=r'''_q14 = ["Overleaf", "LoongTeX"]''',
         test=r'''# Q14 test (2 points)
try:
    pts = 2
    joined = " ".join(_q14).lower()
    assert "overleaf" in joined
    assert "loongtex" in joined
    score = pts; note = "OK"
except Exception as e:
    score = 0; note = str(e)
_GRADES.append((14, score, pts, note))
print("Q14:", score, "/", pts, note)'''),
    dict(num=15, pts=2,
         prompt=r"编译报错：! Undefined control sequence. \citep。最常见的原因是什么？（答案写入字符串 _q15）",
         hint=r"提示：\citep 来自参考文献宏包",
         ans=r'''_q15 = "未引入 natbib/biblatex 等参考文献宏包"''',
         test=r'''# Q15 test (2 points)
try:
    pts = 2
    assert ("宏包" in _q15) or ("natbib" in _q15.lower()) or ("biblatex" in _q15.lower()) or ("cite" in _q15.lower())
    score = pts; note = "OK"
except Exception as e:
    score = 0; note = str(e)
_GRADES.append((15, score, pts, note))
print("Q15:", score, "/", pts, note)'''),
]

TITLE = "# 第 0 章 练习 - 提交版（环境+Python+LaTeX）\n\n说明：请按顺序运行所有单元格。每题先在“答案单元”写出你的答案，再运行紧接的“测试单元”。测试会把得分追加到 `_GRADES`，最后运行“成绩汇总”查看总分。\n"
INIT = "# 自动评分初始化\n_GRADES = []\n"
END_MD = "## 成绩汇总\n\n运行下面的单元格查看得分。\n"
END_CODE = '''# 成绩汇总
total = sum(score for _, score, _, _ in _GRADES)
max_total = sum(pts for _, _, pts, _ in _GRADES)
print("总分:", total, "/", max_total)
for q in _GRADES:
    print(q)
'''

def build(answer_mode):
    cells = [md(TITLE.split("\n")), code(INIT.split("\n"))]
    for q in QUESTIONS:
        cells.append(md((f"### 第 {q['num']} 题（{q['pts']} 分）\n\n{q['prompt']}").split("\n")))
        cells.append(md(f"<details><summary>提示（点击展开）</summary>\n\n{q['hint']}\n\n</details>".split("\n")))
        if answer_mode:
            cells.append(md(("<details><summary>答案（点击展开可查看）</summary>\n\n" + "```python\n" + q["ans"] + "\n```\n\n</details>").split("\n")))
        if answer_mode:
            cells.append(code(q["ans"].split("\n")))
        else:
            cells.append(code([f"# 在此单元格实现第 {q['num']} 题的答案", "# ### YOUR ANSWER HERE", ""]))
        cells.append(code(q["test"].split("\n")))
    cells.append(md(END_MD.split("\n")))
    cells.append(code(END_CODE.split("\n")))
    nb = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.12"}},
          "nbformat": 4, "nbformat_minor": 5}
    return nb

def save(name, nb):
    p = os.path.join(OUT, name)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    print("wrote", p)

save("quiz.ipynb", build(False))
save("answers.ipynb", build(True))
save("quiz_hidden_answers.ipynb", build(True))
print("done")
