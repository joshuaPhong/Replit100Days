# generate a bingo card with ordered and random numbers
import random


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


rnd_num = random_numbers()
# print(rnd_num)
bingo = [
    [rnd_num[0], rnd_num[1], rnd_num[2]],
    [rnd_num[3], "bingo", rnd_num[4]],
    [rnd_num[5], rnd_num[6], rnd_num[7]]
]

# print an fstring bingo | bingo | bingo -------------......
#  alignment. each variable has a space of five chars. aligned to the left, center ant right respectively

print(f"{bingo[0][0]:<5} | {bingo[0][1]:^5} | {bingo[0][2]:>5}")
print("-" * 21)
print(f"{bingo[1][0]:<5} | {bingo[1][1]:^5} | {bingo[1][2]:>5}")
print("-" * 21)
print(f"{bingo[2][0]:<5} | {bingo[2][1]:^5} | {bingo[2][2]:>5}")