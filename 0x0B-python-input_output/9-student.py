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

    def to_json(self):
        """Returns: dictionary rep of the class - Student"""
        return self.__dict__
