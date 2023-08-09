# anagram
# Race, Care  --> Anagram
# Race, acer, cear, erac, care
employees_list = [{
    "name":"kasi",
    "empid":1234,
    "salary":20000,
    "yearofjoining": 2020
    },{
    "name":"kasi",
    "empid":1111,
    "salary":20000,
    "yearofjoining": 2023
    },{
      "name":"nani",
    "empid":1235,
    "salary":23000,
    "yearofjoining": 2023
    },
    {
        "name": "naveen",
        "empid": 1222,
        "salary": 3000,
        "yearofjoining": 2019
    }
]
def search_emp_by_year(emp_obj):
    if emp_obj.get('yearofjoining')>=2020 and emp_obj.get('yearofjoining')<=2023:
        return True
    else:
        return False

def search_emp_by_salar(emp_obj):
    if emp_obj.get('salary')<10000:
        return True
    else:
        return False


# recent_employees = filter(search_emp_by_year, employees_list)
# high_salries_employees = filter(search_emp_by_salar, employees_list)
# print(list(recent_employees))
# print(list(high_salries_employees))

# PTR
# price  -->
# time  --> year and months
# rate of interest --> 18%
# 10000  # 01-01-2021 # 18% # 08-08-2023
# date
def simple_interest(borrowed_date, amount, interest, return_date):
    borrowed_days,borrowed_month, borrowed_year = borrowed_date.split('-') # ['01','01','2021']
    return_days, return_month, return_year = return_date.split('-')
    days = int(return_days)-int(borrowed_days)
    month = int(return_month)-int(borrowed_month)
    year = int(return_year) - int(borrowed_year)
    time = float(str(year)+"."+str(month)) # 1.7 # 2 year 7months

    simple_interest = (amount*time*interest)/100
    return simple_interest

borrowed_date = input("Please enter borrrowed date:")
amount = float(input("Enter amount:"))
rate_of_interest = eval(input("Enter rate of interest in % :"))
return_date = input("Return date:")
interest = simple_interest(borrowed_date, amount, rate_of_interest, return_date)
print("Simple interest is :",interest)
final_amount= amount+interest
print("final amount is ",final_amount)

print(zip("abc","xyz"))



