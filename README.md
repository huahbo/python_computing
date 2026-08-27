# Python 科学计算（课程项目）

本仓库是《Python 科学计算》课程的**教材与配套资源**（私有）。内容源为 Markdown，所有 PDF 均由脚本/CI 从 md 生成。

## 目录

- `docs/`：课程内容（docsify 在线教程 + 构建体系）
  - `docs/chapters/`：**新版教学内容**（每章：正文/案例/误区/练习/上机/参考/教学说明）
  - `docs/原始资料/`：旧版原始内容归档（只读）
  - `docs/教学资源/`：课时表、期末大作业、LaTeX 模板等
  - `docs/教材TeX/`：**可编译 LaTeX 工程**（生成物，可编辑定制区 user_style/user_meta）
  - `docs/build/`：构建脚本、实施计划、设计文档、坑清单
  - `docs/教材PDF/`：生成的每章/全书 PDF（**被 .gitignore 忽略**，由 CI/脚本生成）
- `.github/workflows/texbook.yml`：CI（push 后自动校验 + 生成 PDF/TeX 并上传 artifact）

## 常用命令

```bash
# 一键全家桶：校验 → 每章PDF → 全书PDF（+ --tex 生成TeX工程；--tex-compile 顺带编译）
python docs/build/update_all.py --tex

# 仅全书 PDF
python docs/build/texbook.py --full

# 仅生成/刷新可编译 TeX 工程
python docs/build/emit_tex.py --compile
```

## 说明

- 单源原则：只改 `docs/chapters/**/*.md`；产出（PDF/TeX/图）皆为生成物。
- LaTeX 封面/样式定制：`docs/教材TeX/user_style.tex`、`docs/教材TeX/user_meta.yaml`。
- 详细实施计划：`docs/build/实施计划.md`；构建设计：`docs/build/texbook_design.md`、`docs/build/tex_source_mode_design.md`。
