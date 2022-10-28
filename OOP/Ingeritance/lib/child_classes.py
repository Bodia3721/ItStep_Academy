from lib.parent_classes import *


class Student(Person):

    def __init__(self, name: str, age: int, email: str, phone: str, address: str, rate: float, group: str):
        super().__init__(name, age, email, phone, address)
        self._rate = rate
        self._group = group

    def __str__(self):
        return super().__str__() + f'; rate: {self._rate}; group: {self._group}'

