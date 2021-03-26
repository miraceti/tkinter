from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('ERIC PY')
root.geometry("500x600")

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
 
def add_image():   
    #add an image
    global my_image
    my_image = PhotoImage(file="images/blue4.png")
    position = my_text.index(INSERT)
    my_text.image_create(position, image=my_image)
    my_label.config(text=position)

my_frame = Frame(root)
my_frame.pack(pady=10)

#create scrollbar
text_scroll = Scrollbar(my_frame) 
text_scroll.pack(side=RIGHT, fill=Y)
    
my_text = Text(my_frame, width=40, height=10,font=("helvetica",20), selectbackground="yellow", selectforeground="black", yscrollcommand=text_scroll.set)
my_text.pack(pady=10)

#configure scrollbar
text_scroll.config(command=my_text.yview)

open_button = Button(root, text="open text file", command=open_text)
open_button.pack(pady=10)

save_button = Button(root, text="save the file", command=save_file)
save_button.pack(pady=10)

image_button = Button(root, text="Add image", command=add_image)
image_button.pack(pady=10)

my_label = Label(root, text="")
my_label.pack(pady=10)

root.mainloop()