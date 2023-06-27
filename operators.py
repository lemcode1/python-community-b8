# Arithmatic operators
# a=13.4
# b=6
# print("a+b = ",a+b)
# print("a-b = ",a-b)
# print("a*b = ",a*b)
# print("a/b = ",a/b) # 2.0
# print("a%b = ",a%b)
# print("a//b = ",a//b) # 2.0
# print("a**b = ",a**b) #
# print("2**8 = ",2**8) # 2 power 8
# s1="kasi"
# s2="yedumati"
# print(s1+s2)
# # print(s1-s2)
# print(s1*4)
# print(s1+4)
# b1=True
# b2=True
# print(b1+b2)
# print(b1-b2)
# print(b1*b2)
# print(b1/b2)
# a=20
# b=0
# print(a/b)

# Relational operators  - <  > <= >= ==
# a=20
# b=40
# print(a>b) # 20>40 --> False
# print(a<b) # 20<40 --> True
# print(a<=b) # True
# print(a>=b)
# s1="python"
# s2="python"
# print(s1>s2)
# print(s1<s2)
# print(s1<=s2)
# print(s1>=s2)
# a=True
# b=False
# print(a>=b)
# print(a<=b)
# print(a>b)
# print(a<b)
# print(True>10)
# # print(True>"java")
# print(True>(10>20)) # True>False -> True

# equality operators  == !=
# x=40
# y=40
# print(x==y)
# print(x!=y) # x is not same as y  --> False
# print(False==False) #
# print("lemcode"=="lemcode")
# print("lemcode1"=="lemcode")
# print("lemcode1"!="lemcode")
# print("lemcode"==60)
# a=10
# b=20
# c=30
# print(a>b>c)
# print(a<b>c)
# print(a<b<c)
# print(a<b==a<c)
# print((a<b)==(a<c)) # True == True ==> True

# swap two numbers in python
# Ex: a=2, b=3
# output : a=3 b=2
# a,b=2,3
# print(a,"\t",b)
# # approach 1 :
# a,b = b,a # a,b=3,2 => a=3 b=2
# print(a,"\t",b)

# using addition and subtraction operators
# a=a+b  # 2+3 ==> 5
# # a=5
# b=a-b  # 5-3 ==> 2
# # b =2
# a=a-b  # 5-2 ==> 3
# print(a,"\t",b)
# print first and last value of any string
# s1="lemcode"
# s1="python"
# s1= "programming"
# print(s1[0])
# print(s1[-1])

# Logical operators
# write a program to find largest of three numbers
# Ex: a=10,b=2, c=20
# a=10
# b=2
# c=20
# print(a>b) # True
# print(a>c) # If it returns True it means a is greater than c otherwise a is less than c
# print((a>b) and (a>c)) # True and False --> False

# for boolean data
# print(True and False) # False
# print(True or False) # True
# print(False and True) # False
# print(True or True) # True
# print((not True) or (not False)) # False or True ==> True
# print((not True) and (not False))

# for non-boolean value
# print(10 and 20) # True and True
# print(0 and 10)  # False and True
# print("" and 20) # False
# print("" or "python") # False or True  ===> True
# print(not "")  # not False

# name = "Farhan"
# if not name: # not ""  --> not False --> True
#     print("Name is empty")
# else:
#     print("Name contains something", name)

# account_balance= 2000
# final_balance = account_balance-1000

# Assignemnt operator
# a=30
# b=40
# a=a+50
# a+=50 # a=a+50
# b=b+60
# b+=60
# b%=2 # b=b%2
# print(b)
# b-=20  # b=b-20 -> 0-20
# print(b)


# Ternary operator
# age=16
# output="this person is eligible for vote"  if age>18 else "this person is not eligible, minimum age for vote is 18"
# print(output)

# write a program to check greatest value in both a and b
# condition is a>b
# if a is greater than b then I want to return "a is greater"
# if a is not greater than b then i want to return "b is greater"
a=100
b=60
# x= block1 if condition else block2
x="a is greater" if a>b else "b is greater than a"
print(x)

# Write a program to check maximum of 3 numbers
# Condition a>b and a>c -> then a is greater
# condition b>c and b>a  --> then b is greater
# codition c>a and c>b  --> then c is greater
# a=10
# b=20
# c=120
# # max ="a is greater" if (a>b and a>c) else ("b is greater" if b>a and b>c else "c is greater")
# max="a is greater" if a>b and a>c else "b is greater" if b>a and b>c else "c is greater"
# print(max)

a=20
b=20
# print(type(a))
# print(id(a))
# print(id(b))
# print(a is b)
# print(a is not b)
# a="python"
# b="python"
# print(id(a))
# print(id(b))
# print(a is b)
# a=30
# b=20
# print(id(a))
# print(id(b))
# print(a is b)

# fruits1=['grapes','oranges','banana']
# fruits2=['grapes','oranges','banana']
# print(id(fruits2))
# print(id(fruits1))
# print(fruits2 is fruits1)
# print(fruits1 == fruits2)

# write a program to check whether orange is there in fruit basket
fruit='blueberry'
fruit_basket = ['grape','orange','banana','blueberry']
print(fruit in fruit_basket)
msg=fruit + " is exist" if fruit in fruit_basket else fruit +" doesn't exist"
print(msg)

# write a program to check given character is vowel or not using ternary operator
# Ex : input = 'a'
#   Ouput = a is a vowel
# Ex2 : input = 'z'
# output = z is a consonant


