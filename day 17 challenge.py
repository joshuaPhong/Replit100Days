# the import is not working but works on replit main.py

# from getpass import getpass as input

print("ROCK PAPER SCISSORS")
print("-" * 19)
# how many round in the game
rounds = int(input("How many rounds do you want to play? >>> "))
# initialise the scoring variables
player_one_score = 0
player_two_score = 0
#
p1w = "Player One Wins"
p2w = "Player Two Wins"
# loop through the game play
while True:
    # give the players their score
    print("Player One: ", player_one_score, "Player Two: ", player_two_score)
    # is the game over?
    if player_one_score == rounds:
        print("Game Over\nCongratulations Player One")
        exit()
    else:
        if player_two_score == rounds:
            print("Game Over\nCongratulations Player Two")
            exit()
    # takes the users input for the game conditions
    player_one = input("Player one: Enter 'r' for 'rock', 'p' for 'paper' or "
                       "'s' for 'scissors' >>> ").lower()
    player_two = input("Player two: Enter 'r' for 'rock', 'p' for 'paper' or "
                       "'s' for "
                       "'scissors' >>> ").lower()
    # games winning conditions for each player
    if player_one == player_two:
        print("Its a draw")
        continue
    elif player_one == "r" and player_two == "p":
        print(p2w)
        player_two_score += 1
        continue
    elif player_one == "r" and player_two == "s":
        print(p1w)
        player_one_score += 1
        continue
    elif player_one == "p" and player_two == "r":
        print(p1w)
        player_one_score += 1
        continue
    elif player_one == "p" and player_two == "s":
        print(p2w)
        player_two_score += 1
        continue
    elif player_one == "s" and player_two == "p":
        print(p1w)
        player_one_score += 1
        continue
    else:
        if player_one == "s" and player_two == "r":
            print(p2w)
            player_two_score += 1
            continue

    #         the commented code ask the user if they want to continue the
    #         game and sends them to the top of the loop
    #         this is replaced by the continue command and the exit() after the score
    #         is 3
    # play = input("Play again? y/n ").lower()
    # if play == "n":
    #     break
# unreachable with the exit() functions
print("Thank you for playing")
