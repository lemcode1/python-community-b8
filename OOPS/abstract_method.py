from abc import *

class SuperMarket:
    @abstractmethod
    def basket(self):
        pass

class Customer(SuperMarket):
    def basket(self):
        print("Fill it groceries")

# supermarket_obj = SuperMarket()
# supermarket_obj.basket()


class A: # concrete class
    def method1(self): # concrete method
        print("Inside class a method1")
    def method2(self): # concrete method
        print("Inside class a method2")
    def method3(self): # concrete method
        print("Inside class a method3")

class B(ABC): # abstract class
    def m1(self): # concerete method
        print("Inside class B m1")
    def m2(self): # concrete method
        print("Inside class B m2")
    @abstractmethod
    def m3(self):   # abstract method
        pass

b_obj = B()
b_obj.m1()