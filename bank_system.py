import mysql.connector
db = mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
     database="pythondb"
)
mycursor=db.cursor()

name=[]
ballance=[]

def create_account():
    print('----------------------------------------------------------------------------------------')
    print('================================= ACCOUNT CREATION ====================================')
    print('----------------------------------------------------------------------------------------')
    name=input('enter your name : ')
    mobile=input('enetr your mobile number : ')
    account_no=input('enter  6 digit account number : ')
    atm_no=input('enter 3 digit atm number : ')
    pin=input('enter 4 digit pin for ATM : ')
    money=input('How much you can Add Money : ')
    q="insert into account(name,mobile,acc,atm,pin,money) values(%s,%s,%s,%s,%s,%s)"
    value=(name,mobile,account_no,atm_no,pin,money)
    mycursor.execute(q,value)
    db.commit()
    print('----------------------------------------------------------------------------------------')
    print('============================ ACCOUNT CREATE SUCCESSFULL =============================== ')
    print('----------------------------------------------------------------------------------------')
    q2="select id from account where mobile=("+mobile+")"
    mycursor.execute(q2)
    data = mycursor.fetchall()
    for i in data:
        print('your account ID  = ',i)
    print('----------------------------------------------------------------------------------------')
    menu()
def show_accountdetails():
    print('----------------------------------------------------------------------------------------')
    print('================================== ACCOUNT DETAILS =====================================')
    print('----------------------------------------------------------------------------------------')
    a=input('enter your id  : ')
    q="select * from account where id=("+a+")"
    mycursor.execute(q)
    data1 = mycursor.fetchall()
    for i in data1:
        print('----------------------------------------------------------------------------------------')
        print('your account ID =',i[0],end="    ")
        print('your name =',i[1],end="    ")
        print('your mobile number =',i[2],end="    ")
        print('your account number =',i[3],end="    ")
        print('IFSC code  =',i[4],end="    ")
        print('your ATM number =',i[5],end="    ")
        print('your ATM pin =',i[6])
        print('Ballance =',i[7])
        print('----------------------------------------------------------------------------------------')
    menu() 
    
        
def account():
    print('----------------------------------------------------------------------------------------')
    print('================================ ACCOUNT SECTION =======================================')
    print('----------------------------------------------------------------------------------------')
    menu1()
    print('----------------------------------------------------------------------------------------')
    n=int(input('enter your choice : '))
    if n==1:
        create_account()
    elif n==2:
        show_accountdetails()
    elif n==0:
        menu()
    print('----------------------------------------------------------------------------------------')




def cheack_ballance():
    print('----------------------------------------------------------------------------------------')
    print('================================ BALLANCE =======================================')
    print('----------------------------------------------------------------------------------------')
    a=input('enter your ATM number : ')
    q="select name from account where atm=("+a+")"
    mycursor.execute(q)
    data3 = mycursor.fetchone()
    name.append(data3)
    for i in name:
        j=i
    print('----------------------------------------------------------------------------------------')
    print('HELLOW ...',j)
    q2="select money from account where atm=("+a+")"
    mycursor.execute(q2)
    data4 = mycursor.fetchone()
    ballance.append(data4)
    for l in ballance:
        k=l
    print('YOUR BALLANCE : ',k)
    print('----------------------------------------------------------------------------------------')
    
    atm()
    


def withdrowal():
    print('----------------------------------------------------------------------------------------')
    print('================================ WITHDROWAL SECTION =======================================')
    print('----------------------------------------------------------------------------------------')
    a=input('enter your ATM number : ')
    b=input('enter Ammount : ')
    c=input('enter Your ATM pin : ')
    q="select pin from account where atm=("+a+")"
    mycursor.execute(q)
    data5 = mycursor.fetchone()
    q2="select money from account where atm=("+a+")"
    mycursor.execute(q2)
    data6 = mycursor.fetchone()
    for i in data5:
        j=i
    if c==j:
        for i in data6:
            if int(i)>=int(b):
                total=int(i)-int(b)
                q3="update account set money=("+str(total)+") where atm=("+a+") "
                mycursor.execute(q3)
                db.commit()
                print('----------------------------------------------------------------------------------------')
                print('Withdrowal success ..... please collect your case ')
                print('----------------- THANK YOU ---------------------')
                print('----------------------------------------------------------------------------------------')
                atm()
            else:
                print('----------------------------------------------------------------------------------------')
                print(" you don't have sufficient Ballance ")
                print('----------------------------------------------------------------------------------------')
    else:
        print('  WRONG PIN ENTERED .. please enter correct pin ')

def deposite():
    print('----------------------------------------------------------------------------------------')
    print('================================ DEPOSITE SECTION =======================================')
    print('----------------------------------------------------------------------------------------')
    a=input('enter your ATM number : ')
    b=input('enter Ammount : ')
    c=input('enter Your ATM pin : ')
    q="select pin from account where atm=("+a+")"
    mycursor.execute(q)
    data5 = mycursor.fetchone()
    q2="select money from account where atm=("+a+")"
    mycursor.execute(q2)
    data6 = mycursor.fetchone()
    for i in data5:
        j=i
    if c==j:
        for i in data6:
            k=i
        total=int(k)+int(b)
        q3="update account set money=("+str(total)+") where atm=("+a+") "
        mycursor.execute(q3)
        db.commit()
        print('----------------------------------------------------------------------------------------')
        print('------------------------------------- DEPOSITE SUCCESS ------------------------------')
        print('------------------------------------------ THANK YOU ----------------------------------')
        print('----------------------------------------------------------------------------------------')
        menu2()
    else:
        print('  WRONG PIN ENTERED .. please enter correct pin ')

def atm():
    print('----------------------------------------------------------------------------------------')
    print('================================ ATM  SECTION =======================================')
    print('----------------------------------------------------------------------------------------')
    menu2()
    n=int(input('enter your choice : '))
    if n==1:
        cheack_ballance()
    elif n==2:
        withdrowal()
        atm()
    elif n==3:
        deposite()
        atm()
    elif n==0:
        menu1()
        account()
    else:
        print('invalid input pleae enter correct input ')



def section():
    print('----------------------------------------------------------------------------------------')
    n=int(input('enter your choice : '))
    if n==1:
        account()
    elif n==2:
        atm()
    elif n==0:
        print('----------------------------------------------------------------------------------------')
        print('==========================THANK YOU FOR USING THIS APP ================================== ')
        exit
    else:
        print('invalid input pleae enter correct input ')



def menu2():
    print('press 1 for check balance ')
    print('press 2 for withdrowal money ')
    print('press 3 for deposite money  ')
    print('press 0 for exit ')
    

def menu1():
    print('press 1 for create account ')
    print('press 2 for login account ')
    print('press 0 for exit ')
    

def menu():
    print('press 1 for  using account ')
    print('press 2 for using ATM ')
    print('press 0 for exit ')
    section()
menu()
