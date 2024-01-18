(function () { const pages = \[ /^\\/$/, /^\\/following$/, /^\\/recommended$/, '^/pins.\*', '^/pin.\*', /^\\/course(?!\\/payment\\/)/, /^\\/post\\/.\*/, '^/hot.\*', /^\\/book\\/\\d+/, /^\\/video\\/\\d+/, /^\\/user\\/settings.\*/, /^\\/spost\\/\\d+/, /^\\/notification(?!\\/im)/, '^/backend', '^/frontend', '^/android', '^/ios', '^/ai', '^/freebie', '^/career', '^/article', \]; function isInJuejinApp() { const userAgent = typeof navigator !== 'undefined' ? navigator.userAgent : ''; return /juejin/i.test(userAgent); } if (typeof window !== 'undefined' && !isInJuejinApp()) { try { const path = window.location.pathname; const isAvailable = pages.some((page) => { const reg = new RegExp(page); return reg.test(path); }); if (isAvailable) { const localValue = localStorage.getItem('juejin\_2608\_theme') || '{}'; let { theme = 'light', isFollowSystem = false } = JSON.parse(localValue); if (isFollowSystem) { const themeMedia = window.matchMedia('(prefers-color-scheme: light)'); theme = themeMedia.matches ? 'light' : 'dark'; localStorage.setItem('juejin\_2608\_theme', JSON.stringify({ theme, isFollowSystem })); } document.body.setAttribute('data-theme', theme); } else { document.body.setAttribute('data-theme', 'light'); } } catch (e) { console.error('浏览器不支持localStorage'); } } })()

 [![稀土掘金](./image/e08da34488b114bd4c665ba2fa520a31.svg) ![稀土掘金](./image/6c61ae65d1c41ae8221a670fa32d05aa.svg)](/) 

