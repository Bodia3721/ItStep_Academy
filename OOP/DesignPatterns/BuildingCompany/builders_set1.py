from abc_builder import HouseBuilder
from houses_set1 import *


class WoodHouseBuilder(HouseBuilder):

    def build_foundation(self) -> None:
        print('Будуємо цементний фундамент')

    def build_walls(self) -> None:
        print("Будуємо дерев'яні стіни")

    def build_roof(self) -> None:
        print("Будуємо дерев'яний дах")

    def build_windows(self) -> None:
        print("Вставляємо дерев'яні вікна")

    def build_doors(self) -> None:
        print("Вставляємо дерев'яні двері")

    def get_result(self) -> WoodHouse:
        return WoodHouse('Смерека')


class BrickHouseBuilder(HouseBuilder):

    def build_foundation(self) -> None:
        print('Будуємо залізо-бетонний фундамент')

    def build_walls(self) -> None:
        print("Будуємо цегляні стіни")

    def build_roof(self) -> None:
        print("Будуємо сталевий дах")

    def build_windows(self) -> None:
        print("Вставляємо пластикові вікна")

    def build_doors(self) -> None:
        print("Вставляємо сталеві двері")

    def get_result(self) -> WoodHouse:
        return BrickHouse('Червона цегла')


class ModularHouseBuilder(HouseBuilder):

    def build_foundation(self) -> None:
        print('Будуємо цементний фундамент')

    def build_walls(self) -> None:
        print("Будуємо модульні стіни")

    def build_roof(self) -> None:
        print("Будуємо металевий дах")

    def build_windows(self) -> None:
        print("Вставляємо пластикові вікна")

    def build_doors(self) -> None:
        print("Вставляємо металеві двері")

    def get_result(self) -> WoodHouse:
        return WoodHouse('Екологічний')
