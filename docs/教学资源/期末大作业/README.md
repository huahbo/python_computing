# Python 科学计算项目模板说明

**前置要求（第 0 章已纳入）**

1. 完成第 0 章（`chapters/00-prep/`）：统一环境安装与自检、lab0、LaTeX 报告，能独立编译中文 PDF；
2. 完成第 1~8 章对应的 lab 与 quiz；
3. 学生自带笔记本电脑（BYOD），使用课程统一环境 `scicomp`（见 `教学资源/环境配置/`）。

---

推荐的项目目录结构如下：

- `data/`
  - `raw/`：原始数据（如 `ecommerce_orders.csv` 等）
  - `processed/`：清洗或中间处理后数据
- `notebooks/`：Jupyter Notebook 文件（如 `project1.ipynb`, `project2.ipynb`）
- `src/`
  - `project1/`：与 Project 1 相关的脚本代码
  - `project2/`：与 Project 2 相关的脚本代码
- `reports/`：最终报告（Markdown / PDF / PPT 等）
- `env/`：虚拟环境相关脚本（如创建虚拟环境的 `.bat` / `.sh` 文件）

你可以将本模板复制到任意位置，然后在其基础上填充自己的代码和数据。
