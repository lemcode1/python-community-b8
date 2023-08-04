employee_dict = {
  "status": "success",
  "data": {
    "id": 1,
    "employee_name": "Tiger Nixon",
    "employee_salary": 320800,
    "employee_age": 61,
    "profile_image": ""
  },
  "message": "Successfully! Record has been fetched."
}

print(employee_dict)
employee_dict = {}
# employee_dict[key] = value
employee_dict['name'] = 'Durga'
print(employee_dict)
employee_dict['status'] = 'Active'
# employee_dict['state'] = 'AP'
# employee_dict['country'] = 'India'
# employee_dict['village'] = 'Venkatapuram'
employee_dict['address'] = {
                              "state": "AP",
                              "country": "India",
                              "village": "Venkatapuram"
                          }
# employee_dict['status'] = 'Inactive'
# print(employee_dict)
#
# # we can access values using key
# print(employee_dict['status'])
# if 'mobileno' in employee_dict:
#     print(employee_dict['mobileno'])
# has_key()

# getting values using get()
# print(employee_dict.get('mobileno')) #
# print(employee_dict.get('mobileno','Mobile no is not exist'))
# print(employee_dict.get('mobileno','9999999999'))
#
# print(employee_dict.get('status','Status is not exists'))
# del employee_dict['status']
# print(employee_dict)
# del employee_dict['mobileno']
# employee_dict.clear()
# del employee_dict
# print(employee_dict)

# print(employee_dict['address'])
# print(employee_dict['address'].get('village')) # list[0][2]
# print(employee_dict['address']['village'])
# print(employee_dict.get('address').get('village'))

# print(len(employee_dict))

# roman_numbers = {'I':1, 'V':5 ,'X': 10}
# input= input("Enter input:") # 5-1 = 4
# # VI # 5+1 = 6
# i=0
# output=0
# while i<len(input):
#     number1 = roman_numbers[input[i]] # I = 1
#     if i+1 < len(input):
#         number2 = roman_numbers[input[i+1]] # V = 5
#         if number1>=number2:
#             output += number1
#             i+=1
#         else:
#             output+=number2 - number1
#             i += 2
#     else:
#         output += number1
#         i += 1
# print(output)

# 1 3 5 2 4
#1-3-5-2*4

# print(employee_dict)
#
# print(employee_dict.pop('status'))
# print(employee_dict)
# print(employee_dict.pop('status'))
# print(employee_dict.popitem())
print(employee_dict)
print(employee_dict.keys())
print(employee_dict.values())
print(employee_dict.items())
d2= employee_dict.copy()
print(d2)

# print(employee_dict.setdefault('mobileno',56789))
print(employee_dict.get('mobileno',56789))
print(employee_dict.setdefault('status','Inactive'))
print(employee_dict.get('status','Inactive'))
print(employee_dict)

d3={'empno': 1234, 'empsalary':23451234}
print(employee_dict.update(d3))
print(employee_dict)
# print(employee_dict)

# sort the dict based on keys
emp_keys = list(employee_dict.keys())
emp_keys.sort()
sorted_emp_dict = {key:employee_dict[key] for key in emp_keys}
print(sorted_emp_dict)

# You have a 2-D array of friends like [[A,B],[A,C],[B,D],[B,C],[R,M], [S],[P], [A]]
# Write a function that creates a dictionary of how many friends each person has.
# People can have 0 to many friends. However, there won't be repeat '
input_list = [['A','B'],['A','C'],['B','D'],['B','C'],['R','M'], ['S'],['P'], ['A']]
# A --> B,C --> 2
# B --> A,C,D --> 3
# C --> A,B   --> 2
# D --> B  --> 1
# R  --> M --> 1
# M  --> R --> 1
# S -> 0
# P -> 0
# output = {'A': 2, 'B': 3, 'C':2, 'D':1, 'R':1, 'M': 1, 'S':0,'P':0}
# output = {}
# for item in input_list:
#     for i in item: # ['A','B'] #['P']
#         if len(item)>1: # 1>1
#             output[i] = output.get(i,0)+1 # A=0+1 A:1 # B:1
#             # output[i] += 1
#         else:
#             output[i] = output.get(i,0)+0
# print(output)

# WAP to find number of occurances of each vowel in the string
# input : I want to learn python
# ouput :
#  {'a':2, 'i':1 ,'e':1, 'o':2 }
input = 'I want to learn python'
vowels =('a','e','i','o','u')
# vowels_count = { vowel: input.lower().count(vowel) for vowel in vowels}
vowels_count = {}
for character in input.lower():
    if character in vowels:
       vowels_count[character] = vowels_count.get(character,0) + 1
    # vowels_count[key]
    # vowels_count.get(key)
print(vowels_count)






