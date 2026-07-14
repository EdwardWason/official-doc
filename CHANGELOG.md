# Changelog

本文件记录 official-doc（gongwen-formatter）所有版本的变更。

格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
版本号遵循 [Semantic Versioning](https://semver.org/lang/zh-CN/)。

## [1.1.2] - 2026-07-14

### 安全升级（响应 ClawHub SkillSpector 审计）

#### Added
- `md_to_docx()` 新增 `download_images` 参数（默认 `True`），受限网络环境可设为 `False` 完全关闭网络请求
- `skill.md` 增加"权限声明"段落，按最小权限原则披露网络访问/文件读写/不读取环境变量/不调用 subprocess
- README 中英文版增加 "图片下载网络请求说明 / Network Access Disclosure for Image Download" 用户警告段落

#### Security
- `download_image()` 增加 URL scheme 白名单（仅 `http://`/`https://`/`data:image`），防止 SSRF
- 其他 scheme（`file://`、`ftp://` 等）静默跳过，不发起网络请求
- `requirements.txt` 改用 `~=` 兼容版本锁定（`python-docx~=1.1.0`、`markdown-it-py~=3.0.0`），平衡安全与兼容性

## [1.1.1] - 2026-07-13

#### Changed
- 添加 ClawHub 触发词：`公文格式转换`、`转换公文格式`
- ClawHub slug 改为 `gongwen-formatter`（`official-doc` 已被占用，`official-` 前缀受保护）
- 三平台同步发布（GitHub + ClawHub + SkillHub）

## [1.1.0] - 2026-07-12

#### Added
- 引入 `markdown-it-py` 解析器替代逐行 `split('\n')`，支持多行段落、嵌套列表
- `#` 标题智能判断：单个 `#` 视为大标题（居中不加序号），多个 `#` 视为一级标题（加序号）
- 首行缩进精确对齐国标（640 twips = 2个三号汉字宽度，1汉字=16pt=320twips）
- 新增表格、图片、超链接、代码块、嵌套列表支持
- 加粗文本（`**text**`）自动转为黑体
- 斜体文本（`*text*`）自动转为楷体

#### Fixed
- 黑体字体不再设置 `bold=True`（用户反馈"黑体不需要加粗处理"）
- 移除所有黑体/楷体的 `bold=True` 设置

## [1.0.0] - 2026-07-10

#### Added
- 初始版本：基于 GB/T 9704-2012 标准，将 Markdown 转换为党政机关公文格式 Word 文档
- 实现基础标题层级、段落、列表转换
- 国标页面设置：A4、上 3.7cm/下 3.5cm/左 2.8cm/右 2.6cm、行距 26pt
- 字体规范：方正小标宋/黑体/楷体_GB2312/仿宋_GB2312/宋体
