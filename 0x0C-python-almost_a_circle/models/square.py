#!/usr/bin/python3
"""importing rectangle from the model"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a square"""
    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)
