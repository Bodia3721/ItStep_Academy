from tkinter import *


class MainWindow(object):

    def __init__(self, name: str):
        self._name = name
        self._root = Tk()
        self.config()

    def config(self):
        self._root.title(self._name)

    def run(self):
        self._root.mainloop()


if __name__ == '__main__':

    win = MainWindow("Головне вікно")
    win.run()
