# 04 Python 编程快速强化

> 本节目标：你已学过语言程序设计课，本节不系统讲语法，而是用“自测 + 查漏”的方式强化科学计算最常用的 Python 能力：容器、函数、异常、文件、常用内置函数。先做自测，再针对性看讲解。

## 本节目标

- 能解释并操作 list/dict/tuple/set 的常见方法与切片；
- 熟练使用列表推导式、`zip`、`enumerate`、`sorted`、`max/min/sum`；
- 理解函数参数（默认值、`*args`、`**kwargs`）、作用域与返回值；
- 会写 `try/except`、`with open(...)` 读写文件；
- 养成命名、注释、`if __name__ == "__main__"` 的工程习惯。

---

## 4.1 课前自测（10 分钟，先不看答案）

在 `exercises/quiz.ipynb` 或纸上快速回答：

1. `[1,2,3,4,5][::-1]` 的结果？
2. `{i: i*i for i in range(4)}` 的结果？
3. `sorted(["b","a","c"], reverse=True)` 的结果？
4. `zip([1,2],[3,4])` 转成 list 是什么？
5. 定义 `def f(a=[]): ...` 有什么风险？
6. `try/finally` vs `try/except` 的区别？
7. `with open("a.txt") as f:` 比 `open/close` 好在哪？
8. `*args` 与 `**kwargs` 分别装什么？
9. `"a,b,c".split(",")` 结果？
10. `is` 与 `==` 的区别（举例）？

> 答案与详解在 `exercises/answers.ipynb`。错 3 题以上，建议把本节的“查漏表”逐条过一遍。

## 4.2 变量与类型：会“拆开”就够了

| 类型 | 常用操作 | 注意 |
| ---- | ---- | ---- |
| `int` / `float` | 算术、`//`、`**` | 浮点比较用 `abs(a-b) < 1e-9` |
| `str` | `format`、f-string、`split/join` | 字符串不可变 |
| `list` | 追加、切片、推导式 | 可变；`+` 是新建 |
| `tuple` | 解包、做字典键 | 不可变 |
| `dict` | 键值、`get`、遍历 | 键必须可哈希 |
| `set` | 去重、交并差 | 无序 |

一行代码示例：

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(nums[1:5])            # [1, 4, 1, 5]
print(nums[::-1])           # 反转
print(sum(nums), max(nums), min(nums))
print(sorted(set(nums)))    # 去重排序
print({x: x * x for x in nums[:5]})
```

## 4.3 容器查漏表

**切片**：`[start:stop:step]`，含头不含尾；`step` 为负可倒序；`[::-1]` 最常用。

**列表推导式**：`[表达式 for 项 in 可迭代 if 条件]`；不要嵌套太深，超过两层就写循环。

**字典方法**：

```python
d = {"a": 1, "b": 2}
print(d.get("c", 0))        # 0，不会 KeyError
for k, v in d.items():      # 遍历键值
    print(k, v)
print(d.keys(), d.values())
```

**set**：`set("hello")` 去重；`a & b`、`a | b`、`a - b`。

## 4.4 流程控制与推导式

```python
# 条件表达式（三元）
label = "及格" if score >= 60 else "不及格"

# 列表推导（科学计算里最常见的“批量变换”）
scores = [68, 91, 55, 76, 88]
passed = [s for s in scores if s >= 60]

# 循环里同时拿索引与值
for i, s in enumerate(scores):
    print(i, s)

# 两个列表打包
names = ["张三", "李四"]
for name, s in zip(names, scores[:2]):
    print(name, s)
```

## 4.5 函数：默认值、不定长、作用域

```python
def report(name, scores, *, title="成绩", fmt="%.1f"):
    """返回一行摘要字符串。"""
    total = sum(scores)
    avg = total / len(scores) if scores else 0.0
    return f"[{title}] {name}: 总分 {total}，平均 {fmt % avg}"

