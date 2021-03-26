from tkinter import *

root = Tk()
root.title('ERIC PY')
root.geometry("500x400")

def grab():
    my_label.config(text=my_spin.get())


names = ("j","T","M","N")
# my_spin = Spinbox(root, from_=0, to=10, increment=2, font=("helvetica",20))
# my_spin = Spinbox(root, values=("j","T","M","N") ,font=("helvetica",20))
my_spin = Spinbox(root, values=names ,font=("helvetica",20))
my_spin.pack(pady=20)

my_button = Button(root, text="submit", command=grab)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()