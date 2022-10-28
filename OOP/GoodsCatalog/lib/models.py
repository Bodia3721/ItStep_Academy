class Product(object):

    def __init__(self, name: str, id: int, price: float):
        self._name = name
        self._id = id
        self._price = price

    def __str__(self):
        return f'name: {self._name} , id: {self._id}, price: {self._price} uah'




