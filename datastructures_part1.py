b1=bytes([10,20,30,40])
print(type(b1))
b2=bytes([0,3,4,55,254])
print(b2[3])
print(b1[-1])
b2[3] = 123
print(b2)
