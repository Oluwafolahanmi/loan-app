import random
import time
user_info = {
    3213:["Bukunmi", "Adeola", "bk123", 5000], 
    3216:["Shewa", "Adeniyi", "shew90", 200000], 
    3214: ["Sodeeq", "Money", "sosotakemypain", 10000000000000000]}
def checkBal():
    print(f"Dear {user_info[user_acct][0]}, your account balance is {user_info[user_acct][3]}")
    time.sleep(2)
    operation()
def register():
    fName = input("Enter your first name ")
    LName = input("Enter your last name ")
    passw = input("Enter your password ")
    confirmpass = input("Confirm your password ")
    while passw != confirmpass:
        print("Password does not match")
        passw = input("Enter your password ")
        confirmpass = input("Confirm your password ")
    acct_num = random.randrange(1000, 2000)
    print(f"{fName} {LName} your registration is successful and your account identification number is {acct_num}")
    user_info.update({acct_num:[fName, LName, passw, 0]})
    time.sleep(1)
    login()
def homePage():
    user_decision = input("\n1. Login \n2.Register \nEnter any other key to quit\n")
    if user_decision == "1":
        login()
    elif user_decision == "2":
        register()
def operation():
    decision = input("\n1. Check Balance   2. Deposit    3. Play game    4. Logout\n: ")
    if decision == "1":
        checkBal()
    elif decision == "2":
        deposit()
    elif decision == "3":
        game()
    else:
        homePage()
def deposit():
    acct_num = int(input("ID number: "))
    if acct_num == user_acct:
        amount = int(input("Amount: "))
        if amount > 100000:
            print("Deposit limit exceeded")
            amount = int(input("Amount: "))
        pword = input("password: ")
        if pword == user_info[acct_num][2]:
            user_info[acct_num][3] = (user_info[acct_num][3]) + amount
            print("transaction successful. You have been credited with the sum of #", amount)
            print("Your balance is ",(user_info[acct_num][3]) )
            operation()
        else:
            print("invalid password!\n**********\n")
            operation()
    else:
        print("invalid details\n**********\n")
        operation()
def login():
    global user_acct
    user_acct = int(input("Enter your id number "))
    if user_acct in user_info.keys():
        user_pass = input("Enter your password ")
        if user_pass == user_info[user_acct][2]:
            print("Login Successful")
            time.sleep(1)
            operation()
        else:
            print("Invalid Password. Try again")
            login()
    else:
        decision = input("User not found. Enter 1 to try again, 2 to register and any other key to go home ")
        if decision == "1":
            login()
        elif decision == "2":
            register()
        else:
            homePage()
def stake1():
    global stake
    stake = int(input("amount to stake: #"))
    if stake > user_info[user_acct][3]:
        print("insufficient balance")
        ask = input("1. Fund account \n2. Homepage")
        if ask == "1":
            deposit()
        else:
            operation()
    else:
        staked()
def win1():
    user_info[user_acct][3] = (user_info[user_acct][3]) + win
    print("you won #", win, ". new balance is #", user_info[user_acct][3]) 
    try_again = input("1. Try again \n2. homepage \n: ") 
    if try_again == "1":
        stake1()  
    else:
        operation()
def staked():
    user_info[user_acct][3] = (user_info[user_acct][3]) - stake
    print("You have staked #", stake, "your balance is #", user_info[user_acct][3])
    colors = ["blue", "green", "yellow", "white", "black", "red", "purple", "orange", "brown", "cream", "grey", "navy"]
    comp = set()
    use = set()
    for i in range(3):
        i = random.choice(colors)
        comp.add(i)
    g1 = input("first color: ").lower()
    g2 = input("second color: ").lower()
    g3 = input("third color: ").lower()
    use.add(g1)
    use.add(g2)
    use.add(g3)
    fin = use.intersection(comp)
    # if g1 in comp and g2 in comp and g3 in comp:
    if len(fin) == 3:
        global win
        win = stake * 8
        print("you guessed 3 colors right. computer guessed ", comp)
        win1()
    # elif (g1 in comp and g2 in comp) or (g1 in comp and g3 in comp) or (g2 in comp and  g3 in comp):
    elif len(fin) == 2:
        print("you guessed two colors right. computer guessed ", comp)
        win = stake * 4
        win1()
    # elif g1 in comp or g2 in comp or g3 in comp:
    elif len(fin) == 1:
        print("you guessed one color right. computer guessed ", comp)
        win = stake * 2
        win1()
    else:
        win = 0
        print("you guessed no colors right. computer guessed ", comp)
        win1()
def game():
    print("""Welcome to betting game. The computer will generate 3 random colors, the user will be asked to guess the colors. The user will stake an amount for
          each round, if one color is guessed correctly, user wins double of stake, if two, stake *4, if the three guesses are correct, stake *8. In the absence of a correct guess,
          user loses stake""")
    decision = input("1. proceed \n2. Homepage \n: ")
    if decision == "1":
            stake1()
    else:
        operation()

homePage()