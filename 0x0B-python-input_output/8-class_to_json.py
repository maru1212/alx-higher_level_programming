#!/usr/bin/python3
"""Defines a python class-to-json function."""


def class_to_json(obj):
    """Returns dictionary representation of a class"""
    return obj.__dict__
