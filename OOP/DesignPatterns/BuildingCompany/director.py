from abc_builder import HouseBuilder
from abc_house import House


class Director(object):

    def __init__(self):
        self._builder = None

    def change_builder(self, builder: HouseBuilder):
        self._builder = builder

    def make(self) -> House:
        self._builder.build_foundation()
        self._builder.build_walls()
        self._builder.build_roof()
        self._builder.build_windows()
        self._builder.build_doors()
        return self._builder.get_result()