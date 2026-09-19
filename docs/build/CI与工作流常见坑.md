# CI 与工作流常见坑（PITFALLS: CI / GitHub Actions）

> 本项目长期建设用。新增工作流或改构建脚本前先浏览本文件；踩到新坑请追加，并注明"日期 / 场景"。
> 配套：`脚本编写常见坑.md`（脚本转义 / subprocess / pandoc）、`dsh_更新SOP.md`（版本更新流程）。

## A. 工作流 YAML 与表达式

### A1. GitHub 表达式只认单引号（2026-09-19 真实事故）

- **症状**：push 后出现一条运行记录，**名字就是文件路径**（如 `.github/workflows/xxx.yml`）、**没有 job**、瞬间失败。
- **原因**：`if: steps.check.outcome == "failure"` —— YAML 合法，但 GitHub 表达式语法只接受**单引号**字符串。
- **处理**：改成 `if: steps.check.outcome == 'failure'`。
- **诊断手段**：`actionlint`（见 D1）；或 `gh run view <id> --log-failed`。
- **预防**：任何新工作流先跑 actionlint，再 push。

### A2. `on:` 的 YAML 1.1 解析差异

- PyYAML 会把裸键 `on:` 解析成布尔 `True`（本地校验时 `d["on"]` 会 KeyError），但 GitHub 自己解析正常。
- **预防**：本地校验用 `d.get(True) or d.get("on")`，不要据此判定工作流非法。

## B. CI 环境与依赖

### B1. CI 缺依赖导致整步失败（2026-09-19）

- **症状**：本地一切正常；CI 的"Build"步骤失败，日志显示 `ModuleNotFoundError: No module named 'fitz'`。
- **原因**：新增的 `check_pdf_layout.py` 依赖 PyMuPDF，而 CI 的 `pip install` 列表没加。
- **处理（两手都要）**：① 工作流补依赖 `pip install ... pymupdf`；② 脚本**优雅降级**：

```python
try:
    import fitz
except ImportError:
    print("check_pdf_layout: PyMuPDF 未安装，跳过版式自检")
    sys.exit(0)
```

- **预防**：凡进入 `update_all.py` 的步骤，其依赖必须出现在 CI 安装列表里；可选依赖一律 try/except。

### B2. 中文字符打印导致 GBK 崩溃

- **症状**：Windows 本地/CI 上脚本在打印中文或特殊字符（如 ⏱）时抛 `UnicodeEncodeError`。
- **处理**：入口处统一加：

```python
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
```

- **预防**：所有构建脚本（texbook / emit_tex / pdf_build / part_pdf / check_*）都要有这段守卫；
  正文避免使用字体缺失的字形（如 ⏱），改用文字标记（"时效内容（基线 …）"）。

### B3. 字体差异：CI 与本地排版不同

- 本地 Windows 用 Microsoft YaHei；CI（Ubuntu）用 Noto CJK（由 `build/fonts.py` 自动选择）。
- **后果**：同一份 md 在 CI 与本地生成的 PDF **页数/换行可能不同**。
- **对策**：
  1. 页数表（`教材PDF/README.md`）以**构建产物**为准，不要手写估算；
  2. 版式自检分级：**图片越界 = 硬错**（与字体无关）；**文本超右边界 = 软告警**（字体相关），CI 上不阻断；
  3. 不要写死字体名，统一走 `fonts.py`。

## C. 产物与路径

### C1. artifact glob 漏文件（静默失败）

- **症状**：新增章节后 CI"成功"，但 artifact 里找不到该章 PDF。
- **原因**：上传路径写的是 `docs/教材PDF/0*-*.pdf`，匹配不到 `10-*` / `11-*` / `12-*`。
- **处理**：改为 `0*-*.pdf` + `1*-*.pdf`，再加部分合并 PDF（`第二部分*.pdf`）。
- **预防**：新增章节后，回头确认 CI 的 artifact glob 与触发路径都覆盖到了。

### C2. 触发路径（paths）决定"为什么没重建"

- `texbook.yml` 只在 `docs/chapters/**`、`docs/build/**`、`docs/教材PDF/README.md`、工作流文件变更时触发；
- 改 `docs/教学资源/**` 只会触发 Pages，不会重建 PDF —— 这**不是** CI 坏了。

### C3. 生成物缓存导致的"改了没生效"

- `emit_tex.py` / `texbook.py` 用 md 哈希做缓存：**只改脚本不改 md** 时不会重生成章节文件。
- **真实事故**：修好 part 标注重叠后，`ch09-agent-basics.tex` 仍残留旧的 `\part{...}`，因为哈希未变。
- **处理**：脚本行为变更后用 `python build/emit_tex.py --force`（或删缓存文件）再验证。

## D. 诊断工具箱

### D1. actionlint（推荐，静态校验）

