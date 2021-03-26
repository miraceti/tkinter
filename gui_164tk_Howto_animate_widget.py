from tkinter import *

root=Tk()
root.title('Aniùate Widget')
root.iconbitmap('ergo64.ico')
root.geometry('500x400')

count = 0
size = 26
pos = 100

def contract():
    global count, size, pos
    if count <= 10 and count > 0:
        size -= 2
        my_button.config(font=("helvetica",size))
        my_button.pack_configure(pady = pos)
        count -= 1
        pos -= 20
        root.after(100, contract)

def expand():
    global count, size, pos
    if count < 10:
        size += 2
        my_button.config(font=("helvetica",size))
        my_button.pack_configure(pady = pos)
        count += 1
        pos += 20
        root.after(100, expand)
    elif count == 10:
        contract()

my_button = Button(root, text="Click Me!", command = expand, font=("helvetica",24), fg="red")
my_button.pack(pady=100)

mainloop()