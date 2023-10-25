import random
import time

names = ['Nani', 'JrNtr','Prabhas', 'PavanKalyan']
languages = ['English', 'Hindi', 'Telugu', 'Kannada']

# using list approach
def people_list(num):
    results = []
    for i in range(1, num):
        person = {
            "id": i,
            "name" : random.choice(names),
            "language" : random.choice(languages)
        }
        results.append(person)
    return results


# using generator approach
def people_generator(num):
    for i in range(1,num):
        person = {
            "id": i,
            "name": random.choice(names),
            "language": random.choice(languages)
        }
        yield person

# t1 = time.time()
# results = people_list(10000000)  # list approach
# t2 = time.time()
# print("Time Taken is {}".format(t2-t1))

t1 = time.time()
results = people_generator(10000000) # generator approach
t2 = time.time()
print("Time Taken is {}".format(t2-t1))

# for value in results:
#     print(value)

