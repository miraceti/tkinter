from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('ERIC PY')
root.geometry("500x500")

#r    : read only
# r+  : read and write (en debut de fichier)
# w   : write only (over-writen)
# w+  : write and read (over writen)
# a   : append only (end of file)
# a+  : append and read (end of file)


def open_text():
    text_file = filedialog.askopenfilename(initialdir="D:/eric/python/gui", title="open text file", filetypes=(("Text Files", "*.txt"),))
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    
    my_text.insert(END, stuff)
    
    text_file.close()
    
def save_file():
    text_file = filedialog.askopenfilename(initialdir="D:/eric/python/gui", title="open text file", filetypes=(("Text Files", "*.txt"),))
    text_file =open(text_file,'w')
    text_file.write(my_text.get(1.0, END))
    
    
my_text = Text(root, width=40, height=10,font=("helvetica",20))
my_text.pack(pady=20)

open_button = Button(root, text="open text file", command=open_text)
open_button.pack(pady=20)

save_button = Button(root, text="save the file", command=save_file)
save_button.pack(pady=20)

root.mainloop()