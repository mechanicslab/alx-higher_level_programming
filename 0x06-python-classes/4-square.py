#!/usr/bin/python3
""" A module defining a square class """


class Square:
    """ A square class """

    def __init__(self, size=0):

        """ class constructor method """

        self.__size = size

    @property
    def size(self):
        """ Getter method for size """

        return self.__size

    @size.setter
    def size(self, value):

        """ Setter method for size
        Args:
            value: the size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculates the squares area """

        return self.__size * self.__size
