# Your diary should:
#
# Set an access password.
# Prompt the user to type in a password.
# If they don't get the password right, exit the program.
# If they get it right, they enter the main menu, which gives 'Add' or 'View' diary entries.

# Choosing 'add' should:
# Prompt the user to type the entry and store it in the database with the timestamp as the key.

# Choosing 'view' should: Show the user the previous (most recent) entry. They can then choose to see the next
# previous entry working backwards until they get to the end. Or exit back to the menu.
# import the db
# import the db
# import the db
from replit import db
# imports
import os, time, datetime


def menu():
    while True:
        print("Menu")
        try:
            choice = input("1. Add\n2.View")
            if int(choice) == 1:
                add()
            elif int(choice) == 2:
                view()
            else:
                continue

        except Exception as err:
            print(f"error: {err}")
            continue


def add():
    os.system("clear")
    print("Diary")
    diary = input("Add your entry: ")
    now = datetime.datetime.now()
    key = now
    db[key] = diary

    print(f"{diary} added to the diary")
    time.sleep(1)
    os.system("clear")
    menu()


def view():
    keys = db.keys()
    for key in keys:
        print(f"Your previous entry was {db[key]}")
        choice = input("1. next entry\n2. menu\nEnter: ")
        if int(choice) == 1:
            continue
        else:
            menu()


# have the user set a password
password = input("Choose a password")
# insert the password into the db
db["password_db"] = password
# let the user know that thier password is saved
print(f'your password is {db["password_db"]}. Saved')
time.sleep(1)
os.system("clear")
while True:
    access = input("Enter your password: ")
    # define a variable as the data base keys
    keys = db.keys()
    # loop through the database
    for key in keys:
        # if the value of a key is the same as the password entered
        if db[key] == access:
            menu()
        else:
            # print("Wrong password try again. ")
            continue

