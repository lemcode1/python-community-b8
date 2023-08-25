from Utility import *
class Student:
    """ This class used to display the marks and grade of the student """
    school = "ZPHS"

    @classmethod
    def display_school(cls):
        print("shoolname is ", cls.school)


    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setRollNo(self, rollno):
        self.rollno = rollno

    def getRollNo(self):
        return self.rollno

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks

    # def __init__(self, name, rollno, marks): # instance variable
    #     self.name = name   # instance variable
    #     self.rollno = rollno  # instance variable
    #     self.marks = marks    # instance variable

    def display(self):   # instance method
        print("Hi ", self.name)
        print("Your marks are ", self.marks)
        converted_date = Utility.convert_date_format("03-NOV-2023")
        print("converted date is ", converted_date)
    # there Business anaylyst/ solution architect /  Product owner

    def grade(self):  # instance method
        if self.marks>=90:
            print("You got distinction")
        elif self.marks>=65:
            print("You got first class")
        elif self.marks>=50:
            print("You got second class")
        elif self.marks>=35:
            print("You got third grade")
        else:
            print("You are failed")


name = input("Enter your name:")
marks = float(input("Enter marks:"))
s = Student()
s.setName(name)
s.setMarks(marks)
#
s.display()
s.grade()

# calling class method
# Student.display_school()
# Student.display_school() # calling classmethod with object




