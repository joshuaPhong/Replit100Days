import os
import time
import random

# a list of potential character types
characters_type_list = ["Human", "Elf", "Wizard", "Warrior", "Valkyrie", "Orc"]
# we need a list of dictionaries to keep player characters
players = []


# todo: generate TWO characters.
# change the while to a for loop or use an if
def character():
    for i in range(2):
        os.system("cls")
        print("🧙‍♂️🪄 Character Builder 🧝‍♀️💪")
        print("")
        time.sleep(1)

        if len(players) == 0:
            print("Player One")
        else:
            print("Player", len(players) + 1)

        character_name = input("What is your characters name >>> ")
        time.sleep(1)
        print("What type of character would you like")
        # variable ind is used to change the index in the list
        ind = 0
        # loop through the character list
        for j in range(len(characters_type_list)):
            # print the list index for character selection
            # print the list item for the user
            print(j, ".", characters_type_list[ind])
            ind += 1
        character_type = int(input(">>>"))

        time.sleep(1)

        # create a dictionary of the new players data
        new_character = {"name": character_name,
                         "type": characters_type_list[character_type],
                         "health": health(),
                         "strength": strength()}

        # add new player the list
        players.append(new_character)

        print("Player", [i + 1])
        # access the list character_type with the index []
        print(character_name, "is a", characters_type_list[character_type])
        # access the appended data and print it to the screen
        # players list at index[index] with dict key ["key"]
        print("HEALTH:", players[i]["health"])
        print("STRENGTH:", players[i]["strength"])
        print()

        time.sleep(5)
        # clear the console
        os.system("cls || clear")

        # not needed the range will do it

        # again = input("Build another character?:\n").lower()
        # if again == "no":
        #     time.sleep(1)
        #     os.system("cls || clear")
        #     continue

    else:
        return


def health():
    health_stat = int(((roll_dice(6) * roll_dice(12)) / 2) + 10)
    return health_stat


def strength():
    strength_stat = int(((roll_dice(6) * roll_dice(12)) / 2) + 12)
    return strength_stat


def roll_dice(side):
    result = random.randint(1, side)
    return result


# TODO: simulate battle
# players take turns rolling a six sided die
# winner is the higher roll
# winner deals damage to health points
# play until health points <=0
# use sleep and time to keep a tidy console
# player one = index 0 player two = index 1 in player list
def battle():
    print("Battle")


#
# TODO: GAME PLAY.
#     CHARACTER
#     BATTLE
#     EXIT

character()
battle()

