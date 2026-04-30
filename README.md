# Official Doc - 公文格式转换

> 将 Markdown 文档转换为符合 GB/T 9704-2012 党政机关公文格式的 Word 文档

## ✨ 核心价值

### 🤖 AI Agent 专用技能
专为各类 AI 智能体设计的文档格式转换技能，即下即用，无缝集成。

| 智能体平台 | 集成方式 |
|-----------|----------|
| **OpenClaw** | 技能插件直接调用 |
| **Hermes Agent** | Skill 接口调用 |
| **Claude Code** | Python API 调用 |
| **其他 Agent** | 标准接口适配 |

### 📄 一份内容，双重输出
- **Markdown**：供 AI 机器读取、解析、理解
- **Word 公文格式**：供人类阅读、审批、归档

---

## 🚀 快速开始

### 安装

```bash
pip install python-docx>=1.1.0
```

### Python API 使用

```python
from official_doc import md_to_docx

md_content = """# 工作简报

## 一、上周工作总结

本周完成了系统升级任务。

### （一）主要工作

1. 完成服务器部署
2. 完成数据迁移

### （二）存在问题

部分功能需要优化。
"""

success = md_to_docx(md_content, "工作简报_公文格式.docx")
print("转换成功" if success else "转换失败")
```

### 命令行使用

```bash
# 方式一：直接调用 Python
python -c "
from official_doc import md_to_docx
md_to_docx('# 标题\n\n正文内容', 'output.docx')
"

# 方式二：作为脚本调用
python src/md2docx.py input.md output.docx
```

---

## 📋 公文格式规范（GB/T 9704-2012）

### 页面设置
| 设置项 | 规范值 |
|--------|--------|
| 上边距 | 3.7cm |
| 下边距 | 3.5cm |
| 左边距 | 2.8cm |
| 右边距 | 2.6cm |
| 行间距 | 固定值 26 磅 |
| 首行缩进 | 3 字符 |

### 字体规范
| 元素 | Markdown 标记 | 字体 | 字号 | 加粗 |
|------|--------------|------|------|------|
| 大标题 | `#` | 方正小标宋简体 | 二号 | ❌ |
| 一级标题 | `##` | 黑体 | 三号 | ❌ |
| 二级标题 | `###` | 楷体_GB2312 | 三号 | ✅ |
| 三级标题 | `####` | 仿宋_GB2312 | 三号 | ✅ |
| 正文 | - | 仿宋_GB2312 | 三号 | ❌ |
| 页码 | - | 宋体 | 四号 | ❌ |

### 标题编号规则
| 层级 | 格式示例 |
|------|----------|
| 大标题 | 一、文档标题 |
| 一级标题 | 一、章节名称 |
| 二级标题 | （一）小节名称 |
| 三级标题 | 1. 项目名称 |

---

## 🔧 AI Agent 集成指南

### OpenClaw 集成

```python
from official_doc import md_to_docx

class OfficialDocSkill:
    name = "official-doc"
    description = "公文格式转换 - 将 Markdown 转为党政机关公文格式"

    def execute(self, md_content, output_path):
        success = md_to_docx(md_content, output_path)
        return {
            "success": success,
            "output_path": output_path,
            "message": "公文格式转换完成" if success else "转换失败"
        }
```

### Hermes Agent 集成

```python
# Hermes Agent 技能配置
{
    "name": "official-doc",
    "type": "formatter",
    "entry": "from official_doc import md_to_docx; md_to_docx(md_content, output_path)"
}
```

### 定时任务自动生成简报

```python
import schedule
from official_doc import md_to_docx

def daily_report():
    content = generate_weekly_summary()
    md_to_docx(content, f"工作简报_{date}.docx")

schedule.every().monday.at("09:00").do(daily_report)
```

---

## 📁 项目结构

```
official-doc/
├── src/
│   ├── __init__.py          # 包初始化
│   └── md2docx.py           # 核心转换模块
├── skill.json               # 技能配置文件
├── requirements.txt         # 依赖清单
├── README.md               # 本文档
└── LICENSE                # MIT 许可证
```

---

## 🧪 测试验证

```bash
# 安装依赖
pip install -r requirements.txt

# 运行测试
python -c "
from official_doc import md_to_docx

test_md = '''# 测试文档

## 一、测试标题

这是一个测试段落。

### （一）二级标题

1. 列表项一
2. 列表项二

**加粗文本** 测试。
'''

success = md_to_docx(test_md, 'test_output.docx')
print('测试通过' if success else '测试失败')
"
```

---

## 📜 许可证

MIT License

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

---

**注意**：本工具仅提供格式排版功能，不负责内容审核。请确保使用本工具生成的公文内容符合相关规定和要求。

---

*Built with ❤️ for LLM + AI Agent 生态*
