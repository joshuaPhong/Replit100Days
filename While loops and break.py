# while True:
#     print("This program is running")
#     goAgain = input("Go again?: ")
#     if goAgain == "no":
#         break
# print("Aww, I was having a good time 😭")

# day 16 challenge
print("Name the lyric")
print("-" * 14, "\n")
print("fill in the blank ____ to complete the lyric")
#  loop till complete or exit
counter = 0
while True:
    print("Never going to ____ you up!")
    blank_lyric = input("Fill in the blank >>> ")
    counter += 1
    if blank_lyric.lower().strip() == "give":
        print("Amazing!!!! It took you ", counter, "attempts")
        break
    else:
        try_or_exit = input("Try again? y/n")
        if try_or_exit.lower() == "n":
            break

print("You have been Rick Rolled 😂")
