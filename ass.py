# print("My name is Oluwafolahanmi, i am a boy")
# print("this is a sample assignment")
# print("wahala dey")
# print("wahala no dey") 

# name = "musbau"
# location = "ibadan"
# state="ondo"
# print(f"my name is {name} and i am from {location} in {state} state.")
# defi = float(input("enter a number"))
# sed = float(input("enter a number"))
# tot = sed + defi
# print(tot)

# var = (1, 9)
# print(type(var))
# print("hello \n world")

# print("""
# who are you
# musmus

# """)

# var = range(10,15)
# print(var)
# print(type(result))

# var = 23.4
# newval = int(var)
# print(newval)

# print("This program checks the network of any given phone number belongs to")
# num = input("enter a phone number: ")
# while True:
#     if len(num) < 11 or len(num) > 11:
#         print("The number must contain 11 digits")
#         num = input("enter a phone number: ")
#     else:
#         if (num.startswith("0803") or num.startswith("0806") or num.startswith("0813") or num.startswith("0810") or 
#               num.startswith("0816") or num.startswith("0814") or num.startswith("0903") or num.startswith("0906") or 
#               num.startswith("0703") or num.startswith("0704") or num.startswith("0706") or num.startswith("07025") or 
#               num.startswith("07026")):
#             print("This number is MTN number")
#             break
#         elif (num.startswith("0805") or num.startswith("0807") or num.startswith("0811") or num.startswith("0815") or 
#               num.startswith("0705") or num.startswith("0905")):
#             print("This is a Glo number")
#             break
#         elif (num.startswith("0809") or num.startswith("0817") or num.startswith("0818") or num.startswith("0908") or
#               num.startswith("0909")):
#             print("This is an Etisalat number")
#             break
#         elif (num.startswith("0802") or num.startswith("0808") or num.startswith("0812") or num.startswith("0708") or 
#               num.startswith("0701") or num.startswith("0902") or num.startswith("0901") or num.startswith("0907")):
#                 print("This is an Airtel number")
#                 break
#         else:
#             print("This program is unable to determine the network of this number") 
#             break

 

# print("This program replaces characters in a string\nkindly go through this article;")
pro = ("""
      Punctuality, they say is the soul of business, whatever is what doing 
      at all is what doing well. Classes in SQI is just 2 hrs, Mondays through
      Thursdays. Coming early will let you settled before lectures begins, 
      you will be able to revise what you did yesterday
      Make Punctuality an habit today and see how far it can help you\n""")
# print(pro)
# old = input("what set of characters in the article will you like to replace: ")
# new = input("what will you replace it with: ")
# print(f"""The adjusted article is;\n 
#       {pro.replace(old, new)}""")
# print(pro.split("you")



# questions = ["whats is todays date", "who is sodiq"]
# options = ["a. monday   b. tuesday", "a. boy b. girl"]
# answer = ["a", "b"]

# for i in questions:
#     index = questions.index(i)
#     print(index + 1, end=". ")
#     print(questions[index])
#     print(options[index])
#     user_ans = input(": ")

# name = ["welcome", "to", "monday"]
# for i in name:
#     print(i, end=" ")

# set
# a set is a collection of characters which is unordered and unindexed  

# name = {"toy", "ade", "segun"}
# # print(name)
# name1 = {"will","case", "tint"}
# name2 = ["sodiq", "victor"]
# name.add("grace")
# # print(name)
# # name.update(name2) to add to a set
# # name .discard()  to remove a literal from a set
# name2.extend(name1)
# # print(name2)
# name2.remove("victor")
# print(name2)

# name = "you are a boy"
# # name1 = name.split()
# # print(type(name1))

# for i in name:
#     if i == "u":
#       continue
# print(i)


# # intersection will return the similar values in a compared set 
# set1 = {1, 5, 6, 9, 2, 2, 4, 7}
# set2 = {9, 5, 2, 0, 4}
# set3 = set1.intersection(set2)
# # # print(set1)
# # # print(set2)
# # # print(set3)

# # # union in set will combine set variables without repetition of values
# # set4 = set1.union(set2).union(set3)
# # print(set4)
# set4 = set1.symmetric_difference(set2)  
# print(set1)      
# # returns the values that are not similar
# set1.symmetric_difference_update(set2)
# print(set4)
# print(set1)

# set = ["dele", "giwa", "doyun"]
# se

# print("this progrm collects three sets of numbers from the user and perform set functi0ons on them")
# set1 = []
# set2 = []
# set3 = []

# for i in range(3):
#       user  = input("enter a number: ")
#       set1.append(user)
# sett1 = set(set1)
# print(set(set1))
# for i in range(7):
#       user  = input("enter a number: ")
#       set2.append(user)
# print(set(set2))
# sett2 = set(set2)
# for i in range(5):
#       user  = input("enter a number: ")
#       set3.append(user)
# print(set(set3))
# sett3 = set(set3)

# print("Your 3 sets of numbers are: ")
# print(set(set1))
# print(set(set2))
# print(set(set3))
# op = input("""which of the following operations will you like to perform? 
#            1. Union
#            2. Intersection
#            3. Symmetric Different Update
#            4. Isdisjoint
#            :    """)
# if op == "1":
#       set4 = sett1.union(sett2).union(sett3)
#       print(set4)
# elif op == "2":
#       set4 = sett1.intersection(sett2).intersection(sett3)
#       print(set4)
# elif op == "3":
#       set4 = sett1.symmetric_difference_update(sett2)
#       # set5 = sett3.symmetric_difference_update(set4)
#       print(set4)
# elif op == "4":
#       set4 = sett1.isdisjoint(sett2)
#       # set5 = sett3.isdisjoint(set4)
#       print(set4)
# else:
#       print("Your input does not match the available options")


