import csv
import operator
import re
import sys

dict_errors = {}
dict_per_usr = {}
user_count = []


def log_errors():
    """Set regular expression to find lines containing ERROR"""


with open(log_file) as file:
    for line in file:
        info = re.findall(r"ticky: (?P<logtype>INFO|ERROR)", line)

print(log_errors())


def main():
    log_file = sys.argv[1]


if __name__ == "__main__":
    main()
