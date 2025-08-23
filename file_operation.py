                                                    # Writing to a file
# file_path = r"D:\mycode\python\Daily_Python_Improve\file.txt"

# with open(file_path , "w") as file:
#     file.write("this is a new file I am writting hello boss")
#     file.write("This is a 2nd time I am writting my file related things")

                                                    #Checking File Existence
import os
import time
file_path = r"D:\mycode\python\Daily_Python_Improve\file.txt"

if os.path.exists(file_path):
    print("File exist")
    print("appending the lines......")
    time.sleep(3)
    with open("file.txt" , "a") as file:
        file.write("This is a new file")
    print("Comments added successfully.....")
else:
    print("Not exist")
