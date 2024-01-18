![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd6db9c4bb4e4e518d7e17f6caac0031~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

1\. 文件操作
--------

Python中的文件操作通常使用内置的`open()`函数来打开文件。以下是一个简单的示例：

python

复制代码

`with open("file.txt", "r") as f:     content = f.read()     print(content)`

在这个示例中，我们打开了名为"file.txt"的文件，并将其读入变量`content`中，最后将其打印出来。

`open()`函数的第一个参数是文件名，第二个参数是打开文件的模式。以下是一些常用的模式：

*   `"r"`：只读模式
*   `"w"`：写入模式（会覆盖已有文件）
*   `"a"`：追加模式（不会覆盖已有文件）

2\. 正则表达式
---------

正则表达式是一种强大的工具，可以帮助我们从文本中提取信息或进行文本替换。Python中可以使用内置的`re`模块来进行正则表达式操作。以下是一个示例：

python

复制代码

`import re text = "The quick brown fox jumps over the lazy dog." pattern = r"fox" matches = re.findall(pattern, text) print(matches)`

在这个示例中，我们定义了一个正则表达式模式`r"fox"`，然后使用`re.findall()`函数来查找匹配该模式的所有字符串。最后，我们将匹配的结果打印出来。

3\. 异常处理
--------

在编写程序时，经常需要处理可能出现的错误或异常情况。Python中可以使用`try`和`except`语句来实现异常处理。以下是一个简单的示例：

python

复制代码

`try:     x = 1 / 0 except ZeroDivisionError:     print("Error: division by zero")`

在这个示例中，我们尝试计算1除以0，这将引发一个`ZeroDivisionError`异常。我们使用`try`和`except`语句来捕获该异常并打印出一条错误消息。

4\. 面向对象编程（Object-Oriented Programming）
---------------------------------------

面向对象编程是一种重要的编程范式，Python是一种面向对象的语言。以下是一个简单的示例：

ruby

复制代码

`class Person:     def __init__(self, name, age):         self.name = name         self.age = age          def say_hello(self):         print("Hello, my name is " + self.name) person = Person("Alice", 25) person.say_hello()`

在这个示例中，我们定义了一个名为`Person`的类，并定义了一个构造函数`__init__()`来初始化对象的属性。我们还定义了一个名为`say_hello()`的方法，用于打印出问候语。最后，我们创建一个`Person`对象，并调用`say_hello()`方法。 Python是一种面向对象编程语言，它支持面向对象编程的三个基本概念：封装、继承和多态。面向对象编程的核心思想是将数据和操作数据的方法封装在一起，形成一个对象。

#### 示例代码

ruby

复制代码

`class Animal:     def __init__(self, name, age):         self.name = name         self.age = age     def say_hello(self):         print(f'{self.name} is saying hello') class Cat(Animal):     def __init__(self, name, age, color):         super().__init__(name, age)         self.color = color     def catch_mouse(self):         print(f'{self.name} is catching mouse') cat = Cat('Tom', 2, 'White') cat.say_hello() cat.catch_mouse()`

#### 输出结果

csharp

复制代码

`Tom is saying hello Tom is catching mouse`

5\. Python高级特性
--------------

### 5.1 生成器（Generator）

生成器是一种特殊的函数，可以在函数执行期间多次返回值，并且可以保留当前执行状态，等待下一次调用。它们是高效的迭代器，可以用于处理大量数据或无限流数据，同时也能节省内存。

#### 示例代码

less

复制代码

`pythonCopy code def fib():     a, b = 0, 1     while True:         yield a         a, b = b, a + b f = fib() for i in range(10):     print(next(f))`

#### 输出结果

css

复制代码

`Copy code 0 1 1 2 3 5 8 13 21 34`

### 5.2 装饰器（Decorator）

装饰器是一种函数，用于修改其他函数的行为。它们提供了一种简单的方式来修改函数，而无需修改函数的原始定义。装饰器的常见用途包括添加日志、计时、缓存等功能。

#### 示例代码

python

复制代码

`pythonCopy code import time def timer(func):     def wrapper(*args, **kwargs):         start = time.time()         result = func(*args, **kwargs)         end = time.time()         print(f'{func.__name__} executed in {end - start} seconds')         return result     return wrapper @timer def calculate_sum(n):     return sum(range(n+1)) print(calculate_sum(100000000))`

#### 输出结果

css

复制代码

`Copy code calculate_sum executed in 4.150076866149902 seconds 5000000050000000`

本文转自 <https://juejin.cn/post/7224335234010234935>，如有侵权，请联系删除。