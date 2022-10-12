import csv
import operator
import re
import sys


def log_errors():
    """Set regular expression to find lines containing ERROR"""


with open("/var/log/syslog") as file:
    for line in file:
        info = re.findall(r"ticky: (?P<logtype>INFO|ERROR)", line)

print(log_errors())
