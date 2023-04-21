#!/usr/bin/python3
"""Class called base"""
import json
import csv
import turtle


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a string representation of list dictionaries"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)
