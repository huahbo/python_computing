# 项目运行说明（Windows 10/11 + VS Code）

本说明帮助你在 Windows 10/11 + VS Code 环境下运行本课程的期末项目（Project 1 & Project 2）。

---

## 1. 安装必备软件

### 1.1 安装 Python 3.9+
- 访问 Python 官网下载 Windows 安装包  
- 安装时务必勾选 **Add Python to PATH**

### 1.2 安装 VS Code
- 下载 VS Code 官方 Windows 安装包  
- 安装后打开 VS Code → 左侧「扩展（Extensions）」  
- 安装以下插件：  
  - **Python**
  - （可选）**Jupyter**

---

## 2. 创建项目文件夹

例如创建文件夹：

```
D:\python_scientific_final\
```

将所有项目文件放入该目录，例如：

- `project1_ecommerce_analysis.py`
- `project2_transport_network.py`
- `projects_student.md`
- `projects_teacher.md`
- 数据文件（如 `ecommerce_orders.csv`）
- **RUNNING.md**

---

## 3. 使用 VS Code 打开项目

1. 打开 VS Code  
2. File → Open Folder…  
3. 选择项目目录，例如 `D:\python_scientific_final\`  
4. 左侧资源管理器会显示所有文件

---

## 4. 创建虚拟环境（强烈推荐）

在 VS Code 终端中执行：

```powershell
python -m venv .venv
```

### 激活虚拟环境

PowerShell：

```powershell
.\.venv\Scripts\activate
```

CMD：

```cmd
.venv\Scripts\activate.bat
```

激活成功后命令行前面会出现 `(.venv)`。

---

## 5. 安装依赖库

在虚拟环境中执行：

```bash
pip install numpy scipy sympy pandas matplotlib seaborn networkx statsmodels scikit-learn
```

如果网络较慢，可使用国内镜像（可选）。

---

## 6. 运行 Project 1

### 方式一：直接运行 `.py` 文件
1. 打开 `project1_ecommerce_analysis.py`
2. 确保同目录下有 `ecommerce_orders.csv`
3. 点击右上角「Run」或按 `Ctrl+F5`

生成的图像将保存在当前目录，例如：

- `monthly_sales.png`
- `category_sales.png`
- `daily_sales_prediction.png`

### 方式二：运行 `.ipynb` (如你使用 Notebook)
- 确保 Jupyter 插件已安装  
- 创建或打开 `project1.ipynb`  
- 逐个运行 cell

---

## 7. 运行 Project 2

Project 2 默认使用**合成数据**，可直接运行代码：

1. 打开 `project2_transport_network.py`
2. 点击「Run」或 `Ctrl+F5`

运行后会生成图像：

- `network.png`
- `flow_ma.png`
- `flow_ts_forecast.png`
- `feature_importances.png`
- `price_revenue_curve.png`

---

## 8. 常见问题排查

### ❗ ImportError / ModuleNotFoundError
说明库未安装，重新执行：

```
pip install numpy scipy sympy pandas matplotlib seaborn networkx statsmodels scikit-learn
```

### ❗ 中文路径报错
建议整个项目路径都使用英文文件夹名。

### ❗ 图像未显示
脚本中已使用 `plt.savefig()`，图像会保存在项目目录下。

在 Notebook 中想直接显示图像，可使用：

```python
%matplotlib inline
```

---

## 9. 提交要求（建议）

提交内容包括：

- 代码文件（`.py` 或 `.ipynb`）
- 所有生成的图像
- 课程大作业报告（Markdown / PDF）
- 若使用合成数据，需要描述生成方式

---

祝你顺利完成期末项目！你可以随时让我生成自动化脚本、数据生成脚本或报告模板。  
