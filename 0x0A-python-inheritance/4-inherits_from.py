#!/usr/bin/python3
"""Function called inherits_from"""


def inherits_from(obj, a_class):
    """Returns true if obj is an instance of a class, false otherwise

    Args:
        obj : checked object
        a_class: compared class
    Returns:
        boolean: True or False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
