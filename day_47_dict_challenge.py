# Alright Top Trumpers. Your program should work like this.
#
# Pick a category. Something popular. You know like 'most handsome computer science teachers'. 😆
# Store the information of two different objects in a 2D dictionary.
# The key field should be name.
# The data in the sub dictionary should be some stats about the object. For example:
# Intelligence
# Handsomeness
# L33t c0ding skillz
# Baldness level
# Use an infinite loop to get the user to pick one of the two cards, then pick a stat from that card.
# Display the chosen stat for both cards and output which has won.
# 🥳 Extra points for:
#
# Making the dictionary dynamic, so you can add your own cards.
# Using a loop to play the game in a 2 player format, keeping track of points scored.
import os
import random
import time


# CATEGORY: STAR WARS CHARACTERS
def tidy():
    os.system("cls || clear")
    time.sleep(1)


# DICTIONARY OF CHARACTERS AND THEIR STATS
star_wars_chars = {
    "luke": {
        "type_of_force_user": "jedi",
        "lightsaber": 7,
        "force": 8,
        "level": 7
    },
    "obi-wan": {
        "type_of_force_user": "jedi",
        "lightsaber": 8,
        "force": 9,
        "level": 9
    }
}

while True:
    tidy()
    # PICK A CARD
    print("Choose your card")
    for key in star_wars_chars.keys():
        print(key, end=":\n")
    # for key, value in star_wars_chars.items():
    #     print(key, end=":\n")
    #     # for subkey, subvalue in value.items():
    #     #     print(subkey, subvalue, end=", ")
    user = input("\nEnter: ")
    # COMP PICK A CARD
    while True:
        r_choice = random.choice(list(star_wars_chars.keys()))
        if r_choice != user:
            comp = r_choice
            break
        else:
            continue
    print(f"You selected {user} the computer is {comp}")
    # PICK A STAT
    print("Choose your weapon\nLight saber or force")

    weapon = input("Enter: ").strip().lower()
    print(f"{user} {star_wars_chars[user][weapon]}\n{comp} {star_wars_chars[comp][weapon]}")

    if star_wars_chars[user][weapon] > star_wars_chars[comp][weapon]:
        print(f"{user} Wins")
    else:
        print(f"{comp} Wins")
    time.sleep(1)