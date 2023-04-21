#!/usr/bin/python3
"""Importing base class from the base model"""

from models.base import Base


class Rectangle(Base):
    """Defines a class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instance of a rectangle

        Args:
            width: rectangle width
            height: rectangle height
            x: x
            y: y
            id: id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__width

    @height.setter
    def height(self, value):
        """height setter"""
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.__y = value
