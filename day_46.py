#  our dictionary
clue = {}


# a pretty print function for looping through nested dictionaries
def prettyPrint():
    print()
    for key, value in clue.items():
        # moves along every 'key:subDictionary' pair and outputs the key (the name of the character).
        print(key, end=": ")
        for subKey, subValue in value.items():
            # (nested) `for` loop moves along every sub-key and sub-value in each subDictionary.
            print(subKey, subValue, end=" | ")
        print()


def cluedo_dictionary():
    while True:
        name = input("Name: ")
        location = input("Location: ")
        weapon = input("Weapon: ")

        clue[name] = {"location": location, "weapon": weapon}  # line 7

        prettyPrint()


# accessing a single item
john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John": john, "Janet": janet, "Erica": erica}
# remember the "" '' quotes inside an f-string must be different
# the [] contain the dictionary keys
# print the whole dictionary
print(f"A dict of dict: {courseProgress}")
# print a single nested dictionary
print(f"A nested dict : {courseProgress['Janet']}")
# print a value from a nested dictionary
print(f"A value from a nested dict: {courseProgress['Janet']['streak']}")

