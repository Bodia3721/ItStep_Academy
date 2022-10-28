from tkinter import *
from time import strftime


class MainWindow(object):

    def __init__(self, name: str):
        self._name = name
        self._root = Tk()
        self._clock = Label(self._root)
        self._config()

    def _config(self):
        self._root.title(self._name)
        self._root.geometry('400x200+500+150')
        self._root.config(bg='black')
        self._clock.config(bg='black', fg='yellow', font='Arial 70', text='00:00:00')

    def _tick(self):
        t = strftime('%H:%M:%S')
        self._clock.config(text=t)
        self._clock.after(1000, self._tick)

    def show(self):
        self._clock.pack()
        self._tick()
        self._root.mainloop()


if __name__ == '__main__':

    win = MainWindow('Простий годинник')
    win.show()
