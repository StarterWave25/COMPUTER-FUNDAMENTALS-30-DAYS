import time, mmap

totalOrders = 0
totalRevenue = 0

def getOrders():
    global totalOrders,totalRevenue
    file = open('live_ledger.txt','r+b')

    mm = mmap.mmap(fileno=file.fileno(),length=0)
    orders = mm[0:].splitlines()

    if(len(orders)==totalOrders):
        print(f'==========Dashboard==========\nTotal Orders = {totalOrders}\nTotal Revenue = ₹{totalRevenue}\n')
        return
    
    newOrdersDifference = len(orders) - totalOrders
    newOrdersStart = totalOrders
    newOrdersEnd = totalOrders+newOrdersDifference

    for order in orders[newOrdersStart:newOrdersEnd]:
        decoded_order = order.decode('utf-8')
        order_price = decoded_order.split(' ')[-1][1:]
        totalOrders+=1
        totalRevenue+=int(order_price)

    print(f'==========Dashboard==========\nTotal Orders = {totalOrders}\nTotal Revenue = ₹{totalRevenue}\n')
    file.close()

while True:
    getOrders()
    time.sleep(3)
