# 微信公众号文章获取 Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Trae Skill](https://img.shields.io/badge/Trae-Skill-green.svg)](https://trae.cn)

> 专门用于获取微信公众号文章内容的 Trae Skill，支持文本和图片提取

## ✨ 特性

- 🚀 **轻量级设计** - 只需 `requests` 和 `beautifulsoup4`，总安装大小不到 10MB
- 📝 **完整内容提取** - 提取标题、作者、正文内容
- 🖼️ **图片下载支持** - 自动下载文章中的所有图片
- 📄 **Markdown 输出** - 自动转换为 Markdown 格式
- 🛡️ **反爬机制绕过** - 模拟真实浏览器访问
- ⚡ **快速执行** - 无需安装浏览器驱动

## 📦 安装

### 方法一：直接安装依赖

```bash
pip install requests beautifulsoup4
```

### 方法二：使用 requirements.txt

```bash
pip install -r requirements.txt
```

## 🚀 使用方法

### 作为 Trae Skill 使用

当您在 Trae 中提供微信公众号文章链接时，这个 Skill 会自动被触发：

```
用户: 帮我总结这篇文章 https://mp.weixin.qq.com/s/xxxxx
AI: [自动调用 Skill 获取文章内容并总结]
```

### 作为独立脚本使用

```bash
python fetch_article_with_images.py "https://mp.weixin.qq.com/s/xxxxx"
```

**输出：**
- Markdown 文件：`wechat_articles/文章标题.md`
- 图片文件：`wechat_articles/images/`

## 📖 使用示例

### 示例1：获取文章内容

```python
from fetch_article_with_images import fetch_wechat_article_with_images

url = "https://mp.weixin.qq.com/s/Bwmr8vmAgsBz4g5S8SWX7g"
success = fetch_wechat_article_with_images(url)

if success:
    print("文章获取成功！")
```

### 示例2：批量获取多篇文章

```python
urls = [
    "https://mp.weixin.qq.com/s/article1",
    "https://mp.weixin.qq.com/s/article2",
    "https://mp.weixin.qq.com/s/article3"
]

for url in urls:
    fetch_wechat_article_with_images(url)
    time.sleep(2)  # 避免请求过快
```

## 📁 项目结构

```
wechat-article-fetcher-skill/
├── README.md                   # 项目说明文档
├── LICENSE                     # MIT 许可证
├── requirements.txt            # Python 依赖
├── SKILL.md                    # Trae Skill 定义
├── fetch_article_with_images.py # 主要脚本
├── examples/                   # 使用示例
│   ├── basic_usage.py         # 基础使用示例
│   └── batch_fetch.py         # 批量获取示例
└── docs/                       # 文档
    ├── installation.md        # 安装指南
    ├── usage.md               # 使用指南
    └── troubleshooting.md     # 故障排除
```

## 🔧 配置选项

### 自定义输出目录

```python
fetch_wechat_article_with_images(
    url="https://mp.weixin.qq.com/s/xxxxx",
    output_dir="my_articles"
)
```

### 自定义请求头

```python
headers = {
    'User-Agent': 'Your Custom User Agent',
    'Referer': 'https://mp.weixin.qq.com/'
}
```

## ⚠️ 注意事项

1. **反爬机制**：微信公众号可能有反爬机制，如遇到验证码或登录要求，需要人工介入

2. **请求频率**：建议添加适当的延迟，避免请求过快被限制

3. **图片下载**：部分图片可能有防盗链保护，下载可能失败

4. **内容准确性**：提取的内容基于 HTML 结构，微信更新可能导致提取失败

## 🐛 故障排除

### 问题1：无法获取文章内容

**可能原因：**
- 文章需要登录
- 链接已失效
- 网络连接问题

**解决方案：**
- 检查链接是否有效
- 确认网络连接正常
- 尝试重新运行

### 问题2：图片下载失败

**可能原因：**
- 图片链接失效
- 防盗链保护
- 网络超时

**解决方案：**
- 检查网络连接
- 增加超时时间
- 使用代理

## 🤝 贡献指南

欢迎贡献代码、报告问题或提出建议！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- [requests](https://docs.python-requests.org/) - HTTP 库
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/) - HTML 解析库
- [Trae](https://trae.cn) - AI 开发平台

## 📞 联系方式

- 项目主页：[GitHub Repository]
- 问题反馈：[GitHub Issues]
- 邮箱：your.email@example.com

## 📊 项目统计

![GitHub stars](https://img.shields.io/github/stars/yourusername/wechat-article-fetcher-skill.svg?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/wechat-article-fetcher-skill.svg?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/yourusername/wechat-article-fetcher-skill.svg?style=social)

---

**如果这个项目对您有帮助，请给一个 ⭐️ Star！**
