#!/usr/bin/python3
"""Search for a text and update the text"""


def append_after(filename="", search_string="", new_string=""):
    """ A function which searchew for a word and appends after it.
    Args:
        filename(str): The file to be manipulated.
        search_string(str): The text to be searched for.
        new_string(str): The new text to be appended.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as w:
        w.write(text)
