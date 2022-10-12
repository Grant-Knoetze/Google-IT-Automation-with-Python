import csv
import operator
import re
import sys

dict_errors = {}
dict_per_usr = {}
user_count = []


def open_file():
    """Set regular expression to find lines containing ERROR"""
    with open(log_file) as file:
        data = file.readlines()
    return data


pattern_error = re.search(r"ticky: ERROR ([\w ]*)", line)

print(log_errors())


def main():
    log_file = sys.argv[1]


if __name__ == "__main__":
    main()
