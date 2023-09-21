# Note: Two rules to identify abstract class
# rule1 - It should extend from ABC class
# rule2 - It should have atleast abstract method

# case-1
from abc import *
# class Test: # concrete class
#     pass
#
# test_obj = Test()

# In the above case we can create object for Test class because it is concrete class and it doesn't contain any
# abstract method

# case-2
# class Test(ABC):
#     pass
#
# test_obj = Test()

# in the above case-2 we can create objecct, even it is extended ABC class but it doent have any abstractmethods

# case-3
# class Test(ABC):
#     @abstractmethod
#     def method1(self):
#         pass
#
# test_obj3 = Test()

# In the above case-3 we cant create object because its extending ABC class and having one abstract method

# case-4
# class Test:
#     @abstractmethod
#     def m1(self):
#         pass
#
# test_obj = Test()

# in the above case-4 we can create an object for class contains abstract method becausee we are not extending
# ABC class

# case-5
# class Test:
#     @abstractmethod
#     def m1(self):
#         print("Hello")
#
# test_obj5 = Test()
# test_obj5.m1()


# Case-6
class Vehicle(ABC): # abstract class
    @abstractmethod
    def no_of_wheels(self):
        pass

class BiCycle(Vehicle): # concrete class
    def no_of_wheels(self):
        return 2

class Auto(Vehicle): # concrete class
    def no_of_wheels(self):
        return 3


bycycle_obj = BiCycle()
print(bycycle_obj.no_of_wheels())

auto_obj = Auto()
print(auto_obj.no_of_wheels())


