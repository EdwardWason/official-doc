# 📄 Official Doc - 公文格式转换

---

## v1.0.0 (2026-04-30)

### 🎉 首次发布

正式发布公文格式转换技能 v1.0.0，为 LLM + AI Agent 生态提供专业的党政机关公文格式转换能力。

### ✨ 新增功能

| 功能 | 描述 |
|------|------|
| Markdown 转 Word | 支持完整的 Markdown 语法解析和转换 |
| GB/T 9704-2012 标准 | 严格遵循党政机关公文格式国家标准 |
| 4 级标题编号 | 自动编号大标题、一级、二级、三级标题 |
| 中文引号转换 | 自动将英文引号转换为中文引号 |
| 智能格式处理 | 支持加粗、列表等格式的正确转换 |

### 📋 格式规范

**页面设置**
| 设置项 | 规范值 |
|--------|--------|
| 上边距 | 3.7cm |
| 下边距 | 3.5cm |
| 左边距 | 2.8cm |
| 右边距 | 2.6cm |
| 行间距 | 固定值 26 磅 |
| 首行缩进 | 3 字符 |

**字体设置**
| 元素 | 字体 | 字号 | 加粗 |
|------|------|------|------|
| 大标题 | 方正小标宋简体 | 二号 | ❌ |
| 一级标题 | 黑体 | 三号 | ❌ |
| 二级标题 | 楷体_GB2312 | 三号 | ✅ |
| 三级标题 | 仿宋_GB2312 | 三号 | ✅ |
| 正文 | 仿宋_GB2312 | 三号 | ❌ |
| 页码 | 宋体 | 四号 | ❌ |

### 🤝 支持的 AI Agent

- ✅ OpenClaw
- ✅ Hermes Agent
- ✅ Claude Code
- ✅ 其他标准 Python 环境

### 📊 应用场景

- 定时任务自动生成工作简报
- 行业研报批量格式转换
- 会议纪要标准化输出
- 工作动态周报/月报自动生成

### 🚀 安装方式

```bash
# 方式一：下载 Release 包
unzip official-doc-v1.0.0.zip
cd official-doc
pip install -r requirements.txt

# 方式二：克隆仓库
git clone https://github.com/EdwardWason/official-doc.git
cd official-doc
pip install -r requirements.txt
```

### 📖 使用示例

```python
from official_doc import md_to_docx

md_content = """# 工作简报

## 一、上周工作总结

本周完成了系统升级任务。
"""

success = md_to_docx(md_content, "工作简报_公文格式.docx")
print("转换成功" if success else "转换失败")
```

---

## 🔗 项目链接

- **GitHub**: https://github.com/EdwardWason/official-doc
- **Release**: https://github.com/EdwardWason/official-doc/releases
- **README**: https://github.com/EdwardWason/official-doc/blob/main/README.md

---

*Built with ❤️ for LLM + AI Agent 生态*
