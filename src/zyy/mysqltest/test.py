from rain.client import Client, remote

@remote()
def hello(ctx):
    import pymysql
    db = pymysql.connect("localhost","test","test","TESTDB")
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    db.close()
    return "".join(data)

client = Client("localhost", 7210)

with client.new_session() as session:
    t = hello()             
    t.output.keep()
    session.submit()
    result = t.output.fetch()
    print(result.get_bytes())        
