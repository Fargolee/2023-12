# 一篇文章带你了解Python常用自动化测试框架——Pytest

在之前的文章里我们已经学习了Python自带测试框架UnitTest，但是UnitTest具有一定的局限性

这篇文章里我们来学习第三方框架Pytest，它在保留了UnitTest框架语法的基础上有着更多的优化处理

下面我们将从以下角度来介绍Pytest：

-   Pytest基本介绍
-   Pytest基本使用
-   Pytest进阶内容

## Pytest基本介绍

下面我们首先来简单介绍Pytest及相关内容

### 单元测试框架

我们首先需要知道测试一般分为四个方面的测试：

-   单元测试：称模块测试，针对软件设计中的最小单位——程序模块，进行正确性检查的测试工作
-   集成测试：称组装测试，通常在单元测试的基础上，将所有程序模块进行有序的、递增测试，重点测试不同模块的接口部分
-   系统测试：将整个软件系统看成一个整体进行测试，包括对功能、性能以及软件所运行的软硬件环境进行测试
-   验收测试：指按照项目任务书或合同、供需双方约定的验收依据文档进行的对整个系统的测试与评审，决定是否接收或拒收系统

而我们这篇文章主要针对的是单元测试：

-   Python：通常使用UnitTest和Pytest来进行单元测试自动化，但Pytest已经成为主流
-   Java：通常使用Testng和Junit来进行单元测试自动化，但Testng已经成为主流

最后我们需要明白单元测试框架的主要功能：

-   发现测试用例
    
-   执行测试用例
    
-   判断测试结果
    
-   生成测试报告
    

### 框架基本介绍

下面我们来简单介绍Pytest框架：

-   pytest是一个非常成熟的单元测试框架，经过多版本的迭代，主要优点在于灵活和简单
    
-   pytest具有极强的兼容性和生态环境，它可以结合selenium，requests，appium完成各种不同的自动化
    
-   pytest具有更好的页面展示效果，它可以生成自定义allure报告以及和Jenkins持续集成
    

下面我们给出一些和Pytest框架可以很好聚合的框架类型：

-   pytestpytest-html：主要用来生成html报告的插件
-   pytest-xdist：主要用来进行多线程运行的插件
-   pytest-ordering：主要用来改变用例的执行顺序的插件
-   pytest-rerunfailres：主要用来失败用例重跑的插件
-   allure-pytest：主要用来生成美观自定义的allure报告

我们可以采用一种比较简便的方式来一次性下载这些框架：

```python
# 首先我们需要将这些名称全部放入一个txt文件中，假设我们放在requestment.txt文件中

# requestment.txt文件
pytest-html
pytest-xdist
pytest-ordering
pytest-rerunfailures

# 我们只需要在pycharm的console中输入指令下载该文件夹中全部内容即可
pip install -r requirements.txt

```

## Pytest基本使用

下面我们来介绍Pytest的基本使用

### Pytest默认测试用例

下面我们首先讲解Pytest默认测试用例的格式：

```python
# 首先我们的模块名（文件名）通常被统一存放在一个testcases文件夹中，然后需要保证模块名须以test_开头或者_test结尾
# 例如我们下面的模块名命名就是正确示例
test_demo1
demo2_test

# 然后我们需要注意我们模块中的测试类类名必须以Test开头，并且不能带有init方法
# 例如我们下面的类名命名就是正确示例
class TestDemo1:
class TestLogin:

# 最后我们需要注意我们测试类中的测试方法名（Case名）必须以test_开头
# 例如我们下面的模块名命名就是正确示例
test_demo1(self)
test_demo2(self)

# 我们给出一个测试用例例子：
# 文件名为test_demo1
class TestDemo:
    def test_demo1(self):
        print("测试用例1")

    def test_demo2(self):
        print("测试用例2")
        
# 当然我们上述的要求都不是必须相同的，在后续我们可以进行修改，我们将在下述讲解执行方法时讲解

```

然后我们再来讲解一下Pytest的测试用例该如何执行：

