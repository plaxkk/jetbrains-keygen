# 🔑 JetBrains 라이선스 코드 생성기

[简体中文](README.md) | [English](README.en.md) | **한국어** | [Русский](README.ru.md)

학습·연구 전용 · 정품 사용을 권장합니다 · 3단계 설정

이 저장소에는 다음 파일이 포함되어 있습니다.

- **ja-netfilter.zip** — IDE가 사용자 지정 라이선스 코드를 인식하도록 하는 로컬 Java 에이전트
- **index.html** — 브라우저에서 RSA 서명 코드를 생성하는 정적 웹페이지. Vercel에서 호스팅합니다.
- **ko/index.html** — 검색 엔진이 JavaScript 실행 없이 읽을 수 있는 한국어 페이지

## 대상 제품

제품 목록에는 다음 JetBrains 제품 14종이 포함되어 있습니다.

IntelliJ IDEA, PhpStorm, DataGrip, RubyMine, WebStorm, Rider, CLion, PyCharm, GoLand, DataSpell, dotMemory, Aqua, RustRover, AppCode

- **아무 제품도 선택하지 않으면** 전체 제품용 코드를 생성합니다.
- **특정 제품만 선택하면** 선택한 제품용 코드를 생성합니다.

원본 프로젝트는 유료 플러그인 지원과 설치된 IDE의 자동 인식도 안내하고 있습니다. 제품 버전별 호환성은 별도로 확인해야 하며, 업데이트 후에는 작동하지 않을 수 있습니다.

## 온라인 도구

| 구분 | 주소 | 안내 |
| --- | --- | --- |
| 한국어 | https://jetbrains-keygen.kkplayit.online/ko/ | 한국어 페이지 |
| English | https://jetbrains-keygen.kkplayit.online/en/ | 영어 페이지 |
| 简体中文 | https://jetbrains-keygen.kkplayit.online/ | 중국어 간체 페이지 |
| 대체 주소 | https://jetbrains-keygen.vercel.app/ko/ | 중국 본토에서는 VPN이 필요할 수 있습니다. |

## 3단계 설정

### 1단계: ja-netfilter 에이전트 다운로드

ja-netfilter는 IDE가 사용자 지정 라이선스 코드를 인식하도록 하는 로컬 Java 에이전트입니다. 사용 중인 컴퓨터에 설치해야 합니다.

1. [ja-netfilter.zip](ja-netfilter.zip)을 다운로드합니다. 파일 크기는 약 311 KB이며, 온라인 도구 페이지에서도 다운로드할 수 있습니다.
2. 원하는 폴더에 압축을 해제합니다. 권장 경로는 `~/ja-netfilter/`입니다. 다음 단계에서 사용할 실제 경로를 확인해 두세요.

### 2단계: IDE의 VM Options 설정

**방법 1: IDE 메뉴에서 설정 (권장)**

1. JetBrains IDE를 실행합니다.
2. 메뉴에서 **Help** → **Edit Custom VM Options...**를 선택합니다.
3. 열린 파일의 마지막 줄에 아래 내용을 추가합니다. 예제 경로를 실제 압축 해제 경로로 바꿔 주세요.

```text
-javaagent:/path/to/ja-netfilter.jar
```

macOS 예시:

```text
-javaagent:/Users/your-username/ja-netfilter/ja-netfilter.jar
```

**방법 2: 파일 직접 편집**

아래는 macOS 터미널 예시입니다. 사용자 경로와 제품명은 실제 환경에 맞게 바꿔 주세요.

```bash
echo -e '\n-javaagent:/your-path/ja-netfilter.jar' >> "$HOME/Library/Application Support/JetBrains/ProductName202x.x/ProductName.vmoptions"
```

Windows PowerShell 예시:

