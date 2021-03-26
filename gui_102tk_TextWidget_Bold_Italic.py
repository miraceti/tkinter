from tkinter import *
from tkinter import filedialog
from tkinter import font

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

def select():
    selected = my_text.selection_get()
    my_label.config(text=selected)
    
def bolder():
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")
    
    my_text.tag_configure("bold", font=bold_font)
    
    current_tags = my_text.tag_names("sel.first")
    
    if "bold" in current_tags:
        # remove bold
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        # add bold
        my_text.tag_add("bold", "sel.first", "sel.last")
    
    
def italicser():
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")
    
    my_text.tag_configure("italic", font=italics_font)
    
    current_tags = my_text.tag_names("sel.first")
    
    if "italic" in current_tags:
        # remove italic
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        # add italic
        my_text.tag_add("italic", "sel.first", "sel.last")
    

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
open_button.pack(pady=5)

save_button = Button(root, text="save the file", command=save_file)
save_button.pack(pady=5)

image_button = Button(root, text="Add image", command=add_image)
image_button.pack(pady=5)

select_button = Button(root, text="Select Text", command=select)
select_button.pack(pady=5)

bold_button = Button(root, text="BOLD", command=bolder)
bold_button.pack(pady=5)

italics_button = Button(root, text="ITALICS", command=italicser)
italics_button.pack(pady=5)

my_label = Label(root, text="")
my_label.pack(pady=5)

root.mainloop()