import os, time, random

# list of words to guess
list_of_words = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton", "random", "name", "eurovision",
                 "dawn-shard"]
# choose a random word from the list
random_word = random.choice(list_of_words)

# list of hangman pics for display
pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]
# start a counter for the pics
pics_counter = 0

print("\033[0;31m")
print("hangman".upper())
print("\033[0m")

letter_list = []

while True:
    os.system("cls || clear")
    print()

    print(pics[pics_counter])
    failed = 0
    letter_picked = input("Choose a letter >>> ").lower()

    if letter_picked in letter_list:
        print("you have picked that letter already")

        continue
    else:
        letter_list.append(letter_picked)

    for i in random_word:
        if i in letter_list:
            print(i, end="", )
        else:
            print("_", end="")
            failed += 1

    if letter_picked not in random_word:
        pics_counter += 1
        if pics_counter < 6:
            continue
        else:
            print("You lost")
            break

    if failed == 0:
        print("You won")
        break


#  credit too chris horton/hangmanwordbank.py
#  https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
# for the art
# as well as invisible fox and rysics for the one line list of the art
