print("""\033[95mWelcome to your adventure simulator. I am going to ask you a 
bunch 
of questions and then create an epic story with you as the star!""")
name = input("What is your name: ")
enemy = input("Who is your worst enemy: ")
power = input("What is your super power: ")
live = input("Where do you live: ")
food = input("What is your favorite food: ")
print(f"""Hello \033[31m{name}! Your ability to \033[32m{power} will make sure 
you never have 
to look at \033[33m{enemy} again. Go eat \033[34m{food} as you walk down the 
streets of 
\033[35m{live} and use \033[36m{power} for good and not evil!
""")
