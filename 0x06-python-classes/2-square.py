#!/usr/bin/python3
""" A script for Square class """


class Square:
    """ A Square class """

    def __init__(self, size=0):

        """ the class constructor method """

        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
