class Dog:
    def __init__(self):
        print("inside dog constructor")

    def display_dog(self):
        print("inside display dog")

class Student:

    def __init__(self, name, rollno, marks):
        print("Insdie constructor execution")
        self.name = name
        self.rollno = rollno
        self.marks = marks

    # def __init__(self):
    #     pass

    def display_employee(self):
        self.mail = "test@gmail.com"
        print("Inside dispaly employee")
        print("Hello my name is ",self.name)
        print("My Rollno is ", self.rollno)
        print("Marks are ", self.marks)

    def talk(self):
        self.mobile_no = "345678"
        print("i am talking student on phone ",self.mobile_no)

# student_obj = Student()
# student_obj.talk()
# print(student_obj.__dict__)


student_obj = Student("Nani", "1234","98")
student_obj.mail = "nani@gmail.com"
student_obj.mobil_no = 123456
print(student_obj.__dict__)

student_obj2 = Student("Ravi", "1235","99")
student_obj2.display_employee()
print(student_obj2.__dict__)
# student_obj3 = Student("Raju", "1235","99")
# student_obj3.display_employee()
dog = Dog()
dog.display_dog()
dog.display_dog()
dog.display_dog()
dog2 = Dog()