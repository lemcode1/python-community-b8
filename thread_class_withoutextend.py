# thread class without extending Thread
from threading import *

class Test:
    def display(self):
        for i in range(10):
            print("Child thread")

obj = Test()
t = Thread(target=obj.display)
t.start()

for i in range(10):
    print("Main thread")
