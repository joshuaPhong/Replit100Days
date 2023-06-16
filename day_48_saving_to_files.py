# saving to a file requires three steps
# open
# write
# close
import time

while True:
    f = open("my_file.txt",
             "a+")  # "a+" will write create and append not overwrite
    my_write = input("Enter some text: ")
    f.write(f"{my_write}\n")
    f.close()
    exit_the_program = input("Exit: Y/n")
    if exit_the_program.lower().strip() == "y":
        break


while True:
    # open a text file
    f = open("a_file.txt", "a+")
    # create a variable with user input
    # can we use the split()
    initials = input("Enter your initials: ")
    high_score = input("Enter your high score: ")
    # write to the buffer
    # if using split() access the split like a list with the index
    f.write(f"{initials}, {high_score}, ")
    # close the file. will save the file
    f.close()

    exit_the_program = input("Exit: Y/n")
    if exit_the_program.lower().strip() == "y":
        break

print("Goodbye")
time.sleep(1)
exit()
