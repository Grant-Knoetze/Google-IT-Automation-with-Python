#!/usr/bin/env python3

# The point of OOP is defining real world concepts in a way that the computer understands.

class Apple:
    """Class names should start
    with a capital letter
    according to PEP8.
    """
    pass  # Use pass keyword to show that body is empty.


class Apple:
    """After defining the class we
    can now assign attributes to it."""
    color = " "
    flavor = " "


# To create a new instance
# of any class, we call the
# name of the class as if it
# were a function.
jonagold = Apple()  # Create a new instance of Apple class, and assign it to variable jonagold.
# Now set the values of the attributes using dot notation.
jonagold.color = "red"
jonagold.flavor = "sweet"
# Use print to check if the assignments were successful.
print(jonagold.color)
print(jonagold.flavor)
print(jonagold.color.upper())

granny_smith = Apple()
granny_smith.color = "green"
granny_smith.flavor = "sour"

print(granny_smith.color)
print(granny_smith.flavor)



