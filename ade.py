# def sum(a, b):
#     if a < b:
#         sum = a + b
#         print(sum)
#     else:
#         return False
    
# sum(5, 7)
# print(sum(2, 4))


# name = "3436tyt2"
# if name.isdigit():
#     print("valid number")
# else:
#     print("imputs must contain digits alone")
#     print(name)
    

# a = []
# b = 20
# c = 30
# d = 40
# a.append(b)
# a.append(c)
# a.append(d)
# print(a)
# def ret(g):
#     g += 1
#     inp = input("stop? yes or no : ")
#     if inp == "yes": 
#         p = input("rock, paper or scissors: ")
# import random
# nam = input("enter your name: ")
# sef = ["rock", "paper", "scissors"]
# d = random.choice(sef)
# p = input("rock, paper or scissors: ")
# print(d)
# f = 0
# g = 0
# while True:
#     if d == "rock" and p == "paper":
#         print(f"{nam} won")
#         g += 1
#         inp = input("stop? yes or no : ")
#         if inp == "yes":
#             break
#         else:
#             p = input("rock, paper or scissors: ")
#     elif d == "rock" and p == "scissors":
#         print(f"computer won")
#         f += 1
#         inp = input("stop? yes or no : ")
#         if inp == "yes":
#             break
#         else:
#             p = input("rock, paper or scissors: ")
#     elif d == "paper" and p == "rock":
#         print(f"computer won")
#         f += 1
#         inp = input("stop? yes or no : ")
#         if inp == "yes":
#             break
#         else:
#             p = input("rock, paper or scissors: ")
#     elif d == "paper" and p == "scissors":
#         print(f"{nam} won")
#         g += 1
#         inp = input("stop? yes or no : ")
#         if inp == "yes":
#             break
#         else:
#             p = input("rock, paper or scissors: ")
#     elif d == "scissors" and p == "paper":
#         print(f"computer won")
#         f += 1
#         inp = input("stop? yes or no : ")
#         if inp == "no":
#             break
#         else:
#             p = input("rock, paper or scissors: ")
#     elif d == "scissors" and p == "rock":
#         print(f"{nam} won")
#         g += 1
#         inp = input("stop? yes or no : ")
#         if inp == "yes":
#             break
#         else:
#             p = input("rock, paper or scissors: ")
#     elif (d == "paper" and p == "paper") or (d == "rock" and p == "rock") or (d == "scissors" and p == "scissors"):
#         print("its a draw")
#         inp = input("stop? yes or no : ")
#         if inp == "yes":
#             break
#         else:
#             p = input("rock, paper or scissors: ")
#     #     else:
#     #         p = input("rock, paper or scissors: ")
# if d > p:
#     print(f"computer = {f} , {nam} = {g}. computer won")
# else:
#     print(f"computer = {f} , {nam} = {g}. {nam} won")


# def display(course, *courses):
#     for i in courses
#         print(i)

# a = "maya"
# b = ["dave", "micheal"]
# display(a, b) 


def add(a, b):
    sum = a + b
    return sum


# def sum(a, b):
#     sum = a + b
#     print(sum)

# a = 21
# if 20 > a:
#     add(10, 20)
# elif  a == 21:
#     sum(10, 20)

# g = input("ehat is your name")
# print(g)
# set1 = ran(set1)
def ran(a):
    for i in range(3):
        a = set()
        user  = input("enter a number: ")
        a.add(user)
        print(a)

ran(set1)

# def set1():
#     print("this progrm collects three sets of numbers from the user and perform set functi0ons on them")

#     ran(set1)
#     ran(set2)
#     ran(set3)

#     print("Your 3 sets of numbers are: ")
#     print(set1)
#     print(set2)
#     print(set3)
#     op = input("""which of the following operations will you like to perform? 
#             1. Union
#             2. Intersection
#             3. Symmetric Different Update
#             4. Isdisjoint
#             :    """)
#     if op == "1":
#         set4 = set1.union(set2).union(set3)
#         print(set4)
#     elif op == "2":
#         set4 = set1.intersection(set2).intersection(set3)
#         print(set4)
#     elif op == "3":
#         set4 = set1.symmetric_difference_update(set2)
#         # set5 = sett3.symmetric_difference_update(set4)
#         print(set4)
#     elif op == "4":
#         set4 = set1.isdisjoint(set2)
#         # set5 = sett3.isdisjoint(set4)
#         print(set4)
#     else:
#         print("Your input does not match the available options")
#         print(op)

# set1()