# 第 0 章 课后作业（assignment，12 题）

**说明**：本作业覆盖环境工具、Python 强化与 LaTeX 基础。请先独立完成，再对照"答案要点"。建议用时 2–3 小时。

---

## 题目

### 一、环境与工具（1–3）

1. **环境命令（简答+操作）**：写出（1）创建名为 `scicomp`、Python 3.12 的 conda 环境；（2）激活它；（3）安装 `numpy scipy pandas` 的命令；（4）查看已装包的版本。
2. **VS Code 解释器（简答）**：打开一个 `.py` 后，如何确认当前运行的解释器是 `scicomp`？如果 `import numpy` 报 `ModuleNotFoundError`，列出至少 3 种可能原因并按概率排序。
3. **环境自检（操作）**：运行课程 `check_env.py`，把输出保存为 `env_check.txt`，并指出其中哪些是"必须成功"项、哪些是"可选"项。

### 二、Python 强化（4–9）

4. **切片（编程）**：给定 `nums = [0,1,2,3,4,5,6,7,8,9]`，用一行代码取出：偶数位元素；最后 3 个；反转。
5. **推导式（编程）**：从 `scores = [68, 91, 55, 76, 88, 73]` 中生成新列表：保留 60–89 分的成绩并四舍五入到整数。写两种写法（推导式 + 循环）。
6. **字典（编程）**：给定 `names = ["张三","李四"]`、`avgs = [86.3, 78.0]`，用 `zip` 生成字典 `d = {"张三": 86.3, "李四": 78.0}`，再用 `get` 取 "王五" 的默认值 0。
7. **函数默认值（简答+编程）**：解释 `def f(a, l=[])` 的坑，并改写为安全写法；再用 `*args` 写一个 `def total(*values)` 返回和。
8. **异常与文件（编程）**：写函数 `read_float(path)`：读取文件每一行转 `float`，遇到无效行则 `ValueError` 时打印行号并跳过，最后返回有效数值列表；用 `with` 打开。
9. **常用内置函数（编程）**：用 `enumerate`、`sorted`、`max` 实现：对成绩列表打印"第 i 名 姓名 分数"，并输出最高分姓名。

### 三、LaTeX（10–12）

10. **最小报告（操作）**：用课程模板写一个 1 页 `ctexart` 报告：标题《我的第一份 LaTeX 报告》、一段自我介绍、一个带编号公式 `\bar{x} = \frac{1}{n}\sum x_i`、一个 3 行 3 列表格、一张 `\includegraphics` 插入的图片；用 `latexmk -xelatex` 编译，提交 PDF 与源码。
11. **中文编译（简答）**：为什么必须用 XeLaTeX？如果用 pdflatex 会怎样？举两个在线平台（Overleaf、LoongTeX）各说一个优缺点。
12. **排错（案例分析）**：编译报错 `! Undefined control sequence. \citep`，可能的原因是什么？给出至少两条解决路径（提示：宏包/参考文献工具）。

---

## 答案要点

1. `conda create -n scicomp python=3.12 -y`；`conda activate scicomp`；`pip install numpy scipy pandas`（或 conda）；`pip list` / `conda list` / `python -V`。
2. `Ctrl+Shift+P` → Python: Select Interpreter；查看状态栏右下角；或打印 `sys.executable`。原因：未激活环境；装错环境；VS Code 用旧解释器；包名拼错。
3. 必须项：Python 3.10+、11 个核心库、`xelatex`、`latexmk`；可选：`git`、环境名（但建议一致）。
4. `nums[::2]`、`nums[-3:]`、`nums[::-1]`。
5. 推导式：`[round(s) for s in scores if 60 <= s <= 89]`；循环写法略（注意 `round` 返回 int/float 均为数值）。
6. `names = ["张三","李四"]; avgs = [86.3, 78.0]; d = dict(zip(names, avgs)); print(d.get("王五", 0))`。
7. 默认列表在定义时创建一次，多个调用共享；安全写法 `def f(a, l=None): l = [] if l is None else l`；`def total(*values): return sum(values)`。
8. 关键点：`with open(path, encoding="utf-8") as f:`；`for i, line in enumerate(f): try: val = float(line.strip()) except ValueError: print(i, "跳过")`。
9. 示例：`for rank, (name, s) in enumerate(sorted(zip(names, scores), key=lambda x: x[1], reverse=True), 1): print(rank, name, s)`。
10. 检查：编译通过、PDF 中有公式编号、表格 `\hline`、图片路径正确。
11. XeLaTeX 支持系统字体（中文 ctex）；pdflatex 默认不含 CJK 字体，中文会乱码/报错；Overleaf：模板多/协作强，访问与免费版限制；LoongTeX：中文开箱即用/访问快，生态较小。
12. ① 未引宏包（`natbib`/`biblatex`）；② 用了 `\citep` 但没配参考文献工具。解决：加 `\usepackage{natbib}` 或用 `\cite` + `bibtex`；或改用 `\cite`。
