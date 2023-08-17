
print("writng in module1 __name__ is : ", __name__)
def add(a,b):
    return a+b

def wish_message(message, name):
    return f"Hello {name}, {message}".format(name=name, message=message)

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)