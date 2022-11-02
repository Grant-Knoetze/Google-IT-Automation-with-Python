# Implementation of linear search using the "enumerate" built in method.

list = ["Grant", "Jenny", "Jeffrey", "Jack", "Claire", "Joe", "Jake", "Abigail"]


def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1


print(linear_search(list, "Jack"))
