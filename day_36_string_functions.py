# A list of peoples first and last names
# using print functions, fstrings

import os, time

list_of_names = []


def clean_input(names):
    return names.strip().capitalize()


while True:
    os.system("cls || clear")
    print("Day 36 Challenge\nList of Names\n")
    f_name = clean_input(input("What is your first name? >>> "))
    l_name = clean_input(input("What is yur last name? >>> "))
    whole_name = f"{f_name} {l_name}"
    if whole_name not in list_of_names:
        list_of_names.append(whole_name)
        for item in list_of_names:
            print(item)
            time.sleep(1)
        continue
    else:
        print("That name already exists")
        time.sleep(1)
        continue
