# tvShow = input("What is your favorite tv show? ")
# if tvShow.lower().replace(" ", "") == "starwars":
#     print("Mine too!")
#     faveCharacter = input("Who is your favorite character? ")
#     if faveCharacter.lower() == "darth vader":
#         print("Right answer")
#     else:
#         print("Nah, Darth is the man!!!")
# elif tvShow == "star trek":
#     print("Aww, Janeway and kirk kill the red shirts")
# else:
#     print("Yeah, that's cool and all…")
#
# order = input("What would you like to order: pizza or hamburger? ")
# if order == "hamburger":
#   print("Thank you.")
#   cheese = input("Do you want cheese?")
#   if cheese == "yes":
#     print("You got it.")
#   else:
#     print("No cheese it is.")
# elif order == "pizza":
#   print("Pizza coming up.")
#   toppings = input("Do you want pepperoni on that?")
#   if toppings == "yes":
#     print("We will add pepperoni.")
#   else:
#     print("Your pizza will not have pepperoni.")

# day 7 challenge
# game of thrones character questions

def not_fan():
    print("Not a true fan")


def fan():
    print("True fan")


def test():
    print("lets test that")


print("GAMES OF THRONES CHARACTERS. TRUE FAN?")
print("++++++++++++++++++++++++++++++++++++++")
fav_char = input("Who is your favorite character? > ")
if fav_char.lower() == "john snow":
    test()
    sword = input("What is the name of John Snows sword? > ")
    if sword.lower() == "long claw":
        fan()
        who_gave_sword = input("Who gave John Snow this sword? > ")
        if who_gave_sword.lower() == "jeor mormont" or who_gave_sword.lower() \
                == "lord commander mormont":
            fan()
        else:
            not_fan()
    else:
        not_fan()
elif fav_char.lower() == "drogo":
    test()
    crown = input("Who did Drogro crown king")
    #  whe using logical operators, and, or each comparison must be a
    #  complete statement
    if crown.lower() == "viserys" or crown.lower() == "viserys targaryen":
        fan()
    else:
        not_fan()
#  we can also use the in operator to check multiple string conditions
#  the strings are in a tuple / array of strings.
#  is our string 'in' the tuple of strings
elif fav_char.lower() in ("ned stark", "eddard stark", "lord stark"):
    fan()

else:
    print("your character choice leaves somthing to be desired.")


