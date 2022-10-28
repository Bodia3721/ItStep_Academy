from builders_set1 import *
from director import Director


if __name__ == '__main__':

    wood_team = WoodHouseBuilder()
    brick_team = BrickHouseBuilder()
    modular_team = ModularHouseBuilder()

    chief = Director()

    chief.change_builder(wood_team)
    wood_house = chief.make()
    print(wood_house)
    print('--------------------------------------------')

    chief.change_builder(brick_team)
    brick_house = chief.make()
    print(brick_house)
    print('--------------------------------------------')

    chief.change_builder(modular_team)
    modular_house = chief.make()
    print(modular_house)
    print('--------------------------------------------')


