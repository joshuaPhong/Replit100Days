# import the tkinter module
import tkinter as tk

# create the window (gui)
window = tk.Tk()
# add a title to the window
window.title("Joshua's first window")
# size the window
window.geometry("400x400")

label = 0  # a variable to contain the label text


# a sub routine to update the label
def update():
    global label  # use the label variable from outer scope
    label += 1  # the label will equal the function input. increase the value of label by one


# a sub routine to increase the label value by the users input
def get_from_text_box():
    global label
    # get input from the text box (called text). start at position 1 and get until the end
    number = text.get(1.0, "end")
    try:

        number = int(number)  # cast the input
        label += number  # increase the value of the label by the input
        hello["text"] = label  # hello is the tkinter label variable, and "text" is the inner text
    except ValueError:
        pass


# elements are displayed in the order they are coded

# the pack() function places the elements in the window
# we can add argument to the pack() function.
# e.g. button.pack(side=tk.BOTTOM) we can also use LEFT, RIGHT, TOP AND CENTER.

# we can use the .grid(row=, column=) function instead of pack()

hello = tk.Label(text=label)  # Creates a text box
hello.grid(row=0, column=0)  # aligns the box in a grid
# hello.pack()  # 'pack' places the element on the screen

# Creates a button. Button text is string. Command calls the function. It will increase the label by one

button = tk.Button(text="Click me!",
                   command=get_from_text_box)
button.grid(row=0, column=1)
# button.pack()

# create a text box for user input
# Three arguments, name of the window to place the text box in, height & width.
text = tk.Text(window, height=1, width=50)
text.grid(row=0, column=2)
# text.pack()

# run the tkinter window
tk.mainloop()