print(report("张三", [80, 90]))
print(report("李四", [70, 75], title="期末"))
```

要点：

- 默认参数只在**定义时求值一次**：`def f(a=[])` 会共享列表 → 改用 `def f(a=None): a = [] if a is None else a`；
- `*args` 收集位置参数为元组；`**kwargs` 收集关键字参数为字典；
- 函数内改全局变量要 `global`（尽量别用）；返回值用 `return`；
- 写 `docstring`（第一行字符串），是“会写代码”和“写得专业”的分水岭。

## 4.6 异常、文件与模块

### 异常处理

```python
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("除零啦:", e)
        return None
    finally:
        pass   # 无论成败都执行（比如关文件）

print(safe_div(10, 2))
print(safe_div(1, 0))
```

> 捕获要**具体**：不要裸 `except:`；多个错误写 `except (ValueError, KeyError):`。

### 文件读写

```python
# 写
with open("result.txt", "w", encoding="utf-8") as f:
    f.write("平均分 78.0\n")

# 读
with open("result.txt", encoding="utf-8") as f:
    lines = f.readlines()
print(lines)

# 读 csv（第 0 章只需 csv 模块；第 4 章再学 pandas）
import csv
with open("data/scores.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print(rows[:2])
```

### 模块与包

```python
# 自己的模块
import math
from collections import Counter

print(math.pi)
print(Counter("hello world"))
```

- 自己写模块：同目录 `utils.py` 里定义函数，主程序 `from utils import xxx`；
- 主程序入口：`if __name__ == "__main__":`（被 import 时不执行、直接运行才执行）。

## 4.7 常用内置函数速查

| 函数 | 作用 | 例子 |
| ---- | ---- | ---- |
| `len/sum/max/min` | 长度/求和/最值 | `max(scores)` |
| `enumerate` | 带索引遍历 | `for i, x in enumerate(v):` |
| `zip` | 并行打包 | `dict(zip(names, scores))` |
| `sorted` | 返回新排序列表 | `sorted(d.items(), key=lambda kv: kv[1])` |
| `map/filter` | 映射/过滤（可用推导式替代） | `list(map(str, nums))` |
| `any/all` | 存在/全部 | `any(x > 0 for x in nums)` |
| `round` | 四舍五入 | `round(3.14159, 2)` |
| `isinstance` | 类型判断 | `isinstance(x, (int, float))` |

## 4.8 工程习惯（现在养成，后面 8 章受益）

1. **命名**：变量 `score_list`、函数 `compute_average`；不用 `a1`、`data` 满天飞；
2. **注释**：解释“为什么”，不抄代码本身；
3. **一个文件只做一件事**；能拆函数就不堆在一个 `main` 里；
4. **导入放顶部**；第三方库按字母序排列；
5. **结果可复现**：随机数加种子（后面 NumPy 章会讲）；路径统一用相对路径；
6. **先跑通再优化**：不追求一行神代码。

## 4.9 本节综合小任务（交给 lab 的 Part B）

题目：读入 `lab/data/scores.csv`（字段：学号,姓名,Python,数学,英语），用纯 Python 完成：

- 计算每个人的总分与平均分；
- 找出平均分最高与最低的学生；
- 把“总分 ≥ 240”的学生写入 `result.txt`；
- 统计 60 分以下的人数。

> 完整步骤见 `lab/lab.ipynb` 与 00-07 综合案例。

## 常见误区

| 误区 | 正确做法 |
| ---- | ---- |
| `==` 比较小整数没问题，比较浮点数/字符串用 `is` | 数值比较一律 `==`；`is` 只用于 `None` |
| 默认参数写 `=[]` | 用 `=None` 再在函数内初始化 |
| 直接改列表时产生副作用 | 需要副本时用 `copy` 或切片 `[:]` |
| 循环里 100 万次逐元素计算 | 后面学 NumPy 向量化（第 1 章核心） |
| `except:` 吞掉所有错误 | 捕获具体异常，至少 `print` 出来 |

## 本节小结与思考题

1. 用推导式写出：把 `scores` 中 60~90 分的小数保留两位并去掉重复。
2. 解释 `def add(a, b=10): return a + b` 的默认参数什么时候会被“记住”。
3. 为什么 `with open` 更安全？
