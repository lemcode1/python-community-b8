# String handling
name = "Nani"
print(name[1])
print(name[0:3])
print(name + " yedumati")
# print(name + 10)
print(len(name))
first_name = "kasi"
last_name = " yedumati,3 "
print(last_name)
#last_name = last_name.strip()
last_name = last_name.lstrip()
# last_name = last_name.rstrip()
print(last_name)

# sentence = "Python is program high level interpreted programming language"
# print(sentence.find("program"))
# print(sentence.find("java"))
# # if sentence.find("java")!= -1:
# #     print("word is found")
# # else:
# #     print("word is not found")
# print(sentence.index("program"))
# # print(sentence.index("java"))
# print(sentence.find("program",17,59))
# print(sentence.rfind("program"))
#
# print(sentence.count("program"))
# print(sentence.count("program",17,59))
#
# s1="abcabc"
# s1 = s1.replace("a","z")
# print(s1)
# sentence = "Python is very easy"
# sentence =  sentence.replace("easy","difficult")
# print(sentence)
# names = "kasi durga test nani"
# names = names.strip()
# # names = names.replace(" ","")
# names = names.replace(" ",'-')
# print(names)
# # nameslist = names.split("-")
# nameslist = names.split(" ")
# print(nameslist)
# todays_date = "12/07/2023"
# dates = todays_date.split("/")
# print(dates)
# print(dates[2])
# full_name = "kasi yedumati"
# # print only firstname
# names = full_name.split(" ")
# print(names)
# first_name = names[0]
# last_name = names[1]
# print(first_name)
# print(last_name)
# names = ["virat", "kohli"]
# print(names)
# full_name = ' '.join(names)
# print(full_name)
#
# cities = ['hyderabad','mumbai','vizag','pune']
# cities_string = ':'.join(cities)
# print(cities_string)

# changing case of a string
# s1='learning python Is veRY Easy'
# s1="lErNiNg"
# print(s1.upper())  # LEARNING
# print(s1.lower())  # learning
# print(s1.swapcase()) # LeRnInG
# print(s1.title())    # Learning
# print(s1.capitalize()) # Learning

s= "python"
# print(s.startswith("p"))
# print(s.startswith("n"))
# print(s.endswith("n"))
# print(s.endswith("s"))
# aspirtants = ['kasi Btech', 'Nani Bsc', 'Naga Mca', 'Virat SSC', 'Dhoni Intermediate']
# for i in aspirtants:
#     if i.endswith("Btech") or i.endswith("Bsc"):
#         print(i, " is a graduate")
#     elif i.endswith("Mca"):
#         print(i, " is a post graduate")
#     elif i.endswith("SSC"):
#         print(i, " is a schooling")
#     elif i.endswith("Intermediate"):
#         print(i, " is a intermediate")

mail = "rishika-pamanji@gmail.com"
# print(mail.replace("-",""))
# mail_names = mail.split("-")
# print(mail_names)
# mail = ''.join(mail_names)
# print(mail)
# out_mail = ''
# for i in mail:
#     if i!='-':
#         out_mail+=i
# print(out_mail)

# print("123".isdecimal())

# to check type of characters present in a string
# s1='abc 123'
# print(s1.isalnum()) # False
# print(s1.islower()) # True
# print(s1.isupper()) # False
# print(s1.isalpha()) # False
# print(s1.isdigit()) # False
# print(s1.istitle()) # False
# print(s1.isspace()) # False

# write a program to check the given character is string or number or uppercase or lowercase or space
# s = input("Enter any character: ")
# if s.isalnum():
#     print("Alpha number")
#     if s.isalpha():
#         print("It is a alphabet")
#         if s.istitle():
#             print("It is a title case")
#         elif s.lower():
#             print("lower case value")
#         else:
#             print("upper case")
#     else:
#         print("It is digit")
# elif s.isspace():
#     print("It is a space")
# else:
#     print("Non space special character")


# WAP to add two values from user input
# a = input("Enter a digit:")
# b = input("Enter b digit:")
# if a.isdigit() and b.isdigit():
#     a = int(a)
#     b = int(b)
#     c = a + b
#     print("sum of {0} and {1} is {2} ".format(a, b, c))
# else:
#     print("Dear User, This application accepts numeric values to perform sum, please enter only digit and re-run")


