
# NumPy 高级练习（20题） — 适合有 Python 基础的初学者进阶

**说明**：这份作业覆盖 NumPy 的核心与进阶主题（数据类型、创建、索引与切片、广播、形状变换、视图与拷贝、高级索引、ufunc、线性代数、随机数、I/O、性能与内存布局等）。前半部分为 20 道题（题目），之后给出每题的完整详解与参考代码。请先尝试独立完成题目，再查看答案部分。

---

## 题目（共 20 题）

### 容易/中等（1-8）
1. **数据类型与转换（编程）**  
   创建一个包含整数 `1, 2, 3` 的 NumPy 数组，显式指定为 `np.int32`。将其转换为 `np.float64`，并说明 dtype 变化与内存影响（简述）。

2. **创建与特殊矩阵（编程）**  
   用一行代码创建一个 6x6 的矩阵，其对角线为 1，主对角线下方第一条次对角线为 2，主对角线上方第一条次对角线为 3，其余元素为 0。

3. **reshape 与 -1（编程）**  
   有一个一维数组 `np.arange(30)`。将其重塑为形状 `(2, 3, -1)`，并说明第三维为何自动计算出多少，以及总元素数如何匹配。

4. **视图与拷贝（简答+编程）**  
   给出例子证明：`reshape` 在何种情况下返回视图（view），何种情况返回拷贝（copy）。编写代码创建一个原数组，执行 `reshape`，并用 `arr.base` 或 `np.may_share_memory` 验证。

5. **广播规则（编程）**  
   给定 `A.shape = (4,1,6)` 和 `B.shape = (3,6)`，在 NumPy 中尝试 `A + B`。请说明会怎样进行广播（包括中间将 B 视为何形状），并给出能使这两者可相加的代码示例。

6. **高级索引（编程）**  
   给定数组 `X = np.arange(24).reshape(4,6)`，使用 fancy indexing（整数数组索引）选出第 0、2 行以及第 1、4 列交叉的元素，形成一个 2x2 的数组。

7. **布尔掩码与 np.where（编程）**  
   生成 `arr = np.random.randint(-10, 10, size=15)`，用布尔掩码将所有负数替换为其绝对值（正数），但保留 0 与正数不变。要求使用 **两种不同方法**：一种用布尔索引，另一种用 `np.where`。

8. **ufunc 与 reduce（编程）**  
   用 `np.add.reduce` 与 `np.add.accumulate` 分别作用于 `np.array([1,2,3,4])`，并说明两者的区别与典型应用场景。

---

### 中等/偏难（9-15）
9. **矩阵乘法与 einsum（编程）**  
   给定 `A.shape = (2,3)` 与 `B.shape = (3,4)`，用三种方法计算矩阵乘积 `C = A @ B`：`@` 运算符、`np.dot`/`np.matmul`、以及 `np.einsum`。说明 `einsum` 的字符串表达及其一般优势。

10. **线性代数：求解与条件数（编程+简答）**  
    构造一个接近奇异的 3x3 矩阵（例如使用某一行接近另一行的方式），用 `np.linalg.solve` 解线性系统 `Ax = b`（任选 b），并计算其条件数 `np.linalg.cond(A)`。解释条件数大说明什么，并演示通过改变矩阵（稍微增加扰动）导致解的不稳定性。

11. **特征值与 SVD（编程）**  
    随机生成一个 5x5 的浮点矩阵 `M`（用种子以保证可重复），计算并比较 `np.linalg.eig(M)` 与 `np.linalg.svd(M)` 的输出（讨论何时用 eig，何时用 SVD）。未必要求数学证明，但要演示代码与结果维度。

12. **广播与内存开销（偏难，编程）**  
    使用 `np.ones((1000, 1000))` 与一个形状 `(1000,)` 的向量 `v`。衡量并比较 `A + v`（广播得到的临时数组）与 `A + v[np.newaxis, :]` 两种写法的内存与时间开销（可用 `%timeit` 或 `time` 测量），说明广播不复制时与何时会产生临时数组。

