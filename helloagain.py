import multiprocessing
import time
import threading

def task():
    print("hello")
    time.sleep(.5)
    print("THE END")


p1 = multiprocessing.Process(target=task)
p2 = multiprocessing.Process(target=task)

p1.start()
p2.start()
p1.join()


print("hello from code")

def task():
    for i in range(10):
        print(i, threading.current_thread().name)

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()
