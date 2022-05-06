#!/usr/bin/env Python3

import re

# Using regex to find a PID...

log = "July 31 07:51:48 my_computer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
results = re.search(regex, log)
print(results[1])


def extract_pid(log_line):
    """Define a function
    that extracts the PID
    if possible"""
    regex_new = r"\[(\d+)\]: ([A-Z]*)"
    result = re.search(regex_new, log_line)
    if result is None:
        return None
    return"{} ({})".format(result[1], result[2]) 


print(extract_pid(log))

# Splitting and replacing:

print(re.split(r"[.!?]", "One sentence. Two. Three sentences."))

# Capture in parentheses to include the characters...

print(re.split(r"([.!?])", "One sentence. Two. Three sentences."))
