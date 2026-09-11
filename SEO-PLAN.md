# SEO 检查与执行记录

检查日期：2026-09-11。主站：https://jetbrains-keygen.kkplayit.online/

## 最新执行状态（2026-09-11）

- 已发布到 Vercel 生产环境，中文 `/`、英文 `/en/`、韩语 `/ko/` 均返回 HTTP 200，线上 HTML 与本地生成结果一致。
- 三种语言均提供静态正文、独立 canonical、相互 hreflang、对应语言的标题、摘要与 JSON-LD。站点地图包含三个页面。
- 新增 README.ko.md，中英韩 README 互相链接。翻译源位于 locales/；执行 `python3 scripts/build-locales.py` 重新生成英文、韩语页面和 sitemap.xml。生成文件随源码提交，修改源文件后须先重新生成再发布。
- Bing 站点已通过 HTML 标签验证。已通过 IndexNow 提交三个页面，接口返回 HTTP 202（接收成功，等待密钥验证；不等于已收录）。公开验证文件为 `/indexnow-key.txt`。Bing 站点地图后台提交待完成。
- Naver 验证标签已上线，站点验证停在图形验证码，需要用户完成后继续提交站点地图与页面收集请求。
- 本地验证：50 个翻译键完整覆盖；各语言 canonical/hreflang 一致；HTML ID 无重复；英文、韩语正文无残留中文（语言导航除外）；内联 JS 语法通过；构建可重复。Chrome 验证韩语步骤展开、生成结果、英文切换，390px 宽度无横向溢出。

以下为首次检查时的基线与建议；与最新执行状态冲突时，以本节为准。

## 已确认的问题与本次修复

线上首页返回 HTTP 200，HTML 包含正文，未发现响应头禁止索引；这说明页面可以被获取，不代表 Google 已收录。线上 robots.txt 和 sitemap.xml 返回 NOT_FOUND。首页缺少 description、canonical 和分享元数据。代码中英文通过 JavaScript 按浏览器语言及本地偏好切换，共用同一网址。

本次代码补充：

- HTML 中的 description 和指向主域名的 canonical。
- Open Graph、Twitter 摘要卡片元数据；语言切换同步标题、摘要和 locale。
- WebSite JSON-LD，名称明确为非官方项目，不声明 JetBrains 为发布者。
- robots.txt 与仅包含真实首页的 sitemap.xml。
- main 主内容语义标签。

这些改动需要部署才会生效。未提交搜索引擎、未检测实际收录、未测量 Core Web Vitals，也没有关键词搜索量或外链数据，不给出无依据的综合评分和流量预测。

## 后续优先级

| 优先级 | 工作与原因 | 依赖 | 验证方式及观察指标 |
| --- | --- | --- | --- |
| P1 | 部署基础配置，明确主网址并提供 sitemap 发现入口 | 本次改动发布 | 首页、robots.txt、sitemap.xml 均返回 200；查看网页源代码确认 canonical；GSC 站点地图显示读取成功 |
| P1 | 在 Google Search Console 验证站点并提交 sitemap，检查真实收录问题 | 站点管理权限与部署 | URL 检查中的抓取状态、Google 选择的规范网址、索引状态；若未收录，依报告原因继续排查 |
| P1 | 审核“全系列 14 款产品 + 所有付费插件”等宽泛承诺，标明实际验证的产品、版本、系统及日期 | 维护者提供实际测试记录 | 每项兼容性主张可对应验证记录；未验证项不写确定性保证 |
| P2 | 英文设独立 /en/ 静态页面；中文与英文各自 self-canonical、互相 hreflang，并用可抓取链接切换 | 确认英文获客需求，建立可维护的静态生成流程 | 禁用 JS 仍能获取各自完整语言正文；GSC 分页查看曝光；只加 hreflang 而没有独立页面不算完成 |
| P2 | 补充具有独立价值的技术文章，例如 RSA 签名原理、Java Agent 的工作机制与隔离实验 | 有可复现的原创实验、作者与日期信息 | 用独立 URL、正文内链连接，按主题观察曝光与点击；不批量生成只替换 IDE 名称的页面 |
| P2 | 测量移动端加载，重点检查 head 中同步加载的 forge 脚本 | PageSpeed/Lighthouse 或真实用户监测 | 对比修改前后 LCP、INP、CLS；任何延迟加载方案须验证点击生成时依赖已就绪 |
| P3 | 制作真实站点分享图并添加 og:image，改善分享预览 | 已确认的品牌与视觉素材 | 社交平台抓取预览可读取图片、标题、摘要；分享元数据本身不保证搜索排名提升 |

## 搜索意图与内容边界

首页承接现有工具名称与学习研究意图；正文保留明确的非官方身份及使用限制。技术内容围绕真实实验与解释，避免“官方授权”“永久有效”“全部版本可用”等无证据说法。不要把为搜索引擎撰写的大段重复关键词堆入工具界面。

当前英文切换只是交互功能，新增的动态英文元数据不能替代独立英文页面。备用 vercel.app 域名保留访问用途；相同 HTML 中的主域名 canonical 用于表达规范版本偏好，不强制用户跳离备用站。

## 发布后验收

1. 检查主页源代码中的 description、canonical 和 JSON-LD，确保不含预览部署域名。
2. 访问 /robots.txt 与 /sitemap.xml，确认返回正确正文和 200 状态码，而非错误页。
3. 使用 GSC 的实时 URL 检查与站点地图报告；未有账号权限前，不声称已经提交或收录。
4. 按周记录搜索曝光、点击、查询词和落地页；以 2–4 周作为初次复盘窗口，不承诺固定收录时间。

## 官方参考

- Google 规范网址说明：https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- Google 多语言站点说明：https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites

canonical 与 sitemap 是规范网址信号，并不保证 Google 采用或收录；独立语言 URL 才能为多语言抓取与索引提供清晰入口。
