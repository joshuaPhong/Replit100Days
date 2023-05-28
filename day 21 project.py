# math multiplication project

print("Math Game")
print("-" * 9)
print("Lets test your times tables")
multiple = int(input("Enter your multiple >>> "))
correct = 0
for i in range(1, 11):
    print(i, "X", multiple, "=", )
    ans = int(input(">>> "))
    if ans == i * multiple:
        print("Correct")
        correct += 1
    else:
        print("Sorry, the answer was", ans)

print("You scored", correct, "/10")
if 1 < correct < 5:
    print("Not so good. Keep practicing")
elif 5 < correct <= 7:
    print("Good work 🙂")
elif 8 < correct <= 9:
    print("Great 😁😊")
else:
    print("Great work 😁😁😁😁🤓🤓🤓🤓")
