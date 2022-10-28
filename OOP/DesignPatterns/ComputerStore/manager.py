from abc_computer import Computer
from abc_comp_builder import CompBuilder


class Manager(object):

    def __init__(self):
        self._specialist = None

    def change_builder(self, specialist: CompBuilder):
        self._specialist = specialist

    def make(self) -> Computer:
        self._specialist.connect_processor()
        self._specialist.connect_hard_drive()
        self._specialist.connect_ram()
        self._specialist.connect_video_card()
        self._specialist.connect_cooling_system()
        self._specialist.connect_motherboard()
        return self._specialist.get_result()