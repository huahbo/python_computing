# 03 VS Code 使用与 Jupyter 工作流

> 本节目标：从现在起，你的“写代码”都发生在 VS Code 里。本节教你怎么打开项目、运行脚本、跑笔记本、查错误、用快捷键，让后面 8 章不被工具本身耽误。

## 本节目标

- 会用 VS Code 打开课程目录并在正确的 Python 环境中运行代码；
- 会新建与运行 `.ipynb` 笔记本：运行单元格、重启内核、导出；
- 会在终端激活 `scicomp` 环境、运行 `pip/conda` 命令；
- 会看“问题”面板与运行输出，能读懂简单报错；
- 记住最常用的 10 个快捷键。

---

## 3.1 打开文件夹与工作区

1. 启动 VS Code → `文件 → 打开文件夹`（或 `Ctrl+K Ctrl+O`）；
2. 选择你的课程目录（例如 `D:\Scientific_Computing_Class\course-dist`）；
3. 左边资源管理器出现文件树；把 `chapters/00-prep` 等目录展开即可。

> **工作区 vs 文件夹**：直接打开文件夹即可；只有需要多根目录时才用“工作区（.code-workspace）”。

## 3.2 解释器与内核（重要！）

- **解释器**（跑 .py 用）：`Ctrl+Shift+P` → `Python: Select Interpreter` → 选择 `scicomp`。
- **内核**（跑 notebook 用）：打开 `.ipynb` 后，右上角内核选择器同样选 `scicomp`；没有该内核时在终端执行：

```powershell
conda activate scicomp
python -m ipykernel install --user --name scicomp
```

建议在项目根目录放一个 `.vscode/settings.json` 固定解释器（示例，路径按你的机器改）：

```json
{
  "python.defaultInterpreterPath": "C:/Users/你的用户名/miniconda3/envs/scicomp/python.exe",
  "python.terminal.activateEnvironment": true,
  "jupyter.notebookFileRoot": "${workspaceFolder}"
}
```

## 3.3 运行 Python 脚本

1. 新建 `hello.py`，写：

```python
print("你好，Python 科学计算")
print(2 ** 10)
```

2. 三种运行方式：
   - 右上角的“运行”按钮（Play）；
   - 右键 → `在终端中运行 Python 文件`；
   - 打开集成终端（`Ctrl+``）手动执行 `python hello.py`。

3. 注意终端中的当前目录（`pwd` / `cd`），文件路径建议按“相对项目根目录”写。

## 3.4 Jupyter 笔记本入门

### 新建与运行

- `文件 → 新建文件`，保存为 `lab0.ipynb`（先保存才能识别为笔记本）；
- 每格支持 **代码单元格** 与 **Markdown 单元格**（用 `M` 切换模式，`Y` 切回代码）；
- 运行当前格：`Shift+Enter`（并跳到下一格）或 `Ctrl+Enter`（停在当前格）。

### 会用到的操作

| 操作 | 快捷键 |
| ---- | ---- |
| 上方插入单元格 | `A`（命令模式下） |
| 下方插入单元格 | `B` |
| 删除单元格 | `Ctrl+Shift+K` 或 `DD` |
| 保存 | `Ctrl+S` |
| 重启内核 | `Ctrl+Shift+P` → `Jupyter: Restart Kernel` |
| 全部运行 | `Run All`（工具栏） |
| 导出为 HTML/PDF | 工具栏 → 导出（PDF 推荐用“导出为 HTML 再打印”或先装 LaTeX 依赖） |

### 笔记本规范（从第 0 章养成）

1. 第一格用 Markdown 写标题、姓名、学号、日期；
2. 每个任务前用 Markdown 单元格写清“要做什么”；
3. 一个任务一个代码单元格，避免一个格子塞 200 行；
4. 输出重要的结果用 `print` 或直接显示，方便老师检查；
5. 运行顺序从上到下；中途改了前面的代码务必“重启内核并全部运行”再提交。

## 3.5 终端与包管理

- 在 VS Code 中按 `Ctrl+`` 打开终端；
- 确认环境：

```powershell
conda env list          # 看有哪些环境
conda activate scicomp  # 激活
where python            # 确认用的是 scicomp 的 python
```

- 装/卸包：

```powershell
pip install 包名
pip uninstall 包名
conda install -c conda-forge 包名
```

> 注意：如果终端 `python` 还是系统 Python，说明没激活环境，请先 `conda activate scicomp`。

## 3.6 调试与排错

- **问题面板**（`Ctrl+Shift+M`）：显示语法/类型/导入错误；
- **运行与调试**：在行号左侧点击设置断点，按 `F5` 启动调试；`F10` 单步、`F11` 进入函数；
- **输出乱码**：终端输入 `chcp 65001` 切换 UTF-8；
- **报错读法**（自右向左读）：

```text
Traceback (most recent call last):        ← 出错的调用链
  File "lab0.py", line 12, in <module>    ← 文件与行号
    print(1/0)
ZeroDivisionError: division by zero       ← 最后一行才是真正的错误类型与信息
```

常用错误速查：`NameError`（名字没定义）、`TypeError`（类型不对）、`IndexError`（越界）、`KeyError`（字典缺键）、`FileNotFoundError`（路径不对）、`ModuleNotFoundError`（没装包/环境不对）。

## 3.7 常用快捷键表

| 功能 | 快捷键 |
| ---- | ---- |
| 快速打开文件 | `Ctrl+P` |
| 命令面板 | `Ctrl+Shift+P` |
| 切换终端 | `Ctrl+`` |
| 运行单元格 | `Shift+Enter` |
| 注释/取消注释 | `Ctrl+/` |
| 格式化文档 | `Shift+Alt+F` |
| 全局搜索 | `Ctrl+Shift+F` |
| 打开设置 | `Ctrl+,` |

## 3.8 本节演示（跟着做一遍）

1. 新建 `demo.ipynb`；
2. Markdown 格写标题“我的第一个课程笔记本”；
3. 代码格：

```python
import sys
print(sys.executable)          # 看当前解释器
nums = [1, 2, 3, 4, 5]
print("平均值:", sum(nums) / len(nums))
```

4. 运行后，把 `sys.executable` 的输出和终端 `where python` 对比：应该都是 `scicomp` 的路径；
5. 交给老师/助教检查输出截图。

## 常见问题

| 问题 | 解决 |
| ---- | ---- |
| 右键没有“在终端中运行” | 确认安装了 Python 扩展并已选择解释器 |
| 笔记本运行报“No kernel” | 重启 VS Code，再选 `scicomp`；或执行上面 ipykernel 安装命令 |
| 中文终端乱码 | `chcp 65001`；文件保存用 UTF-8 |
| 运行结果和老师不一样 | 先检查解释器；再检查每次是否“重启内核并全部运行” |

## 本节小结

- 先选对解释器/内核，再写代码；这两步解决 70% 的“我电脑报错”。
- 笔记本 = 代码 + Markdown 说明；按“一个任务一个单元格”组织。
- 报错不可怕：最后一行 = 错误类型，往上找文件与行号。

### 思考题

1. `sys.executable` 输出的路径是 conda 的还是系统的？为什么这很重要？
2. 如果你在 VS Code 里运行 `.py` 成功，但运行 `.ipynb` 失败，最可能的原因是什么？
