class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Gender :", self.gender)

class Student(Person):
    def __init__(self, name, age, gender, rollno, marks):
        super().__init__(name, age, gender)  # calling the super class constructor using super()
        self.rollno = rollno
        self.marks = marks

    def display(self):
        super().display() # calling the super class method using super()
        print("Rollno : ", self.rollno)
        print("Marks : ", self.marks)

student_obj = Student("kasi", 26, "Male", 1234, 99.0)
student_obj.display()




