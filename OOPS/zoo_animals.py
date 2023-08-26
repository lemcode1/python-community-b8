
class Animal:
    def __init__(self, animal_name, legs):
        self.animal_name = animal_name
        self.legs = legs

    def dispaly_animal_behaviour(self):
        print("Inside animal behaviour")


class Zoo:

    def __init__(self, zoo_name , animal_name, legs):
        self.animal = Animal(animal_name, legs)

    def zoo_info(self):
        print("animal name is ",self.animal.animal_name)
        print("animal legs are ", self.animal.legs)

zoo = Zoo("nehru zoo" , "penguin", "2")
zoo.zoo_info()

# Person has a Car
# University has a Department
# Employee has a Bike
# Person has a Iphone