# Online-Railway-Reservation-System
This is a menu driven Railway Reservation Project which is mainly based on the python-mysql connectivity.

The project contains three python files.(The order in which they will be executed)
1.Database Creation.py
2.Table Creation.py
3.Online Railway Reservation Program.py

Software Requirements:
1.Python IDLE
2.MySQL

Connect mysql with python before running this program.
Check by executing the command -( import mysql.connector ) in python IDLE.
If the command gives error, you will have to connect mysql with python.
Otherwise you are good to go.

Files Description:
1. Database Creation.py
This python file contains the program to create the database.The user defined function database() contains the code to create the database in mysql.User will be asked to enter the host type, user name and password which he/she has setup for mysql.

2. Table Creation.py
This python file contains the program to create the tables that will be required in the main program. Remember to create the database by executing the Database Creation.py file before executing this file. Table Creation.py contains the user defined function table that contains the code to create two tables railway and useraccount that will be used in the main program to store user's data.User will be asked to enter the host type, user name, password and database name (name of the database he/she created using Database Creation.py).

3.Online Railway Reservation Program.py
This python file is the main program that will perform the functions like sign in , sign up, delete account, user details, train ticket booking, train ticket checking and train ticket cancelling.Remember to execute the Table Creation.py to create the tables which will be used in this python file before executing it.