# print("whatever this is. Just go with the flow")

# phoneBook = {"Tola": "08198929205", "Dele": "08137382928", "Micheal": "09087766543"}
# print(phoneBook)
# user = input("""which of the following operations wwill you like to perform: 
#             1) Adding to the phonebook
#             2) Viewing the phonebook items
#             3) Deleting from the phonebook
#             : """)
# if user == "1":
#     addName = input("Name of the new contact: ").title()
#     addNum = input("phone number: ") 
#     phoneBook[addName] = addNum
#     print(phoneBook)
# elif user == "2":
#     print(phoneBook)
# elif user == "3":
#     addName = input("name of contact to delete: ").title()
#     del phoneBook[addName]
#     print(phoneBook)



# for i in range(2):
#     print(i, end=". ")
#     print("hello ")


# ret = "what are you? "
# print(ret)
# fre = input(ret)
# print(fre)

# print("press *312# to prompt this program. Follow the prompt to purchase data on Fola network")
# fol = input(": ")
# if fol == "*312#":
#      che = input("""1. buy data
#                  2. check data balance
#                  3. streaming bundles
#                  4. data gifting
#                  5. Next
#                  : """)
#      if che == "1":
#           fru = input("""1. daily and weekend
#                       2. 14days
#                       3. night time only
#                       4. weekly
#                       5. monthly
#                       6. next
#                       : """)
#           if fru == "1":
#                ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                else:
#                     print("unrecognized command")
#           elif fru == "2":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           elif fru == "3":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           elif fru == "4":
#                ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                else:
#                     print("unrecognized command")
#           elif fru == "5":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           elif fru == "6":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           else:
#                print("unrecognized command")
#      elif che == "2":
#           fru = input("""1. daily and weekend
#                       2. 14days
#                       3. night time only
#                       4. weekly
#                       5. monthly
#                       6. next
#                       : """)
#           if fru == "1":
#                ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                else:
#                     print("unrecognized command")
#           elif fru == "2":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           elif fru == "3":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           elif fru == "4":
#                ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                else:
#                     print("unrecognized command")
#           elif fru == "5":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           elif fru == "6":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           else:
#                print("unrecognized command")
#      elif che == "3":
#           fru = input("""1. daily and weekend
#                       2. 14days
#                       3. night time only
#                       4. weekly
#                       5. monthly
#                       6. next
#                       : """)
#           if fru == "1":
#                ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                else:
#                     print("unrecognized command")
#           elif fru == "2":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           elif fru == "3":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           elif fru == "4":
#                ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                else:
#                     print("unrecognized command")
#           elif fru == "5":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           elif fru == "6":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           else:
#                print("unrecognized command")
#      elif che == "4":
#           fru = input("""1. daily and weekend
#                       2. 14days
#                       3. night time only
#                       4. weekly
#                       5. monthly
#                       6. next
#                       : """)
#           if fru == "1":
#                ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                else:
#                     print("unrecognized command")
#           elif fru == "2":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           elif fru == "3":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           elif fru == "4":
#                ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                else:
#                     print("unrecognized command")
#           elif fru == "5":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           elif fru == "6":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           else:
#                print("unrecognized command")
#      elif che == "5":
#           fru = input("""1. daily and weekend
#                       2. 14days
#                       3. night time only
#                       4. weekly
#                       5. monthly
#                       6. next
#                       : """)
#           if fru == "1":
#                ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                else:
#                     print("unrecognized command")
#           elif fru == "2":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           elif fru == "3":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           elif fru == "4":
#                ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                else:
#                     print("unrecognized command")
#           elif fru == "5":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           elif fru == "6":
#                 ret = input("""1. daily 50mb
#                            2. daily 100mb+100mb socials
#                            3. daily 650mb
#                            4. daily 300mb+300secs
#                            5. next
#                            : """)
#                 if ret == "1":
#                     toy = input("""buy now @N50 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "2":
#                     toy = input("""buy now @N100 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "3":
#                     toy = input("""buy now @N200 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "4":
#                     toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                     if toy == "1":
#                         print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                     else:
#                          print("sorry, the operation failed! pls try again.")
#                 elif ret == "5":
#                     fred = input("""1. nights and weekend plans
#                                  2. data + social
#                                  3. data + content
#                                  4. daily boomplay data""")
#                     if fred == "1":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "2":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "3":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     elif fred == "4":
#                          toy = input("""buy now @N500 and select your preferred option 
#                                 1. auto-renewal
#                                 2. one-off
#                                 : """)
#                          if toy == "1":
#                               print("you have selected the auto-renew plan. your request is processing, wait for a confirmation sms.")
#                          else:
#                               print("sorry, the operation failed! pls try again.")
#                     else:
#                          print("unrecognized command")
#                 else:
#                     print("unrecognized command")
#           else:
#                print("unrecognized command")
#      else:
#            print("unrecognized command")
# else:
#            print("unrecognized command")


# y = []
# for i in range(20, 0, -1):   
#     y.append(i)
#     print(y)

# y = input("enter a symbol: ")
# for i in range(0, 40, 3):
#     x = i * y
#     z = ("  ")* i
#     print(z + x)
# for i in range(42, 0, -3):
#     x = (i+1) * y
#     print(x)
# for i in range(0, 40, 3):
#     x = (i+1) * y
#     print(x)
# for i in range(42, 0, -3):
#     x = (i+1) * y
#     print(x)
# for i in range(0, 40, 3):
#     x = (i+1) * y
#     print(x)
# for i in range(42, 0, -3):
#     x = (i+1) * y
#     print(x)
# for i in range(10):
#     print(y * 20) 
# for i in range(10):
#     for j in range(10):
#         print(y, end="")
#     print(y)   

var = "laid"
print(var, " is a word")
      


# print(type(set()))