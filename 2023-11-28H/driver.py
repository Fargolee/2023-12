#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/30 16:58
# @Author  : Lee
# @File    : driver.py

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.quit()