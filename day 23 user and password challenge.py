# a login function.
# loops through user input until the correct credentials are entered
def login():
    while True:
        user = input("What is your username >>>")
        word = input("What is your password >>>")
        if user == "user" and word == "word":
            print("Your in....")
            break
        else:
            print("Incorrect")
            continue


print("LOGIN")
print("-" * 6)
print("Username = user: Password = word")
# call the login function
login()
