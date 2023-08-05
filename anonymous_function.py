# WAP to find square of a number
# using normal function
# def square_number(a):
#     out= a**2
#     return out

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


