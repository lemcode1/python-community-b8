# dynamic list input
# list1 = eval(input("Enter list values:"))
# print(type(list1))

list2 = [10,20,30,40,5,6,7,8,9,1,2,3,4,5,6]
# for i in range(len(list2)): # iterating using index number
#     print(list2[i], end=' ')

# for i in list2:
#     print(i)
i = 0
#
#0 <=15
# 0 1 2 3  15
# while i<len(list2):
#     # 0<=15
#     # 1<=15
#     # 2<=15
#     # 14<=15
#     # 15<=15  --> True
#     print(list2[i]) # --> list2[15]
#     i+=1
# print()

# Display only even numbers from list2
even_list = []
odd_list = []
output = []
# [[10, 20, 30, 40, 6, 8, 2, 4, 6], [5,7,1,3,5]]
# for i in list2:
#     if i%2==0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)
# output.append(even_list)
# output.append(odd_list)
# print(output)
# L1 = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']
# L2 = ['burger', 'hotdog', 'noodles', 'pasta', 'nuggets', 'pizza']
# L1.extend(L2)
# print(L1+L2)
#
# l1=[[10,20],30]
# print(len(l1))
# l2 = l1[0] # [10,20]
# print(l2[0])
# print(l1[0])
# print([10,20][0])
# print(l1[0][1])
# print(l1[1])
# list3 = [[1],[2],[3,4]]
# # [[1], [2], [3, 4]]
# #     0    1    2
# #  list3[2][0]
# print(len(list3))
# print(list3[2][0])
# list4=  [[1,2],[3,4], [5,[6,7,8]]]
#          0     1       2
# list4[2]  --> [5,[6,7,8]]
#                0    1
# list4[2][1] --> [6,7,8]
#                  0 1 2
# list4[2][1][0]
# print(list4[2][1][0])
L1 = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
L2 = [[5,6,7,8],[5,6,7,8],[5,6,7,8]]
L3 = []
# for item in L1: # 3
#     L3.append(item)
# for item in L2:
#     L3.append(item)
# print(L1+L2)

students=['Raj','Naresh','Suresh', 'Raj','Naresh']
print(students.count('Raj'))
print(students.count('Suresh'))
print(students.count('Kasi'))

print(students.index('Naresh'))
print(students.index('Raj'))
# print(students.index('Kasi'))

students.append('Kasi')
print(students)
students.append({'kasi':9986332875})
# students.append(['Gopi','Siva','Naga'])
students.extend(['Siva'])
print(students)

list= [4,5,6,7,2,3,11,13]
#Sort the element in a such a way that have even should come first and odd numbers at last
even_list = []
odd_list = []
output = []
# [[10, 20, 30, 40, 6, 8, 2, 4, 6], [5,7,1,3,5]]
for i in list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
output.extend(even_list)
output.extend(odd_list)
print(output)