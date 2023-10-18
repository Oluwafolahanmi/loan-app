

print("This program simulate a mobile financial application that run bank transactions")
print("""You are allowed to create an account with any of the following banks
      1. FirstBank
      2. GtBank
      3. UBA""")
bank = input("select a bank to open an account with: ")
while True:
    if bank == "1":
        print(f"welcome to FirstBank of Nigeria. Proceed to create an account with us")
        break
    elif bank == "2":
        print(f"welcome to Guarantee Trust Bank. Proceed to create an account with us")
        break
    elif bank == "3":
        print(f"welcome to UBA. Proceed to create an account with us")
        break
    else:
        print("please select a bank from the provided options")
        bank = input("select a bank to open an account with: ")
user = []
Fname = input("First name: ")
Sname = input("Second name: ")
pword = input("select a four digit password: ")
pword1 = input("confirm your password: ")
user.append(Fname)
user.append(Sname)
while True:
    if pword != pword1:
        pword1 = input("password does not match. try again: ")
    else:
        break
user.append(pword)
phonum = input("Phone number: ")
while True:
    if len(phonum) < 11 or len(phonum) > 11:
        print("phone number must be eleven digits")
        phonum = input("Phone number: ")
    else:
        user.append(phonum)
        print(f"""Congratulations on opening an account with us. Your new account details are as follows;
              Account Name: {Fname} {Sname} 
              Account Number: {phonum[1:]} """)
        break
acc = 0
print("\n\n Login" )
phonumb = input("phone number: ")
paword = input("password: ")
while True:
    if (phonumb != phonum and pword != paword) or (phonumb == phonum and pword != paword) or (phonum != phonumb and pword == paword):
        print("incorrect phone number and password")
        phonumb = input("phone number: ")
        paword = input("password: ")
    else:
        print("welcome ", Fname, ", Enjoy free and seamless banking")
        print("Account Balance = #00")
        while True:
            tran = input("Will you like to perform a transaction? yes or no: ")
            if tran == "no":
                break
            elif tran == "yes":
                oper = input("""Select an operation from the following options
                    1. Deposit
                    2. Transfer
                    3. Buy Airtime
                    4. Buy data
                    5. Pay for Utility
                    :   """)
                if oper == "1":
                    x = 3
                    amount = int(input("amount: # "))
                    sbank = input("Source Bank: ")
                    paword = input("password: ")
                    while x > 0:
                        if pword != paword:
                            paword = input("incorrect password. ", (x - 1), " trials left: ")
                            x -= 1
                            if x == 0:
                                print("sorry! transaction failed")
                        else:
                            acc += amount
                            print("Transaction successful. Account balance: #", acc, ":00k")
                            tran = input("Will you like to perform a transaction? yes or no: ")
                            if tran == "yes":
                                continue
                                print("false")
                            else:
                                print("True")
                elif oper == "2":
                    x = 3
                    amount = int(input("amount: # "))
                    bacc = input("bank: ")
                    input("Account name: ")
                    input("Account number")
                    paword = input("password: ")
                    while x > 0:
                        if pword != paword:
                            paword = print("incorrect password. ", (x - 1), " trials left: ")
                            x -= 1
                            if x == 0:
                                print("sorry! transaction failed")
                        else:
                            if acc < amount:
                                print("sorry, insufficient balance.")
                                break
                            else:
                                acc -= amount
                                print("Transaction successful. Account balance: #", acc, ":00k")
                                tran = input("Will you like to perform a transaction? yes or no: ")  
                elif oper == "3":
                    x = 3
                    amount = int(input("amount: # "))
                    bacc = input("network: ")
                    input("phone number: ")
                    paword = input("password: ")
                    while x > 0:
                        if pword != paword:
                            paword = print("incorrect password. ", (x - 1), " trials left: ")
                            x -= 1
                            if x == 0:
                                print("sorry! transaction failed")
                        else:
                            if acc < amount:
                                print("sorry, insufficient balance.")
                                break
                            else:
                                acc -= amount
                                print("Transaction successful. Account balance: #", acc, ":00k")
                                tran = input("Will you like to perform a transaction? yes or no: ")                                                    
                elif oper == "4":
                    x = 3
                    amount = int(input("amount: # "))
                    bacc = input("network: ")
                    input("phone number: ")
                    paword = input("password: ")
                    while x > 0:
                        if pword != paword:
                            paword = print("incorrect password. ", (x - 1), " trials left: ")
                            x -= 1
                            if x == 0:
                                print("sorry! transaction failed")
                        else:
                            if acc < amount:
                                print("sorry, insufficient balance.")
                                break
                            else:
                                acc -= amount
                                print("Transaction successful. Account balance: #", acc, ":00k")
                                tran = input("Will you like to perform a transaction? yes or no: ")                   
                elif oper == "5":
                    x = 3
                    amount = int(input("amount: # "))
                    bacc = input("network: ")
                    input("phone number: ")
                    paword = input("password: ")
                    while x > 0:
                        if pword != paword:
                            paword = print("incorrect password. ", (x - 1), " trials left: ")
                            x -= 1
                            if x == 0:
                                print("sorry! transaction failed")
                        else:
                            if acc < amount:
                                print("sorry, insufficient balance.")
                                break
                            else:
                                acc -= amount
                                print("Transaction successful. Account balance: #", acc, ":00k")
                                tran = input("Will you like to perform a transaction? yes or no: ")
                else:
                    print("invalid command!")
                    oper = input("""Select an operation from the following options
                    1. Deposit
                    2. Transfer
                    3. Buy Airtime
                    4. Buy data
                    5. Pay for Utility
                    :   """)
        
            else:
                print("Response must be yes or no")
                tran = input("Will you like to perform a transaction? yes or no: ")
            break
        break
                




        




        






 