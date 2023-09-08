class Parent:
    def __init__(self):
        print("parent constructor")

class Child(Parent):
    def __init__(self):
        print("Child constructor")

child = Child()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def m1(self):
        print("Inside parent m1 method")

class Doctor(Person):
    def __init__(self, name, age, designation, salary):
        super().__init__(name, age)
        self.designation = designation
        self.salary = salary

    def m2(self):
        print("Inside doctor m2 method")

doctor = Doctor("nani", 36, "Cardialogist", 3000000)
doctor.m2()

# a=10
# a="kasi"
