#!/usr/bin/python3
""" Defines a function which adds a new attribute if possible. """


def add_attribute(obj, att, value):
    """ Add a new attribute to an object if possble.

    Args:
        obj(any): The object ot add an attribute to.
        att(str): The name of the attribute to add to obj.
        value(any): The value of att.

    Raises:
        TypeError: If the attribute cannot be added.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
