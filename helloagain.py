import multiprocessing
import time
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