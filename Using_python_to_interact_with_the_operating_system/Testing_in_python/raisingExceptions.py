#!/usr/bin/env python3

# Add check to check that minlen is at least 1, if not raise an error.

def validate_user(username, minlen):
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    return True





#print(validate_user("Grant", 0))