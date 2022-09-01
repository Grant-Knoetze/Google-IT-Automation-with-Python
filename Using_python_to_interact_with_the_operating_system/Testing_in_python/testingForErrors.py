#!/usr/bin/env python3

import unittest

from raisingExceptions import validate_user


class testValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("valid_user", 3), True)

    def test_too_short(self):
        self.assertEqual(validate_user("inv", 5), False)

    def test_invalid_characters(self):
        self.assertEqual(validate_user("invalid_user", 1), False)

    def invalid_minlen(self):
        """assertRaises ValueError for an invalid minlen,
        assertRaises function from unittest takes the error
        expected to be raised, function, and parameters."""
        self.assertRaises(ValueError, validate_user, "user", -1)


unittest.main()
