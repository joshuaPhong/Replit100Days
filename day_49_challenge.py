import time, os

high_score = 0
name = None

f = open("high.score", "r")

contents = f.read()
contents = contents.split()

for index, item in enumerate(contents):
    try:
        item = int(item)
        if item > high_score:
            high_score = item
            name = contents[index - 1]
    except ValueError:
        continue

f.close()

print(contents)
print(f"{name} has the highest score: {high_score}")
s