from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title('ERIC PY')
root.geometry("600x400")

def open_prog():
    my_prog = filedialog.askopenfilename()
    my_label.config(text=my_prog)
    # open the prog même si chemin avec espace
    os.system('"%s"' % my_prog)

def open_notepad():
    notepad = 'C:/Windows/System32/notepad.exe'
    os.system('"%s"' % notepad)


my_button = Button(root, text="open prog", command=open_prog)
my_button.pack(pady=20)

my_button2 = Button(root, text="open notepad", command=open_notepad)
my_button2.pack(pady=20)

my_label = Label(root,text="")
my_label.pack(pady=20)

root.mainloop()