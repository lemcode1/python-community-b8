# simple calculator to perform addition, subtration, multipliction, division

# This function adds two numbers
def add(a,b):
    return a+b

# This function subtracts two numbers
def subtract(a,b):
    return a-b

# This function multplies two numbers
def multiply(a,b):
    return a*b

# This function divides two numbers
def divide(a,b):
    return a/b


print("Select any one operation from below:")
print("1. Addition")
print("2. Subtract")
print("3. Multiplication")
print("4. Division")

while True:
    selected_option = input("Enter option(1/2/3/4):")
    value1 = float(input("Enter first value:"))
    value2 = float(input("Enter second value:"))

    if selected_option in ('1','2','3','4'):
        if selected_option == '1':
            sum_val = add(value1,value2)
            print("sum of {value1} and {value2} is: {sum_val}".format(value1=value1,value2=value2,sum_val= sum_val))

        elif selected_option == '2':
            subtract_val = subtract(value1,value2)
            print("subtraction of {value1} and {value2} is: {subtract_val}".format(value1=value1,value2=value2,subtract_val= subtract_val))

        elif selected_option == '3':
            multiply_val = multiply(value1,value2)
            print("multiply of {value1} and {value2} is: {multiply_val}".format(value1=value1,value2=value2,multiply_val= multiply_val))

        elif selected_option == '4':
            devide_val = divide(value1,value2)
            print("devide_val of {value1} and {value2} is: {multiply_val}".format(value1=value1,value2=value2,devide_val= devide_val))
    else:
        print("Invalid input select any one option (1/2/3/4)")

    next_opertion = input("Hey user, Do you want to perform another operation(yes/no)")
    if next_opertion == 'no':
        break





