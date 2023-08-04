# WAP for factorial of a number n
# def factorial(n): # 5*4*3*2*1
#     fact = 1
#     while(n>0):
#         fact = fact*n
#         n=n-1
#     return fact

# output = factorial(6)
# print(output)


# recursive method #
# def factorial(n): # 5*4*3*2*1 # n*n-1*n-2*n-3*n-4*1
#     if n==0:
#         result = 1
#     else:
#         result = n*factorial(n-1)  # calling the same function inside function by decrementing n by 1
#     return result
# n=5   # 5*factorial(4)
# n=4   # 5*4*factorial(3)
# n=3   # 5*4*3*factorial(2)
# n=2   # 5*4*3*2*factorial(1)
# n=1   # 5*4*3*2*1*factorial(0)
# n=0   # 5*4*3*2*1*1 = 120

# result = factorial(5)
# print(result)