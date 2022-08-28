#!/usr/bin/env python3

import functools


def hello_message_decorator(func):
    """This is the hello message decorator"""

    def wrapper():
        """This is wrapper inside hello
        message decorator"""

        return ">>>>>> Wrapper: Hello! <<<<<<"
    return wrapper


@hello_message_decorator
def hello_message():
    """This is the hello message function
    Using the @ decorator, control is passed to
    the hello_message_decorator function"""
    return "hello"

print(hello_message())
#message = hello_message_decorator(hello_message)
#print(message())



