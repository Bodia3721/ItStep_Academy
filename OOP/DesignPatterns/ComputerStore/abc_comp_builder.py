from abc import ABC, abstractmethod
from abc_computer import Computer


class CompBuilder(ABC):

    @abstractmethod
    def connect_processor(self):
        pass

    @abstractmethod
    def connect_hard_drive(self):
        pass

    @abstractmethod
    def connect_ram(self):
        pass

    @abstractmethod
    def connect_video_card(self):
        pass

    @abstractmethod
    def connect_cooling_system(self):
        pass

    @abstractmethod
    def connect_motherboard(self):
        pass

    @abstractmethod
    def get_result(self) -> Computer:
        pass