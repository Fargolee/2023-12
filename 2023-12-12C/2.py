#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/26 09:05
# @Author  : Lee
# @File    : 2.py
import urllib.request

# 定义一个url
url = "http://www.baidu.com"
# 模拟浏览器发送数据
response = urllib.request.urlopen(url)
# 获取响应中页面的源码
# read方法，获取的是字节形成的二进制数据, 需要将二进制变成字符串, 使用decode来按照指定的解码格式进行解码
content = response.read().decode('utf-8')
print(content)
