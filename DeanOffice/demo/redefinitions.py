class Vector(object):

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self) -> str:
        return f'({self._x}; {self._y})'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y


if __name__ == '__main__':

    a = Vector(10, 20)
    b = Vector(40, 50)
    c = a + b
    m = a * b

    print(a)
    print('+')
    print(b)
    print('=')
    print(c)

    print()

    print(a)
    print('*')
    print(b)
    print('=')
    print(m)
