#!/usr/bin/python3
"""
is_kind_of_class function module.

Define is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """Return whether obj is an instance of a_class or any of it's parents.
    obj: an object.
    a_class: a class.
    """
    return(isinstance(obj, a_class))
