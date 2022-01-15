from tkinter import *

root = Tk()
root.title('Bind text')
root.iconbitmap('ergo64.ico')
root.geometry('500x300')

def labeler(e):
    my_label.config(text = my_text.get(1.0, END + "-1c") + e.char)

my_text = Text(root, width=50, height=10, font=("helvetica", 11))
my_text.pack(pady=20)

my_label = Label(root, text="type text au dessus", font=("helvetica",14))
my_label.pack(pady=20)

my_text.bind("<Key>", labeler)
root.mainloop()
