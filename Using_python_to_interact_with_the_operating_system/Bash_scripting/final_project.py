#!/usr/bin/env/ python3
import re
import sys


def log_errors():
    """Set regular expression to find lines containing ERROR"""
    errors ={}
    with open("/var/log/syslog") as file:
        error_log = 0
        for line in file:
            info = re.findall(r"(?P<logtype>ERROR)", line)
            errors.append(info)
