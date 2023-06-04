# dynamic lists
import os, time

to_do = []


def loop_list():
    for j in to_do:
        return j


while True:
    print(f"Your to do list: {loop_list()}")
    menu = input("Do you want to add, view, or edit your list >>> ")

    if menu == "add":
        item = str(input("What do you want to add >>> "))
        to_do.append(item)


        print(f"Your updated list {loop_list()}")
        time.sleep(1)
        os.system("cls || clear")
        continue
    elif menu == "view":
        for i in to_do:
            print(i)
    elif menu == "edit":
        for i in to_do:
            print(i)
        remove = input("What would you like to remove?")
        to_do.remove(remove)
    else:
        print("Please enter a valid command")
        continue
os.system("clear")
time.sleep(1)