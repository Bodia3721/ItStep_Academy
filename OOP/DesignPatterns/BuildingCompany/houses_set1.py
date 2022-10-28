from abc_house import House


class WoodHouse(House):

    def __init__(self, wood_type: str):
        super().__init__("Дерев'яний будинок", 24000)
        self._wood_type = wood_type

    def __str__(self):
        return super().__str__() + f'; матеріал: {self._wood_type}'


class BrickHouse(House):

    def __init__(self, brick_type: str):
        super().__init__("Цегляний будинок", 45000)
        self._brick_type = brick_type

    def __str__(self):
        return super().__str__() + f'; матеріал: {self._brick_type}'


class ModularHouse(House):

    def __init__(self, modular_type: str):
        super().__init__("Модульний будинок", 36000)
        self._modular_type = modular_type

    def __str__(self):
        return super().__str__() + f'; матеріал: {self._modular_type}'