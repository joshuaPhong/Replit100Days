print("🤓 Contact card 🤡")

# variable to user input
name = input("Input your name: ")
date = input("Input your date of birth: ")
phone = input("Input your phone number: ")
address = input("Input your address: ")

# create the dictionary in one line
my_dict = {"name": name, "date": date, "phone": phone, "address": address}

# creat the dictionary one key : value pair at a time
# my_dict = {}
# my_dict["name"] = name
# my_dict["date"] = date
# my_dict["phone"] = phone
# my_dict["address"] = address


# send user input straight to a dictionary.
# The variable is the dictionary key : the input is the value
my_dict["age"] = input("Input your age")

# when printing with f-strings.
# remember to use different quotes "f-string" 'key'
print(f"Your age is {my_dict['age']}")

print(f"Your name is {my_dict['name']}.\nYou were born on {my_dict['age']}.\nYour phone number is {my_dict['phone']}")
