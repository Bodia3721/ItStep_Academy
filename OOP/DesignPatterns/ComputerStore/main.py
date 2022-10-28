from comp_builders_set import *
from manager import Manager

if __name__ == '__main__':

    office_team = OfficeCompBuilder()
    coding_team = CodingCompBuilder()
    gaming_team = GamingCompBuilder()

    manager = Manager()

    manager.change_builder(office_team)
    office_comp = manager.make()
    print(office_comp)
    print('--------------------------------------------')

    manager.change_builder(coding_team)
    coding_comp = manager.make()
    print(coding_comp)
    print('--------------------------------------------')
    
    manager.change_builder(gaming_team)
    gaming_comp = manager.make()
    print(gaming_comp)
    print('--------------------------------------------')


