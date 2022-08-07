#!/usr/bin/python3
"""Save obj to a file"""
import json


def save_to_json_file(my_obj, filename):
    """ A function wich writes json file in to a file
    Args:
        my_obj: an object to be wreted to the file
        filename: The new file which includes the object in json form
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        return f.write(json.dumps(my_obj))
