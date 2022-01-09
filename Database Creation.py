#This program will perform the operation to create database.

def database(hostname,username,pswd,databse):
    import mysql.connector as sql
    conn=sql.connect(host=hostname,user=username,passwd=pswd)
    mycursor=conn.cursor()
    s="create database '{}'".format(databse)
    mycursor.execute(s)
hostname=input("Enter the host type:")
username=input("Enter the username:")
pswd=input("Enter the password:")
databse=input("Enter the name you want to give to your database eg-railway :")
database(hostname,username,pswd,databse)
