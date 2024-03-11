import mysql.connector
import sys
sys.dont_write_bytecode = True

cnx = mysql.connector.connect(user='root', 
    password='413426Txwd!',
    host='127.0.0.1',
    database='',
    auth_plugin='mysql_native_password')

# create cursor
cursor = cnx.cursor()

# delete previous db
query = ("DROP DATABASE IF EXISTS `country`;")
cursor.execute(query)

# create db
query = ("CREATE DATABASE IF NOT EXISTS country")
cursor.execute(query)

# use db
query = ("USE country")
cursor.execute(query)

# create table
query = ('''
CREATE TABLE countries(
    name VARCHAR(36),
    capital VARCHAR(20)
)
''')
cursor.execute(query)

# Insert three entries into the table
entries = [
    ('U.S.', 'Washington DC'),
    ('United Kindom', 'London'),
    ('Japan', 'Tokyo')
]

insert_query = "INSERT INTO countries (name, capital) VALUES (%s, %s)"

cursor.executemany(insert_query, entries)

# clean up
cnx.commit()
cursor.close()
cnx.close()    