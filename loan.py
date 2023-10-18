import mysql.connector as connection
import random
import time
adminid = 123456
password = "password"
mydb = connection.connect(host="127.0.0.1", user = "root", password = "Ademola.1234", database = "mydatabase")
mycursor = mydb.cursor()
# mycursor.execute("CREATE  TABLE member (sn INT PRIMARY KEY AUTO_INCREMENT, fname CHAR(55), lname CHAR(30), phone_no VARCHAR(11), gender CHAR(10), State_of_origin CHAR(100), Address VARCHAR(200), password VARCHAR(20), member_id INT, active_loan INT, account_bal INT, count INT)")
# mycursor.execute("CREATE TABLE Non-menmer(Sn INT PRIMARY KEY AUTO_INCREMENT, fname CHAR(55), lname CHAR(30), gender CHAR(10), phoneNum VARCHAR(11), password VARCHAR(20), activeloan INT)")
# mycursor.execute("CREATE TABLE ADMIN(id INT PRIMARY KEY, password VARCHAR(20), balance INT)")
# mycursor.execute("INSERT INTO ADMIN (id, password, balance) VALUES (123456, 'password', 5000000)"); mydb.commit()
# mycursor.execute("DROP TABLE ADMIN")
def start():
    print("YAWOYAWO COOPERATIVE")
    decision = input("\n1. MEMBERS       2. NON MEMBERS    \n>>>>> ")
    if decision == "1":
        members()
    else:
        nonmembers()

def members() :
    decision = input("\n1. REGISTER      2. LOGIN      3.  RETURN  \n>>>> ")
    if decision == "1":
        reg()
    elif decision == "2":
        login()
    else:
        start()  
def reg(): 
    print("\nRegister for this program")
    details, memId, detail, det = ["First name: ", "Last name: ", "Phone number: ", "Gender: ", "State of origin: ", "Address: ", "Password: ", "Confirm password: "], random.randint(2000, 3000), [], [0, 0, 0]
    for i in details:
        k = input(i); detail.append(k)
    while True:
        if detail[6] != detail[7]:
            print("password does not match"); b = input("confirm password: "); detail[7] = b
        else:
            break
    print("congratulations", detail[0], detail[1], "You have successfully registered for this program. Your member Id is", memId)
    detail[7] = memId; detail.extend(det); detail = tuple(detail)
    querry = "INSERT INTO member (fname, lname, phone_no, gender, State_of_origin, Address, password,  member_id, active_loan, account_bal, count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(querry, detail); mydb.commit()
    login()
def fetch():
    sq = f"SELECT * FROM member WHERE member_id = {Id}"; mycursor.execute(sq); global details; details = mycursor.fetchone();  details
def login():
    print("\nLOGIN")
    print("\nwelcome to login")
    global Id
    Id  = int(input("member Id: "))
    fetch()
    if details != None:
        password = input("password: ")
        if password == details[7]:
            print("welcome", details[1], details[2])
            homepage()
        else:
            print("invalid id. try again")
            login()
    else:
        print("User details not found")
        start()
def homepage():
    fetch(); print(f"\nAccount balance = {details[10]}"); decision = input("\n1. DEPOSIT       2. ACTIVE LOAN    3. RETURN \n>>> ")
    sql1 = "SELECT * FROM ADMIN WHERE id = 123456"; mycursor.execute(sql1); detail = mycursor.fetchone()
    if decision =="1":
        if details[9] != 0:
            decision = input("you have an active loan. will you like to pay it first: yes or no : ")
            if decision == "yes":
                repay()
            else:
                trydep = 0; print("1%\ interest on every deposit."); deposit()
                newval = details[10] + amount + (0.01 * amount); sql = "UPDATE member SET account_bal = %s WHERE member_id = %s"; get = (newval, Id)
                mycursor.execute(sql, get); mydb.commit(); fetch(); trydep += 1; sql = "UPDATE member SET count = %s WHERE member_id = %s"; get = (trydep, Id)
                mycursor.execute(sql, get); newval = detail[2] + amount + (0.01*amount); sql = "UPDATE ADMIN SET balance = %s id = 123456"
                mycursor.execute(sql, (newval, )); mydb.commit(); fetch(); print(f"transaction successful."); homepage()
        else:
            trydep = 0; print("1%/ interest on every deposit."); deposit(); newval = details[10] + amount + (0.01 * amount)
            sql = "UPDATE member SET account_bal = %s WHERE member_id = %s"; get = (newval, Id); mycursor.execute(sql, get); newval = detail[2] + amount + (0.01 * amount)
            sql = "UPDATE ADMIN SET balance = %s WHERE id = 123456"; mycursor.execute(sql, (newval, )); mydb.commit(); fetch(); trydep += 1
            sql = "UPDATE member SET count = %s WHERE member_id = %s"; get = (trydep, Id); mycursor.execute(sql, get); mydb.commit(); fetch()
            print(f"transaction successful. New balance = {details[10]}"); homepage()
    elif decision == "2":
        if details[9] == 0:
            print("You have no active loan")
        else:
            print(f"Active loan: {details[9]}")
        decision = input("\n 1. TAKE LOAN      2. REPAY LOAN    3. RETURN  >>> ")
        if decision == "1":
            loan()
        elif decision == "2":
            repay()
        else:
            homepage()
    else:   
        members()
def deposit():
    global amount; amount = int(input("Amount: "))
    while True:
        if amount > 1000000:
            print("Limit exceeded. Limit is #1,000,000")
            amount = input("Amount: ")
        else:
            break
    password = input("Password: ")
    while True:
        if password != details[7]:
            print("incorrect password")
            password = input("Password: ")
        else:
            break
