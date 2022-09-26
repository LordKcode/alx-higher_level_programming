#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""
Rectangle class module.

Define Rectangle class.
"""


class Rectangle(BaseGeometry):
    """Define a Rectangle."""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height)
