#!/usr/bin/python3
"""Define a class BaseGeometry"""


class BaseGeometry:
    """Represent a base geometry"""
    def area(self):
        """A public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate Name and Value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
