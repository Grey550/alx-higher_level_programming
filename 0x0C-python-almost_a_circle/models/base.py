#!/usr/bin/python3
"""Class called base"""


class Base:
    """A function definition with an ID as an argument"""

    __nb_objects = 0

    def __init__(self, id=None):
        """New instance of base

        Args:
            id: int value
        """
        if id is None:
            id = Base.__nb_objects + 1
            Base.__nb_objects += 1
        self.id = id
