# WAP to take name of the student as input and print wish message by name
# input: Kasi
# output: Hello Kasi, Good morning

def wish_message(name):
    print("Hello {name}, good morning".format(name=name))
    return "Hello {name}, good morning".format(name=name)
message = wish_message("Rishika") # function calling
# wish_message("Kasi")  # function calling
print(message)


# WAP to take number as input and print square value
def squareit(number):
    print("Square of {number} is {square}".format(number= number,square=number**2))

squareit(5)
squareit(5100)
squareit(34)

# WAP to check whether the given number is even or odd
def is_even_odd(number):
    if number%2==0:
        print(number, "is Even number")
    else:
        print(number, "is Odd number")

is_even_odd(98)
is_even_odd(99)


# WAP to find factorial of a number
def factorial(number): # number=5 , 5*4*3*2*1 => 120
    result = 1
    for i in range(1,number+1):
        result=result*i
    return result

output = factorial(5)
print(output)
result2= factorial(10)
print(result2)



# Are you really understand the question or are you sure about the question?  --> 50%
# 5*4*3*2*1 ==>
# ababc  ==> aba  bab ==>  40%
# converting your analysys into python ===> 10%



# WAP to find sum of 2 values
# def sum(a,b):
#     return a+b
#
# print(sum(10,20))
# print(sum(100,200))
#
#
# list1=[2, 33, 222, 14, 25]
# print(list1[:-1])

vowels = ()
numbers = ()
def constants():
    vowels = ('a','e','i','o','u')
    numbers = (0,1,2,3,4,5,6,7,8,9)
    return vowels, numbers

v, n = constants()
a = constants() # vowels,numbers # packing
# print(v)
# print(n)
# print(a)

# WAP to find given character is vowels or not
def is_vowel_consonant(ch):
    vowels, numbers = constants()
    if ch in vowels:
        print("given character is a vowel")

is_vowel_consonant('a')

# WAP to accept two numbers and perform sum, subtraction, multiplication, division
#def sum(a,b):
#    return a+b

def sub(a,b): # 10,30 = 20
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def calc_num(a,b):
    # sum = a+b
    # sub = a-b
    # mul = a*b
    # div = a/b
    sum1 = sum(a,b)
    sub1 = sub(a,b)
    mul1 = mul(a,b)
    div1 = div(a,b)
    return sum1, sub1, mul1, div1

# num1 = input("enter first number")
# num2 = input("enter second number")
# sum,sub,mul,div = calc_num(10,30) # 10-30 = -20
# print(sum)
# print(sub)
# print(mul)
# print(div)
# sum,sub,mul,div = calc_num(30,10) # 30-10 = 20
# print(sum)
# print(sub)
# print(mul)
# print(div)
# sum,sub,mul,div = calc_num(a=10,b=30) # 30-10 = 20
# calc_num(10)


# WAP to wish one candidate
def wish_message(name, message):
    print("Hello ",name, " ", message)

wish_message(message = "good morning",name = "Kasi") # keyword arguments
wish_message("Ravi", "good afternoon") # positional arguments
wish_message("Ravi", "good afternoon")
wish_message("Ravi", message = "good afternoon")
# wish_message(name="Ravi", "good afternoon") # invalid

# def wish(name="Everyone", message="Good morning"):
#     print("Hello ",name, " ", message)

def wish(name, message="Good morning"): # name is positional argument, message is default argument
    print("Hello ",name, " ", message)

# def wish(name="Everyone", message): # invalid
#     print("Hello ",name, " ", message)

wish(name="kasi", message="Good afternoon")
wish(name="Naga")

# def sum(a,b=0,c):
#     pass

# total= {}
# def insert(items):
#     if items in total:
#         total[items]+=1  # total['Apple'] = total['Apple'] + 1 # total['Apple'] = 2
#     else:
#         total[items] =1
#         # total['Apple'] = 1 #  total = {'Apple':1}
#     # total['Ball'] = 1 #  total = {'Apple':2, 'Ball':1}
#
# insert('Apple')
# insert('Ball')
# insert('Apple')
# print(len(total))


# when we want to take more than 4 arguments to a function
# when you want perform operation on any numbers of arguments
# def sum(num1,num2,num3,num4):
def sum_numbers(*numbers): # numbers = (10,20)
    print(type(numbers))
    return sum(numbers)

print(sum_numbers(10,20))
print(sum_numbers(10,20,30,40))
print(sum_numbers(10,20,30,40,50,60,70,80,90))

# def display(*courses): # courses = ('btech','mtech','mca','mba')
#     for i in courses:# courses = ('btech','mtech','mca','mba')
#         print(i)
#
# display('btech','mtech','mca','mba')

# we can mix positional arguments and variable length arugments together
# we cant treat variable lenght as a keyword arguments
# def display(s1, *courses):
#     print(s1)
#     print(courses)
# display('btech','mtech','mca','mba')
# def display(*courses, s1): #
#     print(s1)
#     print(courses)
#
# display('btech','mtech','mca', s1= 'mba')

# set, dict -->
# d = {x:x**2 for x in range(1,5) if x%2==0}  # {2:4,4:16} # dict
# print(d)
# print(d['name'])
# list1 = [1,2,4,5,6]

# def display(*courses, s1):
#     # return "hello world"
#      return courses
#
# output = display('btech', s1="")
# print(output)

def test(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for k,v in kwargs.items():
        print(k, " ",v)

test(a=10,b=20,c=30) #
# test(10,20,30) # positional arguments are not allowed

print()

def test2(*args, **kwargs): # first one you need pass variables lenght args, and then keyword lenght args
    print(args)
    print(kwargs)

# test2(10,20,30,a=100,200,c="Ongole") #
# test2(10,20,30,a=100,c="Ongole")
test2(a=10,b="Ongole") # all these will go to kwargs
test2(10,20) # all these will go to args
# test2(a=10,20) # error # kwargs, args


def testing_function(arg1, arg2, arg3=4, arg4=8): # arg1, arg2-> positional , arg3,arg4= default
    print(arg1,arg2,arg3,arg4)

testing_function(10,20) # 10 20 4 8
testing_function(10,20,30,40) # 10 20 30 40
testing_function(10,20,30) # 10 20 30 8
testing_function(arg1=20,arg2=30,arg3=40,arg4=50) # 20 30 40 50
testing_function(arg4=20,arg1=30,arg3=40,arg2=50) # 30 50 40 20
# testing_function() # error











