#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author ：Lee fargolyh@gmail.com
@Project ：2023-12 
@File ：Test.py
@Date ：2023/11/28 20:21 
"""
from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/zh-cn/documentation/webdriver/interactions/alerts/")
driver.find_element('link text','查看样例警告框').click()
sleep(5)
alert = driver.switch_to.alert
alert.accept()
sleep(5)
driver.find_element('link text','查看样例警告框').click()