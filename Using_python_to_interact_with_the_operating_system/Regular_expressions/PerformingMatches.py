#!/usr/bin/env python3

import re

p = re.compile('[a-z]+')
"""+ char is
for "one or more" 
repetitions """
print(p)
p.match("")
print(p.match(""))
# Test with a simple if statement:

# Match objects always have a boolean value of "True"
# Since match() and search() return None when there is
# no match.

match = re.search(pattern=0, string=0)




