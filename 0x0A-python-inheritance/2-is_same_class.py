#!/usr/bin/python3
"""Function definition called is_same_class"""


def is_same_class(obj, a_class):
    """The function returns True if object is the same as
       what the instance specied and if otherwise returns False
    """
    return type(obj) == a_class
