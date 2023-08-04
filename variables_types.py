# Global variables
a=30 # global variable

def addition():
    # a=20 # local varible
    global a
    global b
    b=200
    a=a+50
    print(a)
    print("Adding values")
    # return a+50
def subtraction():
    print(a)
    print(b)
    # print(a) # local variable of addition function cant be accessed
    print("subtraction values")

output= addition()
# print(output)
subtraction()


# Always order execution depends on order of calling the function
# globals()  ==> To get all the global information
x=10
def test():
    x=123
    print(x)
    print(globals())
    print(globals()['x'])
    print(globals()['__file__'])
    # print(x,x)

test()

