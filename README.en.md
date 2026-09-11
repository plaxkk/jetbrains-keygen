# 🔑 JetBrains Activation Code Generator

[简体中文](README.md) | **English** | [한국어](README.ko.md)

For learning & research only · Buy official licenses · Activate in 3 steps

This repository contains two things:

- **ja-netfilter.zip** — a local Java agent that lets your IDE accept a custom activation code
- **index.html** — the activation code generator page (pure static HTML; RSA-signed codes are generated locally in your browser; deployed on Vercel)

## Supported Products

All 14 JetBrains IDEs plus every paid plugin:

IntelliJ IDEA, PhpStorm, DataGrip, RubyMine, WebStorm, Rider, CLion, PyCharm, GoLand, DataSpell, dotMemory, Aqua, RustRover, AppCode

- **Tick nothing** = one code activates the entire family (all-in-one mode)
- **Tick specific products** = activate only what you need

💡 After activation, every JetBrains IDE already installed on your machine picks it up automatically — no per-IDE setup required.

## Online Tool

| Route | URL | Notes |
| --- | --- | --- |
| Route 1 | https://jetbrains-keygen.kkplayit.online/ | Direct access in mainland China |
| Route 2 | https://jetbrains-keygen.vercel.app | May require a VPN in mainland China |

## 3-Step Activation

### Step 1: Download the ja-netfilter agent

ja-netfilter is a local Java agent that makes the IDE accept a custom activation code. It must be installed on your machine.

1. Download [ja-netfilter.zip](ja-netfilter.zip) (311 KB — bundled in this repo, also available on the online tool page)
2. Unzip it anywhere (e.g. `~/ja-netfilter/`). Remember the path — you'll need it in the next step.

### Step 2: Configure the IDE's VM options (the most critical step)

**Method 1: GUI (recommended)**

1. Open any JetBrains IDE
2. Menu bar → **Help** → **Edit Custom VM Options...**
3. Append one line at the end of the file (replace the path with your actual unzip path):

```
-javaagent:/path/to/ja-netfilter.jar
```

macOS example:

```
-javaagent:/Users/your-username/ja-netfilter/ja-netfilter.jar
```

**Method 2: Edit the file manually**

macOS / Linux users, run in a terminal:

```bash
echo -e '\n-javaagent:/path/to/ja-netfilter.jar' >> "$HOME/Library/Application Support/JetBrains/<ProductName>202x.x/<ProductName>.vmoptions"
```

Windows users, run in PowerShell:

```powershell
Add-Content "$env:APPDATA\JetBrains\<ProductName>202x.x\<ProductName>.vmoptions" "`n-javaagent:C:\path\to\ja-netfilter.jar"
```

Common vmoptions locations:

- macOS: `~/Library/Application Support/JetBrains/<ProductName>/<ProductName>.vmoptions`
- Windows: `%APPDATA%\JetBrains\<ProductName>\<ProductName>.vmoptions`

⚠️ Common mistakes:

- Use your actual unzip path — do not copy the examples verbatim
- If the IDE won't start, the path is wrong — delete the vmoptions file and start over
- **Fully quit the IDE and reopen it** after editing

### Step 3: Generate the code & activate the IDE

1. Open the online tool: https://jetbrains-keygen.kkplayit.online/
2. Fill in the licensee (defaults to `User`; shown on the IDE's About page) and the expiry date (defaults to `2099-12-31`)
3. Select products (tick nothing = activate the whole family)
4. Click **✨ Generate** and copy the activation code
5. Open the IDE (make sure Step 2 is done) → the activation dialog appears → choose **Activation code** → paste → click **Activate**

## 🤖 The Lazy Path: Let an AI Agent Do Everything

If you use an AI coding assistant such as Claude Code, Cursor, Hermes Agent, Copilot CLI, paste the prompt below and the AI will run the whole flow for you: download → unzip → configure → activate.

```
Set up my local JetBrains IDE learning/research environment.
Tool URL: https://jetbrains-keygen.kkplayit.online/
Supported products: IntelliJ IDEA, PhpStorm, DataGrip, RubyMine, WebStorm, Rider, CLion, PyCharm, GoLand, DataSpell, dotMemory, Aqua, RustRover, AppCode, as well as paid plugins.
First decide the target based on my actual needs:
1. If I'm going to use a single JetBrains product, tick only that product in the product list on the page, then generate an activation code for it.
2. If I'm going to use all JetBrains products (the full family), tick nothing and generate one code valid for all products.
Steps: download ja-netfilter.zip from the tool URL and unzip it; locate the IDE's vmoptions file; append -javaagent:<unzip-path>/ja-netfilter.jar at the end of the file; restart the IDE; open the tool URL and generate the activation code; in the IDE activation dialog choose Activation code and paste it in.
vmoptions locations: macOS at ~/Library/Application Support/JetBrains/<ProductName>/vmoptions, Windows at %APPDATA%\JetBrains\<ProductName>\vmoptions.
If I haven't explicitly said which product I want, ask me whether I'm activating a single product or all products first — do not default to one product. Use "User" as the licensee name for now.
```

## ⚖️ Disclaimer

- **Educational purpose:** This repository and the ja-netfilter tool are provided solely for studying technical principles such as Java agents, bytecode modification, and RSA signing. Any commercial use is prohibited.
- **Not affiliated:** This project has no affiliation with, sponsorship from, or endorsement by JetBrains s.r.o. JetBrains, IntelliJ IDEA, DataGrip, and other names are registered trademarks of JetBrains s.r.o.
- **User responsibility:** You alone bear full legal responsibility for using this tool to activate JetBrains products. This project provides a technical research tool only and does not encourage or endorse circumventing software licensing. For commercial or work use, please purchase a license from the [JetBrains official store](https://www.jetbrains.com/store/) to support the developers.
- **No warranty:** This tool is provided "as is", without any express or implied warranty, including but not limited to merchantability or fitness for a particular purpose. The tool may stop working after JetBrains version updates.
- **Open source:** ja-netfilter and the site code are open source under the MIT license, for non-commercial research only.

For learning & research only · Please support [JetBrains](https://www.jetbrains.com/) with an official license

## Maintaining language pages

Chinese, English and Korean have independent pages at `/`, `/en/` and `/ko/`. Edit the Chinese source in `index.html` and translations in `locales/en.json` and `locales/ko.json`, then run:

```bash
python3 scripts/build-locales.py
```

This regenerates both translated static pages and the sitemap. Do not edit `en/index.html` or `ko/index.html` directly. Dynamic messages and AI prompts are maintained in `index.html`. Commit generated files before deployment.
