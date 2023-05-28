# day 20 challenge list generator
# using for loop
print("List Generator")
print("-" * 14)

while True:
    # take user inputs
    start = int(input("Enter a starting number >>> "))
    end = int(input("Enter an ending number >>> "))
    increment = int(input("Enter an increment value >>> "))
    # check the user inputs can be used in the range function
    if start > end and increment > 0:
        print("Increment must be negative for a countdown")
        continue
    elif end > start and increment < 1:
        print("Increment must be at least one to count.")
        continue
    else:
        for i in range(start, end, increment):
            print(i)
    break
