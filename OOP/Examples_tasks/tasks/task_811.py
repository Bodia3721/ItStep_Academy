class Circle(object):

    def __init__(self, radius: float):
        self.__radius = radius


    def __str__(self):
        return f'Коло радіусом: {self.__radius}'


    def calc_square(self) -> float:
        return 3.14 * self.__radius ** 2


    def calc_length(self) -> float:
        return 2 * 3.14 * self.__radius


if __name__ == '__main__':

    r = 8
    c1 = Circle(r)
    s1 = c1.calc_square()
    l1 = c1.calc_length()
    print(s1)
    print(l1)