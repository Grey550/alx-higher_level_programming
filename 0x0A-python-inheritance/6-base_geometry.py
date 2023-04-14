#!/usr/bin/python3
"""Class named BaseGeometry"""


class BaseGeometry:
    """An Area function that raises an exception if the area is not
    implemented.
    """

    def area(self):
        raise Exception("area() is not implemented")
