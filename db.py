# The DB file contains the processes and functions to create our Database or connect to it as well as run the initial SQL
# The DB file should also contain query functions that the Service file can use to read or modify the data

import sqlite3 as sqlite
import controller

def connect_db():
    connection = sqlite.connect("qacafe_db")
    return connection

def create_cursor(con):
    local_cursor = con.cursor()
    return local_cursor



admin_query = "SELECT * FROM sqlite_master"
select_query = "SELECT * FROM orders"
create_query = "CREATE TABLE orders (order_id int NOT NULL, customer_name VARCHAR(30), drink VARCHAR(20), size VARCHAR(10), extras VARCHAR(30), price FLOAT(5), PRIMARY KEY(order_id))"
insert_query = "INSERT into orders VALUES(2, 'John Smith', 'Latte', 'Medium', 'Whipped Cream', 4.99)"

#local_cursor.execute(insert_query)


#controller.addFirstOrder()
#controller.addNewOrder()
#orders = controller.viewOrders(local_cursor)
#print(orders)

#print(controller.runQuery(select_query).fetchall())


#connection.commit()