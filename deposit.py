# import time

# class All:
#     def __init__(self):
#         self.user = input("enter your name: ")
#         self.password = input("enter your name: ")
#         self.d = ""
#         self.login()

#     def login(self):
#         self.d = input(": ")
#         if self.user == "Ola" and self.password == "1234":
#             # print(d)
#             self.greeting()
#         else:
#             print("invalid")
#             self.login()

#     def greeting(self):
#         print(self.d)
#         print("welcome")
# All()
# import random
# j, k, f= ["a", "b", "c"], random.randint(23, 100), [2, 3]
# # k = 23
# # f = [2, 3]
# j.append(k); j.extend(f); j = tuple(j)

# print(j)

# x = 2
# if x != 2: 
#     print("b"); else: print("a")
# ept = ["Frontend eng", "Backend eng", "UI/UX", "Data analysis", "Data science", "Project mgt", "Graphics design"]
# a=0
# for i in ept:
#     print(str(a+1)+". "+i)
#     a+=1

# import random
# b = str(random.randint(0, 10))
# details, voterId, detail, det = ["First name: ", "Last name: ", "Gender: ", "Phone number: ", "department: ", "Password: ", "Confirm password: "], (str(random.randint(1234567898765432, 3000000000000000))+b+b+b+b), [], [0, 0, 0, 0, 0, 0]
# for i in details:
#     if i == "department: ":
#         print("department: ")
#         dept = ["Frontend eng", "Backend eng", "UI/UX", "Data analysis", "Data science", "Project mgt", "Graphics design"]; ab = 0
#         for i in dept:
#             print(str(ab+1)+". "+i)
#             ab+=1
#         decision = int(input(">>>>> "))
#         k = dept[decision-1]
#         detail.append(k)
#     else:     
#         k = input(i)
#         detail.append(k)
# print(detail)

k = ("a", "b", "c", "a", "a")
b = max(k, key = k.count)
print(b)