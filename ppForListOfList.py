import random


def prettyPrint(your_list):
    print()
    for rows in your_list:
        for items in rows:
            # items refers to each item in the column for that row
            print(f"{items:^10}", end=" | ")
            # :^10 means 10 characters as the space with the data in the center. The end character has been changed
            # to space vertical line space to make it look more like a table.

        print()

    print()
