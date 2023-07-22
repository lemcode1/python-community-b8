# Creation of Set Objects
# s= {19,20,40} # using { }
# print(type(s))
# s2 = set([10,30,405,60,60])
# print(type(s2))
# print(s2)
# # s3= {}  # empty dict
# s3=set() # empty set
# # l1= list()
# print(type(s3))

# Important functions of Set
s={10,203,40,60}
s.add(44)
# print(s)
# update(x,y,z)
list1=[1,2,3]
s.update(list1,range(20,30))
print(s)
# copy() to clone/copy the set
s1={1,2,3,40,50}
s2=s1.copy()
# s2=s1
s2.add(30)
print(s1)
print(s2)

# pop() --> it removes and return random element from the set
print(s2.pop())
print(s2)

# remove(x) --> It removes the item from the set
# If the specified element is not present then it throws Error
s2.remove(2)
print(s2)
# s2.remove(100)

# discard(x) --> It removes the specified item from the set
# If the specified item is not presenet then it wont throw any Error
# s2.discard(30)
# print(s2)
# s2.discard(200)

# s2.clear()
# print(s2)


# Mathematical operations on Set
# union() --> It returns all the elements present in both the sets
x={1,2,3,4}
y={4,5,6}
print(x.union(y))
print(x|y)

# intersection() --> Returns the common elements present in both the sets
print(x.intersection(y))
print(x&y)

# difference() --> it returns the elemnets present in x but not in y
print(x.difference(y))
print(y.difference(x))
print(y-x)

# symmetric_difference() --> It returns the elements present either x or y but not in both
# It returns only unique elements present in both the sets
print(x.symmetric_difference(y))

# subset()  --> It checks the the subset is available in set or not
# s1={1,2}
# s2={1,2,3,4}
# print(s2.issubset(s1))
# print(s1.issubset(s2))
# if 1 in s2:
#     print("1 is available in set2")

# Set Comprehension
# s = {expression for item in sequence if condition}
str1="java is easy"
vowels = ('a','e','i','o','u')
output = {i for i in str1 if i in vowels}
print(output)
#
# Question-8:
# To store the data like:
# 	i) Aadhaar Card Numbers
# 	ii) Passport Numbers
# 	iii) Bike Numbers
# 	iv) Car Numbers
# 	v) Mobile numbers
# and insertion, updation, deletion operations should be allowed. Which collection is suitable?
