import os
import time


def prettyPrint():

    os.system("cls || clear")
    print("list of Emails:\n")

    for index in range(len(list_of_email)):
        print(f"{index}: {list_of_email[index]}")  # make this an f-string

    time.sleep(1)
