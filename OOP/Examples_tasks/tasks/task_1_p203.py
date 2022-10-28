
class Car(object):

    def __init__(self, name: str, max_speed: float):
        self._name = name
        self._max_speed = max_speed

    def calc_price(self):
        return self._max_speed * 100

    def upgrade(self):
        self._max_speed += 10

    def get_info(self):
        part1 = f'\n>Назва автомобіля: {self._name}'
        part2 = f'\n Швидкість: {self._max_speed} км/год'
        part3 = f'\n Вартість: ${self.calc_price()}'
        return part1+part2+part3


class VipCar(Car):

    def __init__(self, name: str, max_speed: float):
        super().__init__(name, max_speed)

    def calc_price(self):
        return self._max_speed * 250

    def upgrade(self):
        self._max_speed += 5


if __name__ == '__main__':

    car1 = Car('Nissan', 200)
    vipcar1 = VipCar('Lexus', 260)

    print(car1.get_info())
    print(vipcar1.get_info())

    car1.upgrade()
    vipcar1.upgrade()

    print(car1.get_info())
    print(vipcar1.get_info())


