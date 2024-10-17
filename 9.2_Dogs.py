from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
from PIL import Image, ImageTk
from io import BytesIO

from DogsJSON import progress


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
            img.thumbnail((300, 300))
            img = ImageTk.PhotoImage(img)
            label.config(image=img)
            label.image = img # чтобы картинку сборщик мусора не собрал
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

window.mainloop()
