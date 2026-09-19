# -*- coding: utf-8 -*-
"""Generate exercises/quiz.ipynb and answers.ipynb for chapter 11 (第二部分 练习)."""
import json, os

NL = chr(10)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "chapters", "11-agent-cases", "exercises")

def md(nb, text):
    nb.append({"cell_type": "markdown", "metadata": {}, "source": text})

def code(nb, text):
    nb.append({"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": text})

def notebook(cells):
    return {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.12"}}, "nbformat": 4, "nbformat_minor": 5}

def J(*lines):
    return NL.join(lines)

INTRO = J(
    "# 第二部分 自测题（AI Agent 编程）",
    "",
    "**说明**：共 10 题，覆盖第 9–12 章。每题先阅读题目，再在代码单元里把 TODO 补全，**运行自检单元**；全部通过即完成。",
    "答案版见 `answers.ipynb`。建议顺序：学完第 9、10 章做 1–4 题；学完案例后做 5–8 题；做完 lab 后做 9–10 题。",
    "",
    "**环境**：Python 3.10+，numpy / pandas / scikit-learn（与课程环境一致）。",
)

Q = []
# 1
Q.append((J("## 第 1 题（概念）：Agent 循环的五个动作与终止条件", "", "按顺序写出一次 Agent 循环的五个动作（每项一个字，如 "读"），并写出一句话说明循环什么时候结束。", "", "<details><summary>提示</summary>", "", "- 五个动作分别是：读、想、做、看、判；", "- 终止条件不是"代码能跑"，而是某个由人定义的判据。", "</details>"),
 J("# 第 1 题：TODO", "loop_steps = []        # 例：["读", "想", ...]", "stop_condition = ""     # 一句话", "", "# ---- 自检（不要修改）----", "assert loop_steps == ["读", "想", "做", "看", "判"], "五个动作或顺序不对"", "assert "验收标准" in stop_condition, "终止条件里要提到验收标准"", "print("第 1 题通过")"),
 J("# 第 1 题：参考答案", "loop_steps = ["读", "想", "做", "看", "判"]", "stop_condition = "满足人给定的验收标准时结束，而不是代码能跑就算结束"", "", "assert loop_steps == ["读", "想", "做", "看", "判"]", "assert "验收标准" in stop_condition", "print("第 1 题通过")")))
# 2
Q.append((J("## 第 2 题（概念）：斜杠命令与普通对话的区别", "", "补全下面的字典，说明三条常用命令的用途（用途写关键词即可）。", "", "<details><summary>提示</summary>", "", "- 斜杠命令在本地执行，不进入模型上下文；", "- 三条命令：压缩上下文、导出会话、切换权限。", "</details>"),
 J("# 第 2 题：TODO", "commands = {", "    "/compact": "",      # 做什么", "    "/export": "",       # 做什么", "    "/permission": "",   # 做什么", "}", "local_only = None      # True 或 False：斜杠命令是否会进入模型上下文", "", "# ---- 自检 ----", "assert len(commands) == 3", "assert "压缩" in commands["/compact"]", "assert "导出" in commands["/export"] or "下载" in commands["/export"]", "assert "权限" in commands["/permission"]", "assert local_only is False, "斜杠命令不进入模型上下文"", "print("第 2 题通过")"),
 J("# 第 2 题：参考答案", "commands = {", "    "/compact": "压缩较早的会话历史，省上下文",", "    "/export": "把会话日志打包下载，作为作业附件",", "    "/permission": "切换权限档位（只读 / 工作区写 / 全盘）",", "}", "local_only = False", "", "assert "压缩" in commands["/compact"]", "assert "下载" in commands["/export"]", "assert "权限" in commands["/permission"]", "assert local_only is False", "print("第 2 题通过")")))
# 3
Q.append((J("## 第 3 题（概念）：权限三档与适用场景", "", "把三个档位与最合适的场景连起来（用字典表示：档位 -> 场景关键词）。", "", "<details><summary>提示</summary>", "", "- read-only：第一次接触陌生项目；", "- workspace-write：日常开发（推荐默认）；", "- danger-full-access：受控沙箱/一次性脚本环境。", "</details>"),
 J("# 第 3 题：TODO", "tiers = {", "    "read-only": "",", "    "workspace-write": "",", "    "danger-full-access": "",", "}", "", "# ---- 自检 ----", "assert "解释" in tiers["read-only"] or "陌生" in tiers["read-only"]", "assert "日常" in tiers["workspace-write"] or "作业" in tiers["workspace-write"]", "assert "沙箱" in tiers["danger-full-access"] or "一次性" in tiers["danger-full-access"]", "print("第 3 题通过")"),
 J("# 第 3 题：参考答案", "tiers = {", "    "read-only": "第一次接触陌生项目，只让它解释代码",", "    "workspace-write": "日常开发与课程作业（推荐默认）",", "    "danger-full-access": "受控沙箱或一次性脚本环境，慎用",", "}", "", "assert "陌生" in tiers["read-only"]", "assert "日常" in tiers["workspace-write"]", "assert "沙箱" in tiers["danger-full-access"]", "print("第 3 题通过")")))
# 4
Q.append((J("## 第 4 题（概念）：上下文压缩后要保留什么", "", "写出压缩（compaction）后最值得保留的三类信息。", "", "<details><summary>提示</summary>", "", "- 目标与约束；", "- 结论与证据；", "- 最近几轮对话/下一步。", "</details>"),
 J("# 第 4 题：TODO", "keep = []   # 三类信息", "", "# ---- 自检 ----", "assert len(keep) == 3, "写三类"", "text = "".join(keep)", "assert ("目标" in text) or ("约束" in text)", "assert ("证据" in text) or ("结论" in text)", "assert ("下一步" in text) or ("最近" in text)", "print("第 4 题通过")"),
 J("# 第 4 题：参考答案", "keep = ["目标与验收标准", "结论与关键证据", "最近的对话与下一步"]", "", "text = "".join(keep)", "assert len(keep) == 3 and "目标" in text and "证据" in text and "下一步" in text", "print("第 4 题通过")")))
# 5
Q.append((J("## 第 5 题（审查）：找出 agent 产出里的错误", "", "下面是一段"AI 写的"代码。它想算**每个学生**的平均分。请改成正确写法（只改需要改的行）。", "", "```python", "scores = np.array([[82, 90, 78], [60, 65, 70], [95, 88, 92], [70, 72, 68]], dtype=float)", "student_mean = scores.mean(axis=0)   # 这里有问题", "```", "", "<details><summary>提示</summary>", "", "- 形状才是第一判据：想要 4 个数还是 3 个数？", "</details>"),
 J("# 第 5 题：TODO（把下面两行改成正确实现）", "import numpy as np", "scores = np.array([[82, 90, 78], [60, 65, 70], [95, 88, 92], [70, 72, 68]], dtype=float)", "student_mean = scores.mean(axis=0)   # TODO: 改成正确的 axis", "", "# ---- 自检 ----", "assert student_mean.shape == (4,), "形状应为 (4,)"", "assert np.allclose(student_mean, [83.33, 65.0, 91.67, 70.0], atol=0.01)", "print("第 5 题通过")"),
 J("# 第 5 题：参考答案", "import numpy as np", "scores = np.array([[82, 90, 78], [60, 65, 70], [95, 88, 92], [70, 72, 68]], dtype=float)", "student_mean = scores.mean(axis=1)", "", "assert student_mean.shape == (4,)", "assert np.allclose(student_mean, [83.33, 65.0, 91.67, 70.0], atol=0.01)", "print("第 5 题通过")")))
# 6
Q.append((J("## 第 6 题（审查）：为什么不能 fillna(mean)", "", "数据里有一处异常值（期末 = 999）。下面这段处理有问题，请写出正确的处理策略。", "", "```python", "df["期末"] = df["期末"].fillna(df["期末"].mean())   # 有问题", "```", "", "<details><summary>提示</summary>", "", "- 异常值应当**先标记再决策**，而不是被平均值掩盖；", "- 策略要留痕（写进报告）。", "</details>"),
 J("# 第 6 题：TODO", "strategy = ""         # 一句话：异常值怎么处理", "must_record = None    # True 或 False：处理策略是否要写进报告", "", "# ---- 自检 ----", "assert ("标记" in strategy) or ("缺失" in strategy)", "assert "掩盖" not in strategy", "assert must_record is True", "print("第 6 题通过")"),
 J("# 第 6 题：参考答案", "strategy = "先把大于 100 的值标记为缺失，再在报告中说明缺失比例与后续处理方式"", "must_record = True", "", "assert "标记" in strategy and must_record is True", "print("第 6 题通过")")))
# 7
Q.append((J("## 第 7 题（审查）：补全任务卡", "", "把任务卡六件套补全（键名固定）。", "", "<details><summary>提示</summary>", "", "- 六件套：目标、约束、验收标准、证据、复核、提交。", "</details>"),
 J("# 第 7 题：TODO", "card = {", "    "目标": "",", "    "约束": "",", "    "验收标准": "",", "    "证据": "",", "    "复核": "",", "    "提交": "",", "}", "", "# ---- 自检 ----", "assert set(card.keys()) == {"目标", "约束", "验收标准", "证据", "复核", "提交"}", "assert len(card["验收标准"]) >= 8, "验收标准要写具体，不能只有两个字"", "assert all(len(v) > 0 for v in card.values()), "每一项都要填"", "print("第 7 题通过")"),
 J("# 第 7 题：参考答案", "card = {", "    "目标": "修复 scores_buggy.py 的两处错误并补自检",", "    "约束": "只新增 scores_fixed.py，不改 data/ 下原始文件",", "    "验收标准": "平均分形状为 (8,)；归一化逐列 min=0 / max=1；加权第一为王五",", "    "证据": "运行输出 + 三条 assert 通过",", "    "复核": "是否动原始数据、是否逐列、排名是否真排序",", "    "提交": "脚本 + 输出 + 会话记录",", "}", "", "assert set(card.keys()) == {"目标", "约束", "验收标准", "证据", "复核", "提交"}", "assert all(len(v) > 0 for v in card.values())", "print("第 7 题通过")")))
# 8
Q.append((J("## 第 8 题（审查）：把结论改写成合规表述", "", "下面这句话有问题，请改写（不得出现"证明""导致"）。", "", "> 这段实验证明了温度升高导致了设备故障。", "", "<details><summary>提示</summary>", "", "- 观测数据通常只能支持"相关/一致"；", "- 要写清不确定性与局限。", "</details>"),
 J("# 第 8 题：TODO", "conclusion = ""    # 改写后的一句话", "", "# ---- 自检 ----", "assert "证明" not in conclusion and "导致" not in conclusion", "assert ("相关" in conclusion) or ("一致" in conclusion) or ("提示" in conclusion)", "assert len(conclusion) >= 12", "print("第 8 题通过")"),
 J("# 第 8 题：参考答案", "conclusion = "观测数据与"温度升高时故障率上升"这一假设一致，但样本有限，尚不能排除其他因素，需进一步实验验证"", "", "assert "证明" not in conclusion and "导致" not in conclusion", "assert "一致" in conclusion", "print("第 8 题通过")")))
# 9
Q.append((J("## 第 9 题（实操）：写三条断言卡住这个 bug", "", "为下面的函数写 3 条 assert，使得**错误实现**（把每个学生平均分算成每门课平均分）无法通过。", "", "<details><summary>提示</summary>", "", "- 形状、数值、长度各一条。", "</details>"),
 J("# 第 9 题：TODO（在 check 里补三条 assert）", "import numpy as np", "scores = np.array([[82, 90, 78], [60, 65, 70], [95, 88, 92], [70, 72, 68]], dtype=float)", "", "def check(student_mean):", "    student_mean = np.asarray(student_mean)", "    # TODO: 在这里写三条 assert", "    return True", "", "# ---- 自检（不要修改）----", "assert check(scores.mean(axis=1)) is True, "正确实现应当通过"", "bad = scores.mean(axis=0)", "try:", "    check(bad)", "    raise AssertionError("错误实现竟然通过了，说明断言不严")", "except AssertionError as e:", "    assert "断言不严" not in str(e)", "print("第 9 题通过")"),
 J("# 第 9 题：参考答案", "import numpy as np", "scores = np.array([[82, 90, 78], [60, 65, 70], [95, 88, 92], [70, 72, 68]], dtype=float)", "", "def check(student_mean):", "    student_mean = np.asarray(student_mean)", "    assert student_mean.shape == (4,), "每个学生一个平均分"", "    assert np.allclose(student_mean, scores.mean(axis=1)), "数值与手算不一致"", "    assert student_mean.min() >= 60 and student_mean.max() <= 100, "分数超出合理范围"", "    return True", "", "assert check(scores.mean(axis=1)) is True", "try:", "    check(scores.mean(axis=0))", "    raise AssertionError("错误实现竟然通过了")", "except AssertionError as e:", "    assert "竟然" not in str(e)", "print("第 9 题通过")")))
# 10
Q.append((J("## 第 10 题（实操）：写一份 AI 使用声明", "", "按第 10 章 04 节的模板，补全下面字典（每条都要具体）。", "", "<details><summary>提示</summary>", "", "- 工具与版本、使用环节、关键提示词、人工修改、验证方式、未使用 AI 的部分。", "</details>"),
 J("# 第 10 题：TODO", "statement = {", "    "工具与版本": "",", "    "使用环节": "",", "    "关键提示词": "",", "    "人工修改": "",", "    "验证方式": "",", "    "未使用 AI 的部分": "",", "}", "", "# ---- 自检 ----", "assert set(statement.keys()) == {"工具与版本", "使用环节", "关键提示词", "人工修改", "验证方式", "未使用 AI 的部分"}", "assert all(len(v) >= 6 for v in statement.values()), "每一项都要写具体"", "assert "dsh" in statement["工具与版本"].lower() or "DeepSeek" in statement["工具与版本"]", "print("第 10 题通过")"),
 J("# 第 10 题：参考答案", "statement = {", "    "工具与版本": "DeepSeek Harness 0.1.5-rc.2，模型 deepseek-flash，2026-09-19",", "    "使用环节": "代码调试与断言编写（案例一）",", "    "关键提示词": "修复每个学生平均分的 axis 错误，并给出三条断言（见会话记录）",", "    "人工修改": "调整了异常值策略（标记而非填充）、补充了排名输出、复核了归一化逐列",", "    "验证方式": "运行三条 assert；与手算平均值对照；检查 git diff 未改动 data/",", "    "未使用 AI 的部分": "问题定义、结论与报告正文",", "}", "", "assert all(len(v) >= 6 for v in statement.values())", "assert "DeepSeek" in statement["工具与版本"]", "print("第 10 题通过")")))

def build(with_answers):
    cells = []
    md(cells, INTRO)
    for i, (q, quiz_code, ans_code) in enumerate(Q, start=1):
        md(cells, q)
        code(cells, ans_code if with_answers else quiz_code)
    md(cells, J("---", "", "全部通过后，把本 notebook 与 lab 产物一起提交。", ""))
    return notebook(cells)

os.makedirs(OUT, exist_ok=True)
for name, with_answers in (("quiz.ipynb", False), ("answers.ipynb", True)):
    nb = build(with_answers)
    p = os.path.join(OUT, name)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    print("saved", p, "cells:", len(nb["cells"]))
