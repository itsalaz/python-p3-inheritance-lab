#!/usr/bin/env python

from user import User
import random

class Teacher(User):

    knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def teach(self):
        if not self.knowledge:
            return ValueError("I do not know")
        random_index = random.randint(0, len(self.knowledge)-1)
        return self.knowledge[random_index]
        

        