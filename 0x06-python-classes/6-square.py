#!/usr/bin/python3
""" Square module """


class Square:
    """ Defines a square class """

    def __init__(self, size=0, position=(0, 0)):
        """ class constructor
        Args:
            size: length of the square
            position: squares coordinate
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ property to retrieve square size """
        return self.__size

    @size.setter
    def size(self, value):
        """ property setter to set the square size """
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        self.__size = value

    @property
    def position(self):
        """ property to retrieve square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ property to set square positon """
        if not isinstance(self.__position, tuple) or self.__position[0] < 0
        or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ returns the area of the square """
        return self.__size ** 2

    def my_print(self):
        """ prints the square in its position """
        size_dummy = self.__size
        if self.__size == 0:
            print()
        if self.__position[1] > 0:
            print()
        while size_dummy > 0:
            print(f"{' ' * self.__position[0]}{'#' * self.__size}", end='')
            print()
            size_dummy = size_dummy - 1
