from tkinter import *
from tkinter import ttk

root = Tk()
root.title('ERIC PY')
root.geometry("500x500")

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=10)

def hide():
    my_notebook.hide(1)

def show():
   my_notebook.add(my_frame2, text="red tab")

def select():
    my_notebook.select(1)


my_frame1 = Frame(my_notebook, width=500, height=500, bg="blue")
my_frame1.pack(fill="both", expand=1)
my_frame2 = Frame(my_notebook, width=500, height=500, bg="red")
my_frame2.pack(fill="both", expand=1)

my_notebook.add(my_frame1, text="blue tab")
my_notebook.add(my_frame2, text="red tab")

#cacher un onglet
my_button = Button(my_frame1, text="hide tab 2 red", command=hide).pack(pady=10)

#montrer in onglet (en le recréant)
my_button2 = Button(my_frame1, text="show tab 2 red", command=show).pack(pady=10)

#aller dans un onglet different
my_button3 = Button(my_frame1, text="aller a l'onglet 2 red", command=select).pack(pady=10)

root.mainloop()