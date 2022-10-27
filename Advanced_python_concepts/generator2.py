# Create a generator function that squares two numbers

def square_numbers(n):
    for i in range(n):
        yield i ** 2



print(list(square_numbers(5)))
#x = square_numbers(5)

#for num in x:
    #print(num)

# Create generator function

numbers_cubed = (n ** 3 for n in range(98))

for num in numbers_cubed:
    print(num)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
