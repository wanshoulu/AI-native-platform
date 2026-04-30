"""
基础使用示例
演示如何使用微信公众号文章获取工具
"""

import sys
import os

# 添加父目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fetch_article_with_images import fetch_wechat_article_with_images

def main():
    # 示例文章链接
    url = "https://mp.weixin.qq.com/s/Bwmr8vmAgsBz4g5S8SWX7g"
    
    print("=" * 60)
    print("微信公众号文章获取工具 - 基础使用示例")
    print("=" * 60)
    
    # 获取文章
    success = fetch_wechat_article_with_images(url)
    
    if success:
        print("\n✅ 文章获取成功！")
        print("请查看 wechat_articles/ 目录")
    else:
        print("\n❌ 文章获取失败")

if __name__ == "__main__":
    main()
