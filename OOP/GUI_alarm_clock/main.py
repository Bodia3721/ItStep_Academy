from tkinter import *
from tkinter import messagebox
from time import strftime
from os import system


class MainWindow(object):

    def __init__(self, name: str):
        self._name = name
        self._root = Tk()
        self._clock = Label(self._root)
        self._alarm = Entry(self._root)
        self._frame = Frame(self._root)
        self._button1 = Button(self._frame)
        self._button2 = Button(self._frame)
        self.config()
        self._target = ''

    def config(self):
        self._root.title(self._name)
        self._root.geometry('400x200+500+150')
        self._root.config(bg='black')
        self._clock.config(bg='black', fg='lime', font='Arial 50', text='00:00:00')
        self._alarm.config(fg='red', font='Arial 28', justify='center', width=15)
        self._frame.config(bg='black')
        self._button1.config(width=15, text='Увімкнути', font='Arial 11', fg='green')
        self._button2.config(width=15, text='Вимкнути', font='Arial 11', fg='red')

    def _tick(self):
        t = strftime('%H:%M:%S')
        self._clock.config(text=t)
        if t == self._target:
            system('melody.mp3')
            messagebox.showinfo('УВАГА!', f'Вже {self._target}')
        self._clock.after(1000, self._tick)


    def _button1_click_handle(self, event):
        print('Button1 -', event)
        self._target = self._alarm.get()
        messagebox.showwarning('Попередження', f'Будильник увімкнено на {self._target}')

    def _button2_click_handle(self, event):
        print('Button2 -', event)
        self._alarm.delete(0, END)
        self._target = ''
        messagebox.showinfo('Повідомлення', 'Будильник вимкнено')


    def show(self):
        self._clock.pack()
        self._alarm.pack()
        self._frame.pack(pady=20)
        self._button1.pack(side='left')
        self._button2.pack(padx=10)
        self._button1.bind('<Button-1>', self._button1_click_handle)
        self._button2.bind('<Button-1>', self._button2_click_handle)
        self._tick()
        self._root.mainloop()


if __name__ == '__main__':

    win = MainWindow('Простий годинник')
    win.show()