import os
import time


def prettyPrint():
    os.system("cls || clear")
    print("list of Emails:\n")

    counter = 1  # add a counter
    for i in list_of_email:
        print(f"{counter}: {i}")  # make this an f-string
        counter += 1  # adds a number with each new i
    time.sleep(1)