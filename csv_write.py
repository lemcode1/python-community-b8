import csv
#
# with open("student_info.csv", "w", newline="") as file:
#     writer_obj = csv.writer(file)
#     writer_obj.writerow(["studentno","name", "address", "mobileno"])
#     n = int(input("Enter number of students:"))
#     for i in range(n):
#         studentno = input("Enter studentno: ")
#         name = input("Enter name: ")
#         address = input("Enter address: ")
#         mobileno = input("Enter mobileno: ")
#         writer_obj.writerow([studentno, name, address, mobileno])
#
# print("writing student data is completed")

# reading data from csv file
# file = open("student_info.csv", 'r')
# reader_obj = csv.reader(file) # returns csv reader object
# data = list(reader_obj)
# for row in data:
#     # print(line)
#     for word in row:
#         print(word, "\t",end='')
#     print()

# Zipping and unzipping files
# below code is used to zip the folder
from zipfile import *
# zip_obj = ZipFile("classroom_recordings.zip", "w", ZIP_DEFLATED)
# zip_obj.write("student_info.csv")
# zip_obj.write("slicing.py")
# zip_obj.write("Sum.py")
# zip_obj.close()
# print("Zipfile is created")

# unzip the folder
zip_obj = ZipFile("classroom_recordings.zip", "r", ZIP_STORED)
# ZIP_STORED represeents unzip operation
file_names = zip_obj.namelist() # it returns all the unzipped files inside the folder
for name in file_names:
    print("File name ", name)
    print("Content inside the file is: ")
    file_obj = open(name, 'r')
    print(file_obj.read())
    print()
    print("=================================")
