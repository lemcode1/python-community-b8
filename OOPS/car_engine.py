
class Engine:
    a=10

    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity

    def m1(self):
        print("Engine related behaviour")

class Car:
    def __init__(self, model, capacity):
        self.engine = Engine(model, capacity)

    def go_for_ride(self):
        print("car using engine class functionality")
        print(self.engine.a)
        print(self.engine.model)
        print(self.engine.capacity)
        self.engine.m1()

car = Car("2007", "350CC")
car.go_for_ride()


