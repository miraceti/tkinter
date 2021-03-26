from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title('ERIC PY')
root.geometry("400x400")

def color():
    # my_color = colorchooser.askcolor()[0][2]
    my_color = colorchooser.askcolor()[1]
    my_label = Label(root, text=my_color).pack(pady=10)
    my_label2 = Label(root, text="tu as choisi une couleur !", font=("Helvetica",31), bg=my_color).pack()


my_button = Button(root, text="pick a color", command = color).pack()




root.mainloop()