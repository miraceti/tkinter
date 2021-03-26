from tkinter import *

root = Tk()
root.title('ERIC PY')
root.geometry("600x400")

def change(e):
    my_pic = PhotoImage(file="images/blue3.png")
    my_label.config(image=my_pic)
    my_label.image=my_pic

def change_back(e):
    my_pic = PhotoImage(file="images/got1b.png")
    my_label.config(image=my_pic)
    my_label.image=my_pic    

def do_something():
    label2 = Label(root, text="you clicked the button")
    label2.pack(pady=20)

my_pic = PhotoImage(file="images/got1b.png")
# my_label  = Label(root, image=my_pic)
my_label  = Button(root, image=my_pic, command=do_something)
my_label.pack(pady=20)

my_label.bind("<Enter>", change)
my_label.bind("<Leave>", change_back)


root.mainloop()