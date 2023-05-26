# # Solve the following problems with my code
# # Your goal is to print the solution of all 3 calculations to the screen.

# # multiplication
# print(3.4 * 6.8)

# # division
# print(2467 / 4673)

# #raise 10 to the power of 2
# print(10**2)

# # print the remainder when 343 is divided by 4
# print(343 % 4)

myBill = float(input("What was the bill?: "))
tip_percentage = int(input("what % tip will you leave?: "))
tip = myBill * (tip_percentage/100)
print("Your tip is: ", tip)
total_bill = tip + myBill
numberOfPeople = int(input("How many people are splitting the bill?: "))
answer = total_bill / numberOfPeople
# round() takes a number and an int for precision
print("You all owe", round(answer, 2), "dollars.")