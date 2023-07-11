# String handling
name = "Nani"
print(name[1])
print(name[0:3])
print(name + " yedumati")
# print(name + 10)
print(len(name))
first_name = "kasi"
last_name = " yedumati,3 "
print(last_name)
#last_name = last_name.strip()
last_name = last_name.lstrip()
# last_name = last_name.rstrip()
print(last_name)

sentence = "Python is program high level interpreted programming language"
print(sentence.find("program"))
print(sentence.find("java"))
# if sentence.find("java")!= -1:
#     print("word is found")
# else:
#     print("word is not found")
print(sentence.index("program"))
# print(sentence.index("java"))
print(sentence.find("program",17,59))
print(sentence.rfind("program"))

print(sentence.count("program"))
print(sentence.count("program",17,59))

