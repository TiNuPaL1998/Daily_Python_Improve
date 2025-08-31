import os
import time

file_path = r"D:\mycode\python\Daily_Python_Improve\Bike.txt"
#search_value = "823491"  # The value you're looking for

search_value = input("Enter your bike name: ")
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split(":")
            if len(parts) == 2 and parts[1].strip() == search_value:
                brand = parts[0].strip()
                print(f"The brand for price {search_value} is: {brand}")
                break
        else:
            print(f"No brand found with price: {search_value}")
else:
    print("File doesn't exist. Creating new file... Please wait.")
    time.sleep(2)
    with open(file_path, "w") as wr:
        wr.write("ExampleBrand: 000000\n")
    print("File created.")


