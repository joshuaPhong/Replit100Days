# import os, time
#
# # the default for a print statement is a new line
# # each iteration will start on a new line
# for i in range(1, 11):
#     print(i)
#
# # we can change the end of line with the end="" argument
# # this. end=" " will add a space at the end of each iteration
# for i in range(1, 11):
#     print(i, end=" ")
#
# # new line is the same as default. the computer prints enter
# for i in range(1, 11):
#     print(i, end="\n")
#
# # \v is a vertical tab
# for i in range(1, 11):
#     print(i, end="\v")
#
# # sep="" the seperator
# print("If you put")
# print("\033[33m", end="")  # yellow
# print("nothing as the")
# print("\033[35m", end="")  # purple
# print("end character")
# print("\033[32m", end="")  # green
# print("then you don't")
# print("\033[0m", end="")  # default
# print("get odd gaps")
# print("concatenated with the end=\"\"")
# print("If you put", "\033[33m", "nothing as the", "\033[35m", "end character", "\033[32m", "then you", "\033[0m",
#       "get odd gaps", end="")
# print("\n")
# print("concatenated with the sep=\"\"")
# print("If you put ", "\033[33m", "nothing as the ", "\033[35m", "sep character ", "\033[32m", "then you don't ",
#       "\033[0m", "get odd gaps ", sep="")
#
# # turning the cursor on and off
#
# print("Turning the cursor off using escape sequence \'\\033\' with \'[?25l\' and on again with \'[?25h\'")
#
# print('\033[?25moff', end="")
# for i in range(1, 11):
#     print(i)
#     time.sleep(0.2)
#     os.system("cls ||clear")
# print("\033[?25hon")
# time.sleep(2)


def change_color(color, word):
    if color == "yellow":
        print("\033[1;33m", word, end="", sep="")
    elif color == "red":
        print("\033[0;31m", word, end="", sep="")
    elif color == "green":
        print("\033[0;32m", word, end="", sep="")
    elif color == "brown":
        print("\033[0;33m", word, end="", sep="")
    elif color == "blue":
        print("\033[0;34m", word, end="", sep="")
    elif color == "purple":
        print("\033[0;35m", word, end="", sep="")
    elif color == "cyan":
        print("\033[0;36m", word, end="", sep="")
    elif color == "black":
        print("\033[0;30m", word, end="", sep="")
    elif color == "bold":
        print("\033[1m", word, end="", sep="")
    else:
        print("\033[0m", word, sep="", end="")


# change_colour("yellow", "fred")


def change_the_color():
    print("Lets change the colors", end="\n")
    input_color = input("Choose a color >>> ")
    input_text = input("Choose some text to color >>> ")
    return change_color(input_color, input_text)


change_the_color()
