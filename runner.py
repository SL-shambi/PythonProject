# The runner contains the code to Create a User Interface for the Cafe to interact with
# This 'runs' the code and will interact with the Controller directly

# import sqlite3 as sqlite
import controller
import db

connection = db.connect_db()
cursor = db.create_cursor(connection)

# conn = sqlite.connect("qacafe_db")
# cursor = conn.cursor()

print("""
-------- Welcome to QA Cafe --------

What can we help you with?
1) Add Order
2) Read Order By ID
3) Read All Orders
4) Update Order by ID
5) Delete Order by ID
6) Delete All Orders
""")

user_input = input("Which choice do you need? ")

if user_input == "1": 
    controller.addNewOrder(cursor)
elif user_input == "2":
    id = int(input("What ID would you like to see? "))
    controller.viewOrderbyID(cursor, id)
elif user_input == "3":
    controller.viewOrders(cursor)
elif user_input == "4":
    controller.updateOrder(cursor)
elif user_input == "5":
    controller.delByID(cursor)
elif user_input == "6":
    controller.delOrders(cursor)