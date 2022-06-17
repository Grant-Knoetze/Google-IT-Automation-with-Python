#!/usr/bin/env python3

class Apple:
    """The constructor of a class
    is the method that is called when the
    name of the class is called, it
    is always named __init__,
    after which we define a
    string method to return an
    instance's attributes
    in string format."""

    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)


jonagold = Apple("red", "sweet")
print(jonagold.color)
print(jonagold.flavor)

granny_smith = Apple("green", "sour")
print(granny_smith.color)
print(granny_smith.flavor)

print(jonagold)
