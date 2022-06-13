#!/usr/bin/env python3

# Methods are functions that operate on the attributes of a specific instance of
# a class.

# Define a class and create an instance of it.

class Piglet:
    """Objects need methods to
    perform actions, lets give hamlet a voice."""
    def speak(self):
        print("oink oink")


hamlet = Piglet()
# We call the speak method on Hamlet.
hamlet.speak()
