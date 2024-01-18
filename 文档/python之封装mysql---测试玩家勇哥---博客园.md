##  数据查询类封装

### 1\. 功能分析

1.  可以连接不同sql数据库
2.  查一条数据，多条数据
3.  可以获取不同格式的数据

### 2\. 封装成数据库查询类

封装思路:

1.  数据库查询模块有多个功能，且需要复用，所以封装成类
    
2.  在构造方法中创建连接
    
3.  创建对象方法实现各种查询
    
    ```
    # -*- coding: utf-8 -*-
    # @Time : 2019/11/13 14:51
    # @Author : kira
    # @Email : 262667641@qq.com
    # @File : do_mysql.py
    # @Project : risk_project
    
    import pymysql
    from pymysql.cursors import DictCursor
    
    
    class DoMysql:
        """
        sql数据库查询类
        """
    
        def __init__(self, db_config: dict):
            # 创建连接
            engine = db_config.pop('engine', 'mysql')
            if engine.lower() == 'mysql':
                self.conn = pymysql.connect(**db_config)
            elif engine.lower() == 'oracle':
                pass
    
        def __execute(self, sql, action, res_type='t', *args):
            """
            :param sql:
            :param action: 字符串，指定执行cursor对应的方法
            :param res_type: 返回数据类型
            :param args: 
            :return:
            """
            if res_type == 't':
                cursor = self.conn.cursor()
            else:
                cursor = self.conn.cursor(DictCursor)
            try:
                cursor.execute(sql)
                return getattr(cursor, action)(*args)
            except Exception as e:
                raise e
            finally:
                cursor.close()
    
        def get_one(self, sql, res_type='t'):
            """
            获取一条数据
            :param sql:
            :param res_type: 返回数据的类型，默认为t表示以元组返回，'d'表示以字典的形式返回
            :return: 元组/字典
            """
            # 数据库若断开即重连
            self.reConnect()
            return self.__execute(sql, 'fetchone', res_type)
    
        def get_many(self, sql, size, res_type='t'):
            # 数据库若断开即重连
            self.reConnect()
            return self.__execute(sql, 'fetchmany', res_type, size)
    
        def get_all(self, sql, res_type='t'):
            # 数据库若断开即重连
            self.reConnect()
            return self.__execute(sql, 'fetchall', res_type)
    
        def exist(self, sql):
            if self.get_one(sql):
                return True
            else:
                return False
    
        def reConnect(self):
            """
            重连机制
            :@return
            """
            try:
                self.conn.ping()
            except:
                self.conn()
    
        def __del__(self):
            """
            对象销毁的时候自动会被调用
            :return:
            """
            self.conn.close()
    
    
    if __name__ == '__main__':
        db = {
            'engine': 'mysql',  # 指定mysql数据
            'host': '127.0.0.1',
            'user': 'admin',
            'password': '12345',
            'port': 3306,
            'db': 'mysql',
            'charset': 'utf8'
        }
        db = DoMysql(db)
        sql = 'select id, reg_name, mobile_phone from member limit 10'
        # res = db.get_one(sql)
        res = db.get_many(sql, size=5)
        print(res)
    ```
    
    ***
    
    # 总结
    
    以上就是勇哥今天为各位小伙伴准备的内容，如果你想了解更多关于Python自动化测试的知识和技巧，欢迎关注：
    
    我的公众号：百态测试
    
    博客（[奈非天的主页 - 博客园 (cnblogs.com)](https://home.cnblogs.com/u/Nephalem-262667641)）
    
    我会不定期地分享更多的精彩内容。感谢你的阅读和支持！
    
    本文来自博客园，作者：[奈非天](https://www.cnblogs.com/Nephalem-262667641/)，转载请注明原文链接：[https://www.cnblogs.com/Nephalem-262667641/p/17460169.html](https://www.cnblogs.com/Nephalem-262667641/p/17460169.html)