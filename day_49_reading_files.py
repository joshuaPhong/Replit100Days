# open file in "r" read mode. assign a variable
f = open("high.score", "r")
# read the file an assign it a variable
contents = f.read()
# split the contents into separate items
contents = contents.split()
# close the file
f.close()
# print the file
print(contents)

# reading oneline at a time
# open the file
f = open("high.score", "r")
# read a single line
contents = f.readline()
# print the line
print(contents)
# close the file
f.close()

# to use readline in a loop
f = open("high.score", "r")
while True:
    # open the file
    # read a single line
    contents = f.readline().strip()
# check for the end of the file
    if contents == "":
        break
    # print the line
    print(contents)
    # close the file
f.close()


