# creating a thread without using any class
from threading import *
def display():
    for name in range(1,11):
        print("Kasi")
def display_nani():
    for name in range(1,11):
        print("Nani")
# display()
# display_nani()
t = Thread(target=display)  # creating child thread object
t.start()
t2= Thread(target=display_nani) # creating child thread object
t2.start()
for i in range(1,11):  # main thread
    print("ABC")