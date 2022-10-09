#!/usr/bin/env/ python3
import re
import regex


def log_errors():
    """Set regular expression to find lines containing ERROR"""
    with open("syslog.log") as file:
        error_log = 0
        for line in file:
            info = re.findall(r"")
