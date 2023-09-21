from abc import ABC, abstractmethod

class Vehicle(ABC): # abstract class
    @abstractmethod
    def no_of_wheels(self):
        pass

class Bus(Vehicle):
    def no_of_wheels(self):
        return 4


bus_obj = Bus()
print(bus_obj.no_of_wheels())


