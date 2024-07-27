import mysql.connector
from mysql.connector import errorcode
host = "192.168.1.189"
user = "root"
passwd = "Theodora123!"

database_name = "alx_book_store"
try:
    mydb = mysql.connector.connect(
        host = "192.168.1.189",
        user = "root",
        passwd = "Theodora123!"
    )
    cursor = mydb.cursor()
    
    try:
        cursor.execute(f"CREATE DATABASE {database_name}")
        print(f"Database '{database_name}' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print(f"Database '{database_name}' already exists.")
        else:
            print(f"Failed to create database '{database_name}': {err}")

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
#print("Database 'database_name' created successfully!")
#CREATE DATABASE database_name;