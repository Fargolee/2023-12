#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
 
import requests
 
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69"}
 
def all_li():
    url = 'http://101.132.172.60/api/anim/all'
    res = requests.post(url, headers=headers)
    return [(i['name'], i['id']) for i in res.json()['data']]
 
def in_li(title_id):
    url = f'http://101.132.172.60/api/anim/{title_id}/page'
    n = 1
    result = []
    while True:
        data = {
            'page': n,
            'size': 50
        }
        res = requests.post(url, json=data, headers=headers)
        li = [(i['number'], i['id']) for i in res.json()['data']]
        if not li: break
        result.extend(li)
        n += 1
    return result
 
def image_save(name, _id):
    url = f'http://101.132.172.60/api/imgs/{_id}/regular.jpg'
    res = requests.get(url, headers=headers, timeout=10)
    with open(name, 'wb') as f:
        f.write(res.content)
 
if __name__ == '__main__':
    titles = all_li()
    for title in titles:
        print(f"正在下载动漫集：{title[0]}")
        episodes = in_li(title[1])
        for episode in episodes:
            print(f"正在下载第{episode[0]}话")
            image_save(f"{title[0]}_{episode[0]}.jpg", episode[1])