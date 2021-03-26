from tkinter import *

root = Tk()
root.title('ERIC PY')
root.geometry("400x400")

my_listbox = Listbox(root)
my_listbox.pack(pady=15)

#ajout item a la listbox
my_listbox.insert(END, "ceci est un item")
my_listbox.insert(END, "second item")
my_listbox.insert(0, "troisieme item")

#ajout d'une liste d'item
my_list =["un","deux","trois","quatre"]

for item in my_list:
    my_listbox.insert(END, item)

my_listbox.insert(3, "nouveau item")

def delete():
    my_listbox.delete(ANCHOR)
    my_label.config(text='')

def select():
    my_label.config(text=my_listbox.get(ANCHOR))


my_button = Button(root, text="Delete", command=delete)
my_button.pack(pady=10)

my_button2 = Button(root, text="Select", command=select)
my_button2.pack(pady=10)

global my_label
my_label = Label(root, text='')
my_label.pack(pady=10)



root.mainloop()