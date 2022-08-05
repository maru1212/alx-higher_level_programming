#!/usr/bin/python3
""" Author Maranata Feleke. """


def read_file(filename=""):
    """ A function which enables users to read a file. """

    with open(filename, encoding="UTF-8") as myfile:
        print(myfile.read(), end="")
