# Official Doc - 公文格式转换 v1.0.0

## 📋 更新说明

### 新增功能
- ✅ Markdown 转 Word 公文格式
- ✅ 严格遵循 GB/T 9704-2012 标准
- ✅ 支持 4 级标题自动编号
- ✅ 中文引号自动转换
- ✅ AI Agent 标准接口

### 格式规范
- 页边距：上 3.7cm / 下 3.5cm / 左 2.8cm / 右 2.6cm
- 行间距：固定值 26 磅
- 首行缩进：3 字符
- 字体：方正小标宋简体、黑体、楷体_GB2312、仿宋_GB2312

## 🚀 安装方式

### 方式一：直接下载使用
```bash
# 下载压缩包并解压
unzip official-doc-v1.0.0.zip
cd official-doc
pip install -r requirements.txt
```

### 方式二：使用 pip 安装
```bash
pip install git+https://github.com/yourusername/official-doc.git
```

## 📖 使用方法

```python
from official_doc import md_to_docx

md_content = "# 标题\n\n正文内容"
md_to_docx(md_content, "output.docx")
```

## 🤝 支持的 AI Agent

- OpenClaw
- Hermes Agent  
- Claude Code
- 其他标准 Python 环境

## 📜 许可证

MIT License