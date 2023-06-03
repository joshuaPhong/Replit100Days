# function to change the text color


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
    return ""

empty_space = ""
red = "red"
white = "white"
blue = "blue"
yellow = "yellow"
cyan = "cyan"
equals = "="
title = f"{change_color(red, equals)}{change_color(white, equals)}{change_color(blue, equals)}{change_color(yellow, 'Music App')}{change_color(blue, equals)}{change_color(white, equals)}{change_color(red, equals)}"
print(title)
rq = ["Radio", "Queen"]
# for i in rq:
print(f"🔥▶️  \033[0mRadio  Gaga")
print(f"\033[1;33m{rq[1]: >10}")
pnp = ["PREV", "NEXT", "PAUSE"]

print(f"\033[0m{pnp[0]:<10}")
print(f"\033[0;32m{pnp[1]: ^10}")
print(f"\033[0;36m{pnp[2]:>10}")




