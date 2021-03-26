from tkinter import *
from PIL import ImageTk, Image
from tkinter  import filedialog

root = Tk()

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="d:/eric/python/gui/images", title="selectionner un fichier", filetypes=(("png file","*.png"),("jpg files","*.jpg"),("all files","*.*")))

    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


btn = Button(root, text="open file", command=open).pack()
mainloop()