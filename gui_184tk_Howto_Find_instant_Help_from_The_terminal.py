from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

root = Tk()
root.title('TreeBase')
root.iconbitmap('ergo64.ico')
root.geometry('500x500')
root.resizable(True, True)  # largeur , hauteur

# list of widger
# Button, Canvas, Checkbutton, Entry, Frame
# Label, LabelFrame, Listbox, Menu, Menubutton
# Radiobutton, Scale 

my_help = str(help(colorchooser.askcolor))
print(my_help)

# ttk
# Button,  Checkbutton, Entry, Frame
# Label, LabelFrame,   Menubutton, PanedWindow
# Radiobutton, Scale, Scrollbar, Spinbox

#New ttk
# Combobox, Notebook, progressbar, Separator,
# Sizegrip, Treeview



root.mainloop()
