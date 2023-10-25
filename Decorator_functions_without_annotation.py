import math
def wish_decorator(func):
    def inner(name):
        if name == 'Daniel':
            print("Hi ", name, " Good evening!!!!") # new code to enhance the behaviour
        else:
            func(name) # we are calling existing function
    return inner

def wish_message(name):
    print("Hi ",name, " Good morning!!!!")

def decor_division(func):
    def inner(a, b):
        if b==0:
            print("Sorry, we cannot divide values with zero")
        else:
            func(a, b)
    return inner

# @decor_division
def division(a, b):
    return a/b

if __name__ == '__main__':
    # wish_message_decor = wish_decorator(wish_message)   # this is the 2nd way to apply decorator to the existing function
    #
    # wish_message("kasi")         # decorator won't be executed
    # wish_message_decor("Chaitanya")  # decorator will be executed here
    # wish_message_decor("Daniel")     # decorator will be executed here

    decorator_division = decor_division(division)

    print("Division of two values is ", division(20,10))
    # print("Division of two values is ", decorator_division(20, 0))
