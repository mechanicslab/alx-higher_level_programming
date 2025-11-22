#!/usr/bin/python3
""" A module defining a square class """


class Square:
    """ A square class """

    def __init__(self, size=0):

        """ class constructor method
        Args:
            size: the size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """

        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

    def area(self):
        """ Calculates the squares area """

        return self.__size * self.__size
