#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/4 17:59
# @Author  : Lee
# @File    : 1001.py
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
driver.get("https://www.baidu.com")
time.sleep(3)