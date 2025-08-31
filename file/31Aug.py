# name = input("Enter your name: ")
# age = int(input("Enter your Age: "))

# if  age>18:
#     print(f"Dear {name} you are eligible for vote")
# elif  age<18:
#     print(f"Dear {name} you are not eligible for vote")
# else:
#     print("Invalid Age")

#---------------------------------------FOR Loop------------------------------------------------------------------------

# num = int(input("Enter your range: "))
# for i in range(num):
#     if(i%2 == 0):
#         print(i)

#-----------------------------------------Factorial Number--------------------------------------------------------------------------

# fact = int(input("Enter a number : "))

# res = 1
# for i in range(1 , fact+1):
#     res *=i
# print(f"Factorial of {fact} is {res}")

# ----------------------------------------------Read a File----------------------------------------------------------------------------------------
file_path = r"D:\mycode\python\Daily_Python_Improve\Bike.txt"
# import os
# with open(file_path , "r") as file:
#     for i in file:
#         print(i.strip())

#-------------------------------------------------Write A File------------------------------------------------------------------------------
import os
user_input = input("Enter text : ")
with open(file_path , "w") as file:
    file.write(user_input + "\n")
    print("Hii this is for testing purpose only")