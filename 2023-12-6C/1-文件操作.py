#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/6 18:39
# @Author  : Lee
# @File    : 1-文件操作.py
with open('file.txt', 'r', 'a', encoding='utf-8') as f:
   
    content = f.read()

    print(content)