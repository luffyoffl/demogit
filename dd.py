

import mysql.connector
from cffi import error
from mysql.connector import Error
from utill import get_password
try:
    conn=mysql.connector.connect (
        host='localhost',
        user='root',
        password=get_password(),
        database='zoro'
    )
    if conn.is_connected():
        print("connected to db")
        cursor=conn.cursor()
        query="""
        show tables ;
        
        
        """
        conn.commit()
        cursor.execute(query)
        result=cursor.fetchall()
        with open("x.txt","w+") as f:
            for i in result:
                f.write(f"{i}\n")
except error as e:
    print("Error while connecting to db",e)
finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("closed connection to db")
