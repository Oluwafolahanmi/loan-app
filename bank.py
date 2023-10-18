import random
import time

class Bank():
    def __init__(self):
        self.adm_password = 123456
        self.user_info = {
            32136882:["Bukunmi", "Adeola", "bk123", 5000], 
            32136135:["Shewa", "Adeniyi", "shew90", 200000], 
            32134809: ["Sodeeq", "Money", "sosotakemypain", 10000000000000000]}
        self.user_acct = 1
        # self.homePage()

    def homePage(self):
        user_decision = input("You are welcome to Natha bank. Which of the following operation would you like to perform?:\n1. Login \n2.Register \n3. Deposit\nEnter any other key to quit\n")
        if user_decision == "1":
            self.login()
        elif user_decision == "2":
            self.register()
        elif user_decision == "3":
            self.deposit()

    def register(self):
        fName = input("Enter your first name ")
        LName = input("Enter your last name ")
        passw = input("Enter your password ")
        confirmpass = input("Confirm your password ")
        while passw != confirmpass:
            print("Password does not match")
            passw = input("Enter your password ")
            confirmpass = input("Confirm your password ")
        acct_num = random.randrange(32134569, 32139000)
        print(f"{fName} {LName} your registration is successful and your account number is {acct_num}")
        self.user_info.update({acct_num:[fName, LName, passw, 0]})
        time.sleep(1)
        self.login()

    def login(self):
        self.user_acct = int(input("Enter your account number "))
        if self.user_acct in self.user_info.keys():
            user_pass = input("Enter your password ")
            if user_pass == self.user_info[self.user_acct][2]:
                print("Login Successful")
                time.sleep(1)
                self.operation()
            else:
                print("Invalid Password. Try again")
                self.login()
        else:
            decision = input("Account not found. Enter 1 to try again, 2 to register and any other key to go home ")
            if decision == "1":
                self.login()
            elif decision == "2":
                self.register()
            else:
                self.homePage()

    def operation(self):
        decision = input("Which of the following operations would you like to perform?\n1. Check Balance\n2. Transfer \n3. Logout\n")
        if decision == "1":
            self.checkBal()
        elif decision == "2":
            self.transfer()
        else:
            self.homePage()

    def checkBal(self):
        print(f"Dear {self.user_info[self.user_acct][0]}, your account balance is {self.user_info[self.user_acct][3]}")
        time.sleep(2)
        self.operation()

    def transfer(self):
        user_bal = self.user_info[self.user_acct][3]
        recp_acct = int(input("Enter recipient's account number "))
        if recp_acct == self.user_acct:
            print("You can't transfer money to yourself, Thief")
            self.transfer()

        elif recp_acct in self.user_info.keys():
            print(f"You are about to transfer to {self.user_info[recp_acct][0]} {self.user_info[recp_acct][1]}")
            amount = int(input("Enter the amount you want to transfer "))
            while amount > user_bal:
                print(f"You don't have sufficient balance. Enter amount that is lower or equal to your balance: {user_bal}")
                amount = int(input("Enter the amount you want to transfer "))
            else:
                new_am = user_bal - amount
                self.user_info[self.user_acct][3] = new_am
                recp_bal = self.user_info[recp_acct][3] + amount
                self.user_info[recp_acct][3] = recp_bal
                print("Transfer successful")
                try_again = input("Enter 1 to try again and any other key to go home ")
                if try_again == "1":
                    self.transfer()
                else:
                    self.operation()
        else:
            print("Account not found. Try again")
            self.transfer()

    def deposit(self):
        acct_num = int(input("account number: "))
        if acct_num in self.user_info.keys():
            print("account name: ", (self.user_info[acct_num][0]), " ", (self.user_info[acct_num][1]))
            amount = int(input("Amount: "))
            pword = int(input("administrative password: "))
            if pword == self.adm_password:
                self.user_info[acct_num][3] = (self.user_info[acct_num][3]) + amount
                print("transaction successful. recipient have been credited with the sum of #", amount)
                self.operation()
            else:
                print("Access denied!\n**********\n")
                self.homePage()
        else:
            print("User not found\n**********\n")
            self.homePage()
