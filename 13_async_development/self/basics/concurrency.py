from threading import Thread
from concurrent.futures import ThreadPoolExecutor

import time



def greet():
    start = time.time()
    user_name = input("Enter your name: ")
    stop = time.time()
    print(f"Hello {user_name}")
    print(f"Greet took {stop - start} seconds")


def calculate():
    start = time.time()
    print("Starting Calculation: ")
    [x ** 2 for x in range(20000000)]
    stop = time.time()
    print(f"calculate took {stop - start} seconds")


# start = time.time()
#
# greet()
# calculate()
#
# stop = time.time()
#
# print(f"Entire program took {stop-start}")


thread1 = Thread(target=calculate)
thread2 = Thread(target=calculate)

start = time.time()

# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(calculate)
    pool.submit(greet)

print(time.time() - start)
