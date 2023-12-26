# import hashlib
import os
# from replit import db
import random
import time
import sqlite3

# connect to the db
conn = sqlite3.connect("day_71.db")
# create a cursor
c = conn.cursor()
# create a table called users that stores username and passwords
c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
# CHECK THE TABLES IN THE DB
print(f"the db: {c.execute('SELECT * FROM users').fetchall()}")
# add an entry to the db
c.execute("INSERT INTO users VALUES ('test', 'test')")
# check the entry
print(f"the db: {c.execute('SELECT * FROM users').fetchall()}")

SALT = random.randint(1, 10000)


# a function for the menu
def start_menu():
    print("Welcome to the login menu")
    choice = input("1. Login\n2. Signup\n3. Exit\n>>>")

    # control flow
    if choice == "1":
        login()
    elif choice == "2":
        signup()
    elif choice == "3":
        print("GoodBye")
        time.sleep(1)
        exit()
    else:
        print("Invalid choice")
        start_menu()


# a function to add the user to the db
def signup():
    print("Welcome to the signup menu")


# a function to log in the user
def login():
    print("Welcome to the login menu")


# start the program with the menu
if __name__ == "__main__":
    pass
    start_menu()

# close the connection
conn.close()