13. **缺失值与统计（编程）**  
    创建一个含有 NaN 的数组 `arr = np.array([1.0, np.nan, 2.0, 3.0, np.nan])`。计算元素的均值与中位数，要求忽略 NaN，分别用 `np.nanmean`/`np.nanmedian` 与掩码实现两种方法，并比较结果。

14. **排序与 argsort（编程）**  
    给定二维数组 `scores`（形状 `(N, M)`）表示 N 个学生 M 门课成绩，使用 `np.argsort` 找出总分排名前 3 的学生索引，并返回他们的总分与成绩行。请给出示例数据并实现。

15. **文件 I/O（编程）**  
    将一个随机生成的 2D 浮点数组保存为 `.npz`（使用 `np.savez_compressed`），然后读取回来并验证内容相同。同时展示如何用 `np.savetxt` 保存为 CSV 并用 `np.loadtxt` 读取（注意格式问题）。

---

### 稍难（16-20）
16. **结构化数组（编程）**  
    创建一个结构化数组（structured array），包含字段 `name`（长度 10 的字符串）、`age`（int）、`score`（float）。插入 4 条记录，然后按 `score` 排序返回排序后的名字列表。

17. **stride 与内存视图（偏难，编程+解释）**  
    创建 `a = np.arange(16).reshape(4,4)`，然后使用切片创建 `b = a[:, ::2]`（取每行的偶数列）。打印 `a.strides` 和 `b.strides`，解释 stride 的含义，并说明为什么 `b` 是一个视图而非拷贝。

18. **性能优化：向量化 vs Python 循环（编程/测量）**  
    给定一个大数组 `x = np.random.rand(10_000_00)`（一百万元素），实现以下两种运算并比较时间：  
    - 使用 Python 循环逐元素计算 `y[i] = x[i]**2 + 2*x[i] + 1`。  
    - 使用 NumPy 向量化表达式 `y = x**2 + 2*x + 1`。  
    报告两者时间差并简短解释原因。

19. **广播陷阱（偏难，编程）**  
    设计一个例子展示广播可能导致不期望的结果（例如当一个维度为 1 的数组意外扩展时导致计算错误），并说明如何修改代码以避免错误（例如使用 `np.expand_dims` 或重塑 `reshape`）。

20. **综合题：实现一个小功能（编程）**  
    编写一个函数 `moving_average(arr, k)`，使用 NumPy 的 `convolve` 或 `cumsum` 高效计算一维数组 `arr` 的窗口大小为 `k` 的移动平均（边界处理为“有效”模式，即输出长度为 `len(arr)-k+1`）。要求使用向量化实现并给出时间复杂度简要分析。

---

## 答案（详细，带代码与解释） — 请先自行完成题目再查看答案


---

# 答案详解

> 注：所有代码片段可在 Python 环境（含 NumPy）中直接运行。为保证随机相关题目的可重复性，示例中多处设置了 `np.random.seed(0)`。

### 答案 1（数据类型与转换）
```python
import numpy as np
arr = np.array([1,2,3], dtype=np.int32)
print(arr, arr.dtype)
arr2 = arr.astype(np.float64)
print(arr2, arr2.dtype)
```
**解释**：`dtype` 从 `int32` 变为 `float64`。在内存上，`int32` 每元素占 4 字节，`float64` 每元素占 8 字节，所以转换会产生新的数组并占用更多内存。`astype` 默认返回拷贝（除非类型相同）。

---

### 答案 2（特殊对角矩阵）
```python
import numpy as np
# 方法：先创建零矩阵，然后用 np.fill_diagonal 或 np.diag_indices
M = np.zeros((6,6), dtype=int)
np.fill_diagonal(M, 1)
i = np.arange(5)
M[i+1, i] = 2  # 次对角线（下）
M[i, i+1] = 3  # 次对角线（上）
print(M)
```
输出为 6x6，主对角为 1，下对角为 2，上对角为 3。

---

### 答案 3（reshape 与 -1）
```python
import numpy as np
arr = np.arange(30)
mat = arr.reshape(2, 3, -1)
print(mat.shape)
```
`mat.shape` 为 `(2, 3, 5)`，因为 `2*3*? = 30`，故 `? = 5`。使用 `-1` 时 NumPy 自动推断该维度以保证总元素数相同。

