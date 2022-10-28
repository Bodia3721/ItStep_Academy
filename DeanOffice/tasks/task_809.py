class Circle(object):

    def __init__(self, radius: float):
        self.__radius = radius

    def __str__(self):
        return f'Коло радіусом: {self.__radius}'

    def calc_square(self) -> float:
        return 3.14 * self.__radius ** 2


if __name__ == '__main__':

    r = 3
    c1 = Circle(r)
    s1 = c1.calc_square()
    print(round(s1, 2))
