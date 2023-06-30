# recursion challenge
def factorial(value):
    if value == 1:
        print("Done")
    else:
        value *= factorial(value - 1)
    return value

print(factorial(10))