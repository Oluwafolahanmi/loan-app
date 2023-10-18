import mysql.connector as connection
 
mydb = connection.connect(host="127.0.0.1", user = "root", password = "Ademola.1234", database = "mydatabase")

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
# mycursor.execute("USE mydatabase")
# mycursor.execute("CREATE  TABLE customers (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(55), address VARCHAR(255), gender CHAR(10))")
# sql = "INSERT INTO customers(id, name, address, gender) VALUES(200, 'Oluwafolahanmi', 'No. 10, Dugbe', 'male')"
# querry = "INSERT INTO customers (name, address, gender) VALUES (%s, %s, %s)"
# name = input("enter name: ")
# age = input("enter your age: ")
# address = input("address: ")
# gender = input("gender: ")

# info = (name, address, gender)
# mycursor.execute(querry, info)
# mycursor.execute(sql)
# sql = "SELECT * FROM customers"
# sql = "SELECT * FROM customers WHERE id = 200"
# sql = "UPDATE customers SET gender = 'female' WHERE id = 200"

sql = "DELETE FROM customers WHERE id = 201"
mycursor.execute(sql)
# result = mycursor.fetchall()
# result = mycursor.fetchone()
# result = mycursor.fetchmany()
# for row in result:
#     if "Oluwafolahanmi" in row[1]:
#         print("welcome oluwafolahanmi")
    # print(row[2])

# print(result)

mydb.commit()
# mycursor.execute("DROP DATABASE IF EXISTS mydatabase")
