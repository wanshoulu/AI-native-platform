#  Skills 集合

这个目录包含了 AI 平台开发的各种 Skills。

## 📋 目录

### wechat-article-fetcher
**微信公众号文章获取工具**

- **描述**: 专门用于获取微信公众号文章内容的工具
- **功能**: 提取标题、作者、正文，下载图片，转换为Markdown格式
- **触发条件**: 用户输入包含 `mp.weixin.qq.com` 的链接
- **详细文档**: [wechat-article-fetcher/README.md](./wechat-article-fetcher/README.md)

## 🚀 使用方法

### 作为 Trae Skill 使用

当您在 Trae 中提供相关链接或请求时，对应的 Skill 会自动被触发。

### 作为独立工具使用

每个 Skill 都可以独立运行，请查看各自的文档了解详细使用方法。

## 📖 Skill 开发指南

### Skill 结构

每个 Skill 应该包含以下文件：

```
skill-name/
├── SKILL.md           # Skill 定义文件（必需）
├── README.md          # 使用文档
├── requirements.txt   # Python 依赖
├── LICENSE           # 许可证
└── examples/         # 使用示例
```

### SKILL.md 格式

```markdown
---
name: "skill-name"
description: "Skill 描述"
allowed-tools: ["Bash(python:*)"]
---

# Skill 使用指南

## 触发条件
- 触发条件1
- 触发条件2

## 执行流程
1. 步骤1
2. 步骤2
```

## 🤝 贡献

欢迎贡献新的 Skill！

1. Fork 本仓库
2. 在 `skills/` 目录下创建新的 Skill
3. 遵循 Skill 结构规范
4. 提交 Pull Request

## 📄 许可证

每个 Skill 都有独立的许可证，请查看各自的 LICENSE 文件。

## 📞 联系方式

- 项目主页: [AI-native-platform](https://github.com/wanshoulu/AI-native-platform)
- 问题反馈: [GitHub Issues](https://github.com/wanshoulu/AI-native-platform/issues)

---

**更多 Skills 正在开发中...**
