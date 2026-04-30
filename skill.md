# 📄 official-doc - 公文格式转换

## 技能信息

### 基本信息
| 属性 | 说明 |
|------|------|
| **名称** | official-doc |
| **中文名称** | 公文格式转换 |
| **版本** | 1.0.0 |
| **作者** | EdwardWason |
| **许可证** | MIT |
| **主页** | https://github.com/EdwardWason/official-doc |

### 功能描述
将 Markdown 文档转换为符合 **GB/T 9704-2012** 党政机关公文格式的 Word 文档。

### 适用场景
- AI Agent 生成公文格式报告
- 定时任务自动生成工作简报、周报、月报
- Markdown 文档批量转换为标准公文格式
- 行业研报格式标准化输出

---

## 输入参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `md_content` | string | ✅ | Markdown 格式的文本内容 |
| `output_path` | string | ✅ | 输出 Word 文件路径（.docx） |

---

## 输出结果

| 字段 | 类型 | 说明 |
|------|------|------|
| `success` | boolean | 转换是否成功 |
| `output_path` | string | 输出文件路径 |
| `message` | string | 执行结果消息 |

---

## 使用示例

### 基本使用
```python
from official_doc import md_to_docx

md_content = """# 工作简报

## 一、上周工作总结

本周完成了系统升级任务。

### （一）主要工作
1. 服务器部署
2. 数据迁移
3. 测试验证

### （二）下周计划
继续推进优化工作。
"""

success = md_to_docx(md_content, "工作简报_公文格式.docx")
print("转换成功" if success else "转换失败")
```

### AI Agent 集成
```python
# OpenClaw 集成示例
from official_doc import md_to_docx
from openclaw import Skill

class OfficialDocSkill(Skill):
    name = "official-doc"
    description = "公文格式转换 - 将 Markdown 转为党政机关公文格式"
    
    def execute(self, md_content, output_path=None):
        if output_path is None:
            output_path = "output_公文格式.docx"
        
        success = md_to_docx(md_content, output_path)
        
        return {
            "success": success,
            "output_path": output_path,
            "message": "公文格式转换完成" if success else "转换失败"
        }
```

### 定时任务
```python
import schedule
import time
from official_doc import md_to_docx

def generate_report():
    content = generate_report_content()
    today = time.strftime("%Y-%m-%d")
    md_to_docx(content, f"工作简报_{today}_公文格式.docx")

schedule.every().monday.at("09:00").do(generate_report)
```

---

## 格式规范

### 页面设置
| 设置项 | 规范值 |
|--------|--------|
| 上边距 | 3.7cm |
| 下边距 | 3.5cm |
| 左边距 | 2.8cm |
| 右边距 | 2.6cm |
| 行间距 | 固定值 26 磅 |
| 首行缩进 | 3 字符 |

### 字体设置
| 元素 | 字体 | 字号 | 加粗 |
|------|------|------|------|
| 大标题 | 方正小标宋简体 | 二号 | ❌ |
| 一级标题 | 黑体 | 三号 | ❌ |
| 二级标题 | 楷体_GB2312 | 三号 | ✅ |
| 三级标题 | 仿宋_GB2312 | 三号 | ✅ |
| 正文 | 仿宋_GB2312 | 三号 | ❌ |
| 页码 | 宋体 | 四号 | ❌ |

---

## 依赖要求

| 依赖 | 版本 |
|------|------|
| Python | >= 3.8 |
| python-docx | >= 1.1.0 |

---

## 支持平台

- ✅ Windows 10/11
- ✅ Linux
- ✅ macOS

---

## 项目链接

- GitHub: https://github.com/EdwardWason/official-doc
- Release: https://github.com/EdwardWason/official-doc/releases
- README: https://github.com/EdwardWason/official-doc/blob/main/README.md
