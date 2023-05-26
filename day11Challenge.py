# how many seconds in a year
seconds = 60
minute = 60
hour = 24
day = 365

print("Lets calculate the seconds in a year ")
leap_year = input("Is it a leap year? y/n")
if leap_year.lower() == "y":
    day += 1
year = seconds * minute * hour * day
print(year)
