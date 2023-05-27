# the continue command stops executing code and goes back to the
# start of the loop
# the exit() function stops the program
while True:
    print("You are in a corridor, do you go left or right?")
    direction = input("> ")
    if direction == "left":
        print("You have fallen to your death")
        break
    elif direction == "right":
        continue
    else:
        print("Ahh! You're a genius, you've won")
        # exit() if we run the exit() function the program is stopped
        # the print statement below will not be executed
print("That makes you a looser")
