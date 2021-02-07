from tkinter import *

root = Tk()

myLabel1 = Label(root, text="hello world!")
myLabel2 = Label(root, text="My nameis rick")
myLabel3 = Label(root, text="       ")
#myLabel.pack()

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)

root.mainloop()