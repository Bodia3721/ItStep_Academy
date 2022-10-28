from tkinter import *
from tkinter import messagebox
from lib.models import Fractions


class MainForms(object):

    _widgets = dict()

    @classmethod
    def create_widgets(cls):
        cls._widgets['root'] = Tk()

        cls._widgets['frame1'] = Frame(cls._widgets['root'])
        cls._widgets['frame2'] = Frame(cls._widgets['root'])
        cls._widgets['frame3'] = Frame(cls._widgets['root'])

        cls._widgets['caption1'] = Label(cls._widgets['frame1'])
        cls._widgets['input_op'] = Entry(cls._widgets['frame2'])
        cls._widgets['equal_op'] = Button(cls._widgets['frame2'])

        cls._widgets['input_a'] = Entry(cls._widgets['frame2'])
        cls._widgets['delimiter1'] = Label(cls._widgets['frame2'])
        cls._widgets['input_b'] = Entry(cls._widgets['frame2'])

        cls._widgets['input_c'] = Entry(cls._widgets['frame2'])
        cls._widgets['delimiter2'] = Label(cls._widgets['frame2'])
        cls._widgets['input_d'] = Entry(cls._widgets['frame2'])

        cls._widgets['result_1'] = Entry(cls._widgets['frame2'])
        cls._widgets['result_2'] = Entry(cls._widgets['frame2'])
        cls._widgets['delimiter3'] = Label(cls._widgets['frame2'])
        cls._widgets['result_3'] = Entry(cls._widgets['frame2'])

    @classmethod
    def config_widgets(cls):
        cls._widgets['root'].title('Калькулятор звичайних дробів')
        cls._widgets['root'].geometry('450x300+500+200')
        cls._widgets['root'].resizable(False,False)

        cls._widgets['caption1'].config(text='Калькулятор звичайних дробів', font='Aria 20', fg='black')
        cls._widgets['input_op'].config(font='Aria 18', fg='red', width=3, justify='center')
        cls._widgets['equal_op'].config(font='Aria 14', fg='red', width=3, text='=')

        cls._widgets['input_a'].config(font='Aria 18', fg='blue', width=4, justify='center')
        cls._widgets['delimiter1'].config(font='Aria 18', text='-------', fg='gray')
        cls._widgets['input_b'].config(font='Aria 18', fg='blue', width=4, justify='center')

        cls._widgets['input_c'].config(font='Aria 18', fg='blue', width=4, justify='center')
        cls._widgets['delimiter2'].config(font='Aria 18', text='-------', fg='gray')
        cls._widgets['input_d'].config(font='Aria 18', fg='blue', width=4, justify='center')

        cls._widgets['result_1'].config(font='Aria 18', fg='green', width=3, justify='center')
        cls._widgets['result_2'].config(font='Aria 18', fg='green', width=3, justify='center')
        cls._widgets['delimiter3'].config(font='Aria 18', text='-----', fg='gray')
        cls._widgets['result_3'].config(font='Aria 18', fg='green', width=3, justify='center')

    @classmethod
    def place_widgets(cls):
        cls._widgets['frame1'].pack(pady=10)
        cls._widgets['frame2'].pack(pady=10)
        cls._widgets['frame3'].pack()

        cls._widgets['caption1'].pack()
        cls._widgets['input_op'].grid(row=0, column=1, rowspan=3, padx=10)
        cls._widgets['equal_op'].grid(row=0, column=3, rowspan=3, padx=10)

        cls._widgets['input_a'].grid(row=0, column=0)
        cls._widgets['delimiter1'].grid(row=1, column=0)
        cls._widgets['input_b'].grid(row=2, column=0)

        cls._widgets['input_c'].grid(row=0, column=2)
        cls._widgets['delimiter2'].grid(row=1, column=2)
        cls._widgets['input_d'].grid(row=2, column=2)

        cls._widgets['result_1'].grid(row=0, column=4, rowspan=3, padx=10)
        cls._widgets['result_2'].grid(row=0, column=5)
        cls._widgets['delimiter3'].grid(row=1, column=5)
        cls._widgets['result_3'].grid(row=2, column=5)

    @classmethod
    def equal_click_handler(cls, event):
        print(event)

    @classmethod
    def run(cls):
        cls.create_widgets()
        cls.config_widgets()
        cls.place_widgets()
        cls._widgets['equal_op'].bind('<Button-1>', cls.equal_click_handler)
        cls._widgets['root'].mainloop()