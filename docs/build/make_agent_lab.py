# -*- coding: utf-8 -*-
"""Generate lab.ipynb for chapter 11 (three-part lab; Part A runs offline)."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "chapters", "11-agent-cases", "lab", "lab.ipynb")
cells = []

def md(text):
    cells.append({"cell_type": "markdown", "metadata": {}, "source": text})

def code(text):
    cells.append({"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": text})

md("""# 第二部分 上机实验（lab）

**三段式**：Part A 离线（无网络、无 API Key 也能完成）→ Part B 联网（用 dsh 完成三个任务）→ Part C 综合（项目骨架与报告）。

**提交**：Part A 的审查结论与你的断言、Part B 的提示词与产物、Part C 的项目目录与报告 PDF、AI 使用声明。""")

md("""## Part A 离线：环境、复现与审查（约 1 小时）

> 这一部分不需要网络与 API Key：数据与参考产物都在 lab/ 里。""")

code("""# A0 环境与路径自检
import os, sys
import numpy as np, pandas as pd

BASE = "chapters/11-agent-cases/lab"
DATA = os.path.join(BASE, "data")
OUT = os.path.join(BASE, "output")
os.makedirs(OUT, exist_ok=True)

print("Python:", sys.version.split()[0])
print("当前目录:", os.getcwd())
assert os.path.isdir(DATA), "找不到 lab/data，请在 docs/ 目录下运行本 notebook"
print("data/ 内容:", sorted(os.listdir(DATA)))""")

code("""# A1 读数据：干净版与脏版
clean = pd.read_csv(os.path.join(DATA, "scores.csv"))
dirty = pd.read_csv(os.path.join(DATA, "scores_dirty.csv"))
print("干净数据:", clean.shape, list(clean.columns))
print("脏数据:", dirty.shape)
print(dirty.head(3).to_string(index=False))""")

md("""### A2 复现参考产物

sample_agent_output/scores_fixed.py 是一次真实运行的修复产物。运行它，确认输出与案例一中的记录一致。""")

code("""# A2 运行参考实现（离线）
import subprocess
p = subprocess.run([sys.executable, os.path.join("sample_agent_output", "scores_fixed.py")],
                   cwd=BASE, capture_output=True, text=True, encoding="utf-8", errors="replace",
                   env=dict(os.environ, PYTHONIOENCODING="utf-8"))
print("exit code:", p.returncode)
print(p.stdout[-700:])
assert p.returncode == 0, "参考实现应当运行成功"
assert "自检通过" in p.stdout, "参考实现应当打印自检结果"
print("A2 完成")
""")

md("""### A3 你来写三条断言（TODO）

要求：为「每个学生的平均分」写三条断言（形状、数值、取值范围），使错误实现（scores.mean(axis=0)）无法通过。""")

code("""# A3 TODO：在 check_student_mean 里补三条 assert
scores = clean[["平时", "期中", "期末"]].to_numpy(dtype=float)

def check_student_mean(m):
    m = np.asarray(m)
    # TODO: 在这里写三条 assert（形状 / 数值 / 取值范围）
    return True

correct = scores.mean(axis=1)
wrong = scores.mean(axis=0)
try:
    assert check_student_mean(correct) is True
    print("正确实现：通过")
except AssertionError as e:
    print("正确实现被误拦：", e)
try:
    check_student_mean(wrong)
    print("错误实现也通过了 —— 说明断言还不严，继续补")
except AssertionError as e:
    print("错误实现被拦住：", e)""")

code("""# A4 审查一次真实会话（离线）
p = os.path.join(BASE, "sample_agent_output", "run_fix_session.txt")
text = open(p, encoding="utf-8").read()
print("会话长度:", len(text), "字符")
for kw in ["axis=0", "axis=1", "assert", "归一化"]:
    print("关键词", kw, "出现次数:", text.count(kw))
i = text.find("assert")
print("---- 片段 ----")
print(text[i - 200:i + 300] if i > 0 else text[:400])""")

md("""**A4 要回答的三个问题**（写进提交的审查结论）：

