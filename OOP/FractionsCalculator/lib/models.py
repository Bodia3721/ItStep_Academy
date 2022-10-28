class Fractions(object):

    def __init__(self, num: int, den: int, whole: int = 0):
        self._num = num
        self._den = den
        self._whole = whole

    @property
    def num(self):
        return self._num

    @property
    def den(self):
        return self._den

    @property
    def whole(self):
        return self._whole

    def __str__(self) -> str:
        if self._whole != 0:
            return f'({self._whole}){self._num}/{self._den}'
        else:
            return f'{self._num}/{self._den}'

    def __add__(self, other):
        whole = self.whole + other.whole
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fractions(num, den, whole)

    def __sub__(self, other):
        whole = self.whole - other.whole
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fractions(num, den, whole)

    def __mul__(self, other):
        whole = self.whole * other.whole
        num = self.num * other.num
        den = self.den * other.den
        return Fractions(num, den, whole)

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        return Fractions(num, den)

    def normalize(self) -> None:
        if self._num == self._den:
            self._whole += 1
            self._num = 0
            self._den = 1
        elif self._num > self._den:
            self._whole = self._num // self._den
            self._num = self._num%self._den
        self.reduce()

    def reduce(self) -> None:
        a = self._num
        b = self._den
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        nsd = a
        if nsd > 1:
            self._num //= nsd
            self._den //= nsd

