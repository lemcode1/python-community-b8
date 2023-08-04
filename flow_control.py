# week_days=['monday','tuesday','wednesday','thursday','friday','saturday']
# today='sunday'
# if today in week_days: # True
#     print("Today is weekday, I need to join the class")
#     print("After if condition")

# enrolled_students=['Prabhakar','Durga','Farhan','Lingaiah','Pavani','Rajeswar','Rishika','Gopi']
# student_name=input("Please enter your name: ")
# if student_name in enrolled_students:
#        print("{name} is enrolled, allow him to join".format(name=student_name))
# else:
#     print("{name} is not enrolled".format(name=student_name))
# print("outside if-else")

# admin_username='kyedumati'
# admin_pasword="test1234"
# username= input("Enter username:")
# password= input("Enter password:")
#
# if username==admin_username and password==admin_pasword:
#     print("Login successful, welcome to website")
# else:
#     print("Invalid credentials, please enter correct login details")


# If today is weekday and time is 7:30 then i need to join the class, otherwies I will sleep
# from datetime import datetime
# import time
# week_days=['monday','tuesday','wednesday','thursday','friday','saturday']
# print(datetime.now())
# print(datetime.hour)
# print(datetime.minute)
# hours= time.strftime("%H",time.localtime())
# today="wednesday"
# print(hours)
# if today in week_days and int(hours)>7:
#     print("I will join the class")
# else:
#     print("I will continue to sleep")


# find a state based on state code
# state=input("Please enter state:")
# if state=='AP':
#     print("Andhra Pradesh")
# elif state=='CHN':
#     print("Tamilnadu")
# elif state=='KL':
#     print("Kerala")
# elif state=='JK':
#     print("Jammu & Kashmir")
# else:
#     print("Sorry for inconvenience, vodafone services are not available in this state")

# input_char=input("Please enter a char:")
# print(input_char)
# special_chars = ['!','@','#','$','%','^','&','*','(',')','[',']','-','=','_','<']
# vowels=['a','e','i','o','u']
# consonants= ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
# numbers= range(0,10)
# if len(input_char)==1 and input_char not in special_chars:
#     if input_char in vowels:
#         print("{char} is a vowel".format(char=input_char))
#     elif input_char in consonants:
#         print("{char} is a consonant".format(char=input_char))
#     elif int(input_char) in numbers: # '5' in 0,1,2,3,4,5,6,7,8,9
#         print("{char} is a number".format(char=input_char))
#     else:
#         print("It is not a number or character, please try with some other input")
# else:
#     print("You are not giving character, character length should be 1 or you must be giving a special character")


# inner if
# write a program to check given number is positive or negative or zero
# x = int(input("Enter a number:"))
# if x>=0:
#     if x==0:
#         print("Zeroo")
#     else:
#         print("Positive number")
# else:
#     print("Negative number")
# person = 16
# if person < 20:
#     if person >= 18 and person <= 20:
#         print("He is eligible to do internships in any field as well as preparing for competitive exams")
#     else:
#         if person > 10 and person <= 18:
#             print("He is a high school student")
#         else:
#             print("He is an elementary student")
# else:
#     print("He is eligible to work in any software companies")

calc_num(10,20)