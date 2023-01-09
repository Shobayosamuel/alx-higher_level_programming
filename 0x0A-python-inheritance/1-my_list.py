#!/usr/bin/python3
"""Define a class MyList"""


class MyList(list):
    """MyList inherits from list"""
    def __init__(self):
        """initialize the class and make a super class"""
        super().__init__()

    def print_sorted(self):
        """Return a sorted List"""
        print(sorted(self))
