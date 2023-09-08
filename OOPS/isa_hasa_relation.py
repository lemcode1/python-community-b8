class Engine:
    def __init__(self, cc, mileage):
        self.cc = cc
        self.mileage = mileage

    def engine_info(self):
        print("Engine cc is ", self.cc , " and milage it gives is ", self.mileage)


class Car:
    def __init__(self, name, model, color, price, engine):
        self.name = name
        self.model = model
        self.color = color
        self.price = price
        self.engine = engine # has a relationship between car and engine

    def get_car_info(self): # getCarInfo # camelcase naming convenstion
        print("Name of car is {name} model is {model} color is {color} and price is {price} ".format(name = self.name, \
                                                                                model= self.model, color = self.color, price = self.price))



class Person: # parent/super class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat_drink(self):
        print("Person eats biryani and drink beer")


class Employee(Person):# child/sub class
    def __init__(self, person_name, person_age, empno, salary, car):
        super().__init__(person_name, person_age) #
        self.empno = empno
        self.salary = salary
        self.car = car   # has-a relationshp between employee and car

    def work(self):
        print("Employee is working on python development")

    def emp_info(self):
        print("Employee name ,",self.name)
        print("Employee age ,", self.age)
        print("Employee no ,", self.empno)
        print("Employee salary ,", self.salary)
        self.car.get_car_info()

engine_obj = Engine("6500cc", "25KM")
car_obj = Car("Innova", "modelname", "white", 2000000.00, engine_obj)
employee_obj = Employee("Nani", 24, 1234, 65000.00, car_obj)
employee_obj.eat_drink()
employee_obj.work()
employee_obj.emp_info()




