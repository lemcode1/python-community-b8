# import module1,module2
# import module1 as m1
# from module1 import add,factorial
from module1 import add, factorial, wish_message as wm
import module1, module2 as m2

# sum = m1.add(10,30)
sum=add(10,20)
print(sum)

print(factorial(5))

wish= wm("good afternoon", "Java")
print(wish)
print(m2.fun1())
