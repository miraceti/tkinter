from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.geometry("400x400")

var = StringVar()
c=Checkbutton(root, text="click sur cette case", variable=var, onvalue="on", offvalue="off")
c.deselect()
c.pack()

mylabel = Label(root, text=var.get()).pack()

def show(): 
    mylabel = Label(root, text=var.get()).pack()


my_btn = Button(root, text="show valeur", command = show).pack()

mainloop()