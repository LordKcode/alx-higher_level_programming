#!/usr/bin/python3
"""
BaseGeometry class module.

Define BaseGeometry class.
"""


class BaseGeometry:
    """Define a BaseGeometry."""

    def area(self):
        """Raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value is an integer greater than zero.
        name (str): a string.
        value (int): an integer greater than zero.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
