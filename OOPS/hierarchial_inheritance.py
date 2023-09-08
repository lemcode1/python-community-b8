class GrandParent:
    def grand_parent_method(self):
        print("Grand parent method")

class Parent1(GrandParent): # logically 1 method physically total 2methods
    def parent1_method(self):
        print("parent1 method")

class Parent2(GrandParent):
    def parent2_method(self):
        print("parent2 method")

class Child1(Parent1): # logically 3methods grand_parent_method,parent1_method, child1_method
    def child1_method(self):
        print("child1 method")

class Child2(Parent1): # logically 3methods grand_parent_method,parent1_method, child2_method
    def child2_method(self):
        print("child2 method")


child2_obj = Child2()
child2_obj.child2_method()
child2_obj.parent1_method()
child2_obj.grand_parent_method()




