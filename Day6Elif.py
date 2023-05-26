# # password example
# print("SECURE LOGIN")
# username = input("Username > ")
# password = input("Password > ")
# if username == "mark" and password == "password":
#     print("Welcome Mark!")
# elif username == "suzanne" and password == "password":
#     print("Hey there Suzanne!")
# else:
#     print("Go away!")
#
# # check errors example
# season = input("what is your favorite season?")
# if season == "spring":
#     print("Ah! The birds are chirping and flowers blooming.")
# elif season == "summer":
#     print("Catch some sun and cool off with a lemonade.")
# elif season == "autumn":
#     print("The leaves are changing and the air is crisp. Enjoy!")
# elif season == "winter":
#     print("Stay warm by the fire and watch the snow fall.")
# else:
#     print("I don't know that season. Please try again.")

# password challenge
print("PASSWORD CHALLENGE")
print("++++++++++++++++++")
name_challenge = input("enter your name > ")
password_challenge = input("enter your password > ")
if name_challenge.lower() == "mark" and password_challenge.lower() == \
        "password":
    print("Hello", name_challenge.capitalize(), "Your a dick!")
elif name_challenge.lower() == "joshua" and password_challenge.lower() == \
        "password":
    print("Hello", name_challenge.capitalize(), "Wow! You did it!!!")
elif name_challenge.lower() == "guy" and password_challenge.lower() == \
        "password":
    print("Hello", name_challenge.upper(), "Your twaty", name_challenge.capitalize()
          )
else:
    print("You are not a member or got your credentials wrong")

