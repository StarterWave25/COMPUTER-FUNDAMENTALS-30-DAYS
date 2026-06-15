import threading

lock = threading.Lock()
c = 0


def thread1():
    for i in range(10):
        with lock:
            global c
            c += 1
            print('thread 1:c is ', c)


def thread2():
    for i in range(10):
        with lock:
            global c
            c += 1
            print('thread 2:c is ', c)


threading.Thread(target=thread1).start()
threading.Thread(target=thread2).start()
