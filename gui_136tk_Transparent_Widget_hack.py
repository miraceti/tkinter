from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('ERIC PY PROGRAM')
root.geometry('500x500')

# root.attributes('-alpha', 0.5)

# root.wm_attributes('-transparentcolor', 'red')
root.wm_attributes('-transparentcolor', root["bg"])

my_frame = Frame(root, width=200, height=200, bg="red")
my_frame.pack(pady=20, ipady=20, ipadx=20)

my_label = Label(my_frame, text="Hello World" ,bg='red', fg="white", font=("Helvetica",18))
my_label.pack(pady=20)

root.mainloop()