# using the OS library
# import the os lib
import os
# using the OS to make folders and navigate them

#  create a folder with mkdir()
if "Test_mkdir.txt" not in os.listdir():
    os.mkdir("Test_mkdir.txt")

# check if a file is in the directory
files = os.listdir()
if "a_file.txt" not in files:
    print("Error: ")

# rename a file os.rename("file to rename", "new file name")
os.mkdir("a_file.txt")
os.rename("a_file.txt", "a_new_file.txt")

# will print all the files in the current directory as a list
print(os.listdir())
# iterate over the list
for item in os.listdir():
    print(item, end=", \n")


