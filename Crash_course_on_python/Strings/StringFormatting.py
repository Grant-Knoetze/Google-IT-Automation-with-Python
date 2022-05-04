def is_palindrome(input_string):
    """ We'll create two strings,
	to compare them
	raverse through each
	letter of the input string"""
    new_string = ""
    reverse_string = ""

    for letter in input_string.strip():
        """Add any non-blank letters to the
        end of one string, and to the front
        of the other string."""
        if letter != ' ':
            new_string = new_string + letter
            reverse_string = letter + reverse_string

    if new_string.lower() == reverse_string.lower():  # Compare the strings...

        return True
    return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True
