from array import __loader__

import module1 as test
import hello_world

def fun1():
    if __name__ == '__main__':
        print("this program is printing as individual program")
    else:
        print("this program is exeduting as a module")
    print("fun1")

def fun2():
    print("fun2")
#
# print(dir())
# print(dir(test))
# # print(dir(functools))
#
# print(__builtins__)
# # print(__cached__)
# print(__doc__)
# print(__file__)
# print(__loader__)
# print("in module2 __name__ is ",__name__)
# print(__package__)

fun1()