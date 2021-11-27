from tkinter import *
from mss import mss

root = Tk()
root.title('take screenshot')
root.iconbitmap('ergo64.ico')
root.geometry('500x200')

def shot():
    with mss() as sct:
        # definition fichier
        filename = sct.shot(mon=-1, output = "output.png")# mon = numero du moniteur(1 ou 2 ou 3), -1: tous les ecrans capturés
        my_label.config(text= "Screenshot has been saved!")

my_button = Button(root, text="Capture Ecran", font=("helvetica",24), command=shot)
my_button.pack(pady=40)

my_label = Label(root, text="")
my_label.pack(pady=10)

root.mainloop()
