
class Shop(object):

    def __init__(self, shop_name, store_type, numbers_of_units=0):
        self._shop_name = shop_name
        self._store_type = store_type
        self._numbers_of_units = numbers_of_units

    def __str__(self):
        return f'{self.shop_name} - {self.store_type}: {self.numbers_of_units} units'

    @property
    def shop_name(self):
        return self._shop_name

    @property
    def store_type(self):
        return self._store_type

    @property
    def numbers_of_units(self):
        return self._numbers_of_units

    @numbers_of_units.setter
    def numbers_of_units(self, new_value):
        self._numbers_of_units = new_value

    #аналог сеттера
    def set_numbers_of_units(self, new_value):
        self._numbers_of_units = new_value

    def describe_shop(self):
        print(f'\n>Shop name: {self._shop_name}')
        print(f'Store type: {self._store_type}')

    def open_shop(self):
        print(f'The store "{self._shop_name}" has opened!')


class Discount(Shop):

    def __init__(self, shop_name, store_type, discount_products: list, numbers_of_units = 0):
        super().__init__(shop_name, store_type, numbers_of_units)
        self._discount_products = discount_products

    def get_discount_products(self):
        print(f'\n>Products with discount:')
        print('-------------------------')
        k = 0
        for product in self._discount_products:
            k += 1
            print(f' {k}. {product}')