# WAP to reverse the given string
# Ex: input : virat  output : tariv

# Approach 1: using slice operator
# s = input("Enter word to reverse: ")
# reverse_string = s[::-1]
# print(reverse_string)

# Approach 2: Using for/while
reversed_string = ''
# for i in range(len(s)-1,-1,-1):# 5,0,-1  -->  4,3,2,1,0
#     reversed_string= reversed_string + s[i]
# print(reversed_string)

# i = len(s)-1
# while i>=0:
#     reversed_string = reversed_string+s[i]
#     i = i-1
# print(reversed_string)


# WAP to reverse order of words
# input: Python is very easy
# output: easy very is python
# s = input("Enter a sentence to reverse: ")
# i = s.split(" ") # i = ["Python", "is", "very", "easy"]
# reversed_list = i[::-1] # reversed_list = ["easy", "very","is","Python"]
# reversed_string = ' '.join(reversed_list) # easy very is python
# print(reversed_string)

# WAP to reverse each word of the string
# input: python is easy
# output: nohtyp si ysae

# split the words
# take every word and reverse and append to new string
# s = input("Enter a sentence to reverse: ")
# l = s.split()
# reversed_string = []
#
# for word in l:
#     # reversed_string = reversed_string + word[::-1] + " "
#     reversed_string.append(word[::-1])
# print(' '.join(reversed_string))


# WAP for following requirement
#  input : a4b3c2
#  ouput : aaaabbbcc
# input = "a4b3c2"
# output = ''
# i = 0
# while i<len(input):
#     output = output + input[i] * int(input[i+1])
#     i= i+2
#
# print(output)

# print(ord('A'))
# print(ord('B'))
# print(ord('Z'))
# print(ord('a'))
# print(ord('z'))
# print(ord('%'))
# print(chr(65))
# print(chr(1114111))
# print(chr(23456))


# WAP to to perform following activity
# input : ABABCDDDEEEEFFF
# output : ABCDEF
# input = "ABABCDDDEEEEFFF"
input = "1212334445556"
output = ''

# for i in input:
#     if i not in output:
#         output += i
# i = 0
# while i<=len(input)-1:
#     if input[i] not in output:
#         output += input[i]
#     i+=1
# print(output)
# input_set = set(input)
# print(input_set)

# for i in range(len(input)):
#     if i == 0:
#         output = output + 1
#     print(output)



# Find out the number of occurance of each character in the given string
# input : ABABCDDDEEEEFFF
# ouput : A:2, B:2,C:1, D:3, E:4, F:3
# key : values
# char : occurancecount

input = "ABABCDDDEEEEFFF"
output = {}
# ouput = {'A':2,'B':1}
# for i in input:
#     # output[i] = output.get(i,0) + 1
#     if i in output.keys():
#         output[i] += 1
#     else:
#         output[i] = 1
# output = {}
# for i in input:
#     if i not in output.keys():
#         output[i] = input.count(i)
# print(output)

#input1=(9,2,-2,-2)
# input2=4
# input3=(1,4,3)
# input4=3
# output=22

#List a=[ 1,2,3 ,none, none]
# list b=[4,5,3]
# Output=[1,4,2,5,3,3]

a = [1,2,3,None,None]
b= [4,5,3]
c = []
a1=[]
for i in a:
    if i is not None:
        a1.append(i)
# print(a1)
# for i in a:
#     if i is not None:
#         for j in b:
#
#             c.append(i)
#
temp=[]
for i in range(len(a1)+len(b)):
    temp.append("@")

# for i in range(len(temp)):
#     if i%2 == 0:
#         temp[i] = a1[i]
#     else:
#         temp[i] = b[i-1]
temp2 = []
# for item in range(len(b)):
#     for j in [a1,b]:
#         temp2.append(item[j])
#
# temp2 = [sub[item] for item in range(len(b)) for sub in [a1,b]]
# for item in range(len(b)): # item in range(3): 0 1 2
#     for sub in [a1, b]:   # sub in [,[1,2,3][4,5,3]] # 2
#         temp2.append(sub[item]) # [1,2,3] # 1
# print(temp2)

