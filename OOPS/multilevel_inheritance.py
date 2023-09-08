
class GrandParent: # logically and phisically only one method
    def grand_parent_method(self):
        print("Inside grand parent method")

class Parent(GrandParent): # logically 2 methods but physically only one method will be there
    def parent_method(self):
        print("Inside parent method")


class Child(Parent):  # logically 3methods and physically only one method will be there
    def child_method(self):
        print("Inside child method")

# how to call parent_method
parent_obj = Parent()
parent_obj.parent_method()
child_obj = Child()
child_obj.parent_method()

# how to call grand_parent_method
grandparent_obj = GrandParent()
grandparent_obj.grand_parent_method()
parent_obj.grand_parent_method()
child_obj.grand_parent_method()

# how to call child_method
child_obj.child_method()
