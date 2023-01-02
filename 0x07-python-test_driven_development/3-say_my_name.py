#!/usr/bin/python3
"""say_my_name returns a string with the names"""


def say_my_name(first_name, last_name=""):
    """say my name

    Args:
        first_name (str): first name
        last_name (str, optional): lastname. Defaults to "".

    Raises:
        TypeError: must be a string
        TypeError: must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("first_name must be a string")

    print(f"My name is {first_name} {last_name}")
