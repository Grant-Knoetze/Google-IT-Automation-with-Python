import csv
import operator
import re
import sys

dict_errors = {}
dict_per_user = {}
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
            # Generate per_user dictionary
            if pattern_user != None:
                if pattern_user.group(1) not in dict_per_user.keys():
                    dict_per_user[pattern_user.group(1)] = {}
                    dict_per_user[pattern_user.group(1)]["INFO"] = 0
                    dict_per_user[pattern_user.group(1)]["ERROR"] = 0
                    # Count elements for each user
                    if pattern_error != None:
                        dict_per_user[pattern_user.group(1)]["ERROR"] = 1
                    else:
                        dict_per_user[pattern_user.group(1)]["INFO"] = 1
            else:
                if pattern_user != None:
                    dict_per_user[pattern_user.group(1)]["ERROR"] += 1
                else:
                    dict_per_user[pattern_user.group(1)]["INFO"] += 1

        # Sort the dictionaries
        errors_list = sorted(dict_errors.items(), key=operator.itemgetter(1),
                             reverse=True)
        # Insert the header of the table at the beginning
        errors_list.insert(0, ('Error', 'Count'))
        print("\nERRORS Dictionary::::::::::\n")
        print(errors_list)
        print("\nUsers Dictionary:::::::::::\n")
        per_user_list = sorted(dict_per_user.items(), key=operator.itemgetter(0))
        # Insert the header of the table at the beginning
        per_user_list.insert(0, ('Username', {'INFO', 'ERROR'}))
        print(per_user_list)

        # Write errors to csv file
        with open("error_message_csv", "w") as f:
            writer = csv.writer(f)
            for key, value in errors_list:
                writer.writerow([key, value])
                


def main():
    log_file = sys.argv[1]


if __name__ == "__main__":
    main()
