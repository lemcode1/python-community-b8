def generate_firstn(num):
    n=1
    while n<=num:
        yield n
        n = n+1
def gen_abc():
    yield 'A'
    yield 'B'
    yield 'C'

# 0 1 1 2 3 5 8 13,21.......
def fibonacci_numbers(num):
    a,b = 0,1
    while b<=num:
        yield a
        a,b = b,a+b

# gen_output = gen_abc()
# print(type(gen_output))
# print(next(gen_output))
# print(next(gen_output))
# print(next(gen_output))
# for value in gen_output:
#     print(value)

# generated_numbers = generate_firstn(1000)
generated_numbers = fibonacci_numbers(99)
list_values = list(generated_numbers)  # convert generator into list
for value in generated_numbers:
    print(value)