```python
# 首先我们讲解一下全局配置文件pytest.ini
# 我们可以在pytest.ini中进行一些属性的配置来修改Pytest的默认属性，我们需要在项目的根目录下创建，名称必须是pytest.ini

1 [pytest]
2 #参数
3 addopts = ‐vs 				# 这里指当默认使用指令时的一些辅助参数，我们后面会讲解
4 testpaths = ./testcases		# 这里指默认的执行路径，它会默认执行该文件夹下所有的满足条件的测试case
5 python_files = test_*.py		# 这里就是前面我们所说的文件命名规则
6 python_classes = Test*		# 这里就是前面我们所说的类名命名规则
7 python_functions = test_*		# 这里就是前面我们所说的Case命名规则
8 #标记
9 markers =						# 这里是冒烟规则，我们后面会讲到
10 smoke:冒烟用例				 
11 product_manage:商品管理		


# 然后我们首先来讲采用console命令行执行Pytest的方法
# 最简单的就是直接在console命令行输入pytest，如果存在pytest.ini，它会根据文件内容进行执行；如果没有就按照默认格式执行
# 但是我们可以通过一些参数来强化pytest参数指令

# -vs： -v输出详细信息 -s输出调试信息
pytest -vs

# -n： 多线程运行（前提安装插件：pytest-xdist）
pytest -vs -n=2

# --reruns num: 失败重跑（前提安装插件：pytest-rerunfailres）
pytest -vs --reruns=2

# -x: 出现一个用例失败则停止测试
pytest -vs -x

# --maxfail: 出现几个失败才终止
pytest -vs --maxfail=2

# --html: 生成html的测试报告,后面 需要跟上所创建的文件位置及文件名称（前提安装插件：pytest-html）
pytest -vs --html ./reports/result.html

# -k： 运行测试用例名称中包含某个字符串的测试用例，我们可以采用or表示或者，采用and表示都
# 采用or就表示：我们的运行用例名称中包含or两侧的其中一个数据即可
# 采用and就表示：我们的运行用例名称中包含and两侧的所有数据才满足条件
pytest -vs -k "qiuluo"
pytest -vs -k "qiuluo or weiliang"
pytest -vs -k "qiuluo and weiliang"

# -m：冒烟用例执行，后面需要跟一个冒烟名称
# 我们在这里简单介绍一下冒烟用例的执行方法，我们这里其实就是一个分组执行的方法
# 例如我们的用例划分为user_manage用户管理测试和product_manage商品管理测试，我们只希望执行其中一组测试

# 首先我们需要在他们的不同方法上进行@mark划分，具体操作如下：
class TestDemo:
    
    # 我们在Case上采用@pytest.mark. + 分组名称，就相当于该方法被划分为该分组中
    # 注意：一个分组可以有多个方法，一个方法也可以被划分到多个分组中
    @pytest.mark.user_manage
    def test_demo1(self):
        print("user_manage_test1")

    @pytest.mark.product_manage
    def test_demo2(self):
        print("product_manage_test1")
     
    @pytest.mark.user_manage
    @pytest.mark.product_manage
    def test_demo3(self):
        print("manage_test1")

# 我们在执行中只需要采用前面我们所说的-m + 分组名称即可
pytest -vs -m user_manage

# 这里插一句，我们在运行过程中可以采用抛出异常的方式来模拟测试失败：raise Exception() 抛出异常


# 最后我们也可以采用main方法来执行pytest，同样我们也可以使用参数来进行调节
if __name__ == '__main__':
	pytest.main()
    
if __name__ == '__main__':
	pytest.main(["‐vs"])

```

最后我们插入一个简单的案例跳过方法：

```python
# pytest的跳过案例方法其实和unittest是完全相同的
# 我们只需要采用skip或skipif方法来指定参数并贴在方法上即可跳过

# @pytest.mark.skip(跳过原因)

# @pytest.mark.skipif(跳过条件,跳过原因)

# 我们给出一个示例
class TestDemo:
    
    workage2 = 5
    workage3 = 20
    
    @pytest.mark.skip(reason="无理由跳过")
    def test_demo1(self):
        print("我被跳过了")

    @pytest.mark.skipif(workage2<10,reason="工作经验少于10年跳过")    
    def test_demo2(self):
        print("由于经验不足，我被跳过了")
    
    @pytest.mark.skipif(workage3<10,reason="工作经验少于10年跳过")
    def test_demo3(self):
        print("由于经验过关，我被执行了")
        
    def test_demo3(self):
        print("我没有跳过条件，所以我被执行了")

```

### Pytest前后置方法

首先我们需要先了解前后置是什么：

-   前后置就是针对不同层级方法执行前和执行后所需要执行的步骤进行封装并执行
-   这个层级通常被划分为：文件层，类层，方法层

首先我们先来介绍Pytest通过固件来实现前后置的方法：

