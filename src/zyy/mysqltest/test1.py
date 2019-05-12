
#!/usr/bin/python3
 
import pymysql

db = pymysql.connect("localhost","test","test","TESTDB")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")
 
data = cursor.fetchone()
 
print (data)
 
db.close()
