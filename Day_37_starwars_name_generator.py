
title = "star waRS name generator".title()
print(f"\033[0;31m{title: ^70}")

user_input_1 = input("\033[0mPlease enter your First name and Last name.\n>>> ").capitalize()
f_name = (user_input_1.split()[0])[0:3]
l_name = (user_input_1.split()[1])[0:3]
user_input_2 = input("Please enter your mothers maiden name and the city your were born in\n>>> ").capitalize()
m_name = user_input_2.split()[0][0:2]
city = user_input_2.split()[1][:-4:-1]
print(f"Your Star Wars name is {f_name}{l_name} {m_name}{city}")