
import mysql.connector
from mysql.connector import connection

def getAllBases(host,user,contra,pueto):
    db= mysql.connector.connect(
    
    host=str(host),
    user=str(user),
    password=str(contra),
    port=int(pueto),
    
)
    cursor=db.cursor(dictionary=True)
    cursor.execute("show databases")
    
    return cursor.fetchall(), print("exito")


def createbase(host,user,contra,pueto,base):
    db= mysql.connector.connect(
    
    host=str(host),
    user=str(user),
    password=str(contra),
    port=int(pueto),
    
)
    cursor=db.cursor(dictionary=True)
    cursor.execute('''create database  %s;''',(base))
    db.commit()
    cursor.close()

    
  
    

