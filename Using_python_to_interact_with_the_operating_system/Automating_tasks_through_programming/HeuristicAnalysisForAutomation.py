#!/usr/bin/env python3

# Determine whether automation will benefit:
# [time_to_automate < (time_to_perform * amount_of_times_done)]

def total_manual_time(time_to_perform, amount_of_times_done):
    total_time = time_to_perform * amount_of_times_done
    print(total_time)  # In minutes


total_manual_time(5, 12)  # Call the function with values


def automate_or_not(automation_time, total_time):
    if automation_time < total_time: # In minutes
        print("Automate this task.")
    else:
        print("Do not automate this task.")
        print()


automate_or_not(600, 60)  # Call the function
