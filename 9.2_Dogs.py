from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
from PIL import Image, ImageTk
from io import BytesIO


def get_dog_image():
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        response.raise_for_status()
        data = response.json() # в переменной лежит ответ в формате json
        return data['message']
    except Exception as e:
        mb.showerror('Ошибка', f'Возникла ошибка при запросе к API: {e}')
        return None


def show_image():
    image_url = get_dog_image() # получаем ссылку из интернета
    if image_url:
        try:
            response = requests.get(image_url, stream=True) # в ответ получим что-то из этой ссылки
            response.raise_for_status() # получаем статус ответа для обработки исключений
            img_data = BytesIO(response.content) #в переменную загрузили изображение из этой ссылки в двоичном коде
            img = Image.open(img_data) # обрабатываем картинку с помощью библиотеки Pillow
            img_size = (int(width_spinbox.get()), int(height_spinbox.get()))
            img.thumbnail(img_size)
            img = ImageTk.PhotoImage(img)
            # new_window = Toplevel(window)
            # new_window.title('Случайное изображение')
            tab = ttk.Frame(notebook)
            notebook.add(tab, text=f'Изображение №{notebook.index('end')+1}')
            lb = ttk.Label(tab, image=img)
            lb.pack(padx=10, pady=10)
            lb.image = img # чтобы картинку сборщик мусора не собрал
        except Exception as e:
            mb.showerror('Ошибка', f'Возникла ошибка при загрузке изображения: {e}')
    progress.stop() # останавливаем прогрессбар

def prog():
    progress['value'] = 0
    progress.start(30) # увеличиваться будет 1 раз в 30 мсек
    window.after(3000, show_image) # ждем 3 сек и запускаем функцию show_image()

window = Tk()
window.title('Картинки с собачками')
window.geometry('360x420')

label = ttk.Label()
label.pack(pady=10)

button = ttk.Button(text='Загрузить изображение', command=prog)
button.pack(pady=10)

progress = ttk.Progressbar(mode="determinate", length=300)
progress.pack(pady=10)

width_label = ttk.Label(text='Ширина:')
width_label.pack(side='left', padx=(10, 0)) # прижать к левой стороне и отступить слева 10 пикселей, справа 0
width_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
width_spinbox.pack(side='left', padx=(0, 10))

height_label = ttk.Label(text='Высота:')
height_label.pack(side='left', padx=(10, 0)) # прижать к левой стороне и отступить слева 10 пикселей, справа 0
height_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
height_spinbox.pack(side='left', padx=(0, 10))

top_level_window = Toplevel(window)
top_level_window.title('Изображения собачек')

notebook = ttk.Notebook(top_level_window)
notebook.pack(expand=True, fill='both', padx=10, pady=10)

window.mainloop()
