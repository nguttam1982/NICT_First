import mysql.connector

con = mysql.connector.connect(
user='Rabi', password='PCSGlobal@4321', 
host='91.107.217.142', port='54256', database = 'apptek_analytics_db')

c = con.cursor()
c.execute('select * from emp')
result=c.fetchall()
print(type(result))

for i in result:
    print (i)

    