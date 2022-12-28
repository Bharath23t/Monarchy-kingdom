import sqlite3
connection=sqlite3.connect("school.db")
cursor=connection.cursor()
cursor.execute("""DROP TABLE management;""")
sql_command ="""CREATE TABLE management (Rollno INTEGER PRIMARY KEY,Sname VARCHAR(20),grade CHAR(1), course VARCHAR(20));"""
cursor.execute(sql_command)
sql_command ="""INSERT INTO management (Rollno, sname,grade, course) VALUES ("101","Bharath","B","maths and computer");"""
cursor.execute(sql_command)
sql_command ="""INSERT INTO management (Rollno, sname,grade, course) VALUES ("102","jejesh","C","maths and computer");"""
cursor.execute(sql_command)
sql_command ="""INSERT INTO management (Rollno, sname,grade, course) VALUES ("103","Harish","A","maths and computer");"""
cursor.execute(sql_command)
sql_command ="""INSERT INTO management (Rollno, sname,grade, course) VALUES ("104","Eswer","A","Biology and maths");"""
cursor.execute(sql_command)
sql_command ="""INSERT INTO management (Rollno, sname,grade, course) VALUES ("105","Vignesh","D","maths and computer");"""
cursor.execute(sql_command)
connection.commit()
connection.close()
print ("STUDENT TABLE CREATED")