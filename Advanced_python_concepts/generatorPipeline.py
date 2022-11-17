#!/usr/bin/env python3

def odd_filter(nums):
    """Square the number"""
    for num in nums:
        if num % 2 != 0:
            yield num

# Generator pipeline takes odd_filter function 
generator_pipeline = odd_filter(range(1000))
for n in generator_pipeline:
    print(n)