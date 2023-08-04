# Question-1:
# To store the data like:
# 	i) Aadhaar Card Numbers
# 	ii) Passport Numbers
# 	iii) Bike Numbers
# 	iv) Car Numbers
# 	v) Mobile numbers
# and insertion, updation, deletion operations should be allowed. Which collection is suitable?
# selected_option = input("Please select any one options below: "
#       "1.Aadhaar Card Numbers \n"
#       "2.Passport Numbers \n"
#       "3.Car Numbers \n"
#       "4.Mobile numbers \n"
#       )
# aadhar_numbers =set()
# passport_numbers=set()
# car_numbers=set()
# mobile_numbers=set()
#
# if selected_option == '1':
#     aadhaar_no = input("Enter your aadhar number:")
#     aadhar_numbers.add(aadhaar_no)
#     print("Aadhar number added successfully")
# elif selected_option == '2':
#     passport_no = input("Enter your passport number:")
#     passport_numbers.add(passport_no)
#     print("Passport number added successfully")
# elif selected_option == '3':
#     car_no = input("Enter your car number:")
#     car_numbers.add(car_no)
#     print("Car number added successfully")
# elif selected_option == '4':
#     mobile_no = input("Enter your mobile number:")
#     mobile_numbers.add(mobile_no)
#     print("Mobile number added successfully")
# else:
#     print("You have selected invalid operation, please try again")
#
# print(aadhar_numbers)
# print(car_numbers)
# print(mobile_numbers)
# print(passport_numbers)

#EMAPK6789J
#first characters should be alphabets and next 4 characters should be numbers and last character should be alphabet

# 1 api it used to take 6-8 hours
# 300 * 8 ==> 2400 => 100days
# 300*3==> 900/60-> 15 hours --> 10-15mins
# wrote a python which will generate script in 5mins


# for x in range(1,5): # 1,2,3,4 #
#     for y in range(1,5): # 1,2,3,4
#         if x == 1:
#             #break
#             continue
#     print(x, y)
    # 1, 1
    # 2, 4
    # 3, 4
    # 4, 4



# function definition
def even_numbers(n):
    for i in range(1,n):
        if i%2==0:
            print(i, end=' ')
n=int(input("Enter a value"))
even_numbers(n) # function calling
print()
even_numbers(30)
print()
# even_numbers(10)
# print()
# even_numbers(5)
