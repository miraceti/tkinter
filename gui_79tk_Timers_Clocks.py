from tkinter import *
import time

root = Tk()
root.title('ERIC PY')
root.geometry("800x600")

def clock():
    heure = time.strftime("%H")
    minute = time.strftime("%M")
    seconde = time.strftime("%S")
    jour = time.strftime("%A")

    my_label.config(text= heure + ":" + minute + ":" + seconde)
    my_label.after(1000, clock)
    
    my_label2.config(text= jour)

def update():
    my_label.config(text="new text")

my_label = Label(root, text="", font=("Helvetica",50), fg="green", bg="black")
my_label.pack(pady=20)

my_label2 = Label(root, text="", font=("Helvetica",20), fg="green", bg="black")
my_label2.pack(pady=20)

# my_label.after(5000, update)
clock()

root.mainloop()