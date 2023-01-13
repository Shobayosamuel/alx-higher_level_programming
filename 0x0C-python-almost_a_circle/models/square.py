#!/usr/bin/python3
from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """method width property getter

        Returns:
            int:_
        """
        return (self.width)

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """Update the Square.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg == None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif not args:
            if kwargs is not None:
                i = 0
                for key, value in kwargs.items():
                    if key == "id":
                        if value is not None:
                            self.__init__(self.size, self.x, self.y)
                        else:
                            self.id = value
                    elif key == "size":
                        self.width = value
                    elif self.height == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value
    def __str__(self):
        """Return the print() and str() representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                       self.x, self.y,
                                                       self.width)
if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()