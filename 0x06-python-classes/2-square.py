class Square:
    """
    A class to represent Square

    Attributes
    ----------
    size : int
    takes the size of the square
    """

    def __init__(self, size=0):
        """
        Constructs attributes for the square object.

        Attributes
        ----------
        size : int
        takes the size of the square
        """

        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
