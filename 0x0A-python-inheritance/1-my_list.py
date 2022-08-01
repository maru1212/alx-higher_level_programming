#!/usr/bin/python3
""" Author: Marnata Feleke. """


class MyList(list):
    """ A class which inherits from list. """

    def print_sorted(self):
        print(sorted(self))
