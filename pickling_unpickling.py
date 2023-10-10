# writing and reading state of object by using pickle module
import pickle

class Employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def display(self):
        print(self.eno, " ", self.ename, " ", self.esal, " ", self.eaddr)

# pickling
with open("employee_data.txt", "wb") as file:
    emp = Employee(111, "Kasi", "1000", "hyd")
    emp2 = Employee(123, "Kasi", "1000", "hyd")
    pickle.dump(emp, file)
    pickle.dump(emp2, file)
    print("Pickling of employee object is completed")

with open("employee_data.txt", "rb") as file:
    obj = pickle.load(file)
    print("unpickling of employee object is completed")
    obj.display()
    obj = pickle.load(file)
    print("unpickling of employee object is completed")
    obj.display()
