#!/usr/bin/env python3

import unittest

from emails import find_email

class EmailTest(unittest.TestCase):
    def basic_test(self):
        testcase = [None, "Bree", "Campbell"]
        expected = "bree@abc.edu"
        self.assertEqual(find_email(testcase), expected)

# Test for missing parameters, write a test case to handle missing parameter.
    def test_one_name(self):
        testcase = [None, "Kirk", " "]
        expected = "Missing parameters"
        self.assertEqual(find_email(testcase), expected)

# Test for random email address.
    def random_email(self):
        testcase = [None, "Joe", "Soap"]
        expected = "Email address not found"
        self.assertEqual(find_email(testcase), expected)
        
if __name__ == "__main__":
    unittest.main()