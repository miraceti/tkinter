from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('ERIC PY PROGRAM')
root.geometry('500x500')

def hello():
    my_label.config(text="Hello the World")

def goodbye():
    my_label.config(text="Goodbye the World")

def my_popup(e):
    my_menu.tk_popup(e.x_root, e.y_root)

my_menu = Menu(root, tearoff=False)
my_menu.add_command(label="Say Hello", command = hello)
my_menu.add_command(label="Say goodbye", command = goodbye)
my_menu.add_separator()
my_menu.add_command(label="Exit", command = root.quit)

root.bind("<Button-3>", my_popup)

my_label = Label(root, text="", font=("Helvetica",18))
my_label.pack(pady=20)


root.mainloop()