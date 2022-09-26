#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


"""
Square class module.

Define Square class.
"""


class Square(Rectangle):
    """Define a Square."""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
