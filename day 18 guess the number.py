# import thr random module
import random as r

# initialise a random number using the randrange method (start, stop, step)
# we could also use the randint(start, stop)
# a random number between 1 and 10
number = r.randrange(1, 10, 1)
# print(number)
# initialise the attempts counter
count = 0
print("Welcome")
print("-" * 7)
print("Lets guess a number between 1 and 10.")

# start the loop
while True:
    guess = int(input("Guess >>> "))
    if guess == number:
        count += 1
        break
    elif guess > number:
        print("Too high")
        count += 1
        continue
    elif guess < 0:
        print("You broke me 😥")
        exit()
    else:
        print("Too low")
        count += 1
        continue
print("Amazing 😀\nYou guessed correctly in", count, "attempts")
