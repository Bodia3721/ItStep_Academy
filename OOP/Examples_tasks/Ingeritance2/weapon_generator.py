from abc import ABC, abstractmethod


class Weapon(ABC):

    def __init__(self, weapon_name: str, ammo_counts: int, price: float):
        self._weapon_name = weapon_name
        self._ammo_counts = ammo_counts
        self._price = price

    def __str__(self):
        return f'>{self._weapon_name}: {self._ammo_counts} round; price {self._price}$'

    @abstractmethod
    def shoot(self):
        pass


class Gun(Weapon):

    def __init__(self, weapon_name: str, ammo_counts: int, price: float):
        super().__init__(weapon_name, ammo_counts, price)

    def shoot(self):
        print('Pah - Pah - Pah')


class MiniGun(Weapon):

    def __init__(self, weapon_name: str, ammo_counts: int, price: float):
        super().__init__(weapon_name, ammo_counts, price)

    def shoot(self):
        print('BBRRRRRRRRRRRRRRRRR')


class Revolver(Weapon):

    def __init__(self, weapon_name: str, ammo_counts: int, price: float):
        super().__init__(weapon_name, ammo_counts, price)

    def shoot(self):
        print('Raise - BAH! Raise - BAH! Raise - BAH!')


class Kalash(Weapon):

    def __init__(self, weapon_name: str, ammo_counts: int, price: float):
        super().__init__(weapon_name, ammo_counts, price)

    def shoot(self):
        print('Tra-ta-ta-ta-ta-ta-ta!!!')


class Emka(Weapon):

    def __init__(self, weapon_name: str, ammo_counts: int, price: float):
        super().__init__(weapon_name, ammo_counts, price)

    def shoot(self):
        print('Piu-Piu-Piu-Piu-Piu-Piu')


if __name__ == '__main__':

    weapon_1 = Gun('Beretta 92', 16, 700)
    weapon_2 = MiniGun('M134 Minigun', 4000, 3500)
    weapon_3 = Revolver('Colt Cobra', 6, 800)
    weapon_4 = Kalash('AKM', 30, 1700)
    weapon_5 = Emka('M4A1', 30, 1500)

    weapons = [weapon_1, weapon_2, weapon_3, weapon_4, weapon_5]
    for item in weapons:
        print(item)
        item.shoot()