---

### 答案 4（视图与拷贝）
```python
import numpy as np
a = np.arange(12)
b = a.reshape(3,4)          # 通常为 view
print('a.base is None?', a.base is None)
print('b.base is a?', b.base is a)  # True 表示 b 是 view

# 但在某些情况下会返回拷贝，例如改变步长不连续时
c = a[::2]                  # 这是 view（stride 非 1，但仍是 view）
d = c.reshape(2,3) if c.size==6 else c.copy()
print('c.base is a?', c.base is a)

# 强制构造需要拷贝的 reshape（例如非连续内存）
e = np.arange(6)[::2]      # e = [0,2,4]，非连续
try:
    f = e.reshape(3,1)
    print('f.base is e?', f.base is e)  # 通常为 view if shape compatible
except Exception as ex:
    print('reshape exception:', ex)

# 使用 np.may_share_memory 验证
from numpy import may_share_memory
print('may share a and b?', may_share_memory(a,b))
```
**说明**：是否为 view 与底层内存布局（contiguous）和 stride 有关。`reshape` 在可以不改变数据顺序的情况下返回 view，否则返回 copy。使用 `arr.base` 或 `np.may_share_memory` 可检验共享内存。

---

### 答案 5（广播规则）
```python
import numpy as np
A = np.zeros((4,1,6))
B = np.zeros((3,6))
# B is shape (3,6). For broadcasting with A (4,1,6),
# numpy will treat B as (1,3,6) by prepending a 1 dimension,
# then broadcast to (4,3,6) while A broadcasts its middle dim 1 -> 3.
# Try to compute:
try:
    C = A + B
    print('A+B shape:', C.shape)
except Exception as e:
    print('Error:', e)
# If numpy cannot directly broadcast due to mismatched trailing dimensions,
# we can reshape B to (1,3,6) explicitly:
C2 = A + B[np.newaxis, :, :]
print('C2 shape:', C2.shape)  # (4,3,6)
```
**解释**：`B` 会被视为 `(1,3,6)`（在左侧补 1），然后与 `A (4,1,6)` 一起广播至 `(4,3,6)`，其中 `A` 的第 1 轴（中间轴）从 1 扩展到 3，`B` 的第 0 轴从 1 扩展到 4。

---

### 答案 6（高级索引）
```python
import numpy as np
X = np.arange(24).reshape(4,6)
rows = [0,2]
cols = [1,4]
# We want cross elements: take rows 0 and 2, and cols 1 and 4
# Using np.ix_ to form the Cartesian indexing grid
result = X[np.ix_(rows, cols)]
print(result)
```
输出：
```
[[ 1  4]
 [13 16]]
```

---

### 答案 7（布尔掩码与 np.where）
```python
import numpy as np
np.random.seed(0)
arr = np.random.randint(-10, 10, size=15)
print('orig:', arr)

# 方法1: 布尔索引
arr1 = arr.copy()
mask = arr1 < 0
arr1[mask] = -arr1[mask]
print('method1:', arr1)

# 方法2: np.where
arr2 = np.where(arr < 0, -arr, arr)
print('method2:', arr2)
```
两种方法等价。`np.where` 返回新数组（不原地修改），布尔索引可在原地修改（更节省内存）。

---

### 答案 8（ufunc reduce / accumulate）
```python
import numpy as np
a = np.array([1,2,3,4])
print('reduce add:', np.add.reduce(a))        # 1+2+3+4 = 10
print('accumulate add:', np.add.accumulate(a))# [1, 3, 6, 10]
```
**说明**：`reduce` 对数组执行归约，返回单一结果；`accumulate` 返回中间累积结果数组。`accumulate` 常用于生成前缀和等，`reduce` 用于求总和、乘积等。

---

