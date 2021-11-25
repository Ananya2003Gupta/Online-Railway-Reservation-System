#This is the main program that will perform all the functions.
def connectivity():
    import mysql.connector
    mycon=mysql.connector.connect (host=hostname,user=username, passwd=pswd,database=databasename)
    cursor=mycon.cursor()
    mycon.autocommit=True

def menu():
    print('1.YES')
    print('2.NO')
    ch=int(input('DO YOU WANT TO CONTINUE OR NOT:'))
    while ch==1:
        print('WELECOME TO ONLINE RAILWAY RESERVATION SYSTEM')
        print('1.SIGN IN')
        print('2.SIGN UP')
        print('3.DELETE ACCOUNT')
        print('4.EXIT')
        ch1=int(input('ENTER YOUR CHOICE:'))
        if ch1==1:
            a=sign_in()
            if a==True:
                print('WELCOME')
                main()
            else:
                print("ACCOUNT DOES NOT EXIST.")
                continue
        elif ch1==2:
            a=sign_up()
            if a==True:
                main()
            else:
                print('PASSWORD ALREADY EXISTS')
                continue
        elif ch1==3:
            c=delete_account()
            if c==True:
                print('ACCOUNT DELETED')
                continue
            else:
                 print('YOUR PASSWORD OR USERNAME IS INCORRECT')
                 continue

        elif ch1==4:
            print('THANK YOU')
            break
        else:
            print('ERROR 404:PAGE NOT FOUND')
            break
def main():
    print('1.yes')
    print('2.no')
    c=1
    while c!=2:
        c=int(input("Do you want to continue or not:"))
        print('1.TICKET BOOKING')
        print('2.TICKET CHECKING')
        print('3.TICKET CANCELLING')
        print('4.ACCOUNT DETAILS')
        print('5.LOG OUT')
        ch=int(input('Enter your choice:'))
        if ch==1:
            ticket_booking()
        elif ch==2:
            ticket_checking()
        elif ch==3:
            ticket_cancelling()
        elif ch==4:
            account_details()
        elif ch==5:
            print('THANK YOU')
            break
        else:
            print('ERROR 404: ERROR PAGE NOT FOUND')
        
            
def ticket_booking():
    fnm=input('enter ticket booker first name:')
    lnm=input('enter ticket booker last name:')
    phno1=input('enter ticket booker phone number:')
    age=int(input('enter ticket booker age:'))
    print(' M=MALE','\n','F=FEMALE','\n','N=NOT TO MENTION')
    gender=input('enter ticket booker gender M/F/N:')
    while True:
        if gender in ("M","F","N","m","f","n"):
            break
        else:
            print("Error enter again")
            gender=input('enter ticket booker gender M/F/N:')
    v=gender.upper()
    fr=input('enter ticket booker starting point:')
    to=input('enter ticket booker destination:')
    date1=input('enter travel date(dd):')
    date2=input('enter travel month(mm):')
    date3=input('enter travel year(yyyy):')
    date=date3+"-"+date2+"-"+date1
    print(""" SELECT TRAIN:
1. KARNATAKA EXPRESS
2. RAJDHANI EXPRESS
3. SHATABDI EXPRESS
4. DURONTO EXPRESS
5. JAN SHATABDI EXPRESS
6. SAMPARK KRANTI EXPRESS""")
    tr1=int(input("ENTER YOUR CHOICE 1/2/3/4/5/6:"))
    while True:
        if tr1 in (1,2,3,4,5,6):
            break
        else:
            print("Error. Enter again")
            tr1=int(input("ENTER YOUR CHOICE 1/2/3/4/5/6:"))
    tr2={1:'KARNATAKA EXPRESS',2:'RAJDHANI EXPRESS',3:'SHATABDI EXPRESS',4:'DURONTO EXPRESS',5:'JAN SHATABDI EXPRESS',6:'SAMPARK KRANTI EXPRESS'}
    train=tr2[tr1]
    usn=input("ENTER YOUR USERNAME:")
    pswd=input("ENTER YOUR PASSWORD:")
    s1="insert into railway values('{}','{}','{}',{},'{}','{}','{}','{}','{}','{}','{}')".format(fnm,lnm,phno1,age,v,fr,to,date,usn,pswd,train)
    cursor.execute(s1)
    print('BOOKED SUCCESSFULLY')

def ticket_checking():
    print('1.yes')
    print('2.no')
    ch=int(input("do you want to continue or not:"))
    if ch==1:
        usn=input('enter your username:')
        pswd=input('enter your password:')
        phno1=input('enter your phone number:')
        try:
            s1="select * from railway where username='{}' and password='{}' and phno='{}'".format(usn,pswd,phno1)
            cursor.execute(s1)
            data=cursor.fetchall()
            for i in data:
                Data=list(i)

                a=['FIRST NAME','LASTNAME','PHONE NUMBER','AGE','GENDER','STARTING POINT','DESTINATION','DATE','TRAIN']
                print(a[0],'::::',Data[0].upper())
                print(a[1],'::::',Data[1].upper())
                print(a[2],'::::',Data[2])
                print(a[3],'::::',Data[3])
                print(a[4],'::::',Data[4].upper())
                print(a[5],'::::',Data[5].upper())
                print(a[6],'::::',Data[6].upper())
                print(a[7],'::::',Data[7])
                print(a[8],'::::',Data[10])
 
        except:
            print('TICKET DOES NOT EXISTS')
    elif ch==2:
        print('THANK YOU')
    else:
        print('ERROR 404:PAGE NOT FOUND')

