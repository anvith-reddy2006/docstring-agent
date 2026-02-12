# bad_docstrings.py

def subtract(a, b):
    return a - b


def divide(a, b):
    """does division"""
    return a / b


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        """Return info"""
        return self.name, self.age
