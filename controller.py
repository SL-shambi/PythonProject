# The controller contains functions that takes in data (such as Order Strings or ids) 
# and run the functions in the Service Object that interact with the DB
# The controller will typically convert String data into Order Objects that can be used with the Service functions

# The controller sends and collects data from the Service file, and pushes this data to the Runner which can display said data

# Not complete, but a suggestion of the process

def runQuery(cursor, query):
    data = cursor.execute(query)
    return data.fetchall

def addFirstOrder(cursor):
    insert_query = f"INSERT into orders VALUES(3, 'Jim', 'Black Coffee', 'Medium', 'No', 2.99)"
    return cursor.execute(insert_query)

def addNewOrder(cursor):
    order_id = input("Enter order ID: ")
    customer_name = input("Enter customer name: ")
    drink = input("Enter drink: ")
    size = input("Enter drink size: ")
    extras = input("Enter any extras: ")
    price =  input("Enter the price: ")
    insert_query = f"INSERT INTO orders (order_id, customer_name, drink, size, extras, price) VALUES ({order_id}, '{customer_name}', '{drink}', '{size}', '{extras}', {price})"
    return cursor.execute(insert_query)


def viewOrderbyID(cursor, id):
    view_query = f"SELECT * FROM orders WHERE order_id = {id}"
    data = cursor.execute(view_query)
    return data.fetchall()


def delByID(cursor, id):
    delete_query = f"DELETE from orders WHERE order_id = {id}"
    return cursor.execute(delete_query)

def viewOrders(cursor):
    view_query = f"SELECT * FROM orders"
    data = cursor.execute(view_query)
    return data.fetchall()

def delOrders(cursor):
    delete_query = f"DELETE from orders WHERE order_id > 0"
    return cursor.execute(delete_query)

def updateOrder(cursor, field, new_value, id):
    update_query = f"UPDATE orders SET {field} = '{new_value}' where order_id = {id}"
    return cursor.execute(update_query)