class Parent:

    def parent_method(self):
        print("Parent method")

class Child(Parent): # extending parent class

    def child_method(self):
        print("Child method")

parent_obj = Parent()
parent_obj.parent_method()

child_obj = Child()
child_obj.child_method()
child_obj.parent_method()

