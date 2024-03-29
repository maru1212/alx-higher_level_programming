#!/usr/bin/python3
""" Function to check for an object in the same class. """


def is_same_class(obj, a_class):
    """ A function to check for an object in a class.

    Args:
         obj(any): The object to be checked
         a_class(type): To be matched with the object
    Returns:
         If the obj is instance of a class - True
         otherwise - False.
    """

    if type(obj) == a_class:
        return True
    return False
