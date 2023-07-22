# tuple is read only version of list
# Tuple creation
a=(200,30,10,20,30,40)
print(type(a))
a=(10,)
print(type(a))
a=10,20,30,40
print(type(a))
a=()
print(type(a))
# by using tuple() function
a=tuple([10,20,30])
print(type(a))
a=tuple(range(10,20))
print(a)
print(type(a))

# accessing the elements in the tuple
# by using index
print(a[3])
print(a[-2])
# by using slice operator
print(a[2:7])

# Mathematical operators for tuple:
# we can apply mathematical + and * operators
t1=(10,20,30)
t2=(40,50,60)
t3=t1+t2
print(t3)
print(t3*5)

# Important functions of Tuple
# len() to return the number of elements present in the tuple
print(len(t3))
# count() to return the number of occurance of given element in the tuple
count = t3.count(30)
print(count)
# index() to return the index of first occurance of given element
print(t3.index(20))
print(t3.index(60))
# sorted(value,reversed=True/False) -> to sort the tuple in either ascending/descending order
print(sorted(t3))
print(sorted(t3,reverse=True))

# min() and max() --> it find outs the min/max value of tuple
print(min(t3))
print(max(t3))

# cmp() > it is used to compare tuples
# If both tuples are same it returns 0
# if the first tuple is less than second tuple then it returns -1
# if the first tuple is greater than second tuple then it returns +1
t1=(10,20,30)
t2=(40,50,60)
t3=(10,20,30)
# print(cmp(t1,t2)) # -1
# print(cmp(t1,t3)) # 0
# print(cmp(t2,t3)) # +1
# Note : cmp function is only available in python2 but not in python3

a=10
b=30
c=40
t=a,b,c # t=10,30,40
print(t)
print(type(t))
x,y,z=t  # unpacking
print(x,y,z)

# Tuple comprehension
# t=(i for i in range(1,6))
# print(type(t))
# print(t)
# for item in t:
#     print(item)


# PROGRAMS IN TUPLE
# t= ('p','y','t','h','o','n')
# output = ''.join(t)
# print(output)
# t1="python"
# t2="java"
# t3= t1,t2
# print(t3)
# if 'p' in t:
#     print('p is exist')

# input: t=10,20,30,40,30,10,40
# ouput : 10,30,40
# t=10,20,30,40,30,10
# # output = tuple([i for i in t if i in (10,30)])
# s1=set(t)
# output= []
# for i in s1:
#     if t.count(i)>1:
#         output.append(i)
# print(tuple(output))


# X=(1,2,3,4)
# O/p:(1,4,9,16)
# O/p:(4,16)
# X=(1,2,3,4,5,6,8,8,2,3)
# output = tuple([item**2 for item in X if item%2==0])
# print(output)

x="hello python java is good"  # count the number of words in given string and print output in below format
# o/p :hello5 python6 java4 is2 good4
x="hello python java is good"
x=x.split()
l=[]
for word in x:
    a=word + str(len(word))
    # print(a,end=' ')
    l.append(a)
print(l)
print(' '.join(l))