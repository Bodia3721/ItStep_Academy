from client import Client
from creators import *

if __name__ == '__main__':

    client_1 = Client(RoadManager('Київ', 'Львів', 2, 'Промінвест'))
    client_2 = Client(SeaManager('Одеса', 'Ізмаїл', 3, 'ІнвестАгро'))
    client_3 = Client(AirManager('Київ', 'Лісабон', 1, 'КосмоТех'))

    clients = [client_1, client_2, client_3]
    for i in clients:
        i.demo()