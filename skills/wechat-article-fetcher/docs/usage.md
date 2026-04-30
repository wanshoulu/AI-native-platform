# 使用指南

## 快速开始

### 基础使用

```bash
python fetch_article_with_images.py "https://mp.weixin.qq.com/s/xxxxx"
```

### 作为 Python 模块使用

```python
from fetch_article_with_images import fetch_wechat_article_with_images

url = "https://mp.weixin.qq.com/s/xxxxx"
success = fetch_wechat_article_with_images(url)

if success:
    print("文章获取成功！")
```

## 高级用法

### 自定义输出目录

```python
fetch_wechat_article_with_images(
    url="https://mp.weixin.qq.com/s/xxxxx",
    output_dir="my_custom_dir"
)
```

### 批量获取

```python
import time

urls = [
    "https://mp.weixin.qq.com/s/article1",
    "https://mp.weixin.qq.com/s/article2",
    "https://mp.weixin.qq.com/s/article3"
]

for url in urls:
    fetch_wechat_article_with_images(url)
    time.sleep(2)  # 避免请求过快
```

### 自定义请求头

```python
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Referer': 'https://mp.weixin.qq.com/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

response = requests.get(url, headers=headers)
```

## 输出格式

### 文件结构

```
wechat_articles/
├── 文章标题.md          # Markdown 格式的文章内容
└── images/              # 文章中的图片
    ├── 文章标题_1.png
    ├── 文章标题_2.png
    └── ...
```

### Markdown 格式

```markdown
# 文章标题

> **作者**: 作者名
> **来源**: [原文链接](https://mp.weixin.qq.com/s/xxxxx)

## 正文

文章正文内容...

## 图片列表

1. ![](文章标题_1.png)
2. ![](文章标题_2.png)
```

## 使用技巧

### 1. 避免请求过快

```python
import time

for url in urls:
    fetch_wechat_article_with_images(url)
    time.sleep(2)  # 建议间隔2秒
```

### 2. 错误处理

```python
try:
    success = fetch_wechat_article_with_images(url)
    if not success:
        print("获取失败，请检查链接")
except Exception as e:
    print(f"发生错误: {e}")
```

### 3. 日志记录

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"开始获取文章: {url}")
success = fetch_wechat_article_with_images(url)
logger.info(f"获取结果: {'成功' if success else '失败'}")
```

## 性能优化

### 1. 使用代理

```python
proxies = {
    'http': 'http://proxy.example.com:8080',
    'https': 'https://proxy.example.com:8080'
}

response = requests.get(url, headers=headers, proxies=proxies)
```

### 2. 超时设置

```python
response = requests.get(url, headers=headers, timeout=30)
```

### 3. 重试机制

```python
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(total=3, backoff_factor=1)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
```

## 下一步

- 查看 [故障排除](troubleshooting.md) 了解常见问题解决方案
- 查看 [示例代码](../examples/) 了解更多使用场景
