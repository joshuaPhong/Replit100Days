# for loops used when we know how many times we want to iterate
# for new variable in range (number of values):
# for counter in range(10):
#     print(counter)
# range starts at 0

# day 19 challenge. Loan Calculator
# $1000 at 5% per year for 10 years
print("LOAN CALCULATOR")
print("-" * 15)
print("$1000 @ 5% for 10 years")

loan = int(input("How much would you like to borrow >>> "))
years = int(input("How many years will you borrow for >>> "))
rate = int(input("At what rate will you borrow x% >>> "))
for year in range(years):
    loan += loan * (rate / 100)
    print("Year", year + 1, loan)

