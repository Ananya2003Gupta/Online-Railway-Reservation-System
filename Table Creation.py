#this program creates the required tables that will be used in the main program for data storage in the database created using database creation file.
def table():
    import mysql.connector as sql
    mycon=sql.connect(host=hostname,user=username,passwd=pswd,database=databasename)
    cursor=mycon.cursor()
    mycon.autocommit=True
    s1="create table railway(fname varchar(100), lname varchar(100), phno varchar(20), age int(4), gender varchar(1), fromf varchar(100), tod varchar(100), datefd date, username varchar(100), password varchar(100), trainexp varchar(50))"
    cursor.execute(s1)
    s2="create table useraccount(fname varchar(100), lname varchar(100), username varchar(100) primary key, password varchar(100), phno varchar(20), gender varchar(50), dob date, age varchar(4))"
    cursor.execute(s2)
hostname=input("Enter the host type:")
username=input("Enter the username:")
pswd=input("Enter the password:")
databasename=input("Enter the name of database:")
table()
