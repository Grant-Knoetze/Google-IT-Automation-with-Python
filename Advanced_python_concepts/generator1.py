
# Define a simple function first...s
def a_plus_b(a, b):
    result = a + b
    yield result


x = a_plus_b(4, 4)
print(x.__next__())
