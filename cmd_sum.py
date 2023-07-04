from sys import argv

print(argv)
print(len(argv))
if len(argv)==3:
    print(argv[1])
    print(argv[2])
    print("Sum of two given values is ", int(argv[1])+int(argv[2]))
else:
    print("Syntax is incorrect Ex : python filenmae.py val1 val2")