# for loop
# name="kasi"
# for ch in name:
#     print("ch ",ch)

# write a program to print squares of every number from 1 to 10
# for value in range(1,11):
#     #print(value**2)
#      print(value*value)

# name="mahesh babu"
# i=0
# for ch in name:
#     print("Character present at ",i," index is ",ch)
#     i += 1

# write a program to find a given number is odd or even number
# number = int(input("Enter number: "))
# if number%2!=0:
#     print("Odd number")
# else:
#     print("Even number")

# WAP to print all the odd numbers between 0 to 20
# for value in range(21,0,-1):
#     if value%2!=0:
#         print(value, end=' ')

# 4
# 1,2,4 -->
# write a program to print composite numbers between 1 to 20
# for value in range(1,21):
#     factors_count=0
#     for i in range(1,value+1):  # 1,5--> 1,2,3,4  --> 4
#         if value%i==0:
#             factors_count+=1
#     if factors_count>2:
#         print(value, end=' ')


# while loop
# print numbers from 1 to 10 using while loop
# a=1  # initilisation
# while a<=10: # while condition
#     print(a, end=' ')
#     a+=1

# 10
# 3+1 = 4
# 1+1 = 2
# apples=10
# while apples>=3:
#     apples=apples-3  # eating 3 apples
#     apples+=1 # complimentary apple 1
# print(apples)

# factorial program in while program
# 5 --> 5*4*3*2*1 = 120
# val = int(input("Enter integer to find factorial : "))
# i = 1
# factorial = 1
# while i<=val:
#     factorial = factorial*i
#     i+=1
#     # factorial = 1*1 =>
#     # factorial = 1*2=2
#     # factiral = 2*3 = 6
#     # factoral = 6*4 = 24
#     # factorial = 24*5 = 120
# print("Factorial of {val} is {factorial}".format(val=val,factorial=factorial))

# write a multiplication table using while in python
# 5*1 = 5
# 5*2 = 10
# 5*3 = 15
# val = int(input("Please enter a number to get table"))
# i = 1
# while i<=10:
#     print("{val} *  {i} = {mul}".format(val=val,i=i,mul=val*i))
#     i+=1


# inner for
# for i in range(3):
#     # print(i)
#     for j in range(0,3):
#         print("i= ",i, "j = ",j)

# write a program to print composite numbers between 1 to 20
# 4
# 1%4 =
# 2%4
# 3%4
# 4%4
# for value in range(1,21):
#     factors_count=0
#     for i in range(1,value+1):  # 1,5 --> 1,2,3,4
#         if value%i==0:
#             factors_count+=1
#     if factors_count>2:
#         print(value, end=' ')

# palindrome number
# 121 --> 121 == True then it is a palindrome number
# take a number
# reverse the number
# compare actual number to reversed number
# decide wthere it is palindrome or not
# 123
# 321
# 3 2 1 0 -1 -2
# 2,-1,-1  ==> 2 1 0
# num = input("enter a number :")
# reversed_num = ""
# for i in range(len(num)-1,-1,-1): # 2,0,-1 #
#     reversed_num+= num[i]
# print(reversed_num)
# # reversed_num = num[::-1]
# if num == reversed_num:
#     print("It is a palindrome")
# else:
#     print("not a palindrome")


# *
# * *
# * * *
# * * * *
# * * * * *

# I want to find sum of all the numbers from  1 to 10
# 1+2+3+4+5+6+7+8+9+10 = 55
# i = 1
# final_sum = 0
# while i<=10:
#     final_sum = final_sum+ i
#     i+=1 # i = i+1
#     # final_sum = 0+1
#     # final_sum = 1+2
#     # final_sum = 3+3
# print(final_sum)

# fibanocci series ->
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,...............
# next_number = sum(current_val+previous_val)
# Generate fibanacci series from 0 to 30
previous_num = 0
current_val = 1
while current_val<=30:
    # print(i)
    print(current_val, end=' ')
    temp = current_val
    current_val = previous_num + current_val
    previous_num = current_val
