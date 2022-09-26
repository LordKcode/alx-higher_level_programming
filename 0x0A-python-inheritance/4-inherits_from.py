#!/usr/bin/python3
"""
inherits_from function module.

Define inherits_from function.
"""


def inherits_from(obj, a_class):
    """Return whether obj inherits from a_class.
    obj: an object.
    a_class: a class.
    """
    return(issubclass(type(obj), a_class) and not (type(obj) is a_class))
