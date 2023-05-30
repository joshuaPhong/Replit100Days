import os
import time
import random
# a list of potential character types
characters_type_list = ["Human", "Elf", "Wizard", "Warrior", "Valkyrie", "Orc"]
# we need a list of dictionaries to kepp player characters
players = []


def character():
    while True:
        os.system("cls")
        print("🧙‍♂️🪄 Character Builder 🧝‍♀️💪")
        print("")
        time.sleep(1)
        character_name = input("What is your characters name >>> ")
        time.sleep(1)
        print("What type of character would you like")
        # variable ind is used to change the index in the list
        ind = 0
        # loop through the character list
        for i in range(len(characters_type_list)):
            # print the list index for character selection
            # print the list item for the user
            print(i, ".", characters_type_list[ind])
            ind += 1
        character_type = int(input(">>>"))

        time.sleep(1)
        print(character_name, "is a", characters_type_list[character_type])
        print("HEALTH:", health())
        print("STRENGTH:", strength())
        print()
        new_item = {"name": character_name,
                    "type": characters_type_list[character_type],
                    "health": health(), "strength": strength()}
        players.append(new_item)
        print(players)
        time.sleep(5)
        os.system("cls || clear")

        again = input("Build another character?:\n").lower()
        if again == "no":
            break
        time.sleep(1)
        os.system("cls || clear")


def health():
    health_stat = int(((rollDice(6) * rollDice(12)) / 2) + 10)
    return health_stat


def strength():
    strength_stat = int(((rollDice(6) * rollDice(12)) / 2) + 12)
    return strength_stat


def rollDice(side):
    result = random.randint(1, side)
    return result


character()
