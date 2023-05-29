# subroutines are code that cn can be reused
# we use the def()
def myDice():
    import random as ran
    dice = ran.randint(1, 6)
    print("You rolled", dice)


# calling the function
myDice()
# using the function in a loop
for i in range(10):
    myDice()
