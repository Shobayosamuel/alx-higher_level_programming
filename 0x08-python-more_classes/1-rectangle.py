#!/usr/bin/python3
"""Define a rectangle class"""


class Rectangle:
    """Represent a triangle"""
    def __init__(self, width=0, height=0):
        """Represent the triangle

        Args:
            width (int): Width of the triangle. Default to 0.
            height (int): height of the triangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the triangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the width of the triangle according to the conditions"""
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the triangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the height of the triangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
