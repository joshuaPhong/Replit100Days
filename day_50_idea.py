import random
import time


def tidy():
    import os, time
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(1)


def leave_program():
    tidy()
    print("Do you want to exit. Y/n")
    leave = input("Enter: ")
    if leave.strip().lower() == "y":
        print("Goodbye")
        time.sleep(1)
        exit()
    else:
        main_menu()


def menu_message():
    print("💡 Wellcome to your ideas 💡\n\nWould you like to:")
# Your idea storage system should:


# Prompt the user to add an idea, or load a random one.
def main_menu():
    while True:
        tidy()
        menu_message()
        print(f"\t1. Add Idea\n\t2. Random Idea\n\t3. Exit Program")
        main_menu_prompt = input("Enter: ")
        if main_menu_prompt == "1":
            add_idea()
        elif main_menu_prompt == "2":
            random_idea()
        elif main_menu_prompt == "3":
            leave_program()
            break  # Exit the loop
        else:
            print("Invalid input. Please try again.")


# Choosing 'Add an idea' results in:
# A prompt for the user to input their idea.
# Add the idea to a text file called 'my.ideas'.
# Add the idea in append mode, with every new idea on a brand new line.
# todo: DONE
def add_idea():
    tidy()
    print("Add an Idea")
    idea = input("Enter: ")
    with open("my.ideas", "a+") as file:
        file.write(f"{idea}\n")
    main_menu()


# Choosing 'Load random' results in:
# Load the list of ideas.
# Choose one at random.
# todo: DONE


def random_idea():
    tidy()
    with open("my.ideas", "r") as file:
        ideas = file.read().split()
        random_idea = random.choice(ideas)
        print(f"A random idea: {random_idea}")
    main_menu()


# Display it on screen for a few seconds.
# Return to the menu.

# call the functions
main_menu()
