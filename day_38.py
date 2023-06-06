# loops in string chars
my_string = " This is my testing string"
# loop through the chars. letter = a char in the string
for letter in my_string:
    # print each char. default in print is \n
    # print(letter)
    # end="" overrides the default. there is "" no space after each iteration
    print(letter, end="")
print()
#     if statement inside the loop
for letter2 in my_string:
    # check if the letter i r
    if letter2.lower() == "r":
        # change the color to red
        print("\033[0;31m", end="")
    elif letter2.lower() == "t":
        # bold
        print("\033[1m", end="")
    print(letter2, end="")
    # change the color to default / white
    print("\033[0m", end="")

# check if in a list
letter_list = ['a', 'e', 'i', 'o', 'u']
letter_list2 = ['t', 'g']
print()
for letter3 in my_string:
    if letter3.lower() in letter_list:
        # change to cyan
        print("\033[0;36m", end="")
    elif letter3.lower() in letter_list2:
        print("\033[0;30m", end="")
    print(letter3, end="")
    # change to default
    print("\033[0m", end="")
