from tkinter import *

root = Tk()
root.title('ERIC PY PROGRAM')
root.geometry('500x500')

my_label1 = Label(root,
           text = "Stuff\nStuff Stuff\nStuf Stuff Stuff",
           font = ("Helvetica",18),
           bd = 1, relief="sunken")
my_label1.pack(pady=20, ipady=10, ipadx=10)

my_label2 = Label(root,
           text = "Stuff\nStuff Stuff\nStuf Stuff Stuff",
           font = ("Helvetica",18),
           bd = 1, relief="sunken",
           justify = "left")
my_label2.pack(pady=20, ipady=10, ipadx=10)


my_label3 = Label(root,
           text = "Stuff\nStuff Stuff\nStuf Stuff Stuff",
           font = ("Helvetica",18),
           bd = 1, relief="sunken",
           justify ="right")
my_label3.pack(pady=20, ipady=10, ipadx=10)

root.mainloop()