```python
import pymysql  # 导入pymysql
from pymysql.cursors import DictCursor  # 设为字典游标

try:
    # 1 创建连接(相当于连接Python程序和mysql数据库的‘高速公路’)
    conn = pymysql.connect(
        user='root',
        password='54jixuxingfu',
        host='localhost',
        database='spider',
        port=3306
    )

    # 2 创建游标(相当于高速公路上的货车，可以向数据库服务器发送SQL命令)
    cursor = conn.cursor(cursor=DictCursor)  # 设为字典游标

    # 3 准备待执行的SQL命令
    sql_insert = "insert into stu_new(sname, sage, score, sgender, class) values ('娃哈哈', 18, 66, 1, '七年五班')"
    sql_show = "select * from stu_new"

    # 4 执行的SQL命令
    cursor.execute(sql_insert)  # 执行插入命令

    cursor.execute(sql_show)  # 执行显示数据库数据命令
    data = cursor.fetchall()  # 使用fetchall()返回执行结果，格式为字典
    print(data)

    # 5 提交事务(pymysql在执行sql的时候, 默认开启了事务，保证了数据的完整性，防止程序二次运行造成的数据冗余)
    conn.commit()  # 数据无误，提交数据进入数据库，commit数据库就存入数据，反之不存入
except Exception as e:
    print(e)
    conn.rollback()  # 数据有误，回滚(把原先进入数据库的数据给拽回来，后续数据也不再进入数据库)

finally:  # 收尾操作
    if cursor:
        cursor.close()
    if conn:
        conn.close()  # 一定记得要关闭链接

```