def ticket_cancelling():
    print('1.yes')
    print('2.no')
    ch=int(input("do you want to continue or not:"))
    if ch==1:
        fnam=input('enter the ticket holder first name:')
        lnam=input('enter the ticket holder last name:')
        date1=input('enter travel date(dd):')
        date2=input('enter travel month(mm):')
        date3=input('enter travel year(yyyy):')
        tdate=date3+"-"+date2+"-"+date1
        s1="delete from railway where fname='{}' and lname='{}' and datefd='{}'".format(fnam,lnam,tdate)
        cursor.execute(s1)
        print('TICKET CANCELLED')
    elif ch==2:
        print('THANK YOU')
    else:
        print('ERROR 404:PAGE NOT FOUND')

def delete_account():
    a=input('USER NAME:')
    b=input('PASS WORD:')
    c=input('FIRST NAME:')
    try:
        s1="select fname,lname from useraccount where username='{}'".format(a)
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)
        if data[0]==c:
            print('IS THIS YOUR ACCOUNT')
            c1="select fname,lname from useraccount where username='{}'".format(a)
            cursor.execute(c1)
            data1=cursor.fetchall()[0]
            data1=list(data1)
            data1=data1[0]+' '+data1[1]
            s1="select password from useraccount where username='{}'".format(a)
            cursor.execute(s1)
            data=cursor.fetchall()[0]
            data=list(data)
            if data[0]==b:
                x=['FIRST NAME','LAST NAME','PHONE NUMBER','GENDER','DATE OF BIRTH','AGE']
                s1="select fname,lname,phno,gender,dob,age from useraccount where username='{}'".format(a)
                cursor.execute(s1)
                data=cursor.fetchall()[0]
                data=list(data)
                print(x[0],':::',data[0])
                print(x[1],':::',data[1])
                print(x[2],':::',data[2])
                print(x[3],':::',data[3])
                print(x[4],':::',data[4])
                print(x[5],':::',data[5])
                print('1.yes')
                print('2.no')
                vi=int(input('enter your choice:'))
                if vi==1:
                    b1="delete from useraccount where username = '{}'".format(a)
                    cursor.execute(b1)
                    return True
                elif vi==2:
                    print('SORRY,RETRY')
                else:
                    print('ERROR 404:PAGE NOT FOUND')
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')

def sign_up():
    f=input("FIRST NAME:")
    l=input("LAST NAME:")
    a=input('USER NAME:')
    b=input('PASS WORD:')
    c=input('RE-ENTER YOUR PASS WORD:')
    if b==c:
        ph=input("PHONE NUMBER:")
        print(' M=MALE','\n','F=FEMALE','\n','N=NOT TO MENTION')
        gen=input('ENTER YOUR GENDER M/F/N:')
        while True:
            if gen in ("M","F","N","m","f","n"):
                break
            else:
                print("Error enter again")
                gen=input('enter your gender M/F/N:')
        v=gen.upper()
        print("ENTER YOR DATE OF BIRTH")
        d=input("DD:")
        o=input("MM:")
        p=input("YYYY:")
        dob=p+'-'+o+'-'+d
        age=input('YOUR AGE:')
        
        try:
            c1="insert into useraccount values('{}','{}','{}','{}','{}','{}','{}','{}')".format(f,l,a,b,ph,v,dob,age)
            cursor.execute(c1)
            print('WELCOME',f,l)
            return True
        except:
            print('USERNAME ALREADY EXISTS')
            return False
    else:
        print('BOTH PASSWORDS ARE NOT MATCHING')
def sign_in():
    a=input('USER NAME:')
    b=input('PASS WORD:')
    c=input('FIRST NAME:')
    try:
        s1="select fname from useraccount where username='{}'".format(a)
        c1="select fname,lname from useraccount where username='{}'".format(a)
        cursor.execute(c1)
        data1=cursor.fetchall()[0]
        data1=list(data1)
        data1=data1[0]+' '+data1[1]
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)[0]
        if data==c:
            print(' HII ',data1)
            return True
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')
        
def account_details():
    a=input('USER NAME:')
    b=input('PASS WORD:')
    try:
        s1="select password from useraccount where username='{}'".format(a)
        c1="select fname,lname from useraccount where username='{}'".format(a)
        cursor.execute(c1)
        data1=cursor.fetchall()[0]
        data1=list(data1)
        data1=data1[0]+' '+data1[1]
        print(data1)
        cursor.execute(s1)
        data=cursor.fetchone()[0]
        if data==b:
            x=['FIRST NAME','LAST NAME','PHONE NUMBER','GENDER','DATE OF BIRTH','AGE']
            s1="select fname,lname,phno,gender,dob,age from useraccount where username='{}'".format(a)
            cursor.execute(s1)
            data=cursor.fetchall()[0]
            data=list(data)
            print(x[0],':::',data[0])
            print(x[1],':::',data[1])
            print(x[2],':::',data[2])
            print(x[3],':::',data[3])
            print(x[4],':::',data[4])
            print(x[5],':::',data[5])
            return True


        else:
            print("password doesn't match")
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')
        
hostname=input("Enter the host type:")
username=input("Enter the username:")
pswd=input("Enter the password:")
databasename=input("Enter the name of database:"
connectivity()       
menu()




 
