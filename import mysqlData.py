import mysql.connector

con = mysql.connector.connect(
user='root', password='root', 
host='127.0.0.1', port='3306', database = 'SAT')

c = con.cursor()
c.execute('select * from dvt')
result=c.fetchall()
print(type(result))

for i in result:
    print(type(i))
    print (i)

