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

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == []:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance

        Returns:
            class: 
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
        new_instance.update(**dictionary)
        return (new_instance)

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated

        Returns:
            list: List of instantiated classes
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as fil:
                list_dicts = Base.from_json_string(fil.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

if __name__ == "__main__":
    from rectangle import Rectangle
    from square import Square
    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file(list_squares_input)

    list_squares_output = Square.load_from_file()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))
