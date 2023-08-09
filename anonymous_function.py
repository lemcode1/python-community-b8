# WAP to find square of a number
# using normal function
# def square_number(a):
#     out= a**2
#     return out
from functools import reduce
# from functools import *

s=lambda a:a**2
# print(square_number(3))
print(s(4))
print(s(3))
sum_numbers = lambda a,b:a+b
print(sum_numbers(300,400))

# WAP to find biggest of two numbers using lambda functions
biggest_num = lambda a,b:a if a>b else b # ternary operator
print(biggest_num(20,30))


# WAP to filter only even numbers from a list
# list1 = [1,2,3,4,5,6,7,8,9]
# def is_even(a): # this is to perform a conditional check
#     if a%2==0:
#         return True
#     else:
#         return False
#
# even_list = list(filter(is_even, list1[::-1]))
# print(even_list)

# even_list = []
# for i in list1:
#     if i%2==0:
#         even_list.append(i)
# print(even_list)

# filter function -->
# palinrome -->

# WAP to return all vowels from given string
# input : welcome to python
# output : eoeoo
vowels=['a','e','i','o','u']
# def is_vowel(char):
#     if char in vowels:
#         return True
#     else:
#         return False
is_vowel = lambda char:True if char in vowels else False
# vowels_from_list = list(filter(is_vowel,"welcome to python"))
vowels_from_list = list(filter(lambda char:True if char in vowels else False,"welcome to python"))
print(vowels_from_list)

# WAP to find values which are divisible by 100 in the give list
# input: [1,100,200,300,2,30,40,60]
# output: 100,200,300
# list1=eval(input('Enter list of values ex([1,2,3,4]) :'))
list1=[1,100,200,300,2,30,40,60]
def is_divisible_by_hundred(number):
    return number%100==0
    # if number%100==0:
    #     return True
    # else:
    #     return False

# hundred_list = list(filter(is_divisible_by_hundred, list1))
# hundred_list = list(filter(lambda number:True if number%100==0 else False, list1))
hundred_list = filter(lambda number:number%100==0, list1)
print(type(hundred_list))
print(list(hundred_list))


#map()
# WAP to square each item from the list
l = [1,2,3,4,5]
# def square_value(x):
#     return x**2

# output = map(square_value, l)
output = map(lambda x:x**2, l)
# output = filter(lambda x:x**2, l)
print(list(output))

salaries = [1000,2000,4000,5000,500,600]
# bonus = 20% of their salary
final_salaries = list(map(lambda salary:salary*0.2+salary, salaries))
high_paid_employees = filter(lambda salary:salary>2000, salaries)
# def add_bonus(salaries):
#     final_salaries= []
#     for salary in salaries:
#         final_salaries.append(salary * 0.2 + salary)
#     return final_salaries
#
# final_salaries = add_bonus(salaries)
print(final_salaries)
print(list(high_paid_employees))


# [1,2,3,4,5] => 1+2+3+4+5 = 15
l2=[1,2,3,4,5]
final_sum = reduce(lambda x,y:x+y, salaries)
print(final_sum)
final_sum = reduce(lambda x,y:x+y, range(1,100))
print(final_sum)

#

def wish_message(name):
    print("Good morning!! ", name)

wish_message('Chiru')
wish = wish_message # function aliasing
wish('Chiru')

def outer_func():
    print("inside outer first line")
    def inner_func():
        print("insider inner function")
    print("inside outer func last line")
    inner_func()

outer_func()
# inner_func()


str1="01-01-2021"
print(str1.split('-'))