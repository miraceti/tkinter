from tkinter import *
from PIL import ImageTk, Image
from tkinter  import messagebox

root = Tk()

def open():
    global my_img
    top = Toplevel()
    top.title("seconde fenetre")
    # lblt = Label(top, text="Hello TOP!").pack()
    my_img = ImageTk.PhotoImage(Image.open("images/got1b.png"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close windows", command=top.destroy).pack()


btn = Button(root, text="open seconde fenetre", command=open).pack()

lbl = Label(root, text="Hello ROOT!").pack()

mainloop()