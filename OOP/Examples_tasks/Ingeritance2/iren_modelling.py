from lib.models_2 import *
from random import randint

if __name__ == '__main__':

    units = [Unit('default', 1, 1)] * 15
    for i in range(5):
        units[i] = SquareUnit('square', randint(10, 15), 7.8, randint(900, 1200))
    for i in range(5, 12):
        units[i] = RectUnit('rectangle', randint(10, 15), 7.8, randint(900, 1200), randint(1500, 2000))
    for i in range(12, 15):
        units[i] = TriUnit('triangle', randint(10, 15), 7.8, randint(800, 1000), randint(800, 1500))

    total_square = 0
    total_weight = 0
    for unit in units:
        print(unit)
        total_square += unit.calc_square()
        total_weight += unit.calc_weight()

    print(f'Загальна площа: {total_square / 1000000} кв.м')
    print(f'Загальна вага: {total_weight / 1000000} т')