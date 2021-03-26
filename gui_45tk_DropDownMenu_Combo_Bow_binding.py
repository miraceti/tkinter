from tkinter import *
from tkinter import ttk

root = Tk()
root.title('ERIC PY')
root.geometry("400x400")

def selected(event):
    # myLabel = Label(root, text=clicked.get()).pack()
    if clicked.get()=='Vendredi':
        myLabel = Label(root, text="oui c'est vendredi !").pack()
    else:
        myLabel = Label(root, text=clicked.get()).pack()

def comboclick(event):
    # myLabel = Label(root, text=myCombo.get()).pack()
    if myCombo.get()=='Vendredi':
        myLabel = Label(root, text="oui c'est vendredi !").pack()
    else:
        myLabel = Label(root, text=myCombo.get()).pack()


options = [
    "Lundi",
    "Mardi",
    "Mercredi",
    "Jeudi",
    "Vendredi",
    "Samedi",
    "Dimanche",
    ]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=selected)
drop.pack(pady=20)

myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
myCombo.pack()

# myButton = Button(root, text="choisir un jour", command=selected).pack()



root.mainloop()