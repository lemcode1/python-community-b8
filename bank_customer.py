
class Customer:
    """ Customer class with bank operations """

    bank_name = "icici"

    def __init__(self, name, mobileno, mail, balance, ifsc_code):
        self.name = name
        self.mobileno = mobileno
        self.mail = mail
        self.balance = balance
        self.ifsc_code = ifsc_code

    def deposit(self, amount):
        self.balance = self.balance + amount  # adding the balance to his account
        print("Deposit is successfull, your current balance is : ", self.balance)

    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficient funds, cannot continue this transaction")
        else:
            self.balance = self.balance - amount
            print("Dear customer, ",amount," is debited from your account"," and current balance after withdrawl is ", self.balance)


print("Welcome to ICICI bank")
print("Please insert your card")
customer = Customer("kasi", "12345", "kasi@gmail.com", 0.0, "ICIC0001475")
while True:
    print("1. Deposit")
    print("2. Withdraw")
    option = input("Please select any one option above")
    if option == '1':
        deposit_amount = float(input("How much you want to deposit"))
        customer.deposit(deposit_amount)
    elif option == '2':
        withdraw_amount = float(input("How much you want to withdraw"))
        customer.withdraw(withdraw_amount)
    else:
        print("Please enter a valid option")

pin = input("Please enter the pin")
withdraw_amount = input("How much you want to withdraw")


# create a program to take user inputs for employee and salary and show the final salary