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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes a spring representationof list_objs to a file"""
        filename = f"{cls.__name__}.json"

        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary:
            x = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
            x.update(**dictionary)
            return x

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializing and deserializing in CSV"""
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline="") as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height,
                                     obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """serializing and deserializing in CSV"""
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                fieldnames = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
            list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
            list_dicts = [dict([k, int(v)] for k, v in d.items())
                          for d in list_dicts]
            return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
