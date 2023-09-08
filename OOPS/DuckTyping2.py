class Duck:
    def talk(self):
        print("Quack... Quack....")

class Dog:
    def bark(self):
        print("Bow... Bow...")

class Person:
    def talk(self):
        print("Hello.. HI")

def call_talk(obj):
    if hasattr(obj, 'talk'):
        obj.talk()
    elif hasattr(obj, 'bark'):
        obj.bark()

duck_obj=Duck()
call_talk(duck_obj)

human_obj = Person()
call_talk(human_obj)

dog_obj = Dog()
call_talk(dog_obj)

