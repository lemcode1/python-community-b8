
class Calculator:
    # def sum(self, a,b):
    #     return a+b

    # def sum(self, a, b, c=None, d=None):
    #     s= a+b
    #     if c==None:
    #         return s
    #     else:
    #         return s+c
    #     # return a+b+c
    def sum(self, *a):
        total_sum = 0
        for val in a:
            total_sum = total_sum + val
        print("Sum is ", total_sum)
        return total_sum

a = 'arithmatic'
calculator_obj = Calculator()
print(calculator_obj.sum(10,20))
print(calculator_obj.sum(10,20,30))