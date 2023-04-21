#!/usr/bin/python3
"""importing base class from the base model"""
from models.base import Base


class Rectangle(Base):
    """defines a class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instance of a rectangle

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints the output with # character"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        for j in range(self.__y):
            print("")
        for j in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            print("#" * self.__width, end="")
            print("")
