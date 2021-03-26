from tkinter import *

root = Tk()
root.title('ERIC PY')
root.geometry("700x500")


def thing():
    my_label.config(text="tu as clicker sur le bouton")


login_btn = PhotoImage(file='images/blue4.png')

img_label =  Label(image=login_btn)
# img_label.pack(pady=20)


my_button = Button(root, image=login_btn, command = thing, borderwidth=0)
my_button.pack(pady=20)

my_label =  Label(root,text='' )
my_label.pack(pady=20)


root.mainloop()