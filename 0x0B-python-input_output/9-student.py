#!/usr/bin/python3
"""Define a class Student"""


class Student:
    """Object student"""
    def __init__(self, first_name, last_name, age):
        """Initialize the public instances"""
        self.first_name = firstname
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary represntation of a simple data structure."""
        return (self.__dict__)
