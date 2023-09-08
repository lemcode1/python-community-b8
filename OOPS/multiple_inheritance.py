class Father:
    def father_method(self):
        print("Inside father method")

    def color_of_parent(self):
        print("Father is in dark colour")

    def gardening(self):
        print("Father is gardening")

class Mother:
    def mother_method(self):
        print("inside mother method")

    def color_of_parent(self):
        print("Mother is in white colour")

    def gardening(self):
        print("Mother is gardening")

    def cooking(self):
        print("Mother is cooking")
class Son(Father, Mother): # multiple inheritance
    def child_method(self):
        print("inside child method")

    def painting(self):
        print("son is painting")

son_obj = Son()
son_obj.child_method()
son_obj.father_method()
son_obj.mother_method()
son_obj.color_of_parent()
son_obj.gardening()
son_obj.painting()
son_obj.cooking()


