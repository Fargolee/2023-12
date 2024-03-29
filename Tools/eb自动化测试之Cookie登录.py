#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/12 18:40
# @Author  : Lee
# @File    : eb自动化测试之Cookie登录.py
# https://www.cnblogs.com/csfsz/p/17934748.html

from selenium import webdriver
import time
import yaml
import pytest

class TestCookieLogin:
    def setup_class(self):
        self.driver = webdriver.Chrome()

    def test_get_cookies(self):
        # 1. 访问企业微信主页/登录页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # 2. 等待20s，人工扫码操作
        time.sleep(20)
        # 3. 等成功登陆之后，再去获取cookie信息
        cookie = self.driver.get_cookies()
        # 4. 将cookie存入一个可持久存储的地方，文件
        # 打开文件的时候添加写入权限
        with open("cookie.yaml", "w") as f:
            # 第一个参数是要写入的数据
            yaml.safe_dump(cookie, f)

    def test_add_cookie(self):
        # 1. 访问企业微信主页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # 2. 定义cookie，cookie信息从已经写入的cookie文件中获取
        cookie = yaml.safe_load(open("cookie.yaml"))
        # 3. 植入cookie
        for c in cookie:
            self.driver.add_cookie(c)
        time.sleep(3)
        # 4.再次访问企业微信页面，发现无需扫码自动登录，而且可以多次使用
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

    if __name__ == "__main__":
        setup_class()
