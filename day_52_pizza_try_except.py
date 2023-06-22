# Pizza shop challenge using try and except
#
# Prompt the user to input the quantity and size of pizzas.
#
# Multiply the two inputs together to calculate the cost of the pizzas.
#
# Store that in a 2D list with the user's name.
#
# Use try.... except for two reasons:
#
# Include auto-save and autoload. Use it with the autoload. When casting the quantity of pizzas to an integer.
# Avoid the user crashing the program by typing 'three' instead of '3'. Or any other non-integer input. If they do,
# then prompt them to try again.


import time
import traceback
import os

pizza_order = []
debug_mode = True
large_pizza = 10
medium_pizza = 8
small_pizza = 6


def tidy_screen():
    print()
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(1)


def tidy_input(text):
    return text.strip().lower()


def pretty_print_list(a_2d_list):
    print()
    for row in a_2d_list:
        for item in row:
            print(item, end=", ")


#   using a return statement for the pretty print function
# def pretty_print_list(a_2d_list):
#     result = ""
#     for row in a_2d_list:
#         for item in row:
#             result += str(item) + ", "
#         result += "\n"
#     return result


def auto_load(file):
    global pizza_order
    try:
        with (open(file, "r")) as f:
            pizza_order_contents = f.read()
            if pizza_order_contents:
                pizza_order = eval(pizza_order_contents)
            else:
                pizza_order = []
    except Exception as err:
        print(f"Load error: {err}\nTry again")
        if debug_mode:
            print(traceback.format_exc())


def auto_save(file):
    try:
        with open(file, "w") as f:
            f.write(str(pizza_order))
    except Exception as err:
        print(f"Save error: {err}")
        if debug_mode:
            print(traceback.format_exc())


def main_menu_message():
    print("🍕🍕 Pizza 🍕🍕\nWelcome: Lets order")
    time.sleep(1)


def main_menu():
    price = None
    main_menu_message()

    while True:
        tidy_screen()
        user_name = input("Please enter your name: ")
        size = input("What size pizza do you want:\n1. Large\n2. Medium\n3. Small\nEnter >>> ")
        try:
            if int(size) == 1:
                price = large_pizza
            elif int(size) == 2:
                price = medium_pizza
            elif int(size) == 3:
                price = small_pizza
            # else:
            #     print("Input error\nTry again")
            #     continue
        except Exception as err:
            print(f"Input error, try again\n{err}")
            time.sleep(1)
            continue
        quantity = input("How many pizza's do you want: ")
        try:
            cost = price * int(quantity)
        except Exception as err:
            print(f"Error: {err}, try entering a number")
            if debug_mode:
                print(traceback.format_exc())
            continue
        order = [user_name, cost]
        pizza_order.append(order)
        auto_save("pizza_orders.txt")
        print(f"Hello {user_name} your order cost ${cost}")
        pretty_print_list(pizza_order)
#         place another order

        order_again = tidy_input(input("\nDo you want to order another pizza: Y/n\n>>> "))
        if order_again == "y":
            continue
        else:
            print("Thanks for your 🍕 order")
            exit()


auto_load("pizza_orders.txt")
main_menu()
