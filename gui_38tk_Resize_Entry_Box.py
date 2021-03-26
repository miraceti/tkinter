from tkinter import *

root = Tk()
root.geometry("400x500")

def myclick():
    hello = "hello " + e.get() 
    mylabel = Label(root, text = hello)
    e.delete(0,'end')
    mylabel.pack(pady=10)

e = Entry(root, width=50, font=('Helvetica', 24))
e.pack(padx=10, pady=10)

mybutton = Button(root, text="entrez nom", command=myclick)
mybutton.pack(pady=10)

root.mainloop()