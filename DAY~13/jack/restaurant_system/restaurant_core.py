orders = []

# orders.append(("Burger",120))
# orders.append(("Pizza",250))

# print(orders)

# orders
# │
# ├── ('Burger',120)
# ├── ('Pizza',250)

# in normaly customers oder one after another but in real restaurent custemers oders at same time data can be corepted or duplicated
#so thats why python uses threads so we can secure the data and no corepction 

import threading

def customer(name,order):
    print("order recived from "+name)
    place_order(order)

# t1 = threading.Thread(target=customer,args=("Jagan",))
# t2 = threading.Thread(target=customer,args=("Ravi",))
# t3 = threading.Thread(target=customer,args=("Kiran",))

# t1.start()
# t2.start()
# t3.start()

lock = threading.Lock()


def place_order(order):

    with lock:
        orders.append(order)
        with open("live_ledger.txt","a") as file:
            item,price = order
            file.write(item,price+"\n")

items =[
    "dosa",
    "idly",
    "voda",
    "pizza",
    "burger"
]       
for i in range(5): 
    customer("jackk",items[i])

print(orders)
