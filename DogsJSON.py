import requests
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO


def get_json_dog():
    answer_api = requests.get('https://dog.ceo/api/breeds/image/random')
    json_dog = answer_api.json()
    return json_dog['message']


def image_dog_in_tk():
    url_image = get_json_dog()
    if url_image:
        answer_img = requests.get(url_image)
        image = BytesIO(answer_img.content)
        img = Image.open(image)
        img.thumbnail((500, 350))
        img_tk = ImageTk.PhotoImage(img)
        i_m.config(image=img_tk)
        i_m.image = img_tk
    progress.stop()


def func_progress():
    progress.config(value=0)
    progress.start(22)
    window.after(3000, image_dog_in_tk)


window = Tk()
window.geometry('500x450')
window.title('Изображения собак')

i_m = Label()
i_m.pack(pady=[0,10])

btn = ttk.Button(text='Получить собачку', command=func_progress)
btn.pack()

progress = ttk.Progressbar(mode='determinate', length=400)
progress.pack()

window.mainloop()
