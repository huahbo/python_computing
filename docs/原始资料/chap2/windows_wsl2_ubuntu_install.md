# Windows 10/11 下安装 WSL2 与 Ubuntu 指南

**本指南详细说明如何在 Windows 系统中启用 WSL2 并安装 Ubuntu。**

---
**参考文章链接，建议先看下链接**
 子系统的图形界面有兴趣的可以参考安装，刚开始不建议
- https://developer.aliyun.com/article/1675612
- https://zhuanlan.zhihu.com/p/3409048098
- https://www.bilibili.com/video/BV1qbQGYPEg7/?vd_source=df52c49e1f5fe50eef9fd05379f6835d


---
## 一、检查系统版本与前提条件
1. **系统版本**：  
   - Windows 10 版本需 ≥ 2004 (内部版本 19041)  
   - 或 Windows 11（推荐，内置更好的 WSL 支持）

2. **CPU 虚拟化**：  
   - 在 BIOS/UEFI 中启用 Intel VT-x 或 AMD-V

3. **管理员权限**：  
   - 后续步骤需在管理员身份的 PowerShell / CMD 中执行

---
## 二、启用 Windows 功能

在 PowerShell（管理员）中运行以下命令：

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

执行完成后，**重启电脑**。

---
## 三、安装 WSL 与 Ubuntu

### 方法 A：Windows 11 / 新版 Windows 10（推荐）
直接在 PowerShell 中运行：

```powershell
wsl --install -d Ubuntu-22.04
```

说明：
- `wsl --install` 会自动安装所需组件并下载 Ubuntu
- 可以用 `wsl --list --online` 查看可安装的发行版

### 方法 B：旧版 Windows 10（手动安装）
1. 安装 WSL2 内核更新包（MS 官方下载）：  
   https://aka.ms/wsl2kernel

2. 设置默认版本为 WSL2：
```powershell
wsl --set-default-version 2
```

3. 打开 Microsoft Store，搜索并安装 **Ubuntu**（建议 Ubuntu 20.04 或 22.04 LTS）。

---
## 四、常用命令

- 查看已安装的发行版：
```powershell
wsl -l -v
```
- 设置默认发行版：
```powershell
wsl --set-default <DistroName>
```
- 更新 WSL：
```powershell
wsl --update
```
- 关闭所有 WSL 实例：
```powershell
wsl --shutdown
```

---
## 五、常见问题与解决方法

1. **提示缺少内核**：  
   安装内核更新包 https://aka.ms/wsl2kernel

2. **wsl.exe 未识别**：  
   确认已启用 `Windows Subsystem for Linux` 功能，并在重启后再试。

3. **版本转换失败**：  
   确认已启用 CPU 虚拟化，并检查磁盘空间是否充足。

---
## 六、推荐工具

- **Windows Terminal**：多标签终端，支持 PowerShell/WSL
- **VS Code + Remote - WSL 插件**：可在 VS Code 中直接开发 WSL 环境内的代码

---
## 七、完成安装后的首次运行

首次启动 Ubuntu 时会提示：
- 设置用户名和密码  
- 初始化环境

至此，你已完成 Windows 下 WSL2 + Ubuntu 的安装。


