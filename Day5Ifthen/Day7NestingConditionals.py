tvShow = input("What is your favorite tv show? ")
if tvShow.lower().replace(" ", "") == "starwars":
    print("Mine too!")
    faveCharacter = input("Who is your favorite character? ")
    if faveCharacter.lower() == "darth vader":
        print("Right answer")
    else:
        print("Nah, Darth is the man!!!")
elif tvShow == "star trek":
    print("Aww, Janeway and kirk kill the red shirts")
else:
    print("Yeah, that's cool and all…")
