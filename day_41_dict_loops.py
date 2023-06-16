# loops and dictionaries
# define a dictionary
my_dictionary = {"name": "Ian", "health": 99, "strength": 123, "equipped": "sword"}
# loop through the dictionary

# this loop will print out the "keys":
print("The keys")
for i in my_dictionary:
    print("", i, " ", end="")

# print out the :"values"
print("\nthe values")
for i in my_dictionary:
    print(my_dictionary[i], " ", end="")

# built-in functions
# .items()
print("\nUsing the .items() function.")
for items in my_dictionary.items():
    print(items)

print("\nUsing the .items() for the key and the value. We need two variables")
for keys, values in my_dictionary.items():
    print(keys, values)
for keys, values in my_dictionary.items():
    print(f"\nUsing an f-string inside the loop. Key: {keys} Value: {values}")

# including if statements
print("\nUsing if statements in the for loop of a dictionary")
for keys, values in my_dictionary.items():
    print(f"{keys}: {values}")
    if keys == "name":
        print("Your an 🥚")
    if keys == "health":
        if values < 100:
            print("You better eat dude!! 🍊")
    if keys == "strength":
        if values < 100:
            print("Weak sauce man")
        else:
            print("Whoa 💪")
    if keys == "equipped":
        print("ready for battle 🪄🔪🗡️⚔️🏹")

# using the .keys() function
print("\nUsing the .keys() function")
for keys in my_dictionary.keys():
    print(keys, end=" ")

# using the .values()
print("\nUsing the .vales() function")
for values in my_dictionary.values():
    print(values, end=" ")
