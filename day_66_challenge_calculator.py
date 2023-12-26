# import the tkinter module
import tkinter as tk

# make the calculator window
calculator = tk.Tk()
# calculator title
calculator.title("Calculator")
# size the window
calculator.geometry("500x500")

# declare and initialise our user input variable
answer = 0

# todo function to combine string input
#  todo function to capture and assign the operator variable
# todo function to do the calculation





# create a label to display the result

result = tk.Label(text=answer)
result.grid(row=0, column=0)
#  todo use command= lambda: to pass data to the function
#  create the buttons and grid align
one = tk.Button(text="1")
one.grid(row=1, column=0)

two = tk.Button(text="2")
two.grid(row=1, column=1)

three = tk.Button(text="3")
three.grid(row=1, column=2)

four = tk.Button(text="4")
four.grid(row=2, column=0)

five = tk.Button(text="5")
five.grid(row=2, column=1)

six = tk.Button(text="6")
six.grid(row=2, column=2)

seven = tk.Button(text="7")
seven.grid(row=3, column=0)

eight = tk.Button(text="8")
eight.grid(row=3, column=1)

nine = tk.Button(text="9")
nine.grid(row=3, column=2)

# todo: operator buttons

# run the program
tk.mainloop()
