%% 由 build/emit_tex.py 生成（生成物，勿手改）；定制请放 user_style.tex / user_meta.yaml
# 教材TeX（可编译 LaTeX 工程）

- 由 build/emit_tex.py 生成；章节/正文/图均来自 chapters/。
- 可手改：user_style.tex（宏包/页眉/封面）、user_meta.yaml（标题/作者/日期）。
- 编译：cd 教材TeX && latexmk -xelatex main.tex。
- 刷新：python build/emit_tex.py [--check|--compile]。
- 手改且 md 未变的章节会保留（备份 _manual_backup/）。