```bash
# 一次性下载（Windows 示例）
curl -sL -o /tmp/al.zip "https://github.com/rhysd/actionlint/releases/download/v1.7.12/actionlint_1.7.12_windows_amd64.zip"
cd /tmp && unzip -o al.zip && ./actionlint.exe -version

# 校验全部工作流
/tmp/al/actionlint.exe .github/workflows/*.yml
```

### D2. gh CLI（读真实失败日志）

```bash
gh run list --limit 10                       # 最近运行与结论
gh run view <run-id> --log-failed | tail -60 # 只看失败步骤的日志
gh run view <run-id> --json jobs --jq ".jobs[].steps[] | {name, conclusion}"
```

> 本机 `gh` 已登录（账号 huahbo），可直接读私有/公开运行的日志；比翻网页快得多。

### D3. 新增工作流的验证套路

1. actionlint 静态校验；
2. 给该工作流加一条临时 `push: paths: [该文件]` 触发；
3. push 后用 `gh run list` 看结论；
4. 通过后按需保留/移除临时触发（巡检类工作流建议保留自测触发）。

## E. 版式自检（check_pdf_layout.py）使用要点

- **硬错**：图片越界（bbox 触碰页边）→ 必须修（通常是图片过高或浮动到页底）。
- **软告警**：文本超右边界 3–10pt → 多为字体差异或 CJK 标点悬挂（悬挂不计错）；>10pt 且含 ASCII 才算硬错。
- **不要用 pandoc/xelatex 的 .log 判断**：pandoc 成功后会删除日志，"没有日志"≠"没有 overfull"。要判断就跑真实渲染（fitz 读 PDF）。
- 修图顺序：先看 `float` 放置与图片高度上限（`\floatplacement{figure}{tp}` + `0.70\textheight`），再看代码块折行（fvextra），最后看长 URL/长等宽串（xurl + hyphenat）。

## F. 本机工具链：Hindsight 记忆服务（2026-09-19）

### F1. 症状与定位

- 现象一：`hindsight_*` 工具全部 401 —— `Authentication failed: API key required (no apiToken is configured)`。
  说明插件跑在默认的 **cloud** 模式但没配 token。
- 现象二：切到本地 daemon 模式后仍起不来，`~/.hindsight/profiles/<profile>.log` 末尾：
  `RuntimeError: Failed to start embedded PostgreSQL after 5 attempts. Last error: Error: initdb failed`。
  **注意**：此时 LLM 通道往往是好的（日志里有 `Connection verified: deepseek/deepseek-flash`），坏的是嵌入式 PostgreSQL（pg0）在本机 initdb 失败。

### F2. 本机采用的方案（Docker 自托管）

```bash
# 数据面 8888 / 控制面 9999；用 DeepSeek 做事实抽取（Key 取 ~/.dsh/.credentials.yaml 的 refs.DEEPSEEK_API_KEY）
docker run -d --name hindsight --restart unless-stopped -p 8888:8888 -p 9999:9999 \
  -e HINDSIGHT_API_LLM_PROVIDER=deepseek \
  -e HINDSIGHT_API_LLM_API_KEY=$DEEPSEEK_API_KEY \
  -e HINDSIGHT_API_LLM_MODEL=deepseek-flash \
  ghcr.io/vectorize-io/hindsight:latest

# 验证
curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8888/health   # 期望 200
```

启动器 `~/.dsh/dshweb.ps1` 在拉起 dsh web 之前导出：

```powershell
$env:HINDSIGHT_SERVER_MODE = 'self-hosted'
$env:HINDSIGHT_API_URL = 'http://127.0.0.1:8888'
```

### F3. 排查顺序（下次直接照做）

1. `curl -s http://127.0.0.1:8888/health` → 不通就先看 `docker ps --filter name=hindsight` 与 `docker logs --tail 30 hindsight`；
2. 容器正常但工具仍 401 → 确认 dsh web 进程**重启过**（插件只在启动时读环境变量）；
3. 想知道插件实际认为的配置 → 看 `~/.hindsight/coding-agents-logs/plugin.log`；
4. 本地 daemon 模式的日志在 `~/.hindsight/profiles/<profile>.log`，配置在 `~/.hindsight/profiles/<profile>.env`（**含明文 Key**，别提交/截图）。

### F4. 其他坑

- `hindsight-embed` CLI 的输出含 ✓ 等字符，GBK 控制台直接 print 会 `UnicodeEncodeError`，脚本先 `sys.stdout.reconfigure(encoding="utf-8", errors="replace")`；
- PowerShell `Start-Process` 在本机因 `NO_PROXY`/`no_proxy` 键冲突报 `Item has already been added`，改用 node `spawn(..., {detached:true})` 或在子进程 env 里删掉重复变量；
- 容器务必加 `--restart unless-stopped`，否则重启后记忆服务不会自己回来。
