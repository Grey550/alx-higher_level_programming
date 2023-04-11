#!/usr/bin/python3
"""Function named is_kind_of class with two arguments"""


def is_kind_of_class(obj, a_class):
    """
       Returns true if obj is an instance of or is an instance
       of a class that inherited from the class or false otherwise
    """
    return isinstance(obj, a_class)
