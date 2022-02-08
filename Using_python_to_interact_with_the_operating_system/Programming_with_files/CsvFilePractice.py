import os
import csv


# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = "row"

    # Call the function to create the file
    create_file(filename)

    # Open the file


f = open("flowers.csv")
# Read the rows of the file into a dictionary
csv_f = csv.reader(f)
# Process each item of the dictionary
for row in csv_f:
    color, name, type = row
return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
print()

# Call the function
print(contents_of_file("flowers.csv"))
