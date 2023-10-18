import mysql.connector as connection

mydb = connection.connect(host="127.0.0.1", user = "root", password = "Ademola.1234", database = "sqi")
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE IF NOT EXISTS sqi")
# mycursor.execute("CREATE  TABLE customers (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(55), age INT, address VARCHAR(255), gender CHAR(10))")
# querry = "INSERT INTO customers (name, age, address, gender) VALUES (%s, %s, %s, %s)"
# name = input("enter name: ")
# age = int(input("enter your age: "))
# address = input("address: ")
# gender = input("gender: ")

# info = (name, age, address, gender)
# mycursor.execute(querry, info)
# mydb.commit()
# mycursor.execute(querry, info)
# Fname = "tola"
# lname = "kemi"
# print(f"congratulations {Fname} {lname} {0} {"notyetadmitted"} You have successfully registered for this program")



# lists = [(2, 'a', 'b', 207225, 0, 'not yet admitted', 'c', 'd'), (3, 'fola', 'adebowale', 202905, 0, 'not yet admitted', 'ademola1', 'male')]
# guys = list(zip(*lists))
# print(guys)

# mat = 203
# d = 100
# sql = "UPDATE customers SET age = %s WHERE  id = %s"
# ted = (d, mat)
# mycursor.execute(sql, ted)
# mydb.commit()

val = [1, 2, 3]

for i in val:
    print(0/i)
