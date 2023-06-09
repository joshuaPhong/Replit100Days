# dynamic lists
# define the list

# clean the input function
def cleanInput(word):
    return word.strip().lower()


# a pretty print function for our list
def prettyPrint(your_list):
    print()
    for rows in your_list:
        for items in rows:
            # items refers to each item in the column for that row
            print(f"{items:^10}", end=" | ")
            # :^10 means 10 characters as the space with the data in the center. The end character has been changed
            # to space vertical line space to make it look more like a table.

        print()

    print()


my_list = []
# loop until user exits the program
while True:
    # declare variables. assign with user input
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    platform = input("Enter your platform: ")
    # the list of user input we will fill our list with
    row = [name, age, platform]
    # add the  row list to the master list
    my_list.append(row)

    prettyPrint(my_list)
    remove_row = input("Do you want to remove a row? Y/n: ")
    # strip leading and trailing white space. lower case. only check the first letter
    if cleanInput(remove_row[0]) == "y":
        removal_name = input("Enter the name: ")
        for row in my_list:
            for item in row:
                if item == removal_name:
                    my_list.remove(row)
                    prettyPrint(my_list)
    prettyPrint(my_list)

    # exit?
    leave_loop = input("Do you want to exit? Y/n: ")
    if cleanInput(leave_loop) == "y":
        print(f"{my_list}\nGood Bye.")
        break

prettyPrint(my_list)
