from lib.parent_classes import *


class Manager(Person):

    def __init__(self, name: str, age: int, email: str, phone: str, address: str, department: str, salary: int):
        super().__init__(name, age, email, phone, address)
        self._department = department
        self._salary = salary

    def __str__(self):
        return super().__str__() + f'; {self._department} department; salary: {self._salary} usdt'
