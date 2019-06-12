import mysql.connector

config = {'user': 'root', 'password': '@Chao0309'}
connection = mysql.connector.connect(**config)
print(connection)
cursor = connection.cursor()
cursor.execute('show databases')
for db in cursor:
    print(db)
