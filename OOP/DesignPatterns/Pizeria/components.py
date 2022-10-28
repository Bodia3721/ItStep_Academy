from abc import ABC, abstractmethod


class Pizza(ABC):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_cost(self):
        pass


class ItalianPizza(Pizza):

    def __init__(self):
        super().__init__('Італійська')

    def get_cost(self):
        return 12


class MexicanPizza(Pizza):

    def __init__(self):
        super().__init__('Мексиканська')

    def get_cost(self):
        return 10


class NewYorkPizza(Pizza):

    def __init__(self):
        super().__init__('Нью-Йоркська')

    def get_cost(self):
        return 14