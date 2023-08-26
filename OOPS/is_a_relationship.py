
class Parent:
    a = 10 # static variable of Parent
    def __init__(self):
        self.b = 10  # instance variable of Parent

    def house(self):
        print("House owned by parent")

    @classmethod
    def land(cls):
        print("land owned by parent")

    @staticmethod
    def cash():
        print("Cash owned by parent")


class Child(Parent): # IS-A relationship

    # def __init__(self):
    #     super().__init__()

    def play_football(self):
        print("Child is playing football")

child_obj = Child()
child_obj.house()
child_obj.land()
child_obj.cash()
print(child_obj.a)
print(child_obj.b)
child_obj.play_football()



