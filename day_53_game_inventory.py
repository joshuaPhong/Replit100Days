# Your video game inventory system should:
#
# Have a menu that allows the user to:
# Add
# View
# Remove
# Adding an item saves it to a file using capitalize mode. Duplicates are allowed.
# Removing an item deletes it from the file.
# View is trickier. It should output the name of the item and tell you how many of those items you have.
# Use auto-save and auto-load with try... except.

# IMPORTS
import os
import time
import traceback

# VARIABLES
inventory = []
debug_mode = True


def auto_save(file):
    try:
        with open(file, "w") as f:
            f.write(str(inventory))
    except Exception as err:
        print(f"Save error: {err}")
        if debug_mode:
            print(traceback.format_exc())


# clears the screen and pauses the program
def tidy_screen():
    print()
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(1)


def add_item():
    print("Add Items to Your Inventory")
    item = input("Enter an item: ")
    inventory.append(item)
    auto_save("inventory.txt")
    print(inventory)


def view_items():
    pass


def remove_item():
    pass


# a main menu message
def menu_message():
    print("Your Inventory ⚔️🗡️🔪🪄🍊🔪\nUse it well and conquer the foe.")


# the main menu
def menu():
    # clear the screen
    tidy_screen()
    # output the menu message
    menu_message()
    # start a loop for menu options
    while True:
        # menu options
        menu_choice = input("1. Add item\n2. View items\n3. Remove items\nEnter >>> ")
        # try the cast input and call the appropriate function
        try:
            if int(menu_choice) == 1:
                add_item()
            elif int(menu_choice) == 2:
                view_items()
            elif int(menu_choice) == 3:
                remove_item()
            else:
                print("Input error, try again with a number 1-3")
                continue
        #         if the input fails, display a message clear the screen and send the user back to the menu options
        except Exception as err:
            print(f"Error {err}\nTry again")
            time.sleep(1)
            tidy_screen()
            continue


# call the menu to start the program
menu()
