import mysql.connector
import pymysql
from mysql.connector import connect
from mysql.connector import errorcode

from utill import *
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password='root',
    database="zoro",
    #cursorclass=pymysql.cursors.DictCursor

)
try:
    with con.cursor() as cursor:
        create_table="""
        CREATE TABLE  bob1 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        department VARCHAR(100)
        );
        """
        cursor.execute(create_table)

        insert_data="INSERT INTO bob1 (name,department) VALUES (%s,%s)"
        values=[("luffy","captain"),("zoro","swordsmen"),("kaido","emporer")]
        cursor.executemany(insert_data,values)
        con.commit()


        xx="SELECT  * FROM bob1"
        cursor.execute(xx)
        result= cursor.fetchall()

        with open("z.txt","w") as f:
            for row in result:
            #print(row)
                f.write(f"{row}\n")
finally:

     con.close()

