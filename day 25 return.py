import keyboard


def myDice(sides):
    import random as ran
    dice = ran.randint(1, sides)
    return dice


def twoDice():
    import random as ran
    dice_six_side = ran.randint(1, 6)
    dice_eight_side = ran.randint(1, 8)
    six_eight = dice_six_side * dice_eight_side
    return six_eight


print("\033[32mCharacter Stats Generator\n")

while True:

    warrior = input("Name your warrior >>> ")
    health_points = twoDice()
    print(f"{warrior}'s health is {health_points}")
    print("press x to exit")
    leave_loop = input(keyboard.read_key())
    if leave_loop == "x":
        print("exiting")
        break