```python
# 我们通常采用前后置来做一些方法前后的操作
# 如果我们采用方法层的前后置，那么它会在每个方法执行前后去执行该内容
# 如果我们采用类层的前后置，那么它会在调用这个类内所有方法的前后去执行该内容，但是无论该类的方法执行多少次，它只会调用一次
# 例如我们做login测试时，我们只需要在开始测试时打开一次浏览器，然后在测试结束时关闭一次浏览器，那么我们就采用类的前后置
# 我们做login测试时，为了保证前置操作不对后续Case有影响，所以我们在执行方法前打开该网页，执行方法后关闭该网页，采用方法的前后置

# Pytest的固件前后置其实和unittest是基本相同的
# 首先是方法级别的固件前后置
# 它是在每个测试方法(用例代码) 执行前后都会自动调用的结构
# 方法执行之前
	def setUp(self):
		每个测试方法执行之前都会执行
		pass
# 方法执行之后
	def tearDown(self):
		每个测试方法执行之后都会执行
		pass
    
# 然后是针对类级别的固件前后置
# 它是在每个测试类中所有方法执行前后 都会自动调用的结构(在整个类中执行之前或之后执行一次)
# 需要注意：类级别的固件前后置, 是一个类方法
# 类中所有方法之前
    @classmethod
    def setUpClass(cls):
    	pass
# 类中所有方法之后
	@classmethod
	def tearDownClass(cls):
		pass
    
# 最后是针对模块级别的固件前后置
# 在每个代码文件执行前后执行的代码结构
# 需要注意：模块级别的需要写在类的外边直接定义函数即可
# 代码文件之前
	def setUpModule():
		pass
# 代码文件之后
	def tearDownModule():
		pass
    
# 下面我们采用一个用户账户登录的用例来简单展示一下固件前后置

import unittest

class TestLogin(unittest.TestCase):
    
    # 在执行该类前所需要调用的方法
    @classmethod
    def setUpClass(cls) -> None:
    	print('------打开浏览器')
    
    # 在执行该类后所需要调用的方法
    @classmethod
    def tearDownClass(cls) -> None:
    	print('------关闭浏览器')
    
    # 每个测试方法执行之前都会先调用的方法
    def setUp(self):
    	print('输入网址......')
    
    # 每个测试方法执行之后都会调用的方法
    def tearDown(self) -> None:
    	print('关闭当前页面......')
    
    # 测试Case1
    def test_1(self):
    	print('输入正确用户名密码验证码,点击登录 1')
  
	# 测试Case2
    def test_2(self):
    	print('输入错误用户名密码验证码,点击登录 2')


```

然后我们还需要讲解一下Fixtrue实现前后置的方法：

