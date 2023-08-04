def find_two_largest_numbers(input_list):
    largest1 = max(input_list)
    input_list.remove(largest1)
    # Remove the first occurrence of largest1 from the list
    largest2 = max(input_list)
    return largest1, largest2

input_list = [1, 2, 3, 4, 10, 20, 30]
largest1, largest2 = find_two_largest_numbers(input_list)
print(f"Output: {largest1}, {largest2}")


#10. What will be the output of the following Python code?
print("abcdef".find("cd")) # 2
print("cd" in "abcdef") # True
print("abcdef".find("cd") == "cd" in "abcdef")
#11. What will be the output of the following Python code?
print("Hello {name1} and {name2}".format(name1 ='foo', name2 ='bin'))

# list1 is
list1=[2, 33, 222, 14, 25]
print(list1[:-1]) # [start:end:step] # [0:-1:1]
