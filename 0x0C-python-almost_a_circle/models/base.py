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


if __name__ == "__main__":
    from rectangle import Rectangle

    list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
    ]
    json_list_input = Rectangle.to_json_string(list_input)
    list_output = Rectangle.from_json_string(json_list_input)
    print("[{}] {}".format(type(list_input), list_input))
    print("[{}] {}".format(type(json_list_input), json_list_input))
    print("[{}] {}".format(type(list_output), list_output))