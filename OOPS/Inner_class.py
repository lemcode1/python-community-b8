class University:

    def __init__(self, name, website, helpdesk, address):
        print("inside universitiy constructor")
        self.name = name
        self.website = website
        self.helpdesk = helpdesk
        self.address = address

    def call_dept(self):
        dept = self.Department("ECE","ECE001", "Electronics")
        print(dept.dept_test())

    class Department:
        def __init__(self, name, code, subject):
            print("inside dept constructor")
            self.name = name
            self.code = code
            self.subject = subject

        def dept_test(self):
            print("inside inner class dept test")


university_obj = University("lemcodoe", "www.lemcode.com", "6302193992", "Online")
university_obj.call_dept()


class Car:
    def __init__(self): # outer class constructor
        print("Outer class Car object created")

    def car_test(self):
        engine = self.Engine()
        engine.engine_test()

    class Engine:  # inner class
        def __init__(self): # innner class constructor
            print("Inner class Engine object created")

        def engine_test(self): # inner instance method
            print("Inside inner class instance method")


# car = Car()
# engine_obj = car.Engine()  # creating object for Engine class
# engine_obj.engine_test()

