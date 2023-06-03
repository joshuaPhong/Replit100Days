import day_29_print_arguments

# f-strings
# output strings and variables
name = "Joshua"
age = 50
pronouns = "He/Him"
# f-strings using .format
response = (
    "This is an f-string. my name is {name}, I am {age} years old. Also {name} is a {pronouns}.".format(name=name,
                                                                                                        age=age,
                                                                                                        pronouns=pronouns))
print(response)

# f-strings using f""
response_f = f"This is also an f-string. I am still {age} years old. A {pronouns} called {name}."
print(response_f)

# passing an f-string variable to a function
print(day_29_print_arguments.change_color("red", response_f))
print(day_29_print_arguments.change_color("", ""))
# alignment
# f" {variable: Alignment and Number of characters}"
for i in range(1, 101):
    print(f"I have done {i: <3} days of python")
    print(f"I have done {i: ^3} days of python")
    print(f"I have done {i: >3} days of python")

print("30 Days down")
for i in range(1, 30):
    day = input(f"What did you think of day {i}? >>> ")
    print(f"You say that day {i} was \n{day: ^20}")