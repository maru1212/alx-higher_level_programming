#!/usr/bin/python3
""" Author Maranata Feleke. """


def append_write(filename="", text=""):
    """ Is a function which appends a text in an existing text.
    Args:
        filename(str): The name of the file.
        text(str): The text to be appended in the existing file.
    Returns:
        The number of charactors.
    """
    with open(filename, mode="a", encoding="UTF-8") as f:
        return f.write(text)
