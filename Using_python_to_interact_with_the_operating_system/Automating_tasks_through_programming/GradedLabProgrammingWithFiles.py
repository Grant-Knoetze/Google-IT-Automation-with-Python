#!/usr/bin/env python3

# The goal of the script is to read the CSV file and generate a report with the total number of people in each
# department. This function receives a CSV file as a parameter and returns a list of dictionaries from that
# file. For this, we will use the CSV module. The CSV module uses classes to read and write tabular data in CSV
# format. The CSV library allows us to both read from and write to CSV files.
import csv


def read_employees(csv_file_location):
    """Open the CSV file by calling open and then csv.DictReader. DictReader creates an object that operates like a
    regular reader (an object that iterates over lines in the given CSV file), but also maps the information it reads
    into a dictionary where keys are given by the optional fieldnames parameter. If we omit the fieldnames parameter,
    the values in the first row of the CSV file will be used as the keys. So, in this case, the first line of the CSV
    file has the keys and so there's no need to pass fieldnames as a parameter. We also need to pass a dialect as a
    parameter to this function. There isn't a well-defined standard for comma-separated value files, so the parser
    needs to be flexible. Flexibility here means that there are many parameters to control how csv parses or writes
    data. Rather than passing each of these parameters to the reader and writer separately, we group them together
    conveniently into a dialect object. Dialect classes can be registered by name so that callers of the CSV module
    don't need to know the parameter settings in advance. We will now register a dialect empDialect."""
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')
    employee_list = []  # Append the dictionaries to an empty initialised list employee_list as you iterate over
    # the CSV file.
    for data in employee_file:
        employee_list.append(data)
    return employee_list


# Call the function and save it to a variable called employee_list.

employee_list = read_employees(
    "C:\\Users\\grant\\OneDrive\\Documents\\Coursera\\IT_automation_with_python"
    "\\Using_python_to_interact_with_the_operating_system\\Programming_with_files\\Graded_lab\\Employees.csv")
print(employee_list)


def process_data(employee_list):
    """Receives the list of dictionaries "employee_list", as a parameter
    and return a dictionary of department:amount, initialize a new list called department_list, iterate over
    employee_list, and add only the departments into the department_list. The department_list should now have a
    redundant list of all the department names. We now have to remove the redundancy and return a dictionary. We will
    return this dictionary in the format department:amount, where amount is the number of employees in that particular
    department. This uses the set() method, which converts iterable elements to distinct elements. """
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
        department_data = {}
        for department_name in set(department_list):
            department_data[department_name] = department_list.count(department_name)
        return department_data


# Call the function by passing the employee_list from the previous section. Then, save the output in a variable
# called dictionary.
dictionary = process_data(employee_list)
print(dictionary)


def write_report(dictionary, report_file):
    """Writes a dictionary of {department: amount} to a file,
    the report should have the format: <department1>: <amount1> <department2>: <amount2> This function requires a
    dictionary, from the previous section, and report_file, an output file to generate report, to both be passed as
    parameters.Use the open() function to open a file and return a corresponding file object. This function
    requires file path and file mode to be passed as parameters. The file mode is 'r' (reading) by default,
    so you should now explicitly pass 'w+' mode (open for reading and writing, overwriting a file) as a parameter. Once
    the file is open for writing, iterate through the dictionary and use write() on the file to store the data."""
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')
        f.close()


write_report(dictionary, "C:\\Users\\grant\\OneDrive\\Documents\\Coursera\\IT_automation_with_python"
                         "\\Using_python_to_interact_with_the_operating_system\\Programming_with_files\\Graded_lab"
                         "\\report.txt")
