import threading, time, dis, mmap

orders = []
orderId = 71
orders_lock = threading.Lock()

def takeOrder(itemName, price, noOfOrders):
    global orderId
    print('\n===\nNo of Orders of {} are: {}\n===\n'.format(itemName, noOfOrders))

    for i in range(noOfOrders):
        # critical-section --
        orders_lock.acquire()
        orders.append({'orderId':orderId,'itemName':itemName,'price':price})
        writeOrdersLedger(orderId,itemName,price)
        orderId+=1
        orders_lock.release()
        # -------------------

        print('Order: {} created successfully\n'.format(itemName))



def writeOrdersLedger(orderId, itemName, price):
    order = f"{orderId}. {itemName} ₹{price}\n"

    file = open('live_ledger.txt','r+b')

    order_encoded = order.encode('utf-8')

    file.seek(0,2)
    file_size = file.tell()
    file.write(b"\x00"*len(order_encoded))
    file.flush()

    mm = mmap.mmap(fileno=file.fileno(),length=0)
    mm[file_size:file_size+len(order_encoded)] = order_encoded

    mm.flush()
    mm.close()



thread1 = threading.Thread(target=takeOrder, args=['Dosa', 40, 5])
thread2 = threading.Thread(target=takeOrder, args=['Idly', 30, 5])
thread3 = threading.Thread(target=takeOrder, args=['Lemon Rice', 50, 10])


thread1.start()
thread2.start()
thread3.start()


thread1.join()
thread2.join()
thread3.join()