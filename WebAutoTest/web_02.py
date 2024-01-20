#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author ：Lee fargolyh@gmail.com
@Project ：2023-12 
@File ：web_02.py
@Date ：2023/12/30 21:39 
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
element = driver.find_element(By.ID, "kw")
element.send_keys("selenium")

sleep(2)
driver.quit()