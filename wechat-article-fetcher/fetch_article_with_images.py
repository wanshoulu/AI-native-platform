import sys
import os
import requests
from bs4 import BeautifulSoup
import time
import re

def fetch_wechat_article_with_images(url, output_dir="wechat_articles"):
    """
    微信公众号文章获取工具（支持图片）
    使用 requests + beautifulsoup4，无需安装浏览器
    
    Args:
        url: 微信公众号文章链接
        output_dir: 输出目录
    
    Returns:
        bool: 是否成功
    """
    print(f"🚀 正在获取文章内容: {url}")
    
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://mp.weixin.qq.com/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    
    try:
        # 发送HTTP请求
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            # 解析HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 1. 提取标题
            title_tag = soup.find('meta', property='og:title')
            title = title_tag['content'] if title_tag else "未知标题"
            
            # 清理标题中的非法字符
            safe_title = re.sub(r'[<>:"/\\|?*]', '', title)
            
            # 2. 提取作者
            author_tag = soup.find('meta', property='og:article:author')
            if not author_tag:
                author_tag = soup.find('meta', property='og:author')
            author = author_tag['content'] if author_tag else "未知作者"
            
            # 3. 提取正文
            content_div = soup.find(id='js_content')
            
            if content_div:
                # 去除脚本标签
                for script in content_div(["script", "style"]):
                    script.decompose()
                
                # 提取图片
                images = []
                img_tags = content_div.find_all('img')
                print(f"📷 找到 {len(img_tags)} 张图片")
                
                # 创建图片目录
                image_dir = os.path.join(output_dir, "images")
                if not os.path.exists(image_dir):
                    os.makedirs(image_dir)
                
                # 下载图片
                for i, img in enumerate(img_tags, 1):
                    img_url = img.get('data-src') or img.get('src')
                    if img_url:
                        try:
                            # 下载图片
                            img_response = requests.get(img_url, headers=headers, timeout=10)
                            if img_response.status_code == 200:
                                # 确定文件扩展名
                                ext = 'jpg'
                                if 'png' in img_url.lower():
                                    ext = 'png'
                                elif 'gif' in img_url.lower():
                                    ext = 'gif'
                                
                                # 保存图片
                                filename = f"{safe_title}_{i}.{ext}"
                                filepath = os.path.join(image_dir, filename)
                                
                                with open(filepath, 'wb') as f:
                                    f.write(img_response.content)
                                
                                images.append(filepath)
                                print(f"✅ 下载图片 {i}/{len(img_tags)}: {filename}")
                                time.sleep(0.5)  # 避免请求过快
                            else:
                                print(f"❌ 下载图片失败 {i}: 状态码 {img_response.status_code}")
                        except Exception as e:
                            print(f"❌ 下载图片出错 {i}: {str(e)}")
                
                # 提取文本内容
                paragraphs = content_div.find_all(['p', 'br'])
                text_content = []
                for p in paragraphs:
                    text = p.get_text(strip=True)
                    if text:
                        text_content.append(text)
                
                full_text = "\n\n".join(text_content)
                
                # 生成Markdown内容
                markdown_content = f"# {title}\n\n"
                markdown_content += f"> **作者**: {author}\n"
                markdown_content += f"> **来源**: [原文链接]({url})\n\n"
                markdown_content += f"## 正文\n\n{full_text}\n\n"
                
                if images:
                    markdown_content += f"## 图片列表\n\n"
                    for i, img_path in enumerate(images, 1):
                        markdown_content += f"{i}. ![]({os.path.basename(img_path)})\n"
                
                # 保存Markdown文件
                output_file = os.path.join(output_dir, f"{safe_title}.md")
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(markdown_content)
                
                print(f"\n✅ 成功获取文章：{title}")
                print(f"📄 内容已保存至: {output_file}")
                print(f"📷 图片已保存至: {image_dir}")
                print(f"📊 统计: {len(text_content)} 个段落, {len(images)} 张图片")
                
                return True
            else:
                print("❌ 无法定位文章内容，可能需要登录或链接已失效。")
                return False
        else:
            print(f"❌ 访问失败，状态码: {response.status_code}")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ 请求超时，请检查网络连接。")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ 网络请求错误: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ 发生错误: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        fetch_wechat_article_with_images(url)
    else:
        print("使用方法: python fetch_article_with_images.py <微信公众号文章链接>")
        print("示例: python fetch_article_with_images.py https://mp.weixin.qq.com/s/xxxxx")
