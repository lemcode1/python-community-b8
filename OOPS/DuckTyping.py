
class Duck:
    def talk(self):
        print("Quack.... Quack....")

class Dog:
    def talk(self):
        print("Bow.... Bow....")

class Cat:
    def talk(self):
        print("Meow..... Meow.....")

cat = Cat()
dog = Dog()
duck = Duck()

animal_objs = [cat,dog,duck]
for animal in animal_objs:
    animal.talk()