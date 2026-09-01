# 🔑 JetBrains 激活码生成器

仅供学习研究 · 请支持正版 · 三步完成激活

本仓库包含两样东西：

- **ja-netfilter.zip** —— 本地 Java 代理工具，让 IDE 接受自定义激活码
- **index.html** —— 激活码生成页面（纯静态，浏览器本地生成 RSA 签名激活码，已部署到 Vercel）

## 支持范围

支持 JetBrains 全系列 14 款产品 + 所有付费插件：

IntelliJ IDEA、PhpStorm、DataGrip、RubyMine、WebStorm、Rider、CLion、PyCharm、GoLand、DataSpell、dotMemory、Aqua、RustRover、AppCode

- **不勾选任何产品** = 一个激活码激活全部产品（全家桶模式）
- **勾选特定产品** = 只激活你需要的

💡 激活后，你电脑上所有已安装的 JetBrains IDE 都会自动识别，无需每个 IDE 单独操作。

## 在线工具地址

| 线路 | 地址 | 说明 |
| --- | --- | --- |
| 线路一 | https://jetbrains-keygen.kkplayit.online/ | 国内直连 |
| 线路二 | https://jetbrains-keygen.vercel.app | 国内用户需要🪜访问 |

## 三步激活流程

### 步骤 1：下载 ja-netfilter 代理工具

ja-netfilter 是一个本地 Java 代理，让 IDE 接受自定义激活码。必须安装在你的电脑上。

1. 下载 [ja-netfilter.zip](ja-netfilter.zip)（311 KB，仓库内已附带，也可从在线工具页面下载）
2. 解压到任意目录（建议 `~/ja-netfilter/`），记住解压路径，下一步要用

### 步骤 2：配置 IDE 的 VM Options（最关键一步）

**方法 1：图形界面（推荐）**

1. 打开任意 JetBrains IDE
2. 菜单栏 → **Help** → **Edit Custom VM Options...**
3. 在弹出的文件末尾添加一行（把路径换成你的解压路径）：

```
-javaagent:/你的路径/ja-netfilter.jar
```

macOS 示例：

```
-javaagent:/Users/你的用户名/ja-netfilter/ja-netfilter.jar
```

**方法 2：手动编辑文件**

macOS/Linux 用户，终端执行：

```bash
echo -e '\n-javaagent:/你的路径/ja-netfilter.jar' >> "$HOME/Library/Application Support/JetBrains/产品名202x.x/产品名.vmoptions"
```

Windows 用户，PowerShell 执行：

```powershell
Add-Content "$env:APPDATA\JetBrains\产品名202x.x\产品名.vmoptions" "`n-javaagent:C:\你的路径\ja-netfilter.jar"
```

vmoptions 常见位置：

- macOS：`~/Library/Application Support/JetBrains/产品名/产品名.vmoptions`
- Windows：`%APPDATA%\JetBrains\产品名\产品名.vmoptions`

⚠️ 常见错误：

- 路径必须用你实际的解压路径，不能直接照抄
- 如果 IDE 打不开，说明路径填错了——删掉 vmoptions 文件重来
- 修改完后必须**完全退出 IDE 再重新打开**

### 步骤 3：生成激活码 & 激活 IDE

1. 打开在线工具：https://jetbrains-keygen.kkplayit.online/
2. 填写被授权人（默认 `User`，显示在 IDE 的 About 页面）、过期日期（默认 `2099-12-31`）
3. 选择产品（不选 = 全家桶全部激活）
4. 点击 **✨ 生成激活码**，复制生成的激活码
5. 打开 IDE（确保已完成步骤 2）→ 出现激活窗口 → 选择 **Activation code** → 粘贴 → 点 **Activate**

## 🤖 懒人通道：让 AI 帮你全部搞定

如果你有 Claude Code / Cursor / Hermes Agent / Copilot CLI 等 AI 编程助手，把下面这段话发给它，AI 会自动完成下载→解压→配置→激活全流程：

```
帮我配置 JetBrains IDE 的本地学习研究环境。
工具地址：https://jetbrains-keygen.kkplayit.online/
支持产品：IntelliJ IDEA、PhpStorm、DataGrip、RubyMine、WebStorm、Rider、CLion、PyCharm、GoLand、DataSpell、dotMemory、Aqua、RustRover、AppCode 等 JetBrains 产品，以及付费插件。
请先根据我的实际需求判断目标：
1. 如果我要使用某一个 JetBrains 产品，就在网页的产品列表里只勾选对应产品，然后生成激活码。
2. 如果我要使用全部 JetBrains 产品或全家桶，就不要勾选任何产品，直接生成可用于全部产品的激活码。
操作步骤：从 https://jetbrains-keygen.kkplayit.online/ 下载 ja-netfilter.zip 并解压；找到 IDE 的 vmoptions 文件；在文件末尾添加 -javaagent:解压路径/ja-netfilter.jar；重启 IDE；打开工具地址生成激活码；在 IDE 激活窗口选择 Activation code 并粘贴。
vmoptions 常见位置：macOS 在 ~/Library/Application Support/JetBrains/产品名/vmoptions，Windows 在 %APPDATA%\JetBrains\产品名\vmoptions。
如果我没有明确说要哪个产品，请先问我是要激活单个产品还是全部产品，不要默认选择某一个产品。被授权人名字可以先用 User。
```

## ⚖️ 免责声明

- **教育目的：** 本仓库及 ja-netfilter 工具仅供学习研究 Java Agent、字节码修改、RSA 签名等技术原理。禁止用于任何商业目的。
- **非官方：** 本项目与 JetBrains s.r.o. 无任何关联、赞助或授权关系。JetBrains、IntelliJ IDEA、DataGrip 等均为 JetBrains s.r.o. 的注册商标。
- **用户责任：** 使用本工具激活 JetBrains 产品的行为由用户自行承担全部法律责任。本项目仅提供技术研究工具，不鼓励、不提倡规避软件授权。如您用于商业或工作用途，请前往 [JetBrains 官方商店](https://www.jetbrains.com/store/) 购买正版授权，支持开发者持续改进产品。
- **无担保：** 本工具按"原样"提供，不提供任何明示或暗示的担保，包括但不限于适销性、特定用途适用性。工具可能因 JetBrains 版本更新而失效。
- **开源协议：** ja-netfilter 及本网站代码基于 MIT 协议开源，仅供非商业研究使用。

仅供学习与研究使用 · 请支持 [JetBrains](https://www.jetbrains.com/) 正版
