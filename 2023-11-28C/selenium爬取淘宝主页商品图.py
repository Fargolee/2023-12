import re
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

url = 'https://www.taobao.com/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/35.0.1916.114 Safari/537.36'}
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:12306")
service_ = Service()
driver = webdriver.Chrome(service=service_)
driver.get(url)
driver.maximize_window()


def get_content(i):
    img = driver.find_element(by='xpath',
                              value='/html/body/div[6]/div/div/div/div/div[%d]/a/div[1]/img' % i).get_attribute(
        'src')
    img_response = requests.get(img, headers=header)
    img_name = "%d.jpg" % i
    # 判断taobao_img文件夹是否存在
    if not os.path.exists('taobao_img'):
        os.mkdir('taobao_img')
    with open('taobao_img/' + img_name, mode='wb') as f:
        f.write(img_response.content)
    f.close()
    g = open('taobao.csv', mode='a', encoding='utf-8')
    title = driver.find_element(by='xpath',
                                value='/html/body/div[6]/div/div/div/div/div[%d]/a/div[2]/div' % i).get_attribute(
        'innerHTML')
    title = title.replace(
        '<img src="//img.alicdn.com/imgextra/i1/O1CN01rHZjwm1kc1MDCvBIO_!!6000000004703-2-tps-38-20.png">', '')
    g.write(title)
    price = driver.find_element(by='xpath',
                                value='/html/body/div[6]/div/div/div/div/div[%d]/a/div[3]' % i).get_attribute(
        'innerHTML')
    price = price.strip()

    if re.match('<span class="price-value"><em>¥</em>', price):
        price = price.strip('<span class="price-value"><em>¥</em>')
        price = price.replace("</span>", "")
        g.write(',' + price + '\n')
        g.close()


print("----程序至少运行60秒，请耐心等待------")

# 滚动使页面加载完成
for i in range(2000):
    driver.execute_script('scrollTo(0,%d)' % (i * 10))

open('taobao.csv', mode='w', encoding='utf-8')
for i in range(1, 300):  # 300为最大数，不可更大
    get_content(i)

print('运行结束')
