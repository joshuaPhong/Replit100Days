# Your Mokédex should:
#
# Store multiple Mokébeasts using a loop.
# Get user input of the beasts' details.
# Add the details to a 2D dictionary.
# Repeat until the user wants to stop.
# Output the full Mokédex using a prettyPrint() function.
import time

mokedex = {}


def stop():
    while True:
        stop_adding = input("Do you want to leave? Y/n: ")
        if stop_adding.lower().strip() == "y":
            exit()
        else:
            add_mokebeast()


def prettyPrint(dictionary):
    print()
    for key, value in dictionary.items():
        # moves along every 'key:subDictionary' pair and outputs the key (the name of the character).
        print(key, end=": ")
        for subKey, subValue in value.items():
            # (nested) `for` loop moves along every sub-key and sub-value in each subDictionary.
            print(subKey, subValue, end=" | ")
        print()


def add_mokebeast():
    while True:
        name = input("Name: ")
        element = input("Element: ")
        special_move = input("Special Move: : ")
        starting_hp = input("Starting HP: ")
        starting_mp = input("Starting MP: ")
        mokedex[name] = {"element": element, "special_move": special_move, "starting_hp": starting_hp,
                         "starting_mp": starting_mp}  # line 7

        prettyPrint(mokedex)
        time.sleep(1)
        stop()


add_mokebeast()
