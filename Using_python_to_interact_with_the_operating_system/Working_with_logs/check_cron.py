#!/usr/bin/env python3

import re
import sys

logfile = sys.argv[1]
usernames = {}

with open(logfile) as f:
    """Gets the user name of any user who scheduled a CRON job,
    then counts the number of times that user has done so."""
    for line in f:
        if "CRON" not in line:
            continue
            pattern = r"USER \((\w+)\)$"
            result = re.search(pattern, line)
            if result is None:
                continue
            name = result[1]
            usernames[name] = usernames.get(name, 0) + 1

print(usernames)
