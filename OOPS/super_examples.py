class Parent:
    a = 10
    def __init__(self):
        self.b = 10

    def m1(self):
        print('Parent instance method')

    @classmethod
    def m2(cls):
        print('Parent class method')

    @staticmethod
    def m3():
        print("Parent static method")


class Child(Parent):
    a = 999

    def __init__(self):
        # self.b = 888
        super().__init__()
        print(super().a)  # Accessing the 'a' class variable from the parent class
        super().m1()
        super().m2()
        super().m3()
        # super().b  # calling instance variable using super() is not possible, if at all
        # we want to call we need to create and object of super class
        parent_instance = Parent()  # Create an instance of the parent class
        print(parent_instance.b)  # Accessing the 'b' instance variable in the parent class
        print(self.b)


child_obj = Child()