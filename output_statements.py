# print("lin1")
# print()
# print("lin2")
# print("hello \tworld")
# print("hello"+ "world")
# # print("hello"+ 123)
# print("hello world", "kasi yedumati","python program",sep=':')
# print("hello world", "kasi yedumati","python program",sep='and')
# print("hello world", "kasi yedumati","python program",sep='%')
# print("hello world", "kasi yedumati","python program",sep='\n')
# print("abc",end=" ")
# print("xyz")
# fruits=['apple','grapes']
# print(fruits)
# a=100
# b=200
# print("a value is ",a,"b values is ",b)
# s1="python"
# s2="java"
# print("I am learning ",s1, " and ",s2)
s1="python"
s2="java"
print("I am learning %s" %(s1))
print("I am learning %s and %s" %(s1,s2))
a="testing python"
b=200
print("a value is %s b values is %i" %(a,b))

account_balance = 120000
credit_amount = 2000
account_no = "1475XXXXX"
account_balance = account_balance + credit_amount
print(account_balance)
print(credit_amount)
print("Account %s has been credited with %i and your current balance is %i" %(account_no,credit_amount,account_balance))
print("Account {0} has been credited with {1} and your current balance is {2}".format(account_no,credit_amount,account_balance))
print("Account {account_no} has been credited with {credit_amt} and your current balance is {current_bal}".
      format(account_no= account_no,credit_amt =credit_amount,current_bal = account_balance))
print("Account {x} has been credited with {y} and your current balance is {z}".
      format(x= account_no,y =credit_amount,z = account_balance))

name="kasi yedumati"
salary=20000.00
pf_amount=1200.00
# Dear Kasi Yedumati your current month salary is 20000.00 and pf amount is debited 1200.00
print("Dear %s your current month salary is %f and pf amount is debited %f" %(name,salary,pf_amount))
print("Dear {x} your current month salary is {y} and pf amount is debited {z}".format(y=salary,x=name,z=pf_amount))
print("Dear {0} your current month salary is {1} and pf amount is debited {2}".format(name,salary,pf_amount)) # [name,salary,pf_amount]