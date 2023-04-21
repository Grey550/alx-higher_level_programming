#!/usr/bin/python3
"""importing rectangle from the model"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a square"""

    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updating the square

        Args:
            width: square width
            height: square height
            x: x
            y: y
            id: id of the square
        """
        attr = ['id', 'size', 'x', 'y']
        for i, arg in enumerate(args):
            if attr[i] == 'size':
                setattr(self, 'width', args[i])
                setattr(self, 'height', args[i])
            else:
                setattr(self, attr[i], args[i])

        for key, value in kwargs.items():
            if key == 'size':
                setattr(self, 'width', value)
                setattr(self, 'height', value)
            else:
                setattr(self, key, value)
