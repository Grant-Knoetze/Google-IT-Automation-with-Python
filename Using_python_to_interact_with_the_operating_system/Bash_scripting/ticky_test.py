import csv
import operator
import re
import sys

dict_errors = {}
dict_per_usr = {}
user_count = []


# Open the file
def open_file(log_file):
    """Set regular expression to find lines containing ERROR"""
    with open(log_file, "r+") as file:
        data = file.readlines()
    return data


# Match patterns:
def generate_dict(data_lines):
    for line in data_lines:
        pattern_error = re.search(r"ticky: ERROR ([\w ]*)", line)
        pattern_user = re.search(r"\(([\w\. ]*)\)", line)

        # generate dict_errors dictionary
        if pattern_error != None:
            if pattern_error.group(1) not in dict_errors.keys():
                dict_errors[pattern_error.group(1)] = 1
            else:
                dict_errors[pattern_error.group(1)] += 1


print(log_errors())


def main():
    log_file = sys.argv[1]


if __name__ == "__main__":
    main()
