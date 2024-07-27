import mysql.connector
from mysql.connector import errorcode
host = "192.168.1.189"
user = "root"
passwd = "Theodora123!"


try:
    mydb = mysql.connector.connect(
        host = "192.168.1.189",
        user = "root",
        passwd = "Theodora123!"
    )
    cursor = mydb.cursor()
    
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS alx_book_store")
        print(f"Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print(f"Database 'alx_book_store' already exists.")
        else:
            print(f"Failed to create database 'alx_book_store': {err}")

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
#print("Database 'database_name' created successfully!")
#CREATE DATABASE database_name;