# CSV
# using comma seperated value, files
# import the library
import csv

# open the file
with open("alcohol-available-for-consumption-year-ended-december-2022.csv") as a:
    # read the csv file with the csv library
    nz_alc = csv.reader(a)
    # loop through the output and print each row
    for row in nz_alc:
        # prints row as a list
        print(row)
        # use the .join() "seperator" .join(items to join)
        print(", ".join(row))

# use the DictReader() from the csv library
# open the file
with open("alcohol-available-for-consumption-year-ended-december-2022.csv") as a2:
    # DictReader treats the csv file like a dictionary
    a2_dict = csv.DictReader(a2)
    # add the total value of a column
    total = 0
    # loop through the rows
    for row in a2_dict:
        # print a column in a row
        print(row["Data_value"])
        # try to add the value. cast as a float
        try:
            total += float(row["Data_value"])
        # pass if the value cannot be cast
        except:
            pass
# print(nz_alc)
# print the total value of the "Data_value" column
print(f"The total value is {total}")
