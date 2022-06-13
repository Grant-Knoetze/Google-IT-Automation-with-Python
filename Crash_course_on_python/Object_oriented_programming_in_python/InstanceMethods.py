#!/usr/bin/env python3

# Methods are functions that operate on the attributes of a specific instance of
# a class.

# Define a class and create an instance of it.

class Piglet:
    """Objects need methods to
    perform actions, lets give hamlet a voice."""

    def speak(self):
        print("oink oink")

    def squeal(self):
        print("shriek! shriek!")


hamlet = Piglet()
# We call the speak method on Hamlet.
hamlet.speak()

jeronimo = Piglet()
jeronimo.speak()
jeronimo.squeal()


class Kitten:
    name = "Kitty"  # Instance variable.
    years = 0

    def cat_years(self):
        return self.years * 15

    def meow(self):
        print("Meow! I'm {}! Meow!".format(self.name))


misha = Kitten()
misha.name = "Misha"
misha.meow()

prince = Kitten()
prince.name = "Prince"
prince.meow()
prince.years = 2
print(prince.cat_years())

