'''
from database import Database

# 创建数据库对象
db = Database("localhost", "yourusername", "yourpassword", "mydatabase")

# 查询数据
sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"
result = db.query(sql)
for x in result:
  print(x)

# 插入数据
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
db.execute(sql, val)

# 更新数据
sql = "UPDATE customers SET address = 'Canyon 123' WHERE name = 'John'"
db.execute(sql)

# 删除数据
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
db.execute(sql)

# 关闭连接
db.close()

'''

import pymysql


class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.mydb = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.mycursor = self.mydb.cursor()

    def query(self, sql):
        """
        执行查询语句
        :param sql: SQL语句
        :return: 查询结果集
        """
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()

    def execute(self, sql, val=None):
        """
        执行增、删、改操作
        :param sql: SQL语句
        :param val: 参数列表
        """
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "条记录已处理。")

    def close(self):
        """
        关闭游标和数据库连接
        """
        self.mycursor.close()
        self.mydb.close()
