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
