# affirmation and insult generator
#  function that takes a variable and returns that variable in lowercase and
#  without leading and trailing whitespace
def clean_input(a):
    return a.lower().strip()


#  collecting user input as variables for use the print statements
name = input("What is your name >>> ")
day_of_the_week = input("what is the daya of the week >>> ")
season_of_year = input("What is your favourite season in the year >>>")
fav_food = input("What is your favourite food >>> ")

if clean_input(day_of_the_week) == "monday":
    print("Hello", name.capitalize(), "it is great start to the week with",
          fav_food,
          "in our bellies")
elif clean_input(day_of_the_week) == "tuesday":
    print("Hello", name.capitalize())
elif clean_input(day_of_the_week) == "wednesday":
    print(f"Hello {name} it is hump day!!!")
elif clean_input(day_of_the_week) == "thursday":
    print(f"Hello {name}")
elif clean_input(day_of_the_week) == "friday":
    print("Hello" + name + "TGIF")
elif clean_input(day_of_the_week) == "saturday":
    print("Hello", name)
elif clean_input(day_of_the_week) == "sunday":
    print(f"Back to work tomorrow {name}")
else:
    print("I know life is hard! But choose a day of the week. Are you a "
          "goldfish")
