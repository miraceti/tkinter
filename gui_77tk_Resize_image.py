from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('ERIC PY')
root.geometry("800x600")

my_pic = Image.open("images/5.png")

resized =my_pic.resize((250,300), Image.ANTIALIAS)

new_pic = ImageTk.PhotoImage(resized)

#origin 758x1011
my_label = Label(root, image=new_pic)
my_label.pack(pady=20)



root.mainloop()