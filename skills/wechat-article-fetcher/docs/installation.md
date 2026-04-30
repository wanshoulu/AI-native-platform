# 安装指南

## 系统要求

- Python 3.7 或更高版本
- pip 包管理器

## 安装步骤

### 方法一：使用 pip 安装依赖

```bash
pip install requests beautifulsoup4
```

### 方法二：使用 requirements.txt

```bash
pip install -r requirements.txt
```

### 方法三：从源码安装

```bash
git clone https://github.com/yourusername/wechat-article-fetcher-skill.git
cd wechat-article-fetcher-skill
pip install -r requirements.txt
```

## 验证安装

运行以下命令验证安装是否成功：

```bash
python -c "import requests; import bs4; print('安装成功！')"
```

## 可选依赖

如果您需要处理特定格式的图片，可以安装以下可选依赖：

```bash
pip install Pillow  # 图片处理
pip install lxml    # 更快的HTML解析
```

## 故障排除

### 问题1：pip 安装失败

**解决方案：**
```bash
python -m pip install --upgrade pip
pip install requests beautifulsoup4
```

### 问题2：权限错误

**解决方案：**
```bash
pip install --user requests beautifulsoup4
```

### 问题3：网络问题

**解决方案：**
使用国内镜像源：
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests beautifulsoup4
```

## 下一步

安装完成后，请查看 [使用指南](usage.md) 了解如何使用这个工具。
