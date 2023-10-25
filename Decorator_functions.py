def wish_decorator(func):
    def inner(name):
        if name == 'Daniel':
            print("Hi ", name, " Good evening!!!!") # new code to enhance the behaviour
        else:
            func(name) # we are calling existing function
    return inner

@wish_decorator
def wish_message(name):
    print("Hi ",name, " Good morning!!!!")


wish_message("kasi")
wish_message("Chaitanya")
wish_message("Daniel")