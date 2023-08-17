# human being
class Employee:
    """
    Creating this classs to explain and implement the behaviour/actions of any humanbeing
    """
    def __init__(self, emp_no, name, mobile_no, mail):
        self.emp_no = emp_no
        self.name = name
        self.mobile_no = mobile_no
        self.mail = mail

    def add_employee(self):
        print("Inside class add employee method")
        print(self.emp_no)
        print(self.name)
        print(self.mobile_no)


    def update_employee(self):
        print("Inside class add employee method")
#
# obj1 = Employee() # creating an object
# obj1.add_employee() # calling the method inside class
# print(id(obj1))

# obj2 = Employee() # creating an object
# obj2.add_employee() # calling the method inside class
# print(id(obj2))

emp1 = Employee(1234,"kasi","123456","test@gmail.com") # we are creating an object with attributes
emp1.add_employee()

emp2 = Employee(1235,"Ravi","123234456","test2@gmail.com") # we are creating an object with attributes
emp2.add_employee()


# Create a class called Dog , it should bark, it should eat, it should drink, it should sleep
# properties name, bevarage, food, time
#
