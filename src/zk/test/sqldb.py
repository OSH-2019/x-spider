#coding=utf-8
import pymysql
import time

# db = pymysql.connect("localhost","root","111111","xzk")
# print("connection is ok!")

# cursor = db.cursor()

# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,  
#          SEX CHAR(1),
#          INCOME FLOAT )"""

# cursor.execute(sql)

# db.close()

a = time.time()
# 打开数据库连接
db = pymysql.connect("localhost","root","111111","xzk" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 插入语句
for i in range(1,4001):
	sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
	         LAST_NAME, AGE, SEX, INCOME)
	         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
	try:
	   # 执行sql语句
	   cursor.execute(sql)
	   # 提交到数据库执行
	   db.commit()
	except:
	   # 如果发生错误则回滚
	   db.rollback()

 # 关闭数据库连接
db.close()

b = time.time()

print((b-a)/4000)
