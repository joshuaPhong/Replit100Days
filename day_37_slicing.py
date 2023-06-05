# slicing strings string[start:stop:step] stop is <
my_string = "Hello my name is Joshua"
# strings are lists / arrays of chars
# print the first char index 0
print(my_string[0])
# print hello
print(my_string[0: 5])
# we can use the default start = 0
print(my_string[:5])

# the split() function
print(my_string.split())
# how many words are in the string
print(len(my_string.split()))
# print the first word
print(my_string.split()[0])
