#!/usr/bin/python3
"""Defines a class called BaseGeometry"""


class BaseGeometry:
    """Function called area that raises an exception if the
    Area is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
