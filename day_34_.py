import os, time

list_of_email = []


def prettyPrint():
    os.system("cls || clear")
    print("list of Emails:\n")

    # counter = 1  # add a counter
    for index in range(len(list_of_email)):
        print(f"{index}: {list_of_email[index]}")  # make this an f-string
        # counter += 1  # adds a number with each new i
    time.sleep(1)


while True:
    print("Smammer Inc")
    menu = input("Do you want to add, delete, or view email? >>> ")
    print()
    if menu == "view":
        prettyPrint()

    elif menu == "add":
        email = input("Enter the email >>> ")
        list_of_email.append(email)

    elif menu == "delete":
        email = input("Enter the email you want to delete >>> ")
        if email in list_of_email:
            list_of_email.remove(email)
        else:
            print("email does not exist")
            continue

    else:
        print("Enter a valid command")
    time.sleep(1)
    os.system("cls || clear")
