import threading
import mmap
import os
import time

# Shared Resource
orders = []

# Lock to prevent race conditions
orderLock = threading.Lock()

FOLDER = os.path.dirname(os.path.abspath(__file__))
LedgerFile = os.path.join(FOLDER, "ledger.txt")


def CreateLedger():
    if not os.path.exists(LedgerFile):
        with open(LedgerFile, "w"):
            pass
    pass


def writeOrderToFile(order):
    line = f"{order['customer']},{order['item']},{order['price']}\n"
    data = line.encode()

    with open(LedgerFile, "r+b") as f:
        current_size = os.path.getsize(LedgerFile)

        f.seek(current_size + len(data) - 1)
        f.write(b"\x00")
        f.flush()

        mm = mmap.mmap(f.fileno(), 0)
        mm[current_size:current_size + len(data)] = data
        mm.flush()
        mm.close()


def placeOrder(customerName, item, price):

    order = {
        "customer": customerName,
        "item": item,
        "price": price
    }

    # daata adding to shared resource with lock to prevent race conditions
    with orderLock:

        orders.append(order)

        writeOrderToFile(order)

        print(f"{customerName} : ordered {item} - ₹{price}")


def main():

    CreateLedger()

    customerThreads = []

    sampleOrders = [
        ("Alice", "Pizza", 250),
        ("Bob", "Burger", 180),
        ("Charlie", "Coffee", 90),
        ("David", "Pasta", 300),
        ("Eva", "Sandwich", 150),
        ("Frank", "Juice", 80),
        ("Grace", "Cake", 200),
        ("Henry", "Tea", 40),
    ]

    for customer in sampleOrders:

        t = threading.Thread(
            target=placeOrder,
            args=customer
        )

        customerThreads.append(t)
        t.start()

    for t in customerThreads:
        t.join()

    print("\nAll orders processed.")
    print("Orders in shared resource:")
    print(orders)


if __name__ == "__main__":
    main()
