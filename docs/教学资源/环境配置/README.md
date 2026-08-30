# 教学环境配置（第 0 章配套）

> 本目录是《Python 科学计算》课程**统一环境**的标准文件。学生在第 0 章上机时按 `00-02-统一环境安装与自检` 使用；教师可把本目录整体发给学生或放在机房镜像里。

## 文件说明

| 文件 | 用途 |
| ---- | ---- |
| `environment.yml` | conda 环境定义（python 3.12 + 全部课程库），一键重建 `scicomp` |
| `requirements.txt` | pip 等价清单（不想用 conda 时的备选） |
| `check_env.py` | 环境自检脚本：库版本 + `xelatex`/`latexmk`/`git` 是否存在 |
| `vscode-settings.json` | VS Code 共享配置（解释器选择、Jupyter 根目录、LaTeX Workshop 一键编译） |
| `README.md` | 本说明 |

## 快速开始

```powershell
# 1. 创建环境（在课程目录下）
conda env create -f environment.yml

# 2. 激活
conda activate scicomp

# 3. 自检
python check_env.py

# 4. 打开 VS Code，选择解释器 / 内核为 scicomp
```

> 不用 conda 的同学：`conda create -n scicomp python=3.12 -y && conda activate scicomp && pip install -r requirements.txt`。

## VS Code 配置说明

- `python.defaultInterpreterPath`：请把路径改成你机器上 scicomp 环境的 python.exe（或删掉这行，改用 `Python: Select Interpreter`）；
- `jupyter.notebookFileRoot`：让 notebook 的相对路径以项目根为基准；
- `latex-workshop.latex.recipes`：中文 LaTeX 统一用 `latexmk -xelatex`；
- 把本文件内容合并进 `设置（JSON）`即可，不要直接覆盖已有设置。

## 自检通过标准

- Python ≥ 3.10（建议 3.12）；
- 9 个核心库全部有版本号（numpy/sympy/scipy/pandas/matplotlib/seaborn/networkx/statsmodels/scikit-learn）；
- `xelatex`、`latexmk` 能找到（找不到时用 Overleaf / LoongTeX 在线平台过渡）；
- `git` 缺失仅警告（可选）。

## 常见问题

见第 0 章正文 `00-02-统一环境安装与自检.md` 的“常见问题与排错”表。
