#!/usr/bin/env python3

def gen_send(number=10):
    for n in range(number):
        yield n ** 2


gen1 = gen_send()
# Next method only yields the value
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())
