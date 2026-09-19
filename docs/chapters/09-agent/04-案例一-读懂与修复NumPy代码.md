# 04 案例一：读懂并修复 NumPy 代码

> 案例定位：L1 → L2（先只读分析，再单文件修复 + 自测）。
> 复用第 1 章（axis、广播、形状判据）；真实运行记录见 lab/sample_agent_output/。

## 案例背景

课程练习脚本 `scores_buggy.py` 能正常运行、输出的数字看起来也合理，但它有两处**静默错误**：

- `scores.mean(axis=0)` 求的是"每门课的平均分"（3 个数），学员期望的是"每个学生的平均分"（8 个数）；
- `(scores - scores.min()) / (scores.max() - scores.min())` 用的是**全矩阵**的最小/最大值，把三个科目混在一起归一化，导致每列的范围不再是 0 到 1。

另外它打印的"加权总分前 3 名"其实是"前 3 个学生"，不是真正的排名。

**数据**：`lab/data/scores.csv`（8 名学生 × 平时 / 期中 / 期末，满分 100）；**待修脚本**：`lab/data/scores_buggy.py`。

## 任务卡（六件套）

| 要素 | 内容 |
| ---- | ---- |
| 目标 | 找出并修复 `scores_buggy.py` 的错误，产出 `scores_fixed.py` |
| 约束 | 只新增 `scores_fixed.py`；不修改 `data/scores.csv` 与 `scores_buggy.py` |
| 验收标准 | ① 平均分形状为 (8,) 且与手算一致；② 逐列归一化后每列 min=0、max=1；③ 加权总分第一为 王五 91.4 |
| 证据 | 运行 `python scores_fixed.py` 的完整输出 + 三条 assert 通过 |
| 复核 | 原始数据是否被改动、归一化是否逐列、排名是否真排序 |
| 提交 | 脚本 + 运行输出 + 会话记录 |

## 给 Agent 的提示词（原文）

```text
工作区里有一个成绩分析脚本 data/scores_buggy.py 和配套数据 data/scores.csv。请只读分析，不要修改任何文件：
1) 指出脚本里每个隐蔽错误，说明它算出来的到底是什么、为什么错；
2) 给出一个最小复现命令（能证明错误的形状或数值）；
3) 给出修正方案（关键行改成什么）；
4) 为修正后的结果写 3 条可执行断言（形状、逐列归一化范围、加权总分最高分是谁）。
请用简洁的条目输出。
```

## Agent 执行轨迹（示例，基线 v0.1.5-rc.2 / 2026-09-19）

**第一步：读**。它先列出工作区、读脚本与 CSV，确认列名与行数（而不是直接给答案）。推理摘录：

```text
The lab directory only has scores_buggy.py as a .py file ... the buggy script reads data/scores.csv.
Let me read scores.csv to understand the structure and check who 王五 is and confirm columns.
```

**第二步：判**。它给出的问题清单（要点）：

| 位置 | 它算出来的 | 应该是什么 |
| ---- | ---- | ---- |
| `student_mean = scores.mean(axis=0)` | 每门课的平均分，3 个数 | 每个学生的平均分，8 个数（`axis=1`） |
| `norm = (scores - scores.min()) / ...` | 全矩阵归一化：各列 min=[0, 0.25, 0.175]、max=[1, 0.975, 0.925] | 逐列归一化：各列 min 全 0、max 全 1 |
| `total[:3]` | 前 3 个学生 | 按总分降序取前三名 |

**第三步：做 + 看**。它生成 `scores_fixed.py`、运行、把输出贴回来（真实输出）：

```text
每个学生的平均分（共 8 个）:
  张三   83.33
  李四   65.00
  王五   91.67
  赵六   70.00
  钱七   83.00
  孙八   61.67
  周九   91.33
  吴十   76.67
归一化矩阵形状: (8, 3)
逐列归一化范围: min=[0. 0. 0.] max=[1. 1. 1.]
加权总分前 3 名:
  第 1 名 王五   加权总分 91.40
  第 2 名 周九   加权总分 90.90
  第 3 名 钱七   加权总分 82.90
全班平均: 77.83
自检通过：形状 / 逐列归一化范围 / 加权总分最高分为王五
```

> 说明：Agent 还主动指出"原脚本的 `total[:3]` 不是排名"，并把打印口径一起修正——这是"读→判→做→看"完整闭环的体现。
> 示例输出会随版本与模型变化；**可复现的是验收标准与断言，不是这段文字**。

## 修复要点（关键行）