### 答案 9（矩阵乘法三种方法）
```python
import numpy as np
A = np.arange(6).reshape(2,3)
B = np.arange(12).reshape(3,4)
# method1: @
C1 = A @ B
# method2: np.dot / np.matmul
C2 = np.dot(A, B)
C3 = np.matmul(A, B)
# method3: einsum
C4 = np.einsum('ik,kj->ij', A, B)
print('equal?', np.allclose(C1, C2, C3, C4))
print(C1)
```
**einsum 解释**：`'ik,kj->ij'` 指定了索引的收缩方式（i 行, k 列 与 k 行, j 列 相乘并对 k 求和）。`einsum` 在表达复杂张量收缩、避免中间数组时效率更高，灵活性强。

---

### 答案 10（线性系统与条件数）
```python
import numpy as np
# 构造接近奇异矩阵
A = np.array([[1, 2, 3],
              [2, 4.0001, 6],
              [1, 0.9999, 2]])
b = np.array([1, 2, 3])
cond = np.linalg.cond(A)
print('cond(A)=', cond)
x = np.linalg.solve(A, b)
print('solution x =', x)

# 增加小扰动看解的变化
b2 = b + 1e-6*np.random.randn(3)
x2 = np.linalg.solve(A, b2)
print('perturbed solution diff:', np.linalg.norm(x2-x))
```
**说明**：条件数越大，矩阵越接近奇异，线性系统对输入扰动（如 b 的微小变化或系数矩阵元素的微小改变）越敏感，解的不稳定性越高。

---

### 答案 11（特征值与 SVD）
```python
import numpy as np
np.random.seed(0)
M = np.random.randn(5,5)
eigvals, eigvecs = np.linalg.eig(M)
U, s, Vt = np.linalg.svd(M)
print('eigvals shape:', eigvals.shape)
print('svd s shape:', s.shape)
```
**说明**：`eig` 适用于方阵，返回特征值与特征向量，适合对方阵做谱分解（若矩阵可对角化）；`svd` 对任意矩阵均适用，返回奇异值分解 `M = U * diag(s) * Vt`，SVD 对数值稳定且在低秩近似、最小二乘与矩阵条件分析中常用。

---

### 答案 12（广播与内存开销）
```python
import numpy as np, time
A = np.ones((1000,1000))
v = np.arange(1000.0)

t0 = time.time()
C = A + v  # broadcasting
t1 = time.time()
# explicit reshape:
t2 = time.time()
C2 = A + v[np.newaxis, :]
t3 = time.time()

print('A+v time:', t1-t0)
print('A+v[np.newaxis,:] time:', t3-t2)
# 查看是否存在临时数组：在这两种写法下 numpy 都会产生一个输出数组 C
# 广播本身不复制，但实际计算会产生输出数组，除非用 out= 指定保存位置。
```
**说明**：广播的语义本身并不复制数据，但在执行运算时会生成一个输出数组（临时），占用相应内存。使用 `out=` 参数或在原地操作（如 `A += v`）可以避免额外的临时数组。

---

### 答案 13（NaN 处理）
```python
import numpy as np
arr = np.array([1.0, np.nan, 2.0, 3.0, np.nan])
mean1 = np.nanmean(arr)
median1 = np.nanmedian(arr)
print('nanmean, nanmedian:', mean1, median1)

# 用掩码实现:
mask = ~np.isnan(arr)
mean2 = arr[mask].mean()
median2 = np.median(arr[mask])
print('masked mean, median:', mean2, median2)
```
两种方法结果一致。

---

### 答案 14（argsort 排名）
```python
import numpy as np
np.random.seed(0)
scores = np.random.randint(50,100,size=(10,4))  # 10 students, 4 courses
total = scores.sum(axis=1)
top3_idx = np.argsort(-total)[:3]  # 按总分降序取前三
print('top3 indices:', top3_idx)
print('top3 totals:', total[top3_idx])
print('their rows:\n', scores[top3_idx])
```
`argsort` 返回排序后索引，常用 `-total` 实现降序。

---

### 答案 15（I/O）
```python
import numpy as np
np.random.seed(0)
arr = np.random.randn(5,5)

# 保存为 npz
np.savez_compressed('demo.npz', arr=arr)
data = np.load('demo.npz')
arr2 = data['arr']
print('equal npz?', np.allclose(arr, arr2))

# 保存为 CSV
np.savetxt('demo.csv', arr, delimiter=',', fmt='%.6f')
loaded = np.loadtxt('demo.csv', delimiter=',')
print('equal csv?', np.allclose(arr, loaded))
```
`.npz` 可保存多个数组并压缩；CSV 文本保存时注意数值格式与精度。

