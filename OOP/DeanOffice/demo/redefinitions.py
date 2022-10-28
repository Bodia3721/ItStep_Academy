class Vector(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self):
        return f'({self._x}:{self._y})'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * n, self.y * n)
        # return self.x * other.x + self.y * other.y

if __name__ == '__main__':

    a = Vector(10, 20)
    b = Vector(40, 50)
    n = 100

    c = a + b
    m = a * b
    k = a - b
    l = a * n
    p = b * n

    print(f'{a} + {b} = {c}')
    print(f'{a} * {b} = {m}')
    print(f'{a} - {b} = {k}')
    print(f'{a} * {n} = {l}')
    print(f'{b} * {n} = {p}')

