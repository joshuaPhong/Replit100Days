from replit import db
import datetime


# Your program should.

# Display a menu - Add or View tweets.

def menu():
    while True:
        print("Tweet Menu")
        menu_choice = input("1. Add an item: \n2. View an item: \nEnter: ")
        try:
            if int(menu_choice) == 1:
                add()
            elif int(menu_choice) == 2:
                view()
            else:
                print("Try again")
                continue
        except:
            print("input error")

        # 'Add' should:


def add():
    print("Add Tweet")
    tweet = input("Add your tweet: ")
    now = datetime.datetime.now()
    key = now
    db[key] = tweet

    print(db[key])
    # db["key"]
    menu()


# Get the tweet input.
# Store it to the database with the current timestamp as the key value.
# 'View' should:
def view():
    print("View Tweet")
    # reverse the timestamp keys
    rev_keys = db.keys
    # loop through the db
    keys = db.keys()
    for key in keys:
        print(f"""{key}: {db[key]}""")


# Show the tweets in reverse chronological order.

# recursion call the range minus 10????

# Show 10 tweets at a time.
# Prompt the user to show another 10 tweets (yes or no).
# A 'no' choice goes back to the menu.


menu()
