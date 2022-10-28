from abc_computer import Computer


class OfficeComputer(Computer):

    def __init__(self, components):
        super().__init__("Комп'ютер для офісу", 20000)
        self._components = components

    def __str__(self):
        return super().__str__() + f'; компоненти: {self._components}'


class CodingComputer(Computer):

    def __init__(self, components):
        super().__init__("Комп'ютер для програмування", 50000)
        self._components = components

    def __str__(self):
        return super().__str__() + f'; компоненти: {self._components}'


class GamingComputer(Computer):

    def __init__(self, components):
        super().__init__("Комп'ютер для програмування", 110000)
        self._components = components

    def __str__(self):
        return super().__str__() + f'; компоненти: {self._components}'