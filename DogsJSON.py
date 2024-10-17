import requests
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

window = Tk()
window.geometry('500x400')
window.title('Изображения собак')

i_m = Label()
i_m.pack()

btn = Button(text='Получить собачку')
btn.pack()

window.mainloop()
