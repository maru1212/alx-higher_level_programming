#!/usr/bin/python3
""" A function JSON"""


import json

def to_json_string(my_obj):
    """ A function which converts python obj back to json string
    Args:
        my_obj(str): a python obj to be converted to json
    """
    return json.dumps(my_obj)
