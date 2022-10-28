from lib.parent_classes import *


class Teacher(Person):

    def __init__(self, name: str, age: int, email: str, phone: str, address: str, experience: int, salary: int):
        super().__init__(name, age, email, phone, address)
        self._experience = experience
        self._salary = salary

    def __str__(self):
        return super().__str__() + f'; teaching experience: {self._experience} years; salary: {self._salary} usdt'
