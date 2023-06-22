# day 45
# challenge
import time
import os

from cleanInput import cleanInput as cI
from ppForListOfList import prettyPrint as pP


to_do_list = []


def load():
    # refer to the global variable
    global to_do_list
    # Open the file
    with open('todo.txt', 'r') as file:
        content = file.read().strip()

    # Check if the file is empty
    if content:
        # The File is not empty, evaluate the contents
        to_do_list = eval(content)
    else:
        # File is empty, create an empty list
        to_do_list = []


def save():
    f = open("todo.txt", "w")
    f.write(str(to_do_list))
    f.close()


def tidy():
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(1)


def main_menu_message():
    tidy()
    print(f"😀 Welcome 😀")
    print()
    print(f"Press 1 for: Add")
    print(f"Press 2 for: View")
    print(f"Press 3 for: Remove")
    print(f"Press 4 for: Edit")


def main():
    while True:
        main_menu_message()
        choice = int(input("Enter >>> "))
        if choice == 1:
            add()
        elif choice == 2:
            view()
        elif choice == 3:
            remove()
        elif choice == 4:
            edit()
        else:
            print("Invalid entry")
            continue


def main_or_exit():
    while True:
        tidy()
        print(f"1: Return to main menu\n2: Exit")
        choice = int(input("Enter: "))
        if choice == 1:
            main()
        elif choice == 2:
            print("Good Bye")
            exit()
        else:
            print("Invalid entry")
            continue


def add():
    print("add")
    while True:
        tidy()
        to_do = cI(input("To do: "))
        date = cI(input("Date: "))
        priority = cI(input("Priority; High, Medium, or Low: "))
        row = [to_do, date, priority]
        to_do_list.append(row)
        pP(to_do_list)
        time.sleep(2)
        save()
        tidy()
        add_another = cI(input("Do you want to add another record: Y/n"))
        if add_another == "y":
            continue
        else:
            main_or_exit()


def view():
    view_menu()


def view_menu():
    tidy()
    while True:
        print(f"1: View all\n2: View priority\n3: Main Menu")
        choice = int(input("Enter: "))
        if choice == 1:

            view_all()
        elif choice == 2:

            view_priority()
        elif choice == 3:
            main()
        else:
            continue


def view_all():
    tidy()
    print("Your To-Do list: ")
    print()
    for row in to_do_list:
        # print(row)
        for item in row:
            print(item, end=", ")
            time.sleep(2)
    main_or_exit()


def view_priority():
    tidy()
    print("Your To_Do list by Priority:")
    print()
    choice = input("Enter priority; High, Medium, Low: ")
    while True:
        # todo: cou;d we use the pretty print here? a variable for the end=""?
        for row in to_do_list:
            if choice in row:
                for item in row:
                    print(item, end=", ")
                    time.sleep(2)
        main_or_exit()


def remove():
    tidy()
    print(f"What would you like to remove.")
    pP(to_do_list)
    remove_from_list = input("Enter: ")
    for row in to_do_list:
        for item in row:
            if item == remove_from_list:
                to_do_list.remove(row)
    save()
    pP(to_do_list)
    time.sleep(2)
    main_or_exit()


#  we could have removed the entire row and then had the user add a new record
#  this would eliminate the problem of duplicates in list
def edit():
    tidy()
    pP(to_do_list)
    print()
    edit_list_item = input("What item would you like to edit? Enter: ")
    new_list_item = input("What would you like to replace it with? Enter: ")
    for row in to_do_list:
        for index, item in enumerate(row):
            if edit_list_item == item:
                row[index] = new_list_item
    save()
    tidy()
    print(f"Your updated todo list")
    pP(to_do_list)
    time.sleep(2)
    main_or_exit()


load()
main()
