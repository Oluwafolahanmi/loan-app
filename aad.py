print("you are to register for this exam first, then proceed to login with your registered details.")
name = [] 
stuid = []
scores = []
named = []
iden = []
v = 0
while v < 2:
    namee = input("enter your name: ")
    stud = input("enter your student ID: ")
    name.append(namee)
    stuid.append(stud)
    print("congratulations", namee, ". You have successfully registered for this test. Tests start as soon as registration is complete")
    v += 1
print("proceed to login to take test")
v = 0
b = int(input("how many students will take this test: "))
while v < b:
    print("\n\nlogin to take your test")
    nam  = input("Name: ")
    id = input("id: ")
    named.append(nam)
    iden.append(id)
    if nam in name:
        if id in stuid:
            print("welcome", nam)
            print("""Read the instructions carefully. This test contains five 
#       multiple-choice questions. Every correctly answered question 
#       adds 10 marks while wrong answers removes 5 marks from your score.
#       select your answers using the prefix for the option ie 1, 2, 3, 4 
#       Good luck""")
            que = ["How many infinity stones are there?", "What is the only food that cannot go bad?", "What is the most visited Tourist attraction in the world",
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
            scores.append(d)
            v += 1
            # print("The next student can take their test now")
        else:
            print("invalid id")
            id = input("try again: ")
        
    else:
        print("student details not registered")
        break
    
k = scores.index(max(scores))
h = named[k]
f = iden[k]
l = max(scores)
print("the maximum score is ", l, "by ", h, "with registration number", f )


    


        

# print("""Read the instructions carefully. This test contains five 
#       multiple-choice questions. Every correctly answered question 
#       adds 10 marks while wrong answers removes 5 marks from your score.
#       select your answers using the prefix for the option ie 1, 2, 3, 4 
#       Good luck""")
# totalscore = 50
# a = 0
# b = 0
# q1 = input("""How many infinity stones are there?
#            1. 3
#            2. 5
#            3. 6
#            4. 10
#            : """)
# while True:
#     if q1 == "3":
#         a = a + 10
#         b+=1 
#         # print(a)
#         break
#     elif q1 == "1" or q1 == "2" or q1 == "4":
#         a = a - 5
#         print("Wrong, the correct answer is '6'")
#         break
#     else:
#         print("please select from the options provided")
#         q1 = input("""How many infinity stones are there?
#            1. 3
#            2. 5
#            3. 6
#            4. 10
#            : """)

# q2 = input("""What is the only food that cannot go bad?
#            1. Dark chocolate
#            2. Peanut butter
#            3. Canned tuna
#            4. Honey
#            :  """)
# while True:
#     if q2 == "4":
#         a = a + 10
#         b+=1
#         # print(a)
#         break
#     elif q2 == "1" or q2 == "2" or q2 == "3":
#         a = a - 5
#         print("Wrong, the correct answer is 'Honey'")
#         break
#     else:
#         print("please select from the options provided")
#         q2 = input("""What is the only food that cannot go bad?
#            1. Dark chocolate
#            2. Peanut butter
#            3. Canned tuna
#            4. Honey
#            :  """)

# q3 = input("""What is the most visited Tourist attraction in the world
#            1. Eiffel Tower
#            2. Statue of Liberty
#            3. Great Wall of China
#            4. Colosseum
#            :  """)
# while True:
#     if q3 == "1":
#         a = a + 10
#         b+=1
#         break
#     elif q3 == "2" or q3 =="3" or q3 == "4": 
#         a = a - 5
#         print("Wrong, the correct answer is 'Eiffel Tower'")
#         break
#     else:
#         print("please select from the options provided")
#         q3 = input("""What is the most visited Tourist attraction in the world
#            1. Eiffel Tower
#            2. Statue of Liberty
#            3. Great Wall of China
#            4. Colosseum
#            :  """)

# q4 = input("""Which is the heaviest organ in the human body?
#            1.  Brain
#            2. Liver
#            3. skin
#            4. Heart
#            :   """)
# while True:
#     if q4 == "2":
#         a = a + 10
#         b+=1
#         break
#     elif q4 == "1" or q4 =="3" or q4 == "4": 
#         a = a - 5
#         print("Wrong, the correct answer is 'Liver'")
#         break
#     else:
#         print("please select from the options provided")
#         q4 = input("""Which is the heaviest organ in the human body?
#            1.  Brain
#            2. Liver
#            3. skin
#            4. Heart
#            :   """)

# q5 = input("""Who made the third most 3-pointers in the Playoffs in NBA history?
#            1. Kevin Durant
#            2. JJ Redick
#            3. Lebron James
#            4. Kyle Korver
#            :  """)
# while True:
#     if q5 == "3":
#         a = a + 10
#         b+=1
#         break
#     elif q5 == "1" or q5 =="2" or q5 == "4": 
#         a = a - 5
#         print("Wrong, the correct answer is 'Lebron James'")
#         break
#     else:
#         print("please select from the options provided")
#         q5 = input("""Who made the third most 3-pointers in the Playoffs in NBA history?
#            1. Kevin Durant
#            2. JJ Redick
#            3. Lebron James
#            4. Kyle Korver
#            :  """)

# print(f"You got {b} questions correct. your score is {a} out of {totalscore}")
# if a > 40:
#     print("your grade is A")
# elif a > 30 and a < 40:
#     print("your grade is B")
# elif a > 20 and a < 30:
#     print("your grade is C")
# elif a > 10 and a < 20  :
#     print("your grade is E")
# else:
#     print("your grade is F")