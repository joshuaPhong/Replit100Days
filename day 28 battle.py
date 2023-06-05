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
            # print the list names for the user
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

        print("Player", i + 1)

        # access the list character_type with the index []
        print(character_name, "is a", characters_type_list[character_type])
        # access the appended data and print it to the screen
        # players list at index[index] with dict key ["key"]

        if i == 0:
            print("HEALTH:", players[i]["health"])
            print("STRENGTH:", players[i]["strength"])
        else:
            print("HEALTH:", players[i]["health"])
            print("STRENGTH:", players[i]["strength"])

        print()

        time.sleep(1)
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
    os.system("cls || clear")
    print("Battle")
    time.sleep(2)
    time.sleep(1)
    p1_name = players[0]["name"]
    p1_type = players[0]["type"]
    p1_health = players[0]["health"]
    p1_strength = players[0]["strength"]
    p2_name = players[1]["name"]
    p2_type = players[1]["type"]
    p2_health = players[1]["health"]
    p2_strength = players[1]["health"]

    print("Player One")
    print(p1_name, "is a", p1_type)
    print("HEALTH:", p1_health)
    print("STRENGTH:", p1_strength)
    print("\nVS\n")
    print("Player Two")
    print(p2_name, "is a", p2_type)
    print("HEALTH:", p2_health)
    print("STRENGTH:", p2_strength)

    while True:
        os.system("cls || clear")
        time.sleep(1)
        p1r = roll_dice(6)
        p2r = roll_dice(6)

        if p1_health <= 0:
            print(p1_name, "Lost")
            time.sleep(1)
            break
        elif p2_health <= 0:
            print(p2_name, "Lost")
            time.sleep(1)
            break

        print("\nLets Roll\n")

        print("Player One rolls: ", p1r)
        print("Player Two rolls: ", p2r)
        time.sleep(1)
        if p1r == p2r:
            print("Its a draw")
            time.sleep(1)
            continue
        elif p1r > p2r:
            print("Player One Wins")
            p1damage = abs(p1_strength - p2_strength) + 1
            p2_health -= p1damage
            print(p1_name)
            print("HEALTH:", p1_health)
            print("STRENGTH:", p1_strength, "\n")
            print(p2_name)
            print("HEALTH:", p2_health)
            print("STRENGTH:", p2_strength)
            time.sleep(1)
            continue
        else:
            print("Player Two Wins")
            p2damage = abs(p1_strength - p2_strength) + 1
            p1_health -= p2damage
            print(p1_name)
            print("HEALTH:", p1_health)
            print("STRENGTH:", p1_strength, "\n")
            print(p2_name)
            print("HEALTH:", p2_health)
            print("STRENGTH:", p2_strength)
            time.sleep(1)
            continue

    time.sleep(1)


def play_again():
    play_again = input("do you want to play again? >>>")
    if play_again.lower() == "yes":
        time.sleep(1)
        character()
        battle()
    else:
        exit()


# TODO: GAME PLAY.
#     CHARACTER
#     BATTLE
#     EXIT


character()
battle()
play_again()