# Bank()
class bet(Bank):
    def __init__(self):
        Bank.__init__(self)
        self.user_info = {
            3213:["Bukunmi", "Adeola", "bk123", 5000], 
            3216:["Shewa", "Adeniyi", "shew90", 200000], 
            3214: ["Sodeeq", "Money", "sosotakemypain", 10000000000000000]}
        self.stake = 0
        self.win = 0
        self.homePage1()

    def homePage1(self):
        print("welcome to Fola betting app")
        self.user_decision = input("\n1. Login \n2.Register \nEnter any other key to quit\n")
        if self.user_decision == "1":
            self.login()
        elif self.user_decision == "2":
            self.register1()

    def register1(self):
        self.fName = input("Enter your first name ")
        self.LName = input("Enter your last name ")
        self.passw = input("Enter your password ")
        self.confirmpass = input("Confirm your password ")
        while self.passw != self.confirmpass:
            print("Password does not match")
            self.passw = input("Enter your password ")
            self.confirmpass = input("Confirm your password ")
        self.acct_num = random.randrange(1000, 2000)
        print(f"{self.fName} {self.LName} your registration is successful and your account identification number is {self.acct_num}")
        self.user_info.update({self.acct_num:[self.fName, self.LName, self.passw, 0]})
        time.sleep(1)
        self.login() 

    def homePage1(self):
        self.user_decision = input("\n1. Login \n2.Register \nEnter any other key to quit\n")
        if self.user_decision == "1":
            self.login()
        elif self.user_decision == "2":
            self.register1()
    
    def operation1(self):
        self.decision = input("\n1. Check Balance   2. Deposit    3. Play game    4. Logout\n: ")
        if self.decision == "1":
            self.checkBal()
        elif self.decision == "2":
            self.deposit1()
        elif self.decision == "3":
            self.game()
        else:
            self.homePage1()

    def deposit1(self):
        self.acct_num = int(input("ID number: "))
        if self.acct_num == self.user_acct:
            self.amount = int(input("Amount: "))
            if self.amount > 100000:
                print("Deposit limit exceeded")
                self.amount = int(input("Amount: "))
            self.pword = input("password: ")
            if self.pword == self.user_info[self.acct_num][2]:
                self.user_info[self.acct_num][3] = (self.user_info[self.acct_num][3]) + self.amount
                print("transaction successful. You have been credited with the sum of #", self.amount)
                print("Your balance is ",(self.user_info[self.acct_num][3]) )
                self.operation1()
            else:
                print("invalid password!\n**********\n")
                self.operation1()
        else:
            print("invalid details\n**********\n")
            self.operation1()

    def stake1(self):
        self.stake = int(input("amount to stake: #"))
        if self.stake > self.user_info[self.user_acct][3]:
            print("insufficient balance")
            ask = input("1. Fund account \n2. Homepage")
            if ask == "1":
                self.deposit1()
            else:
                self.operation1()
        else:
            self.staked()

    def staked(self):
        self.user_info[self.user_acct][3] = (self.user_info[self.user_acct][3]) - self.stake
        print("You have staked #", self.stake, "your balance is #", self.user_info[self.user_acct][3])
        self.colors = ["blue", "green", "yellow", "white", "black", "red", "purple", "orange", "brown", "cream", "grey", "navy"]
        self.comp = set()
        self.use = set()
        for i in range(3):
            i = random.choice(self.colors)
            self.comp.add(i)
        self.g1 = input("first color: ").lower()
        self.g2 = input("second color: ").lower()
        self.g3 = input("third color: ").lower()
        self.use.add(self.g1)
        self.use.add(self.g2)
        self.use.add(self.g3)
        self.fin = self.use.intersection(self.comp)
        # if g1 in comp and g2 in comp and g3 in comp:
        if len(self.fin) == 3:
            self.win = self.stake * 8
            print("you guessed 3 colors right. computer guessed ", self.comp)
            self.win1()
        # elif (g1 in comp and g2 in comp) or (g1 in comp and g3 in comp) or (g2 in comp and  g3 in comp):
        elif len(self.fin) == 2:
            print("you guessed two colors right. computer guessed ", self.comp)
            self.win = self.stake * 4
            self.win1()
        # elif g1 in comp or g2 in comp or g3 in comp:
        elif len(self.fin) == 1:
            print("you guessed one color right. computer guessed ", self.comp)
            self.win = self.stake * 2
            self.win1()
        else:
            self.win = 0
            print("you guessed no colors right. computer guessed ", self.comp)
            self.win1()

    def win1(self):
        self.user_info[self.user_acct][3] = (self.user_info[self.user_acct][3]) +self.win
        print("you won #", self.win, ". new balance is #", self.user_info[self.user_acct][3]) 
        self.try_again = input("1. Try again \n2. homepage \n: ") 
        if self.try_again == "1":
            self.stake1()  
        else:
            self.operation1()

    def game(self):
        print("""Welcome to betting game. The computer will generate 3 random colors, the user will be asked to guess the colors. The user will stake an amount for
            each round, if one color is guessed correctly, user wins double of stake, if two, stake *4, if the three guesses are correct, stake *8. In the absence of a correct guess,
            user loses stake""")
        self.decision = input("1. proceed \n2. Homepage \n: ")
        if self.decision == "1":
                self.stake1()
        else:
            self.operation1()

fa = bet()
fa