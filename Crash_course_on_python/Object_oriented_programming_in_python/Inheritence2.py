#!/usr/bin/env/python3

class Animal:
    """Define the animal class and assign the class
    variable sound, and define two class methods, one
    special __init__ method, and another speak method."""
    sound = ""
    scream = ""

    def __init__(self, name):
        """Define the special method and the instance variable; name."""
        self.name = name

    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))

    def scream(self) -> object:
        print("I'm {name}! {scream}".format(name=self.name, scream=self.scream))


class Piglet(Animal):
    """Define the Piglet sibling class, and
    instantiate the sound class variable as oink."""
    sound = "Oink!"
    scream = "Freedom for captive pigs!"


# Create an instance of the Piglet class and call the speak method on it:
hamlet = Piglet("Hamlet")
hamlet.speak()
jeronimo = Piglet("Jeronimo")
jeronimo.speak()
