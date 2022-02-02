# Tuples are sequences of elements of any type that are immutable
# The position of the elements inside the tuple have meaning
# Use tuples to represent data that has more than one value, and needs
# to be kept together

full_names = ('John', 'Doe', 'Smith')


# When a function returns a value it returns a tuple

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


result = convert_seconds(5000)
print(result)
print(type(result))

# Tuples can be unpacked

hours, minutes, seconds = result
print(hours, minutes, seconds)

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

