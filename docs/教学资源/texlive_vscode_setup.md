# Windows 安装 TeX Live + VS Code LaTeX Workshop 全流程

## 1. 安装 TeX Live

### 方法一：在线安装（推荐）
1. 打开 [TeX Live 官网下载页](https://www.tug.org/texlive/acquire-netinstall.html)  
   下载 `install-tl-windows.exe`（大约 20MB）。  

2. 双击运行 `install-tl-windows.exe`。  

3. 在安装界面选择：
   - **默认安装**（推荐）：包含常用宏包，体积约 7~8GB。  
   - 安装路径建议保持默认：`C:\texlive\2024`。  

4. 点击 **安装**，等待下载和安装完成。  
   - 在线安装会逐个下载宏包，速度取决于网络和 CTAN 镜像源。  
   - 如果速度慢，可以在安装界面换一个镜像站点（如中国科大、中科院镜像）。  

### 方法二：离线 ISO 安装（适合网速快）
1. 前往 [CTAN 镜像站](http://mirrors.ctan.org/systems/texlive/Images/)，下载 `texlive2024.iso`（约 4GB）。  

2. 右键 ISO → 选择 **装载**，进入虚拟光驱。  

3. 运行 `install-tl-windows.bat`，选择 **完整安装**。  

---

## 2. 配置环境变量

通常安装器会自动配置环境变量，如果没有，请手动设置：

1. 按 `Win + R`，输入 `sysdm.cpl` → 回车。  
2. 在 **高级** → **环境变量** → 找到 **Path** → 编辑。  
3. 添加 TeX Live 的可执行文件路径，例如：  
   ```
   C:\texlive\2024\bin\win32
   ```  
4. 点击确定保存。

### 测试是否成功
打开 **命令提示符 (cmd)**，输入：
```bash
pdflatex --version
```
如果显示版本号，说明安装成功。

---

## 3. 安装 VS Code 与 LaTeX Workshop

1. 下载并安装 [Visual Studio Code](https://code.visualstudio.com/)。  
2. 打开 VS Code，进入 **扩展**（左边小方块图标）。  
3. 搜索并安装 **LaTeX Workshop** 插件。  

---

## 4. 配置 LaTeX Workshop

为了适配中文写作，推荐使用 **XeLaTeX** 编译。  

### 方法一：在 `.tex` 文件里指定
在文档开头加入：
```latex
% !TeX program = xelatex
```

### 方法二：全局配置
在 VS Code 里打开 **设置 (JSON)**，加入：
```json
"latex-workshop.latex.recipes": [
  {
    "name": "xelatex",
    "tools": ["xelatex"]
  }
],
"latex-workshop.latex.tools": [
  {
    "name": "xelatex",
    "command": "xelatex",
    "args": [
      "-synctex=1",
      "-interaction=nonstopmode",
      "-file-line-error",
      "%DOC%"
    ]
  }
],
"latex-workshop.view.pdf.viewer": "tab",
"latex-workshop.latex.autoBuild.run": "onSave"
```

这样，每次保存 `.tex` 文件都会自动编译并在 VS Code 内置 PDF 预览。

---

## 5. 验证安装

1. 新建一个文件 `main.tex`，输入：
   ```latex
   \documentclass{article}
   \usepackage{ctex} % 中文支持
   \begin{document}
   你好，世界！Hello, LaTeX!
   \end{document}
   ```

2. 保存后，LaTeX Workshop 会自动调用 **XeLaTeX** 编译，并生成 `main.pdf`。  
3. 在 VS Code 右侧即可看到 PDF 预览。  

---

✅ 至此，你的 **TeX Live + VS Code LaTeX 写作环境** 就搭建完成了。
