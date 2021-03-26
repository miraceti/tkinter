from tkinter import *
from namer1 import nameit

root = Tk()
root.title('ERIC PY PROGRAM')
root.geometry('500x500')

# greet = nameit("Rock")

def submit():
    greet = nameit(my_box.get())
    my_label.config(text=greet)

my_box = Entry(root)
my_box.pack(pady=20)

my_label = Label(root, text="", font = ("Helvetica", 20))
my_label.pack(pady=20)

my_button = Button(root,text = "entrer Nom" , command=submit )
my_button.pack(pady=20)




root.mainloop()