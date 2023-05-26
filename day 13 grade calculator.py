# create a grade generator from user input
# user inputs a number and the generator converts this into a grade
# the grade is output to the screen

# title of application
print("Exam grade calculator\n")
# define the variables, user input to initialise variables
test_name = input("What is the name of the test you took >>> ")
score_max = int(input(f"What is the maximum score for {test_name} >>> "))
score_actual = int(input(f"What was your score for {test_name} >>> "))
# round the % to two decimal places
score_percent = round((score_actual / score_max * 100), 2)

# define the variable grade
grade = ""
# use if, elif, else to place the % in a grade table
if score_percent >= 90:
    grade = "A+ 😁"
elif 80 < score_percent <= 89:
    grade = "A 😀"
elif 70 < score_percent <= 79:
    grade = "B 😊"
elif 60 < score_percent <= 69:
    grade = "C 🙂"
elif 50 < score_percent <= 59:
    grade = "D 🤷‍♀️"
elif score_percent <= 49:
    grade = "U 🤦‍♀️"
else:
    print("Undefined entry. Please try again.\n")

# output to the user
print(f"Your mark is {score_percent}%. Your final grade is {grade}. ")
