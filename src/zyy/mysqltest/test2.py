from rain.client import Client, remote, blob
import pymysql

@remote()
def hello(ctx):
    db = pymysql.connect("localhost","test","test","TESTDB")
    cursor = db.cursor()
    a=12345
    b=56789
    for i in range(10):
        sql="insert into TESTDB.data(time,num) value(%d,%d)" % (a,b)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
    
    sql = "select num from TESTDB.data where time > %d" % 10000
    cursor.execute(sql)
    results = cursor.fetchall()

    sum = 0
    for row in results:
        sum = sum + row[0]    
    
    db.close()
    return str(sum)



client = Client("localhost", 7210)

with client.new_session() as session:
    t = hello()
    t.output.keep()
    session.submit()
    result = t.output.fetch()
    print(result.get_bytes())