```text
# 文件：data/scores_fixed.py（节选）
student_mean = scores.mean(axis=1)                                   # 每个学生一个值
norm = (scores - scores.min(axis=0)) / (scores.max(axis=0) - scores.min(axis=0))   # 逐列归一化
total = scores @ weights
order = np.argsort(-total)[:3]                                       # 真正的前三名

assert student_mean.shape == (8,)
assert np.allclose(norm.min(axis=0), 0.0) and np.allclose(norm.max(axis=0), 1.0)
assert df["姓名"].iloc[int(np.argmax(total))] == "王五"
```

## 验收标准（可执行，已运行核验）

下面这段不依赖任何数据文件，直接内联了这 8 名学生的成绩，任何机器上都能跑：

```python
import numpy as np
np.set_printoptions(precision=2, suppress=True)

scores = np.array([[82, 90, 78],
                   [60, 65, 70],
                   [95, 88, 92],
                   [70, 72, 68],
                   [88, 76, 85],
                   [55, 68, 62],
                   [91, 94, 89],
                   [76, 80, 74]], dtype=float)
weights = np.array([0.2, 0.3, 0.5])
names = ["张三", "李四", "王五", "赵六", "钱七", "孙八", "周九", "吴十"]

student_mean = scores.mean(axis=1)
norm = (scores - scores.min(axis=0)) / (scores.max(axis=0) - scores.min(axis=0))
total = scores @ weights

assert student_mean.shape == (8,), "每个学生一个平均分"
assert np.allclose(norm.min(axis=0), 0.0) and np.allclose(norm.max(axis=0), 1.0), "逐列归一化"
top = int(np.argmax(total))
assert names[top] == "王五", "加权总分第一应是王五"

print("学生平均分:", np.round(student_mean, 2))
print("逐列范围 min:", norm.min(axis=0), "max:", norm.max(axis=0))
top3 = "; ".join("%s %.2f" % (names[i], total[i]) for i in np.argsort(-total)[:3])
print("加权总分前三:", top3)
print("断言全部通过")
```

```text
学生平均分: [83.33 65.   91.67 70.   83.   61.67 91.33 76.67]
逐列范围 min: [0. 0. 0.] max: [1. 1. 1.]
加权总分前三: 王五 91.40; 周九 90.90; 钱七 82.90
断言全部通过
```

## 人工复核点

1. **有没有动原始数据**：`git status` 里 `data/scores.csv` 与 `scores_buggy.py` 必须原样；
2. **断言是不是自我循环**：检查 assert 是否真的能卡住旧实现（把旧写法代进去应立刻失败）；
3. **排名是否真排序**：看到 `argsort` / `sort_values` 才算数；
4. **解释是否对得上**：它说"axis=0 得到每门课平均分"必须与第 1 章的知识一致。

## 离线替代路径（无网络 / 无 API Key）

直接打开 `lab/sample_agent_output/`：

- `scores_fixed.py`：一次真实运行的修复产物；
- `run_fix_session.txt`：本次会话的完整记录（已脱敏），含推理过程与运行输出。

练习：找出脚本里相对原版的 4 处修改，逐条说明"为什么必须这么改"，并用 1 条断言把其中一处钉死。

## 常见坑

| 坑 | 现象 | 避免方式 |
| ---- | ---- | ---- |
| 只让它"改对"，没给判据 | 它可能只把 `axis=0` 改成 `axis=1`，漏掉归一化 | 验收标准写全三条 |
| 断言写在修复之后的代码里自证 | assert 永远成立，抓不到回归 | 断言要能卡住旧实现 |
| 让它顺手重构 | diff 变得无法审查 | 提示词里写明"不做无关改动" |
| 中文输出在 Windows 控制台乱码 | 看到"锟斤拷"类乱码 | 设 `PYTHONIOENCODING=utf-8` 或改在 VS Code 终端运行 |

## 拓展

1. 把这份数据扩展成"4 次测验 + 权重不同"，让 Agent 写参数化函数并补边界测试（全班缺考一人怎么办）；
2. 让评审代理（另一个子代理）去挑这份修复的毛病，看看它能不能发现"加权总分假设权重已归一化"；
3. 把 `scores_fixed.py` 改造成命令行工具：`python scores_fixed.py --top 3`，并让 Agent 补 `--help` 说明。

## 练习与延伸阅读

- 练习：exercises/quiz.ipynb 第 9 题（审查题：给出这段轨迹，找出仍然存在的问题）；
- 上机：lab/lab.ipynb Part B 任务 1；
- 下一节：05 案例二（数据清洗与可视化流水线）。
