# https://blog.csdn.net/weixin_51802807/article/details/130554366

import os
import re
import sys
import winreg
import requests
from zipfile import ZipFile
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, SessionNotCreatedException


def download_webdriver(driver_version):
    """
    下载更新驱动\n
    驱动下载网址：https://registry.npmmirror.com/binary.html?path=chromedriver/
    """
    # 获取驱动列表
    version_list = requests.get("https://registry.npmmirror.com/-/binary/chromedriver/").json()
    version_list = [version["name"] for version in version_list]
    # 获取符合的驱动版本号
    target_version = driver_version.rsplit(".", 1)[0]  # 112.0.5615.28 >>> 112.0.5615
    for version in version_list:
        result = re.match(f"{target_version}.\d+", version)
        if result != None:
            target_version = result.group(0)
    print(f"目标驱动程序版本: {target_version}")
    # 下载驱动压缩包
    download_url = f"https://cdn.npmmirror.com/binaries/chromedriver/{target_version}/chromedriver_win32.zip"
    res = requests.get(download_url, stream=True)
    file_size = int(res.headers.get('Content-Length'))  # 获取文件总大小(字节)
    file_size_MB = file_size / 1024 / 1024
    with open('./chromedriver_win32.zip', 'wb') as fwb:
        n = 1
        for chunk in res.iter_content(int(file_size / 10) + 1):  # 每次遍历的块大小
            fwb.write(chunk)
            schedule = "████" * n + "    " * (10 - n)
            print(f"进度: {10 * n}% |{schedule}| {(file_size_MB / 10) * n:.2f}MB/{file_size_MB:.2f}MB", end='\r')
            n += 1
    # 解压驱动压缩包
    with ZipFile("./chromedriver_win32.zip") as file:
        file.extract("chromedriver.exe", ".")
    os.remove("./chromedriver_win32.zip")
    print("\n下载/更新完成！")


def create_webdriver(options=None):
    """
    判断浏览器驱动是否正常\n
    return：浏览器驱动对象
    """
    while True:
        try:  # 判断驱动是否正常
            driver = webdriver.Chrome(options=options)
            return driver
        except SessionNotCreatedException as msg:  # 驱动与浏览器版本不一致
            driver_version = re.search("Chrome version (\d+)", str(msg)).group(1)
            chrome_version = re.search("Current browser version is ([\d.]+) with", str(msg)).group(1)
            print(
                f"SessionNotCreatedException: 浏览器版本与驱动程序不兼容，浏览器({chrome_version})，当前驱动程序({driver_version})\n正在更新驱动程序...")
            download_webdriver(chrome_version)
        except WebDriverException as msg:  # 缺少驱动文件
            # 获取本机Chrome浏览器的版本
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                 'SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome')
            chrome_version = winreg.QueryValueEx(key, 'DisplayVersion')[0]  # Version
            print(f"WebDriverException: 缺少浏览器对应的驱动程序，浏览器({chrome_version})\n正在下载驱动程序...")
            download_webdriver(chrome_version)
        except Exception as msg:
            print(msg)
            sys.exit(1)


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = create_webdriver(options)
    print(111)
    driver.quit()