import sqlite3
connection=sqlite3.connect("school.db")
cursor=connection.cursor()
cursor.execute("SELECT * FROM management")
print ("fetchall:")
result=cursor.fetchall()
for r in result:
 print (r)
 print("-----+---------+----+----------------------+--------")