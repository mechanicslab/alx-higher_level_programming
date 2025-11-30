#!/usr/bin/python3
""" A module defining a square class """


class Square:
    """ A square class """

    def __init__(self, size=0):

        """ class constructor method """

        self.__size = size

    @property
    def size(self):

        """ A property method to retrieve size"""

        return self.__size

    @size.setter
    def size(self, value):

        """ A property setter """

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        """ Calculate the square's area """

        return self.__size * self.__size

    def my_print(self):

        """ A public method to print the squares """

        dummy_size = self.__size
        if self.__size == 0:
            print()
        while dummy_size > 0:
            for index in range(self.__size):
                print("#", end='')
            print()
            dummy_size = dummy_size - 1
