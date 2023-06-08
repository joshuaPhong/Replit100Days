import change_color as cc

moke_beast = {"name": None, "type": None, "move": None, "hp": None, "mp": None}
for beast in moke_beast.keys():
    moke_beast[beast] = input(f"Enter {beast}: ").lower().strip()

for key, value in moke_beast.items():

    if moke_beast["type"] == "fire":
        print(cc.change_color("red"))
    elif moke_beast["type"] == "water":
        print(cc.change_color("blue"))
    elif moke_beast["type"] == "spirit":
        print(cc.change_color("cyan"))
    elif moke_beast["type"] == "earth":
        print(cc.change_color("brown"))
    else:
        print(cc.change_color("white"))
    print(f"{key}: {value}", end="")