```python
# 首先我们需要知道Fixtrue所实现的功能基本和固件所实现的功能是一样的，但是会更加方便
# 首先我们给出Fixture的完整格式，然后我们再分开介绍各个参数
@pytest.fixture(scope=None,autouse=False,params=None,ids=None ,name=None)

# scope：作用范围
# 参数主要有三种：function函数，class类，package/session包

# function：在函数层面上执行前后置
# 我们通常采用yield进行前后置划分，yield前是前置，yield后是后置
	@pytest.fixture(scope="function")
	def exe_database_sql():
		print("执行SQL查询")
		yield
		print("关闭数据库连接")
# 我们还可以通过yield或return去返回一些参数在方法中使用
# 但是需要注意，yield返回参数后后置仍旧可以执行，但是return返回参数后后置操作无法执行
	@pytest.fixture(scope="function")
	def exe_database_sql():
		print("执行SQL查询")
		yield "success"
      # return "success" 执行后无法执行后置操作
		print("关闭数据库连接")
# 我们的方法在调用时，可以直接使用exe_database_sql表示返回信息进行输出
def test_2(self，exe_database_sql):
    	print(exe_database_sql)
        
# class：在类之前和之后执行
	@pytest.fixture(scope="class")
	def exe_database_sql():
		print("执行SQL查询")
		yield
		print("关闭数据库连接")
        
# package/session：在整个项目会话之前和之后执行
	@pytest.fixture(scope="session")
	def exe_database_sql():
		print("执行SQL查询")
		yield
		print("关闭数据库连接")

        
# autouse:是否自动启动
# 该参数默认为False，我们可以将其修改为True
# 该参数的功能主要在判断该固件是否在自定义范围内可以自动启动
# 若自动启动，则所有方法在执行时都会自动执行该前后置；但若为False，则我们需要手动启动

# 首先如果是自动启动，则我们无需关心任何参数，我们的所有方法都会自动调用
	@pytest.fixture(scope="function"，autoues=True)
	def exe_database_sql():
		print("执行SQL查询")
		yield
		print("关闭数据库连接")
        
# 但若是关闭自动启动，我们在不同的scope下有不同的调用方法
	@pytest.fixture(scope="function"，autoues=Flase)
	def exe_database_sql():
		print("执行SQL查询")
		yield
		print("关闭数据库连接")
        
# scope = function：我们需要在方法后加上该Fixture方法名
	def test_2(self，exe_database_sql):
    	print(exe_database_sql)
        
# scope = class：我们需要在对应的类上添加@pytest.mark.usefixtures("exe_database_sql")装饰器调用
@pytest.mark.usefixtures("exe_database_sql")
class TestDemo:
    pass

# scope = session:.一般会结合conftest.py文件来实现,我们后面再介绍

# 还需要注意autouse仅限于在自己的类中使用上述方法，如果要跨类使用，那么我们也需要在conftest.py中配置


# params:实现参数化配置
# 通常我们的脚本都是根据导出的yaml文件进行属性填充，针对参数化我们后面再讲，我们先将Fixture的参数化
# params通常后面跟上具体的数据(列表，元组等)，然后我们在调用时有固定的写法
# 首先我们需要在Fixture方法参数中定义一个request，然后使用request.param来使用我们传递的params数据
class TestDemo:
    def read_yaml():
        return ["胡桃","胡桃宝宝","胡桃厨"]
    
    # 首先我们的参数需要获取数据：params=read_yaml()
    @pytest.fixture(scope="function",autouse=False,params=read_yaml())
    # 然后我们的Fixture方法需要一个request参数
	def exe_database_sql(request):
        print("执行SQL查询")
        # 我们通过request.param获取数据，可以采用yield返回该数据
        yield request.param
        print("关闭数据库连接")
        

# ids：参数别名id
# 不能单独使用，必须和params一起使用，作用是对参数起别名 
# 我们在采用pytest进行测试数据输出时会有对应的方法调用n次，该n次采用不同的params参数，这个ids就是修改了console控制台展示数据
class TestDemo:
    def read_yaml():
        return ["胡桃","胡桃宝宝","胡桃厨"]
    
    # 当我们书写了ids，我们的控制输出就不会再是上面的["胡桃","胡桃宝宝","胡桃厨"]，而是我们所书写的["1","2","3"]
    @pytest.fixture(scope="function",autouse=False,params=read_yaml()，ids=["1","2","3"])
	def exe_database_sql(request):
        print("执行SQL查询")
        # 我们通过request.param获取数据，可以采用yield返回该数据
        yield request.param
        print("关闭数据库连接")
        
# name：Fixture别名
# 作用是给fixtrue起别名，一旦使用了别名，那么fixtrue的名称就不能再用了，只能用别名
class TestDemo:
    
    # 如果我们在这里使用到了别名
    @pytest.fixture(scope="function",name="exe_datebase_sql_name")
	def exe_database_sql(request):
        print("执行SQL查询")
        yield 
        print("关闭数据库连接")
        
    # 我们这里就需要使用别名进行操作，之前的名称无法使用
	def test_2(self，exe_datebase_sql_name):
    	print(exe_database_sql)    

```

接下来我们就将会讲解到我们刚刚提到的conftest.py文件：

```python
# 首先我们需要知道conftest.py文件的名字是固定形式，不可改变
# conftest.py文件主要就是用来存储我们的Fixture，然后我们会根据该文件的不同位置来判断可以使用的方法
# conftest可以在不同的目录级别下创建，如果我们在根目录下创建，那么所有case都会使用到该Fixture
# 但是如果我们在testcases文件夹下的某个模块文件下创建conftest.py，那么它的作用范围就只包含在该目录下

# 根目录创建的conftest.py
# 我们在该目录下的conftest文件里写的所有fixture可以在任意测试类下执行
import pytest
@pytest.fixture(scope="function",name="exe_datebase_sql_name")
def exe_database_sql():
    print("全部方法运行前均可以执行")
    yield 
    print("全部方法运行后均可以执行")
# testcases文件下的所有测试类
# 这里需要注意：我们使用conftest下的Fixture时，不需要import导包就可以使用
import pytest
class TestDemo1:
	# 测试Case1
    def test_1(self,exe_datebase_sql_name):
    	print('输入正确用户名密码验证码,点击登录 1' + exe_datebase_sql_name)
        
# testcases文件夹下的usercases文件夹下创建的conftest.py
# 我们在该目录下创建的conftest文件里写的所有fixture仅可以在该目录下的测试类中使用，在其他测试类中使用会出现报错
import pytest
@pytest.fixture(scope="function",name="usercases_fixture")
def exe_database_sql():
    print("usercases方法运行前均可以执行")
    yield 
    print("usercases方法运行后均可以执行")
# testcases文件下的usercases文件夹下的测试类
import pytest
class TestUserCases1:
	# 测试Case1
    def test_1(self,usercases_fixture):
    	print('输入正确用户名密码验证码,点击登录 1' + usercases_fixture)
        
# 最后我们简单给出一个前后置执行顺序优先级：
fixture_session > fixture_class > setup_class > fixture_function > setup

```

