#  creating a debug_mode mode
debug_mode = True

import traceback
myStuff = []
#  try the code
try:
    f = open("Stuff.mine", "r")
    myStuff = eval(f.read())
    f.close()
# if the code doesn't work, then do this.
except:
    print(f"Your file may not exist\n")
# print the rows of the list
for row in myStuff:
    print(row)

# declaring the type of errors, we want to look for
try:
    f = open("Stuff.mine", "r")
    myStuff = eval(f.read())
    f.close()
#     Exception = all errors
except Exception as err:
    print(err)

# printing the traceback
try:
    f = open("Stuff.mine", "r")
    myStuff = eval(f.read())
    f.close()
except Exception as e:
    # use the imported tracback like would normally happen iin console
    # the format exception as a string / printable format
    print(traceback.format_exc())


#  using the debug_mode mode
try:
    f = open("Stuff.mine", "r")
    myStuff = eval(f.read())
    f.close()
except Exception as e:
    # message to the user
    print(f"Error {e}")
    # use the debug mode to show the developer a traceback
    if debug_mode:
        print(traceback.format_exc())