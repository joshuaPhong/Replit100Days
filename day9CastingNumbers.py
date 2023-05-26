# myScore = int(input("Your score: "))
# if myScore > 100000:
#     print("Winner!")
# else:
#     print("Try again 😭")
#
# myPi = float(input("What is Pi to 3dp? "))
# if myPi == 3.142:
#     print("Exactly!")
# else:
#     print("Try again 😭")
#  challenge
generation = int(input("What year were you born >>> "))
if 1925 < generation <= 1946:
    print("You are a traditionalist 👴")
elif 1947 <= generation <= 1964:
    print("You are a baby boomer 👶")
elif 1965 <= generation <= 1981:
    print("You are a gen X 😎")
elif 1982 <= generation <= 1995:
    print("You are a millennial 🐸")
elif 1996 <= generation <= 2015:
    print("You are a gen Y 🥱")
else:
    print("You have no generation")