1. Agent 提出了哪几处问题？各自的证据是什么？
2. 它有没有「先读文件再下结论」？举一处证据。
3. 它的自检断言能拦住错误实现吗？为什么？""")

code("""# A5 脏数据核查（为案例二做准备）
dups = int(dirty["学号"].astype(str).str.strip().duplicated().sum())
missing = dirty.isna().sum().to_dict()
outlier = dirty.loc[dirty["期末"] > 100, ["学号", "姓名", "期末"]].to_dict("records")
print("重复学号:", dups)
print("缺失统计:", missing)
print("异常值行:", outlier)
print("清洗后应有行数:", len(dirty) - dups)""")

md("""---

## Part B 联网：用 dsh 完成三个任务（约 2 小时）

> 需要 API Key。每个任务按「任务卡 → 提示词 → 产物 → 验证 → 记录」五步走，失败尝试也要记录。

| 任务 | 目标 | 关键判据 |
| ---- | ---- | ---- |
| B1 修 bug | 修复 data/scores_buggy.py 的两处静默错误，产出 output/scores_fixed.py | 形状 (8,)；逐列归一化 min=0/max=1；加权第一为王五 |
| B2 清洗出图 | 清洗 data/scores_dirty.csv，输出干净数据、箱线图与清洗报告 | 行数守恒 11 → 10；缺失策略留痕；图有标题与单位 |
| B3 可复现实验 | 对 data/sensor.csv 做趋势检验并写报告 | 重跑一致；给出斜率/区间/R²；含局限一节 |

**提示词模板**（方括号换成你的内容）：

【目标】[一句话]
【约束】只改 output/ 下的文件，不动 data/ 原始数据。
【验收标准】[至少两条可执行判据]
【证据】运行输出 + 断言结果
【复核】我会检查[你要看什么]

**记录要求**：每个任务一行（模型 / 时段 / 耗时 / 花费 / 人工修改 / 结论），格式见第 11 章 06 节。""")

md("""---

## Part C 综合：项目骨架与报告（约 1 小时）

把 B1–B3 的产物整理成一个可提交的小项目，并写报告（可复用期末大作业模板）。""")

code("""# C1 生成项目骨架（全部写在 lab/output/ 下，该目录已在 .gitignore 中）
proj = os.path.join(OUT, "agentproj")
for sub in ["src", "output", "report"]:
    os.makedirs(os.path.join(proj, sub), exist_ok=True)

agents_md = os.path.join(proj, "AGENTS.md")
if not os.path.exists(agents_md):
    lines = [
        "# 项目说明（示例，请按你的项目修改）",
        "本项目是《Python 科学计算》第二部分的上机项目。",
        "",
        "# 环境",
        "- Python 3.12；依赖 numpy / pandas / scipy / statsmodels / scikit-learn / matplotlib",
        "",
        "# 约定",
        "- 原始数据只读；输出一律写到 output/",
        "- 随机过程固定种子 np.random.default_rng(42)",
        "- 每个脚本末尾要有 assert 自检",
        "",
        "# 安全",
        "- 删除/批量替换/安装依赖/联网前必须先问",
        "- 不读取 .credentials.yaml / .env",
        "",
    ]
    open(agents_md, "w", encoding="utf-8").write(chr(10).join(lines))
print("项目骨架:", proj)
print(sorted(os.listdir(proj)))
print(open(agents_md, encoding="utf-8").read()[:180])""")

code("""# C2 报告自检清单（逐条打勾后再提交）
checklist = [
    "报告含数据、方法、结果、局限、AI 使用声明五节",
    "每个结论都有对应输出文件（output/ 内可查）",
    "图有标题与单位，中文无乱码",
    "说明了异常值与缺失值的处理策略",
    "报告由 LaTeX 编译为 PDF，且一次编译通过",
    "附会话记录与实验记录表",
]
for i, item in enumerate(checklist, 1):
    print("%d. [ ] %s" % (i, item))""")

md("""---

## 提交清单

1. quiz.ipynb（10 题全部通过）；
2. Part A：A4 三问的审查结论 + 你自己写的断言（A3）；
3. Part B：三个任务的产物与记录表；
4. Part C：项目目录 lab/output/agentproj/ 与报告 PDF；
5. AI 使用声明。""")

nb = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
      "language_info": {"name": "python", "version": "3.12"}}, "nbformat": 4, "nbformat_minor": 5}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)
print("saved", OUT, "cells:", len(cells))
