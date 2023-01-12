#!/usr/bin/python3
"""Define a class base"""


class Base:
    """
    Represent the base class
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """Initialize the id

        Args:
            id (int, optional): id. Defaults to None.
        """
        if id is not None:
           self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
