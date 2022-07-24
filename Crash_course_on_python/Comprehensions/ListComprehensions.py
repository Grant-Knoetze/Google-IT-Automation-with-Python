# Create an empty list:
multiples = []
for x in range(1, 11):
    multiples.append(x * 7)
    print(multiples)

# To do the above in a list comprehension do as follows:
multiples3 = [x * 7 for x in range(1, 11)]
print(multiples3)
# Another example:
multiples2 = [x ** 8 for multiple in multiples]
print(multiples2)

# A list of strings:
names = ["Grant", "James", "Claire", "Marion", "Gert"]
lengths = [len(name) for name in names]
print(lengths)

# Using a conditional statement in a list comprehension:
z = [x for x in range(1, 101) if x % 3 == 0]
print(z)


def larger_sum(lst1, lst2):
    sum1 = [lst1 for i in lst1]
    sum2 = [lst2 for n in lst2]
    if sum1 >= sum2:
        return lst1
    else:
        return lst2


# Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))




