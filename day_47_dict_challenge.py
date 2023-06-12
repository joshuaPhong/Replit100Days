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
# Making the dictionary dynamic so you can add your own cards.
# Using a loop to play the game in a 2 player format, keeping track of points scored.


# CATEGORY: STAR WARS CHARACTERS
def tidy():
    import os, time
    os.system("cls || clear")
    time.sleep(1)


star_wars_chars = {}


def add_char():
    tidy()
    print("🎴 Add Character Card 💫")
    print()
    while True:
        name = input("What is your characters name: ")
        type = input("What is your characters type: ")
        skill = input("What is your characters skill: ")
        skill_level = input("What is your characters skill level; 0-100: ")
        star_wars_chars[name] = {"type": type, "skill": skill, "skill_level": skill_level}
        print(star_wars_chars)



def pick_a_card():
    #      One Player: user picks a card computer picks a rnd card


add_char()
