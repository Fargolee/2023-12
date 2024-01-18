亲测可用！写于2023年1月10号！别的地方搜到的都不靠谱！

```
#encoding='utf-8'
from selenium import webdriver
import time
import re
from selenium.webdriver.common.by import By
import pandas as pd
import os

def close\_windows():
    #如果有登录弹窗，就关闭
    try:
        dr.implicitly\_wait(20)#智能等待20秒，等待页面的元素加载出来后，就继续执行，下同
        if dr.find\_element(By.XPATH,'//div\[@class="boss-login-dialog"\]//i\[@class="icon-close"\]'):
            dr.find\_element(By.XPATH,'//div\[@class="boss-login-dialog"\]//i\[@class="icon-close"\]').click()
            #13 14行代码的作用是判断是否有弹出登录框，如果弹出登录框则右上角的关闭按钮，若无则跳过执行并告知没有弹窗
    except BaseException as e:
        print('close\_windows,没有弹窗',e)

def get\_current\_region\_job(k\_index,query, city\_no):
    #该函数的作用是获取指定城市指定区域的岗位信息
    #北京101010100
    #上海101020100
    #杭州101210100
    flag = 0
    df\_empty = pd.DataFrame(columns=\['岗位', '地点', '薪资', '工作经验', '学历', '公司', '技能'\])

    global dr
    dr = webdriver.Chrome(executable\_path='/Users/liulinghua/PycharmProjects/NickProject/venv/chromedriver')
    # 将浏览器最大化显示
    dr.maximize\_window()

    # 转到目标网址
    dr.get("https://www.zhipin.com/c101010100/?query={0}&ka=sel-city{1}".format(query, city\_no))  # 北京
    print("打开网址")
    time.sleep(5)
    while (flag == 0):
        close\_windows()
        dr.implicitly\_wait(20)
        job\_list = dr.find\_elements(By.XPATH,'//ul\[@class="job-list-box"\]/li')#这里是获取所有的岗位信息块
        for job in job\_list:#获取当前页的职位30条
            job\_name = job.find\_element(By.CSS\_SELECTOR, '.job-name').text#获取岗位名称
            job\_area = job.find\_element(By.CSS\_SELECTOR, '.job-area').text#获取岗位所在地区
            salary = job.find\_element(By.CSS\_SELECTOR, '.salary').text  # 获取薪资
            experience\_education = job.find\_element(By.XPATH, '//div\[@class="job-info clearfix"\]/ul\[@class="tag-list"\]')
            experience\_education\_list = experience\_education.find\_elements(By.TAG\_NAME, 'li')
            if len(experience\_education\_list)!=2:
                print('experience\_education\_list不是2个，跳过该数据',experience\_education\_list)
                break
            experience = experience\_education\_list\[0\].text
            education = experience\_education\_list\[1\].text
            # 上面31-37行代码是获取工作经验和学历要求
            dr.implicitly\_wait(20)
            company = job.find\_element(By.CSS\_SELECTOR, '.company-name').text#获取公司名
            dr.implicitly\_wait(20)
            skill\_div = job.find\_element(By.CSS\_SELECTOR,'.job-card-footer')
            skill\_list = skill\_div.find\_elements(By.TAG\_NAME,"li")
            skill = \[\]#存储技能的列表skill
            for skill\_i in skill\_list:
                skill\_i\_text = skill\_i.text
                if len(skill\_i\_text) == 0:
                    continue
                skill.append(skill\_i\_text)
            print("job\_skill:", skill)
            #39-50行代码是获取岗位的技能要求

            df\_empty.loc\[k\_index, :\] = \[job\_name, job\_area, salary, experience, education, company, skill\]
            k\_index = k\_index + 1
            print("已经读取数据{}条".format(k\_index))
        close\_windows()
        try:#点击下一页
            dr.implicitly\_wait(20)
            cur\_page\_num=dr.find\_element(By.XPATH,'//div\[@class="options-pages"\]//a\[@class="selected"\]').text#当前所在页面的按钮上的数字
            print('cur\_page\_num:',cur\_page\_num)
            #点击下一页
            dr.implicitly\_wait(20)
            element = dr.find\_element(By.XPATH,'//i\[@class="ui-icon-arrow-right"\]')#找到点击下一页的按钮
            dr.implicitly\_wait(20)
            dr.execute\_script("arguments\[0\].click();", element)
            dr.implicitly\_wait(20)
            new\_page\_num=dr.find\_element(By.XPATH,'//div\[@class="options-pages"\]//a\[@class="selected"\]').text#点击下一页按钮后，当前所在页面的按钮上的数字
            print('new\_page\_num',new\_page\_num)
            if cur\_page\_num==new\_page\_num:#如果当前页面与最新页面的数字一致，则表示已经是最后一页，跳出循环
                flag = 1
                break
        except BaseException as e:
            print('点击下一页错误',e)
            break
    dr.quit()
    # 退出浏览器
    print(df\_empty)
    #写入数据到CSV中
    if os.path.exists("数据.csv"):#存在追加，不存在创建
        df\_empty.to\_csv('数据.csv', mode='a', header=False, index=None, encoding='gb18030')
    else:
        df\_empty.to\_csv("数据.csv", index=False, encoding='gb18030')

    return k\_index

if \_\_name\_\_ == '\_\_main\_\_':
    #get\_current\_region\_job(0,'电竞','101210100')#杭州
    get\_current\_region\_job(0,'电竞','101020100')#北京
    #想要获取其他职位，其他城市，替换搜索关键词或BOSS上对应的城市代号即可

```