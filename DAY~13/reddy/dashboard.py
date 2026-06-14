import mmap
import os
import time
import restaurantCore

LedgerFile = restaurantCore.LedgerFile


def readLedger():

    if not os.path.exists(LedgerFile):
        return []

    if os.path.getsize(LedgerFile) == 0:
        return []

    with open(LedgerFile, "r+b") as f:

        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

        content = mm.read().decode()

        mm.close()

    records = []

    for line in content.splitlines():

        if line.strip():

            customer, item, price = line.split(",")

            records.append(
                {
                    "customer": customer,
                    "item": item,
                    "price": float(price)
                }
            )

    return records


def dashboard():

    sharedOrders = restaurantCore.orders

    if sharedOrders:
        data = sharedOrders
        totalOrders = len(data)
        revenue = sum(order["price"] for order in data)

    else:
        data = readLedger()

        totalOrders = len(data)

        revenue = sum(order["price"] for order in data)

        source = LedgerFile

    print("\n--------------------------")
    print("Restaurant Dashboard")
    print("--------------------------")
    print("Source :", source)
    print("Orders :", totalOrders)
    print("Revenue: ₹", revenue)


if __name__ == "__main__":

    while True:
        dashboard()
        time.sleep(3)
