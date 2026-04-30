# 故障排除

## 常见问题

### 问题1：无法获取文章内容

**症状：**
```
❌ 无法定位文章内容，可能需要登录或链接已失效。
```

**可能原因：**
1. 文章需要登录才能查看
2. 文章链接已失效
3. 网络连接问题
4. 微信服务器限制

**解决方案：**
1. 检查链接是否有效，在浏览器中打开确认
2. 确认网络连接正常
3. 尝试重新运行脚本
4. 如果文章需要登录，需要手动复制内容

### 问题2：图片下载失败

**症状：**
```
❌ 下载图片失败: 状态码 403
```

**可能原因：**
1. 图片有防盗链保护
2. 图片链接已失效
3. 网络超时

**解决方案：**
1. 检查网络连接
2. 增加超时时间
3. 使用代理服务器
4. 手动下载图片

### 问题3：请求超时

**症状：**
```
❌ 请求超时，请检查网络连接。
```

**可能原因：**
1. 网络连接不稳定
2. 微信服务器响应慢
3. 防火墙限制

**解决方案：**
1. 检查网络连接
2. 增加超时时间
3. 使用代理服务器
4. 检查防火墙设置

### 问题4：编码错误

**症状：**
```
UnicodeEncodeError: 'gbk' codec can't encode character...
```

**可能原因：**
1. 系统编码设置问题
2. 文件名包含特殊字符

**解决方案：**
1. 设置系统编码：
```python
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
```

2. 清理文件名：
```python
import re
safe_title = re.sub(r'[<>:"/\\|?*]', '', title)
```

### 问题5：依赖安装失败

**症状：**
```
ERROR: Could not find a version that satisfies the requirement...
```

**可能原因：**
1. pip 版本过旧
2. 网络连接问题
3. Python 版本不兼容

**解决方案：**
1. 升级 pip：
```bash
python -m pip install --upgrade pip
```

2. 使用国内镜像：
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests beautifulsoup4
```

3. 检查 Python 版本：
```bash
python --version  # 需要 3.7+
```

## 调试技巧

### 1. 启用详细日志

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### 2. 检查响应内容

```python
response = requests.get(url, headers=headers)
print(f"状态码: {response.status_code}")
print(f"内容长度: {len(response.text)}")
```

### 3. 保存原始HTML

```python
with open('debug.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
```

### 4. 测试网络连接

```python
import requests
try:
    response = requests.get('https://www.baidu.com', timeout=5)
    print("网络连接正常")
except:
    print("网络连接异常")
```

## 获取帮助

如果以上方法都无法解决问题，请：

1. 查看 [GitHub Issues](https://github.com/yourusername/wechat-article-fetcher-skill/issues)
2. 提交新的 Issue，包含：
   - 错误信息
   - 操作步骤
   - 环境信息（Python版本、操作系统等）
3. 发送邮件到：your.email@example.com

## 性能问题

### 问题：执行速度慢

**解决方案：**
1. 使用更快的HTML解析器：
```bash
pip install lxml
```

2. 减少图片下载：
修改脚本，跳过图片下载

3. 使用多线程：
```python
from concurrent.futures import ThreadPoolExecutor
```

## 安全问题

### 问题：被微信封禁

**解决方案：**
1. 降低请求频率
2. 使用代理池
3. 模拟真实用户行为
4. 添加随机延迟

## 更新日志

查看 [CHANGELOG.md](../CHANGELOG.md) 了解版本更新历史。
