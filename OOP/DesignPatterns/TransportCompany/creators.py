from abc import ABC, abstractmethod
from products import *


class Manager(ABC):

    def __init__(self, point: str, dest: str, term: float, client: str):
        self._point = point
        self._dest = dest
        self._term = term
        self._client = client

    def delivery_order(self):
        print(f'\n>Прийняте замовлення від "{self._client}"'
              f'\n на перевезення з {self._point}'
              f'\n до міста {self._dest}.')
        print(f' Термін - {self._term} днів.')
        print(f' Транспортна одиниця: {self.create_transport()}.')

    @abstractmethod
    def create_transport(self):
        pass


class RoadManager(Manager):

    def __init__(self, point: str, dest: str, term: float, client: str):
        super().__init__(point, dest, term, client)

    def create_transport(self):
        return Truck('Трейлер', 'General Motors', 50, 4.5)


class SeaManager(Manager):

    def __init__(self, point: str, dest: str, term: float, client: str):
        super().__init__(point, dest, term, client)

    def create_transport(self):
        return Ship('Балкер', 'Дніпро', 50000, 6.5)


class AirManager(Manager):

    def __init__(self, point: str, dest: str, term: float, client: str):
        super().__init__(point, dest, term, client)

    def create_transport(self):
        return Airplane('Антонов Ан-225', 'Мрія', 1, 15000)