def repay():
    if details[9] < 1:
        print("You have no active loan"); homepage()
    else: 
        decision = input("\n1. PAY FROM BALANCE      2. DIRECT DEPOSIT   3.  \n>>>"); sql1 = "SELECT * FROM ADMIN WHERE id = 123456"; mycursor.execute(sql1); detail = mycursor.fetchone()
        if decision == "1":
            amt = int(input("Amount: "))
            while True:
                if amt > details[10]:
                    print("insufficient fund"); amt = int(input("Amount: "))
                elif amt > details[9]:
                    print("payment exceed active loan."); amt = int(input("Amount: "))
                else:
                    newval = details[10] - amt; sql = "UPDATE member SET account_bal = %s WHERE member_id = %s"; get = (newval, Id); mycursor.execute(sql, get)
                    fetch(); newval = details[9] - amt; sql = "UPDATE member SET active_loan = %s WHERE member_id = %s"; get = (newval, Id); mycursor.execute(sql, get)
                    newval = detail[2] + amt; sql = "UPDATE ADMIN SET balance = %s WHERE id = 123456"; mycursor.execute(sql, (newval, )); mydb.commit(); fetch()
                    print(f"transaction successful."); homepage()
        elif decision == "2":            
            amt = int(input("Amount: "))
            while True:
                if amt > details[9]:
                    print("payment exceed active loan "); amt = int(input("Amount: "))
                else:
                    newval = details[9] - amt; sql = "UPDATE member SET active_loan = %s WHERE member_id = %s"; get = (newval, Id); mycursor.execute(sql, get)
                    newval = detail[2] + amt; sql = "UPDATE ADMIN SET balance = %s WHERE id = 123456"; mycursor.execute(sql, (newval,)); mydb.commit()
                    fetch(); print(f"transaction successful."); homepage()
        else:
            homepage()
def loan():
    sql1 = "SELECT * FROM ADMIN WHERE id = 123456"; mycursor.execute(sql1); detail = mycursor.fetchone()
    if details[10] > 0:
        print("You are a financial member. Interest rate on your loan is  3%"); deposit(); newval = details[9] + amount + (0.03 * amount); sql = "UPDATE member SET active_loan = %s WHERE member_id = %s"
        get = (newval, Id); mycursor.execute(sql, get); newval = detail[2] - amount; sql = "UPDATE ADMIN SET balance = %s id = 123456"; mycursor.execute(sql, (newval, ))
        mydb.commit(); fetch(); print(f"transaction successful. Active loan = {details[9]}"); homepage()
    else:
        print("You are a non financial member. Interest rate on your loan is 7%"); deposit(); newval = details[9] + amount + (0.07 * amount); sql = "UPDATE member SET active_loan = %s WHERE member_id = %s"
        get = (newval, Id); mycursor.execute(sql, get); newval = detail[2] - amount; sql = "UPDATE ADMIN SET balance = %s id = 123456"; mycursor.execute(sql, (newval, ))
        mydb.commit(); fetch(); print(f"transaction successful. Active loan = {details[9]}"); homepage()
def nonmembers():
    decision = input("\n1. TAKE LOAN       2. REPAY LOAN        3. RETURN     \n>>> ")
    if decision == "1":
        details, memId, detail, det = ["First name: ", "Last name: ", "Phone number: ", "Gender: ", "State of origin: ", "Address: ", "Password: ", "Confirm password: "], random.randint(2000, 3000), [], [0, 0, 0]
        for i in details:
            k = input(i); detail.append(k)
        while True:
            if detail[6] != detail[7]:
                print("password does not match"); b = input("confirm password: "); detail[7] = b
            else:
                break
        # print("congratulations", detail[0], detail[1], "You have successfully registered for this program. Your member Id is", memId)
        detail[7] = memId; detail.extend(det); detail = tuple(detail)
        querry = "INSERT INTO member (fname, lname, phone_no, gender, State_of_origin, Address, password,  member_id, active_loan, account_bal, count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(querry, detail); mydb.commit()
        print("interest rate for nonmembers is 10%")
        deposit()
        newval = details[9] + amount + (0.1 * amount); sql = "UPDATE member SET active_loan = %s WHERE member_id = %s"; get = (newval, Id); mycursor.execute(sql, get)
        mydb.commit(); fetch(); print(f"transaction successful. Active loan = {details[9]}")
    elif decision =="2":
        if details[9] < 1:
            print("You have no active loan"); start()
        else:
            amt = int(input("Amount: "))
            while True:
                if amt > details[9]:
                    print("payment exceed active loan "); amt = int(input("Amount: "))
                else:
                    newval = details[9] - amt; sql = "UPDATE member SET active_loan = %s WHERE member_id = %s"; get = (newval, Id); mycursor.execute(sql, get)
                    mydb.commit(); fetch(); print(f"transaction successful.")
                    break
            if details[9] == 0:

                    start()
        
def admin():
    sql = "SELECT * FROM ADMIN WHERE id = 123456"; mycursor.execute(sql); detail = mycursor.fetchone()
    # print(details)    
    det = int(input("Admin id: ")); passw = input("Admin password: ")
    while True:
        if det != detail[0] or passw != detail[1]:
            print("wrong details"); det = input("Admin id: "); passw = input("Admin password: ")
        else:
            print(f"coop balance = {detail[2]}"); decision = input("\n1. Check detail    2. Quit      \n>>> ")
            if decision == "1":
                Id = int(input("user id: ")); sq = f"SELECT * FROM member WHERE member_id = {Id}"; mycursor.execute(sq); details = mycursor.fetchone()
                if details != None:
                    print(f"\nName: {details[1]} {details[2]}  \nActive loan: {details[9]}  \nAccount balance: {details[10]}\n");  time.sleep(2)
                break

        
# admin()
# reg()
login()