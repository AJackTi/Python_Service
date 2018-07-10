import MySQLdb as mdb

sql_host = "localhost"
sql_username = "username"
sql_password = "password"
sql_database = "databasename"

sql_connection = mdb.connect(sql_host, sql_username, sql_password, sql_database) # Connection

#print sql_connection

cursor = sql_connection.cursor()

cursor.execute("use databasename")

# Create Table
#cursor.execute("create table FromPython(Column1 VARCHAR(10), Column2 INT, Column3 FLOAT(6,2))")

# Create data
cursor.execute("insert into FromPython(Column1, Column2, Column3) values('string', 10, 123.45)")

cursor.execute("select * from FromPython")

output = cursor.fetchone()

print output

sql_connection.commit()

sql_connection.close() # Close
