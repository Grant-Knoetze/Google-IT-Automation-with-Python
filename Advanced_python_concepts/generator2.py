# Create a generator function that squares two numbers

def square_numbers(n):
    for i in range(n):
        yield i ** 2


x = square_numbers(5)
print(x.__next__())
print(x.__next__())
print(x.__next__())