# how to call method of a particular super class ?
# class A:
#     def m1(self):
#         print("A class method")
#
# class B(A):
#     def m1(self):
#         print("B class method")
#
# class C(B):
#     def m1(self):
#         print("C class method")
#
# class D(C):
#     def m1(self):
#         # a = A()
#         # a.m1()
#         A.m1(self)
#         # super(A.self).m1()
#
# d_obj = D()
# d_obj.m1()


# in child class static method we are not allowed to super() generally (but there is a special way)
# class Parent:
#     def __init__(self):
#         print("Parent class constructor")
#
#     def m1(self):
#         print("Parent instance method")
#
#     @classmethod
#     def m2(cls):
#         print("Paretn class method")
#
#     @staticmethod
#     def m3():
#         print("Parent static method")
#
# class Child(Parent):
#     @staticmethod
#     def m1():
#         super().m3()
#         super().m1()
#         super().m2()
#
# Child.m1()



# how to call parent class static method from child class static method by using super()

class A:
    @staticmethod
    def m1():
        print("Parent static method")

class B(A):
    @staticmethod
    def m2():
        super(B,B).m1()

B.m2()


