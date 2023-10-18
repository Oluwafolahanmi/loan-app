name = [] 
stuid = []
named = []
iden = []
user_score = {}
user_id = {}

def reg():
    global namee
    print("\nRegister for this program")
    namee = input("enter your name: ")
    stud = input("enter your student ID: ")
    name.append(namee)
    stuid.append(stud)
    user_id.update({namee:stud})
    print("congratulations", namee, ". You have successfully registered for this program")
    put = input("Do you want to register another student? yes or no: ")
    if put == "yes":
        reg()
    elif put == "no":
        login()
def login():
    print("\nLOGIN")
    print("\nwelcome to login")
    nam  = input("Name: ")
    id = input("id: ")
    named.append(nam)
    iden.append(id)
    if nam in name:
        if id in stuid:
            print("welcome", nam)
            oper()
        else:
            print("invalid id. try again")
            login()
        
    else:
        print("student details not registered. try again")
        start()
def calc():
    print("\nThis program takes two numbers from the user and performs arithmetic operation on the numbers")
    var3 = input("""\n1. addition    2. subtraction   3. multiplication    4. division    5. modulus    6. floor\n : """)
    var1 = float(input("enter first number: "))
    var2 = float(input("enter second number: "))
    add =  var1 + var2
    sub = var1 - var2
    mul = var1 * var2
    div = var1 / var2
    mod = var1 % var2
    flo = var1 // var2

    if var3 == "1":
        print  (add)
    elif var3 == "2":
        print(sub)
    elif var3 == "3":
        print(mul)
    elif var3 == "4":
        print(div)
    elif var3 == "5":
        print(mod)
    elif var3 == "6":
        print("result = ", flo)
def ran(a):
    for i in range(3):
        user  = input("enter a number: ")
        a.add(user)
        print(a)
def test(): 
    que = ["\nHow many infinity stones are there?", "What is the only food that cannot go bad?", "What is the most visited Tourist attraction in the world",
        "Which is the heaviest organ in the human body?", "Who made the third most 3-pointers in the Playoffs in NBA history?" ]
    option = [["1. 3", "2. 5", "3. 6", "4. 10"], ["1. Dark chocolate", "2. Peanut butter", "3. Canned tuna", "4. Honey"], ["1. Eiffel Tower", "2. Statue of Liberty", "3. Great Wall of China", "4. Colosseum"],
            ["1.  Brain", "2. Liver", "3. skin", "4. Heart"], ["1. Kevin Durant", "2. JJ Redick", "3. Lebron James", "4. Kyle Korver"]]
    ansd = ["3", "4", "1", "2", "3"]
    d = 0
    for i in que:
        index = que.index(i)
        print(index + 1, end=". ")
        print(que[index])
        for opt in option[index]:
            print(opt)
        user_ans = input(": ")                
        if user_ans == ansd[index]:
            d += 10
        else:
            d -= 5
            print("The correct answer is option", ansd[index])        
    print("You have successfully completed your test")   
    print("you scored ", d, "out of 50")
    if d < 10:
        print("you have an F")
    elif d >= 10 and d < 20:
        print("you have a D")
    elif d >= 20 and d < 30:
        print("you have a C")
    elif d >= 30 and d < 40:
        print("you have a B")
    else:
        print("you have a Distinction")
    user_score.update({namee:d})
    print("the maximum score is ", {max(user_score.values())}, "by ", {max(user_score, key=user_score.get)}, "with registration number", user_id[namee] )
def set1():
    print("this progrm collects three sets of numbers from the user and perform set functi0ons on them")
    set1 = set()
    set2 = set()
    set3 = set()

    ran(set1)
    ran(set2)
    ran(set3)

    print("Your 3 sets of numbers are: ")
    print(set1)
    print(set2)
    print(set3)
    op = input("""1. Union    2. Intersection    3. Symmetric Different Update    4. Isdisjoint
            :    """)
    if op == "1":
        set4 = set1.union(set2).union(set3)
        print(set4)
    elif op == "2":
        set4 = set1.intersection(set2).intersection(set3)
        print(set4)
    elif op == "3":
        set4 = set1.symmetric_difference_update(set2)
        # set5 = sett3.symmetric_difference_update(set4)
        print(set4)
    elif op == "4":
        set4 = set1.isdisjoint(set2)
        # set5 = sett3.isdisjoint(set4)
        print(set4)
    else:
        print("Your input does not match the available options")
        print(op)
def logout():
    sew = input("\nlogout?. yes or no: ")
    if sew == "yes":
        trad = input("""\n1. Register     2. Login      3. quit: """)
        if trad == "1":
            reg()
        elif trad == "2":
            login()
    elif sew == "no":
        oper()
def oper():
    rit = input("""\n1. Calculation    2. set operation    3. cbt test
            :  """)
    if rit == "1":
        calc()
        yup = input("will you like to perform another operation: ")
        if yup == "yes":
            oper()
        elif yup == "no":
            logout()
        else:
            print("response must be yes or no")
            yup = input("will you like to perform another operation: ")

    elif rit == "2":
        set1()
        yup = input("will you like to perform another operation: ")
        if yup == "yes":
            oper()
        elif yup == "no":
            logout()
        else:
            print("response must be yes or no")
            yup = input("will you like to perform another operation: ")
    elif rit == "3":
        test()
        yup = input("will you like to perform another operation: ")
        while yup != "yes" and yup != "no":
            print("response must be yes or no")
            yup = input("will you like to perform another operation: ")
        else:
            if yup == "yes":
                oper()
            elif yup == "no":
                logout()
    else:
        print("choose from the available options")
        oper()
def start():
    qew = input("\n1. Register     2. Login      3. quit:  ")
    if qew == "1":
        reg()
    elif qew == "2":
        login()

print("Welcome to Fola's program.")
start()