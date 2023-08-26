
class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def eatndrink(self):
        print("Person eats biryani and drink beer/wine")


class Employee(Person):
    def __init__(self, name, gender, age, empno, empsal):
        super().__init__(name, gender, age) # calling parent class constructor
        self.empno = empno
        self.empsal = empsal

    def work(self):
        print("Work on python")

    def empinfo(self):
        print("Emp name ",self.name)
        print("Emp gender ", self.gender)
        print("emp age ", self.age)
        print("Emp number ", self.empno)
        print("emp salary ", self.empsal)

employee_obj = Employee("Raj", "Male", "26", "1234", 260000.00)
employee_obj.eatndrink()
employee_obj.work()
employee_obj.empinfo()

