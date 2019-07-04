# coding=utf-8
import time
import sys
import mysql.connector
reload(sys)
sys.setdefaultencoding('utf-8')
 


config = {
        #'host': '127.0.0.1',
        #'port': 3306,
        'database': 'mysql_db',
        'user': 'root',
        'password': 'Awq991018',
        'charset': 'utf8',
        'use_unicode': True,
        'get_warnings': True,
        'autocommit':True
    }


conn = mysql.connector.connect(**config)

conn = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="Awq991018",
	charset='utf8',
        use_unicode=True,
        get_warnings=True,
        autocommit=True
)
'''
cur = conn.cursor()
#cur.execute("CREATE DATABASE mysql_db")
'''
def time_me(fn):
    def _wrapper(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        seconds = time.time() - start
        print u"{func}函数每{count}条数数据写入耗时{sec}秒".format(func = fn.func_name,count=args[0],sec=seconds)
    return _wrapper
 
#普通写入
@time_me
def ordinary_insert(count):
    sql = "insert into stu(name,age,class)values('test mysql insert',30,8)"
    for i in range(count):
        cur.execute(sql)
 
 
 
#批量
@time_me
def many_insert(count):
    sql = "insert into stu(name,age,class)values(%s,%s,%s)"
 
    loop = count/20
    stus = (('test mysql insert', 30, 30), ('test mysql insert', 30, 31), ('test mysql insert', 30, 32), ('test mysql insert', 30, 32)
                 ,('test mysql insert', 30, 32), ('test mysql insert', 30, 32), ('test mysql insert', 30, 32), ('test mysql insert', 30, 32),
                 ('test mysql insert', 30, 32), ('test mysql insert', 30, 32)
                ,('test mysql insert', 30, 30), ('test mysql insert', 30, 31), ('test mysql insert', 30, 32), ('test mysql insert', 30, 32)
                 ,('test mysql insert', 30, 32), ('test mysql insert', 30, 32), ('test mysql insert', 30, 32), ('test mysql insert', 30, 32),
                 ('test mysql insert', 30, 32), ('test mysql insert', 30, 32))
    #并不是元组里的数据越多越好
    for i in range(loop):
        cur.executemany(sql, stus)
 
#事务加批量
@time_me
def transaction_insert(count):
    sql = "insert into stu(name,age,class)values(%s,%s,%s)"
    insert_lst = []
    loop = count/20
 
    stus = (('test mysql insert', 30, 30), ('test mysql insert', 30, 31), ('test mysql insert', 30, 32), ('test mysql insert', 30, 32)
                 ,('test mysql insert', 30, 32), ('test mysql insert', 30, 32), ('test mysql insert', 30, 32), ('test mysql insert', 30, 32),
                 ('test mysql insert', 30, 32), ('test mysql insert', 30, 32)
                ,('test mysql insert', 30, 30), ('test mysql insert', 30, 31), ('test mysql insert', 30, 32), ('test mysql insert', 30, 32)
                 ,('test mysql insert', 30, 32), ('test mysql insert', 30, 32), ('test mysql insert', 30, 32), ('test mysql insert', 30, 32),
                 ('test mysql insert', 30, 32), ('test mysql insert', 30, 32))
    #并不是元组里的数据越多越好
    for i in range(loop):
        insert_lst.append((sql,stus))
        if len(insert_lst) == 20:
            conn.start_transaction()
            for item in insert_lst:
                cur.executemany(item[0], item[1])
            conn.commit()
            print '0k'
            insert_lst = []
 
    if len(insert_lst) > 0:
        conn.start_transaction()
        for item in insert_lst:
            cur.executemany(item[0], item[1])
        conn.commit()
 
def test_insert(count):
    ordinary_insert(count)
    many_insert(count)
    transaction_insert(count)
 
if __name__ == '__main__':
    if len(sys.argv) == 2:
        loop = int(sys.argv[1])
        test_insert(loop)
    else:
        print u'参数错误'
