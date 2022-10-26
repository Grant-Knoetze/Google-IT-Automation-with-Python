# Create a generator function that squares two numbers

def square_numbers(n):
    for i in range(n):
        yield i ** 2

print(square_numbers(5))
