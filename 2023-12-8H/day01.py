#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author ：Lee fargolyh@gmail.com
@Project ：2023-12 
@File ：day01.py
@Date ：2023/12/8 23:09 
"""
import requests

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

url = 'https://tuchong.com/rest/tags/%E7%BE%8E%E5%A5%B3/posts?page=1&count=20&order=new&before_timestamp='

response = requests.get(url=url, headers=headers)
print(response.json())
