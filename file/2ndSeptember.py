# file_path = r"D:\mycode\python\Daily_Python_Improve\employees.txt"

# file_path = r"D:\mycode\python\Daily_Python_Improve\server.txt"
# import os
# print("File size:", os.path.getsize(file_path), "bytes")
# with open(file_path , "r") as file:
#     print("File opened successfully!")
#     for line in file:
#         print(line.strip())

# employee = input("Enter Employee's name: ")
# import os
# with open(file_path , "r") as file:
#     found = False
#     for i in file:
#         name , salary = i.strip().split(",")
#         if name.lower() == employee.lower():
#             print(f"salary of {employee} is {salary}")
#             found = True
#             break
#     if not found:
#         print(f"{employee} is not found ")

#----------------------------------------------------------Calculate the Average Salary------------------------------

# import os
# with open(file_path , "r") as file:
#     total_salary = 0
#     for i in file:
#         salary = int(i.strip().split(",")[1])
#         total_salary+=salary
# print(f"total salary {total_salary}")
# -----------------------------------------------------------------------Find 1 word from logs file------------------------------
file_path = r"D:\mycode\python\Daily_Python_Improve\server.txt"
import os
count = 0
with open(file_path , "r") as file:
    for line in file:
        if "ERROR" in line.upper():
            count+=1
print(f"count is : {count}")


        