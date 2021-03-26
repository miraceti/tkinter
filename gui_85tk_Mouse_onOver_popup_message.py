from tkinter import *

root = Tk()
root.title('ERIC PY')
root.geometry("500x400")


def button_over(e):
    my_button["bg"] = "white"
    status_label.config(text="moi curseur, je suis au dessus du bouton!!!")

def button_leave(e):
    my_button["bg"] = "SystemButtonFace"
    status_label.config(text="")

my_button = Button(root, text="click Here!", font=("Helvetica", 30))
my_button.pack(pady=60)

status_label = Label(root, text='', bd=1, relief=SUNKEN, anchor=E)
status_label.pack(fill=X, side=BOTTOM, ipady=2)

my_button.bind("<Enter>", button_over)
my_button.bind("<Leave>", button_leave)

root.mainloop()