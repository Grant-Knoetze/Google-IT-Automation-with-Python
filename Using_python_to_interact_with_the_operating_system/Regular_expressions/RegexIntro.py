#!/usr/bin/env python3

import re

# Use the item method in this log:
log = "July 31st 07:51:48 my_computer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
print(log[index + 1:index + 6])

result = re.search(r"a", "July 31st 07:51:48 my_computer bad_process[12345]: ERROR Performing package upgrade")
""" r is for raw string,
 always use for regex in python."""
print(result)

result2 = re.search(r"aza", "plaza")
"""Remember inclusive Vs exclusive
 with sequence splitting"""
print(result2)

result4 = re.search(r"aza", "mo")
"""None"""
"""Remember inclusive Vs exclusive
 with sequence splitting"""
print(result4)

result3 = re.search(r"aza", "bazaar")
print(result3)

""". is a wildcard,
 can represent any character"""

print(re.search(r"[Pp]ython", "Python"))

print(re.search(r"[a-z]way", "The end of the highway"))

