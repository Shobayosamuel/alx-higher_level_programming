#!/usr/bin/python3
"""Define a class Student"""


class Student:
    """Object student"""
    def __init__(self, first_name, last_name, age):
        """Initialize the public instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary represntation of a simple data structure."""
        return (self.__dict__)
students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

for student in students:
    j_student = student.to_json()
    print(type(j_student))
    print(j_student['first_name'])
    print(type(j_student['first_name']))
    print(j_student['age'])
    print(type(j_student['age']))
