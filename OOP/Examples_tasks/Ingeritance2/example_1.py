from abc import ABC, abstractmethod
from math import sqrt


class Shape(ABC):

    def __init__(self, name: str):
        self._name = name

    def __str__(self):
        return f'Фігура - {self._name}'

    @abstractmethod
    def calc_square(self):
        pass


class Circle(Shape):

    def __init__(self, radius: float):
        super().__init__('коло')
        self._radius = radius

    def __str__(self):
        return super().__str__() + f'; радіус: {self._radius}'

    def calc_square(self):
        return 3.14 * self._radius ** 2


class Rectangle(Shape):

    def __init__(self, height: float, length: float):
        super().__init__('прямокутник')
        self._length = length
        self._height = height

    def __str__(self):
        return super().__str__() + f'; висота: {self._height}; довжина: {self._length}'

    def calc_square(self):
        return self._height * self._length


class Triangle(Shape):

    def __init__(self, side_a: float, side_b: float, side_c: float):
        super().__init__('трикутник')
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    def __str__(self):
        return super().__str__() + f'; сторона А: {self._side_a}, сторона В: {self._side_b}, сторона С: {self._side_c}'

    def calc_square(self):
        p = (self._side_a + self._side_b + self._side_c)/2
        return sqrt(p * (p-self._side_a) * (p-self._side_b) * (p-self._side_c))


if __name__ == '__main__':
    fig1 = Circle(23.5)
    print(fig1)
    print(f'Площа кола: {fig1.calc_square()}')

    fig2 = Rectangle(12.3, 18.0)
    print(fig2)
    print(f'Площа прямокутника: {fig2.calc_square()}')

    fig3 = Triangle(4, 8, 10)
    print(fig3)
    print(f'Площа трикутника: {fig3.calc_square().__round__(4)}')

