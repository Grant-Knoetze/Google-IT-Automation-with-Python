# To check whether the string matches the requirements for a python variable...
import re

pattern = r"^[a-zA-Z_]*$" # We store the pattern we want to match as a variable...
print(re.search(pattern, "_this_is_a_valid_variable_name_in_python"))
print(re.search(r"p.ng", "Pangea", re.IGNORECASE))

print(re.search(r"[Pp]ython", "Python"))

print(re.search(r"Pytho[Nn]", "Python"))

print(re.search(r"[a-z]way", "The end of the highway"))

print(re.search(r"[a-z]way", "What a way to go"))

print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))

print(re.search(r"[^A-Za-z ]", "This is a string with spaces."))




