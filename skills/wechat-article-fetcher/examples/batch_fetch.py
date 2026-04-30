"""
批量获取示例
演示如何批量获取多篇文章
"""

import sys
import os
import time

# 添加父目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fetch_article_with_images import fetch_wechat_article_with_images

def main():
    # 示例文章链接列表
    urls = [
        "https://mp.weixin.qq.com/s/Bwmr8vmAgsBz4g5S8SWX7g",  # 第一篇
        "https://mp.weixin.qq.com/s/0syVbkI0ikrTE9ynkqwpbw",  # 第二篇
        # 添加更多链接...
    ]
    
    print("=" * 60)
    print("微信公众号文章获取工具 - 批量获取示例")
    print("=" * 60)
    print(f"准备获取 {len(urls)} 篇文章\n")
    
    success_count = 0
    fail_count = 0
    
    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{len(urls)}] 正在处理: {url}")
        print("-" * 60)
        
        success = fetch_wechat_article_with_images(url)
        
        if success:
            success_count += 1
        else:
            fail_count += 1
        
        # 避免请求过快
        if i < len(urls):
            print("\n等待 2 秒...")
            time.sleep(2)
    
    print("\n" + "=" * 60)
    print("批量获取完成！")
    print(f"✅ 成功: {success_count} 篇")
    print(f"❌ 失败: {fail_count} 篇")
    print("=" * 60)

if __name__ == "__main__":
    main()
