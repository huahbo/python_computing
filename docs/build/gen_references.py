# -*- coding: utf-8 -*-
"""Generate 附录 G 全书总参考文献 from per-chapter references.md.

Rule: 单一事实源 = 各章 references.md + 附录 references.md。
本脚本自动汇总、去重（按 URL）、标注“用于章节”，输出：
  docs/附录/数学算法附录/G-全书参考文献.md

Run: python build/gen_references.py
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DIR = os.path.join(ROOT, "附录", "数学算法附录")
OUT = os.path.join(APP_DIR, "G-全书参考文献.md")
MANIFEST = os.path.join(APP_DIR, "pdf_manifest.txt")
NL = chr(10)

CHAPTER_LABEL = {
    "00-prep": "第0章 前置基础",
    "01-numpy": "第1章 NumPy",
    "02-sympy": "第2章 SymPy",
    "03-scipy": "第3章 SciPy",
    "04-pandas": "第4章 Pandas",
    "05-matplotlib": "第5章 Matplotlib",
    "06-networkx": "第6章 NetworkX",
    "07-statsmodels": "第7章 Statsmodels",
    "08-sklearn": "第8章 scikit-learn",
}

def parse_table(path):
    """从 references.md 提取表格行: (title, url, desc, extra)。"""
    rows = []
    if not os.path.isfile(path):
        return rows
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    for line in lines:
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        url = ""
        for c in cells[1:]:
            m = re.search(r"https?://[^\s)\]>]+", c)
            if m:
                url = m.group(0).rstrip(".,;:") 
                break
        if not url:
            continue
        title = cells[0].strip() if len(cells) > 0 else ""
        if title in ("资料", "链接"):
            title = ""
        desc = cells[2].strip() if len(cells) > 2 else ""
        extra = cells[3].strip() if len(cells) > 3 else ""
        rows.append({"title": title or url, "url": url, "desc": desc, "extra": extra})
    return rows

def categorize(entry):
    s = (entry["title"] + " " + entry["url"] + " " + entry["desc"]).lower()
    official = ["python.org", "code.visualstudio.com", "numpy.org", "scipy.org",
                "docs.scipy.org", "sympy.org", "pandas.pydata.org", "matplotlib.org",
                "networkx.org", "statsmodels.org", "scikit-learn.org", "docs.jupyter.org",
                "docs.conda.io", "tug.org", "git-scm.com", "overleaf.com", "loongtex.com",
                "learnlatex.org", "ctan.org", "pypi.org", "anaconda.com"]
    if any(k in s for k in official) or ("官方" in s) or ("doc/" in s) or ("/reference" in s):
        return "一、官方文档与工具链"
    book = ["教材", "书", "《", "textbook", "handbook", "导论", "机器学习",
            "线性代数", "概率论", "数值分析", "算法导论", "周志华", "西瓜书", "thinkstats"]
    if any(k in s for k in book):
        return "二、教材与书籍"
    tutorial = ["教程", "课程", "课", "tutorial", "lecture", "course", "bootcamp",
                "learn", "入门", "指南", "scipy lectures", "lecture notes", "khan"]
    if any(k in s for k in tutorial):
        return "三、精品教程与课程"
    exercise = ["习题", "练习", "exercise", "100", "实战", "作业"]
    if any(k in s for k in exercise):
        return "四、习题与实战"
    if ("github.com" in s) or ("gitee.com" in s):
        return "五、开源项目与配套仓库"
    zh = ["中文", "镜像", "tuna", "china", "中文版", "站", "国产"]
    if any(k in s for k in zh):
        return "六、中文资料与镜像"
    return "七、其他"

def main():
    entries = {}
    for ch in sorted(os.listdir(os.path.join(ROOT, "chapters"))):
        cdir = os.path.join(ROOT, "chapters", ch)
        if not os.path.isdir(cdir):
            continue
        refs = os.path.join(cdir, "references.md")
        label = CHAPTER_LABEL.get(ch, ch)
        for r in parse_table(refs):
            key = r["url"].rstrip("/")
            if key not in entries:
                r["srcs"] = [label]
                entries[key] = r
            else:
                if label not in entries[key]["srcs"]:
                    entries[key]["srcs"].append(label)
    for r in parse_table(os.path.join(APP_DIR, "references.md")):
        key = r["url"].rstrip("/")
        if key not in entries:
            r["srcs"] = ["附录"]
            entries[key] = r
        else:
            if "附录" not in entries[key]["srcs"]:
                entries[key]["srcs"].append("附录")

    cats = ["一、官方文档与工具链", "二、教材与书籍", "三、精品教程与课程",
            "四、习题与实战", "五、开源项目与配套仓库", "六、中文资料与镜像", "七、其他"]
    by_cat = {c: [] for c in cats}
    for e in entries.values():
        by_cat[categorize(e)].append(e)
    for c in cats:
        by_cat[c].sort(key=lambda e: e["title"])

    lines = []
    lines.append("# 全书总参考文献（附录 G）")
    lines.append("")
    lines.append("> 本页由 `build/gen_references.py` **自动生成**，勿手改。单一事实源 = 各章 `references.md` + 附录 `references.md`；新增/删除引用后重新运行生成即可。")
    lines.append("> 速查方式：按类别浏览；每行“用于”列标注了哪些章节使用该资料，点章节链接可回正文。")
    lines.append("")
    total = len(entries)
    lines.append(f"共汇总 **{total} 条**（来自 9 个章节 + 附录）。")
    for c in cats:
        items = by_cat[c]
        lines.append("")
        lines.append("## " + c)
        lines.append("")
        if not items:
            lines.append("（暂无）")
            continue
        lines.append("| 资料 | 说明 | 用于 |")
        lines.append("| ---- | ---- | ---- |")
        for e in items:
            desc = (e["desc"] or "").replace("|", "／").replace("[", "（").replace("]", "）")
            used = "、".join(e["srcs"])
            title = (e["title"] or "").replace("|", "／").replace("[", "（").replace("]", "）")
            lines.append(f"| [{title}]({e['url']}) | {desc} | {used} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 按章节快速查找")
    lines.append("")
    lines.append("| 章节 | 直接查看该章参考 |")
    lines.append("| ---- | ---- |")
    for ch, lab in sorted(CHAPTER_LABEL.items()):
        link = f"../../chapters/{ch}/references.md"
        lines.append(f"| {lab} | [references.md]({link}) |")
    lines.append("")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(NL.join(lines))
    print("wrote", OUT, "(", total, "entries )")

    if os.path.isfile(MANIFEST):
        txt = open(MANIFEST, encoding="utf-8").read()
        if "G-全书参考文献.md" not in txt:
            with open(MANIFEST, "w", encoding="utf-8") as f:
                f.write(txt.rstrip() + NL + "G-全书参考文献.md" + NL)
            print("manifest updated")

if __name__ == "__main__":
    main()
