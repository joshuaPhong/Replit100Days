# 2d lists list[][]
# access row[] column[]
my_2d_list = [
    ["jonny", 21, "mac"],
    ["corina", 47, "mac"],
    ["josh", 50, "dell"]
]
print(my_2d_list)
print(my_2d_list[0])
print()
print(my_2d_list[0][0], my_2d_list[0][1], my_2d_list[0][2])
# change a value
my_2d_list[0][2] = "linux"
print(my_2d_list)

#  loop over a list of lists
for i in my_2d_list:
    for j in i:
        print(j)