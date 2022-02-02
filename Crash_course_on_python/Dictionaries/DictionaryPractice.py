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

