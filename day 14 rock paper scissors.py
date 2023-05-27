# the import is not working but works on replit main.py

from getpass import getpass as input

print("lets play rock, paper, scissors")

while True:
    player_one = input("Player one: Enter 'r' for 'rock', 'p' for 'paper' or "
                       "'s' for 'scissors'").lower()
    player_two = input("Player two: Enter 'r' for 'rock', 'p' for 'paper' or "
                       "'s' for "
                       "'scissors'").lower()
    if player_one == player_two:
        print("Its a draw")
    elif player_one == "r" and player_two == "p":
        print("Player one Wins.")
        if player_one == "r" and player_two == "s":
            print("Player two wins")
    elif player_one == "p" and player_two == "r":
        print("Player one wins")
        if player_one == "p" and player_two == "s":
            print("Player two wins.")
    else:
        if player_one == "s" and player_two == "p":
            print("Player one wins")
            if player_one == "s" and player_two == "r":
                print("Player two wins")

    play = input("Play again? y/n ").lower()
    if play == "n":
        break


print("Thank you for playing")


