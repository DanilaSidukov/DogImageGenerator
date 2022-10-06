from tkinter import *
import requests
import urllib.parse
from urllib import request
import io
from PIL import ImageTk, Image

def click():
    resp = requests.get("https://dog.ceo/api/breeds/image/random")
    data = resp.json()
    d = data["message"]
    raw_data = urllib.request.urlopen("{}".format(d)).read()
    im = Image.open(io.BytesIO(raw_data))
    image_cat = ImageTk.PhotoImage(im)
    image_out = Label(window, image = image_cat, width= 800, height= 800)
    image_out.grid(column=2, row=3)
    window.mainloop()

window = Tk()
window.geometry("500x400")
window.title("View cats")


lbl_null = Label(window, text="                                   ")
lbl_null.grid(column=0, row=0)

lbl = Label(window, text = "Tap \"View\" to see dog", font=("Comic Sans MS", 20, "bold"))
lbl.grid(column=0, row=1)

btn = Button(window, text="Views", bg="blue", fg="green", font=("Comic Sans MS", 20, "bold"), command = click)
btn.grid(column=2, row=1)



window.mainloop()


