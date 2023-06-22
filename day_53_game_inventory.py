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
import time, os


def tidy_screen():
    print()
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(1)


def add_item():
    pass


def view_items():
    pass


def remove_item():
    pass


def menu_message():
    print("Your Inventory ⚔️🗡️🔪🪄🍊🔪\nUse it well and conquer the foe.")


def menu():
    tidy_screen()
    menu_message()
    while True:
        menu_choice = input("1. Add item\n2. View items\n3. Remove items\nEnter >>> ")
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
        except Exception as err:
            print(f"Error {err}\nTry again")
            time.sleep(1)
            tidy_screen()
            continue


menu()
