from abc import ABC, abstractmethod


class Unit(object):

    def __init__(self, name: str, thickness: float, density: float):
        self._name = name
        self._thickness = thickness
        self._density = density

    def __str__(self):
        return f'{self._name}: {self._thickness} мм, {self._density} г/см.куб'

    @abstractmethod
    def calc_square(self):
        pass

    def calc_weight(self):
        return self.calc_square() * self._thickness * self._density


class SquareUnit(Unit):

    def __init__(self, name: str, thickness: float, density: float, width: float):
        super().__init__(name, thickness, density)
        self._width = width

    def calc_square(self):
        return self._width ** 2


class RectUnit(Unit):

    def __init__(self, name: str, thickness: float, density: float, width: float, length: float):
        super().__init__(name, thickness, density)
        self._width = width
        self._length = length

    def calc_square(self):
        return self._width * self._length


class TriUnit(Unit):

    def __init__(self, name: str, thickness: float, density: float, leg1: float, leg2: float):
        super().__init__(name, thickness, density)
        self._leg1 = leg1
        self._leg2 = leg2

    def calc_square(self):
        return self._leg1 * self._leg2 / 2
