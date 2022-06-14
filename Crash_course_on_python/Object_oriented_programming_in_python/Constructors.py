#!/usr/bin/env python3

class Apple:
    """The constructor of a class
    is the method that is called when the
    name of the class is called, it
    is always named __init__"""

    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


jonagold = Apple("red", "sweet")
print(jonagold.color)
print(jonagold.flavor)
