# def name(arg1,arg2,....):
def pizza_order(topping1, topping2):
    if topping1 == "pepperoni":
        print(topping1, "is a great choice")
    else:
        print(topping1, "is kinda lame on pizza")
        print(topping2, "sounds delicious, much better than", topping1)


topping1 = input("Name a pizza topping. ")
topping2 = input("Name a second pizza topping. ")

pizza_order(topping1, topping2)

def myDice(sides):
    import random as ran
    dice = ran.randint(1, sides)
    print("You rolled", dice)


# calling the function
sides = int(input("How many sides on the die >>> "))
myDice(sides)
# using the function in a loop
for i in range(10):
    myDice(sides)
