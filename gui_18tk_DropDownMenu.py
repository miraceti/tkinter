from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.geometry("400x400")

def show():
    mylabel = Label(root, text=clicked.get()).pack()


options = [
        "lundi",
        "mardi",
        "mercredi",
        "jeudi",
        "vendredi",
        "samedi"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()


my_btn = Button(root, text="show valeur", command=show).pack()

mainloop()