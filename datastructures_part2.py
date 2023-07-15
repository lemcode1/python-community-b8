# s1={10,20,30,100}
# #    0  1  2  3
# print(type(s1))
# s2=set()
# print(type(s2))
# print(s1)
# # print(s1[0])
# s1.update([200,300,5000])
# s1.add(9000)
# s1.add("durga")
# s1.add("durga")
# print(s1)
# s2={"kasi","ramesh","ram","kasi"}
# print(s2)
# l1=[10,20,20,30,40]
# print(l1)
# s3=set(l1) # converting list to set
# print(s3)
# s2.remove("ramesh")
# print(s2)

#vowels=('a','e','i','o','u','A','E','I','O','U')

# # frozenset
# vowels=('a','e','i','o','u','A','E','I','O','U')
# print(vowels)
# vowels2= frozenset(vowels)
# print(vowels2)
# print(type(vowels2))


# dict datatype
student_data = {'1234':'Jr Ntr','1235':'Ram charan'}
# a.add(100)
# print(type(a))
# student_data = {''}
# student_data = {1234:'Jr Ntr',1235:'Ram charan', 1234:'kasi',1236:'kasi'}
# print(type(student_data))
# print(student_data)
# student_data[1237] = 'Naresh'
# student_data[1236] = 'kasi yedumati'
# print(student_data)
# print(student_data.values())
# print(student_data.keys())
# print(student_data[1235])
# print(student_data.get(1235))
# #print(student_data[11222])
print(student_data.get(112223))
print(student_data.get(111122,'No Value found for this key'))
# student1 ={
#     "id": 3061208,
#     "name": "Bhaswar Pillai",
#     "email": "bhaswar_pillai@marks-monahan.example",
#     "gender": "female",
#     "status": "active"
#   }
# student2= {
#     "id": 3061207,
#     "name": "Puneet Sinha III",
#     "email": "puneet_iii_sinha@crona-kertzmann.test",
#     "gender": "male",
#     "status": "active"
#   }
# student_list = []
# student_list.append(student1)
# student_list.append(student2)
# print(student_list)

# range datatype
# r= range(10)
# print(type(r))
# print(r)
# for i in r:
#     print(i)
#
# r2= range(10,20)
# for i in r2:
#     print(i)

# r3=range(10,20,3) # 10 13 16 19
# for i in r3:
#     print(i)

# I want to generate odd numbers between 50 - 100
r = range(51,100,2)
for i in r:
    print(i)

# I want to generate numbers from 10 to 1
"""
r2 = range(10,0,-2) # 10 9 8 7 6 5 4 3 2 1
for i in r2:
    print(i)
"""
