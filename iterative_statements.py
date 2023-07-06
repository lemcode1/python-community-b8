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
apples=10
while apples>=3:
    apples=apples-3  # eating 3 apples
    apples+=1 # complimentary apple 1
print(apples)