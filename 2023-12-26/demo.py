#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author ：Lee fargolyh@gmail.com
@Project ：2023-12 
@File ：demo.py
@Date ：2023/12/26 21:35 
"""
# from selenium import webdriver


# # 设置chromedriver路径
# # chromedriver_path = "/path/to/chromedriver"
#
# # 创建chrome选项
# chrome_options = Options()
# chrome_options.add_argument('--headless')
#
# # 创建webdriver实例
# driver = webdriver.Chrome(options=chrome_options)
#
# # 进行其他webdriver操作

# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# str1 = driver.capabilities['browserVersion']  # 查看chrome版本
# str2 = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]  # 查看python下的chromedriver版本
# print(str1)
# print(str2)
# # 创建浏览器对象
# driver = webdriver.Chrome()
#
# # 执行自动化操作
# # ...
#
# # 程序即将结束时，询问是否关闭浏览器
# choice = input("Do you want to close the browser? (Y/N) ")
# if choice.lower() == "y":
#     # 关闭浏览器
#     driver.quit()
# else:
#     print("Browser will remain open.")


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# # option 1
# # driver = webdriver.Chrome(ChromeDriverManager().install())
#
# # option 2
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# driver = webdriver.Chrome(chrome_options=options)

from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
url = 'https://www.moulem.com/'

driver.get(url=url)

driver.maximize_window()

print(driver.get_window_size())

print(driver.current_url)

print(driver.window_handles)