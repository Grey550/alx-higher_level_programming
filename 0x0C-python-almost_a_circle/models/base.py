#!/usr/bin/python3
"""Class called base"""


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        """Function definition with one argument called ID"""

        if id is None:
            id = Base.__nb_objects + 1
            Base.__nb_objects += 1

        self.id = id
