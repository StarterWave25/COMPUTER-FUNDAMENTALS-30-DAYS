import json
import time
import mmap

FILE_SIZE = 10000
file = open(
    "live_ledger.txt",
    "r+b"
)
memory = mmap.mmap(
    file.fileno(),
    FILE_SIZE,
    access=mmap.ACCESS_READ
)

def read_orders():
    memory.seek(0)
    data = memory.read(
        FILE_SIZE
    )
    text = data.decode()
    text = text.rstrip("\0")

    if text == "":
        return []
    
    orders = json.loads(text)
    return orders

def display_dashboard(orders):

    total_orders = len(orders)
    total_revenue = sum(
        order["price"]
        for order in orders
    )

    print("====================")
    print("RESTAURANT DASHBOARD")
    print("====================")

    print(
        "Total Orders:",
        total_orders
    )

    print(
        "Total Revenue:",
        total_revenue
    )

    print("====================")

while True:

    orders = read_orders()
    display_dashboard(
        orders
    )
    time.sleep(3)