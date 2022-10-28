from abc import ABC, abstractmethod


class Computer(ABC):

    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def __str__(self):
        return f'{self._name} - {self._price} грн'