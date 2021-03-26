from tkinter import *

root = Tk()
root.title('ERIC PY PROGRAM')
root.geometry('500x500')

def new():
    pass

def open():
    pass

def disable_new():
    file_menu.entryconfig("New", state="disabled")
    
def enable_new():
    file_menu.entryconfig("New", state="normal-t")

def delete_new():
    file_menu.delete("New")

#create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# add menu items
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

#add dropdown items
file_menu.add_command(label="New", command=new)
file_menu.add_command(label="Open", command=open)

disable_button = Button(root, text="Disable New", command= disable_new)
disable_button.pack(pady=50)

enable_button = Button(root, text="Enable New", command= enable_new)
enable_button.pack(pady=10) 

delete_new_button = Button(root, text="Delete New", command= delete_new)
delete_new_button.pack(pady=50)

root.mainloop()