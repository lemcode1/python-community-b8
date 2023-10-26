# creating a thread by extending thread class
from threading import *

class PrintMessage(Thread):
    def run(self):
        for i in range(1,11):
            print("Child message")

t= PrintMessage()
t.start()
for i in range(10):
    print("main thread")
