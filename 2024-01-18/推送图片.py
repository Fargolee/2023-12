import base64
import hashlib
import json
import os
import requests
import urllib


def get_daily_sentence():
    """
    爬取金山词霸每日一句
    """
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    r = json.loads(r.text)
    content = r["content"]
    note = r["note"]
    # fenxiang_img = r["fenxiang_img"]
    fenxiang_img = r["picture4"]
    daily_sentence = content + "\n" + note 
    response= requests.get(url= fenxiang_img).content
    with open('imge.png', 'wb') as f:
        f.write(response)
    return daily_sentence

def get_image():
    """
    
    """
    api_url = 'https://api.wetab.link/api/wallpaper/next?type=random'
    r = requests.get(api_url)
    r = json.loads(r.text)
    rawSrc = r['data']["rawSrc"]
    
    response= requests.get(url= rawSrc).content
    with open('imge.png', 'wb') as f:
        f.write(response)
    


def download_bing_images():
    # Bing 每日一图的 URL
    url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8&mkt=zh-CN'
    response = requests.get(url)
    data = response.json()
 
    # 创建一个文件夹来保存图片
    if not os.path.exists('bing_images'):
        os.makedirs('bing_images')
 
    # 遍历每日一图的数据并下载图片
    for image_data in data['images']:
        image_name = image_data['hsh']
        image_url = f'https://cn.bing.com{image_data["url"]}'
 
        try:
            # 下载图片
            response= requests.get(url= image_url).content
            with open(f'bing_images/{image_name}.jpg', 'wb') as f:
                    f.write(response)
            
 
            print(f'图片 {image_name}.jpg 已成功下载！')
           
        except Exception as e:
            print(f'下载失败：{str(e)}')
        
            


def get_base64_and_md5(image_path):
    """
    将图片转为特定格式
    """

    with open(image_path, 'rb') as image_file:
        img_data = image_file.read()
        base64_data = base64.b64encode(img_data).decode('utf-8')
        md5_value = hashlib.md5(img_data).hexdigest()
     
    return base64_data, md5_value

def send_image_to_robot(webhook_url, image_path):
    """
    微信发送图片
    """
    base64_data, md5_value = get_base64_and_md5(image_path)
 
    # 构建请求体
    payload = {
        "msgtype": "image",
        "image": {
            "base64": base64_data,
            "md5": md5_value,
        },
    }
 
    # 发送POST请求
    response = requests.post(webhook_url, json=payload)
 
    # 检查响应状态
    if response.status_code == 200:
        print("图片已成功发送至企业微信机器人")
    else:
        print("发送失败，响应状态码：", response.status_code)

if __name__ == '__main__':
    
    # download_bing_images()
    # get_image()
    for root, dirs, files in os.walk('E:\\Git\\2022\\bing_images'):
        for file in files:
            image_path = os.path.join(root, file)
            print(image_path)
            send_image_to_robot(webhook_url, image_path)
    # image_path = 'bing_images\\f59d4427d7a743fd528f8581869e64c6.jpg'
    # # image_path= 'wallhaven-5we787.jpg'
    # # get_daily_sentence()
    
    
    # download_bing_images()
