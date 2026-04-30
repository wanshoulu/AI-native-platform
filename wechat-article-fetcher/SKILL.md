---
name: "wechat-article-fetcher"
description: "专门用于获取微信公众号文章内容的工具。当用户输入包含 'mp.weixin.qq.com' 的链接时，必须优先调用此 Skill。它能绕过反爬机制，提取纯净的标题、正文和作者信息，并转换为 Markdown 格式。"
allowed-tools: ["Bash(python:*)"]
---

# 微信公众号文章获取指南

## 触发条件
- 用户输入中包含 `mp.weixin.qq.com` 链接。
- 用户明确要求"总结这篇文章"、"读取链接内容"且链接来自微信。

## 执行流程
1. **参数提取**：从用户对话中提取完整的 URL。
2. **环境检查**：检查本地是否安装了 `requests` 和 `beautifulsoup4`。
3. **调用脚本**：执行命令 `python fetch_article_with_images.py <URL>`。
4. **结果处理**：
   - 脚本会生成一个 `wechat_articles/文章标题.md` 文件。
   - 图片会保存在 `wechat_articles/images/` 目录。
   - AI 读取该文件内容。
5. **最终反馈**：基于读取的内容，回答用户的问题（如总结摘要、提取观点等）。

## 异常处理
- 如果脚本返回"链接失效"或"需要登录"，请告知用户该文章可能设有访问权限或链接已过期。
- 如果脚本执行超时，请尝试再次运行一次。

## 功能特性
- ✅ 提取文章标题、作者、正文
- ✅ 自动下载文章中的图片
- ✅ 转换为 Markdown 格式
- ✅ 轻量级设计，无需安装浏览器
- ✅ 成功绕过微信公众号反爬机制

## 使用示例

```bash
# 安装依赖
pip install requests beautifulsoup4

# 运行脚本
python fetch_article_with_images.py "https://mp.weixin.qq.com/s/xxxxx"
```

## 输出格式

```
wechat_articles/
├── 文章标题.md          # Markdown 格式的文章内容
└── images/              # 文章中的图片
    ├── 文章标题_1.png
    ├── 文章标题_2.png
    └── ...
```

## 注意事项

1. **环境依赖**：
   - 只需要 `requests` 和 `beautifulsoup4`
   - 无需安装浏览器

2. **反爬机制**：
   - 已设置合理的请求头
   - 如遇到验证码或登录要求，需要人工介入

3. **性能优化**：
   - 建议添加适当的延迟，避免请求过快
   - 可以考虑使用代理池

4. **错误处理**：
   - 脚本已包含基本的错误处理
   - 建议在实际使用中添加更详细的日志记录
