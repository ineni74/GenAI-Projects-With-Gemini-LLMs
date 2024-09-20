import sqlite3

connection= sqlite3.connect("student.db")

cursor=connection.cursor()

table_info= """
create table STUDENT(NAME VARCHAR(25), CLASS VACHAR(10), SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

cursor.execute("""Insert INTO STUDENT values('sreenivas', 'Data Science', 'A', 90)""")
cursor.execute("""Insert INTO STUDENT values('Prasanna', 'Data Analytics', 'B', 80)""")
cursor.execute("""Insert INTO STUDENT values('Balaram', 'Data Science', 'A', 70)""")
cursor.execute("""Insert INTO STUDENT values('Venkat', 'Data Analytics', 'B', 93)""")
cursor.execute("""Insert INTO STUDENT values('Chethan', 'Data Science', 'A', 78)""")
cursor.execute("""Insert INTO STUDENT values('Hima', 'Data Analytics', 'B', 87)""")
cursor.execute("""Insert INTO STUDENT values('Malli', 'Data Science', 'A', 65)""")

print("inserted records are:")

data= cursor.execute("select * from STUDENT;")
for row in data:
    print(row)

connection.commit()
connection.close()
