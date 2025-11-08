
# Lists
customer_list = []
customer_email_address = []
products_list = []
prices_list = []
fulfilled_orders_list =[]
orders_list = []

# ABI'S CODE

#customer functions
def add_customer():
    name = input("Enter new customer name: ")
    email = input("Enter email for " + name + ": ")
    customer_list.append(name)
    customer_email_address.append(email)
    customer_id = len(customer_list)-1
    print("New customer created:")
    print("Customer ID:", customer_id)
    print("Name:", name)
    print("Email:", email)
    print()

def view_customers():
    print("--- Customers ---")
    for i in range(len(customer_list)):
        print("ID:", i , " | Name:", customer_list[i], "| Email:", customer_email_address[i])

#computing revenue

def compute_revenue_recognized():
    total_recognized_revenue = 0
    for i in range (len(orders_list)):
        if is_order_fulfilled(fulfilled_orders_list, i):
            (customer_id, product_id, qty) = get_order_details(order_list, order)
            total += qty*prices_list[product_id]
    print("Total recognized revenue:", total_recognized_revenue)

def	compute_revenue_bookings():
    total_bookings_revenue = 0
    for order in orders_list:
        (customer_id, product_id, qty) =  get_order_details(order_list, order)
        total+=qty * prices_list[product_id]
    print("Total bookings revenue:" , total_bookings_revenue)
	    

# NEIL’S CODE

def add_order(orders_list, customer_id, product_id, qty):
    orders_list.append("" + str(customer_id) + "," + str(product_id) + "," + str(qty))
    
def get_order_details(orders_list, order_id):
    return(orders_list[order_id].split(","))


def view_orders(orders_list, fulfilled_orders, all_or_fulfilled):
    if (all_or_fulfilled != "all") and (all_or_fulfilled != "fulfilled"):
        return("view_orders: invalid option specified -- should be all or fulfilled -- instead is " + all_or_fulfilled)
    
    for i in range(0, len(orders_list)):
        if all_or_fulfilled == "fulfilled":
            if is_order_fulfilled(fulfilled_orders, orders_list[i]):
                print_order(orders_list[i])
        elif all_or_fulfilled == "all":
            print_order(orders_list,i)
            
def print_order(orders_list, order_id):
    (customer_id, product_id, qty) = get_order_details(orders_list, order_id)
    print ("Order " , order_id)
    print ("  Customer: ", customer_list[customer_id])
    print ("  Product ID: ", product_id)
    print ("  Quantity: ", qty)
    
def is_order_fulfilled(fulfilled_orders, order_id):
    for i in range(0,len(fulfilled_orders)):
        if fulfilled_orders[i] == order_id:
            return True
    return False

def fulfill_order(fulfilled_orders, order_id):
    if (not is_order_fulfilled(fulfilled_orders, order_id)):
        fulfilled_orders.append(order_id)

def display_menu():
    print("""
Welcome to Basic CRM (Customer Relationship Management)!
    
1. Add Customer
2. View Customers
3. Add Product
4. Print catalogue
5. Add order
6. Fulfill order
7. View all unfulfilled orders
8. View all orders
9. Compute revenue recognized
10. Compute bookings

Enter choice:""")

def get_valid_user_choice():
    choice = -1
    while not ((choice >=1) and (choice <=10)):
        if not choice == -1:
            print ("Try again. Choose an option between 1 and 10.")
            choice = int(input())
    return choice

while True:
    display_menu()
    choice = get_valid_user_choice()
    match choice:
        case 1:
            add_customer()
        case 2:
            view_customers()
        case 3:
            #add_product() to be implemented by Sid
            pass
        case 4:
            #print catalog to be implemented by Sid
            pass
        case 5:
            add_order(orders_list,
                      int(input("Customer id: ")),
                      int(input("Product id: ")),
                      int(input("Quantity: ")))
        case 6:
            fulfill_order(fulfilled_orders,
                          int(input("Enter order id to fulfill: ")))
            
        case 7:
            view_orders(orders_list,
                        fulfilled_orders,
                        "fulfilled")
        case 8:
            view_orders(orders_list,
                        fulfilled_orders,
                        "all")
        case 9:
            # Abi to create a function that takes "recognized" or "bookings"
            pass
        case 10:
            # Abi to create a function that takes "recognized" or "bookings"
            pass
        
#SID'S CODE
# Sid -- please put this into a "add_products" function
while True:
    name = input("Product name (or 'q' to quit): ")
    if name.lower() == 'q':
        break
    price = float(input("Product price: "))
    products_list.append(name)
    prices_list.append(price)
    print("Product ID:", len(products_list)-1)
    print()
    print("All products:", products_list)
    print("All prices:", prices_list)


# Test code:
add_order(orders_list, 0, 0, 1)
add_order(orders_list, 1, 0, 1)
print(get_order_details(orders_list, 0))
print(get_order_details(orders_list, 1))
print(orders_list)



