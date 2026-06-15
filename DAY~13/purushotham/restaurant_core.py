import threading
import json
import time
import random
import mmap


orders = []
order_lock = threading.Lock()

FILE_SIZE = 10000
file = open("live_ledger.txt", "w+b")
file.seek(FILE_SIZE - 1)
file.write(b"\0")
file.flush()

memory = mmap.mmap(
    file.fileno(),
    FILE_SIZE
)

def save_ledger():
    data = json.dumps(
        orders,
        indent=4
    )
    data_bytes = data.encode()
    memory.seek(0)
    memory.write(
        b"\0" * FILE_SIZE
    )
    memory.seek(0)
    memory.write(data_bytes)
    memory.flush()

def place_order(orderId, item, price):
    time.sleep(random.randint(1,5))
    order = {
        "orderId": orderId,
        "item": item,
        "price": price
    }

    with order_lock:
        orders.append(order)
        save_ledger()

    print(
        "Order placed!",
        item,
        price
    )

customer_orders = [
    {"orderId": 1, "name": "Pizza", "price": 200},
    {"orderId": 2, "name": "Burger", "price": 150},
    {"orderId": 3, "name": "Coffee", "price": 80},
    {"orderId": 4, "name": "Cake", "price": 120},
    {"orderId": 5, "name": "Pasta", "price": 180},
    {"orderId": 6, "name": "Fries", "price": 90},
    {"orderId": 7, "name": "Soda", "price": 50},
    {"orderId": 8, "name": "Salad", "price": 110},
    {"orderId": 9, "name": "Sandwich", "price": 130},
    {"orderId": 10, "name": "Ice Cream", "price": 70}
]

while True:
    
    threads = []

    for item in customer_orders:
        thread = threading.Thread(
            target=place_order,
            args=(
                item["orderId"],
                item["name"],
                item["price"]
            )
        )
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(
        "Current Orders:",
        len(orders)
    )
    time.sleep(2)