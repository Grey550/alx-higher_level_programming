#!/usr/bin/python3
"""An inherited class from list called MyList"""


class MyList(list):
    """Function that prints the list in ascending order"""

    def print_sorted(self):
        """Prints a list in an ascending order"""
        print(sorted(self))
