#!/usr/bin/python3
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as fil:
            if list_objs == []:
                fil.write("[]")
            else:
                dicts = [x.to_dictionary() for x in list_objs]
                fil.write(Base.to_json_string(dicts))
if __name__ == "__main__":
    from rectangle import Rectangle
    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([r1, r2])

    with open("Rectangle.json", "r") as file:
        print(file.read())