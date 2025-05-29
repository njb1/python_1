from src.strings import is_string_palindrome, make_string_uppercase, welcome_message

import pytest

@pytest.mark.parametrize("input_string, expected_output", [
    ("madam", True),
    ("hello", False),
    ("racecar", True),
    ("python", False),
    ("", True),  # Empty string is considered a palindrome
])
def test_is_string_palindrome(input_string, expected_output):
    input_string, expected_output = input_string, expected_output
    result = is_string_palindrome(input_string)
    print(f"Testing if '{input_string}' is a palindrome: {result}")
    assert result == expected_output


def test_make_string_uppercase():
    input_string = welcome_message
    expected_output = "WELCOME TO THE CROWDSTRIKE PYTHON DEMO!"
    result = make_string_uppercase(input_string)
    print(f"Testing uppercase conversion: {result}")
    assert result == expected_output
