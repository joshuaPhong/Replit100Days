# loops
# while loop
counter = 0
while counter <= 100:
    print("The counter is less than 10: ", counter)
    # counter = counter + 1. Stops an infinite loop
    counter += 1

# while loop with strings. This loop will run until the answer is yes
# initialise the counter
exit_loop = ""
# start the loop + condition
while exit_loop != "yes":
    # the loop will execute code that is indented
    print("Your in the loop")
    # if the user enters yes the variable will not satisfy the condition and
    # the loop will end
    exit_loop = input("Exit? 'yes'").lower()
# the loop will not execute this line becuase it is outside the loop.
# Not indented
print("Your out of the loop")

# day 15 challenge
animal = ""
exit_loop = ""
while exit_loop != "yes":
    animal = input("What animal sound do you want? Cow, Sheep or Dog "
                   ">>> ").lower()
    if animal == "cow":
        print("Moo\n")
    elif animal == "sheep":
        print("Baaaa\n")
    else:
        print("Woof\n")
    exit_loop = input("Do you want to exit? 'yes'").lower()
print("Thank you for using my program")



