#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author ：Lee fargolyh@gmail.com
@Project ：2023-12 
@File ：web_01.py
@Date ：2023/12/29 23:08 
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.bilibili.com/")

driver.find_element(By.CLASS_NAME,'nav-search-input').send_keys('软件测试老白')
driver.find_element(By.CLASS_NAME,'nav-search-btn').click()

sleep(3)
driver.close()