# class Book:
#     def __init__(self, pages):
#         self.pages = pages
#
#     def __add__(self, other): # javabook, pythonbook
#         return self.pages + other.pages
#
#
# java_book = Book(100)
# python_book = Book(200)
# print("Total number of pages :",java_book+python_book) # trying to concatinate two objects

# Rational number 1/3, 2/3, 2/0 ==> 2
class Rational:
    def __init__(self, p=1, q=1):
        self.p = p
        self.q = q

    def __add__(self, other):
        s = Rational()
        s.p = self.p * other.q + self.q * other.p  # 2*5 + 3*2 = 16
        s.q = self.q * other.q    # 3*5 => 15
        return s

# rational1 = Rational(2,3) # 1/3
# rational2 = Rational(2,5) # 2/3
# sum_of_numbers = rational2 + rational1
# print(sum_of_numbers.p, "   ", sum_of_numbers.q)

# 9/9 ==> 1


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __ge__(self, other):
        return self.marks >= other.marks

    def __lt__(self, other):
        return self.marks < other.marks

    def __le__(self, other):
        return self.marks <= other.marks


student_list = []
N = int(input("How many student you want to enter:"))
for i in range(1,N+1):
    print("Enter student ",i, " info: ")
    name = input("Enter Student name: ")
    marks = int(input("Enter Student marks: ")) # string type
    student_obj = Student(name, marks)
    student_list.append(student_obj)

print("Total no of students are ",len(student_list))
print("Total students are ",student_list)
# logic to find our rank1 and rank2
rank1_obj = student_list[0]
rank2_obj = student_list[1]
sorted_list = sorted(student_list, reverse=True)
print("Rank1 object is ", sorted_list[0].name)
print("Rank2 object is ", sorted_list[1].name)
# for student in student_list:
#     if student>rank1_obj:
#         rank2_obj = rank1_obj
#         rank1_obj = student
#     elif rank1_obj > student > rank2_obj:
#         rank2_obj = student
#
# print("Rank1 object is ", rank1_obj.name)
# print("Rank2 object is ", rank2_obj.name)



# kasi_obj = Student("Kasi", 66)
# naga_obj = Student("Naga", 78)
# durga_obj = Student("Durga", 99)
# gopi_obj = Student("Gopi", 98)
# rishika_obj = Student("Rishika", 100)
# pavani_obj = Student("Pavani", 96)
# lingaiah_obj = Student("Lingaiah", 93)
# prabhakar_obj = Student("Prabhakar", 92)
# ravi_obj = Student("Ravi", 32)

# student_list = [kasi_obj, naga_obj,durga_obj,gopi_obj,rishika_obj,pavani_obj,lingaiah_obj,prabhakar_obj,ravi_obj]



# If anyone got <35 then he is fail
# Find top 2 ranks



# if(kasi_obj>=naga_obj):
#     print("Kasi marks are greater than Naga")
# else:
#     print("Naga marks are greater than Kasi")


# WAP to overload multiplication operator to work on employee objects
# Employee , TimeSheet
# 200 * 28 ==> 5600
# emp.salary * timesheet.days ==> final salary

class Employee:
    def __init__(self, name, oneday_salary):
        self.name = name
        self.oneday_salary = oneday_salary

    def __mul__(self, other):
        return self.oneday_salary * other.noof_days_worked

class TimeSheet:
    def __init__(self, name, noof_days_worked):
        self.name = name
        self.noof_days_worked = noof_days_worked
#
# employee_obj = Employee("Nani", 300)
# timesheet_obj = TimeSheet("Nani", 23)
# # 300*23 ==> 6900
# # print("Current month salary of ",employee_obj.name, " is ",employee_obj.oneday_salary * timesheet_obj.noof_days_worked)
# print("Current month salary of ",employee_obj.name, " is ",employee_obj * timesheet_obj)








