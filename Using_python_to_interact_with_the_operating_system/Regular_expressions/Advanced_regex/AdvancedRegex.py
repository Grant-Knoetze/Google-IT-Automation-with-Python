#!/usr/bin/env Python3

import re

# Using regex to find a PID...

log = "July 31 07:51:48 my_computer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])


