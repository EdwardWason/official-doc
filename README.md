# 📄 Official Doc - Document Format Converter

🇨🇳 [中文文档](README_CN.md) | 🇺🇸 English

Convert Markdown documents to Chinese government official document format (GB/T 9704-2012) Word documents.

---

## ⚠️ Important Notes

This tool only provides formatting functionality and does not review content. Please ensure that the official documents generated using this tool comply with relevant regulations and requirements.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🚀 **One-click Conversion** | Convert Markdown to Word official document format easily |
| 📋 **Standard Compliance** | Strictly follows GB/T 9704-2012 standard |
| 🤖 **Multi-Agent Support** | Works with OpenClaw, Hermes Agent, Claude Code, etc. |
| 🔄 **Dual Output** | Generate both Markdown (for machines) and Word (for humans) |
| 📊 **Automation Ready** | Supports scheduled tasks for automatic report generation |
| 📦 **Easy Integration** | Provides standard Python API for system integration |

---

## 🚀 Quick Start

### System Requirements

| Component | Requirement |
|-----------|-------------|
| OS | Windows 10/11, Linux, macOS |
| Python | 3.8+ |
| Dependency | python-docx >= 1.1.0 |

### Installation

**Method 1: Using pip**
```bash
pip install python-docx>=1.1.0
```

**Method 2: Clone repository**
```bash
git clone https://github.com/EdwardWason/official-doc.git
cd official-doc
pip install -r requirements.txt
```

### Usage Example

```python
from official_doc import md_to_docx

# Markdown content
md_content = """# Weekly Report

## 1. Work Summary

Completed system upgrade tasks including:

### 1.1 Main Tasks
1. Server deployment
2. Data migration
3. Testing and verification

### 1.2 Issues
Some features need further optimization.

### 1.3 Next Week Plan
Continue optimization work.
"""

# Convert to official document format
success = md_to_docx(md_content, "weekly_report.docx")
print("Conversion successful" if success else "Conversion failed")
```

---

## 📋 Format Specifications (GB/T 9704-2012)

### Page Settings

| Setting | Value |
|---------|-------|
| Paper Size | A4 (210mm × 297mm) |
| Top Margin | 3.7cm |
| Bottom Margin | 3.5cm |
| Left Margin | 2.8cm |
| Right Margin | 2.6cm |
| Line Spacing | 26pt (fixed) |
| First Line Indent | 3 characters |

### Font Settings

| Element | Markdown | Font | Size | Bold |
|---------|----------|------|------|------|
| Title | `#` | Fangzheng Xiaobiao Song | 2nd | ❌ |
| Heading 1 | `##` | Hei Ti | 3rd | ❌ |
| Heading 2 | `###` | Kai Ti_GB2312 | 3rd | ✅ |
| Heading 3 | `####` | Fang Song_GB2312 | 3rd | ✅ |
| Body | Normal | Fang Song_GB2312 | 3rd | ❌ |
| Page Number | - | Song Ti | 4th | ❌ |

### Heading Numbering Rules

| Level | Format Example |
|-------|---------------|
| Title | I. Document Title |
| Heading 1 | I. Section Name |
| Heading 2 | (I) Subsection Name |
| Heading 3 | 1. Item Name |

---

## 🔧 AI Agent Integration

### OpenClaw Integration

```python
from official_doc import md_to_docx
from openclaw import Skill

class OfficialDocSkill(Skill):
    name = "official-doc"
    description = "Convert Markdown to Chinese government official document format"
    
    def execute(self, md_content, output_path=None):
        if output_path is None:
            output_path = "output.docx"
        
        success = md_to_docx(md_content, output_path)
        
        return {
            "success": success,
            "output_path": output_path,
            "message": "Conversion completed" if success else "Conversion failed"
        }
```

### Hermes Agent Integration

```python
from hermes import Agent

agent = Agent()
result = agent.run_skill(
    skill="official-doc",
    md_content=report_content,
    output_path="weekly_report.docx"
)
```

---

## 📁 Project Structure

```
official-doc/
├── src/                      # Source code
│   ├── __init__.py          # Package initialization
│   └── md2docx.py           # Core conversion module
├── skill.json               # AI Agent skill configuration
├── setup.py                 # Installation configuration
├── requirements.txt         # Dependencies
├── README.md                # English documentation
├── README_CN.md             # Chinese documentation
├── CHANGELOG.md             # Changelog
├── LICENSE                  # MIT License
└── .gitignore               # Git ignore rules
```

---

## 🧪 Testing

```bash
cat > test_official_doc.py << 'EOF'
from official_doc import md_to_docx

def test_conversion():
    md_content = """# Test Document

## 1. Test Title

This is a test paragraph.

### 1.1 Subtitle

**Bold text** test.
"""
    success = md_to_docx(md_content, 'test_output.docx')
    assert success == True
    print("✓ Test passed")

if __name__ == "__main__":
    test_conversion()
    print("✅ All tests passed!")
EOF

python test_official_doc.py
```

---

## 📜 License

MIT License

---

## 🤝 Contributing

Welcome to submit Issues and Pull Requests!

1. Fork this repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'feat: Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📞 Contact

- **GitHub**: [https://github.com/EdwardWason/official-doc](https://github.com/EdwardWason/official-doc)
- **Issues**: [https://github.com/EdwardWason/official-doc/issues](https://github.com/EdwardWason/official-doc/issues)

---

*Built with ❤️ for LLM + AI Agent Ecosystem*
