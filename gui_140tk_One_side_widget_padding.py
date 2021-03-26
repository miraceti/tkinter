from tkinter import *

root=Tk()
root.title('S.P.L.A.S.H!!')
root.geometry('500x500')

root.config(bg="blue")

my_label1 = Label(root, text="Hello World!",
                 bg="white",
                 fg="black",
                 font=("Helvetica",20)
                 )
my_label1.grid(row=0, column=0, pady=50, padx=(50,0))

my_label2 = Label(root, text="Hello World 2!",
                 bg="white",
                 fg="black",
                 font=("Helvetica",20)
                 )
my_label2.grid(row=0, column=1)

mainloop()