#!/usr/bin/env python3

def myOuterFunction(n):
    def myInnerFunction():
        print("Hello from inner function")

    def myInnermostFunction():
        print("This is a second nested function")

    print("Hello from OuterFunction")
    if n % 2 == 0:
        return myInnermostFunction()  # Call inner function from within outer function.
    else:
        return myInnerestFunction()


def myOuterFunction2():
    def myInnerFunction2():
        print("Hello from inner function2")

    print("Hello from OuterFunction2")
    return myInnerFunction2()  # Function can return a function.


myOuterFunction(4)
myOuterFunction2()
