line = "string"
print(line[:1])
line = "string"
print(line[:1])

message = "A kong string with a silly typo"
"""Strings are immutable and a TypeError 
for object assignment is generated..."""
print(message[0:2])
print(message[3:])

new_message = message[0:2] + "L" + message[3:]
"""Therefore concatenate strings"""
print(new_message)
