#!/usr/bin/python3
"""Student to JSON"""


class Student:
    def __init__(self, first_name, last_name, age):
        """ Instatiation of arguments.
        Args:
            first_name(str): first name of the student.
            last_name(str): Last name of the student.
            age(int): the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns: dictionary rep of the class - Student
        Args:
            attrs(list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(elements) == str for elements in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ Back to Object.
        Arg:
            json(dict): a dictionary which will be converted to attr
        """
        for k, v in json.items():
            return getattr(self, k, v)
