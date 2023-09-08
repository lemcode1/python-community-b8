
class Nokia:
    def phone_operating(self):
        print("Using keypad you need to operate")


class NokiaPro(Nokia): # smartphone
    def phone_operating(self):  # It is overriding the behaviour of parent class
        print("Using touch you need to operate")
        super().phone_operating()

nokiapro_obj = NokiaPro()
nokiapro_obj.phone_operating()

nokia_obj = Nokia()
nokia_obj.phone_operating()