```powershell
Add-Content "$env:APPDATA\JetBrains\ProductName202x.x\ProductName.vmoptions" "`n-javaagent:C:\your-path\ja-netfilter.jar"
```

vmoptions 파일의 일반적인 위치:

- macOS: `~/Library/Application Support/JetBrains/ProductName202x.x/ProductName.vmoptions`
- Windows: `%APPDATA%\JetBrains\ProductName202x.x\ProductName.vmoptions`

Linux에서는 위 macOS 경로를 사용하지 말고 IDE의 **Edit Custom VM Options...** 메뉴에서 실제 파일을 여세요.

설정 시 확인할 사항:

- 예제 경로를 그대로 사용하지 말고 실제 압축 해제 위치로 바꿔 주세요.
- 설정 후 IDE가 실행되지 않으면 추가한 javaagent 경로를 확인하세요. 해당 줄을 제거하면 기존 설정을 보존한 채 복구할 수 있습니다.
- 변경 후에는 **IDE를 완전히 종료한 뒤 다시 실행**해야 합니다.

### 3단계: 라이선스 코드 생성 및 IDE 활성화

1. [한국어 도구 페이지](https://jetbrains-keygen.kkplayit.online/ko/)를 엽니다.
2. 사용자 이름과 만료일을 입력합니다. 기본값은 `User`와 `2099-12-31`이며, 이름은 IDE의 About 화면에 표시됩니다.
3. 제품을 선택합니다. 전체 제품용 코드를 생성하려면 선택을 모두 해제하세요.
4. **✨ 라이선스 코드 생성**을 누른 뒤 생성된 코드를 복사합니다.
5. 2단계 설정을 마친 IDE를 실행합니다. 활성화 창에서 **Activation code**를 선택하고 코드를 붙여 넣은 다음 **Activate**를 누릅니다.

## 🤖 AI 코딩 도우미로 설정하기

Claude Code, Cursor, Hermes Agent, Copilot CLI 등의 AI 코딩 도우미를 사용한다면 아래 프롬프트로 다운로드, 압축 해제, 설정, 활성화 과정을 요청할 수 있습니다. 실행 전에 도우미가 제안하는 내용을 확인하세요.

```text
JetBrains IDE의 로컬 학습·연구 환경 설정을 도와주세요.
도구 주소: https://jetbrains-keygen.kkplayit.online/ko/
대상 제품: IntelliJ IDEA, PhpStorm, DataGrip, RubyMine, WebStorm, Rider, CLion, PyCharm, GoLand, DataSpell, dotMemory, Aqua, RustRover, AppCode 및 JetBrains 유료 플러그인.
먼저 제 사용 목적에 맞게 대상을 확인해 주세요.
1. 특정 제품 하나만 사용할 경우 웹페이지에서 해당 제품만 선택한 뒤 라이선스 코드를 생성해 주세요.
2. 전체 제품을 사용할 경우 아무 제품도 선택하지 않고 전체 제품용 코드를 생성해 주세요.
작업 순서: 도구 페이지에서 ja-netfilter.zip을 다운로드하고 압축을 해제합니다. IDE의 vmoptions 파일을 찾아 마지막 줄에 -javaagent:<압축해제경로>/ja-netfilter.jar를 추가합니다. IDE를 다시 실행하고 도구 페이지에서 코드를 생성한 뒤 활성화 창의 Activation code에 붙여 넣습니다.
vmoptions 경로 예시: macOS: ~/Library/Application Support/JetBrains/ProductName202x.x/ProductName.vmoptions; Windows: %APPDATA%\JetBrains\ProductName202x.x\ProductName.vmoptions.
제가 제품을 지정하지 않았다면 특정 제품 하나인지 전체 제품인지 먼저 물어봐 주세요. 임의로 선택하지 마세요. 사용자 이름은 별도 요청이 없으면 User로 지정해 주세요.
```

## ⚖️ 면책 안내

- **교육 목적:** 이 저장소와 ja-netfilter 도구는 Java 에이전트, 바이트코드 수정, RSA 서명 등의 기술 원리를 학습하고 연구하기 위한 용도로만 제공됩니다. 상업적 사용은 금지됩니다.
- **비공식 프로젝트:** 이 프로젝트는 JetBrains s.r.o.와 제휴 관계가 없으며, 해당 회사의 후원이나 승인을 받지 않았습니다. JetBrains, IntelliJ IDEA, DataGrip 등의 명칭은 JetBrains s.r.o.의 등록 상표입니다.
- **사용자 책임:** 이 도구를 사용해 JetBrains 제품을 활성화하는 행위에 대한 법적 책임은 사용자에게 있습니다. 이 프로젝트는 기술 연구 도구를 제공하며 소프트웨어 라이선스 우회를 권장하거나 지지하지 않습니다. 업무 또는 상업적 용도로 사용하는 경우 [JetBrains 공식 스토어](https://www.jetbrains.com/store/)에서 정품 라이선스를 구매해 주세요.
- **보증 없음:** 이 도구는 있는 그대로 제공됩니다. 상품성이나 특정 목적에 대한 적합성을 포함해 어떠한 명시적·묵시적 보증도 제공하지 않습니다. JetBrains 제품이 업데이트되면 도구가 작동하지 않을 수 있습니다.
- **소스 코드:** 원본 프로젝트는 ja-netfilter와 웹사이트 코드를 MIT 라이선스 기반의 비상업적 연구용으로 안내하고 있습니다. 실제 사용 시 각 구성 요소의 라이선스를 확인하세요.

## 번역 페이지 유지보수

중국어 원본은 `index.html`, 영어와 한국어 번역은 `locales/en.json`, `locales/ko.json`에서 관리합니다. 수정 후 아래 명령으로 정적 페이지와 사이트맵을 다시 생성하세요.

```bash
python3 scripts/build-locales.py
```

`en/index.html`과 `ko/index.html`은 생성 파일입니다. 직접 편집하지 마세요. 동적으로 표시되는 알림과 AI 프롬프트는 원본 `index.html`에서 관리합니다.

학습·연구 전용 · [JetBrains](https://www.jetbrains.com/) 정품 사용을 권장합니다.
