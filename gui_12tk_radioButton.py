from tkinter import *

root = Tk()

# r=IntVar()
# r.set("2")

MODES = [
    ("crepe", "crepes"),
    ("fromage","fromage"),
    ("tarte","tarte"),
    ("eclair","eclair")
]

gateau = StringVar()
gateau.set("eclair")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=gateau,  value=mode).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value).pack()

# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()
myButton = Button(root, text="click", command=lambda: clicked(gateau.get())).pack()

# myLabel = Label(root, text=gateau.get()).pack()

mainloop()