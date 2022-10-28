from creators import *


class Client(object):

    def __init__(self, main_manager: Manager):
        self._main_manager = main_manager

    def demo(self):
        self._main_manager.delivery_order()