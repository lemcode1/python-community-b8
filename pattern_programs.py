# Pattern- 1
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
n = 6
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()
# for i in range(n):
#     print("* "* n)


# Pattern -2
"""
1 1 1 1 1
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4
5 5 5 5 5
"""
"""
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
"""

# n = 6
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j, end=" ")
#         # print(j, end=" ")
#     print()

# Pattern - 3
"""
*
* *
* * *
* * * *
* * * * *
"""
# n = 5
# for i in range(n): # rows
#     for j in range(i+1):
#         print("*", end=' ')
#     print()
#


"""
1
1 2 
1 2 3
1 2 3 4
1 2 3 4 5
"""
# n=5
# for i in range(n+1):
#     # p=1
#     for j in range(1,i+1):
#         print(j, end=' ')
#         # p=p+1
#     print()

"""
5 5 5 5 5
4 4 4 4
3 3 3 
2 2
1
"""
# n=5
# for i in range(n,0,-1): # 5 4 3 2 1
#     for j in range(i): # 0 1 2 3 4
#         print(i, end=' ')
#     print()

""" 
0 1 2 3 4
0 1 2 3
0 1 2
0 1 
0
"""
# n=5
# for i in range(n,0,-1): # 5 4 3 2 1
#     for j in range(1,i): # 0 1 2 3 4
#         print(j, end=' ')
#     print()

"""
* * * * * * * * * * *
        *
        *
        *
        *
        *
        *
        *              
"""
def pattern_t(n):
    for i in range(n):
        for j in range(n):
            if i == 0:
                print("* ", end=' ')
            elif j == 5:
                print(" *")
            elif j<=5:
                print("   ",end='')
                continue
        if i==0:
            print()

pattern_t(11)

