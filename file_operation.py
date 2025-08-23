file_path = r"D:\mycode\python\Daily_Python_Improve\file.txt"                                                  
  # Writing to a file
# file_path = r"D:\mycode\python\Daily_Python_Improve\file.txt"

# with open(file_path , "w") as file:
#     file.write("this is a new file I am writting hello boss")
#     file.write("This is a 2nd time I am writting my file related things")
                                                    #Reading the whole content
# import os
# with open(file_path , "r") as file:
#     content = file.read()
#     print(content.strip())                          # strip is use for read the content line by line
                                                    #Checking File Existence
# import os
# import time
# file_path = r"D:\mycode\python\Daily_Python_Improve\file.txt"

# if os.path.exists(file_path):
#     print("File exist")
#     print("appending the lines......")
#     time.sleep(3)
#     with open("file.txt" , "a") as file:
#         file.write("This is a new file")
#     print("Comments added successfully.....")
# else:
#     print("Not exist")




                                                        #Instead of appending, you can read the content, modify it, and then save the changes
# import os
# import time
# file_path = r"D:\mycode\python\Daily_Python_Improve\file.txt"

# if os.path.exists(file_path):
#     print("file is already exist so we are continue with this file...")
#     with open(file_path , "r") as file:
#         lines = file.readlines()

#     if lines:
#         lines[0] = "this is my line How Can I edit this file.\n"

#     with open(file_path , "w") as file:
#         file.writelines(lines)
#         print("First line modified")
# else:
#     print("Does not exit")



