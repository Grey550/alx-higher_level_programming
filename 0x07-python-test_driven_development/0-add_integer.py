#!/usr/bin/python3
"""Function that add two integers"""


def add_integer(a, b=98):
    """Function that does the addition of two integers or floats

    Args:
        a: int
        b: int

    Returns:
        the addition of two integers or floats
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