然后最后我们给出前后置执行的一个总体逻辑顺序：

-   查询当前目录下的conftest.py文件
    
-   查询当前目录下的pytest.ini文件并找到测试用例的位置
    
-   查询用例目录下的conftest.py文件
    
-   查询测试用例的py文件中是否有setup,teardown,setup\_class,teardown\_class
    
-   再根据pytest.ini文件的测试用例的规则去查找用例并执行
    

## Pytest进阶内容

最后我们再来讲解一些pytest比较关键性的一些进阶内容

### Allure效果美化

我们在使用Pytest所生成的页面往往不够美观且展示信息杂乱不好分析，所以我们通常搭载allure来实现界面美化：

-   Allure框架是一个灵活轻量级多语言测试报告工具
-   它不仅可以以WEB的方式展示简介的测试结果，而且允许参与开发过程的每个人从日常执行的测试中最大限度的提取有用信息

下面我们就来学习如何安装使用allure：

```python
# 首先我们需要去下载在电脑上下载allure并配置好环境变量
# 我们这里给出官网下载地址：https://github.com/allure-framework/allure2/releases 
# 温馨提醒：下载链接在github上，如果无法打开可以刷新重试或者使用加速器梯子等辅助工具
# 环境变量的配置只需要将bin文件所在目录放在电脑的Path路径下即可，这里不再展示

# 第二步我们需要在pycharm上下载allure-pytest插件（如果之前pip了那个整体文件，这里应该是已经下载过了）
pip install allure-pytest

# 第三步我们就可以直接来生成allure的测试结果展示界面了

# 1.我们通常首先需要生成一个allure临时Json文件
# 我们通常会加上这么一串"‐‐alluredir=./temps ‐‐clean‐alluredir"
# ‐‐alluredir = 文件生成地址 ： 表示我们将allure临时文件生成在我们所指定的相对临时目录下
# ‐‐clean‐alluredir ： 由于每次都会生成大量文件，所以我们会在生成前清除当前目录下的allure文件，保证我们数据都是最新数据

# 2.我们需要依靠临时文件来生成allure.html网页
# 我们通常在main方法中执行
if __name__ == '__main__':
    # 正常运行
    pytest.main()
    # 休眠：主要为了JSON临时文件的生成
    time.sleep(3)
    # allure generate 固定语句 + allure临时JSON文件目录 + -o 输出指令 + allure.html生成文件目录 + --clean 清除旧数据
    os.system("allure generate ./temps ‐o ./reports ‐‐clean")

```

### Parametrize数据驱动

我们通常会采用Parametrize注解来进行数据驱动，下面我们来详细讲解一下：

```python
# 格式：@pytest.mark.parametrize(参数名称，参数值)
# 意义：我们会将参数名称作为id，然后根据参数值的个数去依次调用，存在n个参数值，我们将会调用n次case

# 1.参数值为列表或元组时，参数名称可以为一个
# 首先我们这里因为使用单个元素的列表（元组），我们的参数名可以为一个
@pytest.mark.parametrize('caseinfo',['胡桃','胡桃宝宝','芙芙'，'芙芙宝宝'])
# 在方法参数里，我们需要调用parametrize的参数名称caseinfo，需要保证一模一样
def test_01_get_token(self,caseinfo):
    # 在这里我们可以借助参数名称caseinfo来代替列表中的元素
    # 列表中存在几个，我们该方法将执行几次，例如现在列表是四个元素，那么我们方法将会重复执行四次并每次按顺序赋值不同的元素
	print("获取统一接口鉴权码："+caseinfo)
    
# 2.参数值为列表的多个时，参数名称可以为多个
# 这里我们列表中嵌套了一个列表，如果我们是单参数名称，那么输出时就会将第一个列表['胡桃厨','胡桃宝宝']输出出去
# 但是如果我们是多参数名称，系统会自动将第一个列表的元素分开赋值给arg1，arg2便于我们分开使用，个人还是比较推荐的
@pytest.mark.parametrize('arg1,arg2',[['胡桃厨','胡桃宝宝'],['芙芙厨','芙芙宝宝']])
# 注意：这里当然也需要和参数名称对应！！！
def test_01_get_token(self,arg1,arg2):
	print("获取统一接口鉴权码："+str(arg1)+" "+str(arg2))

```

