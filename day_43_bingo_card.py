# generate a bingo card with ordered and random numbers
import random
import time
from ppForListOfList import prettyPrint as pP
from cleanInput import cleanInput as cI


def random_numbers():
    list_of_random_numbers = []
    for i in range(0, 8):
        i = random.randint(0, 90)
        if i not in list_of_random_numbers:
            list_of_random_numbers.append(i)
        else:
            continue
    #         returns a list i.e. not by indexes
    return sorted(list_of_random_numbers)


def nextNumber():
    while len(n_num_list) <= 90:
        next_number = random.randint(0, 90)
        if next_number in n_num_list:
            print(next_number)
            time.sleep(1)

            continue
        else:
            n_num_list.append(next_number)
            print(sorted(n_num_list))
            print(len(n_num_list))
            return next_number


n_num_list = []
rnd_num = random_numbers()
# print(rnd_num)
bingo = [
    [rnd_num[0], rnd_num[1], rnd_num[2]],
    [rnd_num[3], "bingo", rnd_num[4]],
    [rnd_num[5], rnd_num[6], rnd_num[7]]
]


# GAME PLAY
def play():
    exes = 0
    x = "X"
    while True:

        do_next_number = input("Next number: Y/n >>> ").title()
        if cI(do_next_number) == "y":
            num = nextNumber()
            print(num)
            for row in range(3):
                for item in range(3):
                    if bingo[row][item] == num:
                        bingo[row][item] = x
                        exes += 1
                        print(f" X's: {exes}")
                        time.sleep(1)
                    if exes == 8:
                        print("You Won")
                        break
                    else:
                        continue

            pP(bingo)
        else:
            print("Goodbye")
            break


# print the bingo table
pP(bingo)
# call play()
play()
