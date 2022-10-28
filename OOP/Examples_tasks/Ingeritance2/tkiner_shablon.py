from cgitb import handler
from tkinter import *


class MyWindow(object):
    _widgets = []

    @classmethod
    def create_components(cls):
        cls._widgets['root'] = Tk()
        cls._widgets['my_button'] = Button(cls._widgets['root'])

    @classmethod
    def config_components(cls):
        cls.widgets['my_button'].config(text='Click me')

    @classmethod
    def place_components(cls):
        cls.widgets['my_button'].pack(padx=15, pady=15)

    @classmethod
    def handler(cls, event):
        print(event)
        # ...
        
    @classmethod
    def bind_components(cls):
        cls.widgets['my_button'].bind('<Button-1>', handler)

    @classmethod
    def run_program(cls):
        cls.create_components()
        cls.config_components()
        cls.place_components()
        cls.bind_components()
        cls._widgets['root'].mainloop()


if __name__ == '__main__':
    MyWindow.run_program()
