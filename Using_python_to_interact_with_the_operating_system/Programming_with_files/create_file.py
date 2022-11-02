import os
import csv


# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,species\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")


create_file("flowers.csv")

# Unpack flowers.csv

with open("flowers.csv") as f:
    csv_file = csv.reader(f)
    for row in csv_file:
        name, color, species = row
    print("Name: {}, color {}, species {}".format(name, color, species))
    print(row[0], row[1], row[2])

