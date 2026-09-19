# -*- coding: utf-8 -*-
"""Check upstream dsh releases against docs/build/dsh_version.yaml.

Usage:
  python build/check_dsh_release.py          # human readable report
  python build/check_dsh_release.py --ci     # write report file; exit 3 when a new version is found

Exit codes: 0 = up to date / unknown, 3 = new upstream version found (CI opens an issue).
"""
import argparse, io, json, os, sys, urllib.request
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSION_FILE = os.path.join(ROOT, "build", "dsh_version.yaml")
REPORT_FILE = os.path.join(ROOT, "build", "_dsh_release_report.md")
MARKER = "时效内容（基线"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def fetch_json(url, timeout=45):
    req = urllib.request.Request(url, headers={"User-Agent": "dsh-release-watch", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", "replace"))


def npm_tags(pkg):
    data = fetch_json("https://registry.npmjs.org/" + pkg.replace("/", "%2F"))
    return data.get("dist-tags", {}), data.get("time", {})


def gh_releases(repo, limit=5):
    url = "https://api.github.com/repos/" + repo + "/releases?per_page=" + str(limit)
    try:
        rels = fetch_json(url)
    except Exception as e:
        return [], str(e)
    out = []
    for r in rels:
        body = (r.get("body") or "").strip().replace(chr(13), "")
        out.append({"tag": r.get("tag_name", ""), "date": (r.get("published_at") or "")[:10],
                    "prerelease": bool(r.get("prerelease")), "notes": body[:400]})
    return out, ""


def timeliness_files():
    hits = []
    for base, _dirs, files in os.walk(os.path.join(ROOT, "chapters")):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(base, fn)
            try:
                t = io.open(p, encoding="utf-8").read()
            except Exception:
                continue
            if MARKER in t:
                hits.append(os.path.relpath(p, ROOT))
    return sorted(hits)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ci", action="store_true")
    args = ap.parse_args()

    cfg = yaml.safe_load(io.open(VERSION_FILE, encoding="utf-8"))
    base = cfg.get("baseline", {})
    up = cfg.get("upstream", {})
    baseline = str(base.get("version", ""))
    pkg = up.get("npm_package", "@deepseek-ai/dsh")
    repo = up.get("github_repo", "deepseek-ai/deepseek-harness")

    lines = ["# dsh 版本巡检报告", "",
             "- 基线版本：" + baseline + "（核对日期 " + str(base.get("checked_at", "?")) + "）",
             "- 上游包：" + pkg + " / 仓库：" + repo, ""]
    status = 0
    try:
        tags, times = npm_tags(pkg)
        lines.append("## npm dist-tags")
        lines.append("")
        for k in ("latest", "next", "alpha"):
            if k in tags:
                lines.append("- " + k + ": `" + str(tags[k]) + "`（发布 " + str(times.get(tags[k], "?"))[:10] + "）")
        latest = str(tags.get("latest", ""))
        lines.append("")
        if latest and latest != baseline:
            status = 3
            lines.append("## ⚠️ 发现新版本：latest = " + latest)
            lines.append("")
            lines.append("需要复核的文件（来自 dsh_version.yaml 的 review_on_change）：")
            lines.append("")
            for rel in cfg.get("review_on_change", []):
                lines.append("- [ ] " + rel)
            lines.append("")
            hits = timeliness_files()
            if hits:
                lines.append("正文中带时效标记的段落（grep 关键词：" + MARKER + "）：")
                lines.append("")
                for rel in hits:
                    lines.append("- [ ] " + rel)
                lines.append("")
        else:
            lines.append("## 结论：与基线一致（latest = " + (latest or "unknown") + "）")
            lines.append("")
    except Exception as e:
        lines.append("## npm 查询失败：" + str(e))
        lines.append("")

    rels, err = gh_releases(repo, 5)
    if err:
        lines.append("## GitHub Releases 查询失败：" + err)
    else:
        lines.append("## 最近发布（GitHub Releases）")
        lines.append("")
        for r in rels:
            flag = "pre-release" if r["prerelease"] else "release"
            lines.append("- `" + r["tag"] + "`（" + r["date"] + "，" + flag + "）")
        if rels:
            lines.append("")
            lines.append("### 最新一条更新说明（节选）")
            lines.append("")
            lines.append("```text")
            lines.append(rels[0]["notes"].strip() or "(空)")
            lines.append("```")
    lines.append("")
    lines.append("## 下一步")
    lines.append("")
    lines.append("按 `docs/build/dsh_更新SOP.md` 的八步执行；完成后更新 `dsh_version.yaml` 的 version / checked_at。")
    lines.append("")

    text = chr(10).join(lines)
    print(text)
    if args.ci:
        io.open(REPORT_FILE, "w", encoding="utf-8").write(text)
        print("[ci] 报告已写入 " + os.path.relpath(REPORT_FILE, ROOT))
    return status


if __name__ == "__main__":
    sys.exit(main())
