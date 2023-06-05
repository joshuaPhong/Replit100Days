import os
import time

list_of_email = []


def prettyPrint():
    os.system("cls || clear")
    print("list of Emails:\n")
    for index in range(len(list_of_email)):
        print(f"{index}: {list_of_email[index]}")  # make this an f-string
    time.sleep(2)
    os.system("cls || clear")


while True:
    print("Spammer Inc")
    menu = input("Do you want to\n1. Add.\n2. Delete\n3. View\n4. Spam\n5. Edit\n6. Erase list\n>>> ")
    if menu == "3":
        prettyPrint()

    elif menu == "1":
        email = input("Enter the email >>> ")
        if email not in list_of_email:
            list_of_email.append(email)
        else:
            print("Email already exists\nTry another")
            time.sleep(2)
            continue
    elif menu == "2":
        email = input("Enter the email you want to delete >>> ")
        # confirm with the user they want to delete
        check_remove = input(f"Are you sure you want to delete {email}?\nEnter yes >>> ")
        if check_remove.lower() == "yes":
            # check the email exists
            if email in list_of_email:
                # remove the email
                list_of_email.remove(email)
            else:
                # the email is not in the list message the user and return them to the main menu
                print("email does not exist")
                continue
        else:
            continue
    elif menu == "4":
        if len(list_of_email) < 10:
            range_var = len(list_of_email)
        else:
            range_var = 9
            # lets spam
        for i in range(0, range_var):
            os.system("cls || clear")
            message = "This is an email for"
            print(f"{message} {list_of_email[i]}.\nIt has come to our attention that you are an 🥚🥚./nSend your "
                  f"money or else all of replit will know 🪄🤡")
            time.sleep(2)
            os.system("cls || clear")
    elif menu == "5":
        print("Edit an email\n")
        email = input("What email would you like to edit?\n>>>  ")
        if email in list_of_email:
            # check the user has the correct email
            check_remove = input(f"Are you sure you want to edit {email}?\nEnter yes >>> ")
            if check_remove.lower() == "yes":
                new_mail = input(f"Please enter the new email\n>>> ")
                for i in range(0, len(list_of_email)):
                    if list_of_email[i] == check_remove:
                        list_of_email[i] = new_mail
            else:
                continue
        else:
            print(f"{email} is not a valid email")
            time.sleep(1)
            continue
    elif menu == "6":
        erase = input("Are you sure you want to erase the list?\nEnter yes >>> ")
        if erase == "yes":
            list_of_email = []
            continue
        else:
            continue
    else:
        print("Enter a valid command")
