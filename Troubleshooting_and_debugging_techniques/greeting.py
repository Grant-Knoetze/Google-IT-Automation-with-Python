import random


def greeting():
    name = input("Hello! What is your name?")
    number = random.randint(0, 100)
    print("Hello " + str(name) + "!" + "Your random number is " + str(number))


greeting()
