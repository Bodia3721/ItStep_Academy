class UahPackage(object):

    def __init__(self, nominal: int, amount: int):
        self._nominal = nominal
        self._amount = amount

    def __str__(self):
        return f'UahPackage: nominal -> {self._nominal} uah; amount -> {self._amount} items'

    def calc_total_sum(self):
        total_sum = self._nominal * self._amount
        print(f'Total sum: {total_sum} uah')


class EurPackage(UahPackage):

    def __init__(self, nominal: int, amount: int, course: float):
        super().__init__(nominal, amount)
        self._course = course

    def __str__(self):
        return super().__str__() + f'; EUR course->  {self._course}'

    def calc_uah_to_euro(self):
        euh_sum = self._nominal * self._amount
        euro_count = euh_sum / self._course
        print(f'{euh_sum} UAH is {euro_count.__round__(3)} EURO')

if __name__ == '__main__':

    package1 = UahPackage(50, 300)
    print(package1)
    package1.calc_total_sum()

    package2 = EurPackage(50, 300, 32.15)
    print(package2)
    package2.calc_uah_to_euro()
