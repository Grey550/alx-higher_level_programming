#!/usr/bin/python3
"""Class named BaseGeometry"""


class BaseGeometry:
    """An Area function that raises an exception if the area is not
    implemented.
    """

    def __init__(self):
        self.BaseGeometry = BaseGeometry

    def area(self):
        raise Exception("area() is not implemented")
