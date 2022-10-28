from abc import ABC, abstractmethod


class Transport(ABC):

    def __init__(self, unit_type: str, unit_model: str, unit_weight: float):
        self._unit_type = unit_type
        self._unit_model = unit_model
        self._unit_weight = unit_weight

    def __str__(self):
        return f'{self._unit_type} - {self._unit_model} / {self._unit_weight}'

    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):

    def __init__(self, unit_type: str, unit_model: str, unit_weight: float, max_height: float):
        super().__init__(unit_type, unit_model, unit_weight)
        self._max_height = max_height

    def __str__(self):
        return super().__str__() + f' / {self._max_height}'

    def deliver(self):
        print('Перевезення по шосейних дорогах ЄС')


class Ship(Transport):

    def __init__(self, unit_type: str, unit_model: str, unit_weight: float, draft: float):
        super().__init__(unit_type, unit_model, unit_weight)
        self._draft = draft

    def __str__(self):
        return super().__str__() + f' / {self._draft}'

    def deliver(self):
        print('Перевезення по Чорному та Середземному морях')


class Airplane(Transport):

    def __init__(self, unit_type: str, unit_model: str, unit_weight: float, flight_range: float):
        super().__init__(unit_type, unit_model, unit_weight)
        self._flight_range = flight_range

    def __str__(self):
        return super().__str__() + f' / {self._flight_range}'

    def deliver(self):
        print('Перевезення по Євразійському континенту')