// Capture UI screenshots of dsh web for the textbook (headless Chromium, clean demo home).
// Usage:  NODE_PATH=<npx-cache>/node_modules node docs/build/capture_dsh_shots.cjs
const { spawn, execSync } = require("node:child_process");
const fs = require("node:fs");
const path = require("node:path");
const { chromium } = require("playwright");

const ROOT = path.dirname(path.dirname(__dirname));
const IMG = path.join(ROOT, "docs", "chapters", "09-agent-basics", "images");
const DEMO = process.env.DSH_DEMO_DIR || path.join(process.env.TEMP || "/tmp", "dsh-demo");
const HOME_DIR = path.join(DEMO, "home");
const WS_DIR = path.join(DEMO, "workspace");
const PORT = 3099;
const SHOTS = [];
let child = null;
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function shot(page, name) {
  const out = path.join(IMG, name);
  await page.screenshot({ path: out, type: "png" });
  SHOTS.push(name);
  console.log("[shot]", name);
}

async function clickAny(page, labels, timeout = 3500) {
  for (const n of [].concat(labels)) {
    for (const how of ["role", "text"]) {
      try {
        const loc = how === "role" ? page.getByRole("button", { name: n }).first() : page.getByText(n, { exact: false }).first();
        await loc.click({ timeout });
        console.log("[click:" + how + "]", n);
        return true;
      } catch (e) {}
    }
  }
  console.log("[miss]", [].concat(labels).join(" / "));
  return false;
}

(async () => {
  fs.mkdirSync(IMG, { recursive: true });
  fs.mkdirSync(WS_DIR, { recursive: true });
  try { execSync("taskkill /PID " + fs.readFileSync(path.join(DEMO, "web.pid"), "utf8").trim() + " /T /F", { stdio: "ignore" }); } catch (e) {}
  await sleep(1500);
  child = spawn("cmd", ["/c", "dsh web --port " + PORT + " --no-open"], {
    cwd: WS_DIR, env: { ...process.env, DSH_HOME: HOME_DIR }, stdio: ["ignore", "pipe", "pipe"],
  });
  let buf = "";
  child.stdout.on("data", (d) => { buf += d.toString(); });
  child.stderr.on("data", (d) => { buf += d.toString(); });
  let url = null;
  for (let i = 0; i < 30 && !url; i++) {
    await sleep(2000);
    const m = buf.match(new RegExp("http://127\\.0\\.0\\.1:" + PORT + "/\\?token=[A-Za-z0-9_\\-]+"));
    if (m) url = m[0];
  }
  if (!url) throw new Error("server did not print a token url");
  console.log("[server] ready");

  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1.5 });
  await page.goto(url, { waitUntil: "domcontentloaded" });
  await sleep(4000);

  // 1) 关掉首次进入的弹窗（内测声明 / API Key 引导），拿到干净首页
  await clickAny(page, ["稍后配置", "继续", "我知道了"]);
  await sleep(1500);
  await clickAny(page, ["稍后配置", "继续"]);
  await sleep(2000);
  await shot(page, "shot_web_home.png");

  // 2) 设置 → 模型
  if (await clickAny(page, ["设置", "Settings"])) {
    await sleep(2500);
    await clickAny(page, ["模型", "模型与密钥", "Models"]);
    await sleep(2500);
    await shot(page, "shot_settings_model.png");
    await page.keyboard.press("Escape").catch(() => {});
    await sleep(1500);
  }

  // 3) 工作区选择器（点了就截图，选不中也保留界面）
  if (await clickAny(page, ["选择工作区", "添加工作区"])) {
    await sleep(2500);
    await shot(page, "shot_workspace_picker.png");
    const inputs = await page.locator("input").all();
    for (const inp of inputs) {
      try {
        await inp.fill(WS_DIR);
        await inp.press("Enter");
        break;
      } catch (e) {}
    }
    await sleep(2500);
    await clickAny(page, ["选择文件夹", "确定", "打开"]);
    await sleep(2500);
  }

  // 4) 斜杠命令菜单（需要工作区已选中，选不中则跳过）
  try {
    const box = page.locator("textarea, [contenteditable=true]").first();
    await box.click({ timeout: 6000 });
    await page.keyboard.type("/", { delay: 150 });
    await sleep(1800);
    await shot(page, "shot_command_menu.png");
  } catch (e) { console.log("[skip] command menu"); }

  await browser.close();
  console.log("[done] shots:", SHOTS.join(", "));
})().catch((e) => { console.error("[fail]", e.message); process.exitCode = 1; }).finally(() => {
  if (child) { try { execSync("taskkill /PID " + child.pid + " /T /F", { stdio: "ignore" }); } catch (e) {} }
});