---

### 答案 16（结构化数组）
```python
import numpy as np
dt = np.dtype([('name', 'U10'), ('age', np.int32), ('score', np.float64)])
data = np.array([('Alice', 23, 88.5),
                 ('Bob', 19, 92.0),
                 ('Cathy', 22, 78.0),
                 ('David', 21, 85.0)], dtype=dt)
# 按 score 排序 (descending)
sorted_idx = np.argsort(data['score'])[::-1]
sorted_names = data['name'][sorted_idx]
print(sorted_names)
```

---

### 答案 17（stride 与视图）
```python
import numpy as np
a = np.arange(16).reshape(4,4)
b = a[:, ::2]
print('a.strides =', a.strides)
print('b.strides =', b.strides)
print('b.base is a?', b.base is a)
```
**解释**：`strides` 表示沿每个轴前进一个元素所需字节数。对于 `a`（默认 C-order、int64），`a.strides` 可能是 `(32,8)`（取决于 dtype），而 `b` 的 stride 第二个轴会变为 `16`（因为跳过了一列），`b` 是基于 `a` 的视图（共享数据），因此 `b.base` 指向 `a`。

---

### 答案 18（向量化 vs 循环）
```python
import numpy as np, time
np.random.seed(0)
x = np.random.rand(1_000_000)
# python loop
t0 = time.time()
y = np.empty_like(x)
for i in range(x.size):
    y[i] = x[i]**2 + 2*x[i] + 1
t1 = time.time()
# numpy vectorized
t2 = time.time()
y2 = x**2 + 2*x + 1
t3 = time.time()
print('loop time', t1-t0)
print('vectorized time', t3-t2)
print('speedup ~', (t1-t0)/(t3-t2))
```
结果会显示向量化版本通常快数十倍甚至上百倍，因为底层用 C 实现并利用连续内存与 SIMD 优化，而 Python 循环每次都有解释器开销。

---

### 答案 19（广播陷阱）
```python
import numpy as np
# 错误例子: 期望把 (3,1) 的列向量与 (3,) 的行向量相加得到 (3,3),
# 但若错误地用了 (1,3) 形状会导致沿错误方向广播
col = np.array([[1],[2],[3]])   # shape (3,1)
row = np.array([10,20,30])      # shape (3,)
# 若误用 row.reshape((3,1)) 则形状(3,1)与(3,1)不能广播到(3,3)
try:
    bad = col + row.reshape(3,1)  # raises or gives wrong shape
    print('bad shape', bad.shape)
except Exception as e:
    print('error as expected', e)

# 正确做法:
good = col + row[np.newaxis, :]  # col (3,1) broadcasts with (1,3) -> (3,3)
print('good shape', good.shape)
```
**提示**：使用 `np.expand_dims` 或 `np.newaxis` 明确控制维度，避免意外广播。

---

### 答案 20（移动平均）
```python
import numpy as np

def moving_average(arr, k):
    arr = np.asarray(arr)
    if k <= 0 or k > arr.size:
        raise ValueError("k must be between 1 and len(arr)")
    # 使用 cumsum 方法: O(n) 时间
    c = np.cumsum(arr, dtype=float)
    # c[k-1:] - c[:-k] ...
    res = (c[k-1:] - np.concatenate(([0.0], c[:-k])) ) / k
    return res

# 示例
x = np.arange(10)
print(moving_average(x, 3))  # [1. 2. 3. 4. 5. 6. 7. 8.]

# 说明：时间复杂度为 O(n)，不依赖于 k（只有常数额外成本），比直接滑窗循环更高效。
```

---

# 结束语
 
文件列表：
- `numpy_assignment.md` — 本题及答案的 Markdown 文档  
- `numpy_assignment.ipynb` — Jupyter Notebook（包含同样内容，可直接在 Jupyter/Colab/Overleaf Notebook 打开）  
- `numpy_assignment.zip` — 包含上面两个文件的压缩包