我们在进行数据驱动时通常会结合Yaml文件来进行数据获取，这里我们简单介绍一下Yaml文件：

```python
# yaml是一种数据格式，扩展名可以是yaml,yml
# 支持#注释，通过缩进表示层级，区分大小写，且yaml文件最后获取的结果展示是一个字典列表格式
# yaml文件经常用于书写配置，例如Java的Spring中的配置文件，而我们也经常采用yaml编写自动化测试用例

# yaml文件通常会出现两种格式

# 字典格式：如果我们正常书写yaml文件，如下就是字典模式
name: 胡桃

# 列表模式：如果我们采用yaml中的列表，那么我们在py获取时也将获得列表
msjy:
    - name1: 胡桃
    - name2: 芙芙
    - ages1: 18
    - ages2: 19
# 我们也可以利用这个特性，直接在yaml中做多个列表，来多次提取
-
	name:'xxx'
    age:18
-
	name:'xxx'
    age:20

# 我们这里首先给出一个解析yaml文件的示例函数：
import os.path
import yaml

# 这里是获取当前路径，因为我们需要找到对应的yaml文件，那么具体路径就需要我们进行拼接
def get_obj_path():
    # 这里我们使用了Python的os类来进行当前路径获取，最后返回结果其实是一个String字符串
    # 我们以'common'作为分界（common是当前文件夹的名称，我们将该Str进行划分，获取前面的部分），获取到前面的路径部分来进行拼接
    return os.path.dirname(__file__).split('common')[0]

# 然后我们这里定义一个方法来解析yaml文件
def read_yaml(yamlPath):
    with open(get_obj_path() + yamlPath,mode = 'r',encoding = 'utf-8') as f:
        # 这里需要我们pip install pyyaml
        value = yaml.load(steam=f,Loader=yaml.FullLoader)
        return value
    
# 然后我们这里采用一个main方法来执行上述用例（其实应该在其他测试类中执行）
if __name__ = '__main__':
    # 调用read_yaml方法并给出yaml路径
    print(read_yaml('testcase/user_manage/get_token.yaml'))

# 了解了所有东西之前我们就可以结合之前的Parametrize来进行操作：
# 我们这里将所需要的数据变为read_yaml读取的yaml文件内容
@pytest.mark.parametrize('caseinfo',read_yaml('testcase/user_manage/get_token.yaml'))
def test_01_get_token(self,caseinfo):
    # 这里我们就可以获取到yaml文件内容并输出了
	print("获取统一接口鉴权码："+caseinfo)
    
# 当然如果我们了解我们的yaml中拥有什么元素，我们还可以采用[]的方式具体表达出来
@pytest.mark.parametrize('caseinfo',read_yaml('testcase/user_manage/get_token.yaml'))
def test_01_get_token(self,caseinfo):
	print("获取统一接口鉴权码：")
    # 这里我们可以直接获取namekey对应的value
    print("caseinfo[name]："+ caseinfo['name'])
    # 这里我们可以分别获取request层下的method，url，data分别对应的value
    print("caseinfo[name]："+ caseinfo['request']['method'])
    print("caseinfo[name]："+ caseinfo['request']['url'])
    print("caseinfo[name]："+ caseinfo['request']['data'])

```

# 结束语

这篇文章中详细介绍了Python的第三方框架pytest，大家在阅读完毕后就掌握了pytest的基本使用方法

下面给出我学习和书写该篇文章的一些参考文章，大家也可以去查阅：

1.  码尚课程：[2023最新pytest接口自动化测试框架，三天带你精通pytest，带你写出最好的代码！（已更新2023新版）\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1py4y1t7bJ/?spm_id_from=333.999.0.0&vd_source=338ccc664622651493b6fe1ded5bc801)
2.  知乎文章：[超详细的 pytest 教程【入门篇】 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/511774800)
3.  CSDN：[Python测试框架：pytest学习笔记-CSDN博客](https://blog.csdn.net/m0_58026506/article/details/134292288)