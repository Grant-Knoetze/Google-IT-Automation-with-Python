#!/usr/bin/env python3

def odd_filter(nums):
    """Yield odd numbers only"""
    for num in nums:
        if num % 2 != 0:
            yield num


def square(nums):
    """Square the numbers"""
    for num in nums:
        num **= 2
        yield num


def create_strings(nums):
    """Create strings"""
    for num in nums:
        yield "The string value is-------->{}".format(str(num))


# Generator pipeline takes odd_filter function
generator_pipeline = create_strings(square(odd_filter(range(1000))))

for n in generator_pipeline:
    print(n)
