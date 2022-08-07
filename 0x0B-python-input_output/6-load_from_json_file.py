#!/usr/bin/python3
"""Creating obj from a JSON file"""
import json


def load_from_json_file(filename):
    """A function wich creats an obj from a JSON file"""
    with open(filename) as f:
        return json.load(f)
