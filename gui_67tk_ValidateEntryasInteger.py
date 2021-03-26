from tkinter import *

root = Tk()
root.title('ERIC PY')
root.geometry("700x500")

def number():
    try:
        # int(my_box.get())
        float(my_box.get())
        reponse.config(text="ceci est un nombre! Bravo")
    except ValueError:
        reponse.config(text="ceci n'est pas un nombre! hoops")

my_label = Label(root, text="Enter a number")
my_label.pack(pady=20)

my_box = Entry(root)
my_box.pack(pady=20)

my_button = Button(root, text="Enter a number", command = number)
my_button.pack(pady=20)

reponse = Label(root,text='')
reponse.pack(pady=20)

root.mainloop()