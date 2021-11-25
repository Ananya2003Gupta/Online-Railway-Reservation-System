#This program will perform the operation to create database.

def database():
    import mysql.connector as sql
    conn=sql.connect(host=hostname,user=username,passwd=pswd)
    mycursor=conn.cursor()
    s="create database railway"
    mycursor.execute(s)
hostname=input("Enter the host type:")
username=input("Enter the username:")
pswd=input("Enter the password:")
database()
