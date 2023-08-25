
class Iphone:
    ringtone = "iphone ringtone"
    # symbol = "apple"

    def __init__(self, ram, model, colour, size):
        self.ram = ram
        self.model = model
        self.colour = colour
        self.size = size
        # Iphone.symbol = "iphone"   # static variables inside constructor, but its not recommended to create here

    def make_audio_call(self):
        pass
    def display_specifications(self):
        Iphone.symbol = "apple"    # static variable inside instance method
        print("Ram is ", self.ram)
        print("Model is ", self.model)
        print("Colour is ", self.colour)
        print("Size is ", self.size)

    @classmethod
    def test1(cls):
        print("class method inside test1")
        cls.symbol = "apple"   # static variable create inside class method
        Iphone.symbol = "apple"

    @staticmethod
    def test2():
        print("inside static method")
        Iphone.symbol = "apple"

iphone_14 = Iphone("8GB", "iphone_14_pro_max", "black","5.7inch")
iphone_14.display_specifications()
print(Iphone.symbol)
# Iphone.symbol = "half-cut-apple"  # modifying static variable
iphone_14.symbol = "abc-apple" # this creates a new instance variable called symbol
print(Iphone.ringtone)
print(iphone_14.__dict__)
del iphone_14.symbol  # it is deleting instance variable
del Iphone.symbol   # it deletes static variable
print(iphone_14.__dict__)
print(Iphone.symbol)  # this is static variable
print(iphone_14.symbol)  # this is instance variable


# iphone_xr = Iphone("8GB", "iphonexr", "white","5.1inch")
# iphone_xr.display_specifications()
# print(iphone_xr.ringtone)
# print(iphone_xr.symbol)
# # print(Iphone.ram)   # error because we cant access instance variables with class
# print(Iphone.symbol)
#
# iphone_14_pro_max = Iphone("8GB", "iphone_14_pro_max", "black","5.7inch")
# iphone_14_pro_max.display_specifications()
# print(iphone_14_pro_max.ringtone)
# print(iphone_14_pro_max.symbol)
# print("before delete size ",iphone_14_pro_max.size)
# del iphone_14_pro_max.size
# # print(iphone_14_pro_max.size)
# print(iphone_14_pro_max.__dict__)
# print(iphone_xr.__dict__)

# iphone_14 = Iphone("8GB", "iphone_14_pro_max", "black","5.7inch")
# iphone_14.storage = "256gb"
# print(iphone_14.ringtone)
# print(Iphone.symbol)
# print(iphone_14.ram)
# print(iphone_14.__dict__)
# print(Iphone.__dict__)
# print(Iphone.ram)
