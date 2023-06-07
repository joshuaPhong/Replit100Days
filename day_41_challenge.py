# challenge
my_dict = {"name": "", "url": "", "description": "", "stars": ""}
for keys in my_dict.keys():
    print(keys, ":\n", end="")
    if keys == "name":
        my_dict["name"] = input("Enter your name: ")
    if keys == "url":
        my_dict["url"] = input("Enter your url: ")
    if keys == "description":
        my_dict["description"] = input("Enter a description: ")
    if keys == "stars":
        my_dict["stars"] = input("rate us on stars: ")

for keys, values in my_dict.items():
    print(keys, values)

# the solution:
website = {"name": None, "url": None, "desc": None, "rating": None}

for name in website.keys():
    website[name] = input(f"{name}: ")

print()
for name, value in website.items():
    print(f"{name}: {value}")
