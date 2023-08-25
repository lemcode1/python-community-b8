import sys
# sys.getrefcount(objectreference)
class CountObjectReference:
    pass

t1=CountObjectReference()
t2=t1
t3=t1
t4=t1
print(sys.getrefcount(t1))





class TestDestruct:

    def __init__(self):
        print("Inside constructor : Object initialization")

    def write_data_to_database(self):
        print("Inside method: write_data_to_database")

    def __del__(self):
        print("Fullfilling last wish and peformaing the clean up activities")


# obj1 = TestDestruct()
# obj1.write_data_to_database()
# obj1 = None  # None
# # obj2 = obj1  # re-referencing the object
# # whenever your object is rereferenced and object is None then those objects eligible for garbage collection
# print("end of application")

# Inside constructor : Object initialization
# Inside method: write_data_to_database
# end of application
# Fullfilling last wish and peformaing the clean up activities


