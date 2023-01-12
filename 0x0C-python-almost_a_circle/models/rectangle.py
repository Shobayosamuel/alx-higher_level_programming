#!/usr/bin/python3
"""Define a Rectangle class"""
from base import Base


class Rectangle(Base):
    """A rectangle class that inherits fro base

    Args:
        Base (class): initializes the number of objects
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the values

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): id inherited from Base. Defaults to None.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """method width property getter

        Returns:
            int:_
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """property setter width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set the height for the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Property setter for x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Return the value for """
        return (self.__y)

    @y.setter
    def y(self, value):
        """Return the value of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the value of the area"""
        return (self.__width * self.__height)

    def display(self):
        """Display the the rectangle"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for x in range(self.height):
            [print(" ", end="") for i in range(self.x)]
            for y in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

if __name__ == "__main__":

    r1 = Rectangle(2, 3, 2, 2)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()