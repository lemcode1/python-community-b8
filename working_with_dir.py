# To know current working directory
import os
cwd = os.getcwd()
print("Current working directory ", cwd)
# To create a sub directory inside the current directory
# os.mkdir("C:\Kasi\lemcode\Trainings\Python\python-community-b8\OOPS\subtest")
#  to create multiple directories like subfolder1 in the subfolder2
# os.makedirs("subfolder1/subfolder2/subfolder3")

# To remove a directory
# os.rmdir("C:\Kasi\lemcode\Trainings\Python\python-community-b8\subfolder1\subfolder2\subfolder3")
# To remove multiple directories in the path
# os.removedirs("subfolder1/subfolder2")

# To rename a directory/folder
os.rename("subtest", "newsubtest")

# Create a folder name is employee_data and create a CSV file(emp.csv) for 10 employees, read and write data,
# I want only the employees whose salary is above 3000
# ENAME	DNAME	JOB	EMPNO	HIREDATE	LOC   salary
# ADAMS	RESEARCH	CLERK	7876	23-MAY-87	DALLAS   2000
# ALLEN	SALES	SALESMAN	7499	20-FEB-81	CHICAGO  1000
# BLAKE	SALES	MANAGER	7698	01-MAY-81	CHICAGO      3000
# CLARK	ACCOUNTING	MANAGER	7782	09-JUN-81	NEW YORK 3500
# FORD	RESEARCH	ANALYST	7902	03-DEC-81	DALLAS   4000
# JAMES	SALES	CLERK	7900	03-DEC-81	CHICAGO      500