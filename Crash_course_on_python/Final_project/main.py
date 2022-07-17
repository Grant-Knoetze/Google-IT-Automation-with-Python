#!/usr/bin/env python3
import datetime


class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

        events = [
            Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
            Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
            Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
            Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
            Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
            Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
        ]


# Define the helper function
def get_event_date(event):
    """This function sorts our list"""
    return event.date


# Define the processing function
def current_users(events):
    """Sort events using the sort method,
    and pass the get_event_date function as
    the key"""
    events.sort(key=get_event_date())
    machines = {}  # Create the dictionary where we will store the names and users of a machine
    for event in events:
        """Check if the machine is in the dictionary,
        if not, add it as an empty set in the value"""
        if event.machine not in machines:
            machines[event.machine] = set()
            """For login events we want to add users to the list, 
            for logout events we want to remove users from the list,
            to do this we use the add and remove methods to 
            add and remove from a set"""
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
            """Once we have done iterating through a list, the 
            dictionary will contain all the events we have used as keys."""
    return machines


def generate_report(machines):
    """Use the items method to return both
    the key and value in the dictionary"""
    for machine, users in machines.items():
        """We only want to print logged in users"""
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))


if __name__ == '__main__':
    print("Script executed successfully!")
