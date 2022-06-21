#!/usr/bin/env python3

class Fruit:
    """Constructor for the fruit
    class, initialize the color
    and flavor attributes as
    instance variables."""

    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "This fruit is {} and its flavor is {} ".format(self.color, self.flavor)


class Apple(Fruit):
    """Define the Apple
    sibling which inherits the attributes
    and methods from its parent class (Fruit)."""

    def __str__(self):
        return "This apple is {} and its flavor is {} ".format(self.color, self.flavor)


class Grape(Fruit):
    """Define the Grape
     sibling which inherits the attributes
     and methods from its parent class (Fruit)."""
    def __str__(self):
        return "This grape is {} and its flavor is {} ".format(self.color, self.flavor)


granny_smith = Apple("green", "sour")
"""Create an instance of the Apple class
granny_smith, and assign attributes to it."""
carnelian = Grape("purple", "sweet")
print(granny_smith.flavor)
print(carnelian.color)
print(granny_smith)
print(carnelian)
