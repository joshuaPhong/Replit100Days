# rainbow-ize a string
def change_color(color):
    if color == "yellow":
        return "\033[1;33m"
    elif color == "red":
        return "\033[0;31m"
    elif color == "green":
        return "\033[0;32m"
    elif color == "brown":
        return "\033[0;33m"
    elif color == "blue":
        return "\033[0;34m"
    elif color == "purple":
        return "\033[0;35m"
    elif color == "cyan":
        return "\033[0;36m"
    elif color == "black":
        return "\033[0;30m"
    elif color == "bold":
        return "\033[1m"
    else:
        return "\033[0m"


print("Lets color a string like a rainbow".title())
input_string = input("Enter a string >>> ")
for letter in input_string:
    if letter.lower() == "b":
        print(change_color("blue"), end="")
    elif letter.lower() == "g":
        print(change_color("green"), end="")
    elif letter.lower() == "p":
        print(change_color("purple"), end="")
    elif letter.lower() == "y":
        print(change_color("yellow"), end="")
    elif letter.lower() == "c":
        print(change_color("cyan"), end="")
    elif letter.lower() == "r":
        print(change_color("red"), end="")
    elif letter == " ":
        print(change_color("white"), end="")
    print(letter, end="")



