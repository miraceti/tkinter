from tkinter import *
from tkinter.tix import *

root = Tk()
root.title('ERIC PY PROGRAM')
root.geometry('500x500')


# create tooltip
tip = Balloon(root)
tip.config( bd=10, bg="blue")

# subcategory
tip.label.config(bg="white", fg="red", bd=20)

tip.message.config(bg="red", fg="white")

my_button = Button(root, text="Click here !")
my_button.pack(pady=50)

my_label = Label(root, text="Some text", font=("Helvetica",20))
my_label.pack(pady=20)

# bind tooltip to Button
tip.bind_widget(my_button, balloonmsg="this is my button")
tip.bind_widget(my_label, balloonmsg="this is my label")


root.mainloop()