from abc_comp_builder import CompBuilder
from computers_set import *


class OfficeCompBuilder(CompBuilder):

    def connect_processor(self):
        print("Підключаємо процесор Intel Core i3")

    def connect_hard_drive(self):
        print("Підключаємо HDD диск")

    def connect_ram(self):
        print("Підключаємо ОЗП на 8 ГБ")

    def connect_video_card(self):
        print("Підключаємо відеокарту NVIDIA GTX 1060")

    def connect_cooling_system(self):
        print("Підключаємо систему охолодження - радіатор")

    def connect_motherboard(self):
        print("Підключаємо материнську плату GIGABYTE B450M")

    def get_result(self) -> Computer:
        return OfficeComputer('офісні')


class CodingCompBuilder(CompBuilder):

    def connect_processor(self):
        print("Підключаємо процесор Intel Core i5")

    def connect_hard_drive(self):
        print("Підключаємо SSD диск")

    def connect_ram(self):
        print("Підключаємо ОЗП на 16 ГБ")

    def connect_video_card(self):
        print("Підключаємо відеокарту MSI GeForce RTX 3060")

    def connect_cooling_system(self):
        print("Підключаємо систему охолодження - MSI 240R RGB")

    def connect_motherboard(self):
        print("Підключаємо материнську плату GIGABYTE B660 HVD")

    def get_result(self) -> Computer:
        return CodingComputer('для програмування')


class GamingCompBuilder(CompBuilder):

    def connect_processor(self):
        print("Підключаємо процесор Intel Core i9")

    def connect_hard_drive(self):
        print("Підключаємо SSD диск")

    def connect_ram(self):
        print("Підключаємо ОЗП на 32 ГБ")

    def connect_video_card(self):
        print("Підключаємо відеокарту GeForce RTX 3080 Ti")

    def connect_cooling_system(self):
        print("Підключаємо систему охолодження -  ASUS ROG STRIX LC II 360 ARGB")

    def connect_motherboard(self):
        print("Підключаємо материнську плату ASUS PRIME Z690-A SOCKET 1700")

    def get_result(self) -> Computer:
        return GamingComputer('ігрові')