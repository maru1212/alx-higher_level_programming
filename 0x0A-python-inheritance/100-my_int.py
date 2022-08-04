#!/usr/bin/python3
""" A class which inherits from int. """


class MyInt(int):
    """ Is a class which inherits from int. """

    def __eq__(self, value):
        """ Overide == operator with !=. """

        return self.real != value

    def __ne__(self, value):
        """ Overides != operator with ==. """

        return self.real == value
