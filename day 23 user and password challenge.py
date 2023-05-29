def login():
    while True:
        user = input("What is your username >>>")
        word = input("What is your password >>>")
        if user == "user" and word == "word":
            print("You in....")
            break
        else:
            print("Incorrect")
            continue


login()
