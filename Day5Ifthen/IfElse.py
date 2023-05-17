# using if conditions
print("\033[32mMarvel character finder")
spider_man = input("Do you like hanging around? y/n\n")
if spider_man.lower() == "y":
    print("You are spiderman.\n")
else:
    print("You are not Spider Man")
korg = input("Do you have a gravelly voice? y/n\n")
if korg.lower() == "y":
    print("You are korg!")
else:
    print("You are not Korg!\n")
captain_marvel = input("Do you feel marvelous? y/n\n")
if captain_marvel.lower() == "y":
    print("You are captain Marvel!")
else:
    print("You are not captain marvel")
print("I dont know who you are!\n")
who_are_you = input("Tell me who you are?\n")
print("Hello", who_are_you)