-   首页
    
    -   [首页](/)
    -   [沸点](/pins)
    -   [课程](/course)
    -   [直播](/live)
    -   [活动](/events/all)
    -   [竞赛](/challenge)
    
    [商城](https://detail.youzan.com/show/goods/newest?kdt_id=104340304)
    
    [APP](/app?utm_source=jj_nav)
    
    [插件](https://juejin.cn/extension?utm_source=jj_nav)
    

-   -   搜索历史 清空
        
    -   创作者中心
        
        -   写文章
            
        -   发沸点
            
        -   写笔记
            
        -   写代码
            
        -   草稿箱
            
        
        创作灵感 查看更多
        
-   ![vip](./image/24127194d5b158d7eaf8f09a256c5d01.svg)
    
    会员
    
-   登录
    
    注册
    

   

 

  

# WebUI自动化测试中隐藏的元素如何操作？三种元素等待方式如何理解？

[虫无涯](/user/3655236621185246/posts)

2023-11-14 2 阅读5分钟

.markdown-body{word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#252933}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px}.markdown-body h1{font-size:24px;line-height:38px;margin-bottom:5px}.markdown-body h2{font-size:22px;line-height:34px;padding-bottom:12px;border-bottom:1px solid #ececec}.markdown-body h3{font-size:20px;line-height:28px}.markdown-body h4{font-size:18px;line-height:26px}.markdown-body h5{font-size:17px;line-height:24px}.markdown-body h6{font-size:16px;line-height:24px}.markdown-body p{line-height:inherit;margin-top:22px;margin-bottom:22px}.markdown-body img{max-width:100%}.markdown-body hr{border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px}.markdown-body code{word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em}.markdown-body code,.markdown-body pre{font-family:Menlo,Monaco,Consolas,Courier New,monospace}.markdown-body pre{overflow:auto;position:relative;line-height:1.75}.markdown-body pre>code{font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8}.markdown-body a{text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff}.markdown-body a:active,.markdown-body a:hover{color:#275b8c}.markdown-body table{display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6}.markdown-body thead{background:#f6f6f6;color:#000;text-align:left}.markdown-body tr:nth-child(2n){background-color:#fcfcfc}.markdown-body td,.markdown-body th{padding:12px 7px;line-height:24px}.markdown-body td{min-width:120px}.markdown-body blockquote{color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8}.markdown-body blockquote:after{display:block;content:""}.markdown-body blockquote>p{margin:10px 0}.markdown-body ol,.markdown-body ul{padding-left:28px}.markdown-body ol li,.markdown-body ul li{margin-bottom:0;list-style:inherit}.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item{list-style:none}.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul{margin-top:0}.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul{margin-top:3px}.markdown-body ol li{padding-left:6px}.markdown-body .contains-task-list{padding-left:0}.markdown-body .task-list-item{list-style:none}@media (max-width:720px){.markdown-body h1{font-size:24px}.markdown-body h2{font-size:20px}.markdown-body h3{font-size:18px}}.markdown-body pre,.markdown-body pre>code.hljs{color:#333;background:#f8f8f8}.hljs-comment,.hljs-quote{color:#998;font-style:italic}.hljs-keyword,.hljs-selector-tag,.hljs-subst{color:#333;font-weight:700}.hljs-literal,.hljs-number,.hljs-tag .hljs-attr,.hljs-template-variable,.hljs-variable{color:teal}.hljs-doctag,.hljs-string{color:#d14}.hljs-section,.hljs-selector-id,.hljs-title{color:#900;font-weight:700}.hljs-subst{font-weight:400}.hljs-class .hljs-title,.hljs-type{color:#458;font-weight:700}.hljs-attribute,.hljs-name,.hljs-tag{color:navy;font-weight:400}.hljs-link,.hljs-regexp{color:#009926}.hljs-bullet,.hljs-symbol{color:#990073}.hljs-built\_in,.hljs-builtin-name{color:#0086b3}.hljs-meta{color:#999;font-weight:700}.hljs-deletion{background:#fdd}.hljs-addition{background:#dfd}.hljs-emphasis{font-style:italic}.hljs-strong{font-weight:700}

# 1 自动化测试中隐藏的元素如何操作?

> 面试中，我们经常会遇到“隐藏元素是如何操作的？”带着这个问题我们看下如何操作？

## 1.1 实现方法

-   针对隐藏因素的操作，常用的操作是通过`JS`脚本定位到该元素，获取对应的元素对象，再通过`removeAttribute`和`setAttribute`两个方法完成属性的删除或重新复制操作，使得当前元素处于显示状态即可。

## 1.2 实现案例

-   以下是自定义的一个HTML页面，该页面是一个登陆页面，其中用户名和登陆按钮都是隐藏的，如下：

```python
<html>
<body>
	用户名:<input id="user_name" name="username" type="hidden" /><br>
	密码:<input id="pass_word" name="password" type="text" /><br>
	<button type="button" name="login" class="login_but" style="display:none;" />
</body>
</html>

```

## 1.3 实现思路

```python
#主要是使用JS脚本改变标签的属性值
hi_name = "document.getElementByID('user_name').setAttribute('type', 'text')"
print(driver.execute_script(hi_name ))

driver.find_element_by_id('user_name').send_keys("admin")
print(driver.find_element_by_name("login"))

driver.execute_script("document.getElementsClassName('login_but')[0].removeAttribute('style')")

```

# 2 三种元素等待方式如何理解？

> 在自动化测试中，会遇到一些比如环境不稳定、网络不稳定的因素，此时可能需要控制脚本执行速度，那么就需要用到元素等待操作。其实不一定设置等待就好，各有利弊，以下是一些观点仅供参考。

## 2.1 强制等待

-   方法：

```python
time.sleep(s)
# s表示具体时间，单位为秒。

```

-   含义：表示等待`s`秒后，进行下一步操作。直接使用`python`内置的`time`模块调用`sleep`方法即可。
-   说明：强制等待又称强制休眠。作用域为当前脚本。没过多行代码需要进行等待设置，那每行代码都需要进行相同的设置操作。
-   优缺点：

优缺点

说明

优点

使用简单，需要用时随时调用即可

缺点

代码重复率高，且影响代码执行速率。不能精确设置等待时间，过长过段貌似都不合适

-   示例：

```python
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost/zentao/user-login.html")

user_name = "$('input:first').val('admin')"
driver.execute_script(user_name)
time.sleep(0.5)

pass_wd = "$(':password').val('ZenTao123456')"
driver.execute_script(pass_wd)
time.sleep(1)

```

## 2.2 隐式等待

-   方法：

```python
driver.implicitly_wait(s)
# s表示具体时间，单位为秒。

```

-   含义：在`s`时间内，页面加载完成，进行下一步操作，直接通过浏览器驱动对象进行调用。
-   说明：隐式等待也称智能等待，也称全局等待。表示整个页面中的所有元素加载完才会执行，会根据内部设置的频率不断刷新页面继续加载并检测当前所执行的元素是否加载完成。

> 如果在设定的时间之前元素加载完成，则不会继续等待，继续执行下一步。

-   优缺点：

优缺点

说明

优点

对整个脚本的生命周期都起作用，只需要设置一次

缺点

程序会一直等待加载完成，才会执行下一步，但有时想要的元素加载完了，其他的元素没有加载完，仍要等待全部加载完才进行下一步，不是很灵活，也有点费时间。

-   示例：

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost/zentao/user-login.html")
driver.implicitly_wait(10)

user_name = "$('input:first').val('admin')"
driver.execute_script(user_name)

pass_wd = "$(':password').val('ZenTao123456')"
driver.execute_script(pass_wd)

```

## 2.3 显式等待

-   方法：

```python
# 导入包
from selenium.webdriver.support.wait import 
# 或者
from selenium.webdriver.support.ui import WebDriverWait

```

-   部分源码如下：

```python
lass WebDriverWait(object):
    def __init__(self, driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None):
        """Constructor, takes a WebDriver instance and timeout in seconds.

           :Args:
            - driver - Instance of WebDriver (Ie, Firefox, Chrome or Remote)
            - timeout - Number of seconds before timing out
            - poll_frequency - sleep interval between calls
              By default, it is 0.5 second.
            - ignored_exceptions - iterable structure of exception classes ignored during calls.
              By default, it contains NoSuchElementException only.

           Example:
            from selenium.webdriver.support.ui import WebDriverWait \n

```

-   参数说明：

参数

说明

`driver`

驱动器对象

`timeout`

设置刷新页面的超时时间

`poll_frequency`

页面刷新频率。默认`0.5s`

`ignored_exceptions`

表示忽略异常，如无法找到元素则抛出`NoSuchElementException`异常

-   `WebDriverWait`模块有两个方法`until`和`until_not`：

```python
    def until(self, method, message=''):
        """Calls the method provided with the driver as an argument until the \
        return value is not False."""
        screen = None
        stacktrace = None

        end_time = time.time() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, 'screen', None)
                stacktrace = getattr(exc, 'stacktrace', None)
            time.sleep(self._poll)
            if time.time() > end_time:
                break
        raise TimeoutException(message, screen, stacktrace)

``````python
    def until_not(self, method, message=''):
        """Calls the method provided with the driver as an argument until the \
        return value is False."""
        end_time = time.time() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if not value:
                    return value
            except self._ignored_exceptions:
                return True
            time.sleep(self._poll)
            if time.time() > end_time:
                break
        raise TimeoutException(message)

```

> 其中：
> 
> 1、method：传入对象分两种，一种是匿名函数；另一种是预置条件对象expected\_conditions。
> 
> 2、message：当出现异常时，把异常信息给message；
> 
> 3、expected\_conditions方法通过from selenium.webdriver.support import expected\_conditions引入。

-   含义：对单个元素设置一定的频率，使其按频率刷新当前页面并检测是都存在该元素。

`WebDriverWait`常用的几个方法如下：

### 2.3.1 判断元素是否被加入DOM树中，不可见

-   判断元素是否被加入`DOM`树中，并不代表元素可见，如果定位到就返回元素；

```python
get_ele = WebDriverWait(driver,10).until(expected_conditions.\
presence_of_element_located(By.ID, "xxx"))

```

### 2.3.2 判断元素是否被加入到DOM中，并可见

-   判断元素是否被加入到`DOM`中，并可见，代表元素可显示，宽和高都大于0；

```python
get_ele1 = WebDriverWait(driver,10).until(expected_conditions.visibility_of_elemen\
t_located((by=By.ID,value='yyy')))

```

### 2.3.3 判断元素是否可见

-   判断元素是否可见，可见返回该元素；

```python
get_ele2 = WebDriverWait(driver,10).until(expected_conditions.visibility_of(driver\
.find_element(by=By.ID,value='zzz')))

```

### 2.3.4 判断是否至少有1个元素存在DOM树中

-   判断是否至少有1个元素存在`DOM`树中，如果定位到就返回列表：

```python
get_ele3 = WebDriverWait(driver,10).until(expected_conditions.presence_of_all_elem\
ents_located(By.CSS_SELECTOR,'.boss')))

```

### 2.3.5 判断指定的元素的属性值中是否包含了预期的字符串

-   判断指定的元素的属性值中是否包含了预期的字符串，返回布尔值；

```python
get_ele4 = WebDriverWait(driver,10).until(expected_conditions.text_to_be_present_i\
n_element_value(By.CSS_SELECTOR,'#su'))

```

### 2.3.6 判断指定的元素中是否包含了预期的字符串

-   判断指定的元素中是否包含了预期的字符串，返回布尔值；

```python
get_ele5= WebDriverWait(driver,10).until(expected_conditions.text_to_be_present_i\
n_element(By.XPATH,"//#[@id='ul']", u'添加'))

```

### 2.3.7 判断元素是否存在DOM中或不可见

-   判断元素是否存在`DOM`中或不可见，如果可见，返回`False`，否则返回这个元素；

```python
get_ele6= WebDriverWait(driver,10).until(expected_conditions.invisibility_of_elem\
ent_located(By.CSS_SELECTOR,'#su'))

```

### 2.3.8 判断元素是否可见且状态为enable

-   判断元素是否可见且状态为`enable`(代表可点击)；

```python
get_ele7= WebDriverWait(driver,10).until(expected_conditions.element_to_be_clicka\
ble(By.CSS_SELECTOR,'#su')).click()

```

[

![avatar](./image/43b26e4825c1494fe485f75d30863340~200x200.image)

虫无涯 ![创作等级LV.4](./image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAA8AQMAAAAAMksxAAAAA1BMVEUAAACnej3aAAAAAXRSTlMAQObYZgAAAA5JREFUKM9jGAWjAAcAAAIcAAE27nY6AAAAAElFTkSuQmCC "创作等级LV.4")   

测开丨质量丨管理



](/user/3655236621185246/posts)

[

223

文章

](/user/3655236621185246/posts)[

39k

阅读

](/user/3655236621185246/posts)[

47

粉丝

](/user/3655236621185246/followers)

目录

收起

-   [1 自动化测试中隐藏的元素如何操作?](#heading-0 "1 自动化测试中隐藏的元素如何操作?")
    
    -   [1.1 实现方法](#heading-1 "1.1 实现方法")
        
    -   [1.2 实现案例](#heading-2 "1.2 实现案例")
        
    -   [1.3 实现思路](#heading-3 "1.3 实现思路")
        
-   [2 三种元素等待方式如何理解？](#heading-4 "2 三种元素等待方式如何理解？")
    
    -   [2.1 强制等待](#heading-5 "2.1 强制等待")
        
    -   [2.2 隐式等待](#heading-6 "2.2 隐式等待")
        
    -   [2.3 显式等待](#heading-7 "2.3 显式等待")
        
        -   [2.3.1 判断元素是否被加入DOM树中，不可见](#heading-8 "2.3.1 判断元素是否被加入DOM树中，不可见")
            
        -   [2.3.2 判断元素是否被加入到DOM中，并可见](#heading-9 "2.3.2 判断元素是否被加入到DOM中，并可见")
            
        -   [2.3.3 判断元素是否可见](#heading-10 "2.3.3 判断元素是否可见")
            
        -   [2.3.4 判断是否至少有1个元素存在DOM树中](#heading-11 "2.3.4 判断是否至少有1个元素存在DOM树中")
            
        -   [2.3.5 判断指定的元素的属性值中是否包含了预期的字符串](#heading-12 "2.3.5 判断指定的元素的属性值中是否包含了预期的字符串")
            
        -   [2.3.6 判断指定的元素中是否包含了预期的字符串](#heading-13 "2.3.6 判断指定的元素中是否包含了预期的字符串")
            
        -   [2.3.7 判断元素是否存在DOM中或不可见](#heading-14 "2.3.7 判断元素是否存在DOM中或不可见")
            
        -   [2.3.8 判断元素是否可见且状态为enable](#heading-15 "2.3.8 判断元素是否可见且状态为enable")
            

友情链接：

-   
-   
-   
-   
-   [extjs 右下角消息框](https://frontend.devrank.cn/traffic-aggregation/123994 "extjs 右下角消息框")
-   [图片滚动js代码](https://frontend.devrank.cn/traffic-aggregation/210759 "图片滚动js代码")
-   [python引号内不分隔](https://backend.devrank.cn/traffic-aggregation/999001 "python引号内不分隔")
-   [洪荒魔猿道小说](https://fanqienovel.com/keyword/3286711 "洪荒魔猿道小说")
-   [308宿舍闹鬼](https://fanqienovel.com/keyword/3038393 "308宿舍闹鬼")
-   [快穿之黑化吧前女友讲的什么](https://fanqienovel.com/keyword/3196604 "快穿之黑化吧前女友讲的什么")

window.\_\_NUXT\_\_=(function(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M){s.loading=a;s.skeleton=d;s.cursor=f;s.data=\[\];s.total=b;s.hasMore=d;C.id=u;C.self\_description=l;C.followed=a;C.viewerIsFollowing=l;C.community=l;C.subscribedTagCount=b;C.wroteBookCount=b;C.boughtBookCount=b;C.isBindedPhone=a;C.level=A;C.user\_id=u;C.user\_name=z;C.company=e;C.job\_title="测开丨质量丨管理";C.avatar\_large="https:\\u002F\\u002Fp9-passport.byteacctimg.com\\u002Fimg\\u002Fuser-avatar\\u002F43b26e4825c1494fe485f75d30863340~300x300.image";C.description="CSDN测试领域优质创作者 | CSDN博客专家 | 阿里云专家博主 | 华为云享专家 | 51CTO专家博主 |【专注测试领域各种技术研究、分享和交流~】";C.followee\_count=219;C.follower\_count=47;C.post\_article\_count=223;C.digg\_article\_count=225;C.got\_digg\_count=256;C.got\_view\_count=38583;C.post\_shortmsg\_count=79;C.digg\_shortmsg\_count=62;C.isfollowed=a;C.favorable\_author=b;C.power=B;C.study\_point=b;C.university={university\_id:f,name:e,logo:e};C.major={major\_id:f,parent\_id:f,name:e};C.student\_status=b;C.select\_event\_count=b;C.select\_online\_course\_count=b;C.identity=b;C.is\_select\_annual=a;C.select\_annual\_rank=b;C.annual\_list\_type=b;C.extraMap={};C.is\_logout=b;C.annual\_info=\[\];C.account\_amount=b;C.user\_growth\_info={user\_id:3655236621185246,jpower:B,jscore:2167.6,jpower\_level:A,jscore\_level:6,jscore\_title:"杰出掘友",author\_achievement\_list:\[\],vip\_level:b,vip\_title:e,jscore\_next\_level\_score:7000,jscore\_this\_level\_mini\_score:2000,vip\_score:b};C.is\_vip=a;C.become\_author\_days=b;C.collection\_set\_article\_count=b;C.recommend\_article\_count\_daily=b;C.article\_collect\_count\_daily=b;C.user\_priv\_info={administrator:b,builder:b,favorable\_author:b,book\_author:b,forbidden\_words:b,can\_tag\_cnt:b,auto\_recommend:b,signed\_author:b,popular\_author:b,can\_add\_video:b};C.juejinPower=B;C.jobTitle="测开丨质量丨管理";C.roles={isBookAuthor:a,isFavorableAuthor:a,isCobuilder:a,isAdmin:a};C.username=z;C.blogAddress=l;C.selfDescription="CSDN测试领域优质创作者 | CSDN博客专家 | 阿里云专家博主 | 华为云享专家 | 51CTO专家博主 |【专注测试领域各种技术研究、分享和交流~】";C.beLikedCount=256;C.beReadCount=38583;C.followerCount=47;C.followingCount=219;C.collectionCount=b;C.createdCollectionCount=b;C.followingCollectionCount=b;C.postedPostsCount=223;C.pinCount=79;C.likedArticleCount=225;C.likedPinCount=62;C.avatar="https:\\u002F\\u002Fp9-passport.byteacctimg.com\\u002Fimg\\u002Fuser-avatar\\u002F43b26e4825c1494fe485f75d30863340~300x300.image";C.latestLoginedInAt=c;C.createdAt=c;C.updatedAt=c;C.phoneNumber=e;C.titleDescription=e;C.followeesCount=219;C.applyEventCount=b;C.need\_lead=b;C.followTopicCnt=b;return {layout:"default",data:\[{renderPost:d}\],fetch:\[{queryString:e,isShowUserDropdownList:a,isShowAddMoreList:a,isFocus:a,isPhoneMenuShow:a,visibleBadge:a,placeholder:e,hiddenProperty:"hidden",searchHistoryVisible:a,searchHistoryItems:\[\],tabBadge:c,isChangePlaceholder:d,showMallBridge:a,removeSearchInputKeyupListener:c,logoImg:"\\u002F\\u002Flf3-cdn-tos.bytescm.com\\u002Fobj\\u002Fstatic\\u002Fxitu\_juejin\_web\\u002Fe08da34488b114bd4c665ba2fa520a31.svg"}\],error:c,state:{view:{activityIndex:{activityList:\[\],pageInfo:{hasNextPage:a,endCursor:e},afterPosition:e,activityListIsLoading:d,activityListIsError:a,userActivityList:\[\],placeholder:e,actionType:{FETCH:"@\\u002Fview\\u002Factivity-index\\u002FFETCH",FETCH\_RECOMMEND\_LIST:"@\\u002Fview\\u002Factivity-index\\u002FFETCH\_RECOMMEND\_LIST",RESET\_ACTIVITY\_LIST:"@\\u002Fview\\u002Factivity-index\\u002FRESET\_ACTIVITY\_LIST",FETCH\_USER\_ACTIVITY\_LIST:"@\\u002Fview\\u002Factivity-index\\u002FFETCH\_USER\_ACTIVITY\_LIST",FETCH\_NEW\_COUNT:"@\\u002Fview\\u002Factivity-index\\u002FFETCH\_NEW\_COUNT",DELETE\_ACTIVITY:"@\\u002Fview\\u002Factivity-index\\u002FDELETE\_ACTIVITY",TOGGLE\_FOLLOW\_USER:"@\\u002Fview\\u002Factivity-index\\u002FTOGGLE\_FOLLOW\_USER",FETCH\_ENTRY\_COMMENT\_LIST:"@\\u002Fview\\u002Factivity-index\\u002FFETCH\_ENTRY\_COMMENT\_LIST",UPDATE\_LIST\_LOADING:"@\\u002Fview\\u002Factivity-index\\u002FUPDATE\_LIST\_LOADING",RESET:"@\\u002Fview\\u002Factivity-index\\u002FRESET"},hotList:{list:\[\],after:e,loading:a,hasNextPage:a,actionType:{UPDATE\_STATE:"@\\u002Fview\\u002Factivity-index\\u002Fhot-list\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Factivity-index\\u002Fhot-list\\u002FFETCH\_MORE",FETCH:"@\\u002Fview\\u002Factivity-index\\u002Fhot-list\\u002FFETCH",RESET:"@\\u002Fview\\u002Factivity-index\\u002Fhot-list\\u002FRESET"}},sidebar:{bannerList:\[\],actionType:{RESET:"@\\u002Fview\\u002Factivity-index\\u002Fsidebar\\u002FRESET",UPDATE\_STATE:"@\\u002Fview\\u002Factivity-index\\u002Fsidebar\\u002FUPDATE\_STATE",FETCH\_BANNER:"@\\u002Fview\\u002Factivity-index\\u002Fsidebar\\u002FFETCH\_BANNER"},recommend:{pageSize:h,page:b,total:b,pointer:c,lastPointer:c,list:\[\],loading:a,error:c,canPrev:d,canNext:d,linkList:\[\],lastFetchOnServer:a,actionType:{UPDATE:"@\\u002Fview\\u002Factivity-index\\u002Fsidebar\\u002Frecommend-topic-list\\u002FUPDATE",FETCH:"@\\u002Fview\\u002Factivity-index\\u002Fsidebar\\u002Frecommend-topic-list\\u002FFETCH",FORCE\_FETCH:"@\\u002Fview\\u002Factivity-index\\u002Fsidebar\\u002Frecommend-topic-list\\u002FFORCE\_FETCH",FETCH\_MORE:"@\\u002Fview\\u002Factivity-index\\u002Fsidebar\\u002Frecommend-topic-list\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Factivity-index\\u002Fsidebar\\u002Frecommend-topic-list\\u002FRESET"},after:b},followed:{pageSize:h,page:b,total:b,pointer:c,lastPointer:c,list:\[\],loading:a,error:c,canPrev:d,canNext:d,linkList:\[\],lastFetchOnServer:a,actionType:{UPDATE:"@\\u002Fview\\u002Factivity-index\\u002Fsidebar\\u002Ffollowed-topic-list\\u002FUPDATE",FETCH:"@\\u002Fview\\u002Factivity-index\\u002Fsidebar\\u002Ffollowed-topic-list\\u002FFETCH",FORCE\_FETCH:"@\\u002Fview\\u002Factivity-index\\u002Fsidebar\\u002Ffollowed-topic-list\\u002FFORCE\_FETCH",FETCH\_MORE:"@\\u002Fview\\u002Factivity-index\\u002Fsidebar\\u002Ffollowed-topic-list\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Factivity-index\\u002Fsidebar\\u002Ffollowed-topic-list\\u002FRESET"},after:b},recommendPin:{list:\[\],after:e,loading:a,hasNextPage:d,actionType:{UPDATE\_STATE:"@\\u002Fview\\u002Factivity-index\\u002Fsidebar\\u002Frecommend-pin-list\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Factivity-index\\u002Fsidebar\\u002Frecommend-pin-list\\u002FFETCH\_MORE",FETCH:"@\\u002Fview\\u002Factivity-index\\u002Fsidebar\\u002Frecommend-pin-list\\u002FFETCH",RESET:"@\\u002Fview\\u002Factivity-index\\u002Fsidebar\\u002Frecommend-pin-list\\u002FRESET"}}},topicPinList:{pageSize:h,page:g,total:b,pointer:c,lastPointer:c,list:\[\],loading:a,error:c,canPrev:d,canNext:d,linkList:\[\],lastFetchOnServer:a,actionType:{UPDATE:"@\\u002Fview\\u002Factivity-index\\u002Ftopic-pin-list\\u002FUPDATE",FETCH:"@\\u002Fview\\u002Factivity-index\\u002Ftopic-pin-list\\u002FFETCH",FORCE\_FETCH:"@\\u002Fview\\u002Factivity-index\\u002Ftopic-pin-list\\u002FFORCE\_FETCH",FETCH\_MORE:"@\\u002Fview\\u002Factivity-index\\u002Ftopic-pin-list\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Factivity-index\\u002Ftopic-pin-list\\u002FRESET"},topicId:e,navList:\[{type:j,name:j,title:"推荐 ",id:j},{type:n,name:n,title:"热门 ",id:n},{type:q,name:q,title:"关注 ",id:q},{type:i,name:"opensource",title:"开源推荐 ",id:"5c09ea2b092dcb42c740fe73"},{type:i,name:"recruitment",title:"内推招聘",id:"5abb61e1092dcb4620ca3322"},{type:i,name:"dating",title:"掘金相亲",id:"5abcaa67092dcb4620ca335c"},{type:i,name:"slacking",title:"上班摸鱼",id:"5c106be9092dcb2cc5de7257"},{type:i,name:"app",title:"应用安利",id:"5b514af1092dcb61bd72800d"},{type:i,name:"tool",title:"开发工具",id:"5abb67d2092dcb4620ca3324"},{type:i,name:"news",title:"New资讯",id:"5c46a17f092dcb4737217152"}\],sortType:r}},search:{search\_result\_from:b,query:e,list:\[\],linkList:\[\],loading:a,skeleton:d,actionType:{FETCH:"@\\u002Fview\\u002Fsearch\\u002FFETCH",FETCH\_MORE:"@\\u002Fview\\u002Fsearch\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fsearch\\u002FRESET"}},columnIndex:{list:{pageSize:h,page:g,total:b,pointer:c,lastPointer:c,list:\[\],loading:a,error:c,canPrev:d,canNext:d,linkList:\[\],lastFetchOnServer:a,actionType:{UPDATE:"@\\u002Fview\\u002FcolumnIndex\\u002Flist\\u002FUPDATE",FETCH:"@\\u002Fview\\u002FcolumnIndex\\u002Flist\\u002FFETCH",FORCE\_FETCH:"@\\u002Fview\\u002FcolumnIndex\\u002Flist\\u002FFORCE\_FETCH",FETCH\_MORE:"@\\u002Fview\\u002FcolumnIndex\\u002Flist\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002FcolumnIndex\\u002Flist\\u002FRESET"},sort:o,category:"all"},hotList:{pageSize:h,page:g,total:b,pointer:c,lastPointer:c,list:\[\],loading:a,error:c,canPrev:d,canNext:d,linkList:\[\],lastFetchOnServer:a,actionType:{UPDATE:"@\\u002Fview\\u002FcolumnIndex\\u002FhotList\\u002FUPDATE",FETCH:"@\\u002Fview\\u002FcolumnIndex\\u002FhotList\\u002FFETCH",FORCE\_FETCH:"@\\u002Fview\\u002FcolumnIndex\\u002FhotList\\u002FFORCE\_FETCH",FETCH\_MORE:"@\\u002Fview\\u002FcolumnIndex\\u002FhotList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002FcolumnIndex\\u002FhotList\\u002FRESET"}}},timelineIndex:{tdkTemplates:\[\],categoryNavList:\[\],tagNavList:\[\],splitTagList:\[\],timelineAdList:\[\],list:\[\],sort:r,category:j,categoryId:e,tagId:e,tag:"全部",actionType:{FETCH\_TIMELINE\_LIST:"@\\u002Fview\\u002FtimelineIndex\\u002FFETCH\_TIMELINE\_LIST",FETCH\_CATEGORY\_LIST:"@\\u002Fview\\u002FtimelineIndex\\u002FFETCH\_CATEGORY\_LIST",FETCH\_TAG\_LIST:"@\\u002Fview\\u002FtimelineIndex\\u002FFETCH\_TAG\_LIST",DELETE\_ENTRY:"@\\u002Fview\\u002FtimelineIndex\\u002FDELETE\_ENTRY",DELETE\_USER\_ENTRIES:"@\\u002Fview\\u002FtimelineIndex\\u002FDELETE\_USER\_ENTRIES",DELETE\_TAG\_ENTRIES:"@\\u002Fview\\u002FtimelineIndex\\u002FDELETE\_TAG\_ENTRIES",FETCH\_MORE:"@\\u002Fview\\u002FtimelineIndex\\u002FFETCH\_MORE",FETCH:"@\\u002Fview\\u002FtimelineIndex\\u002FFETCH",RESET:"@\\u002Fview\\u002FtimelineIndex\\u002FRESET"},serverRenderTimelineList:a,timelineList:{list:\[\],cursor:f,skeleton:d,loading:a,hasMore:d,categoryId:e,tagId:e,sort:e,actionType:{UPDATE\_STATE:"timeline-list\\u002FUPDATE\_STATE",FETCH\_MORE:"timeline-list\\u002FFETCH\_MORE",FETCH:"timeline-list\\u002FFETCH",RESET:"timeline-list\\u002FRESET"}},recommendList:{list:\[\],cursor:f,loading:a,skeleton:d,hasMore:d,actionType:{UPDATE\_STATE:"recommend-list\\u002FUPDATE\_STATE",FETCH\_MORE:"recommend-list\\u002FFETCH\_MORE",FETCH:"recommend-list\\u002FFETCH",RESET:"recommend-list\\u002FRESET"}},followingList:{list:\[\],cursor:f,skeleton:d,loading:a,hasMore:d,actionType:{UPDATE\_STATE:"following-list\\u002FUPDATE\_STATE",FETCH\_MORE:"following-list\\u002FFETCH\_MORE",FETCH:"following-list\\u002FFETCH",RESET:"following-list\\u002FRESET"}}},subscribe:{subscribed:{list:\[\],cursor:f,skeleton:d,loading:a,hasMore:a,actionType:{UPDATE\_STATE:"view\\u002Fsubscribe\\u002Fsubscribed\\u002Flist\\u002FUPDATE\_STATE",FETCH\_MORE:"view\\u002Fsubscribe\\u002Fsubscribed\\u002Flist\\u002FFETCH\_MORE",FETCH:"view\\u002Fsubscribe\\u002Fsubscribed\\u002Flist\\u002FFETCH",RESET:"view\\u002Fsubscribe\\u002Fsubscribed\\u002Flist\\u002FRESET"}},all:{list:\[\],cursor:f,loading:a,skeleton:d,hasMore:a,linkList:e,actionType:{UPDATE\_STATE:"view\\u002Fsubscribe\\u002Fall\\u002Flist\\u002FUPDATE\_STATE",FETCH\_MORE:"view\\u002Fsubscribe\\u002Fall\\u002Flist\\u002FFETCH\_MORE",FETCH:"view\\u002Fsubscribe\\u002Fall\\u002Flist\\u002FFETCH",RESET:"view\\u002Fsubscribe\\u002Fall\\u002Flist\\u002FRESET"}}},entryPublic:{entry:{user:{}},relatedEntryList:\[\],relatedCollectionList:\[\],actionType:{FETCH:"@\\u002Fview\\u002FentryPublic\\u002FFETCH",RESET:"@\\u002Fview\\u002FentryPublic\\u002FRESET"}},user:{user:{},serverRendered:a,userAnnuals:\[\],actionType:{FETCH:"@\\u002Fview\\u002Fuser\\u002FFETCH",RESET:"@\\u002Fview\\u002Fuser\\u002FRESET",UPDATE:"@\\u002Fview\\u002Fuser\\u002FUPDATE",FETCH\_ANNUALS:"@\\u002Fview\\u002Fuser\\u002FFETCH\_ANNUALS"},detailList:{actionType:{RESET:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FRESET"},likeList:{list:\[\],cursor:f,hasMore:a,loading:a,skeleton:a,actionType:{FETCH:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FlikePostList\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FlikePostList\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FlikePostList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FlikePostList\\u002FRESET"}},postList:{list:\[\],hasMore:a,skeleton:a,loading:a,sort:o,actionType:{FETCH:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FpostList\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FpostList\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FpostList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FpostList\\u002FRESET"}},searchList:{list:\[\],hasMore:a,skeleton:a,loading:a,key\_word:e,search\_type:b,cursor:f,isPostSearch:a,actionType:{FETCH:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FsearchList\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FsearchList\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FsearchList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FsearchList\\u002FRESET"}},tagList:{list:\[\],loading:a,skeleton:a,hasMore:a,cursor:f,actionType:{FETCH:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FtagList\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FtagList\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FtagList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FtagList\\u002FRESET"}},collectionList:{list:\[\],userId:e,skeleton:a,hasMore:a,cursor:f,type:"created",loading:a,actionType:{FETCH:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcollectionList\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcollectionList\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcollectionList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcollectionList\\u002FRESET",TOGGLE\_FOLLOW\_COLLECTION:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcollectionList\\u002FTOGGLE\_FOLLOW\_COLLECTION",FOLLOW\_COLLECTION:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcollectionList\\u002FFOLLOW\_COLLECTION",UNFOLLOW\_COLLECTION:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcollectionList\\u002FUNFOLLOW\_COLLECTION",DELELTE\_COLLECTION:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcollectionList\\u002FDELELTE\_COLLECTION",ADD\_COLLECTION:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcollectionList\\u002FADD\_COLLECTION",EDIT\_COLLECTION:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcollectionList\\u002FEDIT\_COLLECTION"}},followerList:{list:\[\],cursor:f,hasMore:a,loading:a,skeleton:a,actionType:{FETCH:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FfollowerList\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FfollowerList\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FfollowerList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FfollowerList\\u002FRESET"}},followingList:{list:\[\],cursor:f,hasMore:a,skeleton:a,loading:a,actionType:{FETCH:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FfollowingList\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FfollowingList\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FfollowingList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FfollowingList\\u002FRESET"}},followingTeamsList:{list:\[\],cursor:f,hasMore:a,skeleton:a,loading:a,actionType:{FETCH:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FfollowingTeamsList\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FfollowingTeamsList\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FfollowingTeamsList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FfollowingTeamsList\\u002FRESET"}},activityList:{list:\[\],cursor:f,hasMore:a,loading:a,skeleton:a,actionType:{FETCH:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FactivityList\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FactivityList\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FactivityList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FactivityList\\u002FRESET"}},bookList:{list:\[\],cursor:f,skeleton:a,hasMore:a,loading:a,type:"wrote",actionType:{FETCH:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FbookList\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FbookList\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FbookList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FbookList\\u002FRESET"}},pinList:{list:\[\],hasMore:a,loading:a,skeleton:a,actionType:{FETCH:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FpinList\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FpinList\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FpinList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FpinList\\u002FRESET"}},courseList:{list:\[\],hasMore:a,loading:a,skeleton:a,actionType:{FETCH:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcourseList\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcourseList\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcourseList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcourseList\\u002FRESET"}},pinPraisedList:{list:\[\],cursor:f,hasMore:a,loading:a,skeleton:a,actionType:{FETCH:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FpinPraisedList\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FpinPraisedList\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FpinPraisedList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FpinPraisedList\\u002FRESET"}},eventList:{list:\[\],cursor:f,hasMore:a,loading:a,skeleton:a,actionType:{FETCH:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FeventList\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FeventList\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FeventList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FeventList\\u002FRESET"}},selfColumnList:{list:\[\],hasMore:a,skeleton:a,loading:a,cursor:f,actionType:{FETCH:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcolumnList\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcolumnList\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcolumnList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcolumnList\\u002FRESET"}},columnFollowedList:{list:\[\],hasMore:a,skeleton:a,loading:a,cursor:f,actionType:{FETCH:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcolumnFollowedList\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcolumnFollowedList\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcolumnFollowedList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcolumnFollowedList\\u002FRESET",FILTER:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002FcolumnFollowedList\\u002FFILTER"}},realtimes:{list:\[\],cursor:f,hasMore:a,loading:a,skeleton:a,actionType:{FETCH:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002Frealtimes\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002Frealtimes\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002Frealtimes\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002Frealtimes\\u002FRESET",DELETE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002Frealtimes\\u002FDELETE"}},realtimeliked:{list:\[\],cursor:f,hasMore:a,loading:a,skeleton:a,actionType:{FETCH:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002Frealtimeliked\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002Frealtimeliked\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002Frealtimeliked\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002Frealtimeliked\\u002FRESET",DELETE:"@\\u002Fview\\u002Fuser\\u002FdetailList\\u002Frealtimeliked\\u002FDELETE"}}}},tag:{tag:{},actionType:{FETCH:"@\\u002Fview\\u002Ftag\\u002FFETCH",FETCH\_LIST:"@\\u002Fview\\u002Ftag\\u002FFETCH\_LIST",RESET:"@\\u002Fview\\u002Ftag\\u002FRESET"},list:{list:\[\],cursor:f,loading:a,skeleton:a,hasMore:a,actionType:{UPDATE\_STATE:"@\\u002Fview\\u002Ftag\\u002Flist\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Ftag\\u002Flist\\u002FFETCH\_MORE",FETCH:"@\\u002Fview\\u002Ftag\\u002Flist\\u002FFETCH",RESET:"@\\u002Fview\\u002Ftag\\u002Flist\\u002FRESET"}}},notification:{user:{actionType:{RESET:"@\\u002Fview\\u002Fnotification\\u002Fuser\\u002FRESET"},listState:{list:\[\],cursor:f,hasMore:a,isLoading:a,messageType:3,msgTotal:b,msgSubMap:{"1":b,"2":b,"3":b,"4":b,"7":b}},list:{pageSize:h,page:g,total:b,pointer:c,lastPointer:c,list:\[\],loading:a,error:c,canPrev:d,canNext:d,linkList:\[\],lastFetchOnServer:a,actionType:{UPDATE:"@\\u002Fview\\u002Fnotification\\u002Fuser\\u002Flist\\u002FUPDATE",FETCH:"@\\u002Fview\\u002Fnotification\\u002Fuser\\u002Flist\\u002FFETCH",FORCE\_FETCH:"@\\u002Fview\\u002Fnotification\\u002Fuser\\u002Flist\\u002FFORCE\_FETCH",FETCH\_MORE:"@\\u002Fview\\u002Fnotification\\u002Fuser\\u002Flist\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fnotification\\u002Fuser\\u002Flist\\u002FRESET"}}},system:{actionType:{RESET:"@\\u002Fview\\u002Fnotification\\u002Fsystem\\u002FRESET"},list:{pageSize:h,page:g,total:b,pointer:c,lastPointer:c,list:\[\],loading:a,error:c,canPrev:d,canNext:d,linkList:\[\],lastFetchOnServer:a,actionType:{UPDATE:"@\\u002Fview\\u002Fnotification\\u002Fsystem\\u002Flist\\u002FUPDATE",FETCH:"@\\u002Fview\\u002Fnotification\\u002Fsystem\\u002Flist\\u002FFETCH",FORCE\_FETCH:"@\\u002Fview\\u002Fnotification\\u002Fsystem\\u002Flist\\u002FFORCE\_FETCH",FETCH\_MORE:"@\\u002Fview\\u002Fnotification\\u002Fsystem\\u002Flist\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fnotification\\u002Fsystem\\u002Flist\\u002FRESET"}}}},column:{serverRenderList:a,column:{id:k},entry:{id:k,screenshot:l,liked:a,article\_id:k,article\_info:{article\_id:k,user\_id:u,category\_id:"6809637776263217160",tag\_ids:\[6809640448827589000,6809640940144329000,6809640427465998000\],visible\_level:b,link\_url:e,cover\_image:e,is\_gfw:b,title:v,brief\_content:w,is\_english:b,is\_original:g,user\_index:5.861884384271107,original\_type:b,original\_author:e,content:e,ctime:"1699930374",mtime:x,rtime:x,draft\_id:y,view\_count:m,collect\_count:b,digg\_count:b,comment\_count:b,hot\_index:b,is\_hot:b,rank\_index:b,status:m,verify\_status:g,audit\_status:m,mark\_content:e,display\_count:b,is\_markdown:g,app\_html\_content:e,version:g,web\_html\_content:"\\u003Cstyle\\u003E.markdown-body{word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#252933}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px}.markdown-body h1{font-size:24px;line-height:38px;margin-bottom:5px}.markdown-body h2{font-size:22px;line-height:34px;padding-bottom:12px;border-bottom:1px solid #ececec}.markdown-body h3{font-size:20px;line-height:28px}.markdown-body h4{font-size:18px;line-height:26px}.markdown-body h5{font-size:17px;line-height:24px}.markdown-body h6{font-size:16px;line-height:24px}.markdown-body p{line-height:inherit;margin-top:22px;margin-bottom:22px}.markdown-body img{max-width:100%}.markdown-body hr{border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px}.markdown-body code{word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em}.markdown-body code,.markdown-body pre{font-family:Menlo,Monaco,Consolas,Courier New,monospace}.markdown-body pre{overflow:auto;position:relative;line-height:1.75}.markdown-body pre\\u003Ecode{font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8}.markdown-body a{text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff}.markdown-body a:active,.markdown-body a:hover{color:#275b8c}.markdown-body table{display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6}.markdown-body thead{background:#f6f6f6;color:#000;text-align:left}.markdown-body tr:nth-child(2n){background-color:#fcfcfc}.markdown-body td,.markdown-body th{padding:12px 7px;line-height:24px}.markdown-body td{min-width:120px}.markdown-body blockquote{color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8}.markdown-body blockquote:after{display:block;content:\\"\\"}.markdown-body blockquote\\u003Ep{margin:10px 0}.markdown-body ol,.markdown-body ul{padding-left:28px}.markdown-body ol li,.markdown-body ul li{margin-bottom:0;list-style:inherit}.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item{list-style:none}.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul{margin-top:0}.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul{margin-top:3px}.markdown-body ol li{padding-left:6px}.markdown-body .contains-task-list{padding-left:0}.markdown-body .task-list-item{list-style:none}@media (max-width:720px){.markdown-body h1{font-size:24px}.markdown-body h2{font-size:20px}.markdown-body h3{font-size:18px}}\\u003C\\u002Fstyle\\u003E\\u003Cstyle data-highlight data-highlight-key=\\"juejin\\"\\u003E.markdown-body pre,.markdown-body pre\\u003Ecode.hljs{color:#333;background:#f8f8f8}.hljs-comment,.hljs-quote{color:#998;font-style:italic}.hljs-keyword,.hljs-selector-tag,.hljs-subst{color:#333;font-weight:700}.hljs-literal,.hljs-number,.hljs-tag .hljs-attr,.hljs-template-variable,.hljs-variable{color:teal}.hljs-doctag,.hljs-string{color:#d14}.hljs-section,.hljs-selector-id,.hljs-title{color:#900;font-weight:700}.hljs-subst{font-weight:400}.hljs-class .hljs-title,.hljs-type{color:#458;font-weight:700}.hljs-attribute,.hljs-name,.hljs-tag{color:navy;font-weight:400}.hljs-link,.hljs-regexp{color:#009926}.hljs-bullet,.hljs-symbol{color:#990073}.hljs-built\_in,.hljs-builtin-name{color:#0086b3}.hljs-meta{color:#999;font-weight:700}.hljs-deletion{background:#fdd}.hljs-addition{background:#dfd}.hljs-emphasis{font-style:italic}.hljs-strong{font-weight:700}\\u003C\\u002Fstyle\\u003E\\u003Ch1 data-id=\\"heading-0\\"\\u003E1 自动化测试中隐藏的元素如何操作?\\u003C\\u002Fh1\\u003E\\n\\u003Cblockquote\\u003E\\n\\u003Cp\\u003E面试中，我们经常会遇到“隐藏元素是如何操作的？”带着这个问题我们看下如何操作？\\u003C\\u002Fp\\u003E\\n\\u003C\\u002Fblockquote\\u003E\\n\\u003Ch2 data-id=\\"heading-1\\"\\u003E1.1 实现方法\\u003C\\u002Fh2\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E针对隐藏因素的操作，常用的操作是通过\\u003Ccode\\u003EJS\\u003C\\u002Fcode\\u003E脚本定位到该元素，获取对应的元素对象，再通过\\u003Ccode\\u003EremoveAttribute\\u003C\\u002Fcode\\u003E和\\u003Ccode\\u003EsetAttribute\\u003C\\u002Fcode\\u003E两个方法完成属性的删除或重新复制操作，使得当前元素处于显示状态即可。\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\u003Ch2 data-id=\\"heading-2\\"\\u003E1.2 实现案例\\u003C\\u002Fh2\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E以下是自定义的一个HTML页面，该页面是一个登陆页面，其中用户名和登陆按钮都是隐藏的，如下：\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\u003Cpre\\u003E\\u003Ccode class=\\"hljs language-python\\" lang=\\"python\\"\\u003E&#x3C;html\\u003E\\n&#x3C;body\\u003E\\n\\t用户名:&#x3C;\\u003Cspan class=\\"hljs-built\_in\\"\\u003Einput\\u003C\\u002Fspan\\u003E \\u003Cspan class=\\"hljs-built\_in\\"\\u003Eid\\u003C\\u002Fspan\\u003E=\\u003Cspan class=\\"hljs-string\\"\\u003E\\"user\_name\\"\\u003C\\u002Fspan\\u003E name=\\u003Cspan class=\\"hljs-string\\"\\u003E\\"username\\"\\u003C\\u002Fspan\\u003E \\u003Cspan class=\\"hljs-built\_in\\"\\u003Etype\\u003C\\u002Fspan\\u003E=\\u003Cspan class=\\"hljs-string\\"\\u003E\\"hidden\\"\\u003C\\u002Fspan\\u003E \\u002F\\u003E&#x3C;br\\u003E\\n\\t密码:&#x3C;\\u003Cspan class=\\"hljs-built\_in\\"\\u003Einput\\u003C\\u002Fspan\\u003E \\u003Cspan class=\\"hljs-built\_in\\"\\u003Eid\\u003C\\u002Fspan\\u003E=\\u003Cspan class=\\"hljs-string\\"\\u003E\\"pass\_word\\"\\u003C\\u002Fspan\\u003E name=\\u003Cspan class=\\"hljs-string\\"\\u003E\\"password\\"\\u003C\\u002Fspan\\u003E \\u003Cspan class=\\"hljs-built\_in\\"\\u003Etype\\u003C\\u002Fspan\\u003E=\\u003Cspan class=\\"hljs-string\\"\\u003E\\"text\\"\\u003C\\u002Fspan\\u003E \\u002F\\u003E&#x3C;br\\u003E\\n\\t&#x3C;button \\u003Cspan class=\\"hljs-built\_in\\"\\u003Etype\\u003C\\u002Fspan\\u003E=\\u003Cspan class=\\"hljs-string\\"\\u003E\\"button\\"\\u003C\\u002Fspan\\u003E name=\\u003Cspan class=\\"hljs-string\\"\\u003E\\"login\\"\\u003C\\u002Fspan\\u003E \\u003Cspan class=\\"hljs-keyword\\"\\u003Eclass\\u003C\\u002Fspan\\u003E=\\u003Cspan class=\\"hljs-string\\"\\u003E\\"login\_but\\"\\u003C\\u002Fspan\\u003E style=\\u003Cspan class=\\"hljs-string\\"\\u003E\\"display:none;\\"\\u003C\\u002Fspan\\u003E \\u002F\\u003E\\n&#x3C;\\u002Fbody\\u003E\\n&#x3C;\\u002Fhtml\\u003E\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\n\\u003Ch2 data-id=\\"heading-3\\"\\u003E1.3 实现思路\\u003C\\u002Fh2\\u003E\\n\\u003Cpre\\u003E\\u003Ccode class=\\"hljs language-python\\" lang=\\"python\\"\\u003E\\u003Cspan class=\\"hljs-comment\\"\\u003E#主要是使用JS脚本改变标签的属性值\\u003C\\u002Fspan\\u003E\\nhi\_name = \\u003Cspan class=\\"hljs-string\\"\\u003E\\"document.getElementByID('user\_name').setAttribute('type', 'text')\\"\\u003C\\u002Fspan\\u003E\\n\\u003Cspan class=\\"hljs-built\_in\\"\\u003Eprint\\u003C\\u002Fspan\\u003E(driver.execute\_script(hi\_name ))\\n\\ndriver.find\_element\_by\_id(\\u003Cspan class=\\"hljs-string\\"\\u003E'user\_name'\\u003C\\u002Fspan\\u003E).send\_keys(\\u003Cspan class=\\"hljs-string\\"\\u003E\\"admin\\"\\u003C\\u002Fspan\\u003E)\\n\\u003Cspan class=\\"hljs-built\_in\\"\\u003Eprint\\u003C\\u002Fspan\\u003E(driver.find\_element\_by\_name(\\u003Cspan class=\\"hljs-string\\"\\u003E\\"login\\"\\u003C\\u002Fspan\\u003E))\\n\\ndriver.execute\_script(\\u003Cspan class=\\"hljs-string\\"\\u003E\\"document.getElementsClassName('login\_but')\[0\].removeAttribute('style')\\"\\u003C\\u002Fspan\\u003E)\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\n\\u003Ch1 data-id=\\"heading-4\\"\\u003E2 三种元素等待方式如何理解？\\u003C\\u002Fh1\\u003E\\n\\u003Cblockquote\\u003E\\n\\u003Cp\\u003E在自动化测试中，会遇到一些比如环境不稳定、网络不稳定的因素，此时可能需要控制脚本执行速度，那么就需要用到元素等待操作。其实不一定设置等待就好，各有利弊，以下是一些观点仅供参考。\\u003C\\u002Fp\\u003E\\n\\u003C\\u002Fblockquote\\u003E\\n\\u003Ch2 data-id=\\"heading-5\\"\\u003E2.1 强制等待\\u003C\\u002Fh2\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E方法：\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\u003Cpre\\u003E\\u003Ccode class=\\"hljs language-python\\" lang=\\"python\\"\\u003Etime.sleep(s)\\n\\u003Cspan class=\\"hljs-comment\\"\\u003E# s表示具体时间，单位为秒。\\u003C\\u002Fspan\\u003E\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E含义：表示等待\\u003Ccode\\u003Es\\u003C\\u002Fcode\\u003E秒后，进行下一步操作。直接使用\\u003Ccode\\u003Epython\\u003C\\u002Fcode\\u003E内置的\\u003Ccode\\u003Etime\\u003C\\u002Fcode\\u003E模块调用\\u003Ccode\\u003Esleep\\u003C\\u002Fcode\\u003E方法即可。\\u003C\\u002Fli\\u003E\\n\\u003Cli\\u003E说明：强制等待又称强制休眠。作用域为当前脚本。没过多行代码需要进行等待设置，那每行代码都需要进行相同的设置操作。\\u003C\\u002Fli\\u003E\\n\\u003Cli\\u003E优缺点：\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\u003Ctable\\u003E\\u003Cthead\\u003E\\u003Ctr\\u003E\\u003Cth\\u003E优缺点\\u003C\\u002Fth\\u003E\\u003Cth\\u003E说明\\u003C\\u002Fth\\u003E\\u003C\\u002Ftr\\u003E\\u003C\\u002Fthead\\u003E\\u003Ctbody\\u003E\\u003Ctr\\u003E\\u003Ctd\\u003E优点\\u003C\\u002Ftd\\u003E\\u003Ctd\\u003E使用简单，需要用时随时调用即可\\u003C\\u002Ftd\\u003E\\u003C\\u002Ftr\\u003E\\u003Ctr\\u003E\\u003Ctd\\u003E缺点\\u003C\\u002Ftd\\u003E\\u003Ctd\\u003E代码重复率高，且影响代码执行速率。不能精确设置等待时间，过长过段貌似都不合适\\u003C\\u002Ftd\\u003E\\u003C\\u002Ftr\\u003E\\u003C\\u002Ftbody\\u003E\\u003C\\u002Ftable\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E示例：\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\u003Cpre\\u003E\\u003Ccode class=\\"hljs language-python\\" lang=\\"python\\"\\u003E\\u003Cspan class=\\"hljs-keyword\\"\\u003Efrom\\u003C\\u002Fspan\\u003E selenium \\u003Cspan class=\\"hljs-keyword\\"\\u003Eimport\\u003C\\u002Fspan\\u003E webdriver\\n\\u003Cspan class=\\"hljs-keyword\\"\\u003Eimport\\u003C\\u002Fspan\\u003E time\\n\\ndriver = webdriver.Chrome()\\ndriver.get(\\u003Cspan class=\\"hljs-string\\"\\u003E\\"http:\\u002F\\u002Flocalhost\\u002Fzentao\\u002Fuser-login.html\\"\\u003C\\u002Fspan\\u003E)\\n\\nuser\_name = \\u003Cspan class=\\"hljs-string\\"\\u003E\\"$('input:first').val('admin')\\"\\u003C\\u002Fspan\\u003E\\ndriver.execute\_script(user\_name)\\ntime.sleep(\\u003Cspan class=\\"hljs-number\\"\\u003E0.5\\u003C\\u002Fspan\\u003E)\\n\\npass\_wd = \\u003Cspan class=\\"hljs-string\\"\\u003E\\"$(':password').val('ZenTao123456')\\"\\u003C\\u002Fspan\\u003E\\ndriver.execute\_script(pass\_wd)\\ntime.sleep(\\u003Cspan class=\\"hljs-number\\"\\u003E1\\u003C\\u002Fspan\\u003E)\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\n\\u003Ch2 data-id=\\"heading-6\\"\\u003E2.2 隐式等待\\u003C\\u002Fh2\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E方法：\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\u003Cpre\\u003E\\u003Ccode class=\\"hljs language-python\\" lang=\\"python\\"\\u003Edriver.implicitly\_wait(s)\\n\\u003Cspan class=\\"hljs-comment\\"\\u003E# s表示具体时间，单位为秒。\\u003C\\u002Fspan\\u003E\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E含义：在\\u003Ccode\\u003Es\\u003C\\u002Fcode\\u003E时间内，页面加载完成，进行下一步操作，直接通过浏览器驱动对象进行调用。\\u003C\\u002Fli\\u003E\\n\\u003Cli\\u003E说明：隐式等待也称智能等待，也称全局等待。表示整个页面中的所有元素加载完才会执行，会根据内部设置的频率不断刷新页面继续加载并检测当前所执行的元素是否加载完成。\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\u003Cblockquote\\u003E\\n\\u003Cp\\u003E如果在设定的时间之前元素加载完成，则不会继续等待，继续执行下一步。\\u003C\\u002Fp\\u003E\\n\\u003C\\u002Fblockquote\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E优缺点：\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\u003Ctable\\u003E\\u003Cthead\\u003E\\u003Ctr\\u003E\\u003Cth\\u003E优缺点\\u003C\\u002Fth\\u003E\\u003Cth\\u003E说明\\u003C\\u002Fth\\u003E\\u003C\\u002Ftr\\u003E\\u003C\\u002Fthead\\u003E\\u003Ctbody\\u003E\\u003Ctr\\u003E\\u003Ctd\\u003E优点\\u003C\\u002Ftd\\u003E\\u003Ctd\\u003E对整个脚本的生命周期都起作用，只需要设置一次\\u003C\\u002Ftd\\u003E\\u003C\\u002Ftr\\u003E\\u003Ctr\\u003E\\u003Ctd\\u003E缺点\\u003C\\u002Ftd\\u003E\\u003Ctd\\u003E程序会一直等待加载完成，才会执行下一步，但有时想要的元素加载完了，其他的元素没有加载完，仍要等待全部加载完才进行下一步，不是很灵活，也有点费时间。\\u003C\\u002Ftd\\u003E\\u003C\\u002Ftr\\u003E\\u003C\\u002Ftbody\\u003E\\u003C\\u002Ftable\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E示例：\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\u003Cpre\\u003E\\u003Ccode class=\\"hljs language-python\\" lang=\\"python\\"\\u003E\\u003Cspan class=\\"hljs-keyword\\"\\u003Efrom\\u003C\\u002Fspan\\u003E selenium \\u003Cspan class=\\"hljs-keyword\\"\\u003Eimport\\u003C\\u002Fspan\\u003E webdriver\\n\\ndriver = webdriver.Chrome()\\ndriver.get(\\u003Cspan class=\\"hljs-string\\"\\u003E\\"http:\\u002F\\u002Flocalhost\\u002Fzentao\\u002Fuser-login.html\\"\\u003C\\u002Fspan\\u003E)\\ndriver.implicitly\_wait(\\u003Cspan class=\\"hljs-number\\"\\u003E10\\u003C\\u002Fspan\\u003E)\\n\\nuser\_name = \\u003Cspan class=\\"hljs-string\\"\\u003E\\"$('input:first').val('admin')\\"\\u003C\\u002Fspan\\u003E\\ndriver.execute\_script(user\_name)\\n\\npass\_wd = \\u003Cspan class=\\"hljs-string\\"\\u003E\\"$(':password').val('ZenTao123456')\\"\\u003C\\u002Fspan\\u003E\\ndriver.execute\_script(pass\_wd)\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\n\\u003Ch2 data-id=\\"heading-7\\"\\u003E2.3 显式等待\\u003C\\u002Fh2\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E方法：\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\u003Cpre\\u003E\\u003Ccode class=\\"hljs language-python\\" lang=\\"python\\"\\u003E\\u003Cspan class=\\"hljs-comment\\"\\u003E# 导入包\\u003C\\u002Fspan\\u003E\\n\\u003Cspan class=\\"hljs-keyword\\"\\u003Efrom\\u003C\\u002Fspan\\u003E selenium.webdriver.support.wait \\u003Cspan class=\\"hljs-keyword\\"\\u003Eimport\\u003C\\u002Fspan\\u003E \\n\\u003Cspan class=\\"hljs-comment\\"\\u003E# 或者\\u003C\\u002Fspan\\u003E\\n\\u003Cspan class=\\"hljs-keyword\\"\\u003Efrom\\u003C\\u002Fspan\\u003E selenium.webdriver.support.ui \\u003Cspan class=\\"hljs-keyword\\"\\u003Eimport\\u003C\\u002Fspan\\u003E WebDriverWait\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E部分源码如下：\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\u003Cpre\\u003E\\u003Ccode class=\\"hljs language-python\\" lang=\\"python\\"\\u003Elass WebDriverWait(\\u003Cspan class=\\"hljs-built\_in\\"\\u003Eobject\\u003C\\u002Fspan\\u003E):\\n \\u003Cspan class=\\"hljs-keyword\\"\\u003Edef\\u003C\\u002Fspan\\u003E \\u003Cspan class=\\"hljs-title function\_\\"\\u003E\_\_init\_\_\\u003C\\u002Fspan\\u003E(\\u003Cspan class=\\"hljs-params\\"\\u003Eself, driver, timeout, poll\_frequency=POLL\_FREQUENCY, ignored\_exceptions=\\u003Cspan class=\\"hljs-literal\\"\\u003ENone\\u003C\\u002Fspan\\u003E\\u003C\\u002Fspan\\u003E):\\n \\u003Cspan class=\\"hljs-string\\"\\u003E\\"\\"\\"Constructor, takes a WebDriver instance and timeout in seconds.\\n\\n :Args:\\n - driver - Instance of WebDriver (Ie, Firefox, Chrome or Remote)\\n - timeout - Number of seconds before timing out\\n - poll\_frequency - sleep interval between calls\\n By default, it is 0.5 second.\\n - ignored\_exceptions - iterable structure of exception classes ignored during calls.\\n By default, it contains NoSuchElementException only.\\n\\n Example:\\n from selenium.webdriver.support.ui import WebDriverWait \\\\n\\n\\u003C\\u002Fspan\\u003E\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E参数说明：\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\u003Ctable\\u003E\\u003Cthead\\u003E\\u003Ctr\\u003E\\u003Cth\\u003E参数\\u003C\\u002Fth\\u003E\\u003Cth\\u003E说明\\u003C\\u002Fth\\u003E\\u003C\\u002Ftr\\u003E\\u003C\\u002Fthead\\u003E\\u003Ctbody\\u003E\\u003Ctr\\u003E\\u003Ctd\\u003E\\u003Ccode\\u003Edriver\\u003C\\u002Fcode\\u003E\\u003C\\u002Ftd\\u003E\\u003Ctd\\u003E驱动器对象\\u003C\\u002Ftd\\u003E\\u003C\\u002Ftr\\u003E\\u003Ctr\\u003E\\u003Ctd\\u003E\\u003Ccode\\u003Etimeout\\u003C\\u002Fcode\\u003E\\u003C\\u002Ftd\\u003E\\u003Ctd\\u003E设置刷新页面的超时时间\\u003C\\u002Ftd\\u003E\\u003C\\u002Ftr\\u003E\\u003Ctr\\u003E\\u003Ctd\\u003E\\u003Ccode\\u003Epoll\_frequency\\u003C\\u002Fcode\\u003E\\u003C\\u002Ftd\\u003E\\u003Ctd\\u003E页面刷新频率。默认\\u003Ccode\\u003E0.5s\\u003C\\u002Fcode\\u003E\\u003C\\u002Ftd\\u003E\\u003C\\u002Ftr\\u003E\\u003Ctr\\u003E\\u003Ctd\\u003E\\u003Ccode\\u003Eignored\_exceptions\\u003C\\u002Fcode\\u003E\\u003C\\u002Ftd\\u003E\\u003Ctd\\u003E表示忽略异常，如无法找到元素则抛出\\u003Ccode\\u003ENoSuchElementException\\u003C\\u002Fcode\\u003E异常\\u003C\\u002Ftd\\u003E\\u003C\\u002Ftr\\u003E\\u003C\\u002Ftbody\\u003E\\u003C\\u002Ftable\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E\\u003Ccode\\u003EWebDriverWait\\u003C\\u002Fcode\\u003E模块有两个方法\\u003Ccode\\u003Euntil\\u003C\\u002Fcode\\u003E和\\u003Ccode\\u003Euntil\_not\\u003C\\u002Fcode\\u003E：\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\u003Cpre\\u003E\\u003Ccode class=\\"hljs language-python\\" lang=\\"python\\"\\u003E \\u003Cspan class=\\"hljs-keyword\\"\\u003Edef\\u003C\\u002Fspan\\u003E \\u003Cspan class=\\"hljs-title function\_\\"\\u003Euntil\\u003C\\u002Fspan\\u003E(\\u003Cspan class=\\"hljs-params\\"\\u003Eself, method, message=\\u003Cspan class=\\"hljs-string\\"\\u003E''\\u003C\\u002Fspan\\u003E\\u003C\\u002Fspan\\u003E):\\n \\u003Cspan class=\\"hljs-string\\"\\u003E\\"\\"\\"Calls the method provided with the driver as an argument until the \\\\\\n return value is not False.\\"\\"\\"\\u003C\\u002Fspan\\u003E\\n screen = \\u003Cspan class=\\"hljs-literal\\"\\u003ENone\\u003C\\u002Fspan\\u003E\\n stacktrace = \\u003Cspan class=\\"hljs-literal\\"\\u003ENone\\u003C\\u002Fspan\\u003E\\n\\n end\_time = time.time() + self.\_timeout\\n \\u003Cspan class=\\"hljs-keyword\\"\\u003Ewhile\\u003C\\u002Fspan\\u003E \\u003Cspan class=\\"hljs-literal\\"\\u003ETrue\\u003C\\u002Fspan\\u003E:\\n \\u003Cspan class=\\"hljs-keyword\\"\\u003Etry\\u003C\\u002Fspan\\u003E:\\n value = method(self.\_driver)\\n \\u003Cspan class=\\"hljs-keyword\\"\\u003Eif\\u003C\\u002Fspan\\u003E value:\\n \\u003Cspan class=\\"hljs-keyword\\"\\u003Ereturn\\u003C\\u002Fspan\\u003E value\\n \\u003Cspan class=\\"hljs-keyword\\"\\u003Eexcept\\u003C\\u002Fspan\\u003E self.\_ignored\_exceptions \\u003Cspan class=\\"hljs-keyword\\"\\u003Eas\\u003C\\u002Fspan\\u003E exc:\\n screen = \\u003Cspan class=\\"hljs-built\_in\\"\\u003Egetattr\\u003C\\u002Fspan\\u003E(exc, \\u003Cspan class=\\"hljs-string\\"\\u003E'screen'\\u003C\\u002Fspan\\u003E, \\u003Cspan class=\\"hljs-literal\\"\\u003ENone\\u003C\\u002Fspan\\u003E)\\n stacktrace = \\u003Cspan class=\\"hljs-built\_in\\"\\u003Egetattr\\u003C\\u002Fspan\\u003E(exc, \\u003Cspan class=\\"hljs-string\\"\\u003E'stacktrace'\\u003C\\u002Fspan\\u003E, \\u003Cspan class=\\"hljs-literal\\"\\u003ENone\\u003C\\u002Fspan\\u003E)\\n time.sleep(self.\_poll)\\n \\u003Cspan class=\\"hljs-keyword\\"\\u003Eif\\u003C\\u002Fspan\\u003E time.time() \\u003E end\_time:\\n \\u003Cspan class=\\"hljs-keyword\\"\\u003Ebreak\\u003C\\u002Fspan\\u003E\\n \\u003Cspan class=\\"hljs-keyword\\"\\u003Eraise\\u003C\\u002Fspan\\u003E TimeoutException(message, screen, stacktrace)\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\n\\u003Cpre\\u003E\\u003Ccode class=\\"hljs language-python\\" lang=\\"python\\"\\u003E \\u003Cspan class=\\"hljs-keyword\\"\\u003Edef\\u003C\\u002Fspan\\u003E \\u003Cspan class=\\"hljs-title function\_\\"\\u003Euntil\_not\\u003C\\u002Fspan\\u003E(\\u003Cspan class=\\"hljs-params\\"\\u003Eself, method, message=\\u003Cspan class=\\"hljs-string\\"\\u003E''\\u003C\\u002Fspan\\u003E\\u003C\\u002Fspan\\u003E):\\n \\u003Cspan class=\\"hljs-string\\"\\u003E\\"\\"\\"Calls the method provided with the driver as an argument until the \\\\\\n return value is False.\\"\\"\\"\\u003C\\u002Fspan\\u003E\\n end\_time = time.time() + self.\_timeout\\n \\u003Cspan class=\\"hljs-keyword\\"\\u003Ewhile\\u003C\\u002Fspan\\u003E \\u003Cspan class=\\"hljs-literal\\"\\u003ETrue\\u003C\\u002Fspan\\u003E:\\n \\u003Cspan class=\\"hljs-keyword\\"\\u003Etry\\u003C\\u002Fspan\\u003E:\\n value = method(self.\_driver)\\n \\u003Cspan class=\\"hljs-keyword\\"\\u003Eif\\u003C\\u002Fspan\\u003E \\u003Cspan class=\\"hljs-keyword\\"\\u003Enot\\u003C\\u002Fspan\\u003E value:\\n \\u003Cspan class=\\"hljs-keyword\\"\\u003Ereturn\\u003C\\u002Fspan\\u003E value\\n \\u003Cspan class=\\"hljs-keyword\\"\\u003Eexcept\\u003C\\u002Fspan\\u003E self.\_ignored\_exceptions:\\n \\u003Cspan class=\\"hljs-keyword\\"\\u003Ereturn\\u003C\\u002Fspan\\u003E \\u003Cspan class=\\"hljs-literal\\"\\u003ETrue\\u003C\\u002Fspan\\u003E\\n time.sleep(self.\_poll)\\n \\u003Cspan class=\\"hljs-keyword\\"\\u003Eif\\u003C\\u002Fspan\\u003E time.time() \\u003E end\_time:\\n \\u003Cspan class=\\"hljs-keyword\\"\\u003Ebreak\\u003C\\u002Fspan\\u003E\\n \\u003Cspan class=\\"hljs-keyword\\"\\u003Eraise\\u003C\\u002Fspan\\u003E TimeoutException(message)\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\n\\u003Cblockquote\\u003E\\n\\u003Cp\\u003E其中：\\u003C\\u002Fp\\u003E\\n\\u003Cp\\u003E1、method：传入对象分两种，一种是匿名函数；另一种是预置条件对象expected\_conditions。\\u003C\\u002Fp\\u003E\\n\\u003Cp\\u003E2、message：当出现异常时，把异常信息给message；\\u003C\\u002Fp\\u003E\\n\\u003Cp\\u003E3、expected\_conditions方法通过from selenium.webdriver.support import expected\_conditions引入。\\u003C\\u002Fp\\u003E\\n\\u003C\\u002Fblockquote\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E含义：对单个元素设置一定的频率，使其按频率刷新当前页面并检测是都存在该元素。\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\u003Cp\\u003E\\u003Ccode\\u003EWebDriverWait\\u003C\\u002Fcode\\u003E常用的几个方法如下：\\u003C\\u002Fp\\u003E\\n\\u003Ch3 data-id=\\"heading-8\\"\\u003E2.3.1 判断元素是否被加入DOM树中，不可见\\u003C\\u002Fh3\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E判断元素是否被加入\\u003Ccode\\u003EDOM\\u003C\\u002Fcode\\u003E树中，并不代表元素可见，如果定位到就返回元素；\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\u003Cpre\\u003E\\u003Ccode class=\\"hljs language-python\\" lang=\\"python\\"\\u003Eget\_ele = WebDriverWait(driver,\\u003Cspan class=\\"hljs-number\\"\\u003E10\\u003C\\u002Fspan\\u003E).until(expected\_conditions.\\\\\\npresence\_of\_element\_located(By.ID, \\u003Cspan class=\\"hljs-string\\"\\u003E\\"xxx\\"\\u003C\\u002Fspan\\u003E))\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\n\\u003Ch3 data-id=\\"heading-9\\"\\u003E2.3.2 判断元素是否被加入到DOM中，并可见\\u003C\\u002Fh3\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E判断元素是否被加入到\\u003Ccode\\u003EDOM\\u003C\\u002Fcode\\u003E中，并可见，代表元素可显示，宽和高都大于0；\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\u003Cpre\\u003E\\u003Ccode class=\\"hljs language-python\\" lang=\\"python\\"\\u003Eget\_ele1 = WebDriverWait(driver,\\u003Cspan class=\\"hljs-number\\"\\u003E10\\u003C\\u002Fspan\\u003E).until(expected\_conditions.visibility\_of\_elemen\\\\\\nt\_located((by=By.ID,value=\\u003Cspan class=\\"hljs-string\\"\\u003E'yyy'\\u003C\\u002Fspan\\u003E)))\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\n\\u003Ch3 data-id=\\"heading-10\\"\\u003E2.3.3 判断元素是否可见\\u003C\\u002Fh3\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E判断元素是否可见，可见返回该元素；\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\u003Cpre\\u003E\\u003Ccode class=\\"hljs language-python\\" lang=\\"python\\"\\u003Eget\_ele2 = WebDriverWait(driver,\\u003Cspan class=\\"hljs-number\\"\\u003E10\\u003C\\u002Fspan\\u003E).until(expected\_conditions.visibility\_of(driver\\\\\\n.find\_element(by=By.ID,value=\\u003Cspan class=\\"hljs-string\\"\\u003E'zzz'\\u003C\\u002Fspan\\u003E)))\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\n\\u003Ch3 data-id=\\"heading-11\\"\\u003E2.3.4 判断是否至少有1个元素存在DOM树中\\u003C\\u002Fh3\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E判断是否至少有1个元素存在\\u003Ccode\\u003EDOM\\u003C\\u002Fcode\\u003E树中，如果定位到就返回列表：\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\u003Cpre\\u003E\\u003Ccode class=\\"hljs language-python\\" lang=\\"python\\"\\u003Eget\_ele3 = WebDriverWait(driver,\\u003Cspan class=\\"hljs-number\\"\\u003E10\\u003C\\u002Fspan\\u003E).until(expected\_conditions.presence\_of\_all\_elem\\\\\\nents\_located(By.CSS\_SELECTOR,\\u003Cspan class=\\"hljs-string\\"\\u003E'.boss'\\u003C\\u002Fspan\\u003E)))\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\n\\u003Ch3 data-id=\\"heading-12\\"\\u003E2.3.5 判断指定的元素的属性值中是否包含了预期的字符串\\u003C\\u002Fh3\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E判断指定的元素的属性值中是否包含了预期的字符串，返回布尔值；\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\u003Cpre\\u003E\\u003Ccode class=\\"hljs language-python\\" lang=\\"python\\"\\u003Eget\_ele4 = WebDriverWait(driver,\\u003Cspan class=\\"hljs-number\\"\\u003E10\\u003C\\u002Fspan\\u003E).until(expected\_conditions.text\_to\_be\_present\_i\\\\\\nn\_element\_value(By.CSS\_SELECTOR,\\u003Cspan class=\\"hljs-string\\"\\u003E'#su'\\u003C\\u002Fspan\\u003E))\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\n\\u003Ch3 data-id=\\"heading-13\\"\\u003E2.3.6 判断指定的元素中是否包含了预期的字符串\\u003C\\u002Fh3\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E判断指定的元素中是否包含了预期的字符串，返回布尔值；\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\u003Cpre\\u003E\\u003Ccode class=\\"hljs language-python\\" lang=\\"python\\"\\u003Eget\_ele5= WebDriverWait(driver,\\u003Cspan class=\\"hljs-number\\"\\u003E10\\u003C\\u002Fspan\\u003E).until(expected\_conditions.text\_to\_be\_present\_i\\\\\\nn\_element(By.XPATH,\\u003Cspan class=\\"hljs-string\\"\\u003E\\"\\u002F\\u002F#\[@id='ul'\]\\"\\u003C\\u002Fspan\\u003E, \\u003Cspan class=\\"hljs-string\\"\\u003Eu'添加'\\u003C\\u002Fspan\\u003E))\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\n\\u003Ch3 data-id=\\"heading-14\\"\\u003E2.3.7 判断元素是否存在DOM中或不可见\\u003C\\u002Fh3\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E判断元素是否存在\\u003Ccode\\u003EDOM\\u003C\\u002Fcode\\u003E中或不可见，如果可见，返回\\u003Ccode\\u003EFalse\\u003C\\u002Fcode\\u003E，否则返回这个元素；\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\u003Cpre\\u003E\\u003Ccode class=\\"hljs language-python\\" lang=\\"python\\"\\u003Eget\_ele6= WebDriverWait(driver,\\u003Cspan class=\\"hljs-number\\"\\u003E10\\u003C\\u002Fspan\\u003E).until(expected\_conditions.invisibility\_of\_elem\\\\\\nent\_located(By.CSS\_SELECTOR,\\u003Cspan class=\\"hljs-string\\"\\u003E'#su'\\u003C\\u002Fspan\\u003E))\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\n\\u003Ch3 data-id=\\"heading-15\\"\\u003E2.3.8 判断元素是否可见且状态为enable\\u003C\\u002Fh3\\u003E\\n\\u003Cul\\u003E\\n\\u003Cli\\u003E判断元素是否可见且状态为\\u003Ccode\\u003Eenable\\u003C\\u002Fcode\\u003E(代表可点击)；\\u003C\\u002Fli\\u003E\\n\\u003C\\u002Ful\\u003E\\n\\u003Cpre\\u003E\\u003Ccode class=\\"hljs language-python\\" lang=\\"python\\"\\u003Eget\_ele7= WebDriverWait(driver,\\u003Cspan class=\\"hljs-number\\"\\u003E10\\u003C\\u002Fspan\\u003E).until(expected\_conditions.element\_to\_be\_clicka\\\\\\nble(By.CSS\_SELECTOR,\\u003Cspan class=\\"hljs-string\\"\\u003E'#su'\\u003C\\u002Fspan\\u003E)).click()\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E",meta\_info:"{\\"plugins\\":\[5\],\\"video\_count\\":0}",catalog:"\[{\\"title\\":\\"1 自动化测试中隐藏的元素如何操作?\\",\\"hash\\":\\"#heading-0\\",\\"deep\\":1,\\"children\\":\[{\\"title\\":\\"1.1 实现方法\\",\\"hash\\":\\"#heading-1\\",\\"deep\\":2,\\"children\\":\[\],\\"visible\\":true},{\\"title\\":\\"1.2 实现案例\\",\\"hash\\":\\"#heading-2\\",\\"deep\\":2,\\"children\\":\[\],\\"visible\\":true},{\\"title\\":\\"1.3 实现思路\\",\\"hash\\":\\"#heading-3\\",\\"deep\\":2,\\"children\\":\[\],\\"visible\\":true}\],\\"visible\\":true},{\\"title\\":\\"2 三种元素等待方式如何理解？\\",\\"hash\\":\\"#heading-4\\",\\"deep\\":1,\\"children\\":\[{\\"title\\":\\"2.1 强制等待\\",\\"hash\\":\\"#heading-5\\",\\"deep\\":2,\\"children\\":\[\],\\"visible\\":true},{\\"title\\":\\"2.2 隐式等待\\",\\"hash\\":\\"#heading-6\\",\\"deep\\":2,\\"children\\":\[\],\\"visible\\":true},{\\"title\\":\\"2.3 显式等待\\",\\"hash\\":\\"#heading-7\\",\\"deep\\":2,\\"children\\":\[{\\"title\\":\\"2.3.1 判断元素是否被加入DOM树中，不可见\\",\\"hash\\":\\"#heading-8\\",\\"deep\\":3,\\"children\\":\[\],\\"visible\\":true},{\\"title\\":\\"2.3.2 判断元素是否被加入到DOM中，并可见\\",\\"hash\\":\\"#heading-9\\",\\"deep\\":3,\\"children\\":\[\],\\"visible\\":true},{\\"title\\":\\"2.3.3 判断元素是否可见\\",\\"hash\\":\\"#heading-10\\",\\"deep\\":3,\\"children\\":\[\],\\"visible\\":true},{\\"title\\":\\"2.3.4 判断是否至少有1个元素存在DOM树中\\",\\"hash\\":\\"#heading-11\\",\\"deep\\":3,\\"children\\":\[\],\\"visible\\":true},{\\"title\\":\\"2.3.5 判断指定的元素的属性值中是否包含了预期的字符串\\",\\"hash\\":\\"#heading-12\\",\\"deep\\":3,\\"children\\":\[\],\\"visible\\":true},{\\"title\\":\\"2.3.6 判断指定的元素中是否包含了预期的字符串\\",\\"hash\\":\\"#heading-13\\",\\"deep\\":3,\\"children\\":\[\],\\"visible\\":true},{\\"title\\":\\"2.3.7 判断元素是否存在DOM中或不可见\\",\\"hash\\":\\"#heading-14\\",\\"deep\\":3,\\"children\\":\[\],\\"visible\\":true},{\\"title\\":\\"2.3.8 判断元素是否可见且状态为enable\\",\\"hash\\":\\"#heading-15\\",\\"deep\\":3,\\"children\\":\[\],\\"visible\\":true}\],\\"visible\\":true}\],\\"visible\\":true}\]",homepage\_top\_time:p,homepage\_top\_status:b,content\_count:1590,read\_time:"5分钟"},author\_user\_info:{user\_id:u,user\_name:z,company:e,job\_title:"测开丨质量丨管理",avatar\_large:"https:\\u002F\\u002Fp9-passport.byteacctimg.com\\u002Fimg\\u002Fuser-avatar\\u002F43b26e4825c1494fe485f75d30863340~300x300.image",level:A,description:"CSDN测试领域优质创作者 | CSDN博客专家 | 阿里云专家博主 | 华为云享专家 | 51CTO专家博主 |【专注测试领域各种技术研究、分享和交流~】",followee\_count:219,follower\_count:47,post\_article\_count:223,digg\_article\_count:225,got\_digg\_count:256,got\_view\_count:38583,post\_shortmsg\_count:79,digg\_shortmsg\_count:62,isfollowed:a,favorable\_author:b,power:B,study\_point:b,university:{university\_id:f,name:e,logo:e},major:{major\_id:f,parent\_id:f,name:e},student\_status:b,select\_event\_count:b,select\_online\_course\_count:b,identity:b,is\_select\_annual:a,select\_annual\_rank:b,annual\_list\_type:b,extraMap:{},is\_logout:b,annual\_info:\[\],account\_amount:b,user\_growth\_info:{user\_id:3655236621185246,jpower:B,jscore:2167.6,jpower\_level:A,jscore\_level:6,jscore\_title:"杰出掘友",author\_achievement\_list:\[\],vip\_level:b,vip\_title:e,jscore\_next\_level\_score:7000,jscore\_this\_level\_mini\_score:2000,vip\_score:b},is\_vip:a,become\_author\_days:b,collection\_set\_article\_count:b,recommend\_article\_count\_daily:b,article\_collect\_count\_daily:b,user\_priv\_info:{administrator:b,builder:b,favorable\_author:b,book\_author:b,forbidden\_words:b,can\_tag\_cnt:b,auto\_recommend:b,signed\_author:b,popular\_author:b,can\_add\_video:b}},category:{category\_id:"6809637776263217160",category\_name:"代码人生",category\_url:"career",rank:7,back\_ground:e,icon:e,ctime:1553759544,mtime:1553759548,show\_type:3,item\_type:m,promote\_tag\_cap:A,promote\_priority:7,id:"6809637776263217160",name:"代码人生",title:"代码人生",alias:"career"},tags:\[{entriesCount:l,subscribed:a,id:"6809640448827588622",tag\_id:"6809640448827588622",tag\_name:"Python",color:"#356E9C",icon:"https:\\u002F\\u002Fp1-jj.byteimg.com\\u002Ftos-cn-i-t2oaga2asx\\u002Fleancloud-assets\\u002Fb51a1dacf9bb7883defe.png~tplv-t2oaga2asx-image.image",back\_ground:e,show\_navi:b,ctime:1436156327,mtime:1699930374,id\_type:9,tag\_alias:e,post\_article\_count:47271,concern\_user\_count:260295,title:"Python",tagId:"6809640448827588622",articleCount:47271,subscribersCount:260295,createdAt:c,updatedAt:c},{entriesCount:l,subscribed:a,id:"6809640940144328718",tag\_id:"6809640940144328718",tag\_name:"Selenium",color:"#000000",icon:"https:\\u002F\\u002Fp1-jj.byteimg.com\\u002Ftos-cn-i-t2oaga2asx\\u002Fleancloud-assets\\u002Fb2afab7ae051dc79fb57.png~tplv-t2oaga2asx-image.image",back\_ground:e,show\_navi:b,ctime:1489370953,mtime:1699930374,id\_type:9,tag\_alias:e,post\_article\_count:502,concern\_user\_count:2739,title:"Selenium",tagId:"6809640940144328718",articleCount:502,subscribersCount:2739,createdAt:c,updatedAt:c},{entriesCount:l,subscribed:a,id:"6809640427465998350",tag\_id:"6809640427465998350",tag\_name:"测试",color:"#D5C072",icon:"https:\\u002F\\u002Fp1-jj.byteimg.com\\u002Ftos-cn-i-t2oaga2asx\\u002Fleancloud-assets\\u002F38c00424af15fa29e3c8.jpg~tplv-t2oaga2asx-image.image",back\_ground:e,show\_navi:b,ctime:1435974765,mtime:1699930374,id\_type:9,tag\_alias:e,post\_article\_count:16326,concern\_user\_count:52310,title:"测试",tagId:"6809640427465998350",articleCount:16326,subscribersCount:52310,createdAt:c,updatedAt:c}\],user\_interact:{id:7300845951865602000,omitempty:m,user\_id:b,is\_digg:a,is\_follow:a,is\_collect:a,collect\_set\_count:b},org:{org\_info:c,is\_followed:a},req\_id:"021699930380286fdbddc010025003800000000000001083fd8cd",status:{push\_status:b},theme\_list:\[{theme:{theme\_id:"7218019389664067621",name:"金石计划征文活动",cover:"https:\\u002F\\u002Fp6-juejin.byteimg.com\\u002Ftos-cn-i-k3u1fbpfcp\\u002Fa46ae3a6e10144d39242aa19e8414290~tplv-k3u1fbpfcp-no-mark:0:0:0:0.image?",brief:"金石计划是针对掘金社区创作者等级 lv4-lv8 的优质原创作者发起的奖金瓜分活动，根据要求完成挑战，即可瓜分现金奖池，心动不如行动，从这里开启通往技术大牛之路的第一步吧！具体规则请查看活动详情：https:\\u002F\\u002Fjuejin.cn\\u002Fpost\\u002F7238403651021783077 （活动结束时创作等级lv4以下不可以瓜分奖池）",is\_lottery:a,is\_rec:a,rec\_rank:b,topic\_ids:\["6824710203087257613"\],hot:6658692,view\_cnt:16277,user\_cnt:13285,status:b,ctime:p,mtime:1686555499,lottery\_begin\_time:p,lottery\_end\_time:p,theme\_type:g,last\_hot:351470}}\],title:v,user:C,viewCount:l,commentsCount:b,isEvent:l,abstract:w,latestCommentAt:c,createdAt:new Date(1699930374000),updatedAt:c,isTopicEvent:a,likedCount:b,likeCount:b,content:e,originalUrl:e,type:"post",collected:a,viewsCount:m,username:z,viewerHasLiked:a,draftId:y,collectionCount:b,isCache:d},entryView:{},author:C,adEntryList:\[\],relatedEntryList:\[\],selectedList:\[\],linkVotingList:\[{keyword:e,url:e,type:e},{keyword:e,url:e,type:e},{keyword:e,url:e,type:e},{keyword:e,url:e,type:e},{keyword:"extjs 右下角消息框",url:"https:\\u002F\\u002Ffrontend.devrank.cn\\u002Ftraffic-aggregation\\u002F123994",type:D},{keyword:"图片滚动js代码",url:"https:\\u002F\\u002Ffrontend.devrank.cn\\u002Ftraffic-aggregation\\u002F210759",type:D},{keyword:"python引号内不分隔",url:"https:\\u002F\\u002Fbackend.devrank.cn\\u002Ftraffic-aggregation\\u002F999001",type:"后端"},{keyword:"洪荒魔猿道小说",url:"https:\\u002F\\u002Ffanqienovel.com\\u002Fkeyword\\u002F3286711",type:e},{keyword:"308宿舍闹鬼",url:"https:\\u002F\\u002Ffanqienovel.com\\u002Fkeyword\\u002F3038393",type:e},{keyword:"快穿之黑化吧前女友讲的什么",url:"https:\\u002F\\u002Ffanqienovel.com\\u002Fkeyword\\u002F3196604",type:e}\],userAnnuals:\[\],columnList:\[\],hitArticleCache:d,authorCard:{},relatedLoaded:a,dynamicDataReady:a,followAuthorPopupTime:b,followAuthorPopupType:b,authorBlockVisible:b,compVisible:{},version:g,actionType:{FETCH:"view\\u002Fcolumn\\u002FFETCH",FETCH\_RELATED:"view\\u002Fcolumn\\u002FFETCH\_RELATED",FETCH\_RECOMMEND:"view\\u002Fcolumn\\u002FFETCH\_RECOMMEND",FETCH\_SELECTED:"view\\u002Fcolumn\\u002FFETCH\_SELECTED",FETCH\_ADDITIONAL:"view\\u002Fcolumn\\u002FFETCH\_ADDITIONAL",FETCH\_SIDEBAR\_ADENTRY:"view\\u002Fcolumn\\u002FFETCH\_SIDEBAR\_ADENTRY",FETCH\_AUTHOR\_EXTRA:"view\\u002Fcolumn\\u002FFETCH\_AUTHOR\_EXTRA",MD\_FALLBACK\_RENDER:"view\\u002Fcolumn\\u002FMD\_FALLBACK\_RENDER",RESET:"view\\u002Fcolumn\\u002FRESET"},recommendedArticleList:{list:\[\],cursor:f,loading:a,skeleton:d,hasMore:a,articleId:e,actionType:{UPDATE\_STATE:"view\\u002Fcolumn\\u002Frecommend-List\\u002FUPDATE\_STATE",FETCH\_MORE:"view\\u002Fcolumn\\u002Frecommend-List\\u002FFETCH\_MORE",FETCH:"view\\u002Fcolumn\\u002Frecommend-List\\u002FFETCH",RESET:"view\\u002Fcolumn\\u002Frecommend-List\\u002FRESET"}}},collection:{collection:{author:{}},actionType:{FETCH:"@\\u002Fview\\u002Fcollection\\u002FFETCH",REFRESH:"@\\u002Fview\\u002Fcollection\\u002FREFRESH",RESET:"@\\u002Fview\\u002Fcollection\\u002FRESET"},list:{pageSize:h,page:g,total:b,pointer:c,lastPointer:c,list:\[\],loading:a,error:c,canPrev:d,canNext:d,linkList:\[\],lastFetchOnServer:a,actionType:{UPDATE:"@\\u002Fview\\u002Fcollection\\u002Flist\\u002FUPDATE",FETCH:"@\\u002Fview\\u002Fcollection\\u002Flist\\u002FFETCH",FORCE\_FETCH:"@\\u002Fview\\u002Fcollection\\u002Flist\\u002FFORCE\_FETCH",FETCH\_MORE:"@\\u002Fview\\u002Fcollection\\u002Flist\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fcollection\\u002Flist\\u002FRESET"},id:e,sort:o}},gettingStarted:{category:{},actionType:{UPDATE\_STATE:"@\\u002Fview\\u002FgettingStarted\\u002FUPDATE\_STATE",FOLLOW:"@\\u002Fview\\u002FgettingStarted\\u002FFOLLOW",RESET:"@\\u002Fview\\u002FgettingStarted\\u002FRESET",UPDATE\_CATEGORY:"@\\u002Fview\\u002FgettingStarted\\u002FUPDATE\_CATEGORY"}},pin:{pin:{user:{},imageUrlList:\[\]},pinList:\[\],actionType:{FETCH:"@\\u002Fview\\u002Fpin\\u002FFETCH",RESET:"@\\u002Fview\\u002Fpin\\u002FRESET"},sidebar:{list:\[\],after:e,loading:a,isRecommend:a,hasNextPage:d,actionType:{UPDATE\_STATE:"@\\u002Fview\\u002Fpin\\u002Fsidebar\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fpin\\u002Fsidebar\\u002FFETCH\_MORE",FETCH:"@\\u002Fview\\u002Fpin\\u002Fsidebar\\u002FFETCH",RESET:"@\\u002Fview\\u002Fpin\\u002Fsidebar\\u002FRESET"}},commentList:{pageSize:h,page:g,total:b,pointer:c,lastPointer:c,list:\[\],loading:a,error:c,canPrev:d,canNext:d,linkList:\[\],lastFetchOnServer:a,actionType:{UPDATE:"@\\u002Fview\\u002Fpin\\u002FcommentList\\u002FUPDATE",FETCH:"@\\u002Fview\\u002Fpin\\u002FcommentList\\u002FFETCH",FORCE\_FETCH:"@\\u002Fview\\u002Fpin\\u002FcommentList\\u002FFORCE\_FETCH",FETCH\_MORE:"@\\u002Fview\\u002Fpin\\u002FcommentList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fpin\\u002FcommentList\\u002FRESET"},pinId:c},subCommentList:{pageSize:h,page:g,total:b,pointer:c,lastPointer:c,list:\[\],loading:a,error:c,canPrev:d,canNext:d,linkList:\[\],lastFetchOnServer:a,actionType:{UPDATE:"@\\u002Fview\\u002Fpin\\u002FsubCommentList\\u002FUPDATE",FETCH:"@\\u002Fview\\u002Fpin\\u002FsubCommentList\\u002FFETCH",FORCE\_FETCH:"@\\u002Fview\\u002Fpin\\u002FsubCommentList\\u002FFORCE\_FETCH",FETCH\_MORE:"@\\u002Fview\\u002Fpin\\u002FsubCommentList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fpin\\u002FsubCommentList\\u002FRESET"},commentId:c}},topic:{topic:e,followedTopicList:\[\],actionType:{FETCH:"@\\u002Fview\\u002Ftopic\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Ftopic\\u002FUPDATE\_STATE",RESET:"@\\u002Fview\\u002Ftopic\\u002FRESET"},allTopicList:{pageSize:E,page:b,total:b,pointer:c,lastPointer:c,list:\[\],loading:a,error:c,canPrev:d,canNext:d,linkList:\[\],lastFetchOnServer:a,actionType:{UPDATE:"@\\u002Fview\\u002Ftopic\\u002FallTopicList\\u002FUPDATE",FETCH:"@\\u002Fview\\u002Ftopic\\u002FallTopicList\\u002FFETCH",FORCE\_FETCH:"@\\u002Fview\\u002Ftopic\\u002FallTopicList\\u002FFORCE\_FETCH",FETCH\_MORE:"@\\u002Fview\\u002Ftopic\\u002FallTopicList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Ftopic\\u002FallTopicList\\u002FRESET"},sortType:n},pinlist:{pageSize:h,page:g,total:b,pointer:c,lastPointer:c,list:\[\],loading:a,error:c,canPrev:d,canNext:d,linkList:\[\],lastFetchOnServer:a,actionType:{UPDATE:"@\\u002Fview\\u002Ftopic\\u002FpinList\\u002FUPDATE",FETCH:"@\\u002Fview\\u002Ftopic\\u002FpinList\\u002FFETCH",FORCE\_FETCH:"@\\u002Fview\\u002Ftopic\\u002FpinList\\u002FFORCE\_FETCH",FETCH\_MORE:"@\\u002Fview\\u002Ftopic\\u002FpinList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Ftopic\\u002FpinList\\u002FRESET"},sortType:r},sidebar:{actionType:{RESET:"@\\u002Fview\\u002Ftopic\\u002Fsidebar\\u002FRESET",UPDATE\_STATE:"@\\u002Fview\\u002Ftopic\\u002Fsidebar\\u002FUPDATE\_STATE"},attender:{pageSize:h,page:g,total:b,pointer:c,lastPointer:c,list:\[\],loading:a,error:c,canPrev:d,canNext:d,linkList:\[\],lastFetchOnServer:a,actionType:{UPDATE:"@\\u002Fview\\u002Ftopic\\u002Fsidebar\\u002Fattender\\u002FUPDATE",FETCH:"@\\u002Fview\\u002Ftopic\\u002Fsidebar\\u002Fattender\\u002FFETCH",FORCE\_FETCH:"@\\u002Fview\\u002Ftopic\\u002Fsidebar\\u002Fattender\\u002FFORCE\_FETCH",FETCH\_MORE:"@\\u002Fview\\u002Ftopic\\u002Fsidebar\\u002Fattender\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Ftopic\\u002Fsidebar\\u002Fattender\\u002FRESET"},topicId:c}},followedList:{pageSize:E,page:b,total:b,pointer:c,lastPointer:c,list:\[\],loading:a,error:c,canPrev:d,canNext:d,linkList:\[\],lastFetchOnServer:a,actionType:{UPDATE:"@\\u002Fview\\u002Ftopic\\u002FfollowedList\\u002FUPDATE",FETCH:"@\\u002Fview\\u002Ftopic\\u002FfollowedList\\u002FFETCH",FORCE\_FETCH:"@\\u002Fview\\u002Ftopic\\u002FfollowedList\\u002FFORCE\_FETCH",FETCH\_MORE:"@\\u002Fview\\u002Ftopic\\u002FfollowedList\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Ftopic\\u002FfollowedList\\u002FRESET"},after:b}},recommendationIndex:{actionType:{FETCH\_USER:"@\\u002Fview\\u002Frecommendation\\u002FFETCH\_USER",FETCH\_MORE:"@\\u002Fview\\u002Frecommendation\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Frecommendation\\u002FRESET",FETCH:"@\\u002Fview\\u002Frecommendation\\u002FFETCH"},cursor:e,hasMore:e,userList:\[\],loading:a,skeleton:d,category:j,categoryNavList:\[\],serverRenderUserList:a},event:{event:{},loading:a,user:{},actionType:{FETCH:"view\\u002Fevent\\u002FFETCH",RESET:"view\\u002Fevent\\u002FRESET"}},coursesIndex:{loading:a,list:\[\],sort:"online",actionType:{FETCH:"view\\u002Fcourses\\u002FFETCH",RESET:"view\\u002Fcourses\\u002FRESET",FETCH\_MORE:"view\\u002Fcourses\\u002FFETCH\_MORE"}},team:{team:{},loading:d,actionType:{FETCH:"@\\u002Fview\\u002Fteam\\u002FFETCH",RESET:"@\\u002Fview\\u002Fteam\\u002FRESET",UPDATE:"@\\u002Fview\\u002Fteam\\u002FUPDATE",FOLLOW:"@\\u002Fview\\u002Fteam\\u002FFOLLOW"},detailList:{actionType:{RESET:"@\\u002Fview\\u002Fteam\\u002FdetailList\\u002FRESET"},posts:{list:\[\],hasMore:a,skeleton:a,loading:a,sort:o,actionType:{FETCH:"@\\u002Fview\\u002Fteam\\u002FdetailList\\u002Fposts\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fteam\\u002FdetailList\\u002Fposts\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fteam\\u002FdetailList\\u002Fposts\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fteam\\u002FdetailList\\u002Fposts\\u002FRESET"}},pins:{list:\[\],hasMore:a,loading:a,skeleton:d,actionType:{FETCH:"@\\u002Fview\\u002Fteam\\u002FdetailList\\u002Fpins\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fteam\\u002FdetailList\\u002Fpins\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fteam\\u002FdetailList\\u002Fpins\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fteam\\u002FdetailList\\u002Fpins\\u002FRESET"}},hire:{list:\[\],hasMore:a,cursor:f,loading:a,skeleton:d,actionType:{FETCH:"@\\u002Fview\\u002Fteam\\u002FdetailList\\u002Fhire\\u002FFETCH",UPDATE\_STATE:"@\\u002Fview\\u002Fteam\\u002FdetailList\\u002Fhire\\u002FUPDATE\_STATE",FETCH\_MORE:"@\\u002Fview\\u002Fteam\\u002FdetailList\\u002Fhire\\u002FFETCH\_MORE",RESET:"@\\u002Fview\\u002Fteam\\u002FdetailList\\u002Fhire\\u002FRESET"}}}},couponList:{list:{"0":s,"1":s,"2":s},showTooltip:a},payment:{selectedDiscount:{},bookletDetail:{},coupons:{availables:\[\],unavailables:\[\]},discountList:\[\]},activityVip:{selectedVipSku:{}}},component:{indexAside:{bannerList:\[\],userList:\[\],actionType:{FETCH\_BANNER:"@\\u002Fcomponent\\u002Faside\\u002FFETCH\_BANNER",FETCH\_USER:"@\\u002Fcomponent\\u002Faside\\u002FFETCH\_USER",CLOSE\_BANNER:"@\\u002Fcomponent\\u002Faside\\u002FCLOSE\_BANNER"}}},dislike:{whiteList:\["1398234521548542",F,G,H,I,J,K\],officialList:\[F,G,"3984285868490807",H,"3562073405009031",I,"4433674252325966","53218623894222","2110693287406632","2498524693925623","430664288836334",J,K,"2832783991648407","3386151545092589"\]},ore:{oreCount:b},avatarMenuInfo:{user\_basic:{},user\_counter:{},user\_growth\_info:{}},common:{theme:"light",isFollowSystem:a},env:{ua:"Mozilla\\u002F5.0 (Linux; Android 6.0.1; Nexus 5X Build\\u002FMMB29P) AppleWebKit\\u002F537.36 (KHTML, like Gecko) Chrome\\u002F119.0.6045.123 Mobile Safari\\u002F537.36 (compatible; Googlebot\\u002F2.1; +http:\\u002F\\u002Fwww.google.com\\u002Fbot.html)",serverEnv:"production",logId:"2023112412302279DF2488A8328B72A532"},auth:{user:c,clientId:c,token:c,qrCode:c,qrCodeStatus:c,qrCodeToken:c,userInitiated:a,loginTeaParams:l},tag:{subscribedTagList:\[\]},entry:{isLikeLoading:a},collection:{},comment:{},bookComment:{},repoComment:{},category:{list:\[\]},user:{subscribedTagList:\[\]},notification:{unreadCount:{user:b,system:b,total:b}},error:{location:c,errorView:c,statusCode:200,needRiskModal:a,riskAppealUrl:e},abTest:{info:{}},suspensionPanel:{needSuspension:d},pinComment:{},pin:{deleteDialogVisible:a,reportDialogVisible:a,targetPin:c,isOnFocus:a},topic:{visible:a},activity:{"2020":{},offer:{is\_show:b,start\_time:b},voteData:l},header:{leadStep:b,isPopupZlink:a},tcc:{tccConfig:c},route:{name:L,path:t,hash:e,query:{},params:{id:k},fullPath:t,meta:{isAvailableDarkMode:d},from:{name:c,path:M,hash:e,query:{},params:{},fullPath:M,meta:{}}}},serverRendered:d,routePath:t,config:{API\_HOST:"api.juejin.cn",CAPTCHA\_HOST:"verify.snssdk.com",PLATFORM\_APPID:{wechat:1277,weibo:1276,github:1045,wechatApp:1070},SCM\_VERSION:"1.0.0.125",REGISTERED\_ROUTES:\[L,"selfPost","noCDNPost","SeoSearch"\],http:{}},globalRefs:{}}}(false,0,null,true,"","0",1,20,"topic","recommended","7300845951865602063",void 0,2,"hot","newest",-62135596800,"following","popular",{},"\\u002Fpost\\u002F7300845951865602063","3655236621185246","WebUI自动化测试中隐藏的元素如何操作？三种元素等待方式如何理解？","1 自动化测试中隐藏的元素如何操作? 1.1 实现方法 针对隐藏因素的操作，常用的操作是通过JS脚本定位到该元素，获取对应的元素对象，再通过removeAttribute和setAttribute两个","1699930376","7300843140758880290","虫无涯",4,2391,{},"前端",100,"1556564194374926","940837680722589","2780007432717400","1204720443866983","852876722177533","3227821828225517","column","\\u002F"));