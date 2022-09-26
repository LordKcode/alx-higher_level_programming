#!/usr/bin/python3
"""
is_same_class function module.

Define is_same_class function.
"""


def is_same_class(obj, a_class):
    """Return whether obj is an instance of a_class.
    obj: an object.
    a_class: a class.
    """
    return(type(obj) is a_class)
