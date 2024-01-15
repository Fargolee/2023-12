#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/15 19:08
# @Author  : Lee
# @File    : Python 封装.py
"""
https://ceshiren.com/t/topic/26229
封装的概念
封装（Encapsulation）
隐藏：属性和实现细节，不允许外部直接访问
暴露：公开方法，实现对内部信息的操作和访问
封装的作用
限制安全的访问和操作，提高数据安全性
可进行数据检查，从而有利于保证对象信息的完整性
封装的实现：隐藏
保护属性：_属性名
私有属性：__属性名
被视作 _类名__属性名

"""
class Account:

    # 普通属性
    bank = 'BOX'
    # 内部属性
    _username = 'Admin'
    # 私有属性
    __password = '666'

#通过类名访问类属性

print(Account.bank)
# BOX
print(Account._username)
# Admin
# print(Account.__password)
# AttributeError: type object 'Account' has no attribute '__password'
print(Account.__dict__)


# 实例化
obj = Account()

print(obj.bank)
# BOX
print(obj._username)
# Admin
# print(obj.__password)
# AttributeError


'''封装的实现：暴露
提供数据访问功能（getter）
计算属性
语法：使用@property装饰器
调用：实例.方法名'''
class Account:
    # 普通属性
    bank = "BOC"
    # 内部属性
    _username = "Hogwarts"
    # 私有属性
    __password = "888"

    @property
    def password(self):
        return self.__password

# 实例化对象
obj = Account()

# 访问实例的私有属性
print(obj.password)  # 将会打印 888

'''封装的实现：暴露
提供数据操作功能（setter）
语法：使用@计算属性名.setter装饰器
调用：实例.方法名
'''
class Account:
    # 普通属性
    bank = "BOC"
    # 内部属性
    _username = "Hogwarts"
    # 私有属性
    __password = "888"

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        # 增加数据的校验
        if len(value) >= 8:
            self.__password = value
        else:
            print("密码长度最少要有8位！")


# 实例化对象
obj = Account()
