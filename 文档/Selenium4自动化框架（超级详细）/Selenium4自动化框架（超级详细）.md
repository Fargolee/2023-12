**目录**

[Selenium4](#Selenium4)

[安装Selenium](#%E5%AE%89%E8%A3%85Selenium)

[安装浏览器驱动](#%E5%AE%89%E8%A3%85%E6%B5%8F%E8%A7%88%E5%99%A8%E9%A9%B1%E5%8A%A8)

 [实战案例](#%C2%A0%E5%AE%9E%E6%88%98%E6%A1%88%E4%BE%8B)

[导入模块及浏览器驱动](#%E5%AF%BC%E5%85%A5%E6%A8%A1%E5%9D%97%E5%8F%8A%E6%B5%8F%E8%A7%88%E5%99%A8%E9%A9%B1%E5%8A%A8)

[导入模块](#%E5%AF%BC%E5%85%A5%E6%A8%A1%E5%9D%97)

[启动驱动](#%E5%90%AF%E5%8A%A8%E9%A9%B1%E5%8A%A8)

[定位元素](#%E5%AE%9A%E4%BD%8D%E5%85%83%E7%B4%A0)

[id、name、class定位](#id%E3%80%81name%E3%80%81class%E5%AE%9A%E4%BD%8D)

[tag\_name定位](#tag_name%E5%AE%9A%E4%BD%8D)

[xpath定位](#xpath%E5%AE%9A%E4%BD%8D)

[css选择器定位](#css%E9%80%89%E6%8B%A9%E5%99%A8%E5%AE%9A%E4%BD%8D)

[link\_text、partial\_link\_text定位](#link_text%E3%80%81partial_link_text%E5%AE%9A%E4%BD%8D)

[其他定位](#%E5%85%B6%E4%BB%96%E5%AE%9A%E4%BD%8D)

[定位一组元素](#%E5%AE%9A%E4%BD%8D%E4%B8%80%E7%BB%84%E5%85%83%E7%B4%A0)

[执行操作](#%E6%89%A7%E8%A1%8C%E6%93%8D%E4%BD%9C)

[浏览器操作](#%E6%B5%8F%E8%A7%88%E5%99%A8%E6%93%8D%E4%BD%9C)

[获取信息](#%E8%8E%B7%E5%8F%96%E4%BF%A1%E6%81%AF)

[导航](#%E5%AF%BC%E8%88%AA)

[警告框](#%E8%AD%A6%E5%91%8A%E6%A1%86)

[添加、获取、删除Cookies](#%E6%B7%BB%E5%8A%A0%E3%80%81%E8%8E%B7%E5%8F%96%E3%80%81%E5%88%A0%E9%99%A4Cookies)

[浏览器窗口](#%E6%B5%8F%E8%A7%88%E5%99%A8%E7%AA%97%E5%8F%A3)

[鼠标操作](#%E9%BC%A0%E6%A0%87%E6%93%8D%E4%BD%9C)

[单击左键](#%E5%8D%95%E5%87%BB%E5%B7%A6%E9%94%AE)

[单击右键](#%E5%8D%95%E5%87%BB%E5%8F%B3%E9%94%AE)

[双击左键](#%E5%8F%8C%E5%87%BB%E5%B7%A6%E9%94%AE)

[拖动](#%E6%8B%96%E5%8A%A8)

[悬停](#%E6%82%AC%E5%81%9C)

[滑动](#%E6%BB%91%E5%8A%A8)

[键盘操作](#%E9%94%AE%E7%9B%98%E6%93%8D%E4%BD%9C)

[等待](#%E7%AD%89%E5%BE%85)

[显式等待](#%E6%98%BE%E5%BC%8F%E7%AD%89%E5%BE%85)

[隐式等待](#%E9%9A%90%E5%BC%8F%E7%AD%89%E5%BE%85)

[强制等待](#%E5%BC%BA%E5%88%B6%E7%AD%89%E5%BE%85)

[关闭浏览器释放资源](#%E5%85%B3%E9%97%AD%E6%B5%8F%E8%A7%88%E5%99%A8%E9%87%8A%E6%94%BE%E8%B5%84%E6%BA%90)

***

## Selenium4

Selenium4是一个用于Web应用的自动化测试工具，利用它可以驱动浏览器执行特定的工作，其直接运行在浏览器中，就像真正的用户在操作一样。其主要功能有：测试应用程序与浏览器的兼容性，测试应用程序功能。

### 安装Selenium

安装Selenium只需要执行如下代码即可：

```
pip install selenium

```

当出现安装超时异常时，可以在代码后面添加：--default-time=1000，如下所示：

```
pip install selenium --default-timeout=1000

```

或者切换到国内源的方式来安装。

安装成功后，执行如下操作来查看安装的版本：

```
pip show selenium

```

如下所示：

![](./image/fcf81cab0d024ec092f9675c661d915a.png)

 安装了selenium是不是可以做自动化测试了呢？答案是：不是。

Selenium是用于Web应用的自动化测试工具，那当然使用浏览器的驱动。

### 安装浏览器驱动

这里我使用的是Chrome的浏览器，所以演示安装Chrome的浏览器驱动——chromedriver。

在安装浏览器驱动之前，需要查看自己的浏览器版本，如下图所示：

![](./image/96eff1d1ce4b42c4af850ce8591fa336.png)

接下来我们在[chromedriver](https://registry.npmmirror.com/binary.html?path=chromedriver/ "chromedriver")官网下载对应的版本，如下图所示：

![](./image/dda96f7e914649dd8781a97f1a4c979d.png)

 这里我们的chrome浏览器的版本为113.0.5672.127，那么我们选择113.0.5672.63/版本下载即可。

![](./image/1cec570b080a4433a975da553e2fd074.png) 

这里我们下载的是window版本的Chromedriver，这里没有64位的，那么我们下载32位即可。

下载后解压并把解压的chromedriver.exe文件拖到Python的Scripts目录下即可，如下图所示：

![](./image/384698b7befc4dc28a84605ea5f4d1b0.png)

###  实战案例

接下来我们通过在百度搜索演示自动化搜索内容来体验一下如何实现自动化。示例代码如下：

```python
# 导入selenium模块
from selenium import webdriver

from time import sleep
from selenium.webdriver.common.by import By

# 启动浏览器驱动
driver=webdriver.Chrome()

# 访问url
driver.get('https://www.baidu.com')

# 定位元素
el=driver.find_element(By.ID,'kw')

# 执行自动化操作
el.send_keys('NBA头条')
bt=driver.find_element(By.ID,'su').click()
# 休眠5秒
sleep(5)

# 关闭浏览器并释放进程资源
driver.quit()

```

运行上面的代码，运行结果如下：

![](./image/ea3d99d777854ba0b5a9bac7ecd03468.gif)

 在上面的自动化中可以得出自动化测试基本步骤为：

1.  导入自动化测试模块并启动浏览器驱动；
    
2.  访问测试网页；
    
3.  定位元素；
    
4.  执行测试操作；
    
5.  关闭浏览器并释放资源。
    

接下来我们将一一讲解上面的步骤。

## 导入模块及浏览器驱动

### 导入模块

在进行自动化测试之前，首先需要导入webdriver模块，代码如下：

```
from selenium import webdriver

```

webdriver是selenium模块中的一个子模块，其取代了嵌入到被测试Web应用中的JavaScript，与浏览器的紧密集成支持创建更高级的测试，避免了JavaScript安全模型导致的限制。

是一个基于HTTP网络协议进行交互的服务(俗称代理)，用于接收和处理两端的信息内容。

其工作基本流程为：

![](./image/39f1f59b4b49441cbd73e69800b7dcf6.png)

 Webdriver接收到代码后，经过处理来发送给浏览器，浏览器根据处理后的代码执行对应的操作，浏览器执行后完把执行结果返回给Webdriver，Webdriver将执行结果处理并返回给代码展示出来。

### 启动驱动

启动浏览器驱动只需要调用webdriver模块中的函数即可，语法格式如下：

```
webdriver.浏览器名()

```

注意：浏览器名首字母需要大写且后面加括号。

示例代码如下：

```
driver=webdriver.Chrome()   #启动谷歌浏览器驱动

```

这里我们启动的是Chrome浏览器的驱动，其他主流浏览器启动代码如下：

```
driver=webdriver.Ie()      #启动IE浏览器驱动
driver=webdriver.Firefox()      #启动火狐浏览器驱动
driver=webdriver.Edge()    #启动Edge浏览器驱动

```

## 定位元素

设置好窗口后，想要执行自动化操作，需要定位页面源码中显示的所有HTML所包含的元素内容。

我们有八种元素定位的方法：id、name、class、tag\_name、xpath、css\_selector、link\_text、partial\_link\_text。

### id、name、class定位

在一般情况下，页面源码中的id都是唯一的，所以只要知道页面元素中的id，就可以定位到该元素，但name、class值可以有重复，所以要注意页面元素中的name、class值有没有重复，假如有的话，selenium默认会返回第一个name或class的元素，假设有如下页面元素标签：

```
<input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">

```

我们只需要使用find\_element()方法来定位该元素，该方法语法格式如下：

```python
from selenium.webdriver.common.by import By
driver.find_element(By.ID,'元素id')
driver.find_element(By.name,'元素name')
driver.find_element(By.class,'元素class')

# 或
driver.find_element('id','元素id')
driver.find_element('name','元素name')
driver.find_element('class','元素class')

```

示例代码如下：

```python
from selenium.webdriver.common.by import By
driver.find_element(By.ID,'kw')
driver.find_element(By.name,'wd')
driver.find_element(By.class,'s_ipt')

```

这样就可以定位到元素了。

### tag\_name定位

tag\_name定位是通过标签名来定位，例如div、a、input标签等等，当页面中存在多个相同的标签时，默认返回第一个标签元素，其语法格式如下：

```python
from selenium.webdriver.common.by import By
driver.find_element(By.TAG_NAME,"标签名")
# 或
driver.find_element('tag name',"标签名")

```

假设有如下页面元素标签：

```
<input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">

```

示例代码如下：

```python
from selenium.webdriver.common.by import By
driver.find_element(By.TAG_NAME,"input")
# 或
driver.find_element('tag name',"input")

```

这样就可以定位到input标签了。

### xpath定位

xpath是XML路径语言，是XML文档中定位元素的语言，常用的规则如下表所示：

表达式

描述

nodename

获取该节点的所有子节点

/

从当前节点获取直接子节点

//

从当前节点获取子孙节点

\*

获取当前节点

\*\*

获取当前节点的父节点

@

选取属性

\[\]

添加筛选条件

例如：

```
//title[@lang='eng']

```

其表示选择所有名称为title，同时属性lang的值为eng的节点。

在Selenium自动化测试中，使用xpath定位元素语法格式如下：

```python
from selenium.webdriver.common.by import By
driver.find_element(By.XPATH,"xpath规则")
# 或
driver.find_element('xpath',"xpath规则")

```

接下来我们定位百度搜索的输入框，如下图所示：

![](./image/0504516c06fd46579a9f16038acaaa37.png)

 示例代码如下：

```bash
from selenium.webdriver.common.by import By
driver.find_element(By.XPATH,'//input[@id="kw"]')
#或
driver.find_element('xpath','//input[@id="kw"]')

```

这样就可以定位到百度输入框的元素了。

使用xpath定位时，还可以使用运算符来增加定位的准确性，运算符如下表所示：

运算符

描述

or

或运算

and

与运算

mod

计算除法的余数

|

计算两个节点集

+、-、\*、div

加法、减法、乘法、除法

\=、!=、<、<=、>、>=

等于、不等于、小于、小于等于、大于、大于等于

示例代码如下：

```bash
from selenium.webdriver.common.by import By
driver.find_element(By.XPATH,'//input[@id="kw" and @name="wd"]')
#或
driver.find_element('xpath','//input[@id="kw" and @name="wd"]')

```

这样就可以定位到百度输入框的元素了。

### css选择器定位

css选择器是用于查找HTML元素，定位速度比xpath快，css选择器常用语法表达式如下表：

表达式

例子

描述

#

#myid

选择id为myid的元素

.

.myclass

选择class为myclass的元素

\*

\*

选择所有元素

element

div

选择div标签元素

\>

div>li

选择div的所有li元素

+

div+li

选择同一级中在div之后的所有li元素

\[=\]

type='mytest'

选择type值为mytest的元素

在Selenium自动化定位中，使用css选择器语法格式如下：

```bash
from selenium.webdriver.common.by import By
driver.find_element(By.CSS_SELECTOR,"css选择")
# 或
driver.find_element('css selector',"css选择")

```

示例代码如下：

```bash
from selenium.webdriver.common.by import By
driver.find_element(By.CSS_SELECTOR,"#kw")
# 或
driver.find_element('css selector',"#kw")

```

这样就可以定位到元素了。

### link\_text、partial\_link\_text定位

link\_text、partial\_link\_text都是用来定位标签内的文本，其中link\_text必须指明标签内的全部文本，而partial\_link\_text只需要指定标签内部分文本即可定位，其语法格式如下：

```bash
from selenium.webdriver.common.by import By
driver.find_element(By.LINK_TEXT,'标签内全部文本')
driver.find_element(By.PARTIAL_LINK_TEXT,'标签内部分文本')

# 或
driver.find_element('link text','标签内全部文本')
driver.find_element('partial link text','partial link text')

```

假设有如下标签：

```
<div class="myclass">自动化测试工具selenium</div>

```

示例代码如下：

```bash
from selenium.webdriver.common.by import By
driver.find_element(By.LINK_TEXT,'自动化测试工具selenium')
driver.find_element(By.PARTIAL_LINK_TEXT,'自动化')

# 或
driver.find_element('link text','自动化测试工具selenium')
driver.find_element('partial link text','自动化')

```

这样就可以定位该div标签元素了。

### 其他定位

除了上面的八种定位元素的方法，Selenium4引进了相对定位器。

相对定位器是依据人的习惯来进行定位，通过上下左右和附近五种方法定位。

### 定位一组元素

在上面的定位元素中，只能定位一个元素，等我们想定位一组元素时，例如，定位一组a标签，如下图所示：

![](./image/6fb9fe1481ca42379325b2412d5e34ae.png)

 当我们想定位红框中a标签时，只需要把find\_element改为find\_elements即可，代码如下所示：

```
el=driver.find_elements(By.XPATH,'//*[@id="s-top-left"]/a')

```

运行结果如下：

![](./image/c101a8e0095144d6b316779f4eb0db00.png)

## 执行操作

### 浏览器操作

浏览器操作常用的操作有：

-   获取浏览器信息，导航；
    
-   处理警告框；
    
-   添加、获取、删除Cookies；
    
-   大小、切换窗口。
    

#### 获取信息

获取浏览器信息主要有获取标签、当前URL，其方法分别如下所示：

```bash
driver.title  # 获取浏览器当前页面的标签
driver.current_url  # 获取浏览器当前地址栏的URL
driver.page_source  # 获取当前html源码
driver.name   # 获取浏览器名称(chrome)
driver.get_window_rect() # 获取浏览器尺寸，位置
driver.get_window_position() # 获取浏览器位置(左上角)


```

示例代码如下：

```bash
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
title=driver.title
url=driver.current_url
print(title,url)

```

运行输出如下：

```
百度一下，你就知道 https://www.baidu.com

```

这样就成功获取到浏览器的当前页的标签及URL链接了。

#### 导航

导航最常用的操作是打开、前进、后退和刷新页面，其实现方法分别为：

```
driver.get(url)     # 打开网页
driver.back()     # 返回上一个页面
driver.forward()    # 回到下一个页面
driver.refresh()       # 刷新本页面

```

示例代码如下：

```bash
from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")   # 打开百度
driver.get('https://cn.bing.com')   # 打开必应
sleep(2)  
driver.back()         # 返回百度网页
sleep(2)
driver.forward()        # 前进必应网页
driver.refresh()        # 刷新必应网页

```

运行结果如下：

![](./image/0ca6d5385c1d4f8caf69450ea6395e50.gif)

 这样就实现了浏览器的打开、后退、前进、刷新操作。

#### 警告框

有三种警告框：Alerts警告框、Confirm确认框、Prompt 提示框。

**Alerts警告框**：其显示一条自定义消息及关闭该警告框的按钮，如下图所示：

![](./image/25f1602995214da8aaac0a71728b5bef.png)

 **Confirm确认框**：其显示一条自定义消息及确认和取消该警告框的按钮，如下图所示：

![](./image/5310defdb2084f80a45db7aa01a30887.png)

 **Prompt 提示框**：其显示一条自定义消息、输入文本框及确认和取消该警告框的按钮，如下图所示：

![](./image/7b72db23245446d7b8a86dacfcde83df.png)

 处理这些警示框，首先使用switch\_to.alert自动定位当前警示框，再使用text、accpet、dismiss、send\_keys等方法进行操作操作，其中：

-   text：获取警示框内的文字；
    
-   accpet：接受（确认）弹窗内容；
    
-   dismiss：解除（取消）弹窗；
    
-   send\_keys： 发送文本至警告框。
    

接下来我们在Selenium的开发文档网页中演示如何处理警告框，该网页如下所示：

![](./image/e64c7e3ab37b46bf98a5e0d34d38407b.png)

 Alerts警示框示例代码如下：

```bash
from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/zh-cn/documentation/webdriver/interactions/alerts/")
driver.find_element('link text','查看样例警告框').click()
sleep(5)
alert = driver.switch_to.alert
alert.accept()
sleep(5)
driver.find_element('link text','查看样例警告框').click()

```

首先我们打开Selenium开发文档官网，再通过link\_text来定位警示框弹出框，为了更好地看到效果，这里我们使用了sleep休眠，运行结果如下：

![](./image/e275e89854974be48363a3d92ea46843.gif)

 Confirm确认框、Prompt提示框和Alerts警示框几乎一样，只是定位元素的内容不同，这里我就不一一解释了，直接上代码：

```bash
# Confirm确认框
from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/zh-cn/documentation/webdriver/interactions/alerts/")
driver.find_element('link text','查看样例确认框').click()
sleep(1)
Confirm=driver.switch_to.alert
Confirm.dismiss()


# Prompt提示框
from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/zh-cn/documentation/webdriver/interactions/alerts/")
driver.find_element('link text','查看样例提示框').click()
sleep(1)
Confirm=driver.switch_to.alert
Confirm.dismiss()

```

#### 添加、获取、删除Cookies

Cookies主要用于识别用户并加载存储的信息，有些情况，我们需要携带Cookies才可以继续访问浏览器或者浏览网页的更多信息，在Selenium自动化测试中，我们通过使用如下方法来添加、获取、删除Cookies，

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.add_cookie(Cookies值)     # 添加Cookies
driver.get_cookie(Cookies名称)       # 获取单个Cookies
driver.get_cookies()      # 获取全部Cookies
driver.delete_cookie(Cookies名称)    # 删除单个Cookies
driver.delete_all_cookies()      # 删除全部Cookies

```

注意：添加Cookie仅接受一组已定义的可序列化JSON对象。

示例代码如下：

```python
from time import sleep

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
sleep(1)
driver.add_cookie({'name':'mycookies','value':'123456'}) # 添加名为mycookies的cookies，其值为123456
print(driver.get_cookie('mycookies'))       # 获取名为mycookies的cookies信息
print(driver.get_cookies())             # 获取全部cookies的信息
driver.delete_cookie('mycookies')        # 删除名为mycookies的信息
print(driver.get_cookies())         # 获取全部cookies的信息
driver.delete_all_cookies()         # 删除全部cookies的信息 
print(driver.get_cookies())         # 获取全部cookies的信息

```

运行结果如下所示：

![](./image/f46eb7f123ef4a0ab048670ea5944069.png)

 这样就成功实现了添加、获取、删除Cookies值了。

#### 浏览器窗口

大小

webdriver提供了set\_window\_size(宽, 高)来修改自动化测试时浏览器启动的窗口大小，示例代码如下：

```python
from selenium import webdriver    #导入模块
driver = webdriver.Chrome()     #启动浏览器驱动
driver.get('https://www.baidu.com')
driver.set_window_size(1500, 800)   #调整浏览器高为800，宽为1500

```

也可以使用maximize\_window()方法使窗体最大化，示例代码如下：

```python
from selenium import webdriver    #导入模块
driver = webdriver.Chrome()     #启动浏览器驱动
driver.get('https://www.baidu.com')
driver.maximize_window()   #最大化窗口

```

切换

在进行浏览器操作时，打开了一个新的标签页后，代码监控的浏览器标签页并不是最新打开的标签页，示例代码如下：

```python
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://blog.csdn.net/')

el=driver.find_element(By.ID,'toolbar-search-input')
el.send_keys('Selenium')
bt=driver.find_element(By.ID,'toolbar-search-button').click()
sleep(2)
print(driver.title)  # 输出标签页标题
driver.quit()

```

运行上面的代码，终端输出的内容是：

```
CSDN博客-专业IT技术发表平台

```

但最新的标签页标题为：Selenium- CSDN搜索。

这时我们需要获取打开的窗口句柄，并切换到最新的窗口，示例代码如下：

```python
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://blog.csdn.net/')

el=driver.find_element(By.ID,'toolbar-search-input')
el.send_keys('Selenium')
bt=driver.find_element(By.ID,'toolbar-search-button').click()
windows = driver.window_handles   # 获取浏览器打开的窗口句柄
driver.switch_to.window(windows[-1])  # 切换到最新的窗口
sleep(2)
print(driver.title)  # 输出标签页标题
driver.quit()

```

运行结果为：Selenium- CSDN搜索。

注意：获取窗口句柄的返回值类型为数组，而且最新的窗口句柄放在数组最后面，所以通过-1下标来获取最新的句柄。

新建

当我们需要新建一个页面方法其他URL链接时，可以使用new\_window()方法，示例代码如下：

```python
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('https://cn.bing.com/')
driver.switch_to.new_window()   # 新建标签页
driver.get('https://www.baidu.com/')
sleep(5)      # 休眠5秒
driver.quit()     # 关闭浏览器并释放进程资源

```

运行结果如下：

![](./image/87892dbe765f475dbcedba011efe270f.gif) 

截图

我们可以通过get\_screenshot\_as\_file()方法对打开的标签页进行截图保存，示例代码如下：

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.get_screenshot_as_file('screenshot.png')
driver.quit()

```

### 鼠标操作

常用的鼠标操作方法如下：

方法

描述

click()

单击左键

context\_click()

单击右键

double\_click()

双击

drag\_and\_drop()

拖动

move\_to\_element()

鼠标悬停

perform()

执行所有ActionChains中存储的动作

除了单击左键，上面的方法需要用到ActionChains方法，而且需要使用perform方法执行ActionChains的动作。

#### 单击左键

单击左键使用click()方法即可，示例代码如下：

```
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
el=driver.find_element(By.ID,'kw')
el.send_keys('NBA头条')
bt=driver.find_element(By.ID,'su').click()  # 单击左键
sleep(3)   # 休眠3秒
driver.quit()     # 关闭浏览器并释放进程资源

```

这里我们定位了搜索按钮，然后鼠标单击左键就会跳到了搜索结果页，运行结果如下：

![](./image/fa506f9b96a148bf968c797ed3697508.gif)

#### 单击右键

单击右键使用context\_click()方法即可，示例代码如下：

```python
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
bt=driver.find_element(By.ID,'su')  # 定位元素
ActionChains(driver).context_click(bt).perform()        # 使用ActionChains方法调用context_click方法实现单击右键
sleep(3)   # 休眠3秒
driver.quit()     # 关闭浏览器并释放进程资源

```

运行结果如下：

![](./image/8e6d83444101447b98204853fa2ec776.gif)

#### 双击左键

双击左键使用double\_click()方法即可，示例代码如下：

```
# 定位搜索按钮
button = driver.find_element('选择器','元素位置')
# 执行双击动作
ActionChains(driver).double_click(button).perform()

```

#### 拖动

拖动鼠标使用drag\_and\_drop()方法，该方法需要传递两个参数：

-   source：拖动的元素；
    
-   target：拖到目标位置；
    

示例代码如下：

```
# 定位要拖动的元素
source = driver.find_element('选择器','xxx')
# 定位目标元素
target = driver.find_element('选择器','')
# 执行拖动动作
ActionChains(driver).drag_and_drop(source, target).perform()

```

#### 悬停

鼠标悬停使用move\_to\_element()方法来实现，示例代码如下：

```python
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
bt=driver.find_element(By.XPATH,'//*[@id="s-top-left"]/div/a')  # 定位元素
ActionChains(driver).move_to_element(bt).perform()        # 使用ActionChains方法调用context_click方法实现单击右键
sleep(2)   # 休眠2秒
driver.quit()     # 关闭浏览器并释放进程资源

```

运行结果如下：

![](./image/40e61a67b18f4561bee9ff835e643ae8.gif)

#### 滑动

滑动操作需要使用execute\_script方法来实现，其传入的参数为JavaScript代码，示例代码如下：

```python
from time import sleep

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.runoob.com/")
js='window.scrollTo(0, 500);'
# 使用execute_script方法执行JavaScript代码来实现鼠标滚动
driver.execute_script(js) # 向下滚动 500 像素
sleep(5)
driver.quit()

```

运行结果如下：

![](./image/9e78eef5b7554660854f130ddbafa848.gif)

除了自定滑动的距离，我们还可以指定滑动到的页面元素，示例代码如下：

```python
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_window_size(500, 500)
driver.get("https://www.baidu.com/")
sleep(2)
target = driver.find_element(By.ID,'su')        # 定位元素
driver.execute_script("arguments[0].scrollIntoView();", target) # 滑动到定位元素
sleep(2)
driver.quit()

```

运行结果如下：

![](./image/aa9bc4bbd6c44e6b9a54f71b7f9e5232.gif)

### 键盘操作

在webdriver中的keys类中，提供了很多按键方法，常用的按键操作有：

操作

描述

Keys.ENTER

回车键

Keys.BACK\_SPACE

删除键

Keys.CONTROL

Ctrl键

Keys.F1

F1键

Keys.SPACE

空格

Keys.TAB

Tab键

Keys.ESCAPE

ESC键

Keys.ALT

Alt键

Keys.SHIFT

Shift键

Keys.ARROW\_DOWN

向下箭头

Keys.ARROW\_LEFT

向左箭头

Keys.ARROW\_RIGHT

向右箭头

Keys.ARROW\_UP

向上箭头

接下来我们以回车键来演示，示例代码如下：

```python
from selenium import webdriver
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
el=driver.find_element(By.ID,'kw')        # 定位元素
el.send_keys('NBA头条',Keys.ENTER)        # 输出内容后按回车键
sleep(2)    # 休眠2秒
driver.quit()   # 关闭浏览器并释放进程资源

```

运行结果如下：

![](./image/18d23bd131db481db933a5d7874d1e83.gif)

### 等待

由于页面元素不会一下子就全部渲染出来，当定位还没渲染出来的元素时，就会报错，那么我们需要设置一下等待，等待可以分为：显式等待、隐式等待和强制等待。

#### 显式等待

显式等待主要是使用WebDriverWait来实现，其语法格式如下：

```
WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)

```

其中：

-   driver：浏览器驱动；
    
-   timeout：最长超时时间，默认以秒为单位；
    
-   poll\_frequency：检测的间隔步长，默认为0.5s；
    
-   ignored\_exceptions：超时后的抛出的异常信息，默认抛出NoSuchElementExeception异常。
    

在使用WebDriverWait时，需要搭配until或until\_not方法来使用，其语法格式如下：

```
until(method,message='')
until_not(method,message='')

```

其中：

-   method：指定预期条件的判断方法；
    
-   message：超时后抛出的提示；
    

常用的method方法有：

方法

描述

title\_is('')

判断当前页面的 title 是否等于预期

title\_contains('')

判断当前页面的 title 是否包含预期字符串

presence\_of\_element\_located(locator)

判断元素是否被加到了 dom 树里，并不代表该元素一定可见

visibility\_of\_element\_located(locator)

判断元素是否可见，可见代表元素非隐藏，并且元素的宽和高都不等于0

visibility\_of(element)

跟上一个方法作用相同，但传入参数为 element

text\_to\_be\_present\_in\_element(locator ,'')

判断元素中的 text 是否包含了预期的字符串

text\_to\_be\_present\_in\_element\_value(locator ,‘’)

判断元素中的 value 属性是否包含了预期的字符串

frame\_to\_be\_available\_and\_switch\_to\_it(locator)

判断该 frame 是否可以 switch 进去，True 则 switch 进去，反之 False

invisibility\_of\_element\_located(locator)

判断元素中是否不存在于 dom 树或不可见

element\_to\_be\_clickable(locator)

判断元素中是否可见并且是可点击的

staleness\_of(element)

等待元素从 dom 树中移除

element\_to\_be\_selected(element)

判断元素是否被选中,一般用在下拉列表

element\_selection\_state\_to\_be(element,True)

判断元素的选中状态是否符合预期，参数 element，第二个参数为 True/False

element\_located\_selection\_state\_to\_be(locator,True)

跟上一个方法作用相同，但传入参数为 locator

alert\_is\_present()

判断页面上是否存在 alert

示例代码如下：

```python
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
element = WebDriverWait(driver, 2, 0.5,ignored_exceptions=None).until(EC.presence_of_element_located((By.ID, 'toolbar-search-input')),message='超时!') # 定位不存在的标签
element.send_keys('NBA',Keys.ENTER)
sleep(5)    # 休眠5秒
driver.quit()   # 关闭浏览器并释放进程资源

```

运行结果为：message：超时！

#### 隐式等待

Webdriver提供了三种隐式等待方法：

-   implicitly\_wait：识别对象时的超时时间；
    
-   set\_script\_timeout：异步脚本的超时时间；
    
-   set\_page\_load\_timeout：页面加载时的超时时间。
    

这三种方法的语法格式如下：

```
implicitly_wait('时间')
set_script_timeout('时间')
set_page_load_timeout('时间')

```

大家可以根据需求来选择隐式等待的方法，这里演示implicitly\_wait方法，示例代码如下：

```python
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.implicitly_wait(5)  # 隐式等待5秒
el=driver.find_element(By.ID,'kw1')  # 获取id为kw1的元素
el.send_keys('NBA头条')
bt=driver.find_element(By.ID,'su').click()  # 单击左键
sleep(3)   # 休眠5秒
driver.quit()     # 关闭浏览器并释放进程资源

```

id为kw1的元素不存在，所以5秒后就会报错。

#### 强制等待

强制等待通过休眠sleep方法来实现，不管元素是否存在、是否已加载出来，都会等到休眠时间结束才会继续下一步操作，示例代码如下：

```python
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
sleep(5)
el=driver.find_element(By.ID,'kw')
el.send_keys('NBA头条')
bt=driver.find_element(By.ID,'su').click()  # 单击左键
sleep(3)   # 休眠5秒
driver.quit()     # 关闭浏览器并释放进程资源

```

## 关闭浏览器释放资源

在完成自动化操作后，需要关闭浏览器并释放资源，示例代码如下：

```
driver.quit()  # 关闭所有标签页
driver.close()  # 关闭当前标签页

```

关闭当前标签页时，要注意切换到你想要关闭的标签页。

好了，Selenium4自动化框架就学到这里了。

公众号：白巧克力LIN

该公众号发布Python、数据库、Linux、Flask、自动化测试、Git、算法、Vue3等相关文章！

\- END -