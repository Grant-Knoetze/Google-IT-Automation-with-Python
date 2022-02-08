# Dictionary practice:
x = {}
print(type(x))

file_counts = {"py": 34, "jpg": 89, "txt": 64, "webp": 82}
print(file_counts)

# Use the key to access the value, syntax is square brackets as for accessing an index in a list:
print(file_counts["txt"])

# Use "in" keyword to check if a key is contained in a dictionary: - Why is it False for value? Only checks for keys :)
print("webp" in file_counts)
print(34 in file_counts)

# Add a key:value pair:
file_counts["html"] = 987
print(file_counts)

# Use a key that already exists in the dictionary:
file_counts["webp"] = 875
print(file_counts)

# Delete a key:
del file_counts["html"]
print(file_counts)

# Iterating through the dictionary using a for loop:
for extension in file_counts:
    print(extension)

# Using a comprehension to iterate over the dictionary:
extension_list = [print(extension) for extension in file_counts]

# Using items method to return value:
for ext, amount in file_counts.items():
    """First element is key (ie:ext)
    second element is value (ie:amount)"""
    print("There are {} files with the .{} extension".format(amount, extension))

# Use built in methods to access keys or values:
print(file_counts.keys())
for keys in file_counts.keys():
    print(keys)

print(file_counts.values())
for values in file_counts.values():
    print(values)


def count_letters(text):
    """Initialize an empty dictionary"""
    result = {}
    """If letter is not in dictionary
    initialize an entry in dictionary 
    with a value of 0"""
    for letter in text:
        if letter not in result:
            result[letter] = 0
            """Increment the count for
            that letter in the dictionary"""
    result[letter] += 1
    return result


print(count_letters("ssssssssss"))
print(count_letters("Grant Knoetze"))
