from dataclasses import dataclass
from enum import Enum

USER_ADULT_AGE = 18


class Status(Enum):
    student = "student"
    worker = "worker"


@dataclass
class User:
    name: str
    age: int
    status: Status
    items: list[str]

    def is_adult(self):
        return self.age >= USER_ADULT_AGE

    # def __init__(self, name, age, status, items):
    #     self.name = name
    #     self.age = age
    #     self.status = status
    #     self.items = items

    # def __eq__(self, other):
    #     return (self.name == other.name and
    #             self.age == other.age and
    #             self.status == other.status and
    #             self.items == other.items)


class Worker(User):

    status = Status.worker

    def __init__(self, name, age, items):
        self.name = name
        self.age = age
        self.items = items


